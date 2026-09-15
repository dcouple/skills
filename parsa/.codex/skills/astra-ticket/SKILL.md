---
name: astra-ticket
description: Take a GitHub ticket through Astra planning, Luna implementation, PR creation, optional Sol QA, Luna/Astra reviews, and bounded QA revalidation.
---

# Astra Ticket

Input: a GitHub issue URL or `owner/repo#number`.

- Before task work, verify the active orchestrator is GPT-6 Astra
  (`gpt-6-astra`) using authoritative runtime/session metadata.
- Stop if different or unverified; defaults and user assertions are not proof.
- Except QA, use `gpt-5.6-luna` at `max` for every subagent.
  Verify model/effort support before spawning; stop if unavailable.
  Never substitute another model.
- Set model and effort explicitly on every spawn; use fresh context when
  required. Pass applicable workflow overrides, ticket, workspace, and artifacts.
- Reuse passing checks at the same commit; after changes, rerun affected checks unless a concrete finding requires broader validation.
- Before each review and final handoff, inspect human/bot feedback and CI; address actionable findings, report unfinished checks after five minutes, and claim ready only with actionable threads resolved and required checks passing on the final SHA.
- For low-risk changes whose correctness is quickly verifiable with deterministic checks—such as copy, translations, docs, formatting, metadata, or simple config—mark internal Luna/Astra reviews (steps 6–8) skipped and default step 5 QA to skipped unless requested; retain applicable checks, affected-flow retests, final-head CI, and available GitHub feedback handling.

1. Read the issue/comments and relevant artifacts in repo `TMP/` or `tmp/`,
   `$TMPDIR`, and `/tmp`; check stale context against the ticket and code.
   If Grain is connected, use `grain` to reuse the linked task workspace. For new work, honor explicit destinations; otherwise use `Development Artifacts/<org>/<repo>` in the intended Grain organization. Confirm any ambiguous organization or repository.
   Verify its organization, folder, and intended audience; include the location beside its link. Update the task workspace name for the PR through supported operations, retaining its ID and the shared repository folder. If Grain is unavailable, silently continue locally.
   When Grain is connected, keep all development artifacts in one canonical task workspace in that folder, retain local copies, and pass its workspace ID to every subagent.
2. As Astra, read `simple-plan` and use its planning steps to investigate and
   produce a concise plan. Preserve the ticket's intent, constraints, and scope.
   Use `create-ticket`'s intent-capture guidance to ground the reported sequence, expected/actual behavior, consequence, and evidence gaps. Create or refresh the linked human-readable brief with the proposed approach and meaningful tradeoffs before coding; preserve required local plan/spec files.
   Reuse the ticket's recorded Socrates verdict when its premise and supporting evidence still hold. If absent or materially changed, dispatch a fresh Luna Max agent using [Socrates](../create-ticket/references/socrates.md) with the ticket, draft plan, and repository evidence. Resolve material findings with the user before implementation; if an existing solution meets the agreed outcome, end with the evidence and guidance.
   Autonomously derive detailed specs: files, changes, dependencies, edge cases,
   acceptance criteria, and checks. Save the plan/specs under task-specific `tmp/`.
   This workflow authorizes proceeding without `simple-plan`'s routine approval pause once premise findings are resolved.
3. Spawn Luna Max implementers with the ticket, plan, specs, and artifacts;
   sequence dependent tasks, wait for completion, and inspect work/check results.
4. Spawn a Luna Max agent to use `prepare-pr` and open or update the PR.
   Pass explicit code/branch-preparation and draft-PR overrides to `prepare-pr`; after QA (or an explicit skip) and internal reviews finish, mark ready, then check any triggered automated reviews and final-head CI and address actionable feedback before handoff.
5. Before reviews, ask asynchronously whether to run end-to-end PR QA; state
   it will run after 60 seconds without a reply. Yes starts QA; no skips it.
   Use a timed, interruptible wait; do not treat a pending question as silence
   before 60 seconds elapse. If timed input is unavailable, wait for an answer.
   For QA, spawn GPT-5.6 Sol (`gpt-5.6-sol`) at reasoning effort `medium`
   using `pr-test-automation`; verify model support without substitutions.
   Delegate QA bug fixes and pushes to Luna Max, then have Sol rerun affected
   flows before reviews. Report blocked QA honestly; never call it a pass.
   Capture QA screenshots; when Grain is connected, save and verify media/reports there instead of release assets; otherwise follow `pr-test-automation`'s durable-publication behavior.
   Keep the PR self-contained using `prepare-pr`'s exposition rules, with behavior, tested SHA, QA verdict, limitations and named evidence links; when using Grain, lead with key screenshots/videos, then longer artifacts.
   Return the same verified evidence link in the final handoff; explicitly report unavailable capture or publication rather than claiming upload.
6. Run up to three fresh Luna Max reviews sequentially; stop after a clean review. Use
   the `review` skill on the current PR. After each review, delegate actionable
   fixes, checks, and pushes to Luna Max before starting the next review.
   For all reviews, use `COMMENT` when authenticated as the PR author.
7. Review the resulting PR yourself as Astra, using the same `review` skill.
   Delegate any fixes to Luna Max, then verify those fixes yourself.
8. If review fixes invalidate completed QA, Sol retests affected flows, then
   one fresh Luna Max agent reviews the fixes covered by that rerun.
   Report remaining findings; do not restart the review loops.
9. Return the PR URL, QA/check results with tested commits, and open findings. Do not merge.
   After an authorized merge or when revisiting a merged PR, confirm GitHub reports `MERGED`; when Grain is connected, mark the task complete and move only its workspace to the repository's completed-work destination if configured and supported. Preserve IDs/shares and the shared repository folder, verify the destination and links, and report unavailable moves.
   When Grain is connected, update the same human-readable brief with before/after behavior and verified results from the published PR after QA (or an explicit skip), reviews and final-head CI. Preserve original intent, sources, and decision history alongside the current result; verify matching content and reciprocal evidence links, then open Grain last.

Read `create-ticket` for intent capture, the bundled Socrates role for the premise check, and `prepare-pr`, `pr-test-automation` (if running QA), and `review` when used. Preserve required tracker publication, local paths, and evidence contracts alongside Grain.
Find `review` in `~/.claude/skills/review/` or dcouple/skills's `parsa/.claude/skills/review/`.
Read referenced criteria; report missing skills. These workflow overrides take precedence.
