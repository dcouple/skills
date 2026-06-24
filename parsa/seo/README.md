# SEO Agent Skills

SEO agents need connected data the same way business agents need a context base.

For business, the context base is `.business/` markdown files built from connected apps.
For SEO, the context base is live analytics data pulled from PostHog, Google Search Console,
and Ahrefs. If the data isn't connected, you're guessing. Don't guess.

**Important**: These skills should be run with **Claude Opus 4.6**, which performs
significantly better than 4.7 or 4.8 at copywriting and writing in specific voice styles.

## Required connectors

Before any SEO skill is useful, these must be connected:

| Connector | What it provides | How to connect |
|-----------|-----------------|----------------|
| **PostHog** | Page views, user behavior, feature usage, funnel data | PostHog MCP server or API key |
| **Google Search Console** | Indexing status, search queries, impressions, CTR, position | GSC MCP or API |
| **Ahrefs** (via Composio) | Keyword rankings, backlinks, competitor data, content gaps | Composio MCP with Ahrefs integration |

If a user hasn't connected these, the skills should tell them to set up connectors first.
Everything in SEO should be data-driven. No guessing.

## Three buckets

### 1. Proactive monitoring (CEO work)

Know what's happening before something breaks. Run regularly (weekly or monthly).

```txt
seo-briefing                     (pull all data, correlate, produce report)
  -> seo-content-strategy        (decide what to create/update based on the data)
```

### 2. Reactive (something changed, fix it)

Traffic dropped, page lost rankings, competitor launched something. Start with a
briefing focused on the problem, then execute.

```txt
seo-briefing                     (pull data for the affected pages)
  -> content-readability-pass    (rewrite if copy is the issue)
  -> content-authority-pass      (add E-E-A-T if authority is the issue)
  -> seo-content-drafting        (create new content if a gap opened)
```

### 3. Foundational audits (run anytime to improve)

These don't need a briefing. Run them whenever you want to raise the floor.

```txt
content-readability-pass         (audit + rewrite for voice and comprehension)
content-authority-pass           (explainers, glossary, author, E-E-A-T, schema)
```

## The full flow

When running the complete cycle (monthly), it's data first, strategy second, execution third:

```txt
seo-briefing                     (CEO skill: pull all data, correlate, report)
  -> seo-content-strategy        (what to create/update based on the data)
  -> content-readability-pass    (audit + rewrite existing pages)
  -> content-authority-pass      (explainers, glossary, E-E-A-T, author)
  -> seo-content-drafting        (new pages: blog posts, landing pages, comparisons)
```

## Human attention model

Human attention should be concentrated in:

1. `seo-briefing` review: understand what the data says
2. `seo-content-strategy` approval: agree on what to create/update
3. Voice sample or voice guide: the readability pass needs to know your voice

Everything after strategy approval should run as automatically as possible.

## Primary skills

### `seo-briefing`

The CEO morning briefing. Pull analytics from all connected sources, correlate,
and produce a snapshot:

- **Traffic**: page views, sessions, trends (PostHog)
- **Search**: impressions, clicks, CTR, avg position by page and query (GSC)
- **Indexing**: which pages are indexed, which aren't, which were submitted but not indexed (GSC)
- **Rankings**: keyword positions, movement, new keywords appearing (Ahrefs)
- **Content gaps**: keywords competitors rank for that you don't (Ahrefs)
- **Backlinks**: new/lost backlinks, referring domains (Ahrefs)
- **Action items**: pages to index, pages losing traffic, keywords to target, content to create

Writes `.seo/briefing.md`.

### `seo-content-strategy`

Consumes the briefing and decides what to do:

- Which existing pages need a readability rewrite (high traffic, low engagement)
- Which concepts need explainer pages (high search volume, no page exists)
- Which blog posts to write (trending keywords, content gaps, competitor analysis)
- Which pages need indexing requests
- Which pages are underperforming and why
- Priority order based on effort vs impact

Writes `.seo/strategy.md`.

**Human checkpoint**: Strategy must be approved before execution skills run.

### `content-readability-pass`

Audit and rewrite existing copy for voice, comprehension, and readability.
See `content-readability-pass/SKILL.md` for full steps.

### `content-authority-pass`

Add E-E-A-T signals: explainer pages, glossary, author attribution, structured data, OG images.
See `content-authority-pass/SKILL.md` for full steps.

### `seo-content-drafting`

Create new content based on the strategy:

- Blog posts targeting specific keywords with proper voice
- Landing pages for high-value search intents
- Comparison pages (vs competitors)
- Category pages for SEO clusters
- Update/backdate posts to fill publishing cadence gaps

Each piece of content should:
- Target a specific keyword or intent from the strategy
- Include proper metadata, JSON-LD schema, OG images
- Have author byline with headshot and dates
- Link to related docs, explainer pages, and glossary terms
- Include external authority links for E-E-A-T
- Follow the voice guide

## Support data (auto-generated)

### `.seo/` handoff structure

```txt
.seo/
  briefing.md              (latest CEO briefing snapshot)
  strategy.md              (approved content strategy)
  index-requests.md        (URLs submitted for indexing + status)
  keyword-targets.md       (keywords being targeted + current position)
  content-calendar.md      (what to publish and when)
```

## Fast paths

### Quick readability fix

```txt
content-readability-pass
```

### Add E-E-A-T to existing site

```txt
content-authority-pass
```

### Full SEO cycle (monthly)

```txt
seo-briefing
seo-content-strategy
content-readability-pass
content-authority-pass
seo-content-drafting
```

### Reactive: traffic dropped on a page

```txt
seo-briefing              (pull current data for that page)
content-readability-pass   (rewrite if copy is the issue)
content-authority-pass     (add E-E-A-T if authority is the issue)
```

## Mental model

SEO is not about tricks. It's about:

1. **Data**: know what's happening (briefing)
2. **Strategy**: decide what to do about it (strategy)
3. **Readability**: make existing content understandable (readability pass)
4. **Authority**: make it credible to Google (authority pass)
5. **Creation**: fill gaps with new content (drafting)

The goal is not to game search engines. The goal is to make your content
genuinely useful to the person searching, then make sure Google knows about it.
