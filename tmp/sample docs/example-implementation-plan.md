# Reliable Webhook Delivery — Phase 2 Implementation Plan

**Phase:** 2 — Retry engine (backoff, attempt tracking, dead-letter)
**Depends on:** Phase 1 (outbox schema, dispatcher, worker skeleton — merged)
**Spec:** `example-spec.md`

## Context Summary

Phase 1 landed durable at-least-once delivery with **no retry**: a `delivery` row is written transactionally with the business change (status `pending`), a dispatcher moves `pending` rows onto the job queue, and a worker performs a single HTTP POST. On success the row goes `delivered`; on failure it currently goes straight to `failed` and stops. There is no backoff, no attempt history, and no dead-letter state.

This phase makes delivery *reliable*: failed attempts are retried on an exponential-backoff schedule with jitter, each attempt is recorded, and exhaustion lands the delivery in a `dead` state that Phase 4 will expose and replay.

## Key Decisions (restated for this phase)

- **Backoff schedule (D3):** 5 attempts total at approximately 1m, 5m, 30m, 2h, 6h, each with ±20% jitter. Treat the schedule as a tunable constant in one place, not a hardcoded scatter.
- **Retry classification:** retry on network errors, timeouts, and HTTP 5xx / 429. Do **not** retry on 4xx other than 429 (client rejected the payload — retrying won't help); mark those `dead` immediately with a distinct reason.
- **At-least-once is preserved:** a retry re-sends the *same* event with the *same* event id (idempotency headers arrive in Phase 3; leave the header hook point but don't implement signing here).
- **Attempt tracking is append-only:** each attempt is its own record, so history is never overwritten — this is what Phase 4's history API will read.

## Tasks (ordered, file/module granularity)

1. **Schema: attempt history + delivery state.** Add a `delivery_attempts` table (delivery_id, attempt_number, started_at, status, http_status, error_reason, next_retry_at). Extend the `delivery` status enum with `retrying` and `dead`, and add `attempt_count` + `next_retry_at` to the `delivery` row. Migration must be backward-compatible with in-flight Phase 1 rows.

2. **Backoff policy module.** Introduce a single `retry_policy` module that, given an attempt number, returns the next delay (with jitter) or signals "exhausted." Keep the schedule as data (a list of base delays) so it is trivially tunable and unit-testable. No delivery logic here — pure function.

3. **Retry classification.** In the worker's result-handling path, classify the outcome (success / retryable / permanent) based on transport error and HTTP status per the decision above. This replaces the current "any failure → failed" branch.

4. **Worker: record attempt + schedule next.** On each attempt, append a `delivery_attempts` row. On retryable failure, ask `retry_policy` for the next delay, set the delivery to `retrying` with `next_retry_at`, and re-enqueue with a delay (or leave for the sweeper — see task 5). On exhaustion or permanent failure, set `dead` with a reason. On success, `delivered`.

5. **Dispatcher/sweeper: pick up due retries.** Extend the existing dispatcher so it also selects `retrying` rows whose `next_retry_at` is due and re-enqueues them. Ensure a row can't be double-enqueued (claim/lease the row or use a status guard). This reuses the Phase 1 sweeper — do not build a second scheduler.

6. **Metrics + logs.** Emit per-attempt structured logs (delivery id, attempt number, outcome, next_retry_at) and counters for attempts, retries, and dead-letters. No bodies or secrets in logs.

## Verification / Acceptance

- **WHEN** a customer endpoint returns 503 on the first attempt, the delivery **shall** transition to `retrying` with `next_retry_at` ~1m out and a `delivery_attempts` row recorded.
- **WHEN** all 5 attempts fail, the delivery **shall** transition to `dead` and stop being re-enqueued.
- **WHEN** an endpoint returns 400, the delivery **shall** transition to `dead` immediately with a `permanent_client_error` reason and exactly one attempt.
- **WHEN** an attempt succeeds after prior failures, the delivery **shall** transition to `delivered` and no further attempts occur.
- **WHILE** a delivery is `retrying`, the sweeper **shall not** enqueue it more than once per due window (no duplicate in-flight attempts).
- Backoff delays observed in `delivery_attempts` match the schedule within the jitter band.
- Integration test: simulate an endpoint that fails N times then succeeds; assert attempt count and final state for N = 0..5.

## Out of Scope

- Request signing / HMAC and idempotency-key generation (Phase 3 — only leave the header injection point).
- Delivery-history API and manual redelivery (Phase 4).
- Circuit breaker and customer alerting (Phase 5).
- Changing the backoff schedule values based on product input (ship the proposed defaults; tuning is a follow-up).

---

## Why this format works

This plan is calibrated for a **frontier implementer**: it says *what to build and why, in what order* — at **file/module granularity** — and deliberately stops short of line-level code.

- **Context Summary** re-establishes state so the implementer needs no other document to start: what Phase 1 left behind and what this phase must change. This is the recap Kiro's `tasks.md` assumes from `design.md`.
- **Key Decisions are restated, not re-derived.** The spec owns the rationale; the plan pins the few decisions that shape *this* phase (schedule, retry classification, append-only attempts) so nothing load-bearing is lost in the hand-off.
- **Tasks are ordered by dependency and named by module** ("backoff policy module", "dispatcher/sweeper"), not by diff. Each task states intent and the *why* where it's non-obvious (e.g. "reuse the Phase 1 sweeper — do not build a second scheduler"), which steers the implementer away from the likely wrong turn without dictating code.
- **Acceptance criteria are EARS-style** (WHEN/WHILE/…​shall), so the implementer can self-verify and a reviewer has an objective bar.
- **Out of Scope** fences the work — the single most effective guard against a capable model gold-plating into adjacent phases.
