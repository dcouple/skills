# tyler

A Claude Code-only variant of the delegation-loop workflow. Claude Code is the
harness; Fable conducts; sub-agents do the specialized work; implementation and
review swap onto Codex in Phase 2.

## The Orchestra

The flow separates *clarity*, *capture*, and *execution*:

1. **`/discussion`** — clarify, understand, figure out. General-purpose: it
   spawns `code-researcher` / `web-researcher` for questions and the
   `investigator` (with `app-user` for reproduction) when the topic is a
   defect. It produces clarity, never artifacts.
2. **`/create-feature` · `/create-epic` · `/create-issue`** — manually invoked
   capture skills. Each turns what the conversation established into a lean
   work item at `./tmp/<id>/item.md` (Feature Ticket, Epic Spec, or Bug
   Report, raw sources in `./tmp/<id>/refs/`) with verification criteria and a
   learning gate. `/create-issue` runs the investigator itself if the root
   cause isn't already established.
3. **`/do <item>`** — the autonomous pipeline: plan → plan-review loop →
   implement → verify → clean up → PR-review loop → PR + wrap-up.
4. **`/postmortem`** — when a result falls short, root-cause it in *our
   system* (skill/agent/template), not just the code.

| Role | Runs on | Notes |
| --- | --- | --- |
| Overseer (conducts `/do`, all judgment) | main session — Fable | |
| Explore codebase | `code-researcher` — Sonnet | |
| Web research | `web-researcher` — Sonnet | |
| Drive the app / verify | `app-user` — Sonnet | |
| Write the diff | **Codex** GPT-5.5 `medium`, workspace-write | via the `codex` skill; Claude `implementer` (Opus) is the fallback |
| Review the plan | **dual lane**: Codex GPT-5.5 `high` + `plan-reviewer` (Opus) | in parallel; Must-Fix gate = union of both |
| Review the diff + security | **dual lane**: Codex GPT-5.5 `high` + `code-reviewer` (Opus) | in parallel; Must-Fix gate = union of both |
| Reproduce & root-cause | `investigator` — Opus | Codex swap deferred — stays a Claude sub-agent for interactive dispatch |

Codex lanes are dispatched by the **`codex` skill**
(`.claude/skills/codex/`), which wraps `codex exec` per role — model, effort,
sandbox (reviewers read-only + ephemeral; implementer workspace-write with
`resume --last` across fix loops), output capture, and verdict parsing. If
the CLI is missing or a lane fails, `/do` degrades to single-lane Claude
agents and flags it in the wrap-up.

Review loops exit on **zero Must Fix from both lanes** (cap 3 passes;
cap-outs are flagged in the wrap-up). High effort is the review lane;
implementation runs at medium. Never route customer-facing copy through
Codex.

Build tracker and design decisions: `../tmp/plan/build-plan.md`.

## Where formats live (single copy each — no duplicates to drift)

- **`.claude/references/`** — anything referenced by more than one skill, or by
  any agent: the shared blocks (`verification-criteria.md`,
  `system-analysis.md`) and every agent's output format
  (`references/agents/<agent>/…`). Agents are flat `.md` files by design
  (Claude Code has no agent-folder format), so each agent's body carries a
  pointer — "Read `~/.claude/references/agents/<name>/<format>.md`" — plus a
  few non-negotiable lines as a safety net if the file is missing.
- **`.claude/skills/<name>/references/`** — document formats produced by
  exactly one skill (feature-ticket, epic-spec, bug-report,
  implementation-plan, wrap-up-report, postmortem).
- `../tmp/templates/README.md` is the index mapping every format to its live
  home.

The six skills above are the whole surface — no standalone utilities. Web
research is the `web-researcher` agent, review is the `code-reviewer` agent,
and all commit/PR prep lives in `/do`'s final step.

## Keeping in sync

```bash
git -C "$REPO" pull --ff-only
rsync -a "$REPO/tyler/.claude/skills/" "$HOME/.claude/skills/"
rsync -a "$REPO/tyler/.claude/agents/" "$HOME/.claude/agents/"
rsync -a "$REPO/tyler/.claude/references/" "$HOME/.claude/references/"
rsync -a "$REPO/tyler/.codex/skills/" "$HOME/.codex/skills/"
```

The `.codex/skills/` role skills (implementer, plan-reviewer, code-reviewer)
are thin pointers into `~/.claude/agents/` and `~/.claude/references/` — the
charters and formats stay single-copy across both harnesses.

`rsync` without `--delete` won't remove skills/agents that were deleted from
this repo — prune those by hand (or pass `--delete` if nothing hand-made lives
in your local folders).
