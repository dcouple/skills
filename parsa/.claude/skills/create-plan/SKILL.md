---
name: create-plan
description: Research a significant change, reconcile a plan with its intent and research, and review it before implementation.
argument-hint: "[feature description or ticket reference]"
allowed-tools: Read, Grep, Glob, WebFetch, WebSearch, Write, Task
---

# Create plan

## Rules

- Produce a plan, not application code. Planning does not authorize implementation.
- Preserve the user's why, locked decisions, non-goals, and success criteria.
- Discover the actual repository structure, stack, and checks; do not impose a preferred architecture.
- Choose tests, compatibility, and migration work from project contracts and change risk, not blanket bans.

## Research

1. Read applicable repository instructions and inspect the affected entrypoints, data contracts, integration surfaces, and existing patterns.
2. Open every existing file used as evidence and verify line anchors in the current checkout.
3. Use primary external documentation where repository evidence cannot answer a question.
4. Ask only about decisions that materially block planning; label assumptions and unresolved mismatches.

## Draft three artifacts

Use supplied locations when present; these are the defaults:

| Artifact | Location | Purpose |
|---|---|---|
| Intent brief | `tmp/plan-artifacts/YYYY-MM-DD-description-brief.md` | Outcome, audience, locked decisions, constraints, non-goals, success criteria |
| Research dossier | `tmp/plan-artifacts/YYYY-MM-DD-description-research-dossier.md` | Verified anchors, reusable patterns, gotchas, useful docs, suggested approach |
| Reconciled plan | `tmp/ready-plans/YYYY-MM-DD-description.md` | Authoritative implementation handoff |

- Use [plan_base.md](plan_base.md) for the plan's structure.
- Ask a fresh `research-dossier-writer` for the supporting dossier from the same brief; save its returned content if it cannot write.
- Keep the provisional plan outside `ready-plans` until reconciliation.

## Evidence and reconciliation

- In `Verified Repo Truths`, use `Fact`, `Evidence`, and `Implication`; add search scope/results as `Search Evidence` for absence claims.
- Keep proposed changes in `Delta Design` and `Tasks`, not in fact sections.
- Mark affected paths as existing or new; remove illustrative filenames from the finished plan.
- Compare draft and dossier. Recheck factual conflicts against the repository rather than choosing whichever sounds better.
- Import useful anchors and constraints, not the whole dossier; record material additions, resolutions, and exclusions in `Reconciliation Notes`.
- Keep the brief authoritative for intent and link all source artifacts.

## Review

1. Send the saved plan, brief, dossier, and current checkout to a fresh reviewer with `subagent_type: "plan-reviewer"` (or the installed alias).
2. If the Codex plugin is available, run its fresh second-opinion audit in parallel and wait for both lanes.
   Example, when supported: `/codex:rescue --wait --fresh --model gpt-5.6-sol --effort xhigh audit [plan] against [brief] and the current repository`.
3. Merge findings. Fix supported factual errors and omissions; bring only unresolved scope or design decisions to the user.
4. Do not mark the plan ready while factual blockers remain. Repeat review if requested or needed to verify material revisions.

## Finish

- Return a short summary, artifact links, review status, and any remaining decisions.
- Implementation is a separate step, such as `implement <plan-path>`; do not start it here.
- Default lifecycle: `tmp/ready-plans/` → `tmp/done-plans/` after verified implementation, or `tmp/cancelled-plans/` if abandoned.

## Grain handoff

- If connected, read/update all planning artifacts in the supplied task folder, or `Development Artifacts/YYYY-MM-DD-<task>`; this overrides local-only storage in support skills.
- Pass the folder ID and storage rule to researchers/reviewers; sync outputs for agents without access and update status in the same artifacts.
- Keep needed local files and privacy limits; without Grain, continue locally silently.
