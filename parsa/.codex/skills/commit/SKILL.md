---
name: commit
description: Commit the current task's changes locally while preserving unrelated work and staged changes.
---

# Commit

## Scope

- Use the user's request, conversation, and relevant plan to identify this task's changes.
- Inspect both `git diff` and `git diff --cached`; a file appearing in a plan does not make every change in it yours.
- Leave unrelated work untouched. If ownership overlaps and cannot be separated safely, ask rather than guessing.
- Follow project conventions for whether working notes belong in Git; do not automatically commit temporary artifacts.

## Commit

1. Check status; stop if no changes are in scope.
2. Stage explicit files or hunks, never `git add .` or `git add -A`.
3. Preserve unrelated staged work without including it in this commit. Check the exact commit diff for secrets.
4. If secrets are present, exclude them and report the blocker without exposing their values.
5. Use a supplied commit message; otherwise follow repository conventions, for example `fix: handle an empty response`.
6. Commit locally without repeated approval requests. Do not push.

## Report

- Commit SHA and subject.
- Included changes and work left uncommitted.
- A relevant next step, if any.

This skill needs no new report file. Read supplied Grain context when available; keep code and Git state in the repository.
