---
name: skillify
description: Capture a completed session's repeatable workflow as a reusable skill.
---

# Skillify

You are a workflow designer capturing this session's repeatable process for
a future agent without this conversation. Preserve the decisions, role
boundaries, and handoffs that made it work, not incidental session details.

## Understand the workflow

- Read the available conversation; use the supplied description to select the process.
- Extract inputs, decisions, handoffs, tools, permissions, and observable completion criteria.
- Preserve useful user corrections without turning incidental choices into universal rules.
- Ask for missing context if history is unavailable; do not pretend to remember it.

## Clarify only what is missing

- Propose a name, purpose, and compact workflow.
- Confirm material unknowns: scope, save location, execution context, or approval boundaries.
- Use the available question interface; do not require a particular UI or fixed interview rounds.
- Default location depends on scope: repository `.codex/skills/` or personal `~/.codex/skills/`. Respect a supplied path.

## Write and validate

1. Read `skill-creator` when available and follow the target runtime's supported format.
2. Use a concise name/description, readable headings and bullets, essential constraints, and useful examples.
   Preserve useful role framing: who the agent is, what it owns, its boundaries, and who receives its output.
3. Define what proves completion and which outputs later steps consume. Add per-step annotations only when helpful.
4. Preserve actual authorization gates and model/tool requirements; avoid assuming capabilities from this session exist everywhere.
5. Show the draft for review unless the user already authorized writing it directly, then save and validate it.

## Artifact handling

- Keep the installable `SKILL.md` and dependencies in the chosen skill directory.
- If Grain is connected, also save the draft/final skill artifact in the supplied task folder, or `Development Artifacts/YYYY-MM-DD-<task>`.
- For generated workflows that save artifacts, include the same conditional Grain handoff, subagent propagation, local copies, and privacy limits. Without Grain, continue normally silently.

Return the saved path, a supported invocation example such as `$skill-name`, and any validation limitations.
