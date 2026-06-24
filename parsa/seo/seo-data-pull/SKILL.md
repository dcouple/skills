---
name: seo-data-pull
description: (support) Discover connected analytics sources, pull data, and write .seo/data/ snapshots for other SEO skills.
allowed-tools:
  - Read
  - Write
  - Bash
  - Agent
  - WebSearch
  - WebFetch
  - mcp__posthog__*
  - mcp__composio__*
when_to_use: >
  This is a support skill. Don't invoke it directly. Other SEO skills
  (seo-briefing, seo-readability-pass, seo-authority-pass, seo-content-strategy,
  seo-content-drafting) call it as their first step when they need fresh data.
  If .seo/data/ is stale or missing, any SEO skill should run this first.
model: claude-opus-4-6
---

# SEO Data Pull

Discover what analytics, search, and SEO tools are connected, pull data from
all of them, and write structured snapshots to `.seo/data/`. Other SEO skills
read from this directory instead of pulling data themselves.

This is a support skill. It runs as the initial stage of other SEO skills,
not as a standalone workflow.

## Goal

Produce `.seo/data/` with fresh snapshots from every connected source.
If a source isn't connected, note the gap. Never fail because a source is
missing. Work with what's available.

## Steps

### 1. Discover connected sources

Check what analytics, search, and SEO tools are available:
- PostHog, GA4, Plausible, or similar analytics (MCP or API)
- Google Search Console (MCP or API)
- Ahrefs, Semrush, or similar via Composio or direct API
- Any other relevant MCP tools

List what's connected and what's not.

**Success criteria**: Know exactly which sources are available.

### 2. Pull analytics data

From whatever analytics source is connected (PostHog, GA4, etc.):
- Total page views and unique visitors (30-day trend)
- Top pages by views
- Pages with biggest gains and drops vs prior period
- Blog post performance
- New vs returning visitors

Write to `.seo/data/analytics.md`.

If no analytics source is connected, write a stub noting the gap.

**Success criteria**: `.seo/data/analytics.md` exists with whatever data was available.

### 3. Pull search console data

From Google Search Console (if connected):
- Total impressions, clicks, CTR, avg position (30-day trend)
- Top queries by impressions and clicks
- Queries with improving/declining position
- Pages with high impressions but low CTR
- Indexing status: submitted, indexed, not indexed, errors
- Recently submitted pages and their indexing outcome

Write to `.seo/data/search-console.md`.

**Success criteria**: `.seo/data/search-console.md` exists.

### 4. Pull SEO tool data

From Ahrefs, Semrush, or similar (if connected via Composio):
- Current keyword rankings and movement
- New keywords appeared for
- Lost keywords
- Competitor keyword gaps
- Backlink profile: new/lost, referring domains
- Domain rating trend

Write to `.seo/data/seo-tool.md`.

**Success criteria**: `.seo/data/seo-tool.md` exists.

### 5. Write the data manifest

Write `.seo/data/manifest.md` listing:
- Which sources were connected and pulled
- Which sources were missing (and what data is therefore unavailable)
- Timestamp of the pull
- Recommended actions to connect missing sources

**Success criteria**: `.seo/data/manifest.md` exists. Any SEO skill can read this to know what data is available.

## Staleness

Data snapshots are considered stale after 24 hours. If `.seo/data/manifest.md`
exists and its timestamp is within 24 hours, other skills can skip re-pulling.
If it's older, re-run this skill.
