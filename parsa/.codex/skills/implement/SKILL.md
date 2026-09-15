---
name: implement
description: Execute an approved plan with one primary implementation stream and checks for completeness and intent fidelity.
---

# Implement

## Load and scope

- Read the supplied plan and its linked brief/dossier; otherwise locate the relevant approved plan in `tmp/ready-plans/`.
- The brief governs why; the plan governs execution; the dossier supplies evidence. Surface conflicts rather than silently narrowing scope.
- Identify actions needing separate approval, such as destructive operations or external configuration changes. Ordinary scoped implementation follows project policy.
- Inspect migration requirements before coding; do not defer safety decisions until after execution.

## Implement

1. Execute directly as the primary owner, using the full plan, intent, workspace, and acceptance criteria.
2. Keep dependent work together. Sidecars are appropriate only for disjoint writes with a clear integration contract and one final integration owner.
3. Update plan progress and record material deviations as `Plan Delta`; escalate changes that weaken intent or exceed authority.
4. Run the project's applicable checks at meaningful checkpoints, for example its test suite, lint, typecheck, or build commands.
5. Verify the actual runtime or user-facing path, not just the existence of new files.

## Review

- Run `implementation-reviewer` against the brief, plan, diff, and check evidence, preferably in fresh context.
- Use a fresh second-opinion review when useful and available; a separate Claude workflow is optional.
- Wait for all started lanes, merge findings, fix supported issues, and verify affected checks/review criteria again.
- Bring unresolved decisions to the user as one combined set. Do not call blocked or failing checks a pass.

## Schema and operational changes

- Detect changes using the project's actual schema and migration locations, not a particular filename.
- Follow its migration-generation workflow only when configured and within authorization; inspect and report generated changes.
- Do not apply migrations or destructive operations without the required approval. Never hide destructive statements by showing only additive SQL.
- Keep code completion separate from pending deployment or human steps.

## Finish

- Move an applicable local plan from `tmp/ready-plans/` to `tmp/done-plans/` only after its completion criteria and review gates pass.
- Report task completeness, checks, intent fidelity, review findings, and remaining manual steps.
- Do not commit, push, or open a PR unless the user or parent workflow authorizes it.

## Grain handoff

- If connected, read/update every workflow artifact in the supplied Grain folder, or `Development Artifacts/YYYY-MM-DD-<task>`; this overrides local-only storage in invoked skills.
- Pass the folder ID and rule to all agents; sync outputs for agents without access, including plan status and review evidence.
- Keep source code and executable files in their required project locations, plus needed local artifact copies. Preserve privacy limits; without Grain, continue locally silently.
