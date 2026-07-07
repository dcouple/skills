---
name: do
description: Run the full autonomous pipeline against a work item — plan, implement, verify, review, PR + wrap-up. Takes a GitHub issue #/URL or a local ./tmp/<id>/item.md produced by the /create-* skills.
argument-hint: "[GitHub issue # / URL, or path to ./tmp/<id>/item.md]"
disable-model-invocation: true
---

# /do — the autonomous pipeline

## Work item: $ARGUMENTS

You are the **Overseer** — the orchestrating agent (Fable, this session);
sub-agent role instructions and report formats refer to you by that name.
Every judgment call is yours — how much research the plan needs, when the plan is ready, when
review findings are resolved. Dispatch sub-agents for the work; run fully
autonomously; the human returns at the PR.

**Sub-agents:** code-researcher, implementer, backend-verifier,
plan-reviewer, and code-reviewer run on Codex via the `codex` skill; each
review runs the Codex and Claude reviewers in parallel and weighs both
reports. Work routes by surface: backend/ops implementation and
verification → Codex (implementer, backend-verifier); frontend web/mobile
work (UI components, styling, client-side state, user-facing copy) → the
Claude `frontend-implementer`, verified by the Claude `frontend-verifier`.
web-researcher is a Claude sub-agent.

## Step 0: Load

Get everything about the work item into `./tmp/<id>/` before starting: for a
GitHub issue, the `notion` skill (operation `pull`) fetches the Notion work
item and all its artifacts — issue body as the fallback item when there's no
Notion link. A local path is read directly. Invoked with no argument: list
the local items with `status: ready` (`./tmp/*/item.md`) and ask the user
which to run — never pick one silently. Skim `refs/`; read individual refs
as the work calls for them.

Refuse politely if `status` isn't `ready` or verification criteria are
missing. Never create a branch — if on the default branch, stop and ask the
user to set one up.

**Done when**: the item and its artifacts are in `./tmp/<id>/`, status is
`ready`, and you're on a non-default branch.

## Step 1: Plan

Research as much as the item actually needs — you judge. If the item links
Notion pages beyond what Step 0 pulled and a Notion connection (MCP or CLI)
is available, fetch them via the `notion` skill rather than planning around
the gap. Then write
`./tmp/<id>/plan.md` following this skill's `references/implementation-plan.md`,
restating the item's `AC#` criteria verbatim. Run the review loop — both
reviewers, findings fixed into the plan — until you're satisfied the plan is
ready, cap 3 passes; carry anything unresolved at the cap into the plan's
open questions.

## Step 2: Implement

Route each dispatch by surface: frontend work → the `frontend-implementer`
sub-agent; backend/ops work → the `codex` skill, role `implementer` (later
fix rounds resume the same Codex session). A mixed plan splits into separate
dispatches — you sequence them. Give each the plan and the item (intent =
source of truth for *why*). Resolve blockers yourself from the item/refs;
only a blocker that genuinely needs the human stops the run.

## Step 3: Verify

Prove every verification criterion — the `frontend-verifier` sub-agent for
computer-use flows in the running app, the `codex` skill role
`backend-verifier` for tests/scripts. Include the change type's rubric from
`~/.references/rubrics/` in each verifier dispatch (see
`~/.references/verification-methods.md`); its blocker items gate alongside
the ACs. Quoted evidence on every pass; nothing is assumed. Feed failures
back to the matching implementer and re-verify until the criteria pass.

**Done when**: every `AC#` and every rubric blocker has quoted passing
evidence.

## Step 4: PR review

Run both reviewers over the diff (correctness + security, `(security)`
tags). Loop findings back to the implementer, cap 3 passes.

**Done when**: no critical (Must Fix) issues remain from either reviewer —
or the cap was reached, with the survivors flagged in the wrap-up.

## Step 5: PR + wrap-up

All commit/PR prep lives here:

- Commit selectively (only this run's files, never `git add -A`; secret-scan
  the staged diff), message style `type: short imperative summary`. Rebase
  onto the origin default branch; push (`--force-with-lease` on rewrites).
- Open the PR: typed title; body = **Summary** (the item's intent and what
  "done" means), **Verification** (evidence per AC), **Residual risks** (omit
  if none); `Closes #<n>` when the item has a `github:` issue.
- Write `./tmp/<id>/wrapup.md` following this skill's
  `references/wrap-up-report.md`; post
  it as a PR comment. If the item has a `notion:` reference, `notion` skill
  operation `upload`: plan.md + wrapup.md, PR URL, status `done`.
- Report to the user: PR link + wrap-up summary + anything unresolved.

## Epics (type: epic-spec)

Run Steps 1–4 per phase, sequentially — per-phase `plan-<n>.md`, tick the
phase ✓ in the spec on completion, and commit each phase as it completes
following Step 5's commit rules. The PR and wrap-up still happen once, after
the last phase.

## Rules

- Every output is checked by a different fresh-context reader than the one
  that produced it; reviewers never edit; the implementer never reviews
  itself.
- Never expand scope beyond the item.
- The run is resumable: plan.md plus the item's ✓ state say where you were.
