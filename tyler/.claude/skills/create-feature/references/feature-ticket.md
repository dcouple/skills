# Feature Ticket — format

> Produced by `/create-feature`. Saved as `./tmp/<id>/item.md`.
> **Lean and high-signal.** Everything here is required-minimal; raw sources go in `refs/`.

---
```yaml
---
type: feature-ticket
id: <id>
status: ready         # draft | ready | done
pr: <url or # — filled when /do opens it>
---
```

# Feature: `<title>`

## Intent
`<the why + the underlying goal behind the request — not just the requested solution.`
`A few sentences. This is what /do optimizes for and what PR review is judged against.>`

## Desired end state
`<what "done" looks like from the user's side. A before → after helps. No implementation.>`

## Key architecture directions
`<ONLY the locked decisions + any rejected alternative worth naming. Directions, not a`
`design — no file lists or pseudo-code. If the model can reasonably decide it, omit it.`
`Number them (D1, D2…) if there's more than one — reviews cite them by ID.>`

## Starting points (non-exhaustive)
- `<file/module>` — `<why it's relevant, one clause>`

`<2–4 pointers that orient /do without dictating design. Omit section if unknown.>`

## Verification criteria
`<embed shared/verification-criteria.md — acceptance in EARS + how verify proves it>`

## Out of scope
- `<explicit exclusion — the guard against gold-plating>`

## Justification
- `<claim challenged in the Socratic gate>` — `<the reason that held>`

`<distilled from the socrates Q&A, one line per surviving question. This is the`
`item's "FAQ": why this exists, why this shape, why not the cheaper alternative.`
`On a fast pass, socrates' one line naming what convinced it; if the user waived`
`the gate: "Socratic gate waived by user." Full dialogue, if long, in`
`refs/socratic-dialogue.md.>`

## Open questions
- `[NEEDS CLARIFICATION]` `<unresolved design choice — name it, don't paper over it>`

`<omit section if none>`

## References (optional, in refs/)
- `refs/discussion.md`
- `refs/mockup.png`
