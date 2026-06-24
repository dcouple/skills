---
name: seo-content-drafting
description: (execution) Create new SEO content: blog posts, landing pages, comparison pages based on the content strategy.
allowed-tools:
  - Read
  - Edit
  - Write
  - Bash
  - Agent
  - WebSearch
  - WebFetch
when_to_use: >
  Use when the user wants to create new content for SEO: blog posts, landing
  pages, comparison pages, or category pages. Usually follows seo-content-strategy.
  Examples: 'write the blog posts', 'create the landing pages', 'draft the
  comparison page', 'fill the content calendar'.
model: claude-opus-4-6
---

# SEO Content Drafting

Create new content based on the approved content strategy. Blog posts, landing
pages, comparison pages, explainer pages, category pages.

**Important**: Run with Claude Opus 4.6.

## Prerequisite

`.seo/strategy.md` should exist from a prior `seo-content-strategy` run.
A voice guide should exist in the repo (`AGENTS.md` or `VOICE.md`).
If either is missing, tell the user to run the prerequisite skill first.

## Goal

Create publication-ready content that:
1. Targets specific keywords from the strategy
2. Matches the founder's voice (reference the voice guide)
3. Includes proper SEO metadata, JSON-LD, and OG images
4. Has author byline with headshot and dates
5. Links to related docs, explainer pages, and glossary terms
6. Includes external authority links for E-E-A-T
7. Passes the humanity test (first-timer can understand it)

## Steps

### 1. Read the strategy and voice guide

Read `.seo/strategy.md` for what to create and why.
Read the voice guide for how to write it.
Identify which content items are approved for creation.

**Success criteria**: Clear list of content to create with target keywords and intent.

### 2. Research each topic

For each piece of content:
- WebSearch the target keyword to see what currently ranks
- Read the top 3 results to understand what the audience expects
- Identify gaps in existing content (what they don't cover)
- Find authoritative sources to reference (E-E-A-T)
- Check if the site has related pages to link to

**Success criteria**: Each topic has research notes, competitive context, and source links.

### 3. Draft content

Write each piece following the site's patterns:
- Match existing component structure (check how other pages are built)
- Use the voice guide for tone and style
- Include proper metadata: title with brand suffix, description with differentiators
- Add JSON-LD schema (Article for blog, FAQPage for FAQ sections, WebPage for landing)
- Create OG image files if the site has a programmatic banner system
- Add AuthorByline component with "Last updated" date
- Use `<Term>` component for glossary words if the site has one

For blog posts:
- Add to the posts array in the correct chronological position
- Set appropriate date (current date or backdated per strategy)
- Include author field

For landing pages:
- Create page.tsx in the appropriate app directory
- Add to footer navigation if it's a primary page
- Add to sitemap if manually maintained

**Success criteria**: Each piece of content is complete with metadata, schema, OG images, byline, and internal/external links.
**Rules**:
- Never keyword-stuff. Write for the reader, optimize for the search engine second.
- Every external link should go to a real, authoritative source
- Titles under 60 characters including brand suffix
- Descriptions include platform/differentiator keywords
- Dates in human-readable format (Month Day, Year)
- No em dashes. Use commas, colons, periods, or sentence breaks.

### 4. Internal linking pass

After all content is drafted, do a linking pass:
- New pages link to relevant existing docs, explainers, and glossary
- Existing pages that mention concepts covered by new pages get links added
- Footer or navigation updated if new pages are primary surfaces
- Glossary updated with any new terms introduced

**Success criteria**: Every new page links to at least 2-3 existing pages. Existing pages link back where relevant.

### 5. Build, verify, deploy

Run the production build to catch errors.
Create a PR with a summary of all content created, target keywords, and the strategy context.
After merge, produce the list of new URLs for Google Search Console indexing.

**Success criteria**: Build passes. PR merged. URL list for indexing provided.
**Artifacts**: List of new URLs to request indexing for.
