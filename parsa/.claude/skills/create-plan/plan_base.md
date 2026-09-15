# Implementation Plan

- Fill in concrete evidence and decisions; remove template instructions before handoff.
- Keep the core sections below. Add architecture, pseudocode, or domain-specific details only where they clarify the work.

## Summary

- What ships and which areas change.

## Intent / Why

- User outcome and why it matters.
- Constraints, non-goals, and what must remain true.
- Observable success criteria.

## Source Artifacts

- Intent brief and research dossier paths/links.
- Include Grain links when connected.

## Verified Repo Truths

Group by relevant area, such as state, entrypoints, UI, or integrations.

- Fact: current-state claim.
  - Evidence: verified `file:line` reference.
  - Implication: why the fact matters.
  - Search Evidence: searched locations, query, and results for absence claims only.

## Locked Decisions

- Settled product or design choices; do not reopen them without new evidence.

## Known Mismatches / Assumptions

- Mismatch or assumption, evidence, and resolution; write `None` if absent.

## Critical Codebase Anchors

- Verified paths and the patterns, invariants, or gotchas they demonstrate.
- Relevant external documentation with URLs and applicable versions.

## Files Being Changed

- List or tree of verified paths marked `MODIFY`, `CREATE`, or `DELETE`.
- Distinguish existing files from proposed files.

## Reconciliation Notes

- What was imported from the dossier, resolved through rechecking, or deliberately excluded.

## Delta Design

For each affected area:

- Existing behavior.
- Proposed change and rationale.
- Integration, compatibility, migration, and failure risks where applicable.

## Architecture / Key Pseudocode

- Show how the pieces fit together; a short explanation is enough for a simple change.
- Include pseudocode only for tricky logic, using the project's language and conventions.

## Tasks

Repeat per task in dependency order:

- Goal and affected files.
- Existing pattern to follow, if useful.
- Important caveats or dependencies.
- Observable definition of done.

## Validation

- Record the project's actual commands and expected results: for example, `pytest`, `cargo test`, or a repository-defined lint/typecheck script.
- Include focused regression coverage and manual scenarios proportional to the change.
- Distinguish automated checks from actions requiring human approval or external access.

## Open Questions

- Unresolved decisions or missing evidence; write `None` if absent.

## Deprecated / Removed Code

- In-scope cleanup and compatibility implications, if any.

## Handoff checks

- Evidence and paths verified; facts separated from proposals.
- Intent, integration points, and required constraints preserved.
- No placeholder paths or unresolved factual blockers.
- Plan, brief, dossier, and review links available to the implementer.
