---
name: seo-authority-pass
description: (foundational) Add E-E-A-T signals: explainer pages, glossary, author attribution, structured data, OG images, and SEO metadata.
allowed-tools:
  - Read
  - Edit
  - Write
  - Bash
  - Agent
  - WebSearch
  - WebFetch
when_to_use: >
  Use when the user wants to improve SEO authority, add E-E-A-T signals,
  create explainer pages, add author attribution, or optimize metadata.
  Examples: 'add E-E-A-T', 'create explainer pages', 'add author bylines',
  'SEO pass', 'add a glossary', 'authority pass', 'add structured data',
  'create a what-is page'.
model: claude-opus-4-6
---

# Content Authority Pass

Add E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) signals
across a product website: explainer pages for hard concepts, a glossary,
author attribution with bylines and headshots, structured data schemas,
OG images, and consistent SEO metadata.

**Important**: Run this skill with Claude Opus 4.6. It performs significantly
better than 4.7 or 4.8 at copywriting and writing in specific voice styles.

## Prerequisites

- **Voice guide**: Must exist in repo (`AGENTS.md`, `VOICE.md`, or `CLAUDE.md`). If missing, run `seo-readability-pass` first (it creates one).
- **Term list (optional)**: If `seo-readability-pass` produced a list of concepts needing explainers, use it. Otherwise, discover terms in step 1.

## Goal

Every page should signal authority to both readers and Google:
1. Hard concepts link to plain-language explainer pages
2. Every content page has an author byline with headshot, link, and "last updated" date
3. An author page exists with real credentials and external source links
4. Structured data (JSON-LD) is on every page
5. OG images generate programmatically
6. Page titles follow a consistent brand pattern
7. Meta descriptions always mention key differentiators and platform support

## Steps

### 1. Identify concepts needing explainer pages

If a term list exists from a prior content-readability-pass, use it.
Otherwise, scan all content pages for:
- Technical terms used repeatedly but never formally defined
- Product-specific concepts that get mentioned without explanation
- Multi-word concepts that mean something specific (e.g., "worktree isolation", "agent orchestration")
- Industry terms the target audience might not know

Research each term with WebSearch to understand:
- What people actually search for (keyword intent)
- What authoritative sources exist to reference (official specs, respected blogs, research papers)

**Success criteria**: A prioritized list of concepts to create explainer pages for.
**Human checkpoint**: Present the list and get approval before creating pages.

### 2. Create a glossary index page

Create a `/glossary` page that:
- Lists all terms alphabetically with plain-language definitions
- Links to dedicated explainer pages where they exist
- Uses `DefinedTermSet` JSON-LD schema
- Has a "Missing a term?" CTA
- Includes OG image generation
- Uses the site's existing design patterns and component library

**Success criteria**: Glossary page renders with all terms and proper schema.

### 3. Create E-E-A-T explainer pages

For each approved concept, create a dedicated page following this pattern:
- URL: `/what-is-[concept]` or `/what-does-[concept]-mean`
- Plain-language explanation written in the founder's voice (reference the voice guide)
- "The problem" section (why this concept matters to the reader)
- "How [product] does it" section (tie it back naturally)
- Comparison table where relevant
- FAQ section with `FAQPage` JSON-LD schema (6+ questions)
- Links to related docs and other explainer pages
- External authority links (official specs, Anthropic/Google blogs, respected sources)
- OG image generation (reuse site's banner style if one exists)
- Proper metadata with brand title suffix
- "Related docs" section at the bottom

**Success criteria**: Each page passes the "would a first-timer understand this?" test. Every page has JSON-LD, OG images, and external authority links.
**Rules**:
- Write in the voice guide's style, not generic explainer tone
- Every claim should link to a source where possible
- Reference Anthropic, Google, or other respected sources for AI concepts
- Don't keyword-stuff; write for the reader first
- Titles should be under 60 characters including the brand suffix
- Descriptions should mention key platform/OS support where relevant

### 4. Create or update author page

Research the author online (LinkedIn, GitHub, X, news articles, university pages) to build a credible bio.

Create `/author/[name]` with:
- Headshot image in `/public/authors/`
- Bio with real credentials, linked to external sources (not just claimed)
- Hackathon wins, speaker series, published work, notable roles
- Social links (GitHub, LinkedIn, X)
- `Person` JSON-LD schema with `sameAs` links
- Auto-populated list of blog posts by this author
- OG image generation

**Success criteria**: Author page has verifiable credentials with external links. No claims without sources. Every notable achievement links to proof.
**Rules**:
- Every credential must link to an external source (news article, event page, GitHub, etc.)
- Don't include outdated or dead links
- Write the bio in first person, matching the voice guide

### 5. Add author bylines across all pages

Create a reusable `AuthorByline` component with:
- Small headshot (28x28 rounded)
- "by [Author Name]" linking to the author page
- "Last updated [date]" line below
- Top border separator and generous top margin for visual breathing room

Add to: all explainer pages, glossary, and landing pages (before FAQ section).

Update blog post template to show:
- Byline with headshot and "Published [Month Day, Year]" at top
- "Last updated [date]" at the very bottom of the article

Ensure all dates display as "Month Day, Year" format everywhere (never ISO format in UI).

**Success criteria**: Every content page has visible author attribution with dates. Dates are human-readable.

### 6. SEO metadata pass

Establish a brand title pattern and apply it everywhere:
- Homepage: `[Brand] — [Tagline] | [Differentiators]`
- Blog posts: `[Title] — [Brand]`
- Landing pages: `[Title] — [Brand] | [Category descriptor]`
- Explainer pages: `[Title] — [Brand]`

Update all meta descriptions to include key differentiator keywords and platform support (e.g., "Windows, Windows with WSL, macOS, Linux").

Add the glossary and explainer pages to the site footer in a "Learn" column for discovery.

Update the sitemap if it's manually maintained.

**Success criteria**: Consistent titles under 60 chars across all pages. Descriptions include differentiators. Footer links to glossary and explainer pages.

### 7. Build, verify, deploy

Run the production build to catch errors.
Create a PR with a clear summary of everything added.
After merge, produce a list of all new and updated URLs for Google Search Console indexing.

**Success criteria**: Build passes. PR merged. URL list provided for indexing.
**Artifacts**: List of URLs to request indexing for in Google Search Console.
