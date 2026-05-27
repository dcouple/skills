---
name: business-context
description: Build the filesystem business context base for a stakeholder-facing task before discussion, spec, or artifact work.
---

Rules:
- No drafting.
- No spec creation.
- Pull relevant context from connected apps, MCP/tools, local files, prior deliverables, and user-provided material.
- Normalize context into markdown files under `.business/context/`.
- Separate facts, assumptions, unknowns, constraints, and sources.
- If context is missing, say what is missing instead of guessing.

Read:
- user request / ticket / transcript / task description
- available files and app/tool results

Write:
- `.business/context/context.md`
- `.business/context/source-index.md`
- `.business/context/known-facts.md`
- `.business/context/assumptions-unknowns.md`
- `.business/context/constraints.md`

Output:
- source inventory
- known facts
- assumptions
- unknowns
- constraints
- suspected real business goal
- recommended next step: research-adversary or discussion

Principle: if it is not in the business context base, it does not exist to the agent.
