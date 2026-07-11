# Epic Spec — format

> Produced by `/create-epic`. Saved as `./tmp/<id>/item.md`.
> Same spine as a Feature Ticket at higher altitude, **plus sequential phases**.
> Each phase is a self-contained work item; `/do` runs each phase's channel in order.

---
```yaml
---
type: epic-spec
id: <id>
status: ready         # draft | ready | done
pr: <one PR for the whole epic — phases commit sequentially>
---
```

# Epic: `<title>`

## Problem / context
`<the broader problem this epic addresses>`

## Goals
- `<goal>`

## Non-goals
- `<reasoned exclusion — a real possibility deliberately rejected>`

## Key architecture decisions (cross-cutting)
- **D1** — `<decision>` — `<rationale>` · rejected: `<alternative + why not>`
- **D2** — `<decision>` — `<rationale>` · rejected: `<alternative>`

`<Number every decision; plans and review reports cite them by ID ("violates D2").`
`Directions, not design — no file lists or pseudo-code.>`

## Phases (sequential)
| # | Phase | Desired end state | Depends on | Size | ✓ |
|---|-------|-------------------|-----------|------|---|
| 1 | `<name>` | `<user-side done>` | — | S/M/L | [ ] |
| 2 | `<name>` | … | 1 | M | [ ] |

> `✓` is state — checked when that phase's channel completes.

### Phase 1 — `<name>`
- **Scope:** `<what's in>`
- **Out of scope:** `<what's not>`
- **Key files/modules:** `<starting points, one clause each>`
- **Verification:** `<embed shared/verification-criteria.md for this phase>`

### Phase 2 — `<name>`
`<repeat the block per phase. Each block is self-contained so /do can pick the`
`phase up alone — verification criteria live here, never in the table.>`

## Cross-cutting concerns
`<security · observability · migration — anything true across phases>`

## Justification
- `<claim challenged in the Socratic gate>` — `<the reason that held>`

`<distilled from the socrates Q&A, one line per surviving question: why this`
`epic exists, why these phases, why not the cheaper shape. If the user waived`
`the gate: "Socratic gate waived by user.">`

## Open questions
- `[NEEDS CLARIFICATION]` `<resolve before the affected phase is picked up>`

## References (optional, in refs/)
- `refs/discussion.md`
