# Rubric — background job / worker change

1. **[blocker]** Idempotency under at-least-once delivery: invoke the job
   twice with the same payload; no duplicated side effects. Evidence:
   double-invoke output + the resulting state.
2. **[blocker]** Failure path: a failing payload retries per policy and lands
   in the DLQ / failure state, not an infinite loop. Evidence: the retry/DLQ
   trace.
3. **[blocker]** Each `AC#` proven by running the job against a real queue or
   invoking its handler with a real payload — not only unit-testing helpers.
4. Structured logs carry job id + attempt count. Evidence: log excerpt.
5. Irreversible side effects (payments, emails) are guarded — outbox pattern,
   dedupe key, or explicit once-only check. Evidence: the guard exercised.

Known failure modes: side effect fires before the transaction commits;
poison message blocks the queue; retry storm on a downstream outage; clock-
dependent behavior that only manifests in production timezones.
