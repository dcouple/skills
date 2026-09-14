---
name: business-artifact
description: Draft and review a business deliverable from an approved specification.
---

Read `.business/specs/ready/spec.md`, its review, and the context needed to
support the deliverable. Write `.business/artifacts/draft.md` in the requested
format and maintain `claim-evidence-ledger.md` beside it:

| Claim | Evidence | Status | Risk | Fix |
|---|---|---|---|---|

Ground claims, figures, dates, and commitments in the sources; flag missing
evidence rather than inventing it. Run `business-artifact-reviewer` in fresh
context, saving its result to `.business/reviews/artifact-review.md`. Apply
concrete fixes and resolve them before handing off; bring required human gates
or material unknowns to the user. Return the draft, ledger, review, and next step.

If Grain is connected, read/update these artifacts in the task's Grain folder
(standalone: `Development Artifacts/YYYY-MM-DD-<task>`). Pass that folder and
storage rule to reviewers; sync their files if they lack access. Keep needed
local copies and privacy limits; without Grain, continue locally silently.
