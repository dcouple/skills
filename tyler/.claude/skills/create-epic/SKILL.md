---
name: create-epic
description: Captures a discussed multi-phase workstream as an Epic Spec work item ready for /do. Use when the user explicitly asks to create an epic, epic spec, feature epic, or spec spanning several sequential phases — e.g. "create an epic for this", "turn this into a spec", "this is bigger than one feature, write it up". For a single-outcome change use /create-feature instead.
argument-hint: "[epic title or one-line summary]"
allowed-tools: Read, Write, Edit, Glob, Grep, Task
---

# Create Epic

## Epic: $ARGUMENTS

Turn what the conversation has established (typically a `/discussion`) into an Epic
Spec that `/do` can execute phase by phase. The completion artifact is
`./tmp/<id>/item.md` with `status: ready`. Epics run **sequentially** in one PR —
phase n+1 starts only after phase n's channel completes.

This skill *captures and sharpens* — it does not re-run the discussion.

## Steps

### 1. Assemble the core from the conversation
Drive toward what the spec needs, pulling from the discussion so far:
- **Problem / context** — the broader problem and why now
- **Goals and desired end state** — what the world looks like when the epic lands
- **Locked directions** — only decisions the model shouldn't re-make (number them D1, D2…)
- **Out of scope**

Where the conversation left a gap, ask the user directly — one focused round. If a
codebase or external fact is missing, dispatch `code-researcher` or `web-researcher`
to fill exactly that gap.

**Success criteria**: the user has explicitly agreed to problem, end state, each locked
direction, and the out-of-scope list.

### 2. Cut the phases
Split the work into sequential phases, each a self-contained work item: one coherent
outcome, independently verifiable, buildable on the phases before it. Don't split
because many files are touched — split where verification surfaces genuinely differ.
If it collapses to one phase, say so and suggest `/create-feature` instead.

**Success criteria**: phase table agreed with the user — each phase has a goal, scope,
and its own verification surface; order confirmed.

### 3. Write the work item
- Pick `<id>`: short kebab-case slug from the title. Create `./tmp/<id>/`.
- Write `item.md` following `references/epic-spec.md` (frontmatter + body; don't emit
  the template's "— format" header or guidance quotes).
- Per-phase verification criteria per `references/verification-criteria.md`:
  EARS-style, numbered `AC1…` within each phase, each mapped to an automated or
  computer-use method.
- Keep it LEAN and at spec altitude: no file lists, pseudo-code, or task sequences —
  `/do`'s plan stage owns the *how* per phase.
- Save transcript-worthy raw material to `./tmp/<id>/refs/` and link from the item —
  never inline.
- Leave `status: draft` for now.

**Success criteria**: `item.md` exists; phases are sequential and independently
verifiable; every AC is numbered, observable, and mapped; spec altitude respected.

### 4. Learning gate [human]
Ask the user to state back, in one or two sentences, the phase cut and the key
decision(s). One exchange, not a quiz. If their read conflicts with the doc, reconcile
before proceeding.

**Success criteria**: the user's teach-back matches the item.

### 5. Mark ready and hand off
Set `status: ready` in `item.md`.

```
Suggested next steps:
- `/do ./tmp/<id>/item.md` — run the pipeline; phases execute sequentially, one PR
- `/discussion [follow-up]` — if a phase boundary needs more thinking first
```
