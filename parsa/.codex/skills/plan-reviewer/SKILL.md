---
name: plan-reviewer
description: Review an implementation plan against repository evidence, user intent, and supporting research before coding.
---

# Plan review

## Read

- The plan and applicable repository instructions.
- Supporting brief as the authority for intent; research dossier as evidence to verify.
- Referenced code and current integration points, not just filenames.

## Review

- Repo accuracy: existing paths, line anchors, contracts, and runtime wiring.
- Fact purity: `Fact / Evidence / Implication`, plus search evidence for absence claims; no proposals presented as facts.
- Intent: why, locked decisions, non-goals, and success criteria survive planning.
- Reconciliation: useful research was incorporated without unsupported claims or unnecessary duplication.
- Completeness: dependency order, edge cases, error handling, and project-appropriate validation.
- Simplicity: reuse existing patterns where they fit; flag unjustified architecture or compatibility changes.

## Useful findings

- “Task 3 consumes the schema from Task 1, so these tasks cannot run in parallel.”
- “The plan adds an error helper, but this existing helper already covers the behavior.”
- “The view lacks loading and empty states; follow the nearest comparable view.”

## Return

- Numbered findings ordered by severity, each with what, where, evidence, and a concrete suggestion.
- Prioritize factual and intent blockers over stylistic alternatives; say when no material findings remain.
- Return unresolved product decisions to the coordinator instead of asking the user mid-review.
- If saving a review and Grain is connected, use the shared task folder, or `Development Artifacts/YYYY-MM-DD-<task>`. Keep needed local copies and privacy limits; otherwise continue normally silently.
