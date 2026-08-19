---
name: discussion
description: Have an implementation-focused discussion about a feature, bug, or approach without making code changes. Use when the goal is to think through options before planning or coding.
---

# Discussion

This skill is for conversation only.

Rules:
- Do not edit, create, or delete project files.
- Read code as needed to ground the discussion in the real codebase.
- Be opinionated about tradeoffs, but distinguish fact from recommendation.

Workflow:
1. Clarify the topic and desired outcome.
2. Inspect relevant code paths if the discussion depends on current behavior.
3. Before responding to the user, reference the installed `rewrite-simply` skill
   and apply it to the discussion response.
4. Present concrete options, constraints, and tradeoffs.
5. Ask targeted follow-up questions when needed.
6. End with a recommended next step, usually `create-plan`, `simple-plan`, `investigate`, or implementation.

Prototype before you ask:

Classify every fork question before you surface it in step 5. If the answer is
observable by running something — behavior, timing, output, perf, layout —
build the cheapest throwaway probe outside the project tree, run it, and
present the result with a recommendation instead of the question. Reserve
questions for genuine product or preference calls no experiment can settle. A
probe usually answers faster than a human, and it hands them a result to react
to instead of a decision to make.
