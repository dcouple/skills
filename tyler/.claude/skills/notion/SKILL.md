---
name: notion
description: The Notion bridge for work items — creates a Notion work item mirroring a GitHub issue, uploads artifacts (item.md, refs/, plan.md, wrapup.md) to it, and pulls a work item's artifacts down to ./tmp/<id>/. Used by /create-feature, /create-epic, /create-issue (publish) and /do (pull before work, upload after). Use when a work item needs to be published to, updated in, or fetched from Notion.
argument-hint: "[publish|upload|pull] [work-item id, GitHub issue #/URL, or Notion page URL]"
---

# Notion bridge

## Request: $ARGUMENTS

Notion is the durable home for work-item artifacts; GitHub carries the issue
and the PR; `./tmp/<id>/` is the local working copy. This skill is the one
place that knows how to move material between the three. One invocation = one
operation: `publish`, `upload`, or `pull`.

## Setup (every invocation)

1. **Load the Notion tools**: use ToolSearch with a query like
   `+notion search create fetch update attachment` and load what the
   operation needs (search, fetch, create-pages, update-page,
   create-attachment). Tool names vary by connector — match on the `notion`
   prefix. If no Notion tools resolve and no `notion` CLI is on PATH, return
   `NOTION UNAVAILABLE: <what was tried>` — the caller proceeds
   GitHub + local only and says so.
2. **Find the target database** — resolution order, most specific wins:
   1. The project `CLAUDE.md`'s `Work-item tracking` section
      (`notion_data_source`) — per-repo override only.
   2. `config.yaml` in this skill's directory — the global default; also
      defines the database's property names.
   3. Neither set → search Notion for the work-items database once, confirm
      the match with the user, and offer to save it into this skill's
      `config.yaml` so the search never repeats.

**Success criteria**: tools loaded and a data source resolved (or an explicit
`NOTION UNAVAILABLE`).

## Operation: publish  (called by /create-feature, /create-epic, /create-issue)

Inputs: `./tmp/<id>/` with a ready `item.md`, plus the GitHub issue URL the
caller just created.

1. Dedup first: query the data source for a page whose GitHub-issue-URL
   property equals this issue — an exact property query, not workspace
   full-text search. Found → this publish updates that page in place.
2. Create (or update) one page in the work-items data source:
   - Title: the item's title (same as the GitHub issue title).
   - Properties (as the database schema allows): GitHub issue URL, work-item
     type (`feature-ticket | epic-spec | bug-report`), status `ready`.
   - Page body: the full `item.md` content — the human-readable mirror.
3. Upload every file in `./tmp/<id>/refs/` to the page (attachments for
   binaries, sub-pages for markdown), named as on disk. Also attach the RAW
   `item.md` and each markdown ref as file attachments: Notion re-renders
   page bodies (tables, checkboxes, frontmatter fences all mutate), so the
   attachments are the canonical bytes and the body is just for reading.
4. Return the new page URL to the caller — the caller cross-links it in both
   directions: append the canonical line `**Notion:** <page URL>` to the end
   of the GitHub issue body (`gh issue edit --body-file`), and write the URL
   into `item.md`'s frontmatter as `notion:`. When publish runs ad hoc (no
   calling skill), do both edits as part of this operation. The exact
   `**Notion:**` line format matters — `pull` looks for it.

**Success criteria**: page exists with the item body and every `refs/` file;
page URL returned.

## Operation: upload  (called by /do at wrap-up, or ad hoc)

Inputs: the work item's Notion page URL (from `item.md` frontmatter or the
GitHub issue body) and the files to add (`plan.md`, `wrapup.md`, new refs).

1. Add each file to the page as in publish step 2 — update in place if a
   sub-page with the same name exists (a re-run replaces, never duplicates).
2. Update the page's status property to match `item.md` (`done` after a
   successful `/do`), and add the PR URL if provided.

**Success criteria**: every input file visible on the page; status/PR current.

## Operation: pull  (called by /do before work)

Inputs: a GitHub issue number/URL or a Notion page URL.

1. If given a GitHub issue: `gh issue view` and find the canonical
   `**Notion:** <url>` line in its body (fall back to any Notion page URL
   found anywhere in the body). No Notion link → return `NO NOTION ITEM`
   (the caller falls back to treating the issue body itself as the work
   item).
2. Fetch the page. Derive `<id>` from the item's frontmatter `id:` (or slug
   the title). Prefer the RAW `item.md` file attachment when present — it's
   byte-identical to what was published; reconstruct from the page body only
   when no attachment exists.
3. Fetch every sub-page and attachment; save each to `./tmp/<id>/refs/<name>`
   (same preference: raw attachment over rendered sub-page). If a plan from
   a prior run exists, save it as `./tmp/<id>/plan.md`.
4. Set the page's status property to `in-progress` — the database stays an
   honest at-a-glance board while `/do` runs (`upload` flips it to `done`).
5. Return the local paths written.

**Success criteria**: `./tmp/<id>/item.md` exists locally and every artifact
on the page has a local copy under `./tmp/<id>/`.

## Rules

- Notion is the mirror, `item.md` on disk is the working truth during a run —
  push at milestones (publish, wrap-up), don't sync continuously.
- Never store secrets in Notion pages; artifacts only.
- One work item = one page. Dedup by exact GitHub-issue-URL property query
  against the data source (workspace full-text search only as a fallback) —
  re-publishing must update, not duplicate.
