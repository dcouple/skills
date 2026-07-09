---
name: pane-work-recap
description: Summarize recent Pane workspace activity from active panes, archived panes, branches, pull requests, and agent logs. Use when the user asks what they worked on, what they finished, what shipped, what is still active, or asks for a recap over a time window such as today, yesterday, last 24 hours, this week, recently, or open-ended "what have I been working on?"
---

# Pane Work Recap

## Overview

Reconstruct what happened in Pane over a requested time window and explain it
conversationally. Prefer public RunPane commands; use local Pane databases,
git, GitHub, and agent transcript stores only as best-effort evidence when the
official RunPane output does not yet expose enough detail.

## Rules

- Do not mutate repositories, panes, branches, PRs, deployments, or production
  systems. This skill is read-only.
- Do not hardcode user-specific paths. Discover the Pane data directory from
  `runpane doctor --json`, `PANE_DIR`, or explicit user input.
- Do not require bundled scripts. Run ordinary shell, RunPane, git, GitHub, and
  SQLite commands directly as needed.
- Prefer RunPane JSON over Pane internals. Treat direct SQLite/log inspection as
  a fallback and label its caveats.
- Summarize actual workstreams, not just pane names. One pane may contain
  multiple PRs or follow-up tasks.
- Never dump raw agent transcripts by default. Extract final summaries, PR URLs,
  checks, deploy notes, and review findings.
- Call out evidence gaps: missing `archived_at`, missing GitHub auth, removed
  worktrees, unavailable transcript stores, or ambiguous branch matches.

## Time Window

Normalize the user's request before collecting evidence.

- Exact duration, such as "last 24 hours" or "last 3 days": use a rolling
  window from now.
- Calendar words, such as "today", "yesterday", or "this week": use the user's
  local calendar if known; otherwise state the timezone used.
- Open-ended "recently" or "what have I been working on": include active panes
  plus archived/recently updated panes from the last 7 days unless a shorter
  context is clearly implied.
- If timestamps come from SQLite, remember SQLite `CURRENT_TIMESTAMP` is UTC.
  State whether output timestamps are local time or UTC.

## Collection Workflow

### 1. Confirm RunPane

Start with the active Pane instance:

```bash
runpane doctor --json
```

If `runpane` is not on PATH and the user is clearly inside Pane, use the
runtime guidance available in the current environment. If no RunPane command is
available, say that the recap can only use local filesystem evidence and ask for
the Pane data directory if it cannot be discovered.

If a future RunPane build exposes a first-class recap command, prefer it:

```bash
runpane panes recap --since <window> --include-active --include-archived --json
```

Otherwise, continue with the fallback below.

### 2. Gather Pane State

Use public commands first:

```bash
runpane panes list --json
runpane repos list --json
runpane agent-context --json
```

If these outputs do not include archived pane history, inspect the Pane data
directory reported by `doctor`. Use SQLite only if the schema is present:

```bash
sqlite3 "$PANE_DIR/sessions.db" ".tables"
sqlite3 "$PANE_DIR/sessions.db" ".schema sessions"
```

Useful tables when available:

- `sessions`: pane/session name, status, archived flag, timestamps, worktree
  path, project id.
- `projects`: repo names and paths.
- `tool_panels`: terminal, Codex, Claude, browser, explorer, and diff panels.
- `session_outputs`: often archive operation logs, not full transcripts.
- `execution_diffs` and `prompt_markers`: optional detail when present.

If there is no `archived_at` column, use `archived = 1` plus `updated_at` as
the best proxy and state that caveat.

### 3. Resolve Branches And PRs

For each pane/worktree:

- If the worktree still exists, run git commands in that worktree.
- If the worktree was removed, use the saved repo path from Pane state and infer
  candidate branches from the worktree slug and matching branch refs.
- Use `git branch --all --format='%(refname:short)|%(committerdate:iso8601)|%(subject)'`
  to find surviving local or remote branches.
- If `gh` is authenticated, attach PRs with:

```bash
gh pr list --repo <owner>/<repo> --head <branch> --state all \
  --json number,title,state,url,headRefName,baseRefName,createdAt,updatedAt,mergedAt,closedAt,author
gh pr view <number> --repo <owner>/<repo> \
  --json number,title,state,url,body,changedFiles,additions,deletions,files,commits,mergedAt,closedAt
```

If a branch produced multiple PRs, list each PR separately. If an active pane
worked on an open PR and a merged PR, separate those in the summary.

### 4. Locate Agent Logs

Use transcript paths from RunPane if it provides them. Otherwise discover local
agent stores from environment variables or standard home-relative paths.

Codex:

- Default root: `${CODEX_HOME:-$HOME/.codex}/sessions`
- Match by `session_meta.payload.cwd`, worktree path, branch slug, pane name, or
  PR URL.
- Read compactly with JSON filters; useful records are `session_meta` and
  assistant `response_item` messages near the end or around PR/check/deploy
  terms.

Claude:

- Default root: `${CLAUDE_CONFIG_DIR:-$HOME/.claude}/projects`
- Match by worktree path slug, pane name, branch slug, or PR URL.
- Check main `.jsonl` files plus `subagents/*.meta.json` for agent roles such
  as explore, implementer, plan-reviewer, and implementation-reviewer.

If logs are huge, search first with `rg -l` and then read only matching files.
Useful search terms include pane slug, worktree path, branch name, PR URL,
`merged`, `deployed`, `checks`, `review`, `PostHog`, `Stripe`, and `IndexNow`.

### 5. Build The Recap

Group findings into conversational buckets:

- **Shipped / merged:** merged PRs, deploys, indexing submissions, release tags,
  and production verification.
- **Finished but not merged:** completed branches, ready PRs, passed QA, or
  archived panes without a merge.
- **Still active / open:** active panes, open PRs, draft PRs, failing checks, or
  follow-up work.
- **Agent evidence:** which agents worked, what they did, notable review
  findings, and what got fixed because of review.
- **Caveats:** missing transcript rows, reused panes, ambiguous branches,
  unavailable GitHub auth, or direct DB fallback assumptions.

Prefer a natural narrative over a raw table. A table is useful for dense PR
lists, but the user is usually asking for memory reconstruction, not a report
dump.

## Output Style

Start with the high-signal answer:

```text
You shipped three things and had one open workstream in that window.
```

Then summarize per workstream:

```text
`pane name` -> repo/branch -> PR(s)
What changed, what checks or deploys happened, and what is still open.
```

End with evidence quality:

```text
I found Codex logs for all four panes and Claude logs for two. Pane's own DB
only kept archive-operation output, so the agent summaries came from the agent
transcript stores.
```

Keep the tone conversational and concrete. Do not overstate completion when the
evidence only shows local changes or an open PR.
