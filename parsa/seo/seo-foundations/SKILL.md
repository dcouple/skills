---
name: seo-foundations
description: (greenfield) Map the product, the competitors, the search landscape, the page types that win, and the non-page surfaces where buyers and agents find products. Produces the keyword map, competitor map, page inventory, and discovery checklist every later SEO skill and the content pass build on.
allowed-tools:
  - Read
  - Write
  - Bash
  - Agent
  - WebSearch
  - WebFetch
when_to_use: >
  Use when starting SEO from scratch, onboarding a new site, planning the page
  set for a site that does not exist yet, or when the agent doesn't know what
  the product is, who the competitors are, or what keywords matter. This is
  the zeroth step before seo-briefing and before any content pass. Examples:
  'start SEO from scratch', 'set up SEO for this site', 'who are our
  competitors', 'what should we rank for', 'what pages should the site have',
  'SEO foundations', 'greenfield SEO'.
model: claude-opus-4-6
---

# SEO Foundations

Figure out what you're selling, who you're competing with, what people
actually type, which page types win those queries, and where else a buyer
or an agent finds a product. This is the starting point for everything else,
and it has to be complete without the user telling you what to look for.

Run it once when starting SEO on a site, and again after a competitor's
pricing changes or the product's scope moves. It works whether or not a site
exists yet. After it, the other skills (briefing, strategy, readability,
authority, drafting) and the content pass have the context they need.

## Goal

Produce, with every number cited and every fact dated:

1. `.seo/foundations.md`: product, competitors, search landscape, content
   map, starting point, messaging notes (the summary every later skill reads).
2. `docs/seo/keyword-map.md`: query families, representative queries,
   intent, demand evidence, who holds each query today, and the page that
   owns it.
3. `docs/seo/competitor-map.md`: who ranks for what, page structures worth
   matching, weak spots, and a corrections table for anything the repo's own
   docs got wrong.
4. `docs/seo/page-inventory.md`: every page to exist at launch, with slug,
   the one query it owns, a one-line angle, priority, build order, and the
   top ten by expected value.
5. `docs/seo/discovery-checklist.md`: every non-page surface, what each needs
   from us, and the order to do them.
6. `.seo/data/`: the working data behind all of it (competitor crawls,
   search-result maps, demand pulls, surface checks), archived by
   `seo-data-organize` at the end.

Rules that apply to every step: cite every number or claim with the URL or
file it came from; date everything; write "no cited volume" or "not checked"
instead of guessing; treat vendor self-reports as marketing; never rely on a
single search tool's ranking as a live SERP (say what tool produced the
ordering and re-verify the top opportunities in a browser before writing
briefs).

## Steps

### 0. Inputs, and the case with no site

Read whatever exists: the site, the repo's README and design docs, the
product, pricing, and roadmap docs, and any prior research. If there is no
live site, say so in every deliverable and work from the docs and the
competitors; the page inventory then doubles as the site's first page plan.
Record what analytics and SEO tools are connected (`seo-data-pull` style
manifest); with no site there is nothing to pull, and the manifest says so.

**Success criteria**: a manifest of inputs and connected sources, including
what is missing.

### 1. Understand the product

Crawl the website, or read the docs when there is none. Answer:

- What does this product do? (one sentence)
- Who is it for? (a specific buyer, not "developers"; and if the product is
  agent-facing, name the agent as a reader too)
- What problem does it solve? (the pain, not the feature)
- What makes it different? (the wedge)
- What words does the product use for its own concepts? (these become the
  glossary and the copy's vocabulary)
- What is shipped, what is planned, what is reserved? (the honesty line every
  page must respect)

Classify the product, because the page-type map in step 5 depends on it:
developer tool or infra, B2B SaaS, vertical SaaS, consumer, marketplace or
data product, API-first or agent-first. Most products are two of these.

If the messaging is unclear, note it. Unclear messaging means the content
skills won't produce good pages either, and the user may need to fix
positioning first.

**Success criteria**: a plain-language summary of product, audience, pain,
differentiator, vocabulary, and ship status.

### 2. Discover competitors

Where you look depends entirely on who the product is for. Don't default to
GitHub and Reddit for everything. Start by asking: how does the target buyer
actually find and evaluate products like this?

**First, figure out the discovery channel.** Based on the audience from step 1:

- **Developer tools, infra, open source**: GitHub trending and topics,
  awesome-lists, Reddit niche subs, Hacker News (Show HN and Ask HN), Product
  Hunt, dev communities on X and Bluesky, package registries. Prioritize
  repos with recent commits; discard dead projects.
- **Agent-first or API products**: MCP registries and directories, AI client
  directories, `llms.txt` directories, awesome-agent lists, skills
  registries, "for AI agents" and "MCP" queries. Competitors here are often
  adjacent categories (data APIs, scrapers, automation tools) that rank for
  the same words.
- **B2B SaaS**: G2, Capterra, GetApp, comparison blogs, "best X for Y"
  listicles, LinkedIn, industry newsletters.
- **Vertical SaaS**: the competitors may be agencies, freelancers, or manual
  workflows. Industry forums, trade publications, Facebook and LinkedIn
  groups, niche subreddits, events.
- **Consumer**: app stores, TikTok, Instagram, YouTube reviews,
  "alternatives to X" searches, influencer recommendations.

**Then search those channels.** Generate 10 to 15 queries a real buyer would
type: the category, "[problem] tool", "[known tool] alternative", "how to
[job]", "[product type] for [audience]". Record who shows up. Keep a list of
rivals that surface unprompted and are not in the user's list; they matter
for the map even if they are small.

**Narrow the wedge.** At each level of narrowing ask who the competitors
are, whether the messaging lands, where this audience goes, and who refers
buyers.

**The messaging test**: if the competitors you expect show up for the
queries you think matter, you're in the right space. If the user has to
name them by hand, the messaging doesn't match how buyers search. Flag it.

**The adjacent-category trap**: check whether a neighbouring category is
colonising your keywords (for example, "AI brand mention alerts" now means
mentions inside AI answers, not alerts delivered to an agent). Record which
phrasings are ambiguous; every page on those phrasings must disambiguate in
its first screen.

Note: at zero-to-one, traditional SEO data (Ahrefs, keyword volumes) is less
useful than discovery patterns; it becomes valuable once there is traffic
to optimise.

**Success criteria**: 5 to 10 active competitors with the channel that
surfaced each, plus the unprompted rivals, plus the ambiguous phrasings.
**Human checkpoint**: confirm or add competitors, unless the user already
named them in the brief; if they must add many that did not surface, note
the messaging gap.

### 3. Map what competitors are doing

Fan this out: one research agent per competitor, in parallel, each writing
one file under `.seo/data/competitors/`. For each competitor record:

- **Site structure**: sitemap URL count and counts by path pattern (blog,
  compare, alternatives, vs, per-source or per-integration pages, glossary,
  docs, use cases, audiences, free tools, programmatic pages). List the
  full slugs for comparison, alternative, source, audience, and agent pages;
  those are the ones you will compete with. Check the URL patterns they do
  not have (a 404 on `/glossary`, `/about`, `/changelog`, `/<x>-vs-<y>`).
- **Titles and H1s** of the money pages, and the keyword each targets.
- **Blog**: post count, date range, cadence over the last six months,
  authors, visible dates and "updated" labels, batch-refresh patterns.
- **E-E-A-T**: author pages, bios, logos, testimonials, review badges,
  original research, structured data (curl the HTML and grep for
  `application/ld+json`).
- **Agent surfaces** (for any product a model might buy): `/llms.txt`,
  `/llms-full.txt`, `/.well-known/mcp.json` or server cards, OpenAPI,
  machine-readable pricing, MCP registry entries, AI-crawler rules in
  robots.txt, an npm or PyPI CLI, a skills library. This is the baseline a
  new product must match before it can out-do anyone.
- **Pricing**: every tier with monthly and annual, limits, overages,
  add-ons, what is tier-gated; where two of their own pages disagree, say so.
  Note price history where third parties document it.
- **Weak spots**: missing page types, undated pages, stale numbers, copy
  drift between pages, claims that don't survive a check, thin templates.
- **Structures worth matching**: the skeleton of their best alternatives
  page, best vs page, best per-source page, best agent page, and free tools,
  section by section.

Then write a corrections table: every place the repo's own docs are behind
what the sites show today. Do not edit those docs from this skill; list the
corrections for the user.

**Success criteria**: one dated, cited crawl file per competitor and a
competitor map that says who owns which query and why.

### 4. Map the search landscape

Fan this out too, by query family. The families below are product-agnostic;
substitute the product's own nouns. For each query, record rank, domain,
title, page type, and whether the holder is the principal, a rival, or a
third party, and note the method's limits.

**Query families to cover, every time:**

1. Category head terms and "[category] tool / software / platform".
2. "[category] for [audience]" and "[category] for [use case]".
3. "[competitor] alternative" and "[competitor] alternatives", for every
   competitor, both forms.
4. "[a] vs [b]", for pairs buyers actually compare, including pairs that do
   not involve the product (third-party pairs are traffic too).
5. "[competitor] pricing", "[competitor] review", "is [competitor] worth it",
   "[competitor] reddit".
6. Per-integration, per-source, per-platform, or per-format pages: "[thing]
   [category]" for each thing the product connects to, watches, exports to,
   or runs on (sources for a monitoring tool, integrations for a SaaS,
   platforms for a consumer app, file formats for a converter, frameworks
   for a devtool).
7. "[job] how to", "[job] with [agent or automation tool]", and the free
   variant "free [job] tool".
8. "what is [term]" and "[term] vs [term]" for the category's vocabulary.
9. "[category] API", "[category] MCP server", "[category] for AI agents",
   "[category] SDK" for anything a program might call.
10. Migration queries when a competitor shut down, was acquired, or raised
    prices: "[dead tool] alternative", "[tool] shut down", "[tool] price
    increase".
11. Mini-tool queries: "[x] calculator", "[x] generator", "[x] checker",
    "[x] builder", "[x] estimator".

**Demand signals to pull** (zero-to-one has no Search Console; use these):
Google autocomplete through the suggest endpoint for each seed and seed plus
a letter, Bing autocomplete as a second opinion, Google Trends relative
interest between terms, any published volume only with its source and date,
HN and Reddit threads asking for tools (count them and date them),
competitor traffic estimates as a brand-demand proxy. Say plainly when a
source was unreachable.

**Gap tells** (a query nobody owns): a marketplace actor, a forum thread, a
GitHub issue, a Wikipedia page, or a deprecated project ranking in the top
five means no vendor built the page. **Beatability rules**: the principal
does not defend its own "alternative" query; the holders are short,
undated, or quote stale prices; the SERP is padded with unrelated results
(low volume, cheap to take but small); the principal is dead; the query's
intent fits the product better than the current holders. **Skip rules**:
category mismatch, a principal that owns most slots with its own hub, a
head term owned by enterprise product pages and long listicles when the site
has no authority yet.

**Success criteria**: a keyword map with, per family, the queries, the
intent, the evidence, the holders, the beatability call, and the owning
page. Each query has exactly one owning page.

### 5. Page types that win, and the page inventory

Order the inventory by the page types that intercept buyers and earn links,
not by what is easiest to write. From most to least valuable for a new site:

1. **Alternatives pages**, one per competitor, singular and plural query,
   including dead or acquired competitors (migration pages with dated
   deadlines).
2. **Versus pages**: first-party ("us vs X") for every live competitor, and
   third-party pairs ("X vs Y") where neither principal defends the query.
3. **Pricing teardowns**: "[competitor] pricing" with a dated table and the
   price history; rival pages contradict each other, so accuracy wins.
4. **Per-integration, per-source, or per-platform pages**, one per thing
   the product connects to, leading with the ones nobody has a page for.
5. **Mini tools**: calculators, builders, checkers, estimators, activity
   stats. They rank for their own queries and earn links; ship the formula in
   the description and the live version behind a key.
6. **Cookbooks, playbooks, recipes, skills**: one job each, with the exact
   call, also published in the form agents install (a skills registry, a
   SKILL.md, an awesome-list entry).
7. **Audience pages**: "[category] for [audience]" where no audience-specific
   page ranks.
8. **Agent surfaces** for anything a program might buy: an MCP page, an API
   page, a "for agents" page, a page for the delivery mechanism.
9. **Free-tier and free-tool pages**: "free [job]".
10. **Guides and listicles**: the category's "best X tools" written for the
    product's actual reader, and the how-to guides the gap tells revealed.
11. **Glossary, docs, about, changelog**: entity coverage and E-E-A-T, not
    early traffic.

For each page in the inventory: slug, the one query it owns, secondary
queries it may list, a one-line angle, priority (P0 launch day, P1 launch
week, P2 first month, P3 later), and for status-bearing pages the ship
status the page must print. Define the priorities so they do not contradict
the rows; give a launch-day build order; name the top ten by expected value
(demand times winnability times fit) and say why each; state the dependencies
(what must exist before a page can be honest); add a wave-2 section with the
next set of alternatives, pairs, tools, and cookbooks so the plan does not
stop at launch.

**Page rules every money page follows**: concede where the other product
wins before saying what changes; a dated pricing table with a "figures
verified on" line; a named author and a visible date; FAQ with FAQPage
schema, six to ten questions whose answers stand alone; internal links to at
least three siblings; the exact call or the exact form for anything a
program can do; planned status in the first screen; one owning query per
page; disambiguation from the adjacent category where the phrasing is
ambiguous.

Map every page to a template the site can render from a content file
(compare, alternatives, pair, source or integration, playbook, article,
tool, glossary, docs, audience, hub). Name the pages the existing template
set is missing; a page with no template is a UI decision, not a copy
decision.

Run `cold-read` on the inventory with a fresh agent before publishing it.
The findings that recur: a priority rule that contradicts its rows, two
competing orderings, status columns that mix access and status, a page
counted twice, queries with two owners, a page both kept and dropped, new
page kinds with no template, undefined product terms, citations with bare
filenames. Fix them before the PR.

**Success criteria**: an inventory a frontend team can build from and a
founder can order from, with counts that add up.

### 6. Discovery surfaces beyond the pages

A stranger or an agent finds a product in more places than its site. List
every surface for this product type, check each live, and record what it
needs from us (files, forms, schemas, accounts, cost, prerequisites). Cover:

- **Files on the domain**: `llms.txt` and `llms-full.txt` in spec shape, a
  docs-level `llms.txt`, machine-readable pricing, `.well-known` files for
  MCP, OpenAPI, and API catalogs, `robots.txt` that allows AI crawlers by
  name, an `AGENTS.md` in each public repo (not on the site), a `SKILL.md`
  where agents install skills, `.md` twins of pages.
- **Registries and directories for the product type**: MCP registries
  (official, and the aggregators), AI client directories (Claude connectors
  and plugins, Cursor, OpenAI plugins, VS Code and GitHub), package
  registries, `llms.txt` directories, app stores, G2 and Capterra and
  AlternativeTo and SaaSHub, Product Hunt and its auto-generated alternatives
  pages, Crunchbase, StackShare, Indie Hackers, AI-tool directories and
  their fees, automation directories (Zapier, Make, n8n), API directories,
  awesome-lists and GitHub topics with their contribution rules, skills
  registries.
- **For each**: the exact mechanism, the requirements, whether each
  competitor is listed today, and what to prepare.
- **Names**: check availability on every registry the product will publish
  to and the GitHub handle. Do not reserve names with placeholder releases;
  that is squatting under registry policy. Claim only what a registry
  supports (an npm org for a scope, a DNS record for a namespace) and publish
  real code.

Start the checklist with the actions that are free, time-sensitive, and
need no product: names, org handles, DNS records, an aged launch account.
Order the rest by phase.

**Success criteria**: a checklist with a "what discatch needs" line per
surface and a sequence tied to the roadmap.

### 7. Write the documents

`.seo/foundations.md` in this shape, plus the four `docs/seo/` files above
and a `docs/seo/README.md` index with the method caveats:

```markdown
# SEO Foundations — [site name]

## Product
- What it does: [one sentence]
- Who it's for: [specific audience, and the agent if it is a reader]
- The pain it solves: [problem]
- The wedge: [what makes it different]
- Words the product uses: [vocabulary]

## Competitors
| Competitor | How we found them | Their strength | Our advantage |
|------------|------------------|----------------|---------------|

## Search Landscape
| Query | Who ranks | Our position | Opportunity |
|-------|-----------|-------------|-------------|

## Competitor Content Map
### [Competitor]
- Comparison pages, alternative pages, per-source pages, audience pages
- Agent surfaces
- Blog frequency, E-E-A-T signals
- Weak spots

## Starting Point (priority order)
1. [action] — [why this first]

## Messaging Notes
- [ambiguous phrasings, adjacent-category collisions, positioning gaps]
- [corrections the repo docs need]
```

Then archive everything with `seo-data-organize`.

**Success criteria**: any agent running `seo-briefing`, `seo-content-strategy`,
or a content pass after this has the context it needs, and every number can
be traced to a file in `.seo/data/`.

### 8. Hand off to the content pass

The inventory is not the copy. When the user asks for the pages:

- The site should be content-driven: one content module per page kind, a
  template per kind, the route registry, sitemap, and `llms.txt` generated
  from the same data. Figure out the UI first (which templates exist, which
  the inventory needs), then the content.
- Write one brief for the writers that says where the truth lives, the
  rules that never bend (never name a provider, planned means planned,
  concede first, dated numbers, no invented features), the voice, the depth
  targets per page type, the block vocabulary, and how to finish (typecheck,
  a copy-to-review file for anything invented, a done file).
- One writer per content file, in parallel, each told how to write, what to
  write, who for, and given named examples to match. Use the strongest
  writing model available; the copy is the product. Assign by file so
  writers never collide; add second-wave pages in their own files and wire
  them in afterwards.
- Regenerate screenshots and Lighthouse, cold-read the money pages, and list
  the copy-to-review items in the PR body.
