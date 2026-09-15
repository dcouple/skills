---
name: seo-content-strategy
description: Turn search, audience, and performance evidence into a prioritized plan for content creation, updates, and technical follow-up.
---

# SEO content strategy

Decide what to do next and why. Planning does not authorize execution.

## Inputs

- Read the latest briefing, foundations, and relevant source data from the supplied destination or shared task folder.
- If evidence is missing, use `seo-briefing` for available performance data or `seo-foundations` for a new site. A zero-traffic site can have a strategy; label its hypotheses.
- Confirm audience, business goals, constraints, and any already-approved work.

## Evaluate opportunities

1. Find pages with meaningful reader or business value, missed intent, poor performance, or technical blockers.
2. Inspect current search results and existing site coverage before proposing a new page.
3. Use measured volume/difficulty when available; do not invent estimates from ordinary search results.
4. Separate quick fixes, substantial rewrites, new pages, and investigations.
5. Rank by likely value, evidence strength, effort, risk, and dependencies. Make uncertainty visible.

Examples of possible actions:

- Revise a title when query-level evidence supports a mismatch.
- Improve an existing explanation rather than creating a duplicate page.
- Investigate indexability before requesting indexing.
- Refresh stale facts; change “last updated” only after a substantive update.
- Create a comparison only when the product belongs in the answer set and fair proof is available.

## Output

Use the requested destination, otherwise `.seo/strategy.md`:

- Source links, dates, goals, and assumptions.
- Prioritized actions with target page/query, evidence, expected benefit, effort, and success check.
- Dependencies, proof gaps, and optional publishing schedule.
- Suggested execution skill: `seo-readability-pass`, `seo-authority-pass`, `seo-content-drafting`, or project-specific equivalent.

Get approval before execution unless the user or authorized parent workflow already approved this scope. Preserve explicit human gates.

## Shared artifacts

If Grain is connected, save the strategy and supporting research in the shared task folder and pass its ID/storage rule downstream. Local paths are working-copy defaults. Otherwise continue normally; do not publish, commit, or push without authorization.
