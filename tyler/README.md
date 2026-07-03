# tyler

A Claude Code-only subset of the delegation-loop workflow. Claude Code is the
harness for discussion, investigation, planning, and review; implementation is
delegated to Codex via `codex exec`.

## Model routing

Model effort follows the job:

| Phase | Where it runs | Model |
| --- | --- | --- |
| discussion / investigate / create-spec / create-plan | main session | Claude Fable |
| codebase exploration (`codebase-explorer` agent) | sub-agent | Sonnet |
| web research (`researcher` agent), plan review (`plan-reviewer` agent) | sub-agent | Opus |
| implementation (`/implement`, `/simple-plan`) | `codex exec` | GPT-5.5, effort `high` |
| implementation fallback (`implementer` agent) | sub-agent | Opus |
| review gate — Claude lane (`implementation-reviewer` agent) | sub-agent | Fable |
| review gate — Codex lane | `codex exec`, read-only | GPT-5.5, effort `xhigh` |

The Codex calls pin `-m gpt-5.5 -c model_reasoning_effort="..."` explicitly so
they survive `~/.codex/config.toml` drift. Requires the `codex` CLI; every
skill falls back to Claude sub-agents when it is unavailable.

## Keeping in sync

```bash
git -C "$REPO" pull --ff-only
rsync -a "$REPO/tyler/.claude/skills/" "$HOME/.claude/skills/"
rsync -a "$REPO/tyler/.claude/agents/" "$HOME/.claude/agents/"
```

Do not use `--delete` unless you want this repo to remove other local skills
or agents.
