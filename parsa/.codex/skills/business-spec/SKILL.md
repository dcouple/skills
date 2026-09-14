---
name: business-spec
description: Turn a business discussion brief and sourced context into a reviewed deliverable specification.
---

Read `.business/discussion/brief.md` and its relevant context, including
stakeholder research. Route missing or stale context to `business-context` or
`business-research-adversary` before specifying; do not invent it here.

Use `spec_base.md` to write `.business/specs/ready/spec.md`. Give a fresh writer
the goal, audience, supported claims, objections, acceptance criteria, reviewer
roles, and human gate. Link the source artifacts. Do not draft the deliverable.

Run `business-spec-reviewer` in fresh context and save its result to
`.business/reviews/spec-review.md`. Apply supported fixes or return to the
appropriate context/discussion stage. Finish with an approved spec or the
specific missing evidence or human decision.

When Grain is connected, read/update artifacts in the task folder (standalone:
`Development Artifacts/YYYY-MM-DD-<task>`) and pass its ID/storage rule to the
reviewer. Keep local files and privacy limits; otherwise continue locally silently.
