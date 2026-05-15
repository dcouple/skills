---
name: company-gtm-operating-system
description: Build a top-down GTM/product operating system for a new company from a rough idea, using market research, competitor mapping, keyword/domain strategy, product thesis, architecture foundations, vendor stack, and routed docs.
argument-hint: "[rough company idea, competitors, domains, ICP, repo path, or constraints]"
---

# Company GTM Operating System

Turn a rough startup or product idea into a repo-backed company operating system: market/category understanding, domain experiments, product thesis, technical foundations, GTM ops, vendor defaults, and an execution-ready docs knowledge base.

## Inputs

- `$ARGUMENTS`: The rough company/product idea and any known competitors, domains, ICPs, keywords, analogies, repo path, cloud credits, preferred vendors, or technical constraints.
- Existing repo context, if present.
- User-provided links, competitor sites, sitemaps, docs, domain names, pricing pages, or analogy companies.

## Goal

Produce a durable company knowledge base that routes all important early decisions from `docs/README.md` and captures:

- market/category shape
- competitor and sitemap observations
- keyword/search strategy
- domain and naming experiments
- ICP and product thesis
- product workflow and non-negotiables
- technical architecture foundations
- infrastructure/cost/portability assumptions
- GTM ops and vendor stack
- open decisions and next steps

If the user wants repository changes finalized, commit and push the docs foundation.

## Rules

- Start from market/category/search demand before app screens or implementation.
- Treat competitors and sitemaps as evidence for the category shape, page strategy, pricing model, and buyer language.
- Prioritize high-leverage keywords and domain opportunities early; they can shape the whole product motion.
- Domains are experiments with distinct theses, voices, metadata, conversion paths, and ICPs. Do not recommend duplicate sites unless there is a deliberate canonical/redirect plan.
- Preserve user corrections as operating rules. If the user says a detail matters, capture it explicitly in docs.
- Separate GTM docs from technical architecture docs, but route both from the core README.
- Avoid public trust/compliance/security claims before the product, controls, policies, and legal posture support them.
- Keep trust/security/compliance as internal product guardrails even when public pages stay lightweight.
- Prefer `/docs` on the relevant product domain over a docs subdomain when SEO authority matters.
- For agent/developer products, include APIs, SDKs, CLI, MCP, OpenAPI, `llms.txt`, examples, and agent-readable docs in the product thesis.
- For infra-heavy products, capture provider adapters, cost guardrails, portability boundaries, and benchmark plans rather than hardcoding one provider too early.
- Use external research when information may have changed, when competitors or current vendors are referenced, or when exact pricing/product capabilities matter.
- When editing files, keep changes scoped and commit only the work relevant to this foundation.

## Steps

### 1. Frame The Market Hunch

Capture the rough idea, job-to-be-done, category, buyer/user assumptions, use cases, urgency, and why now.

Ask or infer:

- What painful job is being solved?
- Who likely searches for it?
- Who pays for it?
- What existing category language already exists?
- What analogies or prior founder lessons matter?

**Success criteria**: A concise initial thesis exists with category, JTBD, ICP assumptions, and product ambition.

### 2. Research Category Shape

Use competitor sites, pricing pages, sitemaps, docs, public pages, and search results to understand the market.

Look for:

- category names
- page types
- pricing models
- buyer language
- vertical pages
- compliance or trust claims
- API/developer surfaces
- docs/help-center structure
- feature vocabulary
- conversion paths

Prefer sitemaps and HTTP/page reads for site shape. Use web research for current facts.

**Success criteria**: Competitor/category observations are summarized with source links and implications for positioning, pages, pricing, and product surface.

### 3. Extract Keyword And Demand Strategy

Identify search terms and intent clusters.

Include:

- head terms
- high-intent commercial terms
- pain/job terms
- vertical terms
- API/developer terms
- agent/discoverability terms
- paid-search test terms
- content/page ideas

Distinguish curiosity traffic from workflow/buyer intent.

**Success criteria**: A keyword strategy exists with clusters, target pages, likely intent, and measurement assumptions.

### 4. Define Naming And Domain Strategy

Brainstorm and evaluate names/domains against:

- category fit
- spoken memorability
- search alignment
- enterprise trust
- developer/API friendliness
- creator/consumer friendliness
- URL availability
- ability to run distinct experiments

If multiple domains exist, assign each one a distinct thesis.

**Success criteria**: The docs identify primary and secondary domains, each domain's role, and how domains should avoid duplicate content.

### 5. Define Product Thesis And Workflow

Translate market research into product principles.

Capture:

- primary user workflow
- MVP wedge
- supported formats/surfaces
- review/approval needs
- auditability needs
- data model concepts
- product quality metrics
- what not to build yet
- public claims to avoid

**Success criteria**: A product brief exists with workflow, ICP, MVP direction, technical direction, and product capabilities that matter.

### 6. Define Domain Experiment Docs

Create a standard schema for each domain experiment.

Recommended files per domain:

```text
docs/<domain-slug>/
  README.md
  one-pager.md
  analogies.md
  angle.md
  seo-gtm.md
  product-surface.md
  experiments.md
```

Each domain should capture:

- ICP
- thesis
- voice
- keywords
- CTA
- product surface
- analogies
- page strategy
- experiments
- success metrics

**Success criteria**: Every domain has a routed folder with the same schema and clearly distinct positioning.

### 7. Define Architecture Foundations

Capture the technical operating model without prematurely overbuilding.

Include:

- target repo structure
- app/library boundaries
- frontend strategy
- docs strategy
- API/worker split
- data schemas to define later
- compute/model providers
- storage and queue assumptions
- portability boundaries
- Docker/container direction
- infra-as-code direction
- deployment constraints
- cost/egress guardrails

For provider-heavy products, define adapter boundaries and benchmark criteria.

**Success criteria**: Architecture docs explain how the company can build the first product without locking itself into fragile provider assumptions.

### 8. Define GTM Ops And Vendor Stack

Capture the operational stack needed to test demand.

Include:

- Google Search Console
- Bing Webmaster Tools
- analytics, usually PostHog
- support/chat, such as Crisp
- docs framework, such as Nextra
- docs path strategy, usually `/docs`
- billing, usually Stripe
- transactional email, such as Resend
- error tracking, such as Sentry
- database
- queue
- object storage
- DNS/CDN/WAF
- observability
- conversion events
- setup order

**Success criteria**: GTM ops and vendor assumptions are documented with open decisions separated from defaults.

### 9. Create The Docs Knowledge Base

Write a routed `docs/README.md` and focused foundation docs.

Recommended root docs:

```text
docs/README.md
docs/product-brief.md
docs/market-foundation.md
docs/competitor-and-industry-map.md
docs/keywords.md
docs/gtm-foundation.md
docs/gtm-ops-and-vendor-stack.md
docs/strategic-analogies.md
docs/repo-structure.md
docs/cost-and-portability-foundation.md
docs/open-questions-and-decisions.md
docs/next-steps.md
docs/research-index.md
```

Add domain folders from Step 6.

**Success criteria**: `docs/README.md` routes by intent and all important decisions are reachable from it.

### 10. Review For Missed Nuance

Do a final pass for:

- user corrections
- named analogies
- competitor references
- domain decisions
- keyword priorities
- infra constraints
- vendor decisions
- open questions
- docs routing
- duplicate or redundant domain docs
- claims that are too strong
- decisions that belong in root docs but are buried in a domain doc

**Success criteria**: The docs preserve the actual reasoning and tradeoffs, not just a sanitized summary.

### 11. Commit And Push If Requested

If working in a Git repo and the user wants the foundation saved:

1. Run `git status --short --branch`.
2. Review the diff.
3. Stage only relevant docs.
4. Commit with a scoped docs message.
5. Push to the requested branch or default branch.
6. Confirm clean status.

**Success criteria**: The docs foundation is committed and pushed, with commit SHA reported to the user.

## Suggested Follow-Up Docs

When the first foundation is complete, propose the highest-leverage missing docs rather than expanding everything at once:

- `data-schema-foundation.md`
- `job-state-and-metering-foundation.md`
- `local-dev-and-env-foundation.md`
- `secrets-and-config-foundation.md`
- `ci-cd-and-infra-ops-foundation.md`
- `pricing-packaging-foundation.md`
- `open-source-and-developer-docs-foundation.md`

## Trigger Phrases

Use this skill when the user says things like:

- "help me think through a new company"
- "turn this idea into a company foundation"
- "build the GTM/product docs for this startup"
- "research competitors and create the operating docs"
- "we need a GTM operating system"
- "make this repeatable for a new company"
- "start from market research and work top-down"
- "figure out domains, positioning, product, and repo structure"
