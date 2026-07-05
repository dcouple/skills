---
name: codex
description: Dispatches one Codex (GPT-5.5) sub-agent via `codex exec` — implementer, plan-reviewer, code-reviewer, code-researcher, or investigator — and returns its report. Used by /do, /discussion, and /create-issue whenever one of these roles runs; not normally invoked by the user directly. Use when a pipeline stage needs its Codex sub-agent dispatched, resumed for a fix round, or re-run.
argument-hint: "[role] [inputs: item/plan paths, question, pass number]"
allowed-tools: Bash(codex:*), Bash(which:*), Read, Glob
---

# Dispatch a Codex sub-agent

## Dispatch: $ARGUMENTS

Run one Codex sub-agent non-interactively and hand its report back to the
caller. One dispatch = one role + its inputs. Codex is the OpenAI coding
agent CLI; each dispatch is a fresh GPT-5.5 session that knows nothing about
this conversation — the prompt must carry everything the role needs.

## Role table

| Role | Model / effort | Sandbox | Session |
| --- | --- | --- | --- |
| `implementer` | `gpt-5.5` / `medium` | `workspace-write` | persistent — resume for fix rounds |
| `plan-reviewer` | `gpt-5.5` / `high` | `read-only` | `--ephemeral` |
| `code-reviewer` | `gpt-5.5` / `high` | `read-only` | `--ephemeral` |
| `code-researcher` | `gpt-5.5` / `medium` | `read-only` | `--ephemeral` |
| `investigator` | `gpt-5.5` / `high` | `workspace-write` | `--ephemeral` |

High effort is for judgment-heavy roles (review, investigation); medium for
implementation and codebase exploration. The investigator gets
`workspace-write` so it can run tests and repro scripts, but its charter
forbids editing project files. Never route customer-facing copy through
Codex.

## Steps

### 1. Preflight
`which codex` — if missing, return `CODEX UNAVAILABLE` immediately so the
caller can fall back to the Claude sub-agent of the same name. Confirm the
role is in the table; anything else is not a Codex role.

**Success criteria**: codex resolved and role recognized (or `CODEX
UNAVAILABLE` returned).

### 2. Build the prompt
Every prompt names the role instructions and output format by absolute path —
Codex reads them itself, so there is exactly one copy of each:

```
You are acting as the <role> in an automated software-development pipeline
conducted by a separate orchestrating agent. Your report is consumed by that
orchestrator, not by a human.

First read these two files:
1. Your role instructions: ~/.claude/agents/<role>.md — follow the body;
   ignore the YAML frontmatter (tools/model apply to a different harness).
2. Your output format: ~/.references/agents/<role>/<format file> — your
   final message must follow it exactly.

Inputs for this run:
- work item: <item path>
- plan: <plan path, if the role uses one>
- question / defect report: <for code-researcher / investigator>
- review pass: <k>/3 <reviewers only>
- prior findings by ID: <reviewers, pass 2+> / fix instructions: <implementer fix rounds>

Print the report as your final message, in exactly the specified format.
```

Format files: implementer → `implementation-result.md` · plan-reviewer /
code-reviewer → `review-report.md` · code-researcher →
`codebase-findings.md` · investigator → `root-cause-finding.md`.

**Success criteria**: prompt carries the role, both file paths, and every
input the role needs — nothing assumed from this conversation.

### 3. Execute
Run via Bash (timeout 600000 ms), from the repo root:

```bash
# read-only roles (plan-reviewer, code-reviewer, code-researcher)
codex exec -m gpt-5.5 -c model_reasoning_effort="<per role table>" \
  -s read-only --ephemeral --skip-git-repo-check -C <repo root> \
  -o <scratchpad>/codex-<role>-<n>.md "<prompt>"

# investigator (may run tests/repro scripts; charter forbids edits)
codex exec -m gpt-5.5 -c model_reasoning_effort="high" -s workspace-write \
  --ephemeral --skip-git-repo-check -C <repo root> \
  -o <scratchpad>/codex-investigator.md "<prompt>"

# implementer (first run)
codex exec -m gpt-5.5 -c model_reasoning_effort="medium" -s workspace-write \
  --skip-git-repo-check -C <repo root> \
  -o <scratchpad>/codex-implementer.md "<prompt>"

# implementer fix round — keep its session context
codex exec resume --last -o <scratchpad>/codex-implementer-fix<k>.md \
  "<combined review findings + fix instructions>"
```

Parallel dispatches (e.g. several code-researchers, or a reviewer alongside a
Claude sub-agent) run as background Bash calls.

**Success criteria**: exit 0 and the `-o` output file exists and is non-empty.

### 4. Return the report
Read the output file. Check the status line the format requires (reviewers:
`**Verdict:**` + `**Counts:**` with the Must Fix count · implementer:
`**Status:** DONE | DONE_WITH_CONCERNS | BLOCKED | NEEDS_CONTEXT` ·
code-researcher: `**Bottom line:**` · investigator: `**Root cause:**` with a
confidence word). Return the report verbatim to the caller, prefixed with one
line: `CODEX <role>: <status line>`.

If the run errored, timed out, or the report lacks its status line after one
retry, return `CODEX ROLE FAILED: <reason>` plus whatever output exists — the
caller decides whether to fall back to the Claude sub-agent.

**Success criteria**: caller received either a well-formed report or an
explicit `CODEX UNAVAILABLE` / `CODEX ROLE FAILED`.

## Rules

- One dispatch, one role — never batch two roles into one Codex session.
- Reviewer and researcher dispatches are read-only: one that edited files is
  a failed run, treat its output as suspect.
- Don't launch a second implementer session while one is resumable —
  `resume --last` preserves its context across fix rounds.
