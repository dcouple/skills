# Preflight

## Before You Start: Preflight

QA evidence is current-head evidence and the Manual tests checklist is the
body's contract, so anything that would change either runs first. On a large
PR (over 10 files or 300 hand-written lines) that has not had a `refactor`
pass, say so and offer it before driving anything. A refactor landed after
QA means this whole pass runs again. Likewise `cold-read` on the PR body
comes before QA, so the checklist you execute is the one the reader will see.

Before spending a long QA pass, verify the PR is in a testable state. Pass
the identified PR number or URL to every `gh pr view` call (bare `gh pr view`
defaults to the current branch's PR, which may differ from the test target):

- **Mergeability.** Check `gh pr view <PR> --json mergeable,mergeStateStatus`.
  A conflicting PR may get no gating CI run at all, and QA evidence against a
  conflicting head is evidence against code that will change on merge. If
  conflicting, report blocked rather than driving.
- **Head SHA incorporated.** Confirm the PR's `headRefOid` is part of the
  tested state (`gh pr view <PR> --json headRefOid`). When testing companion
  PRs together, the local HEAD may be a merge commit that incorporates
  multiple PR heads; verify the target PR's head is in the ancestry
  (`git merge-base --is-ancestor <headRefOid> HEAD`) and record the composite
  SHA rather than requiring an exact match. A checkout that does not contain
  the PR head produces evidence for code the reviewer is not looking at.
- **CI existence.** Check whether at least one workflow run exists for the
  PR's head commit (`gh run list --commit <headRefOid>`). If the repo has CI
  and no run registered, something is wrong (path filters, a conflicting
  state, a workflow syntax error). Note it; do not assume the code is healthy.
- **Tools alive.** Verify every tool the run will need before the first long
  flow: authenticated CLIs, running services, connectors, test-mode keys.
  A flow that dies at step 7 for a missing login wastes the entire run.
