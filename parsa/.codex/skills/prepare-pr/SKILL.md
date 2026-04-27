---
name: prepare-pr
description: Prepare a branch for review by committing scoped changes, rebasing on main, running builds, and creating or updating a pull request. Use when the user wants the branch ready for PR review.
---

# Prepare PR

This is a high-trust workflow. Surface any destructive or ambiguous step before proceeding.

Workflow:
1. Group current changes into logical commits, ideally by done-plan.
2. Create focused commits without staging unrelated work.
3. Fetch and rebase onto `origin/main`.
4. Resolve obvious conflicts directly. Ask the user about semantic conflicts.
5. Run the relevant build steps and fix straightforward failures.
6. Create a visual PR diagram before opening/updating the PR:
   - Use the `excalidraw-pr-diagrams` skill.
   - Keep all generated diagram working files under `/tmp`, usually `/tmp/codex-pr-diagrams/<branch-or-pr>/`.
   - Add a `## Visual Overview` section to the PR body.
   - Include explicit `Before` and `After` diagrams in the visual overview.
   - Prefer GitHub-rendered Mermaid in the PR body and save matching `.excalidraw` source under `/tmp`.
7. Create or update the PR with a summary built from the plans, current diff, and visual overview.
8. Push with `--force-with-lease` only when rebase made it necessary.

Rules:
- Never use blanket staging.
- Treat secrets and credentials as stop conditions.
- Keep build-fix commits separate when they are distinct from the feature work.
- If GitHub CLI or network access is unavailable, report exactly where the flow stopped.
