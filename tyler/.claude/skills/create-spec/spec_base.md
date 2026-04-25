# <Spec Title>

> **Spec, not plan.** This document captures *what* and *why*, not *how*. Implementation details (files, pseudo-code, tasks) live in the per-phase plans produced by `/create-plan`.

## Problem

<One specific scenario or pain. What's broken or missing today. Concrete beats abstract — describe an actual moment where the status quo fails.>

## Appetite

<Rough scope budget: small (days), medium (1–2 weeks), large (multiple weeks). Think of this as the time you're willing to spend before deciding whether to keep going.>

## Approach

<The shaped solution. Key technologies, system boundaries, data flows. Use a C4 Context or Container diagram if the system shape is non-trivial. Prose, not pseudo-code.>

## Architectural Decisions

<One subsection per decision. Use Y-statement form where it fits: "In the context of X, facing Y, we chose Z over A, accepting B, because C.">

### Decision 1: <name>
- **Choice:** <what we'll do>
- **Rationale:** <why>
- **Trade-off:** <what we accept>

### Decision 2: <name>
- **Choice:**
- **Rationale:**
- **Trade-off:**

## Rabbit Holes

<Known traps, hard parts, edge cases that could blow up scope if we're not careful. Bullet list.>

## No-gos

<Explicitly out of scope. What this spec does NOT cover. Bullet list.>

## Open Questions

<`[NEEDS CLARIFICATION]` markers — must be resolved before phases are picked up by `/create-plan`. Remove this section once empty.>

## Implementation Phases

Each row becomes its own `/create-plan` invocation. The `✓` column marks whether a plan has been created from that phase (text-state checkbox; not interactive in renderers — `/create-plan` flips it via Edit). Phases must be independently plannable from this spec alone — context will be cleared between phases.

| ✓ | # | Phase | Goal | Scope (in) | Out of scope | Depends on | Key files / modules | Size |
|---|---|-------|------|------------|--------------|------------|---------------------|------|
| [ ] | 1 | <name> | <one-line outcome> | <bullets of what's in> | <deferred to later phases> | — | <paths or modules, if known> | S/M/L |
| [ ] | 2 | <name> | … | … | … | Phase 1 | … | M |
| [ ] | 3 | <name> | … | … | … | Phase 1, 2 | … | S |

### Phase notes

For phases that need more detail than fits in the table row. Keep it scope-level — not implementation-level.

#### Phase 1: <name>

<Constraints, success criteria, references that a fresh-context `/create-plan` invocation needs beyond the table row. Skip this subsection if the row is self-contained.>

#### Phase 2: <name>

<…>
