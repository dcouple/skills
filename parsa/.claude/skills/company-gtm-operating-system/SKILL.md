---
name: company-gtm-operating-system
description: "Build a company GTM and product planning knowledge base when starting from a rough business idea."
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

## Work by stage

Use existing current evidence and settled decisions rather than restarting
research. Read the reference for the stage the requested work needs:

- Establish the market, competitors, keywords, and naming: [market research](references/market-research.md).
- Define product, domain experiments, architecture, and vendors: [product and architecture](references/product-and-architecture.md).
- Assemble and review the knowledge base, commit only if requested: [handoff](references/handoff.md).

Continue across stages when the user requested the full operating system.
A narrower request uses only its relevant stage and dependencies. Preserve the
shared rules above, including public-claim evidence and authorization boundaries.

## Suggested Follow-Up Docs

When the first foundation is complete, propose the highest-leverage missing docs rather than expanding everything at once:

- `data-schema-foundation.md`
- `job-state-and-metering-foundation.md`
- `local-dev-and-env-foundation.md`
- `secrets-and-config-foundation.md`
- `ci-cd-and-infra-ops-foundation.md`
- `pricing-packaging-foundation.md`
- `open-source-and-developer-docs-foundation.md`
