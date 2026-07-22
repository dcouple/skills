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
   - Use the rendered Excalidraw image as the primary visual. Add Mermaid only when the user requests a text-rendered fallback.
   - Reuse a repository-owned long-lived release such as `pr-assets`, and follow the diagram skill's unique naming, collision, manifest, and metadata/direct-content verification rules. Creating that release is a separate hard stop requiring an exact grant such as `{"action":"create_release","repo":"owner/name","tag":"pr-assets"}`; generic GitHub, PR, comment, or asset-upload authorization does not grant it. Otherwise prepare the exact commands and marked Markdown and report the blocker.
7. Audit existing PR body/comment image references. Replace dead, expiring, temporary, or local-only URLs with verified durable assets. Update agent-owned marked sections in place, preserve author text outside them, and change only a broken URL when it sits in author-owned prose.
8. Push the branch. Use `--force-with-lease` only when the rebase made it necessary.
9. Create or update the PR with a summary built from the plans, current diff, and a visual overview bounded by `<!-- pr-visual-overview:start -->` / `<!-- pr-visual-overview:end -->` that embeds the verified image inline. Read the PR back and confirm it is non-draft when the requested outcome is a ready PR.

Rules:
- Never use blanket staging.
- Treat secrets and credentials as stop conditions.
- Keep build-fix commits separate when they are distinct from the feature work.
- If GitHub CLI or network access is unavailable, report exactly where the flow stopped.
