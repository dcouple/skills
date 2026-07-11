# QA verification — external-evidence discipline

> Read by `/do` Step 5's QA-pass dispatches: the `frontend-verifier` driving
> the app, the `backend-verifier` running command-shaped checks. Extends
> `verification-methods.md` — same proof standard, plus the rules that make
> automated QA evidence trustworthy end to end.

## Discover connected tooling first

Inventory what this environment can already prove things with before the
first flow: MCP servers and connectors (analytics, email/SMS, payments,
CRM — a Composio-style tool catalog often holds an authenticated tool for
the product even when nothing is configured in the repo), authenticated
CLIs (`gh`, payment/cloud CLIs), local containers and their logs. Product
data queried through a connected tool beats any local inference — prefer
it wherever one exists, and name in the report which tools you used and
which were missing.

## Build what's missing

The run is allowed to make its own tools. No browser driver in the repo?
Install one in the scratch directory — never pollute the repo or its
lockfiles. Need a probe script, webhook listener, or log parser? Write it
in scratch and remove it after. Drive UIs by stable user-visible selectors
(labels, button text, routes), and pull verification links/codes from
local service logs when the environment emits them.

## External verification

A network request only proves the app *tried*; ingestion is proven at the
receiving system. When a flow ends in an external system — analytics,
payments, email/SMS, webhooks — confirm arrival there: query the connected
tool or API for the event, never just the browser's network tab. No
connector available → the item is `Left to human — <reason>`, not assumed.
Record what lets a human find the test again: event ids,
customer/subscription ids, dashboard URLs, the date range and filters
queried.

## Unique test identity

Stamp the run's actions with a unique marker (e.g. `agent-e2e-<timestamp>`
in names, emails, note fields) and query external systems by that marker —
it separates this run's evidence from prior runs and from real users.

## Preflight

Before a long flow, verify the tools it needs are alive: authenticated CLIs
(`gh auth status` and peers), running services/containers, connectors,
test-mode keys wherever the flow touches money. A flow that dies at step 7
for a missing login wastes the run — fail fast at step 0.

## Test-mode safety

Stay in test/staging mode by default. Real production mutations — payments,
messages to real users, destructive data operations, feature-flag flips —
are never taken: stop that action, mark the checklist item
`Left to human — <reason>`, and continue the rest of the run.

## Automation artifacts

Products treat automated browsers differently — analytics SDKs silently
drop events from bot-flagged sessions (`navigator.webdriver`, headless
user-agent brands). When the goal is proving ingestion, mask the
automation signals for the test context only, and disclose the masking in
the report. Pace critical flows like a human — batched events need time to
fire in order — and rerun with slower pacing before calling an ordering
anomaly a product bug. Every artifact the harness caused (mocked signals,
prevented navigation, dummy keys) is named in the report, never left to be
mistaken for product behavior.

## Evidence hosting

Screenshots and clips are evidence, not repo content — never commit them.
Upload to whatever host the environment provides and inline the URLs in
the PR comment so previews render where the reviewer reads. Durable +
scriptable: a rolling GitHub release (`gh release create pr-assets` once,
then `gh release upload pr-assets <img>` — asset URLs render inline and
outlive the review). GitHub user-attachment URLs are just as durable but
have no API (browser-only); a project upload endpoint or temporary image
host works too. When only a temporary host is available, note its
expiry next to the link and keep the textual evidence (quoted output, ids)
self-sufficient without the image.

## Cleanup

Kill the listeners, processes, and temp state the run started; leftovers
poison the next run's evidence.
