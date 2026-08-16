---
name: refactor
description: Post-PR refactor pass — sizes the diff against origin/main, fans out refactor-simple (and refactor-deep on large changes) as fresh subagents that cannot see each other, merges their plans once with max-severity rules, shows the merged report, and only on the user's word hands it to refactor-apply. Use after a PR is open, or whenever the user asks to refactor or clean up the branch.
argument-hint: "[--size=small|large] [--plan-only]"
---

# Refactor

One command for the post-PR quality pass. It sizes the change, runs the right
analyses independently, merges once, stops for the user, then applies.

## Why the analyses run blind

Two analyses that see each other's findings converge into one opinion. Run
independently, `refactor-simple` and `refactor-deep` overlap on about half
their findings and the other half is complementary — and the severe
correctness findings tend to come from one of them alone. So each analysis
runs in a fresh subagent with no access to the other's output, and the merge
happens exactly once, here, after both are done. Never re-run an analysis to
"confirm" another; repeated runs on the same diff converge on the same
findings, and averaging them has been shown to demote real Criticals.

## Process

### 1. Size the change

```bash
git fetch origin main
git diff origin/main...HEAD --numstat
```

Exclude lockfiles, generated files, and vendored directories from the count.
Under ~10 hand-written files and ~500 lines is **small**; above is **large**.
`--size` overrides. State the size and the file count before fanning out.

### 2. Fan out, independently

Each analysis runs as a separate fresh-context subagent (the Agent tool, one
per analysis, launched in the same message so they run concurrently). Each
subagent invokes its skill and returns the absolute path of the plan it wrote.
The subagent prompt names the skill and the worktree, and nothing else — no
findings, no hints, no other agent's output.

- **small**: `refactor-simple` only.
- **large**: `refactor-simple` and `refactor-deep`, concurrently.

Each writes its own file under `./tmp/`. They do not share a file and do not
read each other's.

### 3. Merge once

Read every plan and produce one merged report at
`./tmp/refactor-merged-[timestamp].md`. Rules, in priority order:

1. **Cluster** findings that point at the same file/area and the same
   underlying issue, even if worded differently.
2. **Max severity, never average.** A finding that is Critical in one plan and
   Warning in another is Critical. A reproduced defect keeps its reproduction.
3. **Sole-source findings are kept.** Corroboration is not required; the
   independent runs are expected to disagree, and the disagreement is signal.
4. **Tag every item** with its source — `[S]`, `[D]`, or `[S+D]` — so the
   reader can see who found what.
5. **Do not re-score.** The merged report carries each plan's quality score
   as reported, plus the merged Critical/Warning/Info counts. Do not invent a
   combined score.
6. Pre-existing-not-against-this-PR items stay in Info, unchanged.

Keep every item's `file:line`, fix, and auto-fixable flag from its source
plan. The merged report is the same shape as the individual plans, so
`refactor-apply` reads it unchanged.

### 4. Stop for the user

Run `fresh-eyes` on the merged report first — it is a document a person reads
to decide what to change in their code, and fresh-eyes may reorder, retitle,
and clarify but never touch a severity, a finding, or a `file:line`. Then show
it — Criticals in full, Warnings and Info summarised — with the auto-fixable
and manual counts, and stop. This is the gate: nothing
is applied until the user says so. `--plan-only` ends here.

Auto-fixable items are the safe class; still show them. Manual items always
wait for the user's judgment on each.

### 5. Apply

On the user's go, invoke `refactor-apply` on the merged report — auto-fixable
first, then manual with the user. When apply finishes, re-run the same
analyses (step 2, fresh subagents again) once and show the delta: what
closed, what remains, anything new. One verification pass, not a loop to a
target score.

## Rules

- Steps 1-4 modify no tracked files. Only step 5 edits code, and only after
  the user's explicit go.
- Analyses run in fresh subagents and never see each other. Do not pass one
  plan into another analysis for any reason.
- Merge means cluster and keep the maximum, never vote, never average.
- If a subagent fails or returns no plan, say so and merge what exists; do
  not re-run it with hints from the plan that succeeded.
