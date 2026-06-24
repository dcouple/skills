---
name: seo-foundations
description: (greenfield) Crawl your site, find competitors, map the search landscape, and build the starting point for all SEO work.
allowed-tools:
  - Read
  - Write
  - Bash
  - Agent
  - WebSearch
  - WebFetch
when_to_use: >
  Use when starting SEO from scratch, onboarding a new site, or when the agent
  doesn't know what the product is, who the competitors are, or what keywords
  matter. This is the zeroth step before seo-briefing. Examples: 'start SEO
  from scratch', 'set up SEO for this site', 'who are our competitors',
  'what should we rank for', 'SEO foundations', 'greenfield SEO'.
model: claude-opus-4-6
---

# SEO Foundations

Figure out what you're selling, who you're competing with, and what the search
landscape looks like. This is the starting point for everything else.

Run this once when you're starting SEO on a new site. After this, the other
skills (briefing, strategy, readability, authority, drafting) have the context
they need.

## Goal

Produce `.seo/foundations.md` with:
1. What the product is and who it's for (in plain language)
2. A list of competitors with evidence for why they're competitors
3. The keywords and search intents that matter
4. What competitors are doing that you're not
5. Where to start

## Steps

### 1. Understand the product

Crawl the website. Read the homepage, docs, pricing, about page, and any
landing pages. Answer these questions:

- What does this product do? (one sentence)
- Who is it for? (specific audience, not "developers")
- What problem does it solve? (the pain, not the feature)
- What makes it different? (the wedge)
- What words does the site use to describe itself?

If the site's messaging is unclear, note that. Unclear messaging means the
agent skills won't produce good content either. The user may need to fix
positioning before SEO work starts.

**Success criteria**: A plain-language summary of the product, audience, pain, and differentiator.

### 2. Discover competitors

Competitors come from how real users discover products, not just search results.
Check these sources in order:

**GitHub**: Search for the product category. Look at recent repos, trending
repos, and awesome-lists. Prioritize projects with recent commits and activity.
Discard dead projects (no commits in 3+ months, archived repos). If the user
has GitHub connected, check their stars and the repos they follow for context.

**Reddit and Hacker News**: Search for the product category and common pain
points. Recent launch posts and "what do you use for X?" threads surface real
competitors. Product Hunt launches are also useful for newer tools.

**Web search**: Generate 10-15 queries a buyer would actually type:

- "[product category]" (e.g., "agent manager")
- "[problem] tool" (e.g., "run multiple AI agents")
- "[alternative to known tool]" (e.g., "claude squad alternative")
- "[how to do X]" (e.g., "how to run AI agents in parallel")
- "[product type] for [platform]" (e.g., "agent manager for windows")

Record who shows up in results across all these sources. The products that
keep appearing are your competitors.

**The messaging test**: If your competitors show up when you search the
keywords you think matter, good. Your product is in the right search space.
If they don't, and the user has to manually add competitors, that's a signal:
the product's messaging doesn't match how people actually search and discover.
Flag this. Positioning may need work before content work starts.

Note: At zero-to-one, traditional SEO data (Ahrefs, Semrush) is less useful
than discovery patterns. How do people find new tools? GitHub, Reddit, Product
Hunt, Hacker News, Twitter. That's where you start. SEO tool data becomes
more valuable at one-to-100 when you're optimizing existing traffic.

**Success criteria**: A list of 5-10 active competitors discovered through real user discovery channels, with the sources that surfaced them.
**Human checkpoint**: Ask the user to confirm or add competitors. If they have to add many that didn't show up organically, note the messaging gap.

### 3. Map what competitors are doing

For each confirmed competitor, crawl their site (or at minimum their sitemap,
homepage, blog, docs, and comparison pages). Record:

- What pages do they have? (blog posts, landing pages, comparison pages, glossary, etc.)
- What keywords are they clearly targeting? (look at page titles and H1s)
- Do they have comparison pages? ("X vs Y")
- Do they have alternative pages? ("alternatives to X")
- Do they have explainer/glossary pages? ("what is X")
- How often do they publish blog posts?
- What's their content quality like? (voice, readability, depth)
- Do they have E-E-A-T signals? (author pages, dates, credentials, sources)

**Success criteria**: A content map for each competitor showing what they've built.

### 4. Identify the gaps and starting points

Compare what you have vs what competitors have:

**Obvious first moves** (do these immediately):
- Comparison pages: "Your product vs [each competitor]"
- Alternative pages: "[competitor] alternatives"
- These pages target people actively evaluating tools. High intent.

**Messaging and positioning**:
- Does your homepage clearly state what you are, who you're for, and why you're different?
- Can an agent crawling your site understand your positioning in 30 seconds?
- If not, the copy needs work before creating more content.

**Content gaps**:
- Explainer pages competitors have that you don't
- Blog topics competitors cover that you don't
- Keywords competitors rank for that you have no page for

**Structural SEO**:
- Does the site have proper metadata on every page?
- Are there OG images?
- Is there an author page?
- Is there a glossary?
- Is structured data (JSON-LD) on key pages?

**Success criteria**: A prioritized list of what to build, starting with the highest-intent pages.

### 5. Write the foundations document

Write `.seo/foundations.md`:

```markdown
# SEO Foundations — [site name]

## Product
- What it does: [one sentence]
- Who it's for: [specific audience]
- The pain it solves: [problem]
- The wedge: [what makes it different]

## Competitors
| Competitor | How we found them | Their strength | Our advantage |
|------------|------------------|----------------|---------------|
| [name] | [search query] | [what they do well] | [where we win] |

## Search Landscape
| Query | Who ranks | Our position | Opportunity |
|-------|-----------|-------------|-------------|
| [query] | [top results] | [not ranking / page X] | [what to do] |

## Competitor Content Map
### [Competitor 1]
- Comparison pages: [list]
- Blog frequency: [X/month]
- Explainer pages: [list]
- E-E-A-T signals: [yes/no, what]

## Starting Point (priority order)
1. [action] — [why this first]
2. [action] — [why]
3. ...

## Messaging Notes
- [any gaps or issues with current positioning]
```

**Success criteria**: Foundations document is complete. Any agent running `seo-briefing` or `seo-content-strategy` after this has the context it needs.
**Artifacts**: `.seo/foundations.md` is referenced by all other SEO skills as baseline context.
