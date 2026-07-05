# Bug: Webhook deliveries stuck in `retrying` forever after a worker crash mid-attempt

**Labels:** bug, webhooks, reliability · **Severity:** High · **Priority:** P1

## Summary

If a delivery worker crashes *after* claiming a `retrying` delivery but *before* recording the attempt result, the delivery is left leased with no `next_retry_at` advance. The sweeper never re-enqueues it, so the event is never delivered and never dead-lettered — it silently hangs indefinitely.

## Expected vs. Actual

- **Expected:** A worker crash mid-attempt should be self-healing. The lease should expire and the sweeper should re-enqueue the delivery on its normal backoff schedule, eventually delivering it or marking it `dead`.
- **Actual:** The delivery stays `status = retrying` with a stale `lease_owner` and a `next_retry_at` in the past. It is neither retried nor dead-lettered. It requires a manual DB update to recover.

## Steps to Reproduce

1. Configure a customer endpoint that returns HTTP 503 (forces the delivery into `retrying`).
2. Emit an event so a `delivery` row is created and picked up: confirm `status = retrying`, `attempt_count = 1`.
3. Wait for the retry to become due and let a worker claim it (`lease_owner` set, `next_retry_at` in the past).
4. Kill the worker process (`SIGKILL`) during the in-flight POST — before it writes the `delivery_attempts` row.
5. Wait past the lease TTL and the next sweeper cycle.
6. Query the delivery: it is still `retrying`, `attempt_count` still `1`, `lease_owner` still set, and no new `delivery_attempts` row exists.

Reproduces ~100% when the kill lands between claim and result write.

## Environment

- Service: `webhook-dispatcher` v2.4.1 (Phase 2 retry engine)
- Runtime: Node 20.11, Postgres 15.4
- Environment: staging and production
- First observed: 2026-07-03 during a rolling deploy that recycled workers

## Evidence

```
2026-07-03T14:22:07Z INFO  worker=w-7 claimed delivery id=dlv_9f3a attempt=2 next_retry_at=2026-07-03T14:22:05Z
2026-07-03T14:22:08Z <no further logs for dlv_9f3a — worker w-7 SIGKILLed during rolling deploy>
-- 40 minutes later --
sweeper query: SELECT ... WHERE status='retrying' AND next_retry_at <= now() AND lease_owner IS NULL
  -> dlv_9f3a NOT selected (lease_owner = 'w-7', never cleared)
```

Count in production: 217 deliveries in this stuck state, oldest 4 days.

## Suspected Area

The sweeper's selection predicate requires `lease_owner IS NULL`, but a crashed worker never releases its lease. There is a lease TTL column but the sweeper does not consider *expired* leases as reclaimable. Likely fix is in the dispatcher/sweeper reclaim query (`dispatcher/sweeper.ts` — the `selectDueRetries` predicate) to also select rows whose lease is past its TTL, and to clear the stale `lease_owner` on reclaim. Overlaps with the "don't double-enqueue" guard from the Phase 2 plan — the reclaim path must be idempotent.

## Severity & Impact

**High.** Silent, permanent event loss for affected deliveries — the worst failure mode for a reliability feature, and it violates the at-least-once goal. Triggered by any worker restart/crash, including routine deploys, so the stuck set grows over time. No customer-facing error surfaces, so it's discovered late. Manual recovery required today.

---

## Why this format works

A good bug report lets an implementer fix the problem *without reconstructing missing context*.

- **Summary + Expected/Actual first** gives the reader the whole shape in three sentences; Actual is stated as **observed behavior**, and the *cause* is confined to "Suspected Area" (an assumption, clearly labeled) — the QA-standard separation of observation from diagnosis.
- **Numbered repro from a known state** with exact statuses and the precise failure window ("between claim and result write") makes it deterministically reproducible — the single most valuable property of a bug report.
- **Environment + Evidence (real logs, real counts)** turn "it's broken" into a scoped, quantified problem (217 rows, 4 days) that also conveys urgency.
- **Severity & Impact** ties the bug back to the spec's at-least-once goal and explains *why it's P1* (silent, growing, deploy-triggered), so triage is objective rather than a guess.
