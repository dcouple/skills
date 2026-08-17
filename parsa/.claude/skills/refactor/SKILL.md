---
name: refactor
description: Post-PR refactor pass — sizes the diff against the remote default branch, fans out refactor-simple (and refactor-deep on large changes) as fresh subagents that cannot see each other, merges their plans once with max-severity rules, shows the merged report, and only on the user's word hands it to refactor-apply. Use after a PR is open, or whenever the user asks to refactor or clean up the branch.
argument-hint: "[--size=small|large] [--plan-only]"
---

# Refactor

One command for the post-PR quality pass. It sizes the change, runs the right
analyses independently, merges once, stops for the user, then applies. It
runs after review and before `fresh-eyes` on the PR body and before QA: it
changes the head, and QA evidence must be current-head evidence.

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

### 5. Apply, then prove it

On the user's go, invoke `refactor-apply` on the merged report — auto-fixable
first, then manual with the user. `refactor-apply` leaves its edits
uncommitted; this step commits them as one scoped commit (message names the
plan and the round) so the adversary has an exact diff to review. Every later
fix round is committed the same way before its adversary runs.

Then run the **adversarial loop**, as one continuous chain — do not stop
between rounds to report; the user reads the outcome. Adversary passes are
numbered 1 to 3, and 3 is the cap:

1. **Pass 1 — the apply commit.** A fresh subagent reviews that commit's diff
   **only** (`git diff <sha>~1..<sha>`), briefed to prove it broke something:
   treat every claim in the apply report as a claim to falsify; check that
   behaviour-preserving changes preserved behaviour, and that a consolidation
   did not narrow an edge case a caller depended on. Where a test claims to
   demonstrate a defect fix, run it on the parent (must fail) and the head
   (must pass); characterization tests for behaviour-preserving changes may
   pass on both. It returns CLEAN or REGRESSION with `file:line` and a repro.
2. **On REGRESSION**, hand the repro back to the applier for a repair, commit
   it, and run pass 2 — a fresh adversary on the repair commit alone. Each
   repair adds the repro as a test proven failing on its parent.
3. **Pass 3 is the last.** If it is reached, the repairs are hand-tuning to
   the last reported inputs while breaking the next; the repair before pass 3
   is **spec-driven, not patch-driven** — the applier writes the input class
   as a test table or replaces the mechanism with a pure derivation, and
   STOPS rather than commits if the correct fix needs scope beyond the files
   at hand. Whatever pass 3 finds is reported to the user with the plan,
   not repaired.

A CLEAN pass advances. At the cap, advance anyway: the survivors are
reported as open Criticals beside the delta, and the user decides. Then
re-run the analyses (step 2, fresh subagents) once and show the delta: what
closed, what remains, anything new.

Why: on the first real run, two apply commits passed every check and their
own new tests, and the adversary found a reproduced regression in each; the
repairs then broke adjacent cases twice, with tests that passed trivially.
Nothing but an adversary told to falsify caught any of it.

## Rules

- Steps 1-4 modify no tracked files. Only step 5 edits code, and only after
  the user's explicit go.
- Analyses run in fresh subagents and never see each other. Do not pass one
  plan into another analysis for any reason.
- Merge means cluster and keep the maximum, never vote, never average.
- If a subagent fails or returns no plan, say so and merge what exists; do
  not re-run it with hints from the plan that succeeded.
- The adversarial loop runs in one chain. Waiting on a human between rounds
  turns ten minutes of agent work into hours; report at the end.
