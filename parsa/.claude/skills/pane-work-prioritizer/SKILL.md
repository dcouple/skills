---
name: pane-work-prioritizer
description: Recommend the next work items from current Pane and GitHub evidence, including blockers and concrete next actions.
---

# Prioritize work

## Scope and rules

- This is a recommendation, not permission to start work, change panes, comment, assign, merge, or modify code.
- Use the requested scope; otherwise start with active/recent Pane repositories and relevant GitHub queues.
- Prefer current evidence over pane names, old branches, or memory. State missing signals and query limits.

## Collect

1. Confirm GitHub identity and available RunPane commands, for example `gh auth status` and `runpane doctor --json`.
2. Read active/recent panes, repositories, and worktree activity. Use relevant logs only when they clarify a candidate's state.
3. Query review requests, authored open PRs, assigned issues, and relevant teammate PRs.
4. Enrich top candidates with checks, draft state, review decisions, blockers, labels, and update times.
5. If unresolved feedback affects ranking, fetch paginated review-thread state; flat top-level comments cannot prove that a PR is clear.

Useful query examples, scoped to the user's request:

```text
gh search prs --review-requested=@me --state=open --archived=false
gh search prs --author=@me --state=open --archived=false
gh search issues --assignee=@me --state=open --archived=false
```

## Rank

- Start with explicit urgency, incidents, security/data risks, and work that unblocks others.
- Prefer finishing high-value work near completion over opening more work, unless impact or urgency says otherwise.
- Assess draft decisions and active workstreams before treating stale backlog or every assigned issue as urgent.
- Explain tradeoffs; priority labels and recency are evidence, not an automatic scoring formula.

## Recommend

- Return a short ranked list with link, reason, next action, and blocker/uncertainty.
- Suggest an available workflow where useful: investigation for an unknown failure, planning for a clear feature, review/QA for a completed branch, or feedback handling for an open PR.
- Do not require this collection's skills if the environment provides a different workflow.
- Include “not next” items only when that helps reduce noise. End with evidence gaps.

## Saved recommendation

- No file is required by default. If requested and Grain is connected, save the report in the supplied task folder, or `Development Artifacts/YYYY-MM-DD-<task>`.
- Keep needed local copies and privacy limits; without Grain, use the requested local handoff silently.
