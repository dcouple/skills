---
name: create-ticket
description: Capture conversation context and explicit human intent into one or more high-level GitHub tickets. Use when the user asks to create a ticket, issue, GitHub equivalent of a planning intent brief, delegation ticket, backlog item, or asks to turn the current discussion into ticket(s), especially when the work should be framed by intent, scope, acceptance criteria, inputs needed, and non-exhaustive starting points.
---

# Create Ticket

## Overview

Create GitHub issues that preserve human intent and delegation context without turning the ticket into an implementation plan. The output should feel like the GitHub equivalent of a planning intent brief: clear enough for another agent or engineer to investigate and execute, but not overloaded with premature file-by-file instructions.

## Workflow

1. Identify the target repository from the local checkout, the user's links, or prior conversation. If the repository is ambiguous and cannot be inferred safely, ask one concise question.
2. Extract the user's actual intent from the conversation. Prefer the latest explicit user instruction over older context.
3. Decide whether to create one ticket or many:
   - Create one ticket when the work has one outcome, one owner, and one coherent acceptance surface.
   - Split into multiple tickets when the conversation contains independent outcomes, different owners, materially different release timing, or distinct product/engineering surfaces.
   - Do not split merely because several files or pages may be touched.
4. Draft the issue title and body using the conventions below.
5. If the user already explicitly asked to create the ticket, create it. If they asked to discuss or asked whether enough information exists, show the draft or summarize the intended ticket first.
6. Assign, label, or milestone only when the user requested it or the conversation makes it unambiguous. Avoid guessing labels.
7. After creation, return the issue URL(s) and briefly state what was captured.

## Title Format

Use Conventional Commits-inspired issue titles by default:

```text
type: short imperative summary
```

Good examples:

- `docs: update public pricing references`
- `feat: add workspace invite reminders`
- `fix: correct onboarding redirect state`
- `chore: audit stale billing copy`

Prefer common types such as `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `perf`, `ops`, or `design`. Keep the title readable as an issue title; do not force strict commit syntax when it would obscure the work.

## Standard Format

Use these headers by default:

```md
## Intent
Short description of the business, product, or engineering goal and why this work matters.

## Scope
What should be included in the work. Keep this outcome-focused, not file-by-file.

## Starting Points
Optional non-exhaustive references, links, files, docs, examples, or search terms.

This list is not exhaustive. Treat it as a starting point and investigate further before implementation.

## Acceptance Criteria
- Observable condition that must be true when complete.
- Another condition.
- Any explicit exclusions or edge cases.

## Inputs Needed
Any missing product decisions, copy, pricing, designs, credentials, stakeholder approvals, or other information needed before implementation.

## Notes
Context, constraints, risks, or handoff guidance for the assignee or implementation agent.
```

Omit a section only when it would be empty or misleading. Keep `Intent`, `Scope`, and `Acceptance Criteria` unless the user asks for a very lightweight ticket.

## Writing Rules

- Write tickets for delegation, not for self-documentation.
- Preserve the user's language for product intent when it is clear and useful.
- Mention code references only as examples or starting points unless the user asked for exact implementation direction.
- Mark starting points as non-exhaustive whenever they come from a quick scan, memory, or partial conversation.
- Make acceptance criteria observable and outcome-based.
- Put unresolved decisions in `Inputs Needed`; do not bury blockers in prose.
- Do not fabricate details, prices, owners, deadlines, labels, or implementation constraints.
- Keep the title action-oriented, Conventional Commits-inspired, and specific enough to scan in an issue list.

## GitHub Tooling

Prefer the GitHub plugin or app tools when available. If the connector cannot access the repo, use authenticated `gh` from the local checkout. Before using `gh`, resolve the repository with `gh repo view` or `git remote -v` when needed.

When creating more than one issue, create them sequentially and return a compact list of issue URLs with titles.
