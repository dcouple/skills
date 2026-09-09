---
name: seo-from-calls
description: "Mine customer call transcripts (Doozy captures) for unmet search intents, validate against the existing site and competitive landscape, and draft the pages that fill the gaps. Use when the user wants to turn sales call insights into SEO pages — 'what pages should we create from today's calls', 'turn that call into pages', 'SEO from calls'."
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Agent
  - WebSearch
  - WebFetch
  - ToolSearch
when_to_use: >
  Use when the user wants to extract SEO page ideas from customer calls,
  Doozy captures, or sales conversation transcripts. Examples: 'what SEO pages
  should we create from today's calls', 'turn those transcripts into pages',
  'mine calls for page ideas', 'seo from calls'.
model: claude-opus-4-6
---

# SEO From Calls

Turn customer call transcripts into SEO pages. Every product, site, and call
is different — this skill is a starting framework for discovery, not a rigid
recipe. Adapt the steps, skip what does not apply, and follow the signals
wherever they lead.

The core insight: when a real buyer calls and asks questions the website does
not answer, those questions are unmet search intents. Other people are
searching for the same answers and finding nothing — or finding a competitor.

## When to use

After sales or discovery calls when the user wants to identify and create new
SEO pages. Typically triggered by: "what pages should we create from those
calls", "seo from calls", or "turn that call into pages."

## Starting points

The phases below are a typical shape, not a checklist. Some runs will skip
phases, reorder them, or spend most of their time in one. Let the
conversation and the signals drive the process.

### Gather transcripts

Get the raw material — call transcripts, notes, or summaries. Sources vary:

- **Doozy captures**: load tools via ToolSearch (`mcp__doozy__list_captures`,
  `mcp__doozy__get_capture`), list recent captures, fetch transcripts
- **Pasted notes or summaries**: the user may share what they already
  distilled from a call
- **Multiple calls**: patterns across calls matter more than any single one

### Extract buying signals

Listen for what the caller could not find on the site. Common signal types
(not exhaustive — every product surfaces different ones):

- **Questions they asked** — unmet search intents
- **What they already tried** — reveals their search journey and where the
  site lost them
- **Their existing tools** — integration or coexistence page opportunities
- **Their industry or role** — vertical gaps the site does not address
- **Competitors they mentioned** — comparison page opportunities
- **Pricing confusion** — conversion leaks; if the caller could not
  understand pricing, visitors are bouncing silently
- **Organizational complexity** — multi-location, multi-team, permissions,
  oversight needs that no current page addresses

One caller's question is anecdotal. When two callers independently hit the
same wall, that is a signal worth acting on.

### Cross-reference the existing site

Before proposing new pages, understand what already exists. The shape of this
research depends on the site:

- Map every existing page route in the codebase
- For each extracted signal, check: does a page already cover this? Is it
  findable (linked from navigation, footer, other pages)?
- Identify pages that exist but are underleveraged — missing from nav,
  poorly cross-linked, or not in the right category

In parallel, research the competitive landscape for the gaps:
- What are people searching for around these topics?
- Who currently ranks?
- What content patterns work in this space?

### Discuss and prioritize

Present findings to the user. Be opinionated — recommend, do not just list.
Typical categories (adapt to what you find):

1. **Quick fixes** — conversion leaks, missing nav links, unclear copy
   (highest ROI, no new pages)
2. **New pages on existing templates** — if the site already has a pattern
   for comparison pages, integration pages, or vertical pages, new entries
   are low-effort
3. **New page types** — pages that need something the site does not have yet

Highlight where the user's initial ideas should be adjusted based on what
actually exists. Deprioritize with reasoning, not just silence.

### Draft the pages

When the user approves, build the pages directly. Study the existing site's
patterns first — templates, config structures, routing conventions, deploy
requirements — and match them exactly. New pages should look like they have
always been part of the site.

Source and date every claim about a competitor or third-party tool.

### Verify

Run the site's build to confirm the new pages compile. Check that
cross-links, navigation updates, and deploy config are all in place.

## Quality principles

- New pages should be discoverable — linked from navigation, cross-linked
  from related pages
- Third-party claims cite a source and carry a date
- Pricing pages address any confusion the calls surfaced
- The site's existing voice, structure, and deploy conventions are respected

## Relationship to other SEO skills

This skill turns qualitative customer signals into pages. It complements:

- `seo-content-strategy` — works from analytics data, not calls
- `page-strategy` — plans a single page from a keyword
- `seo-readability-pass` — rewrites existing copy
- `seo-authority-pass` — deep competitor analysis
