---
name: business-artifact
description: Draft and review a business deliverable from an approved specification.
---

# Business artifact

## Read

Use supplied input/output paths when present; these are the default inputs:

- Approved `.business/specs/ready/spec.md` and `.business/reviews/spec-review.md`.
- Relevant context and stakeholder research under `.business/context/`.

## Draft

- Write `.business/artifacts/draft.md` in the requested format.
- Ground claims, figures, dates, and commitments in sources; flag missing evidence.
- Maintain `claim-evidence-ledger.md` beside the draft:

| Claim | Evidence | Status | Risk | Fix |
|---|---|---|---|---|

## Review and finish

1. Run `business-artifact-reviewer` in fresh context; save `.business/reviews/artifact-review.md`.
2. Apply concrete fixes before handoff; bring required human gates or material unknowns to the user.
3. Return the draft, ledger, review, and next step.

## Grain handoff

- If connected, read/update these artifacts in the task's Grain folder; standalone: `Development Artifacts/YYYY-MM-DD-<task>`.
- Pass the folder and storage rule to reviewers; sync their outputs if they lack access.
- Keep needed local copies and privacy limits; without Grain, continue locally silently.
