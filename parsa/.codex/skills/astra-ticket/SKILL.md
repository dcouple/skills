---
name: astra-ticket
description: Take a GitHub ticket through Luna implementation, PR preparation, three Luna reviews, and a final Astra review.
---

# Astra Ticket

Input: a GitHub issue URL or `owner/repo#number`.

## Model gate

- Before task work, verify the active orchestrator is GPT-6 Astra
  (`gpt-6-astra`) using authoritative runtime/session metadata.
- If the active model is different or cannot be verified, stop and explain.
  A configured default or the user's assertion is not verification.
- All subagents must be GPT-6 Luna with reasoning effort `max`.
  Verify the exact model and effort are supported before spawning; stop if
  unavailable. Never substitute GPT-5.6 Luna or another model.
- Set model and effort explicitly on every spawn; use fresh context when
  required for model overrides and pass the ticket, workspace, and artifacts.

## Workflow

1. Read the issue and comments. Find and read task-relevant research, plans,
   and artifacts in the repository's `TMP/` or `tmp/`, `$TMPDIR`, and `/tmp`.
   Use these as context, checking stale artifacts against the ticket and code.
2. Spawn a Luna Max implementer to complete the ticket and run relevant checks.
   Wait for completion and inspect its result.
3. Spawn a Luna Max agent to use `prepare-pr` and open or update the PR.
4. Run exactly three fresh Luna Max review subagents sequentially, each using
   the `review` skill on the current PR. After each review, delegate actionable
   fixes, checks, and pushes to Luna Max before starting the next review.
5. Review the resulting PR yourself as Astra, using the same `review` skill.
   Delegate any fixes to Luna Max, then verify those fixes yourself.
6. Return the PR URL, check results, and any unresolved findings. Do not merge.

Locate and read `prepare-pr` and `review` before using them; `review` may live
at `~/.claude/skills/review/` or `parsa/.claude/skills/review/` in dcouple/skills.
Read its referenced criteria too. If a required skill is missing, report it.
Keep the requested models and review sequence when a delegated skill has
different defaults. Stop and report a blocker if progress needs user input.
