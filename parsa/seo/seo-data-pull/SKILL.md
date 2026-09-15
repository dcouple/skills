---
name: seo-data-pull
description: Collect relevant search and analytics snapshots from available sources, record their scope, and compare compatible periods for an SEO workflow.
---

# SEO data pull

Use as a support step or for a direct data request. Pull what answers the question, not everything a connected account exposes.

## Scope and freshness

- Confirm the site/property, date range, timezone, filters, and metrics.
- Read the current manifest and a relevant prior snapshot before overwriting working data.
- Reuse cached data only when scope and freshness fit the request. A 24-hour cache is a default, not proof that the underlying source is current.
- Respect API quotas and permissions; do not connect accounts or change instrumentation as part of a read-only pull.

## Discover available sources

- Use connected analytics, search consoles, SEO tools, or supplied exports. Examples include GA4, Plausible, PostHog, GSC, Ahrefs, and Semrush; none is mandatory.
- Inspect the actual schema and supported API before writing queries. Record unavailable sources or fields without inventing data.
- Select relevant events and aggregate dimensions. Avoid collecting identifiable people, emails, or organizations unless necessary and authorized.
- Package downloads and repository activity are optional context for projects where those metrics matter.

## Collect snapshots

- Analytics: relevant traffic, landing pages, referrers, and conversion counts/rates.
- Search: clicks, impressions, CTR, position, queries, and page trends where available.
- SEO tools: applicable rankings, links, and competitor gaps, labeled with the provider's definitions.
- Use matching comparison windows, segment definitions, and source filters. Note reporting delays, sampling, incomplete periods, and attribution limits.
- Referrer-domain matches can suggest an AI channel; they do not identify all AI-driven visits.

## Save and summarize

Default working files are `.seo/data/analytics.md`, `search-console.md`, `seo-tool.md`, and `manifest.md`; use supplied locations instead when present.

The manifest records:

- Source/property, query or export reference, filters, timezone, and data period.
- Pull time and source freshness, schema used, coverage, and failures.
- Links to current and prior snapshots, plus experiments awaiting measurement.

Show a compact summary with current, prior, and change columns when useful. Compute deltas only for comparable values; use unknown/“—” for missing baselines and avoid percentage division by zero. Suggest only instrumentation gaps that materially block the question; do not implement them.

## Shared artifacts

If Grain is connected, save safe snapshots, manifests, and reports in the shared task folder and pass its ID/storage rule downstream. Preserve dated versions; local query/export files may be working copies. Otherwise use normal project storage silently. Do not automatically commit/push analytics or upload sensitive raw records.
