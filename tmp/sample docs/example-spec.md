# Reliable Webhook Delivery — Spec

**Status:** Accepted · **Owner:** Platform team · **Last updated:** 2026-07-05

## Problem / Context

We emit domain events (e.g. `payment.succeeded`, `invoice.finalized`) that customers consume via webhooks. Today delivery is best-effort and synchronous: the API process POSTs to the customer endpoint inline during request handling. This has three failures:

- **Data loss.** If the customer endpoint is down or slow, the event is dropped — there is no retry and no record of the attempt.
- **Latency coupling.** A slow customer endpoint blocks our request thread, degrading unrelated API traffic.
- **No visibility.** Customers cannot see delivery history, and support cannot answer "did event X get delivered?"

We need durable, asynchronous, retried delivery with visibility, without changing the public event schema.

## Goals

- **At-least-once delivery** of every accepted event, with bounded automatic retries and exponential backoff.
- **Decouple** delivery from the request path — producing an event must not block on the customer endpoint.
- **Observability:** every attempt recorded; customers can view delivery status and redeliver manually.
- **Security:** every request signed so customers can verify authenticity.
- **Graceful failure:** after retries are exhausted, the event lands in a dead-letter state, inspectable and replayable.

## Non-Goals

- **Exactly-once delivery.** We commit to at-least-once; consumers must be idempotent. (Explicitly rejected — exactly-once across an untrusted network is not worth the cost.)
- **Ordered delivery.** We do not guarantee events arrive in emission order in this iteration. Ordering is a plausible future feature, deliberately deferred.
- **Customer-side consumer tooling / SDKs.** Out of scope.
- **Changing the event payload schema.** The wire format of events is frozen.

## Key Architecture Decisions

### D1 — Durable queue + worker pool, not inline delivery
Producing an event writes a `delivery` row (status `pending`) in the same transaction as the business change, then enqueues a job. A separate worker pool performs the HTTP POST. **Rationale:** the transactional write is the durability boundary — if the process dies after commit, the delivery is recovered by a sweeper. Decouples customer latency from our request path. *Alternative rejected:* pushing directly to an external queue (SQS) at event time — introduces a dual-write consistency problem with the business transaction (outbox pattern chosen instead).

### D2 — Transactional outbox as the source of truth
The `delivery` table is an outbox: the business transaction and the delivery record commit atomically. A dispatcher polls/streams `pending` rows into the job queue. **Rationale:** guarantees no event is lost even if the queue enqueue fails, because the row already exists and a sweeper will pick it up. *Alternative rejected:* relying on the queue alone (loses events on enqueue failure).

### D3 — Exponential backoff with jitter, capped attempts
Retry schedule: attempts at ~1m, 5m, 30m, 2h, 6h (5 attempts), each with ±20% jitter. After the last attempt fails, status → `dead`. **Rationale:** balances fast recovery from transient blips against not hammering a down endpoint; jitter avoids thundering-herd on shared customer infra. Exact schedule is a tunable constant, not a contract.

### D4 — HMAC-SHA256 request signing over the raw body + timestamp
Each request carries `X-Signature` (HMAC of `timestamp.body` with the endpoint's secret) and `X-Timestamp`. **Rationale:** lets customers verify authenticity and reject replays; signing the timestamp+body prevents replay and tampering. *Alternative rejected:* mTLS — too high an integration burden for most customers.

### D5 — Idempotency key per delivery
Every request includes `X-Event-Id` (stable across retries). **Rationale:** since we are at-least-once, the consumer needs a stable key to dedupe. This is how we make "at-least-once + idempotent consumer" safe.

### D6 — Endpoint circuit breaker
If an endpoint returns failures beyond a threshold, we open a breaker and pause delivery to that endpoint for a cool-off window, surfacing an alert to the customer. **Rationale:** protects both sides from wasteful retries against a persistently broken endpoint.

## Phases

| Phase | Scope | Status |
|---|---|---|
| 1 | Outbox schema + transactional write + dispatcher + worker skeleton (durable at-least-once, no retry yet) | ☐ Not started |
| 2 | Retry engine: backoff schedule, attempt tracking, dead-letter state | ☐ Not started |
| 3 | Request signing (HMAC) + idempotency headers | ☐ Not started |
| 4 | Delivery-history API + manual redelivery endpoint | ☐ Not started |
| 5 | Circuit breaker + customer alerting | ☐ Not started |

Phases are independently shippable and ordered by dependency: durability first, then reliability, then security, then visibility, then protection.

## Cross-Cutting Concerns

- **Security:** signing secrets stored encrypted at rest; rotation supported (dual-secret window). Never log full request bodies or secrets.
- **Observability:** per-attempt structured logs, metrics for delivery latency / success rate / dead-letter rate, and a dashboard.
- **Migration:** existing inline delivery runs in parallel behind a flag; cut over per-customer, then remove the inline path.
- **Backpressure:** worker concurrency bounded; queue depth alerted.

## Open Questions

- What is the right maximum attempt count and total retention window for `dead` deliveries before purge? (Proposed: 5 attempts, 30-day retention — needs product sign-off.)
- Do we expose retry schedule to customers or keep it internal? (Leaning internal/tunable.)
- Should manual redelivery reset the attempt counter or create a new delivery record? (Leaning: new record linked to the original.)

---

## Why this format works

This spec sits at **Google-design-doc altitude**: it is decision-dense and contains **no code**. Its job is to make the expensive, hard-to-reverse choices explicit and defensible, so that any implementer — human or frontier model — inherits the *what* and the *why* without being told the *how*.

- **Goals / Non-Goals** bound the work. The non-goals (exactly-once, ordering) are *reasoned rejections*, not throwaways — they pre-empt the most likely over-engineering, echoing Google's guidance to guard against solving speculated future problems.
- **Key Architecture Decisions each carry a rationale and a rejected alternative.** This is the load-bearing payload: an implementer can make correct local choices *because* it understands why the outbox, the backoff, and the idempotency key exist. Decisions like D2 (outbox) and D5 (idempotency) are exactly the constraints that are cheap to state and catastrophic to miss.
- **The phases table is the hinge to implementation plans.** Each row spawns one plan and is checked off as it lands — the stateful "stable what" that spec-kit and Kiro separate from the volatile "how."
- **Open Questions** are surfaced rather than hidden, in the spirit of Oxide RFDs: an honest unresolved question is more useful than a false certainty.
