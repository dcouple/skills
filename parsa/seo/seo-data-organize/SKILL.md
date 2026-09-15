---
name: seo-data-organize
description: Preserve SEO snapshots, decisions, and experiment history with a browsable index without deleting working data.
---

# Organize SEO history

Keep the current context easy to find and prior evidence recoverable.

## Preserve the run

- Use the existing project storage convention or shared task folder.
- Copy the current briefing, strategy, and relevant data into a dated snapshot; keep working files intact.
- Include a time or run identifier when multiple snapshots share a date. Do not overwrite an earlier run.
- Default local layout: `.seo/archive/YYYY/MM/DD/run-id/`, `.seo/experiments/`, and `.seo/index.md`.

## Track changes and experiments

- Inspect only relevant, authorized work. Distinguish planned, implemented, merged, and published changes.
- Record the target, action, date, strategy reference, baseline/period, intended metric, review date, and actual release state.
- A change log is not automatically a controlled experiment; label observational before/after comparisons accordingly.
- Update an existing experiment when appropriate instead of duplicating it. Recognize legacy `.seo/experiments.md` records.

Example record:

```markdown
# Clarify onboarding guide

- Target: /guide/getting-started
- Action and release state: [verified change, date, link]
- Rationale: [strategy reference]
- Baseline and measurement window: [metric, source, period]
- Review date: [date]

## Follow-ups

- [Date]: [measured result, caveats, next check]
```

## Update the index

- Link latest artifacts, snapshots, active experiments, outcomes, and source manifests.
- Check links and flag stale data using the project's freshness needs.
- Do not delete stale files, reorganize unrelated material, or commit/push without authorization.

## Grain

If connected, preserve snapshots and index/experiment updates in the shared Grain task folder, with stable links passed to downstream work. This overrides local-only paths; local working copies are fine. Otherwise continue normally. Keep sensitive material private and do not widen sharing permissions.
