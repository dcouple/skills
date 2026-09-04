---
name: seo-launch
description: Spin up a product's organic-discovery foundations from a repository or website, from product and search research to a complete page plan or verified implementation PRs. Use for a new SEO launch, not a single-page edit or ongoing traffic-loss audit.
---

# SEO Launch

Turn a product into an evidence-backed set of useful, discoverable pages.
Orchestrate the work through its requested finish line; a research report is not
completion when the user asked for implemented pages. Do not promise rankings
or traffic.

## Inputs and finish line

Accept a repository, site URL, or both; optional product notes/PDFs, audience,
markets/languages, page scope, budget, and existing research. Discover missing
technical details from the project. Ask only for choices that materially change
the product positioning, audience, or authorized work.

For a URL-only request without a repository, use the user's chosen output
directory or a clearly reported task-local directory. The `.seo/` paths below
are relative to that location. Do not create or register a repository implicitly.

Choose the mode from the user's request and state it:

- **Plan only:** produce foundations, a page inventory, and an actionable brief;
  do not change application code or open PRs.
- **Through PR:** research, plan, implement, review, test, and create/update the
  scoped PRs. Requires the user's implementation and PR authorization. A URL
  alone or a request to explore an idea is not that authorization.

Prefer the existing marketing repository for public pages. Read an app/backend
repository to verify capabilities when needed; do not infer permission to
refactor it. Keep unrelated app cleanup in a separate workstream.

## Operating rules

- Reuse existing foundations, briefs, analytics, and approved decisions. Never
  replace a user-approved page set with a smaller batch silently. Conversely,
  do not copy another product's competitors, page count, positioning, or byline.
- Map actual search intent before choosing page families. Comparisons,
  alternatives, use cases, guides, integrations, glossary, and identity pages
  are candidates, not a mandatory checklist.
- Distinguish verified product behavior, marketing claims, proposals, and
  unknowns. Never invent pricing, credentials, customers, screenshots, search
  volumes, analytics access, or human approval.
- Use the user's preferred models and budget. Reserve the strongest reasoning
  model for ambiguous positioning and difficult review; use cheaper capable
  workers for research, writing, implementation, and routine checks. Do not
  hardcode a provider or model version.
- Keep one implementation owner per overlapping file set. Start with modest
  concurrency (normally one or two workers); reduce it on resource pressure.
  Research claims once and share the resulting evidence rather than repeatedly
  crawling or polishing quotes in every writer context.
- Merge, deployment, publication, indexing submissions, paid services, and
  production/customer-data access are separate actions requiring appropriate
  authorization. PR completion does not grant them.

## Workflow

### 1. Establish the product and current state

Read repository instructions and supplied materials. Inspect the actual public
site, relevant implemented flows, existing content, sitemap, robots rules,
metadata, and `.seo/` artifacts. Identify the product, specific audience,
problem, differentiator, conversion action, and supported markets/languages.

Reuse `seo-foundations` when available, reading its instructions first; otherwise
perform that research directly. Use this same availability check for other
skills below. Do not depend on a particular local path, agent runtime, or tool.

**Success criteria:** `.seo/foundations.md` records the verified identity,
current coverage, evidence sources, and unresolved assumptions. A real
positioning ambiguity is surfaced, not disguised as a routine editorial choice.

### 2. Research buyer intent and competitors

Search the channels where this audience actually evaluates solutions. Include
manual workflows, services, or non-software alternatives when relevant. Inspect
current search results and competitor pages; retain query, URL, retrieval date,
and the specific claim each source supports. Prefer official sources for
features and prices, and independent buyer evidence for discovery patterns.

Use authorized analytics/search-console data if available. For a greenfield
site, qualitative query evidence is sufficient to plan; do not block on missing
paid SEO tools or invent quantitative demand. Label estimates and hypotheses.
Present the proposed competitor set for correction; where the user delegates
routine choices, record it as agent-selected rather than human-confirmed.

**Success criteria:** a reusable evidence ledger and intent/competitor map
explain why each proposed opportunity belongs to this product. Unsupported
claims are marked unknown or omitted, not endlessly researched.

### 3. Define the complete page set and templates

Create `.seo/page-inventory.md` (or the project's existing equivalent). For each
page record: route, page family, target query and intent, audience job, title,
meta description, supporting evidence, conversion action, related links,
create/update decision, and implementation batch/status. Consolidate overlapping
intent before generating near-duplicate pages.

Define templates around the reader's decision, not a generic word count:

- Comparisons and alternatives: meaningful criteria, tradeoffs, who each choice
  suits, and dated supporting facts. Do not put your product first everywhere
  or assert an exclusive advantage that competitors also provide.
- Guides and use cases: concrete steps/examples, limitations, and a useful
  answer independent of the sales pitch.
- Identity/integration pages: truthful product, author, compatibility, and
  availability details. Include FAQs only when they answer real questions.

Use available page-strategy/content-planning skills where they fit. Do not route
a new site into a data-dependent optimization workflow whose prerequisites are
absent. Preserve the site's design and create enough representative layout
detail to test information depth, mobile behavior, and template suitability.

**Success criteria:** `.seo/launch-brief.md` identifies the complete justified
scope, templates, acceptance criteria, exclusions, dependencies, and batches.
When routine scope decisions are delegated, finalize a proposed inventory with
documented assumptions; otherwise obtain approval before implementing it.
Material positioning or scope changes still require input. Every promised page
is accounted for. In plan-only mode, hand off here with the
measurement plan from step 6; stop before application edits.

### 4. Implement through bounded workstreams

In through-PR mode, use the repository's available implementation workflow
(such as `do`) with the exact brief and evidence paths. Otherwise plan and
implement directly using repository conventions. Review the plan for intent
fidelity and actual code integration before writing the full page set.

Validate representative templates first, then fill the agreed inventory in
bounded batches. Keep a shared product-facts source and route inventory to
prevent drift. Integrate metadata, canonical URLs, crawlability, sitemap,
internal navigation, and appropriate structured data; never add invented
ratings or other unsupported markup. Preserve intentional authentication and
indexing exclusions.

Track stage, owner, artifacts, current commit, next action, and blocker in
`.seo/launch-status.md` or the existing workflow's state artifact. Keep temporary
logs/screenshots out of commits unless the repository expects them. Verify
dispatch delivery before claiming a worker started. Use the environment's
supported monitor/events for continuation, not ad hoc polling scripts.

**Success criteria:** all in-scope pages and infrastructure are integrated in
the intended branch(es), with explicit accounting for any genuine blocker.
Do not stop merely because a worker finished a phase.

### 5. Review, verify, and prepare PRs

Run available editorial review (such as `page-review`) and a focused code review.
Check usefulness, factual support, comparison fairness, duplication, and
template-specific failures. Review fixes in the affected areas rather than
restarting broad reviews indefinitely. Escalate a repeated unresolved finding
with its evidence and a concrete decision needed.

Run the repository's required checks and a route/content audit. Verify built
pages in a browser at desktop and narrow sizes: representative pages from every
template, navigation, links, metadata/canonicals, indexability, accessibility,
and structured-data consistency. Cross-check the full route inventory; a few
screenshots alone do not prove every promised page exists. Document unavailable
checks honestly and use safe local fixtures rather than live customer data.

Create/update scoped PRs when authorized. Tie review and test evidence to the
current head; fixes or rebases invalidate affected downstream verification,
which must run again before handoff. Read back the PR; offer a separate manual
cold-read when useful rather than adding another automatic review loop.
Do not call a PR ready while
actionable correctness findings or required failing checks remain.

**Success criteria:** verified PR URL(s), complete page accounting, current-head
test/review evidence, and clearly stated external-only gaps. If genuinely
blocked, report partial completion and the exact next action, not success.

### 6. Leave a measurement handoff

Record the baseline date, existing available impressions/clicks/indexing and
conversion measures, or explicitly note that no baseline is available. Propose
early crawl/indexing checks after an authorized launch and a 3–6 month review
of query coverage, impressions, CTR, useful conversions, cannibalization, and
pages worth improving or consolidating. Anchor that interval to actual
publication, not PR creation.

**Success criteria:** `.seo/measurement-plan.md` names the metrics, data sources,
review window, and decisions they inform. A proposed reassessment is not a
scheduled job; do not claim monitoring or create an automation without the
necessary tool support and user authorization.
