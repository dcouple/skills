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
   and `notion:`.
5. On `NOTION UNAVAILABLE`, the issue must still carry everything a remote
   `/do` needs — post each artifact as its own issue comment, wrapped in
   markers so Step 0 can harvest them back:

   ```
   <!-- ORCHESTRA-ARTIFACT path="refs/discussion.md" -->
   <full file content>
   <!-- /ORCHESTRA-ARTIFACT -->
   ```

   One comment per file (`item.md` itself is the issue body, so just the
   `refs/` files). A comment holds ~65K chars; split oversized files into
   `part=1/2` markers. Then tell the user Notion was skipped and the issue
   is self-contained.

Done when: the issue exists, every artifact is reachable from it (Notion
work item, or marker-delimited comments in degraded mode), and each of
issue / Notion page / item.md links to the others.
