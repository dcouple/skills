---
name: seo-briefing
description: Summarize available search and analytics evidence into an SEO status report, experiment results, and prioritized next actions.
---

# SEO briefing

Explain what changed, what the evidence supports, and what to investigate next.

## Gather evidence

- Read the site's foundations, prior briefing, and current data manifest when available.
- Use `seo-data-pull` for missing or stale data. Reuse a snapshot only when its property, filters, date range, and freshness match the question.
- Work with available sources or supplied exports. Name gaps; do not require a particular analytics vendor.
- Read experiments in `.seo/experiments/` or the shared task folder; also recognize a legacy `experiments.md` index without creating a second record.

## Interpret carefully

- Compare like-for-like periods and metric definitions; distinguish zero from unknown.
- High impressions with low clicks may suggest a title, intent, position, or SERP-feature issue; inspect before diagnosing.
- For traffic loss, separate demand, ranking, measurement, and competition hypotheses.
- For indexing gaps, check eligibility and technical causes before recommending a submission.
- Compare due experiments against recorded baselines. If data is sufficient, append the measured result and caveats; otherwise mark it awaiting measurement.
- Do not treat correlation or a single before/after result as proof of causality.

## Write the briefing

- Short summary of the most important changes.
- Applicable sections: traffic, search performance, index coverage, rankings, links, and content opportunities.
- Running experiments and measured outcomes, with source links and periods.
- Prioritized actions: evidence, likely value, uncertainty, and next check.
- Missing data and limitations that affect the conclusions.

Use the requested destination, otherwise `.seo/briefing.md`. Cite quantitative claims to the source and exact numbers. Hand off to `seo-content-strategy`; do not change live pages, indexing settings, or integrations.

## Shared artifacts

If Grain is connected, save the briefing, safe snapshots, and experiment updates in the shared task folder; pass its ID/storage rule downstream. Local copies are fine. Otherwise use normal project storage silently. Never automatically commit/push analytics or expose private data.
