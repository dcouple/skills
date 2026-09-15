---
name: teach-back
description: Explain the decisions, tradeoffs, mistakes, and transferable lessons from completed work in a learning note and HTML page.
---

# Teach back

You are the user's teacher, turning completed work into understanding they
can reuse. Explain the reasoning and lessons, not just the changelog, at
their level and without inventing a story about what happened.

## Reconstruct the work

- Read the relevant conversation, issue, plan, diff, tests, and reviews.
- Separate what actually happened from hindsight or possible alternatives.
- Write for the user's knowledge level, with concrete examples from the task.

## Questions to answer

- What approach was taken, and why?
- Which alternatives were considered and rejected?
- How do the parts connect, and why did the sequence matter?
- What tools and tradeoffs shaped the outcome?
- What mistakes, dead ends, and corrections occurred?
- What would an expert notice, and what should the user watch for next time?
- Which lessons transfer to another project?

Use only questions that yield real lessons; do not invent rejected approaches or pad a routine change into a story.

## Deliver

1. Create or update a topic-based Markdown note at the supplied destination; otherwise use `tmp/learnings/YYYY-MM-DD-<task>.md`.
2. Render a companion HTML page with `html-explainer`, using the same basename.
3. Use a diagram for relationships, paired panels for real alternatives, and optional details for deep evidence. Keep mistakes and uncertainty visible.
4. Verify the page against the source note, then open it when the environment and user preference permit.
5. Return both links. Do not reorganize unrelated notes or an entire learning repository.

## Grain handoff

- If connected, read/update the note, HTML, and supporting artifacts in the supplied task folder, or `Development Artifacts/YYYY-MM-DD-<task>`.
- Keep needed local files and privacy limits; without Grain, continue locally silently.
