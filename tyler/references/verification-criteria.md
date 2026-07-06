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

## Writing rules (each criterion)

- **Singular** — one observable outcome per criterion; split compound "and"s.
- **Measurable** — a number, state, or specific message; no quality adjectives
  ("fast", "gracefully").
- **No escape clauses** — "where possible", "attempt to", "as appropriate"
  make a criterion unfalsifiable.
- **Positively stated** — "shall not fail" isn't testable; state the
  observable outcome that should happen instead.
- **Deterministic** — a check can return a binary pass/fail.

Gut check: could someone unfamiliar with the project build exactly this and
prove they did?

## Verification map (how `/do` proves it)
Every criterion maps to at least one method. The ✓ column is **state**, ticked by
the verify stage — not a menu of options.

| Criterion | Method | Command / flow | ✓ |
|---|---|---|---|
| AC1 | automated | `npm run test <path>` | [ ] |
| AC2 | computer-use | `<flow to drive in the running app>` | [ ] |
| AC3 | automated | `<script>` | [ ] |

Methods: pick from `~/.references/verification-methods.md` — lint/static
rules, type checks, unit/integration tests, scripts (backend), natural
navigation of the running app (frontend/mobile), migration checks, and more.
The verify stage additionally applies the change type's rubric from
`~/.references/rubrics/`. Evidence is quoted command output / interaction
transcripts (screenshots & video deferred).

**Rule:** the verify stage must not report success until every mapped method passes.
