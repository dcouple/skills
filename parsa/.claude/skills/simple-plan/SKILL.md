---
name: simple-plan
description: Investigate a straightforward change and propose a concise plan before approved implementation.
argument-hint: "[what the user wants done]"
allowed-tools: Read, Grep, Glob, WebFetch, Agent
---

# Simple Plan

Investigate the requested change before proposing implementation. Use `create-plan` for broad or risky work.

## My Plan Will Include

### Intent and Sources
- Triggering problem, why it matters, intended outcome, constraints and non-goals from the ticket/discussion
- Available source links or artifact paths; flag missing rationale and distinguish proposed assumptions from user decisions

### Current State

- Current behavior or an evidenced root cause
- File references and code snippets where relevant

### Proposed Changes

- Clear explanation of what needs to change
- File references and code snippets where necessary
- Task list of all work to be done

### My Advice

- Relevant tradeoffs or architectural advice, only where they affect the decision.

## Process

1. Investigate the codebase first
2. Present the plan to the user
3. Wait for approval unless the user or invoking workflow already authorizes autonomous implementation
4. After approval, prefer one primary `implementer` sub-agent to execute the whole plan rather than fragmenting it by default
5. Keep the user's stated why, constraints, and non-goals explicit during implementation rather than letting the task list silently replace them
6. After implementation, run the Claude `implementation-reviewer` and Codex review in parallel when the plugin is available, and wait for both before declaring completion
7. If the Codex plugin is unavailable, run the Claude `implementation-reviewer` alone before declaring completion

## Notes

- Instructions must be very clear with code snippets and file paths
- If implementation proceeds, keep one primary implementation authority unless the write scopes are clearly disjoint
- The final review must check both task completion and whether the implementation still satisfies the user's original intent
- Planning alone does not authorize implementation

## Artifacts

- If saving a plan and Grain is connected, use the supplied task folder, or `Development Artifacts/YYYY-MM-DD-<task>`; pass its ID and storage rule to implementers/reviewers and sync their outputs.
- Keep needed local files and privacy limits; without Grain, continue locally silently.

User Query: $ARGUMENTS
