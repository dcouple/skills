---
name: create-issue
description: Captures a defect as a Bug Report work item ready for /do, running the investigator first if the root cause isn't already established. Use when the user explicitly asks to create an issue, bug report, or ticket for a defect — e.g. "create an issue for this", "write this bug up", "file this" — typically after a discussion or investigation has surfaced it.
argument-hint: "[bug title or one-line summary]"
allowed-tools: Read, Write, Edit, Glob, Grep, Task, Skill, Bash(gh:*)
---

# Create Issue

## Issue: $ARGUMENTS

Turn a defect the conversation has surfaced (typically via `/discussion`) into a lean
Bug Report that `/do` can fix autonomously. The completion artifact is
`./tmp/<id>/item.md` with `status: ready` — diagnosis captured, fix delegated.
This skill documents; it never fixes code.

## Steps

### 1. Take stock of the investigation
Check what the conversation already established: reproduction, root cause + evidence,
confidence level. A root-cause finding from an `investigator` dispatch during
`/discussion` is the ideal input — reuse it, don't redo it.

If the root cause is **not** yet established, run the investigation now:
- Dispatch the investigator via the `codex` skill (role `investigator`) with the full
  report (expected vs actual, environment, known repro steps, traces); it returns its
  standard root-cause finding. Fallback on `CODEX UNAVAILABLE`/`CODEX ROLE FAILED`:
  the Claude `investigator` sub-agent.
- If reproduction requires driving the running app, dispatch `app-user` first to
  exercise the flow and capture evidence, then pass its transcript along with the
  defect report.
- If the investigator cannot reproduce: say so plainly. Do not invent a cause. Either
  gather more from the user (logs, exact environment) and re-dispatch, or proceed with
  root cause marked `Hypothesis:` and what-was-tried captured in `refs/`.

**Success criteria**: a root-cause finding in hand with an honest confidence level
(`confirmed | likely | hypothesis`) — or a documented failed-to-reproduce with the
attempts listed.

### 2. Confirm impact and severity
Where judgment is needed, confirm with the user: who is affected, how widespread, why
it matters now, and whether the suggested resolution path should be locked as a
direction or left to `/do`. Skip the ceremony when severity is obvious.

**Success criteria**: severity (`critical | high | medium | low`) and business impact
agreed with the user.

### 3. Write the Bug Report
- Pick `<id>`: short kebab-case slug from the bug title. Create `./tmp/<id>/`.
- Write `item.md` following `references/bug-report.md` (frontmatter + body; don't emit
  the template's "— format" header or guidance quotes).
- Reproduction steps go **in the report** — deterministic enough for the verify stage
  to re-run them. Raw traces, logs, and long transcripts go to `./tmp/<id>/refs/`
  (e.g. `refs/error-trace.txt`), linked not inlined. If the investigation produced a
  current-state deep-dive worth keeping, save it per
  `~/.references/system-analysis.md` as `refs/system-analysis.md`.
- Verification criteria per `~/.references/verification-criteria.md` must include:
  - **AC1**: the reproduction flipping from fail to pass — the repro steps double as
    the failing case the fix must flip.
  - **Prevention criteria**: what stops this class of bug recurring (a regression
    test, a guard, an invariant) — verifiable, not aspirational.

**Success criteria**: `item.md` exists; repro is re-runnable; AC1 maps to the repro;
prevention criteria present; raw material linked from `refs/`.

### 4. Learning gate [human]
Ask the user to state back, in one or two sentences, the root cause and how the fix
will be verified. One exchange, not a quiz. If their read conflicts with the doc,
reconcile before proceeding.

**Success criteria**: the user's teach-back matches the item.

### 5. Mark ready and publish
1. Set `status: ready` in `item.md` (leave `draft` if the cause is still a hypothesis
   and the user wants more evidence first — publish happens either way, so the
   evidence trail lives with the issue).
2. Create the GitHub issue: `gh issue create` in the project's repo (from the
   `Work-item tracking` section of the project's `CLAUDE.md`, or the current repo) —
   title `fix: <bug title>`, body = summary, severity, reproduction steps, root cause
   + confidence.
3. Invoke the `notion` skill, operation `publish`, with `./tmp/<id>/` and the issue
   URL — it creates the Notion work item and uploads `item.md` + every `refs/` file
   (traces, transcripts, system analysis), returning the page URL.
4. Cross-link: add the Notion page URL to the GitHub issue body (`gh issue edit`),
   and record both in `item.md` frontmatter as `github:` and `notion:`. On
   `NOTION UNAVAILABLE`, proceed GitHub + local only and tell the user.

**Success criteria**: issue exists, Notion work item exists with all artifacts (or
its absence was reported), and each of issue / Notion page / item.md links to the
others.

```
Suggested next steps:
- `/do <issue # or ./tmp/<id>/item.md>` — run the autonomous pipeline to fix and verify
- `/discussion [topic]` — if the bug exposed a design question bigger than the fix
```
