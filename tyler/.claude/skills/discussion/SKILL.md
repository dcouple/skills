---
name: discussion
description: Interactive back-and-forth to clarify, understand, or figure something out — an idea, an approach, a tradeoff, or a suspected bug. Use when the user wants to think out loud or explore before committing to anything — e.g. "let's discuss X", "help me understand Y", "why is Z happening", "what should we do about W". Produces clarity plus a dated decision log, not deliverables; work items are created afterward with /create-feature, /create-epic, or /create-issue.
argument-hint: "[idea, question, or topic]"
---

# Discussion

## Topic: $ARGUMENTS

Have an interactive, opinionated discussion. The goal is shared clarity — understanding
the problem, weighing the options, or pinning down what's actually happening — not a
document. When the discussion converges on something worth building or fixing, the user
invokes the matching `/create-*` skill; this skill's job ends at clarity.

## Conversation and research only — unless asked

Don't edit source files, propose diffs to apply, or write documents, specs, tickets,
or verification criteria unless the user explicitly asks for one mid-discussion.
Capture belongs to the `/create-*` skills, and doing it unprompted drags the
conversation down to paperwork altitude. The one exception is Step 3's
decision log — a record of what was decided, not a deliverable.

## Steps

### 1. Dispatch the right specialist for each question
Delegate legwork to sub-agents so bulky exploration stays out of this thread. Pick by
what the user is actually asking:

- **How does our code work? What exists today?** → the `codex` skill, role
  `code-researcher` (returns file:line findings).
- **What do the docs / ecosystem / other people do?** → the `web-researcher`
  sub-agent (returns a cited dossier). Reach for it whenever up-to-date
  information or outside opinions would sharpen the discussion — library
  versions, current best practice, how others solved this.
- **Why is this broken? Is this a bug?** → the `codex` skill, role `investigator`
  (reproduces and root-causes, returns a finding with evidence and confidence).
  If reproduction requires driving the running app, dispatch `frontend-verifier`
  first to exercise the flow and capture evidence, then pass its transcript along
  with the defect report.

Only research what the discussion actually needs — let questions pull research, not
the other way around. Dispatch mid-conversation as new questions arise; run
independent dispatches in parallel.

**Success criteria**: every claim you make about the codebase, ecosystem, or defect
traces to a sub-agent finding or user statement, not a guess.

### 2. Discuss and converge
- Present findings and options with tradeoffs; be opinionated — recommend with
  reasoning, defer to user judgment.
- Name disagreements and unresolved choices instead of papering over them.
- Keep altitude: decisions and direction, not file-by-file detail.

**Success criteria**: the user says the question is answered, the direction is clear,
or they're ready to capture a work item.

### 3. Log the decisions, then hand off
When the discussion converges, write the decision log to
`./tmp/discussions/YYYY-MM-DD-<slug>.md`: the decisions made and why, the
direction chosen and over what alternatives, constraints the user stated,
open questions. A few lines each — dated and slugged so parallel
workstreams never collide. This is how intent survives past the
conversation: the `/create-*` drafting step reads it, and anyone resuming
the thread starts from it instead of from memory.

Then point at the capture skill — don't run it yourself unless the user asks:

```
Decision log: ./tmp/discussions/YYYY-MM-DD-<slug>.md

Suggested next steps:
- `/create-feature [title]` — capture a single-outcome change as a Feature Ticket
- `/create-epic [title]` — capture a multi-phase workstream as an Epic Spec
- `/create-issue [title]` — capture a defect (investigated here) as a Bug Report
- `/discussion [follow-up]` — keep exploring a different aspect
```
