---
name: astra-ticket
description: Take a GitHub ticket through Astra planning, Luna implementation, PR creation, optional Sol QA, three Luna reviews, and a final Astra review.
---

# Astra Ticket

Input: a GitHub issue URL or `owner/repo#number`.

- Before task work, verify the active orchestrator is GPT-6 Astra
  (`gpt-6-astra`) using authoritative runtime/session metadata.
- If the active model is different or cannot be verified, stop and explain.
  A configured default or the user's assertion is not verification.
- Except QA, use `gpt-5.6-luna` at `max` for every subagent.
  Verify model/effort support before spawning; stop if unavailable.
  Never substitute another model.
- Set model and effort explicitly on every spawn; use fresh context when
  required for model overrides and pass the ticket, workspace, and artifacts.

1. Read the issue and comments. Find and read task-relevant research, plans,
   and artifacts in the repository's `TMP/` or `tmp/`, `$TMPDIR`, and `/tmp`.
   Use these as context, checking stale artifacts against the ticket and code.
2. As Astra, read `simple-plan` and use its planning steps to investigate and
   produce a concise plan. Preserve the ticket's intent, constraints, and scope.
   Autonomously derive detailed specs: files, changes, dependencies, edge cases,
   acceptance criteria, and checks. Save the plan/specs under task-specific `tmp/`.
   This workflow authorizes proceeding without `simple-plan`'s approval pause.
3. Spawn Luna Max implementers with the ticket, plan, specs, and artifacts;
   sequence dependent tasks, wait for completion, and inspect work/check results.
4. Spawn a Luna Max agent to use `prepare-pr` and open or update the PR.
5. Before reviews, ask asynchronously whether to run end-to-end PR QA; state
   it will run after 60 seconds without a reply. Yes starts QA; no skips it.
   Use a timed, interruptible wait; do not treat a pending question as silence
   before 60 seconds elapse. If timed input is unavailable, wait for an answer.
   For QA, spawn GPT-5.6 Sol (`gpt-5.6-sol`) at reasoning effort `medium`
   using `pr-test-automation`; verify model support without substitutions.
   Delegate QA bug fixes and pushes to Luna Max, then have Sol rerun affected
   flows before reviews. Report blocked QA honestly; never call it a pass.
6. Run exactly three fresh Luna Max review subagents sequentially, each using
   the `review` skill on the current PR. After each review, delegate actionable
   fixes, checks, and pushes to Luna Max before starting the next review.
   For all reviews, use `COMMENT` when authenticated as the PR author.
7. Review the resulting PR yourself as Astra, using the same `review` skill.
   Delegate any fixes to Luna Max, then verify those fixes yourself.
8. Return the PR URL, QA/check results, and unresolved findings. Do not merge.

Read `prepare-pr`, `pr-test-automation` (if running QA), and `review` when used.
Find `review` in `~/.claude/skills/review/` or dcouple/skills's `parsa/.claude/skills/review/`.
Read its referenced criteria too. If a required skill is missing, report it.
Follow this workflow's model/sequence overrides; stop for genuine user decisions.
