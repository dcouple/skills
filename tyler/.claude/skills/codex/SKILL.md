---
name: codex
description: Dispatches one Codex (GPT-5.5) sub-agent via `codex exec` — implementer, backend-verifier, plan-reviewer, code-reviewer, code-researcher, or investigator — and returns its report. Used by /do, /discussion, and /create-issue whenever one of these roles runs; not normally invoked by the user directly. Use when a pipeline stage needs its Codex sub-agent dispatched, resumed for a fix round, or re-run.
argument-hint: "[role] [inputs: item/plan paths, question, pass number]"
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
| `backend-verifier` | `gpt-5.5` / `medium` | `workspace-write` | `--ephemeral` |
| `plan-reviewer` | `gpt-5.5` / `high` | `read-only` | `--ephemeral` |
| `code-reviewer` | `gpt-5.5` / `high` | `read-only` | `--ephemeral` |
| `code-researcher` | `gpt-5.5` / `medium` | `read-only` | `--ephemeral` |
| `investigator` | `gpt-5.5` / `high` | `workspace-write` | `--ephemeral` |

High effort is for judgment-heavy roles (review, investigation); medium for
implementation, exploration, and verification. The investigator and
backend-verifier get `workspace-write` so they can run tests and scripts,
but their charters forbid editing project files. The `implementer` role is
for backend/ops work only — frontend web/mobile code and customer-facing
copy go to the Claude `frontend-implementer` sub-agent, never through Codex.

## Steps

### 1. Build the prompt
Every prompt names the role instructions and output format by absolute path —
Codex reads them itself, so there is exactly one copy of each:

```
You are acting as the <role> in an automated software-development pipeline
conducted by the Overseer, a separate orchestrating agent. Your report is
consumed by the Overseer, not by a human.

First read these two files:
1. Your role instructions: <instructions path per the mapping below>.
2. Your output format: <format path per the mapping below> — your
   final message must follow it exactly.

Inputs for this run:
- work item: <item path>
- plan: <plan path, if the role uses one>
- question / defect report: <for code-researcher / investigator>
- review pass: <k>/3 <reviewers only>
- prior findings by ID: <reviewers, pass 2+> / fix instructions: <implementer fix rounds>

Print the report as your final message, in exactly the specified format.
```

Role instructions: Codex-only roles (implementer, investigator,
backend-verifier) → `~/.references/agents/<role>/instructions.md` · roles
with a Claude twin (code-researcher, plan-reviewer, code-reviewer) →
`~/.claude/agents/<role>.md` (tell Codex to follow the body and ignore the
YAML frontmatter — it applies to a different harness).

Format files, under `~/.references/agents/<role>/`: implementer →
`implementation-result.md` · plan-reviewer / code-reviewer →
`review-report.md` · code-researcher → `codebase-findings.md` ·
investigator → `root-cause-finding.md` · backend-verifier →
`../frontend-verifier/verification-result.md` (shared verifier format,
verify mode).

**Success criteria**: prompt carries the role, both file paths, and every
input the role needs — nothing assumed from this conversation.

### 2. Execute
Run via Bash (timeout 600000 ms), from the repo root:

```bash
# effort / sandbox / --ephemeral per the role table
codex exec -m gpt-5.5 -c model_reasoning_effort="<effort>" -s <sandbox> \
  [--ephemeral] --skip-git-repo-check -C <repo root> \
  -o <scratchpad>/codex-<role>-<n>.md "<prompt>"

# implementer fix round — keep its session context
codex exec resume --last -o <scratchpad>/codex-implementer-fix<k>.md \
  "<combined review findings + fix instructions>"
```

Parallel dispatches (e.g. several code-researchers, or a reviewer alongside a
Claude sub-agent) run as background Bash calls.

**Success criteria**: exit 0 and the `-o` output file exists and is non-empty.

### 3. Return the report
Read the output file. Check the status line the format requires (reviewers:
`**Verdict:**` + `**Counts:**` with the Must Fix count · implementer:
`**Status:** DONE | DONE_WITH_CONCERNS | BLOCKED | NEEDS_CONTEXT` ·
code-researcher: `**Bottom line:**` · investigator: `**Root cause:**` with a
confidence word · backend-verifier: `**Verdict:**` pass|fail). Return the
report verbatim to the caller, prefixed with one line:
`CODEX <role>: <status line>`.

If the run errored, timed out, or the report lacks its status line after one
retry, return the error plus whatever output exists to the caller.

**Success criteria**: caller received a well-formed report (or the error
after one retry).

## Rules

- One dispatch, one role — never batch two roles into one Codex session.
- Reviewer and researcher dispatches are read-only: one that edited files is
  a failed run, treat its output as suspect.
- Don't launch a second implementer session while one is resumable —
  `resume --last` preserves its context across fix rounds.
