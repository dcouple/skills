# Codebase Findings — agent output format

> Returned **in-conversation** by the Code Researcher (Sonnet) during the plan stage —
> **not a file**. Precise `file:line` references so the plan can be accurate without the
> Overseer re-reading the codebase.
> **Open with the bottom line** so the Overseer can branch without reading the body.

---

**Bottom line:** `<one line — the answer the plan needs>`

## Relevant files
- `<path:line>` — `<what's here, why it matters to this work>`

## Existing patterns to follow
- `<pattern>` — `<where it's used (path:line)>`

## Boundaries / integration points
- `<system boundary or integration point the work touches>`

## Not found / open questions  *(required — "none" only after actually looking)*
- `<what was searched for and not found, or couldn't be determined>`

## Gotchas  *(omit section if none)*
- `<landmine, inconsistency, or constraint the plan must respect>`

---
Return conclusions and references, not file dumps. Every claim carries a `path:line`.
The Overseer plans against these findings — what you didn't find is as load-bearing
as what you did.
