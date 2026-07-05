# Verification Criteria — shared block

Embedded inside Bug Reports, Feature Tickets, and each Epic phase. This is the
contract `/do`'s **verify** stage proves against, so it must be testable — no
vague "works correctly."

## Acceptance criteria (EARS-style, numbered)
Write each as a trigger → observable response. Number them — plans restate them
verbatim and reviews cite them by ID.
- **AC1** — WHEN `<trigger>` the system shall `<observable response>`.
- **AC2** — WHILE `<state>` the system shall `<response>`.
- **AC3** — IF `<unwanted condition>`, THEN the system shall `<response>`.

**Good:** "WHEN a webhook delivery fails 5 times, the system shall mark the endpoint
`degraded` and expose it at `GET /health`." *(observable, runnable)*
**Bad:** "Webhook retries should work correctly." *(untestable — never write this)*

## Verification map (how `/do` proves it)
Every criterion maps to at least one method. The ✓ column is **state**, ticked by
the verify stage — not a menu of options.

| Criterion | Method | Command / flow | ✓ |
|---|---|---|---|
| AC1 | automated | `npm run test <path>` | [ ] |
| AC2 | computer-use | `<flow to drive in the running app>` | [ ] |
| AC3 | automated | `<script>` | [ ] |

Methods: **automated** (tests/scripts) · **manual / computer-use** (drive the running
app) · evidence is text/log for now (screenshots & video deferred).

**Rule:** the verify stage must not report success until every mapped method passes.
