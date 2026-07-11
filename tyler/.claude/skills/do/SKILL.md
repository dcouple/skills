---
name: do
description: Run the full autonomous pipeline against a work item — plan, implement, verify, PR, post-PR review + QA, wrap-up. Takes a GitHub issue #/URL or a local ./tmp/<id>/item.md produced by the /create-* skills.
argument-hint: "[GitHub issue # / URL, or path to ./tmp/<id>/item.md]"
disable-model-invocation: true
---

# /do — the autonomous pipeline

## Work item: $ARGUMENTS

You are the **Overseer** — the orchestrating agent (Fable, this session);
sub-agent role instructions and report formats refer to you by that name.
Every judgment call is yours — which lane the item takes, how much research
the plan needs, when the plan is ready, when review findings are resolved. Dispatch sub-agents for the work; run fully
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

Set the lane first, and record it in `plan.md`'s frontmatter:

- **light** — one surface, a handful of files, low blast radius, no
  schema/auth/async changes. No dossier; research directly. Review loops
  this run cap at 1 pass instead of 3.
- **full** — everything else. Epics are always full.

Full lane: dispatch the `codex` skill, role `code-researcher`, to map the
territory the plan builds on — critical codebase anchors, patterns to
reuse, load-bearing gotchas, exact `file:line` evidence for every claim.
When the item leans on an external library, framework, or API the repo
alone can't answer, dispatch the `web-researcher` sub-agent in parallel —
its cited findings (URL + why + the critical insight) go into the dossier
too. Save the combined findings as `./tmp/<id>/refs/research-dossier.md` —
the researchers report in-conversation; you persist the dossier.
Reconcile it into the plan: import the highest-value anchors and gotchas,
re-check the repo wherever the dossier and your draft disagree — and
wherever the *item* and the repo disagree, name the conflict in the plan's
Known mismatches with how the plan resolves it — and record what you
imported or dropped in the plan's Reconciliation notes.

Research beyond that as the item actually needs — you judge. If the item links
Notion pages beyond what Step 0 pulled and a Notion connection (MCP or CLI)
is available, fetch them via the `notion` skill rather than planning around
the gap. Then write
`./tmp/<id>/plan.md` following this skill's `references/implementation-plan.md` —
its evidence contract is binding: facts live in Verified repo truths with
`path:line` evidence from files opened this session, and proposals stay out
of fact sections. When genuinely uncertain about a requirement or design
detail, never decide by silent assumption — name it in the plan's Open
questions and proceed on the least-committal reading. Restate the item's
`AC#` criteria verbatim. Run the review
loop — both reviewers, findings fixed into the plan — until you're satisfied
the plan is ready, cap 3 passes (light lane: 1); carry anything unresolved
at the cap into the plan's open questions. Score the plan's `confidence:`
(1–10, one-pass implementation confidence) as each pass exits — while
budget remains within the caps, a low score is the signal to spend it (more
research, another pass); the score recorded after the last pass is final.
Never a reason to stop the run.

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

## Step 4: PR

The PR is an artifact, not the finish line — open it once the work
verifies, then improve it in place (Step 5). All commit/PR prep lives here:

- **Build gate first**: discover the project's own build/typecheck/lint
  workflow (`package.json` scripts, Makefile, CI config — ask the repo,
  don't assume) and run it. Failures are must-fix before the PR opens.
- **Deploy notes scan**: scan the run's diff for schema/migrations, env
  vars/secrets, infra/CI, new third-party dependencies, and one-time
  scripts/backfills. Surface findings; never apply or gate on them.
- Commit selectively (only this run's files, never `git add -A`; secret-scan
  the staged diff), message style `type: short imperative summary`. Rebase
  onto the origin default branch; push (`--force-with-lease` on rewrites).
- Open the PR: typed title; body = **Summary** (the item's intent and what
  "done" means), **Verification** (evidence per AC), **Manual tests** (the
  human-exercisable flows derived from the ACs, risk-tiered — Must: breaks
  data/auth/money if wrong; Important: user-facing behavior; Nice:
  cosmetic — each item traced to the change motivating it, 10–20 items
  total, plus an "areas not affected" line so safe surfaces are skippable —
  Step 5's QA pass executes it), **Deploy notes** (each finding: what changed + the
  action the human takes before/at deploy — name env vars/secrets, never
  their values; omit when the scan finds nothing), **Residual risks** (omit
  if none); `Closes #<n>` when the item has a `github:` issue.

## Step 5: Post-PR review + QA

Reviews run against the open PR and fixes land on it — self-correction
happens on the artifact, not before it exists.

- Run both reviewers over the PR diff (correctness + security, `(security)`
  tags). Loop findings back to the matching implementer and push the fixes;
  cap 3 passes (light lane: 1).
- When no Must Fix remains from either reviewer — or the cap was reached,
  survivors flagged in the wrap-up — run the **QA pass**: execute the PR
  body's Manual tests checklist best-effort, highest risk tier first. The
  `frontend-verifier` drives the running app and captures screenshots; the
  `codex` skill role `backend-verifier` runs the command-shaped items. Both
  dispatches follow `~/.references/qa-verification.md` — external-system
  confirmation by unique marker, preflight, test-mode safety, cleanup. Post
  the results as a PR comment: each item ticked with its evidence, or
  explicitly left to the human with the reason.
- After the loop and QA, post surviving Should Fix / Nice to Have findings
  as line-anchored inline PR comments (`gh api` reviews, event `COMMENT` —
  never `REQUEST_CHANGES`: the loop owns Must Fix, and capped survivors are
  flagged in the wrap-up; these orient the returning human, they gate
  nothing).

## Step 6: Wrap-up

- Write `./tmp/<id>/wrapup.md` following this skill's
  `references/wrap-up-report.md`; post
  it as a PR comment. If the item has a `notion:` reference, `notion` skill
  operation `upload`: plan.md + wrapup.md, PR URL, status `done`.
- Report to the user: PR link + wrap-up summary + QA items left to the
  human + anything unresolved.

## Epics (type: epic-spec)

Run Steps 1–3 per phase, sequentially — per-phase `plan-<n>.md`, tick the
phase ✓ in the spec on completion. After each phase verifies, review the
phase diff — both reviewers, same Must-Fix gate and cap — fix and
re-verify, then run the build gate and commit the phase following Step 4's
commit rules. After the last phase, continue from Step 4's PR steps
(deploy-notes scan over the whole epic diff, rebase, push, open the PR) and
run Steps 5–6 once for the whole epic.

## Rules

- Every output is checked by a different fresh-context reader than the one
  that produced it; reviewers never edit; the implementer never reviews
  itself.
- Never expand scope beyond the item.
- The run is resumable: plan.md plus the item's ✓ state say where you were.
