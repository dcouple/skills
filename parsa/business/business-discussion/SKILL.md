---
name: business-discussion
description: Have a business-goal discussion using the context base without drafting the deliverable.
---

Role: Main human-in-the-loop stage. Before discussing, make sure the context base exists — never discuss on empty context.

Rules:
- No artifact drafting.
- Ensure context first: if `.business/context/` is missing or empty, run or request `business-context`; for serious work also run or request `business-research-adversary`. The discussion must be grounded in real internal + external context, not guesses.
- Read the context files, then probe only high-leverage uncertainties.
- Prefer concrete options and recommendations over broad questionnaires.
- Clarify the decision, audience, stakes, constraints, and non-goals.

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
