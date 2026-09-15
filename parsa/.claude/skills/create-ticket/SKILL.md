---
name: create-ticket
description: Turn conversation intent into GitHub tickets with clear scope, acceptance criteria, and unresolved inputs.
argument-hint: "[ticket request, conversation summary, or issue intent]"
allowed-tools: Read, Grep, Glob, Bash
---

# Create Ticket

## Ticket Request: $ARGUMENTS

Your job is to turn this conversation into a clean delegation ticket.

The ticket should let someone else do the work without needing the whole chat.
It should capture what we mean, why it matters, what counts as done, and what is
still missing. Do not turn it into a detailed implementation plan unless I ask
for that.

## Workflow

1. Identify the target repository from the local checkout, my links, or prior conversation. If the repository is ambiguous and cannot be inferred safely, ask one concise question.
2. Extract what I actually want delegated. Prefer my latest explicit instruction over older context.
3. Decide whether to create one ticket or many:
   - Create one ticket when the work has one outcome, one owner, and one coherent acceptance surface.
   - Split into multiple tickets when the conversation contains independent outcomes, different owners, materially different release timing, or distinct product/engineering surfaces.
   - Do not split merely because several files or pages may be touched.
4. Draft the issue title and body using the conventions below.
5. If I already explicitly asked to create the ticket, create it. If I asked to discuss or asked whether enough information exists, show the draft or summarize the intended ticket first.
6. Assign, label, or milestone only when I requested it or the conversation makes it unambiguous. Avoid guessing labels.
7. After creation, return the issue URL(s) and briefly state what was captured.

## Title Format

Follow the repository's issue-title conventions. One possible format is:

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

What triggered the work, why it matters, and the intended user/business/engineering outcome. Preserve relevant constraints and non-goals, and cite the originating discussion or artifacts when available.

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

Keep `Intent`, `Scope`, and `Acceptance Criteria`; lightweight tickets may compress these into short prose but must retain the motivation and intended outcome. Omit other sections only when empty or misleading.

## Writing Rules

Read [references/intent-handoff.md](references/intent-handoff.md) when capturing intent; its complete and incomplete examples show what to preserve and what never to invent.

- Ground Intent in the source discussion/artifacts: include the trigger, why it matters, desired outcome, constraints and non-goals plus available source links; flag missing rationale in Inputs Needed rather than inventing it.
- Write tickets for delegation, not for self-documentation.
- Preserve my language for product intent when it is clear and useful.
- Mention code references only as examples or starting points unless the user asked for exact implementation direction.
- Mark starting points as non-exhaustive whenever they come from a quick scan, memory, or partial conversation.
- Make acceptance criteria observable and outcome-based.
- Put unresolved decisions in `Inputs Needed`; do not bury blockers in prose.
- Do not fabricate details, prices, owners, deadlines, labels, or implementation constraints.
- Keep the title action-oriented and specific enough to scan in an issue list.

## GitHub Tooling

Prefer available GitHub tools when present. If no GitHub connector is available, use authenticated `gh` from the local checkout. Before using `gh`, resolve the repository with `gh repo view` or `git remote -v` when needed.

When creating more than one issue, create them sequentially and return a compact list of issue URLs with titles.

- Submit titles/bodies as data using a connector or body-file/JSON input, never interpolated shell source; read back the created issue to verify its repository and content.
- If saving drafts or supporting files and Grain is connected, use the supplied task folder, or `Development Artifacts/YYYY-MM-DD-<task>`, and link the created ticket. Keep needed local files and privacy limits; otherwise continue normally silently.
