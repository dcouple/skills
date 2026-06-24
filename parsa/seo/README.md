# SEO Agent Skills

![SEO workflow overview](../../docs/seo-workflow-map.png)

_Source: [docs/seo-workflow-map.excalidraw](../../docs/seo-workflow-map.excalidraw)_

## What this is

These are AI agent skills for SEO. You give them to Claude or Codex, and they handle the work: pulling your analytics, figuring out what's working and what's not, rewriting copy that doesn't sound right, creating explainer pages, adding author credentials, and drafting new content.

Each skill is one step in the process. They're composable: you can run one by itself, or chain them together for a full SEO cycle.

## How it works, simply

There are 8 skills. They start with foundations (if you're new), then break into three buckets:

### 0. Starting from scratch (greenfield)

If you're new to SEO or onboarding a new site, start here. If you already know your competitors and search landscape, skip to step 1.

- **`/seo-foundations`** crawls your website, figures out what you're selling and who it's for, then searches GitHub, Reddit, Product Hunt, and the web to find your competitors. It maps what content they have, identifies the obvious first pages to create (comparison pages, alternatives), and flags messaging gaps. It writes `.seo/foundations.md` so every skill after it has context.

At zero-to-one, traditional SEO data (Ahrefs, keyword volumes) is less useful than discovery patterns. How do real people find new tools? That's GitHub trending, Reddit "what do you use for X" threads, and Product Hunt. This skill starts there.

### 1. Know what's happening (proactive)

Before you write anything, look at the data. What pages are getting traffic? What keywords are you ranking for? What's not indexed? What are competitors doing that you're not?

- **`/seo-briefing`** pulls data from your analytics (PostHog, Google Analytics, etc.), your search console (Google Search Console), and your SEO tools (Ahrefs, Semrush, etc.). It produces a single report: here's what's working, here's what's not, here's what to do about it.

- **`/seo-content-strategy`** reads that report and turns it into a prioritized plan. Which pages to rewrite, which explainer pages to create, which blog posts to write, in what order.

You review the strategy. Once you approve it, the execution skills run.

### 2. Do the work (execution + foundational)

These skills don't need a briefing. You can run them anytime. But they're more useful when a strategy tells them what to focus on.

- **`/seo-readability-pass`** audits your existing pages for readability. Are you using jargon nobody understands? Passive voice? Sentences that are too long? It rewrites everything to match your voice: short sentences, simple words, no tech speak unless it's explained immediately.

- **`/seo-authority-pass`** adds E-E-A-T signals. That stands for Experience, Expertise, Authoritativeness, Trustworthiness. It's what Google looks for to decide if your content is credible. This skill creates explainer pages for hard concepts (like "what is a daemon?"), adds a glossary, builds an author page with real credentials, adds bylines with headshots and dates, and adds structured data so Google understands your pages better.

- **`/seo-content-drafting`** creates new content: blog posts, landing pages, comparison pages. Each piece targets a specific keyword from the strategy, uses your voice, and includes all the SEO fundamentals (metadata, schema, OG images, author byline, internal links, external authority links).

### 3. React when something breaks (reactive)

Traffic dropped? Page lost rankings? Competitor launched something? Start with a briefing focused on the problem, then run whichever skill fixes it.

### After everything: organize

- **`/seo-data-organize`** runs at the end. It archives your data into dated folders so you can look back at any week and see what happened. It tracks experiments (what you changed, why, and whether it worked). Over time, your `.seo/` folder becomes a searchable history of every SEO decision you've made.

## The full monthly cycle

```
0. /seo-foundations            ← first time only: understand product, find competitors
1. /seo-briefing               ← pull all data, see what's happening
2. /seo-content-strategy       ← decide what to do (you approve this)
3. /seo-readability-pass       ← fix existing copy
4. /seo-authority-pass         ← add credibility signals
5. /seo-content-drafting       ← create new content
6. /seo-data-organize          ← archive everything, track experiments
```

You don't have to run all of them every time. Need a quick copy fix? Just run `/seo-readability-pass`. Want to add explainer pages? Just `/seo-authority-pass`. The skills work alone or together.

## What you need to connect

These skills pull real data. The more sources you connect, the better they work. If a source isn't connected, the skill skips that part and tells you what you're missing.

| What | Why you need it | Options |
|------|----------------|---------|
| **Analytics** | Know which pages get traffic | [PostHog](https://github.com/PostHog/posthog-mcp), Google Analytics, Plausible |
| **Search console** | Know what people search for, what's indexed | Google Search Console |
| **SEO tool** | Know your keywords, backlinks, and competitors | Ahrefs or Semrush via [Composio](https://github.com/ComposioHQ/composio) |

The copy skills (readability pass, authority pass) don't need any data. They just need your website's code and a voice guide. You can run them right now without connecting anything.

For finding more connectors: [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers), [Composio](https://github.com/ComposioHQ/composio), [official MCP servers](https://github.com/modelcontextprotocol/servers).

## Where your data lives

All SEO data lives in a `.seo/` folder inside your website repo. The skills create and maintain it automatically.

```
.seo/
  index.md                 ← table of contents (auto-generated)
  briefing.md              ← latest briefing
  strategy.md              ← latest strategy

  data/                    ← current data snapshots
    manifest.md            ← what's connected, when it was pulled
    analytics.md
    search-console.md
    seo-tool.md

  archive/                 ← dated history (one folder per run)
    2026/06/24/
      briefing.md
      strategy.md
      data/

  experiments/             ← what you changed and whether it worked
    2026-06-24-name.md
```

## Where you spend your attention

You don't need to micromanage every step. Focus on two things:

1. **Read the briefing.** Understand what the data says.
2. **Approve the strategy.** Agree on what to create or update.

Everything else runs automatically. The skills handle the writing, the metadata, the structured data, the OG images, the author bylines, the internal linking, and the archiving.

## Model choice

Use **Claude Opus 4.6** for all copy work. It's significantly better than 4.7 or 4.8 at writing in a specific voice and producing natural, readable content. The newer models are great at code but tend to produce generic-sounding copy.

## Quick reference

| Skill | Phase | What it does |
|-------|-------|-------------|
| `/seo-briefing` | proactive | Pull data from all sources, produce a report |
| `/seo-content-strategy` | proactive | Turn the report into a prioritized plan |
| `/seo-readability-pass` | foundational | Audit and rewrite copy for voice and clarity |
| `/seo-authority-pass` | foundational | Add explainer pages, glossary, author, E-E-A-T |
| `/seo-content-drafting` | execution | Write new blog posts, landing pages, comparisons |
| `/seo-foundations` | greenfield | Crawl site, find competitors, map search landscape |
| `/seo-data-pull` | support | Shared data pulling (called by briefing) |
| `/seo-data-organize` | support | Archive data, track experiments, build wiki |
