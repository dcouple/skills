---
name: business-discussion
description: Have a business-goal discussion using the context base without drafting the deliverable.
---

Role: Main human-in-the-loop stage. Before discussing, you MUST make sure the context base exists. NEVER discuss on empty context.

Rules:
- MUST NOT draft the artifact.
- REQUIRED — ensure context first: if `.business/context/` is missing or empty, you MUST run or request `business-context`; for serious work you MUST also run or request `business-research-adversary`. The discussion MUST be grounded in real internal + external context, never guesses.
- MUST read the context files before probing, then probe only high-leverage uncertainties.
- Prefer concrete options and recommendations over broad questionnaires.
- MUST clarify the decision, audience, stakes, constraints, and non-goals.

Read:
- `.business/context/context.md`
- `.business/context/research-adversary.md`
- `.business/context/known-facts.md`
- `.business/context/assumptions-unknowns.md`
- `.business/context/constraints.md`

Write:
- `.business/discussion/brief.md`

Output:
- confirmed goal
- confirmed audience/stakeholders
- intended reader transformation
- artifact type
- key decisions
- unresolved questions
- risks/watchouts
- recommended next step
