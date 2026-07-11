# Implementation Plan — format

> Produced by `/do` (plan stage) from the work item. Saved as `./tmp/<id>/plan.md`
> (per issue; one per phase for epics). Reviewed by Plan Reviewer, then updated with
> progress and plan-deltas during implement.
> **Calibrated for a frontier implementer: what to build & why, at file/module**
> **granularity — not line-level code.** No placeholder content: "TBD" or "add
> appropriate error handling" in a plan is a plan failure, not a plan.
> Pre-save check: every `modify` path exists in the repo, every `new` path fits
> the repo's current conventions, no template/placeholder paths, no line number
> that wasn't verified in this checkout. Cheap mechanical catch: grep the plan
> for `<feature>`, `path/to/`, `TBD`, and fact bullets missing `Evidence:`.

---
```yaml
---
type: implementation-plan
item: <id>
lane: <light | full>
phase: <n | —>
confidence: <1-10 — one-pass implementation confidence, scored after review>
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

## Verified repo truths
`<what exists now, so the implementer needs no other doc — facts only, no proposals.`
`Present tense; no "we add", "will", or other future wording here. Every bullet:>`

- **Fact**: `<one present-tense claim about the repo>`
  **Evidence**: `path/to/file.ts:12-34` `<opened this session>`
  **Implication**: `<why it shapes this plan>`

`<Absence claims — "no X exists", "never called" — additionally carry`
`**Search evidence**: the search that came up empty.>`

## Key decisions (restated for this work)
`<the locked calls from the item that shape this work — so nothing load-bearing is lost.>`

## Known mismatches / assumptions
`<where the item's ask conflicts with repo reality — the conflict and how this`
`plan resolves it — plus any assumption the plan stands on. Or "none". A false`
`premise surfaced here is caught at plan review; buried, it ships to the PR.>`

## Reconciliation notes
`<full lane: anchors/gotchas/docs imported from refs/research-dossier.md, conflicts`
`re-checked against the repo and how they resolved, dossier content intentionally`
`dropped as low-value. Light lane: "light lane — no dossier".>`

## Tasks (ordered, file/module granularity)
- [ ] 1. `<task — what & why, where>`
- [ ] 2. `<task>`

## Verification / acceptance
`<restate the item's numbered EARS criteria VERBATIM, plus the exact commands/flows`
`that prove each — the plan is self-sufficient; the implementer never opens the item.>`

## Out of scope
`<carried from the item + anything explicitly deferred>`

## Deprecated / removed
`<code this change makes dead — hunted, not assumed: superseded helpers,`
`orphaned exports, flags nothing reads anymore — or "none">`

## Open questions
`<unresolved review findings carried at the cap, and anything the run must`
`judge as it goes — or omit the section>`

## Plan deltas (filled during implement)
- `<deviation + reason>`   *(or "none")*
