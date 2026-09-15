---
name: business-discussion
description: Clarify a business deliverable's goal, audience, and decisions from gathered context before drafting.
---

# Business discussion

## Read

- Read the supplied context; default: `.business/context/` facts, constraints, unknowns, and stakeholder research.
- If context is missing, run `business-context` first; include `business-research-adversary` for serious work.

## Discuss

- Use evidence and concrete options to settle material unknowns; do not reconfirm settled decisions.
- Do not draft the deliverable at this stage.
- Useful questions:
  - Who is the primary reader, and what should change for them?
  - What format fits that goal, and what is out of scope?
  - What constraints, stakes, or unresolved decisions affect the work?

## Write

Save the brief at the supplied path, or `.business/discussion/brief.md`, with:

- Confirmed goal, audience, and intended reader response.
- Format, key decisions, constraints, and non-goals.
- Remaining questions, risks, and recommended next step.

## Grain handoff

- If connected, read/update artifacts in the task's shared folder; standalone: `Development Artifacts/YYYY-MM-DD-<task>`.
- Pass its ID and storage rule to support agents; sync their outputs if they lack access.
- Keep needed local files and privacy limits; without Grain, continue locally silently.
