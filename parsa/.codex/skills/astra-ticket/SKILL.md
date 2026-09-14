---
name: astra-ticket
description: Take a GitHub ticket through Luna implementation, PR creation, optional Sol QA, three Luna reviews, and a final Astra review.
---

# Astra Ticket

Input: a GitHub issue URL or `owner/repo#number`.

## Model gate

- Before task work, verify the active orchestrator is GPT-6 Astra
  (`gpt-6-astra`) using authoritative runtime/session metadata.
- If the active model is different or cannot be verified, stop and explain.
  A configured default or the user's assertion is not verification.
- Except the QA agent below, all subagents must be GPT-6 Luna at effort `max`.
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
4. Before reviews, ask asynchronously whether to run end-to-end PR QA; state
   it will run after 60 seconds without a reply. Yes starts QA; no skips it.
   Use a timed, interruptible wait; do not treat a pending question as silence
   before 60 seconds elapse. If timed input is unavailable, wait for an answer.
   For QA, spawn GPT-5.6 Sol (`gpt-5.6-sol`) at reasoning effort `medium`
   using `pr-test-automation`; verify model support without substitutions.
   Delegate QA bug fixes and pushes to Luna Max, then have Sol rerun affected
   flows before reviews. Report blocked QA honestly; never call it a pass.
5. Run exactly three fresh Luna Max review subagents sequentially, each using
   the `review` skill on the current PR. After each review, delegate actionable
   fixes, checks, and pushes to Luna Max before starting the next review.
6. Review the resulting PR yourself as Astra, using the same `review` skill.
   Delegate any fixes to Luna Max, then verify those fixes yourself.
7. Return the PR URL, QA/check results, and unresolved findings. Do not merge.

Read `prepare-pr`, `pr-test-automation` (if running QA), and `review` when used.
The `review` skill may live
at `~/.claude/skills/review/` or `parsa/.claude/skills/review/` in dcouple/skills.
Read its referenced criteria too. If a required skill is missing, report it.
Keep the requested models and review sequence when a delegated skill has
different defaults. Stop and report a blocker if progress needs user input.
