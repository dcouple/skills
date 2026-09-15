---
name: handoff
description: Prepare a verified resumption brief when moving work to another agent, device, or session, including local-to-cloud coding handoffs. Use for "hand this off," "continue elsewhere," or "save where we are." Not a general recap, automatic task launch, or claim that local files have transferred.
---

# Handoff

You are the outgoing collaborator. Give the next person or agent enough verified context to continue without rediscovering the work or repeating mistakes.

## Capture what matters

- Preserve the goal, why it matters, constraints, non-goals, and decisions with their reasons. Distinguish approved work from suggestions.
- Read the current state rather than trusting the transcript. Record completed work, unfinished work, meaningful failed attempts, blockers, and the next concrete action.
- Link authoritative instructions, plans, evidence, and artifacts. Distill only what the next worker needs; do not dump the conversation or rely on hidden session context.
- Include pending approvals and the boundary of authorized work. Preparing the handoff does not launch another agent or approve further actions.

## Make coding work portable

- Identify the repository, branch, exact commit, issue/PR, and relevant setup instructions. Include project-specific checks with their results and the revision they tested.
- Inspect staged, unstaged, untracked, and unpushed work. Identify task changes separately from unrelated edits; local paths and commit hashes alone are not proof of remote availability.
- Make required code and files reachable through an authorized push or access-controlled transfer, or clearly mark them as not transferred. Do not commit, push, or upload unrelated work merely to complete a handoff.
- Record required tools, services, and credential names or setup steps, never secret values. Do not assume the receiving agent has local plugins, skills, credentials, or network access.
- Keep private code and patches in access-controlled locations, not a public explanation page. If work cannot transfer safely within the request, identify the exact missing step.

## Save one authoritative brief

- Honor an explicit destination. Otherwise, when Grain is connected, read its installed skill and update the existing task workspace; if none exists, create a clearly named one in `Development Artifacts`. Retain its ID for subsequent updates.
- Make the brief readable to both humans and agents, with essential text visible rather than hidden behind interactive controls. Reference existing artifacts instead of duplicating them.
- For cross-device delivery, prefer a public-safe Grain share when public sharing is authorized by the request or an established user preference. Otherwise use an appropriately restricted destination or ask before publishing.
- Inspect what the share exposes, not just its title. Exclude secrets, private source, and sensitive context; if removing them would make the handoff unusable, use access-controlled GitHub instead. Return the actual verified share URL, never invent one.
- If Grain is unavailable or unsuitable, update a clearly labeled handoff/status section on the existing PR, or the issue if there is no PR. Preserve the original intent, acceptance criteria, and other contributors' content; use a timestamped comment when editing the body would be disruptive.
- If neither destination is writable, return a self-contained, copyable brief in chat and say it is not saved remotely. Do not create a new issue or PR just to store a handoff unless requested.
- Keep necessary local working files, but never make them the only copy required for a remote handoff. A connected save failure must be reported, even if a fallback succeeds.

## Verify and deliver

- Read back the saved brief and check its links, revision, and sharing scope. Verify public links without relying on your signed-in session when possible; distinguish that from untested recipient access to private resources.
- Return the brief's link and a paste-ready instruction to resume, naming the first action and any transfer/access blockers.
- Tell the receiving agent to read repository instructions and reconcile the brief with the current branch, issue/PR, and artifact state before acting. A handoff is a checkpoint, not proof that nothing has changed.
