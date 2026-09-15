---
name: discussion
description: Discuss a feature, question, or approach using evidence and tradeoffs, without changing the project.
---

# Discussion

## Rules

- Discuss the user's topic; do not implement, edit project files, or produce patches.
- Read relevant code or sources when the answer depends on them.
- Distinguish observed facts from recommendations and unresolved assumptions.
- Apply `rewrite-simply` when available to keep responses easy to skim.

## Discuss

1. Establish the desired outcome from the request and known context.
2. Investigate only what helps the current decision; use an explorer or researcher for independent questions when useful.
3. Present concrete options, tradeoffs, and a recommendation.
4. Ask about product choices and preferences that evidence cannot settle.

## Probe when useful

- For observable questions, a small isolated probe can replace guesswork: for example, testing output shape or measuring latency.
- Keep probes outside the project, reversible, and within existing authorization; do not contact production or install dependencies without appropriate scope.
- If saving probe evidence and Grain is connected, use the task's shared folder, or `Development Artifacts/YYYY-MM-DD-<task>`. Keep needed local files and privacy limits; otherwise continue normally silently.

## Handoff and next steps

First recap the trigger, why it matters, desired outcome, constraints/non-goals, decisions, open questions and available source references. Distinguish user intent from proposed assumptions; keep this handoff in conversation without editing project files. Include `create-ticket` as a next step when the discussion is ready for delegation.

End with the next useful step, such as more discussion, research, investigation, or planning. Do not imply approval to implement.
