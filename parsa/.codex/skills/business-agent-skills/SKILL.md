---
name: business-agent-skills
description: Coordinate a business deliverable from context and discussion through specification, drafting, review, and release preparation.
---

# Business workflow

## Rules

- Run each stage in fresh context with a saved handoff.
- Settle the goal and important decisions with the user during discussion.
- Continue authorized work without repeating approval requests at every stage.
- Build context before discussion or specification; stakeholder research belongs to context.
- Dispatch support skills as fresh subagents with the relevant handoff paths.
- Keep the full sequence for high-stakes external work; shorten it for trivial edits or exact copying.

## Stages

Use supplied artifact paths when present; `.business/` is the default layout.

| Stage | Handoff under `.business/` |
|---|---|
| `business-context` | `context/`: context, source-index, known-facts, assumptions-unknowns, constraints |
| `business-research-adversary` | `context/research-adversary.md` |
| `business-discussion` | `discussion/brief.md` |
| `business-spec` + `business-spec-reviewer` | `specs/ready/spec.md`, `reviews/spec-review.md` |
| `business-artifact` + `business-artifact-reviewer` | `artifacts/draft.md`, claim-evidence ledger, `reviews/artifact-review.md` |
| `business-prepare-release` (when preparing delivery) | `artifacts/final.md`, `reviews/release-checklist.md` |

## Finish

- Return the artifact, review status, and remaining decisions.
- Surface unsupported commitments and required human gates.
- Preparing an artifact does not authorize sending or publishing it.

## Grain handoff

- When connected, read/update all workflow artifacts in the supplied Grain folder, or `Development Artifacts/YYYY-MM-DD-<task>`; this overrides local-only storage in invoked skills.
- Pass its ID and storage rule to every stage; sync outputs for agents without access.
- Keep local working files and privacy limits. Without Grain, continue locally silently.
