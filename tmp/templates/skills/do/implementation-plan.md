# Implementation Plan — format

> Produced by `/do` (plan stage) from the work item. Saved as `./tmp/<id>/plan.md`
> (per issue; one per phase for epics). Reviewed by Plan Reviewer, then updated with
> progress and plan-deltas during implement.
> **Calibrated for a frontier implementer: what to build & why, at file/module**
> **granularity — not line-level code.** No placeholder content: "TBD" or "add
> appropriate error handling" in a plan is a plan failure, not a plan.

---
```yaml
---
type: implementation-plan
item: <id>
phase: <n | —>
---
```

# Implementation Plan — `<item / phase>`

## Files changed
`<every file this plan touches — lets a reviewer gauge blast radius at a glance.`
`Keep the "what" to one clause; the tasks below carry the detail.>`

| File | Change | What |
|---|---|---|
| `path/to/file.ts` | modify | `<one clause>` |
| `path/to/new-file.ts` | new | `<one clause>` |
| `path/to/old-file.ts` | delete | `<one clause>` |

## Context summary
`<what exists now; recap the relevant current state so the implementer needs no other doc.`
`Present-tense, evidence-backed — not proposals.>`

## Key decisions (restated for this work)
`<the locked calls from the item that shape this work — so nothing load-bearing is lost.>`

## Tasks (ordered, file/module granularity)
- [ ] 1. `<task — what & why, where>`
- [ ] 2. `<task>`

## Verification / acceptance
`<restate the item's numbered EARS criteria VERBATIM, plus the exact commands/flows`
`that prove each — the plan is self-sufficient; the implementer never opens the item.>`

## Out of scope
`<carried from the item + anything explicitly deferred>`

## Plan deltas (filled during implement)
- `<deviation + reason>`   *(or "none")*
