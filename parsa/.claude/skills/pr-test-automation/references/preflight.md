# Preflight

## Before You Start: Head And Body Must Be Final

QA evidence is current-head evidence and the Manual tests checklist is the
body's contract, so anything that would change either runs first. On a large
PR (over 10 files or 300 hand-written lines) that has not had a `refactor`
pass, say so and offer it before driving anything - a refactor landed after
QA means this whole pass runs again. Likewise `cold-read` on the PR body
comes before QA, so the checklist you execute is the one the reader will see.
