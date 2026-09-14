---
name: business-agent-skills
description: Coordinate a business deliverable from context and discussion through specification, drafting, review, and release preparation.
---

# Business workflow

Run each stage in fresh context with a saved handoff. The user settles the
goal and important decisions during discussion; continue through the remaining
authorized work without asking for approval again at every stage.

| Stage | Handoff under `.business/` |
|---|---|
| `business-context` | `context/`: context, source-index, known-facts, assumptions-unknowns, constraints |
| `business-research-adversary` | `context/research-adversary.md` |
| `business-discussion` | `discussion/brief.md` |
| `business-spec` + `business-spec-reviewer` | `specs/ready/spec.md`, `reviews/spec-review.md` |
| `business-artifact` + `business-artifact-reviewer` | `artifacts/draft.md`, claim-evidence ledger, `reviews/artifact-review.md` |
| `business-prepare-release` | `artifacts/final.md`, `reviews/release-checklist.md` |

Build context before discussion or specification. External stakeholder research
belongs to context, not the spec stage. Dispatch the support skills as fresh
subagents with the relevant handoff paths. Keep the full sequence for high-stakes
external work; trivial edits or exact copying can use a shorter path without
manufacturing empty stage artifacts.

Return unresolved product decisions, unsupported commitments, and required
human gates to the user. Preparing the final artifact does not authorize sending
or publishing it. Finish with the artifact, review status, and remaining decisions.

If Grain is connected, read and keep these artifacts updated in one
`Development Artifacts/YYYY-MM-DD-<task>` folder; pass its ID and this storage
rule to every stage. Keep local working files and privacy limits. Without Grain,
continue with `.business/` silently.
