---
name: simple-plan
description: Investigate a straightforward change and propose a concise plan before approved implementation.
---

# Simple Plan

When the user directly asks for a change, investigate first and propose a short
plan before writing code.

## Plan Contents

### Intent and Sources
- Triggering problem, why it matters, intended outcome, constraints and non-goals from the ticket/discussion
- Available source links or artifact paths; flag missing rationale and distinguish proposed assumptions from user decisions

### Current State

- root cause or current behavior
- concrete file references

### Proposed Changes

- what needs to change
- file references where relevant
- task list in implementation order

### Advice

- architectural or implementation guidance when useful

## Process

1. Investigate the codebase first
2. Present the plan to the user
3. Wait for approval unless the user or invoking workflow already authorizes autonomous implementation
4. After approval, keep one primary implementation authority by default
5. Keep the user's why, constraints, and non-goals explicit during implementation
6. After implementation, run `implementation-reviewer`
7. Prefer a fresh skeptical second review pass before declaring completion
8. If you have a separate Claude workflow available, it can be the parallel
   second-opinion lane, but Codex remains primary on this path

## Notes

- Keep the plan concise but concrete
- Include file references whenever possible
- If the task is broad or risky, recommend switching to `create-plan`
- Planning alone does not authorize implementation

## Artifacts

- If saving a plan and Grain is connected, use the supplied task folder, or `Development Artifacts/YYYY-MM-DD-<task>`; pass its ID and storage rule to implementers/reviewers and sync their outputs.
- Keep needed local files and privacy limits; without Grain, continue locally silently.
