# Verification Result — agent output format

> Returned **in-conversation** to the Overseer — **not a file** — by a verifier:
> the Claude `frontend-verifier` (all modes) or the Codex `backend-verifier`
> (verify and QA modes, via tests/scripts instead of the browser).
> Modes, selected by the dispatch prompt: **verify** (from `/do`'s verify stage —
> prove the work meets its numbered criteria; `/do`'s QA pass uses the same format,
> one row per Manual-tests checklist item, Result additionally allowing
> `Left to human — <reason>`) and **reproduce** (from `/discussion` or
> `/create-issue` — make a reported failure happen deterministically; the failure
> occurring IS the successful result).
> Your final message IS the report — no preamble, no process narration.

---

## Output format — verify mode

**Verdict:** <pass | fail — the specific blocking criterion>

## Criteria checked
| Criterion | Method | Result | Evidence |
|-----------|--------|--------|----------|
| AC1 — <criterion> | <flow / script / test> | Pass / Fail | <quoted output or log excerpt — required for every row> |

## What was exercised
<the flow driven / commands run — enough for someone to re-run it>

## Anomalies   (omit section if none)

A Pass without quoted evidence is not a Pass. Do not report success until
every criterion's mapped method actually passes — verify does not pass on
partial.

---

## Output format — reproduce mode

**Verdict:** <reproduced | could not reproduce — what was tried>

## Reproduction steps
<numbered, from a known state — the shortest deterministic path you found>

## Observed behavior
<what happens, stated as observation, with quoted evidence>

## Anomalies   (omit section if none)

If you could not reproduce, list every path you tried and the state you tried
it from — a documented failure to reproduce is a valid, useful result.
