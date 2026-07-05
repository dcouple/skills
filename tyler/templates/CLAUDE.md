# CLAUDE.md — template

> Copy this file to a codebase's root as `CLAUDE.md` and fill in each section.
> Universal instructions live in `AGENTS.md` (single copy, both harnesses);
> this file adds only what is Claude-specific. Delete this header block after
> copying.

See @AGENTS.md for the project overview, commands, architecture, conventions,
and boundaries. Everything there applies here — do not duplicate it.

## Work-item tracking

The workflow skills (`/create-feature`, `/create-epic`, `/create-issue`,
`/do`) publish every work item as a GitHub issue and mirror its artifacts to
a Notion work item (see the `notion` skill).

```yaml
github_repo: <owner>/<repo>   # where gh issue create targets; omit to use the current repo
# notion_data_source: <ID or URL>   # OVERRIDE only — the default lives in the
#                                   # notion skill's config.yaml; set this only
#                                   # if this repo publishes to a different database
```

Work-item artifacts (item.md, refs/, plan.md, wrapup.md) live locally under
`./tmp/<id>/` during a run and in the Notion work item durably. `./tmp/` is
scratch — never commit it.

## Claude-specific notes

- Sub-agent and skill definitions come from the user-level setup
  (`~/.claude/`, `~/.references/`, `~/.codex/`) — this repo does not carry
  its own.
- <anything else only Claude needs: MCP servers to prefer, browser-automation
  notes for the app-user agent, model-routing exceptions for this project>
