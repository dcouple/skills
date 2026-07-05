# PR Review — #482: Phase 2 retry engine (backoff, attempt tracking, dead-letter)

**Reviewer:** orchestrator · **Base:** `main` · **Files:** 9 changed (+612 / −77)

## Verdict: Request changes — one blocking correctness bug in the reclaim path; solid overall

The phase is well-structured and matches the plan: the backoff policy is isolated and tested, attempt history is append-only, and retry classification is correct. There is **one blocking issue** (a lost-update race that reintroduces the exact double-enqueue the plan warned against) and two important items. Nits are optional. Once the blocking item is fixed I expect to approve on re-review.

## Blocking

- **issue (blocking): `dispatcher/sweeper.ts:73` — lost-update race lets two workers claim the same retry.**
  The reclaim query reads due `retrying` rows and then updates `lease_owner` in a separate statement, with no atomic guard. Two sweeper instances running concurrently will both select `dlv_x`, both set their own `lease_owner`, and both enqueue it → duplicate in-flight attempts. This violates the plan's acceptance criterion "the sweeper shall not enqueue a retrying delivery more than once per due window."
  *Failure scenario:* two dispatcher pods (normal HA config) → the same delivery is POSTed twice within seconds → customer receives duplicate events *and* the second attempt's result overwrites the first's row. Under load this compounds.
  *Fix:* make the claim atomic — `UPDATE ... SET lease_owner = $me WHERE id = $id AND lease_owner IS NULL RETURNING ...` (or `SELECT ... FOR UPDATE SKIP LOCKED`), and only enqueue rows the claim actually returned.

## Important

- **suggestion (important): `worker/deliver.ts:118` — 429 is classified as permanent, but the plan says retry it.**
  The classifier lumps all 4xx into `permanent`. Per the plan's retry-classification decision, `429 Too Many Requests` should be **retryable** (it's transient backpressure, and Phase-later rate limiting depends on this being right). Split 429 out of the permanent branch.
  *Failure scenario:* a customer briefly rate-limits us → we dead-letter deliverable events instead of retrying → silent under-delivery.

- **issue (important): `retry_policy.ts:24` — jitter can produce a negative delay.**
  `base * (1 + rand(-0.2, 0.2))` is fine, but `rand` here returns `[-0.2, 0.25)` due to an off-by-one in the range mapping, so the top of the band is wrong and a boundary case yields a delay below the intended floor. Clamp to a minimum and fix the range. Add a property test asserting `delay ∈ [base*0.8, base*1.2]`.

## Nits

- **nitpick (non-blocking): `migrations/0012_attempts.sql:1`** — `delivery_attempts.error_reason` is untyped `text`; a CHECK constraint or enum matching the classifier's reasons would keep DB and code in sync. Fine to defer.
- **nitpick (non-blocking): `worker/deliver.ts:140`** — log line interpolates `next_retry_at` as a raw Date; use the ISO helper already used elsewhere for consistency.
- **thought (non-blocking):** the backoff schedule constant lives in `retry_policy.ts` as intended — nice. Consider a one-line comment linking it to spec decision D3 so the "tunable, not a contract" intent survives.

## Praise

- **praise: `retry_policy.ts`** — clean separation of the schedule as pure data with a pure `nextDelay(attempt)` function. This is exactly the isolate-and-unit-test shape the plan asked for, and the table-driven tests cover the exhaustion boundary well.
- **praise: `worker/deliver.ts:95`** — append-only `delivery_attempts` writes (never mutating prior attempts) set Phase 4's history API up cleanly. Good forward-thinking.

---

## Why this format works

This review is built to be **acted on in priority order**, and to make the merge/no-merge decision obvious.

- **Verdict first** (Request changes + one-line rationale) tells the author the outcome and *why* before any detail — the AI-review-tool convention of leading with a summary judgment, and consistent with Google's standard of a clear bar for approval.
- **Severity tags separate blocking from nits** using Conventional-Comments grammar (`issue (blocking):`, `suggestion (important):`, `nitpick (non-blocking):`). The author knows precisely what gates merge versus what is optional polish — the whole point of decorations.
- **Every finding carries a `file:line`** and, for correctness bugs, a concrete **failure scenario** ("two pods → duplicate events") that proves the bug is real rather than theoretical. This is what turns a comment into something an implementer can fix without debate.
- **Findings tie back to the plan/spec** (the double-enqueue criterion, the 429 decision, spec D3), so the review enforces the agreed contract rather than the reviewer's taste.
- **Genuine praise is included** and specific — it reinforces the good structural choices (isolated policy, append-only attempts) so they're repeated, per Google's guidance that reviews should also recognize good work.
