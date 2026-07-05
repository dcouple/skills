---
name: create-feature
description: Captures a discussed feature as a lean Feature Ticket work item ready for /do. Use when the user explicitly asks to create a feature, feature ticket, or turn the current discussion into a feature — e.g. "create a feature for this", "make this a ticket", "write this up as a feature". For multi-phase workstreams use /create-epic instead.
argument-hint: "[feature title or one-line summary]"
disable-model-invocation: true
allowed-tools: Read, Write, Edit, Glob, Grep, Task, Skill, Bash(gh:*)
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
`code-researcher`; Claude `code-researcher` sub-agent as fallback); for an external
fact, the `web-researcher` sub-agent.

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
  numbered `AC1…`, each mapped to an automated or computer-use method. No "works
  correctly".
- Keep it LEAN: `/do` starts fresh and is capable — omit anything it can reasonably
  decide itself.
- Save transcript-worthy raw material (key discussion excerpts, mock-ups, links,
  research worth keeping) to `./tmp/<id>/refs/` and link from the item — never inline.
- Leave `status: draft` for now.

**Success criteria**: `item.md` exists; every AC is numbered, observable, and mapped;
nothing in the item restates what refs/ or the model already covers.

### 4. Learning gate [human]
Ask the user to state back, in one or two sentences, the key decision(s) and the
verification approach. One exchange, not a quiz. If their read conflicts with the doc,
reconcile — update the doc or the understanding — before proceeding.

**Success criteria**: the user's teach-back matches the item.

### 5. Mark ready and publish
1. Set `status: ready` in `item.md`.
2. Create the GitHub issue: `gh issue create` in the project's repo (from the
   `Work-item tracking` section of the project's `CLAUDE.md`, or the current
   repo) — title `feat: <item title>`, body = the item's intent, desired end
   state, and verification criteria summary.
3. Invoke the `notion` skill, operation `publish`, with `./tmp/<id>/` and the
   issue URL — it creates the Notion work item and uploads `item.md` + every
   `refs/` file, returning the page URL.
4. Cross-link: add the Notion page URL to the GitHub issue body
   (`gh issue edit`), and record both in `item.md` frontmatter as `github:`
   and `notion:`. On `NOTION UNAVAILABLE`, proceed GitHub + local only and
   tell the user.

**Success criteria**: issue exists, Notion work item exists with all
artifacts (or its absence was reported), and each of issue / Notion page /
item.md links to the others.

```
Suggested next steps:
- `/do <issue # or ./tmp/<id>/item.md>` — run the autonomous pipeline against this item
- `/discussion [follow-up]` — if a gap surfaced that needs more thinking first
```
