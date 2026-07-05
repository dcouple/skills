# Ticket: Add per-endpoint delivery rate limiting to the webhook dispatcher

**Labels:** enhancement, webhooks · **Milestone:** Webhooks hardening

## Intent

Some customer endpoints can't absorb bursts — when we fan out many events at once (e.g. a nightly batch that finalizes thousands of invoices), we overwhelm their receiver and *cause* the 5xx storms that then trigger our own retries, amplifying load on both sides. We want to cap the delivery rate **per endpoint** so we deliver at a pace the endpoint can sustain, smoothing bursts into a steady stream. This protects customers, reduces wasteful retries, and is a natural complement to the circuit breaker (Phase 5) — rate limiting prevents the breaker from tripping in the first place.

## Scope

- Enforce a configurable **maximum deliveries per second per endpoint** in the dispatcher/worker path.
- A sensible default limit applied to all endpoints, overridable per endpoint.
- When the limit is reached, deliveries **wait** (stay `pending`/`retrying` and are re-scheduled shortly) rather than being dropped or counted as failures.
- Limiting must be correct across multiple worker instances (it's a distributed rate limit, not per-process).

## Acceptance Criteria

- **WHILE** an endpoint is at its configured rate, additional due deliveries **shall** be deferred (not sent, not failed) and retried on a short delay.
- Sustained delivery rate to a single endpoint **shall not** exceed its configured limit (± a small burst allowance), verified under a multi-worker load test.
- A per-endpoint limit override **shall** take effect without redeploy.
- Deferral due to rate limiting **shall not** count against a delivery's retry/attempt budget or move it toward `dead`.
- Rate-limit deferrals **shall** be observable via a metric (deferred count per endpoint).

## Non-Goals

- Global (cross-endpoint) rate limiting or fairness scheduling between endpoints.
- Customer-facing configuration UI for the limit (internal/config-driven for now).
- Changing the retry backoff schedule.
- Priority tiers between event types.

## Starting Points (non-exhaustive)

- `dispatcher/sweeper.ts` — where due deliveries are selected and enqueued; the natural choke point to consult a limiter before enqueuing.
- `worker/deliver.ts` — the HTTP send path; the fallback enforcement point.
- `config/endpoints.ts` — endpoint config model, where a per-endpoint limit field would live.
- We already run Redis for leases — likely the right substrate for a distributed token-bucket limiter. Confirm before adding a new dependency.

## Open Questions

- Token bucket vs. sliding window — token bucket is probably the right fit (allows small bursts, simple). Confirm during design.
- What default rate is safe without being too conservative? (Starting proposal: 10/s per endpoint — needs validation against real traffic.)
- Should the limit be expressed per-second or per-minute for smoother behavior on low-volume endpoints?

---

## Why this format works

This is a **high-level delegation ticket**, deliberately distinct from a full implementation plan. It says *what & why + where to start* and stops — it does not order tasks or prescribe modules to change, because the point is to hand a capable implementer (or a planning step) enough intent to run.

- **Intent leads with the problem**, not the solution ("endpoints can't absorb bursts → we cause the 5xx storms we then retry"), moving from "I want a thing" to "here is the problem this solves" — the enhancement-ticket best practice.
- **Acceptance Criteria are EARS-style and testable**, so "done" is unambiguous even though the ticket prescribes no code.
- **Non-Goals fence the delegation** — they stop a capable implementer from expanding into global fairness or a config UI.
- **Starting Points are pointers, explicitly non-exhaustive** — they orient without dictating, and even flag a decision to confirm (reuse Redis vs. new dependency) rather than pre-deciding it.
- **Open Questions** hand the recipient the design choices worth surfacing, rather than papering over them. A full implementation plan would *resolve* these; a ticket *names* them.
