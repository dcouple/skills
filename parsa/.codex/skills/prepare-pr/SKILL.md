---
name: prepare-pr
description: "Prepare scoped changes and verification for an opened or updated pull request."
---

# Prepare PR

Finish the requested branch-to-PR handoff using this repository's conventions.
Read only plans relevant to this task; a done-plan is helpful context, not a
prerequisite to preparing ad-hoc changes.

## Scope and branch

Inspect status, staged changes, diff, remote default branch, and any existing PR.
Create a work branch or isolated worktree when needed. Include only authorized
changes; leave unrelated edits and `./tmp/` scratch out of commits. Ask only if
ownership or the intended base cannot be resolved from the task and repository.

Fetch the intended base. Integrate upstream according to repository policy;
rebase only the task-owned branch. Resolve clear conflicts and ask about
semantic conflicts that change intent. Revalidate affected behavior after
integration. Stage explicit paths or hunks and inspect the staged diff for
secrets before committing.

## Validation and migration notes

Use checks appropriate to the touched surfaces and required by the repository.
Reuse current passing evidence until code, dependencies, configuration, or the
environment changes. Fix task-caused failures before declaring the PR ready.
If schema changes need migrations, discover the repository's generation
workflow and include the actual reviewed migration or SQL with application
ordering in the PR. Never run production migration commands or silently drop
destructive statements from the proposed change.

## PR content and visuals

Lead with the problem, what changed, and the resulting behavior. Include checks
with results, remaining manual work, and material risks. Follow any required
repository template. Preserve author-owned text when updating an existing PR;
replace only the agent-owned marked sections.

Use `excalidraw-pr-diagrams` when a before/after relationship, architecture, or
flow needs visual explanation, or the repo requires it. A simple prose or
configuration change can use a concise explanation without generating media.
Load that skill's publishing contract before any media upload. Keep generated
working files outside the repository.

For durable media, an existing `pr-assets` release upload needs its own exact
structured grant, such as `{"action":"upload_release_asset","repo":"owner/name","tag":"pr-assets"}`.
Creating a release or changing its metadata is a separate grant, such as
`{"action":"create_release","repo":"owner/name","tag":"pr-assets"}`.
Generic PR authorization grants neither. Without the needed grant, prepare
filenames, manifest, exact commands, and marked Markdown locally; report the
publication blocker and continue independent PR preparation. Do not use a
temporary host, overwrite assets, or claim a required visual is published.

When visuals exist, retain the diagram skill's unique naming, collision checks,
manifest, and direct-content verification. Audit image references in the PR
sections being updated and retain verified durable URLs.

## Push, open, and verify

Push the task branch; use `--force-with-lease` only for an authorized rewrite
of its already-pushed history after checking remote state. Create or update
one PR with the intended base and head using structured input or `--body-file`.
Read back the persisted body, URL, branch, head SHA, base, and draft state.
Report a non-draft PR as ready only when required checks and requested evidence
are complete. Otherwise use a draft and state the exact blocker.

Inspect the title and body for accuracy and reader clarity. A separate
`cold-read` or refactor pass runs only when requested; it is not an automatic
PR gate. Continue into requested QA or review-feedback stages when authorized.
Stop at the requested PR handoff; do not merge, bump a version, release, deploy,
or change production without its own authorization.
