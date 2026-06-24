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

Where you look depends entirely on who the product is for. Don't default to
GitHub and Reddit for everything. Start by asking: how does the target buyer
actually find and evaluate products like this?

**First, figure out the discovery channel.** Based on the audience from step 1:

- **Developer tools, infra, open source**: GitHub trending, awesome-lists,
  Reddit (r/programming, r/selfhosted, niche subs), Hacker News, Product Hunt,
  Twitter/X dev communities. Prioritize repos with recent commits. Discard dead
  projects (no activity in 3+ months).

- **B2B SaaS (generic)**: G2, Capterra, comparison blogs, "best X for Y"
  articles, LinkedIn discussions, industry newsletters. The buyer is googling
  "best [category] for [use case]" and reading listicles.

- **Niche/vertical SaaS** (e.g., AI design for real estate): The competitors
  might not be other software. They might be agencies, freelancers, or manual
  workflows. Look at: industry-specific forums, trade publications, Facebook
  groups, niche subreddits, LinkedIn groups, industry events. The discovery
  channel is where that audience already hangs out, not where developers hang
  out.

- **Consumer products**: App stores, TikTok, Instagram, YouTube reviews,
  "alternatives to X" searches, influencer recommendations.

**Then search those channels.** Generate 10-15 queries a real buyer would type,
appropriate to their channel:

- "[product category]" (e.g., "agent manager")
- "[problem] tool" (e.g., "run multiple AI agents")
- "[alternative to known tool]" (e.g., "claude squad alternative")
- "[how to do X]" (e.g., "how to run AI agents in parallel")
- "[product type] for [audience]" (e.g., "AI staging photos for realtors")

Record who shows up across the channels that matter for this audience.

**Narrow the wedge.** The broader the product, the more competitors you'll
find. The goal is to narrow: go from "AI design tool" to "AI staging photos
for recently sold home properties." At each level of narrowing:
- Who are the competitors at this level?
- Is the messaging clear enough that someone in this niche gets it immediately?
- Where does this specific audience go to find tools like this?
- Who refers buyers? (agents, consultants, communities, directories)

**The messaging test**: If your competitors show up when you search the
keywords you think matter, good. You're in the right space.
If they don't, and the user has to manually name competitors, that's a signal:
the messaging doesn't match how buyers actually search. Flag this.
Positioning may need work before content work starts.

Note: At zero-to-one, traditional SEO data (Ahrefs, keyword volumes) is less
useful than discovery patterns. SEO tool data becomes more valuable at
one-to-100 when you're optimizing existing traffic.

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
