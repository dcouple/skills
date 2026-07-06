---
name: create-feature
description: Captures a discussed feature as a lean Feature Ticket work item ready for /do. For multi-phase workstreams use /create-epic instead.
argument-hint: "[feature title or one-line summary]"
disable-model-invocation: true
---

# Create Feature

## Feature: $ARGUMENTS

Turn what the conversation has established (typically a `/discussion`) into a Feature
Ticket that `/do` can execute autonomously. The completion artifact is
`./tmp/<id>/item.md` with `status: ready`.

This skill *captures and sharpens* — it does not re-run the discussion. If the
conversation already settled a point, write it down; don't re-litigate it.

## Steps

### 1. Assemble the core from the conversation
Drive toward the four things the ticket needs, pulling from the discussion so far:
- **Intent** — the why behind the request
- **Desired end state** — user-visible "done"
- **Locked directions** — only decisions the model shouldn't re-make (number them D1, D2…)
- **Out of scope**

Where the conversation left a gap, ask the user directly — one focused round, not a new
discussion. If a codebase fact is missing, dispatch the `codex` skill (role
`code-researcher`); for an external fact, the `web-researcher` sub-agent.

**Success criteria**: the user has explicitly agreed to intent, end state, each locked
direction, and the out-of-scope list.

### 2. Check the shape
One coherent outcome with one verification surface fits a Feature Ticket. If what
emerged is really multiple sequential, independently verifiable phases, say so and
suggest `/create-epic` instead — don't force an epic into a ticket. When in doubt,
prefer the smaller shape.

**Success criteria**: shape confirmed (or handed off to `/create-epic`).

### 3. Write the work item
- Pick `<id>`: short kebab-case slug from the title. Create `./tmp/<id>/`.
- Write `item.md` following `references/feature-ticket.md` (frontmatter + body; don't
  emit the template's "— format" header or guidance quotes).
- Embed verification criteria per `~/.references/verification-criteria.md`: EARS-style,
  numbered `AC1…`, each mapped to a method from
  `~/.references/verification-methods.md` — a lint rule, test, script (backend), or
  natural navigation of the running app (frontend/mobile), matched to the change
  type's rubric in `~/.references/rubrics/`. No "works correctly".
- Keep it LEAN: `/do` starts fresh and is capable — omit anything it can reasonably
  decide itself.
- Save transcript-worthy raw material (key discussion excerpts, mock-ups, links,
  research worth keeping) to `./tmp/<id>/refs/` and link from the item — never inline.
- Leave `status: draft` for now.

**Success criteria**: `item.md` exists; every AC is numbered, observable, and mapped;
nothing in the item restates what refs/ or the model already covers.

### 4. Socratic gate
Always dispatch the `socrates` sub-agent with the draft's path (round 1). It
calibrates its own intensity: a straightforward, well-justified draft gets a
fast pass with zero to two questions; an unargued or scope-grown one gets the
full adversarial challenge — necessity, root cause, simpler alternatives,
shape, assumptions, consequences, completeness (is this the whole of it?).
- Relay the questions to the user **verbatim** and wait for answers — don't
  answer for them; the gate exists to make the user justify the item.
- Re-dispatch socrates with the answers to judge them (round 2); press
  `partial`/`evasive` answers once. Cap: two judged rounds, then proceed with
  anything unresolved carried into Open questions.
- If the dialogue changes the item — narrower scope, different shape
  (`/create-epic`), or not worth doing — update `item.md` or stop.
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
`feat: <item title>`, issue body = the item's intent, desired end state,
verification criteria summary, and the Justification section.

**Success criteria**: published and cross-linked per the shared procedure.

```
Suggested next steps:
- `/do <issue # or ./tmp/<id>/item.md>` — run the autonomous pipeline against this item
- `/discussion [follow-up]` — if a gap surfaced that needs more thinking first
```
