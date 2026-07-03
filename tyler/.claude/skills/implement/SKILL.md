---
name: implement
description: Executes an approved plan — by default delegating end-to-end implementation to Codex (GPT-5.5, effort high) via `codex exec`, with Claude implementer sub-agents as fallback. Always finishes with a dual review gate (Claude Fable reviewer + Codex GPT-5.5 xhigh reviewer). Use after a plan is approved.
argument-hint: "[plan file path] [claude|codex]"
disable-model-invocation: true
---

# Implementation Agent

## Plan to Execute: $ARGUMENTS

**Model routing:** implementation runs on GPT-5.5 (effort `high`) through the
Codex CLI; review runs on Claude Fable plus a GPT-5.5 `xhigh` Codex lane.
Executor selection from $ARGUMENTS:

- default (no keyword) or `codex`: Codex is the primary executor
- `claude`: use Claude implementer sub-agents instead
- If Codex is the executor but the `codex` CLI is unavailable (`which codex`
  fails) or the run errors out, fall back to the Claude implementer flow and
  say so explicitly in the final report.

## Step 1: Load and Review Plan

- If a path is provided: Read from $ARGUMENTS
- If no path: Find the most recent plan in `./tmp/ready-plans/`

Review the plan to understand: implementation phases, task checklist, technical requirements, dependencies between tasks, and success criteria.

## Step 2: Identify Dangerous Commands

**BEFORE ANY IMPLEMENTATION**, scan the plan for commands that must NOT be run automatically:

- Environment variable changes
- Package installations that change `package.json`
- Any destructive operations

**Collect into a "Manual Steps" list** and present to the user before proceeding.

> **Note:** Schema/migration handling is done automatically in Step 5 after implementation and review — do NOT handle it here.

## Step 3: Execute — Codex Primary Lane (default)

If the executor is **Codex** and the CLI is available, run **one** end-to-end
implementation via the Bash tool (timeout 600000 ms):

```bash
codex exec -m gpt-5.5 -c model_reasoning_effort="high" -s workspace-write \
  -C <repo root> --skip-git-repo-check \
  -o <scratchpad>/codex-implement-out.md \
  "implement the plan at [plan path]. Supporting brief / intent artifact: [path or ticket URL if available]. Treat the brief as the source of truth for why and the plan as the source of truth for how. You are the primary implementation authority for this run. Do not silently simplify or defer scope. A task is not complete until the end-to-end runtime or user-facing path is wired and still preserves the intended outcome. Run npm run typecheck and npm run lint as you work. Update the plan progress where practical and report any remaining manual steps or unresolved blockers clearly."
```

- Read the final message from the `-o` output file when the run completes.
- Do **not** launch multiple Codex runs for the same primary stream unless the
  user explicitly asks for more delegation.
- Do **not** also spawn a Claude implementer for the same primary stream.
- For follow-up fixes after review, prefer `codex exec resume --last "<fix
  instructions>"` so Codex keeps its session context, instead of a fresh run.

## Step 3b: Execute — Claude Fallback Lane

Use this lane when the user passed `claude`, or when the Codex CLI is missing
or its run failed.

1. **Break the plan into chunks**: group related tasks (2-5 per chunk),
   respecting dependencies — schema before API, backend before frontend,
   types before implementations:

   ```
   Phase 1: Foundation (Sequential) → Schema, types
   Phase 2: Core (Parallel) → Backend chunks, frontend chunks
   Phase 3: Integration (Sequential) → Connect frontend to backend
   ```

2. **Spawn implementers**: use `Task tool` with `subagent_type: "implementer"`
   for each chunk — parallel for independent chunks, sequential for dependent
   ones. Each agent prompt must include: specific tasks, relevant context,
   file paths, success criteria.

## Step 4: Dual Review Gate

After the primary execution lane completes, run **both** review lanes in
parallel and **wait for both** before continuing. Do not treat the first
result that returns as sufficient. (If the Codex CLI is unavailable, run only
the Claude lane and note that in the report.)

**Claude review lane (Fable):**

```
Task tool:
  subagent_type: "implementation-reviewer"
  prompt: "Review the implementation against the supporting brief / intent artifact first, then against the plan at [path].
    Treat the brief as the source of truth for why and the plan as the source of truth for how.
    Run npm run typecheck and npm run lint.
    Check every task in the plan was completed.
    Flag any gaps, missing integrations, convention violations, or brief-intent regressions.
    Report completeness status for each plan task."
```

**Codex review lane (GPT-5.5 xhigh, read-only):**

```bash
codex exec -m gpt-5.5 -c model_reasoning_effort="xhigh" -s read-only \
  -C <repo root> --skip-git-repo-check --ephemeral \
  -o <scratchpad>/codex-review-out.md \
  "Review the uncommitted implementation diff (git diff and untracked files) against the supporting brief / intent artifact first, then against the plan at [plan path]. Focus on whether the code preserves the intended outcome, actually satisfies every plan task, and reaches the finish line at runtime: missing plan tasks, runtime wiring, auth and permission gaps, transaction boundaries, race conditions, background-job registration, dead code paths. End your response with exactly one line: VERDICT: APPROVED or VERDICT: REVISE followed by the blocking reasons."
```

Parse the `VERDICT:` line from the Codex output file.

**Fix-and-review-again loop:**

- If either lane flags blocking issues, feed the combined findings back to the
  executor — `codex exec resume --last` for the Codex lane, or the implementer
  sub-agent for the Claude lane — then re-run **both** review lanes.
- Repeat until both lanes pass, capping at 3 iterations; if still failing,
  stop and report the unresolved findings to the user.

## Step 5: Generate Dev Migration SQL (If Schema Changed)

After the review gate passes, check if `schema.ts` was modified:

```bash
git diff origin/main --name-only | grep schema.ts
```

If schema.ts was changed:

1. Run `npm run db:diff:dev` and capture the output.
2. Present TWO separate blocks to the user:

**Schema changes (migration SQL):**
```sql
BEGIN;
-- the generated migration SQL here
COMMIT;
```

**Apply migration to dev database:**
```bash
npm run db:migrate:dev
```
(Or whatever the actual command is — run it and show the result.)

3. Only include additive SQL (CREATE, ADD). If destructive SQL (DROP, ALTER type) appears, flag it and ask the user to confirm before proceeding.

If schema.ts was NOT changed, skip this step silently.

## Step 6: Move Plan to Done

Once all tasks pass review and the implementation is complete, move the plan file from `./tmp/ready-plans/` to `./tmp/done-plans/`:

```bash
mv ./tmp/ready-plans/<plan-file>.md ./tmp/done-plans/
```

Create `./tmp/done-plans/` if it doesn't exist. Only move the plan when all tasks are confirmed complete — if the reviewer found unresolved issues, wait until they are fixed.

## Step 7: Present Results

Present the combined findings from both review lanes to the user:

```
Implementation complete.

Executor: Codex (gpt-5.5, effort high) | Claude implementer (fallback: [reason])

Quality checks:
  typecheck: PASS/FAIL
  lint: PASS/FAIL

Review gate:
  Claude reviewer (Fable): PASS/FAIL — [key findings]
  Codex reviewer (gpt-5.5 xhigh): VERDICT: APPROVED/REVISE — [key findings]
  Fix-and-review iterations: [count]

Completeness: X/Y tasks done
[List any MISSING or PARTIAL items]

Issues found: [count]
[Summarize key issues if any]

Manual steps remaining:
- [ ] [Dangerous commands from Step 2, if any]

Schema changes:
  [If Step 5 ran, show the migration SQL and apply command here]
  [If no schema changes, show "None"]

Plan moved to: ./tmp/done-plans/<plan-file>.md

Next steps:
- Fix any issues flagged above
- `/prepare-pr` — Commit, build, and open/update a PR
```

If the reviewer found issues, offer to fix them before the user commits. Only move the plan to `done-plans/` after all issues are resolved.
