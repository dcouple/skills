---
name: do
description: Run the full autonomous pipeline against a work item — plan → plan review → implement → verify → clean up → PR review → open PR + wrap-up. Takes a Bug Report, Feature Ticket, or Epic Spec produced by /create-issue, /create-feature, or /create-epic. Use when a work item is status ready and the branch is set up.
argument-hint: "[path to ./tmp/<id>/item.md]"
disable-model-invocation: true
---

# /do — the autonomous pipeline

## Work item: $ARGUMENTS

You are the **orchestrator** (Fable, this session): you make every judgment
call and dispatch specialized sub-agents for the work. Run fully
autonomously — **no mid-run human checkpoints**. The human returns at the PR.

**Who runs what:** web research and app driving/verification are Claude
sub-agents (`web-researcher`, `app-user`, Sonnet). Codebase research,
implementation, and both kinds of review are **Codex sub-agents**, dispatched
via the `codex` skill (roles `code-researcher`, `implementer`,
`plan-reviewer`, `code-reviewer`). Each review additionally runs the Claude
sub-agent of the same name **in parallel** with the Codex reviewer — two
independent readers, different blind spots. If the `codex` skill returns
`CODEX UNAVAILABLE`/`CODEX ROLE FAILED`, use the same-named Claude sub-agent
alone and note it in the wrap-up. Never route customer-facing copy through
Codex.

## Step 0: Load & preflight

1. Read the item at $ARGUMENTS (default: most recently modified
   `./tmp/*/item.md` with `status: ready`). Its frontmatter `type` selects the
   mode: `feature-ticket` / `bug-report` → single channel; `epic-spec` → Step 7.
2. Refuse politely if `status` is not `ready`, or verification criteria are
   missing — send the user back to the `/create-*` skill that owns the item type.
3. Branch check: `git branch --show-current`. You do NOT create branches — if
   on the default branch, stop and ask the user to set one up. This is the
   only permitted stop.
4. Skim `refs/` filenames now; read individual refs only as the work calls
   for them.

## Step 1: Plan

1. Dispatch 1–3 code-researchers via the `codex` skill (parallel, scoped: one
   per area the item touches) for current-state facts — Claude
   `code-researcher` sub-agents on Codex fallback. Spawn `web-researcher`
   only if an external unknown blocks planning.
2. Write `./tmp/<id>/plan.md` following `references/implementation-plan.md`:
   Files-changed table first, context, key decisions restated, ordered
   file/module tasks, the item's `AC#` criteria restated **verbatim** with
   exact commands, out of scope. No placeholders — "TBD" is a plan failure.

## Step 2: Plan-review loop  (≤3 passes, exit on zero Must Fix from both reviewers)

1. Run **both reviewers in parallel** and wait for both:
   - Codex reviewer: invoke the `codex` skill — role `plan-reviewer`, with
     plan path, item path, pass number `k`, prior findings by ID on pass 2+.
   - Claude reviewer: spawn the `plan-reviewer` sub-agent with the same inputs.
2. The Must-Fix gate is the **union** of both reviewers' Must Fix items,
   deduped by their `D#`/`AC#` citation (same citation + same locus = one
   finding). Consider the reports side-by-side — never merge by re-ranking.
   Fix every Must Fix in the plan; apply Should Fix where cheap. Re-review
   (both reviewers).
3. Cap-out after 3 passes: proceed, and carry the unresolved items into the
   wrap-up's Residual risks.

## Step 3: Implement

Invoke the `codex` skill — role `implementer`, with plan path and item path
(intent = source of truth for *why*). It executes the plan, keeps plan.md
true, and returns a ≤15-line result with Status. Fix rounds (from Steps 4/6)
go back through the `codex` skill as resumes, keeping the session's context.

Fallback: on `CODEX UNAVAILABLE`/`CODEX ROLE FAILED`, spawn the Claude
`implementer` sub-agent with the same inputs.

On `BLOCKED`/`NEEDS_CONTEXT`: resolve from the item/refs yourself and
re-dispatch — do not stop the run unless the blocker genuinely needs the
human (then record it and continue what's still possible).

## Step 4: Verify  (prove it, don't assume it)

1. Run every row of the item's verification map: spawn `app-user` for
   computer-use flows; run test/script methods directly via Bash.
2. Tick the map's ✓ boxes in the item as methods pass.
3. Any Fail → feed the failing criterion + evidence back to `implementer`
   (Step 3) and re-verify. This loop has its own cap: max 3 verify-fix
   round-trips, then proceed with the failure flagged in the wrap-up.

## Step 5: Clean up

Defensive, not comprehensive — one implementer dispatch (the `codex` skill as
a resume of the Step-3 session; Claude `implementer` if on fallback): simplify
what this change added, merge with existing functionality where obvious,
confirm deprecated/dead code from this diff is removed. Nothing beyond this
diff's blast radius. Re-run quality checks.

## Step 6: PR-review loop  (≤3 passes, exit on zero Must Fix from both reviewers)

1. Run **both reviewers in parallel** and wait for both:
   - Codex reviewer: invoke the `codex` skill — role `code-reviewer`, with
     item path, plan path, pass number.
   - Claude reviewer: spawn the `code-reviewer` sub-agent with the same inputs.
   Each reads the diff cold and returns Must/Should/Nice findings with
   `(security)` tags.
2. The Must-Fix gate is the **union** of both reviewers' findings, deduped by
   `D#`/`AC#` citation — the loop proceeds only when *both* report zero Must
   Fix. Every Must Fix → implementer fixes (codex resume, or Claude
   fallback) → re-review with both reviewers (mark prior IDs
   fixed/persists/new). Cap-out after 3: proceed and flag in wrap-up.

## Step 7: Epics  (type: epic-spec)

Run Steps 1–6 **per phase, sequentially** — phase n+1 starts only after phase
n's channel completes. Per-phase plans at `./tmp/<id>/plan-<n>.md`; tick the
phase's ✓ in the spec's table on completion. One PR for the whole epic: open
it after the LAST phase; commit each phase to the branch as it completes
(same `type: summary` message style as Step 8). A phase blocked by an unresolved
`[NEEDS CLARIFICATION]` stops the epic there — wrap up what's done.

## Step 8: PR + wrap-up

All PR prep lives here — there is no separate commit or prepare-pr skill.

1. Update item frontmatter: `status: done`, `pr:` filled.
2. Commit: stage selectively — only files this run touched, never
   `git add -A` — and scan the staged diff for secrets before committing.
   Message style: `type: short imperative summary` (feat / fix / docs /
   chore / refactor / test / perf).
3. Sync the branch: rebase onto the origin default branch; if the rebase
   pulled in changes, re-run the quality checks. Push (`--force-with-lease`
   when rewriting an already-pushed branch).
4. Open the PR (`gh pr create`) — title from the item title in the same
   `type:` style; body sections: **Summary** (the item's intent and what
   "done" means — desired end state for features, expected behavior restored
   for bugs), **Verification** (evidence per AC, one line each), and
   **Manual steps / residual risks** (omit if none).
5. Write `./tmp/<id>/wrapup.md` following `references/wrap-up-report.md`:
   what was built, verification evidence per AC, final review outcome
   ("Must Fix: 0 · passes used k/3" — or cap-out flags), residual risks,
   deltas vs plan. Post it as a PR comment (`gh pr comment`).
6. If a `pr-test-automation` skill is available, run it.
7. Report to the user: PR link + wrap-up summary + anything capped out.

## Rules

- Trust the plan, verify the work: every stage's output is checked by a
  different fresh-context reader than the one that produced it.
- Reviewers/verifiers never edit; the implementer never reviews itself.
- Never expand scope beyond the item; gold-plating is a plan failure.
- If the run dies mid-pipeline, it is resumable: plan.md + the item's ✓ state
  say where you were.

Work item: $ARGUMENTS
