---
name: simple-plan
description: Quick gut-check before implementing when the user directly asks you to do something (e.g. "add X", "fix Y", "change Z"). Investigates, proposes a lightweight plan, and implements after approval. Use this instead of /create-plan when the user wants something done, not a formal plan.
argument-hint: "[what the user wants done]"
allowed-tools: Read, Grep, Glob, WebFetch, Bash, Task
---

# Simple Plan

When the user directly asks me to make a change, I will first investigate and propose a plan before implementing anything. This ensures alignment before any code is written.

## My Plan Will Include

### Current State
- Root cause analysis explaining the current state
- File references and code snippets where relevant

### Proposed Changes
- Clear explanation of what needs to change
- File references and code snippets where necessary
- Task list of all work to be done

### My Advice
Feedback from a principal engineer perspective, providing overall architectural and implementation guidance.

## Process

1. Investigate the codebase first (spawn `codebase-explorer` sub-agents for broad searches)
2. Present the plan to the user
3. **Only when the user approves** will I proceed
4. After approval, delegate execution to Codex (GPT-5.5, effort high) via the Bash tool (timeout 600000 ms), passing the entire plan directly as the prompt:

   ```bash
   codex exec -m gpt-5.5 -c model_reasoning_effort="high" -s workspace-write \
     -C <repo root> --skip-git-repo-check \
     -o <scratchpad>/codex-simple-plan-out.md \
     "<the full approved plan, plus: Do not silently simplify or defer scope. Run the project's typecheck/lint as you work and report any blockers.>"
   ```

   If the `codex` CLI is unavailable or the run fails, fall back to spawning an `implementer` sub-agent with the same plan, and say so in the report.
5. After execution, run one review pass: spawn an `implementation-reviewer` sub-agent (Fable) to check the diff against the plan. Feed any blocking findings back to the executor (`codex exec resume --last` for Codex) and re-review until clean.

## Notes

- Instructions must be very clear with code snippets and file paths
- I will not implement anything until the user approves

User Query: $ARGUMENTS
