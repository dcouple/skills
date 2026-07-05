---
name: codex
description: Dispatches one Codex (GPT-5.5) lane via `codex exec` — implementer, plan-reviewer, or code-reviewer — and returns the lane's report. Used by /do for its implement stage and both review loops; not normally invoked by the user directly. Use when a /do stage needs its Codex lane run, resumed for a fix loop, or re-reviewed.
argument-hint: "[role: implementer|plan-reviewer|code-reviewer] [inputs: item/plan paths, pass number]"
allowed-tools: Bash(codex:*), Bash(which:*), Read, Glob
---

# Codex lane dispatch

## Dispatch: $ARGUMENTS

Run one Codex lane non-interactively and hand its report back to the caller
(normally the `/do` Overseer). One dispatch = one role + its inputs.

## Role table

| Role | Model / effort | Sandbox | Session |
| --- | --- | --- | --- |
| `implementer` | `gpt-5.5` / `medium` | `workspace-write` | persistent — resume for fix loops |
| `plan-reviewer` | `gpt-5.5` / `high` | `read-only` | `--ephemeral` |
| `code-reviewer` | `gpt-5.5` / `high` | `read-only` | `--ephemeral` |

Effort is pinned per role — high is the review lane, medium the implement
lane. Never route customer-facing copy through Codex.

## Steps

### 1. Preflight
`which codex` — if missing, return `CODEX UNAVAILABLE` immediately so the
caller can fall back to the Claude agent lane. Confirm the role is in the
table; anything else is not a Codex lane.

**Success criteria**: codex resolved and role recognized (or `CODEX
UNAVAILABLE` returned).

### 2. Build the prompt
Every prompt names the role charter and format by absolute path — Codex reads
them itself (single copy, no inlining):

```
You are running as the <role> in the dcouple Orchestra.
Read your role charter at ~/.claude/agents/<role>.md (ignore the frontmatter —
tools/model are Claude-harness fields; your boundaries are in the body) and
your output format at ~/.claude/references/agents/<role>/<format>.md.
Inputs: work item <item path> · plan <plan path> · pass <k>/3
<role-specific inputs: prior findings by ID on pass 2+ (reviewers);
fix instructions (implementer fix loop)>
Print the report as your final message, in exactly the charter's format.
```

Format files: implementer → `implementation-result.md`; plan-reviewer /
code-reviewer → `review-report.md`.

**Success criteria**: prompt carries role, charter + format paths, and every
input path the role needs.

### 3. Execute
Run via Bash (timeout 600000 ms), from the repo root:

```bash
# reviewer lanes
codex exec -m gpt-5.5 -c model_reasoning_effort="high" -s read-only \
  --ephemeral --skip-git-repo-check -C <repo root> \
  -o <scratchpad>/codex-<role>-pass<k>.md "<prompt>"

# implementer lane (first run)
codex exec -m gpt-5.5 -c model_reasoning_effort="medium" -s workspace-write \
  --skip-git-repo-check -C <repo root> \
  -o <scratchpad>/codex-implementer.md "<prompt>"

# implementer fix loop — keep its session context
codex exec resume --last -o <scratchpad>/codex-implementer-fix<k>.md \
  "<combined review findings + fix instructions>"
```

**Success criteria**: exit 0 and the `-o` output file exists and is non-empty.

### 4. Return the report
Read the output file. Check the status line the format requires (reviewers:
`**Verdict:**` + `**Counts:**` with Must Fix count; implementer:
`**Status:** DONE | DONE_WITH_CONCERNS | BLOCKED | NEEDS_CONTEXT`). Return the
report verbatim to the caller, prefixed with one line:
`CODEX <role> pass <k>: <verdict/status>`.

If the run errored, timed out, or the report lacks its status line after one
retry, return `CODEX LANE FAILED: <reason>` plus whatever output exists — the
caller decides whether to fall back to the Claude agent.

**Success criteria**: caller received either a well-formed report or an
explicit `CODEX UNAVAILABLE` / `CODEX LANE FAILED`.

## Rules

- One dispatch, one role — never batch two roles into one Codex session.
- Reviewer lanes are read-only and ephemeral: a reviewer that edited files is
  a failed lane, treat its output as suspect.
- Don't launch a second implementer session while one is resumable —
  `resume --last` preserves its context across the fix loop.
