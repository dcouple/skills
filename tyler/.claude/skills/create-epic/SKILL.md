---
name: create-epic
description: Captures a discussed multi-phase workstream as an Epic Spec work item ready for /do. For a single-outcome change use /create-feature instead.
argument-hint: "[epic title or one-line summary]"
disable-model-invocation: true
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
codebase fact is missing, dispatch the `codex` skill (role `code-researcher`); for an
external fact, the `web-researcher` sub-agent.

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
- Per-phase verification criteria per `~/.references/verification-criteria.md`:
  EARS-style, numbered `AC1…` within each phase, each mapped to a method from
  `~/.references/verification-methods.md` matched to that phase's change type
  (rubrics in `~/.references/rubrics/`).
- Keep it LEAN and at spec altitude: no file lists, pseudo-code, or task sequences —
  `/do`'s plan stage owns the *how* per phase.
- Save transcript-worthy raw material to `./tmp/<id>/refs/` and link from the item —
  never inline.
- Leave `status: draft` for now.

**Success criteria**: `item.md` exists; phases are sequential and independently
verifiable; every AC is numbered, observable, and mapped; spec altitude respected.

### 4. Socratic gate
Always dispatch the `socrates` sub-agent with the draft's path (round 1). It
calibrates its own intensity, but a multi-phase commitment is never
"straightforward" — expect the full challenge. For an epic it bears down on
shape (are the phases real?), appetite, consequences, and completeness,
alongside necessity and assumptions.
- Relay the questions to the user **verbatim** and wait for answers — don't
  answer for them; the gate exists to make the user justify the item.
- Re-dispatch socrates with the answers to judge them (round 2); press
  `partial`/`evasive` answers once. Cap: two judged rounds, then proceed with
  anything unresolved carried into Open questions.
- If the dialogue changes the item — fewer phases, collapse to
  `/create-feature`, or not worth doing — update `item.md` or stop.
  Abandoning here is a success, not a failure.
- Write the distilled Q&A into a `## Justification` section in `item.md`
  (one line per question: claim challenged — reason that held). Long
  exchanges go to `refs/socratic-dialogue.md`, linked from the item.
- The user may waive the gate explicitly; record
  `Socratic gate waived by user.` in the Justification section.

**Success criteria**: socrates returned `pass` (or the cap was reached, or
the user waived); `## Justification` written into `item.md`.

### 5. Mark ready and publish
Publish per `~/.references/publish-work-item.md` — issue title
`feat: <epic title>`, issue body = the epic's problem, end state, the
phases table, and the Justification section.

**Success criteria**: published and cross-linked per the shared procedure.

```
Suggested next steps:
- `/do <issue # or ./tmp/<id>/item.md>` — run the pipeline; phases execute sequentially, one PR
- `/discussion [follow-up]` — if a phase boundary needs more thinking first
```
