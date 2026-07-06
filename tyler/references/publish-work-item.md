# Publish a work item — shared procedure

Used by `/create-feature`, `/create-epic`, and `/create-issue` after
`item.md` is written. The caller supplies the issue title prefix (`feat:` or
`fix:`) and the issue body summary.

1. Set `status: ready` in `item.md`.
2. Create the GitHub issue: `gh issue create` in the project's repo (from the
   `Work-item tracking` section of the project's `CLAUDE.md`, or the current
   repo) — title `<prefix> <item title>`, body per the caller.
3. Invoke the `notion` skill, operation `publish`, with `./tmp/<id>/` and the
   issue URL — it creates the Notion work item and uploads `item.md` + every
   `refs/` file, returning the page URL.
4. Cross-link: add the Notion page URL to the GitHub issue body
   (`gh issue edit`), and record both in `item.md` frontmatter as `github:`
   and `notion:`. On `NOTION UNAVAILABLE`, proceed GitHub + local only and
   tell the user.

Done when: the issue exists, the Notion work item exists with all artifacts
(or its absence was reported), and each of issue / Notion page / item.md
links to the others.
