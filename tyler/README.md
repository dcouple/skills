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

| Role | Agent | Phase-1 model | Phase-2 target |
| --- | --- | --- | --- |
| Overseer (conducts `/do`, all judgment) | main session | Fable | Fable |
| Explore codebase | `code-researcher` | Sonnet | Sonnet |
| Web research | `web-researcher` | Sonnet | Sonnet |
| Drive the app / verify | `app-user` | Sonnet | Sonnet |
| Write the diff | `implementer` | Opus | `codex exec` GPT-5.5, effort `medium` |
| Review the plan | `plan-reviewer` | Opus | `codex exec` GPT-5.5, effort `high` |
| Review the diff + security | `code-reviewer` | Opus | `codex exec` GPT-5.5, effort `high` |
| Reproduce & root-cause | `investigator` | Opus | `codex exec` GPT-5.5, effort `high` |

Review loops exit on **zero Must Fix** (cap 3 passes; cap-outs are flagged in
the wrap-up). Phase 2 also adds **dual reviewers** — Codex high + Claude Opus
in parallel, Must-Fix gate = the union of both. High effort is the
review/investigation lane; implementation runs at medium. Never route
customer-facing copy through Codex.

Build tracker and design decisions: `../tmp/plan/build-plan.md`. Document
formats: `../tmp/templates/` (skills carry their own copies in `references/`).

## Utility skills

`/commit`, `/prepare-pr`, `/release`, `/research-web`, `/review` are standalone
utilities outside the Orchestra: selective commits, manual PR prep, release
PRs, deep web research, and reviewing PRs that didn't come out of `/do`.

## Keeping in sync

```bash
git -C "$REPO" pull --ff-only
rsync -a "$REPO/tyler/.claude/skills/" "$HOME/.claude/skills/"
rsync -a "$REPO/tyler/.claude/agents/" "$HOME/.claude/agents/"
```

`rsync` without `--delete` won't remove skills/agents that were deleted from
this repo — prune those by hand (or pass `--delete` if nothing hand-made lives
in your local folders).
