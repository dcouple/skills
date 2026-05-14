---
name: site-content-audit
description: "Audit a site, sitemap, content section, competitor, or URL portfolio for SEO/content quality patterns. Use for ClickUp-style traffic-loss forensics, sitemap XML analysis, Ahrefs/Semrush/GSC export analysis, SERP replacement analysis, template-footprint risk, competitor teardown, pruning, merging, rewriting, refreshing, redirecting, or recovery sequencing."
---

# Site Content Audit

Use this skill when the unit of analysis is larger than one page: a sitemap, content section, competitor, traffic decline, template family, or URL portfolio.

Core rule: separate demand loss from ranking loss. Do not blame AI overviews, Google updates, backlinks, or topical breadth until the evidence shows whether traffic disappeared or transferred elsewhere.

## Inputs To Gather

- Sitemap XML, sitemap index, URL list, or crawl export.
- Optional traffic/ranking exports from GSC, Ahrefs, Semrush, or similar tools.
- Date range and known traffic-change dates.
- Competitor URLs or current SERPs for important lost queries.
- Sample HTML/pages from winners and losers.
- Product scope and content strategy context.

Use public web research or official Google sources when current update timing or policy language matters. Prefer local files/exports when the user supplies them.

## Scripts

- `scripts/sitemap_inventory.py`: parse sitemap XML/indexes from a file or URL into CSV/JSON.
- `scripts/content_fingerprint.py`: analyze HTML files or URLs for title/H1/schema basics, CTA/product-promo phrases, repeated headings, product mentions, and template markers.
- `scripts/merge_search_exports.py`: merge URL inventories with optional search exports using tolerant column mapping.
- `scripts/portfolio_triage.py`: classify URL/export rows into keep, refresh, rewrite, merge, prune, redirect, or manual-review buckets.

Run scripts only when they materially reduce manual work. For small inline data, analyze directly.

## Workflow

1. Build or inspect the URL inventory. Use `sitemap_inventory.py` when sitemap/XML parsing is needed.
2. Segment URLs by section, template, topic, intent, product fit, and page type.
3. Merge traffic/ranking exports if available. Use `merge_search_exports.py`.
4. Distinguish ranking loss from demand loss and transfer of traffic. Load `references/serp-replacement-logic.md`.
5. Sample winners and losers. Use `content_fingerprint.py` for repeated promotional, technical, or template patterns.
6. Evaluate section/template risk. Load `references/template-footprint-risk.md`.
7. Map each URL or group to an action. Load `references/portfolio-action-matrix.md`.
8. Calibrate findings against good/bad editorial systems. Load `references/good-vs-bad-examples.md`.
9. Produce a prioritized audit with evidence strength. Use `references/site-audit-workflow.md`.

## Output Format

Return:

- Scope and data sources
- Key caveats and missing evidence
- Loss/audit map by section, template, topic, intent, and product fit
- SERP replacement findings
- Technical/editorial/promotional fingerprints
- Root-cause hypotheses ranked by evidence strength
- URL action buckets
- Recovery sequence
- Follow-up data needed

Avoid overclaiming causality. Mark update correlation, backlink changes, and AI cannibalization as hypotheses unless supported by query-level and SERP-level evidence.
