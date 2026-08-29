---
name: refactor
description: Pre-review refactor pass. Sizes the diff against the remote default branch, fans out refactor-simple (and refactor-deep on large changes) as fresh subagents that run blind to each other, merges their plans once with max-severity rules, shows the merged report, and hands it to refactor-apply on the user's word. Use before final review, whether or not a PR is already open, or whenever the user asks to refactor or clean up the branch.
argument-hint: "[--size=small|large] [--plan-only]"
---

# Refactor

One command for the pre-review quality pass. It sizes the change, runs the right
analyses independently, merges once, stops for the user, then applies. It
runs after implementation and before final review, `fresh-eyes` on the PR body,
and QA; the PR may already be open, but QA is the final readiness gate.

## Why the analyses run blind

Two analyses that see each other's findings converge into one opinion. Run
independently, `refactor-simple` and `refactor-deep` overlap on about half
their findings, the other half is complementary, and the severe correctness
findings tend to come from one of them alone. So each analysis runs in a
fresh subagent with no access to the other's output, and the merge happens
exactly once, here, after both are done. Repeated runs on the same diff
converge on the same findings, and averaging them has demoted real Criticals;
one run per analysis is the rule.

## Process

### 1. Size the change

```bash
BASE=$(git symbolic-ref -q refs/remotes/origin/HEAD | sed 's|refs/remotes/||')
[ -n "$BASE" ] || BASE=origin/$(git remote show origin | sed -n 's/.*HEAD branch: //p')
git fetch origin "${BASE#origin/}"
git diff "$(git merge-base "$BASE" HEAD)" --numstat
```

Merge-base to working tree, so uncommitted work counts; the remote's real
default branch, not an assumed `main`.

Exclude lockfiles, generated files, and vendored directories from the count.
Under ~10 hand-written files and ~500 lines is **small**; above is **large**.
`--size` overrides. State the size and the file count before fanning out.

### 2. Fan out, independently

Each analysis runs as a separate fresh-context subagent (the Agent tool, one
per analysis, launched in the same message so they run concurrently). Each
subagent invokes its skill and returns the absolute path of the plan it wrote.
The subagent prompt names the skill and the worktree, and nothing else.

- **small**: `refactor-simple` only.
- **large**: `refactor-simple` and `refactor-deep`, concurrently.

Each writes its own file under `./tmp/`, and reads only its own.

### 3. Merge once

Read every plan and produce one merged report at
`./tmp/refactor-merged-[timestamp].md`. Rules, in priority order:

1. **Cluster** findings that point at the same file/area and the same
   underlying issue, even if worded differently.
2. **Keep the maximum severity.** A finding that is Critical in one plan and
   Warning in another is Critical. A reproduced defect keeps its reproduction.
3. **Sole-source findings are kept.** Corroboration is not required; the
   independent runs are expected to disagree, and the disagreement is signal.
4. **Tag every item** with its source, `[S]`, `[D]`, or `[S+D]`, so the
   reader can see who found what.
5. **Carry each plan's quality score as reported**, plus the merged
   Critical/Warning/Info counts. The merged report has no combined score.
6. Pre-existing-not-against-this-PR items stay in Info, unchanged.

Keep every item's `file:line`, fix, and auto-fixable flag from its source
plan. The merged report is the same shape as the individual plans, so
`refactor-apply` reads it unchanged.

### 4. Stop for the user

Run `fresh-eyes` on the merged report first: a person reads it to decide what
to change in their code. Fresh-eyes may reorder, retitle, and clarify;
severities, findings, and `file:line` stay as written. Then show it, Criticals
in full, Warnings and Info summarised, with the auto-fixable and manual
counts, and stop. This is the gate: nothing
is applied until the user says so. `--plan-only` ends here.

Auto-fixable items are the safe class; still show them. Manual items always
wait for the user's judgment on each.

### 5. Apply, then prove it

On the user's go, invoke `refactor-apply` on the merged report, auto-fixable
first, then manual with the user. `refactor-apply` leaves its edits
uncommitted; this step commits them as one scoped commit named for the plan
and the round. Run the repository checks named by the merged plan, then hand
the final head to the workflow's single capped review phase. Do not start a
separate refactor-review loop or rerun the analyses automatically.

## Rules

- Steps 1-4 modify no tracked files. Only step 5 edits code, and only after
  the user's explicit go.
- Analyses run in fresh subagents, blind to each other; a plan stays out of
  every other analysis.
- Merge means cluster and keep the maximum severity.
- If a subagent fails or returns no plan, say so and merge what exists.
- Refactor ends before the shared review budget begins; final QA follows that
  review and is never followed by more code changes.
