---
name: runpane-orchestrator
description: Orchestrate RunPane issue-to-PR workstreams across discussion, planning, implementation, review, PR testing, and CLI dogfooding without stealing user focus. Use when the user asks Claude Code to fan out GitHub issues, manage multiple Pane workstreams, or run the Pane discussion-plan-implement-review loop.
---

# RunPane Orchestrator

Use RunPane as the control plane for long-running engineering work. This skill
spawns and babysits agent panes or panels, advances each issue through the
team's discussion -> create-plan -> implement -> review -> PR-test -> PR
workflow, and captures RunPane dogfood findings as issues or PRs.

## Inputs

- `$ARGUMENTS`: Target repo, issue URLs/numbers, author filters such as "all
  issues I created", or an open-ended improvement goal.

## Goal

For each selected issue, produce a reviewable PR with local/automated evidence,
independent reviewer output processed, and any RunPane CLI friction documented
or fixed in a separate tracked workstream. Do not merge, deploy, release, or
bump versions unless the user explicitly authorizes that exact action.

## Pane Chat Work Questions

When Pane Chat is asked what the user has been working on or what they should
work on next, treat it as a read-only work question, not an issue-to-PR
orchestration job.

- Use `pane-work-recap` for "what did I do / what shipped / what is active?"
- Use `pane-work-prioritizer` for "what should I do next / what is blocked /
  what should I ignore?"
- If the Pane runtime exposes the dcouple skills cache, also read the shared
  agent-agnostic guide at `parsa/pane-chat/work-questions.md`.
- Ground priority recommendations in this skill system: name the next workflow
  skill, such as `investigate`, `discussion`, `plan`/`create-plan`,
  `simple-plan`, `implementation-reviewer`/`review`, `pr-test-automation`,
  `prepare-pr`, `page-review`, `site-content-audit`, or `teach-back`.

## Rules

- Agent-created panes and panels should be background work by default. Pass
  `--source agent` and the current CLI's no-focus/background option when
  available, then verify the JSON and the user's focus behavior.
- If a RunPane command reports `active:false` or `focused:false` but the app
  still switches the visible pane, treat that as a RunPane bug and file or
  update an issue with exact commands, expected behavior, actual behavior, and
  root-cause notes.
- Do not rely on static sleeps. Prefer RunPane wait/status primitives such as
  ready, idle, text, or status-change waits. Keep terminal snapshots compact;
  store long outputs in files or issue comments rather than repeatedly adding
  full screen payloads to the orchestrator context.
- For composer submission, prefer `runpane panels submit-composer --strategy
  auto` after pasting long prompts. Confirm `verifiedSubmitted:true` and then
  wait for real output. Do not spend tokens guessing whether Enter or
  Ctrl+Enter is the right submit key.
- If a Codex or Claude update prompt blocks startup, follow the blocker
  payload's suggested `runpane panels submit --text "<choice>"` command, then
  continue.
- Keep each issue's artifacts together: issue URL, pane id, panel ids, branch,
  worktree path, discussion summary, plan path, checks, PR URL, and reviewer
  conclusions.
- Run Codex and Claude review passes independently when the PR is ready. Feed
  both outputs back into the implementation pane, ask it to decide which
  findings are legitimate, fix legitimate issues, and rerun the loop until only
  intentional tradeoffs or very small edge cases remain.
- Use focused git staging. Do not stage unrelated user or agent work. Never use
  destructive git commands unless the user explicitly asks.
- Stop before merge, release, deploy, version bump, production mutation, or
  other irreversible actions unless the user explicitly authorized that step.

## Steps

### 1. Resolve the Work Queue

Identify the repo and issues to operate on. If the user says "all issues I
created", query GitHub rather than guessing:

```bash
gh issue list --repo <owner>/<repo> --author @me --state open \
  --json number,title,url,body,labels,createdAt,updatedAt
```

If the task is open-ended self-improvement, create or choose one high-leverage
RunPane issue and keep it separate from product-feature work.

**Success criteria**: Every workstream has an issue URL/number, target repo,
and explicit constraints such as "do not merge" recorded in the orchestrator
notes.

### 2. Start Background Work Panes

Create one pane per issue unless the user asked for a single shared pane. Use
background creation so the user can keep talking to the orchestrator:

```bash
runpane panes create --repo "<repo name or path>" \
  --name "issue-<number>-<short-slug>" \
  --agent codex \
  --source agent \
  --wait-ready \
  --json \
  --yes
```

If the CLI cannot resolve the active repo, pass the explicit repo name or path.
If startup returns a blocker, handle it with the suggested command and then
resume:

```bash
runpane panels submit --panel <panel-id> --text "<choice>" --yes --json
```

Capture `paneId`, `panelId`, `worktreePath`, and the created branch name.

**Success criteria**: Each issue has a ready agent pane/panel, the JSON shows
background creation, and any focus theft has been filed or appended to a
RunPane issue.

### 3. Run Discussion

Paste a discussion prompt into each issue's first panel. Use this shape:

```text
Use the discussion skill for this GitHub issue.

Do not edit files yet. Read the code only as needed. I want a grounded
implementation discussion: current behavior, likely code paths, options,
tradeoffs, risks, and the recommended next skill.

Issue:
<issue URL>

<issue title and body>
```

For long prompts, paste through RunPane and submit through the composer helper:

```bash
runpane panels input --panel <panel-id> --input-file <prompt-file-or-> --yes --json
runpane panels submit-composer --panel <panel-id> --strategy auto --yes --json
runpane panels wait --panel <panel-id> --for idle --timeout-ms <milliseconds> --json
```

Use the exact current CLI syntax for long text or file input; the important
part is that the terminal shows the prompt was pasted, the submit helper
verifies submission, and the panel becomes idle after producing output.

**Success criteria**: Each discussion output gives a concrete recommendation:
create-plan, investigate, simple-plan, or implement, with enough context to
hand off.

### 4. Advance to Planning or Investigation

If the discussion says the issue is not understood, run `investigate` first and
write the root cause back to the issue. Otherwise run `create-plan`:

```text
Use the create-plan skill for this GitHub issue and discussion result.

Source issue:
<issue URL>

Discussion summary:
<paste concise discussion result or path to saved output>

Create a plan that preserves the issue intent, names the relevant files, lists
checks, and calls out any assumptions. Do not implement yet.
```

Wait for idle, then inspect the plan enough to decide whether it is coherent.
For very small changes, `simple-plan` may replace `create-plan`, but only when
the blast radius is clearly narrow.

**Success criteria**: The workstream has either a root-cause investigation note
or an implementation plan with concrete file targets and check commands.

### 5. Implement

Run implementation in the same workstream pane so the pane retains the context
and branch:

```text
Use the implement skill for the approved plan.

Carry the implementation through focused checks and implementation review.
Preserve the issue intent. Do not merge, deploy, release, or bump versions.
```

Babysit with event-driven waits rather than sleeps. When the pane becomes idle,
inspect the summary, changed files, and reported checks. If implementation
stops early, feed back the missing plan tasks or blocker and continue.

**Success criteria**: The implementation pane reports complete work, relevant
checks have run or failures are clearly documented, and the branch contains only
scoped changes for that issue.

### 6. Run PR Test Automation and Prepare the PR

After implementation review passes, run PR testing:

```text
Use the pr-test-automation skill for this branch.

Test the PR-relevant flows with tool evidence where possible. Separate passed
automated checks from remaining manual checks.
```

Then prepare the PR:

```text
Use the prepare-pr skill.

Commit only scoped changes, rebase on main, run relevant checks, push the
branch, and create or update the PR. Do not merge, deploy, release, or bump
versions.
```

**Success criteria**: A PR exists with linked issue(s), a useful summary,
checks/test notes, and no unrelated changes included.

### 7. Run Independent Review Tabs or Panels

Within the same workstream pane, prefer new tabs for reviewers if the current
RunPane build can create them without stealing focus. If focus behavior is not
trustworthy, use background panels or panes and record that as a dogfood note.

Run a Codex review and a Claude review independently. In each reviewer context,
start `/review` or the equivalent review skill, answer interactive prompts
until the review is actually running, then wait for idle.

**Success criteria**: Both reviewers produce findings or explicitly report no
actionable issues, and their outputs are saved or pasted back into the main
implementation panel.

### 8. Resolve Review Findings

Paste the reviewer outputs into the implementation pane:

```text
Here are independent Codex and Claude review findings for this PR.

Decide which findings are legitimate. Fix legitimate issues directly, reject
false positives with concrete reasons, rerun the relevant checks, and update the
PR if needed. Keep looping until only intentional tradeoffs or very small edge
cases remain.

<review outputs>
```

If review finds real issues, rerun implementation review, PR testing as needed,
and the independent reviewer loop for the changed area.

**Success criteria**: All legitimate review findings are resolved or explicitly
rejected with reasons, checks are updated, and the PR is still scoped.

### 9. Document Dogfood Findings

Whenever the orchestration exposed RunPane friction, update the appropriate
issue or create a new one. Include:

- exact command
- expected behavior
- actual behavior
- observed JSON/status payload
- terminal/composer symptoms
- root-cause hypothesis or confirmed code path
- suggested next steps

High-value findings from this reference workflow include:

- `runpane version` and `runpane --version` must be pure metadata commands and
  must not open a Pane window.
- Background agent pane creation must not switch the user's visible active pane
  through either panel activation or session-created renderer events.
- Composer submission should expose an opinionated, verified default so agents
  do not waste context deciding between Enter and Ctrl+Enter.
- Wait APIs should support compact status-change notifications and bounded
  snapshots so orchestrators do not ingest full terminal screens unnecessarily.

**Success criteria**: Each CLI/product friction point is either fixed in its own
branch/PR or documented in a GitHub issue with enough context for a future
agent to implement it.

### 10. Final Handoff

Summarize the state per issue:

- issue URL
- pane/panel ids
- branch
- PR URL
- checks run
- reviewer loop status
- remaining manual checks
- RunPane dogfood issues or PRs created

End in review state. Do not merge, release, deploy, or bump versions unless the
user explicitly returns and asks for that exact action.

**Success criteria**: The user can come back to a compact dashboard of PRs,
checks, review status, and open manual decisions.
