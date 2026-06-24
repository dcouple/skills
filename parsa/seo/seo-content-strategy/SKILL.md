---
name: seo-content-strategy
description: (proactive) Turn an SEO briefing into a prioritized content plan: what to create, update, and index.
allowed-tools:
  - Read
  - Write
  - Bash
  - Agent
  - WebSearch
  - WebFetch
when_to_use: >
  Use when the user wants to decide what content to create or update based on
  data. Usually follows seo-briefing. Examples: 'what should we write',
  'content strategy', 'what pages need work', 'plan the next batch of content',
  'what keywords should we target'.
model: claude-opus-4-6
---

# SEO Content Strategy

Consume the SEO briefing and decide what to do: which pages to rewrite, which
explainers to create, which blog posts to write, which pages to index.

**Important**: Run with Claude Opus 4.6.

## Prerequisite

`.seo/briefing.md` must exist from a prior `seo-briefing` run. If it doesn't,
tell the user to run `seo-briefing` first. Don't strategize without data.

## Goal

Produce `.seo/strategy.md` with a prioritized content plan that balances
effort vs impact. Every recommendation must tie back to a specific data point
from the briefing.

## Steps

### 1. Read the briefing

Read `.seo/briefing.md` and identify:
- Pages losing traffic (candidates for rewrite)
- Pages not indexed (submit for indexing)
- High-impression/low-CTR pages (title/description fixes)
- Content gaps from competitor analysis (new pages to create)
- Keywords with no dedicated page (explainer or landing page opportunity)
- Blog publishing cadence (gaps in the calendar)

**Success criteria**: A list of opportunities ranked by data signal strength.

### 2. Research keyword intent

For each content gap or new page opportunity, research:
- Monthly search volume (Ahrefs or WebSearch estimates)
- Search intent (informational, navigational, commercial, transactional)
- What currently ranks (competitor content quality)
- Whether an existing page could be updated vs creating new

Use WebSearch to check what Google actually shows for target queries.

**Success criteria**: Each opportunity has estimated volume, intent type, and competitive difficulty.

### 3. Categorize the work

Sort recommendations into buckets:

**Quick wins** (high impact, low effort):
- Title/description rewrites for high-impression/low-CTR pages
- Indexing requests for pages GSC hasn't crawled
- Adding "last updated" dates to stale pages

**Readability rewrites** (medium effort):
- Pages with declining traffic that need voice/comprehension fixes
- Flag these for `content-readability-pass`

**New explainer pages** (medium effort):
- Concepts with search volume but no dedicated page
- Flag these for `content-authority-pass`

**New blog posts** (higher effort):
- Keyword gaps, trending topics, competitor content to counter
- Flag these for `seo-content-drafting`

**New landing pages** (higher effort):
- Commercial-intent keywords with no landing page
- Comparison pages, category pages, feature pages

### 4. Prioritize by effort vs impact

Rank everything in a single prioritized list. For each item:
- What to do (specific action)
- Why (data point from briefing)
- Expected impact (traffic estimate, ranking opportunity)
- Effort level (quick win / half day / full day)
- Which skill executes it

**Success criteria**: A numbered priority list where #1 is the best ROI action.

### 5. Write the strategy

Write `.seo/strategy.md`:

```markdown
# Content Strategy — [date]

## Based on
Link to .seo/briefing.md, date of data pull

## Quick Wins
1. [action] — [data point] — [expected impact]
...

## Pages to Rewrite (readability pass)
- [page] — [why] — [data]
...

## Explainer Pages to Create (authority pass)
- [concept] — [search volume] — [intent]
...

## Blog Posts to Write (content drafting)
- [title idea] — [target keyword] — [volume] — [why now]
...

## Landing Pages to Create
- [page] — [target intent] — [volume]
...

## Indexing Requests
- [URL] — [status] — [submitted date]
...

## Publishing Calendar
| Week | What | Type | Target keyword |
|------|------|------|----------------|
...
```

**Success criteria**: Strategy is specific, data-backed, and prioritized. Every recommendation ties to a briefing data point.
**Human checkpoint**: Strategy must be approved before execution skills run.
**Artifacts**: `.seo/strategy.md` feeds into readability pass, authority pass, and content drafting.
