---
name: create-plan
description: "Produce an evidence-backed implementation plan for a substantial feature or change."
argument-hint: "[feature description or ticket reference]"
allowed-tools: Read, Grep, Glob, WebFetch, WebSearch, Write, Task
---

# Create Plan

Produce a plan another agent can execute without reconstructing the conversation.
Preserve the user's why, scope, locked decisions, non-goals, and success criteria.
A plan describes the requested result; a template does not expand that scope.

## Inspect the affected area

Open the relevant entrypoints, contracts, integrations, and existing patterns.
Broaden research when a dependency or unresolved question calls for it. Do not
map the entire repository or read unrelated docs as a prerequisite to drafting.
Reuse evidence from the current checkout unless its source changed.

- Verify existing paths and line anchors before citing them. Mark proposed paths
  as new and never present a proposed design as a current repository fact.
- In `Verified Repo Truths`, retain `Fact`, `Evidence`, and `Implication` for each
  material claim. Absence claims also need scoped `Search Evidence`.
- Record mismatches with the brief and resolve factual ones from the repository.
  Ask only about decisions that materially change intent, safety, or scope.
- Consult primary documentation when external or version-sensitive behavior
  changes the plan; save the useful citation and conclusion.

## Write the implementation contract

Use [plan_base.md](plan_base.md) for the detailed format. Fill applicable
sections; omit irrelevant example sections and placeholders. Keep these facts
available to implementers and reviewers:

- Intent / Why, Locked Decisions, and success criteria.
- Source Artifacts: the canonical brief or a compact intent snapshot; link a
  research dossier if one was needed. If intent lives in the plan, say so.
- Verified Repo Truths, Critical Codebase Anchors, and Known Mismatches /
  Assumptions with evidence separate from proposals.
- Files Being Changed, dependency-ordered Tasks, relevant design decisions,
  integration points, and observable completion conditions.
- Validation: commands derived from this repo, the behavior each proves, and
  required human/environment steps. Add regression tests when a changed
  behavior or failure risk needs them; avoid speculative test scaffolding.
- Reconciliation Notes and Open Questions where applicable.

Create a separate research dossier only when substantial research or a fresh
handoff benefits from it. Keep it selective; reconcile useful anchors and
conflicts into the plan instead of forcing readers to load duplicate prose.
Preserve necessary compatibility when existing consumers require it; record the
reason rather than introducing a speculative abstraction.

Save the plan in `./tmp/ready-plans/YYYY-MM-DD-description.md`. Put optional
supporting files in `./tmp/plan-artifacts/`. Keep scratch out of commits unless
the repository explicitly tracks these artifacts.

## Review and finish

Use the Claude `plan-reviewer` agent (`subagent_type: "plan-reviewer"`).
When an independent Codex lane is required or materially useful and available,
run it alongside the Claude lane and wait for both.
Merge findings, resolve factual blockers and in-scope corrections, and rerun
only the review affected by a material revision. A clean pass ends review;
extra passes need a concrete unresolved question, not an arbitrary quota.

For a planning-only request or an explicit review pause, return the plan link,
key decisions, and any genuine questions. For an already-authorized end-to-end
request, hand the reviewed plan to `implement` and continue within that grant.
A standing run-continuously grant persists across this handoff. Do not mark a
plan ready while a factual blocker remains, or interpret readiness as authority
for merge, release, deployment, production changes, or expanded scope.
