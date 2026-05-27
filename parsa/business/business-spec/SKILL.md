---
name: business-spec
description: Create a business deliverable spec from the discussion brief and existing context base, then run spec review.
---

Role: This is the business equivalent of `/plan`. After the human-heavy `business-discussion` stage, this skill should do as much of the remaining spec work automatically as possible.

Rules:
- MUST NOT draft the artifact.
- MUST create a spec clear enough that a fresh agent can produce the artifact without reading the whole conversation.
- MUST ground every claim in context files.
- MUST include research-adversary inputs explicitly.
- MUST define acceptance criteria and reviewer panel.
- Stop for human input only when context/spec gaps block progress or high-stakes judgment is required.

Coordinate support skills:
- Context and research-adversary are context steps that already ran before discussion. business-spec MUST NOT produce them.
- If context or research-adversary is missing or stale, you MUST send the workflow back to context-building (`business-context` / `business-research-adversary`). NEVER produce them here.
- After drafting the spec, you MUST run or request `business-spec-reviewer`.
- If review returns revise/build-more-context, you MUST patch the spec or send the workflow back to the right support stage.

Read:
- `.business/context/*.md`
- `.business/discussion/brief.md`
- `spec_base.md`

Write:
- `.business/specs/ready/spec.md`
- `.business/reviews/spec-review.md` via `business-spec-reviewer`

Output:
- ready spec if approved
- or a concise blocker report with the exact missing context/human decision needed

Use `spec_base.md` for the spec structure.
