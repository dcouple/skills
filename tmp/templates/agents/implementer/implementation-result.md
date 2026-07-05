# Implementation Result — agent output format

> Returned **in-conversation** by the Implementer during `/do`'s implement stage —
> **not a file**. The Implementer also updates `plan.md` directly: ticks tasks, records
> plan-deltas, keeps the Files-changed table true.
> **Keep the return under ~15 lines** — the detail lives in `plan.md`.

---

**Status:** `<DONE | DONE_WITH_CONCERNS | BLOCKED | NEEDS_CONTEXT>`

`<DONE_WITH_CONCERNS = complete, but something merits Overseer attention — never`
`silently produce work you're unsure about. BLOCKED / NEEDS_CONTEXT: put the`
`specifics under Blockers; the Overseer acts on them directly.>`

## What was built
`<1–3 lines tied to the plan tasks completed>`

## Plan deltas
- `<deviation from plan + reason>`   *(or "none")*

## Quality checks  *(exact command → result; a bare "pass" is uncheckable)*
- tests: `<command>` → `<e.g. 14/14 passing>`
- typecheck: `<command>` → `<result>` · lint: `<command>` → `<result>`

## Blockers / needs Overseer
- `<what stalled or needs a decision>`   *(or "none")*

---
A task isn't done until its runtime/user-facing path is wired end-to-end. Report
last-mile gaps (routes not mounted, controls with no effect) as incomplete, not done.
Files touched live in `plan.md`'s Files-changed table — don't repeat them here.
