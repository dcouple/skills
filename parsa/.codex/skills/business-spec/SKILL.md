---
name: business-spec
description: Turn a business discussion brief and sourced context into a reviewed deliverable specification.
---

# Business specification

## Rules

- Make the spec usable by a fresh writer without the conversation history.
- Ground claims in context; do not draft the deliverable.
- Ask for human input only when missing information or high-stakes judgment blocks progress.

## Read

Use supplied paths when present; these are the defaults:

- `.business/discussion/brief.md`.
- Relevant `.business/context/` evidence, including stakeholder research.
- [spec_base.md](spec_base.md) for the specification structure.

Route missing or stale context to `business-context` or `business-research-adversary` before specifying.

## Write

Save `.business/specs/ready/spec.md` with:

- Goal, audience, and intended reader response.
- Supported claims, source links, and stakeholder objections.
- Acceptance criteria, reviewer roles, and human gate.

## Review and finish

1. Run `business-spec-reviewer` in fresh context; save `.business/reviews/spec-review.md`.
2. Apply supported fixes or return to the appropriate context/discussion stage.
3. Return the approved spec, or the exact missing evidence or human decision.

## Grain handoff

- If connected, read/update artifacts in the task folder; standalone: `Development Artifacts/YYYY-MM-DD-<task>`.
- Pass its ID and storage rule to support agents; sync their outputs if they lack access.
- Keep needed local files and privacy limits; without Grain, continue locally silently.
