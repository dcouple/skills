# Verification Methods — shared reference

The menu of ways to prove a change works. Used by the `/create-*` skills when
mapping each `AC#` to a method, and by `/do`'s verify stage when proving them.
Per-surface checklists live in `rubrics/` — pick the one matching the change
type and require its evidence.

## The menu

| Method | Proves | Evidence to capture |
|---|---|---|
| Custom lint / static rule (ESLint, Semgrep) | a structural invariant holds — including in future changes | CI pass + the rule source |
| Type check | contracts at call sites (runtime shape still needs a validator at boundaries) | `tsc --noEmit` (or equiv.) output |
| Unit tests | logic paths of one unit; keep them free of I/O and sleeps | test report |
| Integration / API tests | routing, serialization, queries against a real HTTP layer and real DB (Testcontainers-style), not mocked handlers | test report |
| E2E browser (Playwright-style / computer-use) | the whole user journey via real rendering — user-visible behavior, role-based locators | interaction transcript + assertion output (screenshot alone is not proof) |
| Mobile simulator (XCUITest / Espresso / Maestro-style) | native flows, gestures, deep links | test report or driven-flow transcript |
| Visual regression | pixels unchanged vs baseline (behavior not included) | before/after diff pair |
| Accessibility scan (axe-style) | the automatable ~half of a11y issues | violation report, 0 critical |
| Script (backend changes, one-off behavior) | a specific runtime behavior end-to-end | quoted command output + exit code |
| Migration checks | row counts, domain-invariant queries, dry run in a transaction, tested rollback | pre/post counts + invariant query results |
| Performance budget (Lighthouse-CI-style) | metrics within thresholds | report with metric values (average 3 runs) |
| Smoke test | deployed service alive and wired | HTTP codes + latency |

## Minimum proof by change type

| Change type | Minimum | Rubric |
|---|---|---|
| Frontend UI | behavior-level test or natural E2E navigation + a11y scan; visual diff if layout-sensitive | `rubrics/frontend-web.md` |
| Mobile UI | simulator-driven flow of the changed journey | `rubrics/mobile-app.md` |
| Backend API | integration test through the real HTTP layer incl. error-path and authz cases | `rubrics/backend-api.md` |
| Data / schema migration | dry run + row counts + one domain-invariant query + tested rollback | `rubrics/data-migration.md` |
| CLI / script | exit-code contract + idempotency (run twice) + `--dry-run` if state-mutating | `rubrics/cli-script.md` |
| Background job | double-invoke idempotency + retry/DLQ path | `rubrics/background-job.md` |

## Rules

- **Every `AC#` names the check that proves it.** Passing tests that don't
  map to a criterion prove nothing about the criterion; coverage numbers are
  not evidence.
- **Evidence over assertion.** A pass is the command, its quoted output, and
  its exit code — never the implementer's claim. Screenshots supplement;
  they don't prove the interaction path.
- **Prefer the durable guard.** When verification (or a bug) exposes a class
  of violation, encode it as a custom lint/static rule — it re-verifies every
  future change for free. This is the strongest "prevention criteria" for
  Bug Reports.
- **Test behavior, not implementation.** Assertions target public API and
  rendered output; a test that exercises only mocks of code we own verifies
  the mock. Exercise at least one real boundary.
- **A flaky gate is a finding, not a pass.** A check that needed retries to
  go green gets reported, not retried into silence.
