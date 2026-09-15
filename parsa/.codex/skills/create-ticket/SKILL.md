---
name: create-ticket
description: Capture work and evolving intent during discussion as one or more GitHub tickets, Grain briefs, or both. Use for ticket or issue creation, follow-ups, backlog capture, delegation, and revisions as decisions change. Preserve the what, why, outcome, scope, and acceptance criteria.
---

# Create ticket

You are the keeper of intent at delegation. Help the next person understand what should change, why it matters, and what success looks like.

## Capture the intent

- Read the conversation, existing issue, and linked briefs. Use the latest explicit user decisions to establish the current what, why, affected people, and desired outcome.
- Preserve the user's useful language, constraints, and scope boundaries. Separate verified facts, user decisions, proposed approaches, and open questions.
- Keep current intent at the top. When it evolves, retain a short history of what changed, the reason, and its source; mark earlier decisions as superseded.
- Read [intent-handoff.md](references/intent-handoff.md) for examples of complete, incomplete, and evolving intent. Capture missing rationale in Inputs Needed and ask when it materially changes the work.

## Shape the delegation

- Choose the requested handoff: one or more tickets, Grain briefs, or both. Keep a coherent outcome together; split independent outcomes, owners, or release timing, and link shared context and dependencies.
- Resolve the repository for GitHub work and inspect related issues or briefs. Reuse the matching artifact for an authorized revision; create follow-ups for distinct work.
- Use a readable, action-oriented title following repository conventions, such as `fix: make refund exports reconcilable`.
- Keep **Intent**, **Scope**, and **Acceptance Criteria** in each ticket or brief. Explain the what and why, the agreed work, and observable outcomes, with concrete examples where helpful.
- Add **Inputs Needed**, **Starting Points**, and **Decision History** when useful. Label code references as exploratory starting points and implementation ideas as proposals.
- Ground every requirement in the available sources. Preserve source links or identifiable discussion references so later planners and reviewers can recover the reasoning.
- Apply this skill during discussion when concrete work or changing intent needs capture. Draft within exploratory discussion; save or publish when the request or active workflow authorizes that destination. Use requested or unambiguous assignees, labels, and milestones.

## Keep a living Grain brief

- When saving intent and Grain is connected, follow its installed skill to create or update the relevant briefs. Honor Grain-only, GitHub-only, combined, and draft-only requests; for ticket work, prefer a linked Grain brief alongside the issue.
- Reuse the supplied task workspace or an existing linked brief. For new work, use a clearly named workspace in `Development Artifacts`; retain its ID as the ticket, branch, and PR become available.
- Explain the problem and desired experience from first principles. Read [explain-visually](../explain-visually/SKILL.md) when a visual would clarify the intent; contribute to this same brief.
- Use readable headings, bullets, and directly accessible text. Keep the current what, why, scope, acceptance criteria, open inputs, and source-backed decision history together.
- When tickets and briefs coexist, keep each issue self-contained and cross-link the corresponding artifacts. Grain holds the richer explanation; the issue carries the current delegation contract and a concise history of material changes.
- On an authorized revision, reconcile the latest discussion and linked artifacts before updating them. Preserve accurate human contributions and surface conflicting decisions for resolution.
- If Grain is disconnected, keep the full brief in GitHub when ticket publication is authorized; otherwise return a copyable draft in the requested available destination. Report failed connected saves and the status of each artifact independently.
- Match artifact access to the intended audience. Keep sensitive material in approved private destinations and create public shares when the user has authorized that audience. Pass the workspace ID and storage rule to helpers.

## Verify and return

- Prefer available GitHub tools, with authenticated `gh` as a fallback. Send titles and bodies as structured data or body files.
- Before publishing, read as the assignee: can they explain what changes, why, how success is observed, and which decisions remain open?
- Read back each saved ticket or brief; verify content, cross-links, audience, and current intent. Inspect any visual companion and state the limits of available verification.
- Return the ticket and brief links grouped by outcome, with save status where needed. Carry these references into subsequent planning, implementation, and PR handoffs.
