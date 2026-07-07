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
Draft `./tmp/<id>/item.md` per `~/.references/draft-work-item.md`, using this
skill's `references/feature-ticket.md` as the template. Suitable methods for a
feature's ACs: a lint rule, test, script (backend), or natural navigation of
the running app (frontend/mobile).

**Success criteria**: `item.md` exists; every AC is numbered, observable, and mapped;
nothing in the item restates what refs/ or the model already covers.

### 4. Socratic gate
Run the gate per `~/.references/socratic-gate.md`. For a feature it bears
down on necessity, root cause, simpler alternatives, and shape; a
straightforward, well-justified draft fast-passes with zero to two questions.
If the dialogue reveals a multi-phase shape, hand off to `/create-epic`.

**Success criteria**: gate procedure complete — socrates returned `pass` (or
the cap was reached, or the user waived); `## Justification` written into
`item.md`.

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
