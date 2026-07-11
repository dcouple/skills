# Rubric — backend API change

1. **[blocker]** Each `AC#` proven by an integration test or script through
   the real HTTP layer against a real datastore — not mocked handlers.
   Evidence: test report or quoted request/response.
2. **[blocker]** Error paths tested explicitly: at least one non-2xx case
   (invalid input) with the expected status and body shape. Evidence: the
   failing-case output.
3. **[blocker]** AuthZ on new/changed surfaces: an unauthorized caller gets
   the expected rejection. Evidence: the rejected request's output.
4. **[blocker]** Backward compatibility: existing consumers' request/response
   shapes unchanged, or the break is named in the item. Evidence: schema/
   contract check or the diff of the response shape.
5. Idempotent or transactional where the operation implies it (retried
   request doesn't double-apply). Evidence: double-invoke output.
6. New surface appears in logs with enough context to debug (request id,
   caller). Evidence: log excerpt from the exercised call.

Known failure modes: route handler written but not mounted; validation on
the happy path only; N+1 query introduced on a list endpoint; secrets or
PII in the new log lines.
