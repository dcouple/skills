# Verification Result — agent output format

> Returned **in-conversation** by the App user (Sonnet, computer-use) during `/do`'s
> verify stage — **not a file**. Proves the work against the item's verification
> criteria; its outcome is summarized into `wrapup.md`.
> **Open with the verdict** — verify does not pass on partial.

---

**Verdict:** `<pass | fail — <the specific blocking criterion>>`

## Criteria checked
| Criterion | Method | Result | Evidence |
|-----------|--------|--------|----------|
| `AC1 — WHEN … the system shall …` | `<flow / script / test>` | Pass / Fail | `<quoted output or log excerpt — required for every row>` |
| `AC2 — WHILE … shall …` | … | Pass / Fail | … |

## What was exercised
`<the flow driven in the running app / the commands run — enough to re-run it>`

## Anomalies  *(omit section if none)*
`<anything off that isn't a criterion failure — slow paths, console errors, odd states>`

---
Verify means *proving it's done*, not *assuming*. A Pass without quoted evidence is
not a Pass. Do not report success until every criterion's mapped method actually
passes; if something can't be exercised, say so — don't guess.
