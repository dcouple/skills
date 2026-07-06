---
name: create-issue
description: Captures a defect as a Bug Report work item ready for /do, running the investigator first if the root cause isn't already established.
argument-hint: "[bug title or one-line summary]"
disable-model-invocation: true
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
  standard root-cause finding.
- If reproduction requires driving the running app, dispatch `frontend-verifier`
  first to exercise the flow and capture evidence, then pass its transcript along
  with the defect report.
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
- Verification criteria per `~/.references/verification-criteria.md` (methods:
  `~/.references/verification-methods.md`) must include:
  - **AC1**: the reproduction flipping from fail to pass — the repro steps double as
    the failing case the fix must flip.
  - **Prevention criteria**: what stops this class of bug recurring — a regression
    test, a custom lint/static rule (the most durable guard), or an invariant —
    verifiable, not aspirational.

**Success criteria**: `item.md` exists; repro is re-runnable; AC1 maps to the repro;
prevention criteria present; raw material linked from `refs/`.

### 4. Socratic gate
Always dispatch the `socrates` sub-agent with the draft's path (round 1). It
calibrates its own intensity — a confirmed cause with a contained fix gets a
fast pass with zero to two questions. For a bug report it bears down on root
cause vs symptom (does the cause survive another "why"?), evidence, whether
the fix prevents the class or just this instance, and completeness — are
there sibling instances of the same defect class elsewhere, or follow-up
work this fix implies?
- Relay the questions to the user **verbatim** and wait for answers — don't
  answer for them; the gate exists to make the user justify the item.
- Re-dispatch socrates with the answers to judge them (round 2); press
  `partial`/`evasive` answers once. Cap: two judged rounds, then proceed with
  anything unresolved carried into Open questions.
- If the dialogue changes the item — deeper cause to chase, severity
  re-graded, or not worth fixing now — update `item.md`, re-dispatch the
  investigator, or stop. Abandoning here is a success, not a failure.
- Write the distilled Q&A into a `## Justification` section in `item.md`
  (one line per question: claim challenged — reason that held). Long
  exchanges go to `refs/socratic-dialogue.md`, linked from the item.
- The user may waive the gate explicitly; record
  `Socratic gate waived by user.` in the Justification section.

**Success criteria**: socrates returned `pass` (or the cap was reached, or
the user waived); `## Justification` written into `item.md`.

### 5. Mark ready and publish
Publish per `~/.references/publish-work-item.md` — issue title
`fix: <bug title>`, issue body = summary, severity, reproduction steps, root
cause + confidence, and the Justification section. Exception: leave
`status: draft` if the cause is still a hypothesis and the user wants more
evidence first — publish happens either way, so the evidence trail lives
with the issue.

**Success criteria**: published and cross-linked per the shared procedure.

```
Suggested next steps:
- `/do <issue # or ./tmp/<id>/item.md>` — run the autonomous pipeline to fix and verify
- `/discussion [topic]` — if the bug exposed a design question bigger than the fix
```
