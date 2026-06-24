---
name: seo-data-organize
description: (support) Archive and organize .seo/ data into a dated wiki structure for historical tracking.
allowed-tools:
  - Read
  - Write
  - Bash
when_to_use: >
  This is a support skill that runs at the end of any SEO workflow. It archives
  the current .seo/ working data into a dated, browsable wiki structure so
  nothing gets lost and you can track SEO progress over time. Other SEO skills
  should call this as their final step.
model: claude-opus-4-6
---

# SEO Data Organize

Archive and organize `.seo/` working data into a dated, browsable wiki
structure. Runs at the end of any SEO workflow so data accumulates into a
searchable history instead of getting overwritten.

This is a support skill. Other skills call it as their final step.

## Goal

Over time, `.seo/` becomes a self-organized wiki of SEO data:
- Every briefing, strategy, and content decision is dated and preserved
- You can look back at any week and see what the data said
- Experiments and their outcomes are tracked
- The current working state is always clean and fresh

## Directory structure

```
.seo/
  data/                          # current working data (from seo-data-pull)
    manifest.md
    analytics.md
    search-console.md
    seo-tool.md

  briefing.md                    # current working briefing
  strategy.md                    # current working strategy

  archive/                       # dated snapshots (this skill creates these)
    2026/
      06/
        24/
          briefing.md
          strategy.md
          data/
            manifest.md
            analytics.md
            search-console.md
            seo-tool.md
        10/
          briefing.md
          ...
      05/
        27/
          briefing.md
          ...

  experiments/                   # tracked experiments
    2026-06-24-windows-landing-page.md
    2026-06-10-remote-pane-blog-post.md

  index.md                       # auto-generated table of contents
```

## Steps

### 1. Archive current working data

If `.seo/briefing.md` or `.seo/strategy.md` exist:
- Create the dated archive directory: `.seo/archive/YYYY/MM/DD/`
- Copy `briefing.md`, `strategy.md`, and `data/*` into the archive
- Don't move them. Copy. The working files stay for the next skill that needs them.

**Success criteria**: Today's data is preserved in the archive. Working files still exist.

### 2. Track experiments

Scan the current strategy and any PRs merged since the last organize run.
For each new piece of content created or significant change made:
- Create an experiment file: `.seo/experiments/YYYY-MM-DD-short-name.md`
- Record: what was done, why (link to strategy), target keyword/metric, baseline data
- If a prior experiment exists for the same page, append a "follow-up" section with current data

Experiment files use this format:

```markdown
# [Short name]

- **Date**: YYYY-MM-DD
- **Type**: new page / rewrite / E-E-A-T / blog post
- **Target**: [keyword or metric]
- **Baseline**: [data from briefing at time of creation]
- **Action**: [what was done]
- **Strategy ref**: [link to .seo/archive/YYYY/MM/DD/strategy.md]

## Follow-ups
- YYYY-MM-DD: [updated data, outcome so far]
```

**Success criteria**: Every content action from this cycle has an experiment file.

### 3. Update the index

Regenerate `.seo/index.md` as a table of contents:

```markdown
# SEO Data Index

## Latest
- [Current briefing](briefing.md) — YYYY-MM-DD
- [Current strategy](strategy.md) — YYYY-MM-DD

## Archive
- [2026-06-24](archive/2026/06/24/) — briefing, strategy, data
- [2026-06-10](archive/2026/06/10/) — briefing, strategy
- ...

## Active Experiments
- [windows-landing-page](experiments/2026-06-24-windows-landing-page.md) — tracking
- [remote-pane-blog-post](experiments/2026-06-10-remote-pane-blog-post.md) — tracking
- ...

## Data Sources
- [Current manifest](data/manifest.md) — what's connected
```

**Success criteria**: `.seo/index.md` is up to date and links to everything.

### 4. Clean stale working files

If working files in `.seo/` are older than 7 days and have been archived,
note them as stale in the index. Don't delete them automatically.

**Success criteria**: Stale data is flagged but not destroyed.
