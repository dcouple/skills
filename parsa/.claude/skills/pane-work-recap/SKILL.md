---
name: pane-work-recap
description: Reconstruct recent work across Pane sessions, Git branches, PRs, and relevant agent logs without changing work state.
---

# Pane work recap

## Scope

- Use the requested repositories and time window; distinguish rolling durations from local calendar dates and state the timezone.
- For “recently,” use active work plus roughly seven days of recent activity unless context suggests otherwise.
- Read only: do not create panes, change branches, edit PRs, or start implementation.

## Collect evidence

1. Discover the active instance with `runpane doctor --json`; use documented public commands available in the installed version.
2. Read pane/repository state, for example `runpane panes list --json`, `runpane repos list --json`, and `runpane agent-context --json` when supported.
3. Resolve branches and PRs from actual worktrees and saved metadata. Treat slug-based matches for removed worktrees as inferences.
4. Read current GitHub state when authenticated; separate multiple PRs from a reused pane.
5. Inspect only relevant agent logs when public state is insufficient. Extract summaries, checks, and evidence links rather than dumping transcripts.

## Fallbacks

- Discover the data directory from runtime output, `PANE_DIR`, or supplied configuration; never hardcode a user's checkout path.
- If SQLite inspection is needed, open an existing database read-only and inspect its schema first.
- `updated_at` on an archived session is only a proxy when `archived_at` is missing; SQLite timestamps may be UTC.
- Agent logs may live under `${CODEX_HOME:-$HOME/.codex}/sessions` or `${CLAUDE_CONFIG_DIR:-$HOME/.claude}/projects`; match by workspace/branch/PR before reading.
- Label unavailable authentication, removed worktrees, missing history, and ambiguous matches.

## Report

- Lead with what happened in the requested window, grouped by real workstream.
- Distinguish locally completed, PR open, merged, released, and deployed; none proves the next stage automatically.
- Include relevant PR links, agent/check evidence, and what remains active.
- Use a small table for dense mappings; otherwise use short sections and bullets.

## Saved recap

- No report file is needed by default. If requested and Grain is connected, save it in the supplied task folder, or `Development Artifacts/YYYY-MM-DD-<task>`.
- Keep needed local copies and privacy limits; without Grain, use the requested local handoff silently.
