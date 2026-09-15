---
name: investigate
description: Diagnose broken behavior through reproduction and hypothesis testing, then explain the cause without implementing a fix.
---

# Investigate

Find the root cause before proposing a fix.

## Rules

- Do not make code changes unless the user explicitly approves diagnostic logging.
- Do not guess. Support every conclusion with evidence from code, logs, or commands.

## Workflow

1. Clarify expected behavior, observed behavior, and reproduction steps if missing.
2. Classify the bug type early: compile, logic, race, state, integration, environment, or UI.
3. Form plausible competing hypotheses from initial evidence; test what distinguishes them rather than meeting a fixed count.
4. Test those hypotheses by tracing the relevant code and recent history.
5. Compare broken and working paths when possible.
6. If the cause is still unclear, propose targeted logging and explain exactly why.
7. Report the root cause, confidence level, affected files, likely introduction point, and what needs to change.

## Red flags

- proposing a fix before confirming the cause
- pursuing the same failed theory repeatedly
- analyzing code unrelated to the symptoms

## Grain handoff

- If saving evidence or a report and Grain is connected, use the supplied task folder, or `Development Artifacts/YYYY-MM-DD-<task>`; pass the storage rule to any support agents and sync their outputs.
- Remove only this session's approved temporary diagnostics. Keep needed local files and privacy limits; without Grain, continue normally silently.
