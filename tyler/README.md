# tyler

A dual-harness development workflow (codenamed "Orchestra" in the build plan —
that name stays out of the runtime files so every dispatched model gets plain
definitions). Claude Code is the orchestrating harness: Fable makes the
judgment calls and dispatches sub-agents; Codex (GPT-5.5) runs the
engineering-heavy roles.

## The workflow

The flow separates *clarity*, *capture*, and *execution*:

1. **`/discussion`** — clarify, understand, figure out. General-purpose: it
   dispatches the code-researcher / `web-researcher` for questions and the
   investigator (with `app-user` for reproduction) when the topic is a
   defect. It produces clarity, never artifacts.
2. **`/create-feature` · `/create-epic` · `/create-issue`** — manually invoked
   capture skills. Each turns what the conversation established into a lean
   work item at `./tmp/<id>/item.md` (Feature Ticket, Epic Spec, or Bug
   Report, raw sources in `./tmp/<id>/refs/`) with verification criteria and a
   learning gate, then **publishes** it: a GitHub issue in the project repo
   plus a Notion work item (via the `notion` skill) holding `item.md` and
   every artifact, cross-linked both ways. `/create-issue` runs the
   investigator itself if the root cause isn't already established.
3. **`/do <issue # or item path>`** — the autonomous pipeline: pull the work
   item's artifacts from Notion into `./tmp/<id>/` (when given a GitHub
   issue) → plan + review loop → implement → verify → PR-review loop →
   PR + wrap-up, with `plan.md`/`wrapup.md` uploaded back to the Notion work
   item at the end. Deliberately high-level: the orchestrator judges how much
   research a plan needs and when each review loop has converged.
4. **`/postmortem`** — when a result falls short, root-cause it in *our
   system* (skill/agent/template), not just the code.

| Role | Runs on | Fallback / notes |
| --- | --- | --- |
| Orchestrator (conducts `/do`, all judgment) | main session — Fable | |
| Web research | Claude `web-researcher` — Sonnet | |
| Drive the app / verify | Claude `app-user` — Sonnet | |
| Explore codebase | **Codex** GPT-5.5 `medium`, read-only | Claude `code-researcher` (Sonnet) |
| Reproduce & root-cause | **Codex** GPT-5.5 `high`, workspace-write | Claude `investigator` (Opus) |
| Write the diff | **Codex** GPT-5.5 `medium`, workspace-write | Claude `implementer` (Opus) |
| Review the plan | **two parallel reviewers**: Codex GPT-5.5 `high` + Claude `plan-reviewer` (Opus) | Must-Fix gate = union of both |
| Review the diff + security | **two parallel reviewers**: Codex GPT-5.5 `high` + Claude `code-reviewer` (Opus) | Must-Fix gate = union of both |

Every Codex role is dispatched by the **`codex` skill**
(`.claude/skills/codex/`), the one place that knows the `codex exec`
mechanics per role — model, effort, sandbox (reviewers/researchers read-only
+ ephemeral; implementer workspace-write with `resume --last` across fix
rounds; investigator workspace-write for running tests, edits forbidden by
its role instructions), output capture, and status-line parsing. If the CLI
is missing or a dispatch fails, the caller falls back to the same-named
Claude sub-agent and flags it.

Review loops exit when **no Must Fix remains from either reviewer** — the
orchestrator judges when a loop has converged and flags anything left
unresolved in the wrap-up. High effort is for judgment-heavy roles (review,
investigation); implementation and exploration run at medium. Never route
customer-facing copy through Codex. `/do` and the three `/create-*` skills
are user-invoked only (`disable-model-invocation`) — the model never fires
them on its own.

Build tracker and design decisions: `../tmp/plan/build-plan.md`.

## Where formats live (single copy each — no duplicates to drift)

- **`tyler/references/`** (synced to `~/.references/` — harness-neutral,
  sibling of `~/.claude` and `~/.codex`) — anything referenced by more than
  one skill, or by any agent: the shared blocks (`verification-criteria.md`,
  `system-analysis.md`) and every agent's output format
  (`references/agents/<agent>/…`). Agents are flat `.md` files by design
  (Claude Code has no agent-folder format), so each agent's body carries a
  pointer — "Read `~/.references/agents/<name>/<format>.md`" — plus a few
  non-negotiable lines as a safety net if the file is missing.
- **`.claude/skills/<name>/references/`** — document formats produced by
  exactly one skill (feature-ticket, epic-spec, bug-report,
  implementation-plan, wrap-up-report, postmortem).
- `../tmp/templates/README.md` is the index mapping every format to its live
  home.

The six workflow skills above, plus two infrastructure skills the others
invoke — `codex` (dispatches Codex roles) and `notion` (the GitHub ↔ Notion
artifact bridge) — are the whole surface. Web research is the
`web-researcher` sub-agent, review lives inside `/do`, and all commit/PR
prep lives in `/do`'s final step.

## Project templates

`templates/` holds copyable per-project scaffolding: `AGENTS.md` (universal
agent instructions both harnesses read) and `CLAUDE.md` (points to AGENTS.md,
adds Claude-only notes, and carries the optional `Work-item tracking`
overrides — the Notion work-items database default lives in the notion
skill's `config.yaml`; a project sets `notion_data_source` only to publish
somewhere different). Copy both into a codebase root and fill in the
sections.

## Keeping in sync

```bash
git -C "$REPO" pull --ff-only
rsync -a "$REPO/tyler/.claude/skills/" "$HOME/.claude/skills/"
rsync -a "$REPO/tyler/.claude/agents/" "$HOME/.claude/agents/"
rsync -a "$REPO/tyler/references/" "$HOME/.references/"
rsync -a "$REPO/tyler/.codex/skills/" "$HOME/.codex/skills/"
```

The `.codex/skills/` role skills (implementer, plan-reviewer, code-reviewer,
code-researcher, investigator) are thin pointers into `~/.claude/agents/`
(role instructions) and `~/.references/` (output formats) — one copy of each
document across both harnesses.

`rsync` without `--delete` won't remove skills/agents that were deleted from
this repo — prune those by hand (or pass `--delete` if nothing hand-made lives
in your local folders).
