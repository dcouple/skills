---
name: seo-briefing
description: (proactive) Pull analytics from PostHog, GSC, and Ahrefs. Correlate data and produce an actionable SEO briefing.
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
  Use when the user wants an SEO status report, morning briefing, analytics
  overview, or wants to understand how their site is performing. Examples:
  'SEO briefing', 'how is the site doing', 'pull analytics', 'morning report',
  'check indexing status', 'what keywords are we ranking for'.
model: claude-opus-4-6
---

# SEO Briefing

Pull data from all connected analytics sources, correlate it, and produce a
single actionable briefing. This is the CEO morning report for SEO.

**Important**: Run with Claude Opus 4.6.

## Data sources

The more sources connected, the better the briefing. At minimum, you need
analytics (PostHog, GA4, Plausible, etc.) and search data (GSC). Keyword/backlink
data (Ahrefs, Semrush) makes the briefing significantly more actionable.

Check what's available via MCP tools, Composio integrations, or direct API access.
If a source isn't connected, skip that section and note the gap in the briefing
so the user knows what they're missing.

## Goal

Produce `.seo/briefing.md` with:
1. What's working (traffic up, rankings improving, new keywords)
2. What's not working (traffic down, pages not indexed, rankings dropping)
3. What to do about it (specific, prioritized action items)

Every claim must cite the data source and specific numbers. No vibes.

## Steps

### 1. Discover available data sources

Check what analytics, search, and SEO tools are connected:
- Look for PostHog, GA4, Plausible, or similar analytics MCP/API
- Look for Google Search Console access
- Look for Ahrefs, Semrush, or similar via Composio or direct API
- Check for any other relevant MCP tools (WebSearch as fallback for competitor data)

If no analytics source is connected at all, recommend the user set one up first.
Otherwise, work with what's available and note gaps.

**Success criteria**: Know which sources are available. At least one analytics source connected.

### 2. Pull PostHog data

Query PostHog for the last 30 days vs prior 30 days:
- Total page views and unique visitors (trend)
- Top pages by views
- Pages with biggest gains and drops
- Blog post performance
- Landing page conversion (if funnels exist)
- New vs returning visitors

**Success criteria**: Traffic data with 30-day trends and page-level breakdown.

### 3. Pull Google Search Console data

Query GSC for:
- Total impressions, clicks, CTR, avg position (30 day trend)
- Top queries by impressions and clicks
- Queries with improving/declining position
- Pages with impressions but low CTR (title/description opportunity)
- Indexing status: how many pages submitted, how many indexed, which are not indexed
- New pages that were recently indexed (or not)
- Any indexing errors or warnings

**Success criteria**: Search performance data with indexing status for every important page.

### 4. Pull Ahrefs data

Query Ahrefs via Composio for:
- Current keyword rankings and movement
- New keywords the site appeared for
- Lost keywords
- Competitor keyword gaps (keywords they rank for, you don't)
- Backlink profile: new/lost backlinks, referring domains
- Domain rating trend

**Success criteria**: Keyword and backlink data with competitor context.

### 5. Correlate and produce briefing

Cross-reference the three data sources:
- Pages with high impressions but no clicks -> title/description problem
- Pages with traffic drops + ranking drops -> content quality or competition
- Pages not indexed -> submit for indexing
- New pages indexed + gaining traffic -> working, do more like this
- Competitor keywords you don't rank for -> content gaps to fill
- High-traffic pages with poor readability -> readability pass candidates

Write `.seo/briefing.md` with sections:

```markdown
# SEO Briefing — [date]

## Summary
3-5 bullet executive summary

## Traffic (PostHog)
Numbers, trends, top pages, biggest movers

## Search Performance (GSC)
Queries, impressions, clicks, CTR, position trends

## Indexing Status
Pages indexed, not indexed, recently submitted, errors

## Rankings (Ahrefs)
Keyword positions, movement, new/lost keywords

## Backlinks (Ahrefs)
New/lost, referring domains, domain rating

## Content Gaps
Keywords competitors rank for that we don't

## Action Items (prioritized)
1. [specific action] — [why] — [expected impact]
2. ...
```

**Success criteria**: Briefing written with every claim citing a data source and number. Action items are specific and prioritized.
**Artifacts**: `.seo/briefing.md` feeds into `seo-content-strategy`.
