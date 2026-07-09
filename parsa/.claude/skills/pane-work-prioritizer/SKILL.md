---
name: pane-work-prioritizer
description: Recommend what to work on next across a Pane workspace and GitHub activity. Use when the user asks what they should work on next, what to prioritize, what is blocked, what needs review, what PRs should be merged, what issues matter, or wants a triage of active/recent repos, panes, PRs, issues, checks, reviews, and recent work.
---

# Pane Work Prioritizer

## Overview

Rank the user's next work across Pane and GitHub. Combine active Pane context,
recent repo activity, open PR state, review requests, assigned issues, CI,
review comments, and recency into a short recommendation that says what to do
first and what to ignore for now.

## Rules

- Stay read-only unless the user explicitly asks to comment, assign, close,
  merge, rebase, start panes, or change code.
- Give a ranked recommendation, not an inventory dump.
- Ground the recommendation in the dcouple skill system: tell the user which
  skill/workflow should be used next for each ranked item.
- Prefer current GitHub and RunPane state over memory. If GitHub auth,
  RunPane, or local repo data is unavailable, say which signal is missing.
- Do not treat every assigned issue as urgent. Use labels, PR state, checks,
  recency, active panes, business impact, and blockers to infer priority.
- Do not treat a pane name or stale branch as proof of active work. Check
  branches, PRs, agent logs, and recent updates before calling something live.
- Include "probably not next" items when the queue is noisy.
- If the user gives a scope, respect it. Otherwise default to active panes,
  recently updated/archived panes, the last 10 locally or Pane-active repos,
  and GitHub queues across repos the authenticated user can see.

## Collection Workflow

### 1. Establish Identity And Scope

Use the authenticated GitHub user when available:

```bash
gh auth status
gh api user --jq '.login'
```

If the user asks for "next" without a timeframe, use current state plus recent
activity. If they ask for a time period, use it to choose recent repositories
and Pane activity, but still include currently blocking review requests and
open PRs.

### 2. Gather Pane And Local Repo Signals

Start with public RunPane commands:

```bash
runpane doctor --json
runpane panes list --json
runpane repos list --json
runpane agent-context --json
```

If RunPane is unavailable, use local git repositories from the current workspace
and conventional user checkout roots only as best-effort evidence. Do not
hardcode personal absolute paths; prefer `$HOME`-relative discovery when needed.

For each candidate repo, record:

- Active panes or recently archived panes tied to the repo.
- Last local commit/update time.
- Current branch names and whether worktrees still exist.
- Any branch or PR URLs found in agent logs if the user asked for Pane-aware
  prioritization.

### 3. Gather GitHub Queues

Check inbound review first:

```bash
gh search prs --review-requested=@me --state=open --archived=false \
  --json repository,number,title,url,author,updatedAt,isDraft --limit 100
```

Then check the user's open authored PRs and assigned issues:

```bash
gh search prs --author=@me --state=open --archived=false \
  --sort updated --order desc \
  --json repository,number,title,url,author,updatedAt,isDraft --limit 100

gh search issues --assignee=@me --state=open --archived=false \
  --sort updated --order desc \
  --json repository,number,title,url,updatedAt,labels,author --limit 100
```

For the recent repos, also inspect repo-local open PRs because teammates' PRs
may need attention even when GitHub did not explicitly request review:

```bash
gh pr list --repo <owner>/<repo> --state open \
  --json number,title,url,isDraft,author,updatedAt,reviewDecision,mergeStateStatus,labels --limit 50
```

For top candidates, inspect details:

```bash
gh pr view <number> --repo <owner>/<repo> \
  --json number,title,url,isDraft,author,updatedAt,reviewDecision,mergeStateStatus,statusCheckRollup,latestReviews,reviews,reviewRequests,comments,labels
```

Use `statusCheckRollup` to separate passing, failing, pending, skipped, and
unknown checks. Search results do not expose `reviewDecision`; enrich authored
PR candidates with `gh pr list` or `gh pr view` before ranking them by review
state. Use `latestReviews` and `reviews` to identify review decisions and
review-body findings. Use `comments` only for top-level PR discussion, not as a
complete review signal. If the ranking depends on inline review comments, fetch
them explicitly:

```bash
gh api repos/<owner>/<repo>/pulls/<number>/comments --paginate
```

Do not dump long bot reviews.

### 4. Map Items To Skills

Use the team's skill system to explain the practical next step:

- Unknown failure, crash, or regression: `investigate`.
- Fuzzy product idea or broad feature: `discussion`, then `create-ticket`.
- Crisp implementation issue: `plan`/`create-plan` or `simple-plan`, then
  `implement`.
- Completed branch that needs confidence: `review`, then `pr-test-automation`.
- Branch that should become a PR: `prepare-pr`.
- Open PR with review findings: `implement` for fixes, then review again.
- PR that is ready but untested: `pr-test-automation`.
- Public docs, support copy, SEO, or marketing page: `page-strategy`,
  `page-review`, or `site-content-audit` before implementation.
- Business-facing artifact: `business-context -> business-discussion ->
  business-spec -> business-artifact -> business-artifact-reviewer`.
- Finished non-trivial work: `teach-back`; use `share-fix` only after explicit
  approval to post externally.

### 5. Rank Work

Use this priority order as a heuristic, then explain the judgment:

1. Explicit review requests, production incidents, security issues, billing or
   migration blockers, release failures, and broken deploys.
2. Fresh open PRs that are close to shipping: passing checks, non-draft, recent
   updates, clear review status, small follow-up needed.
3. High-impact draft PRs that need a decision: QA complete, checks passing, or
   one explicit human/product choice before ready-for-review.
4. Active Pane workstreams with recent agent activity and a clear next action.
5. Assigned P0/P1 issues, especially if labeled bug, security, reliability,
   data loss, billing, or customer-facing.
6. Large backlog waves, stale dirty PRs, old drafts, and personal experiments
   only after the above are clear.

When two items compete, prefer finishing work already near merge over starting
new backlog work, unless the new issue is a real incident or business blocker.

## Output

Start with a direct answer:

```text
I would work on <item> first, then <item>. The main reason is that your review
queue is empty, but these two PRs are already close to shipping.
```

Then give 3-7 ranked items. For each item include:

- Repo and PR/issue URL.
- Why it ranks there.
- One concrete next action.
- The next skill or workflow to use.
- Any blocker or uncertainty.

Add a short "probably not next" section for noisy backlog areas, stale PRs, or
repos with no actionable queue.

End with evidence quality:

```text
Signals used: active panes, last 10 recent repos, GitHub review requests,
open authored PRs, assigned issues, PR checks, and review comments. I could not
read archived pane logs, so I did not use them as proof of completion.
```

Keep the response conversational. The user is asking for judgment, not a full
GitHub audit.
