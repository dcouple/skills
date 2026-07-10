# QA verification — external-evidence discipline

> Read by `/do` Step 5's QA-pass dispatches: the `frontend-verifier` driving
> the app, the `backend-verifier` running command-shaped checks. Extends
> `verification-methods.md` — same proof standard, plus the rules that make
> automated QA evidence trustworthy end to end.

## External verification

A network request only proves the app *tried*; ingestion is proven at the
receiving system. When a flow ends in an external system — analytics,
payments, email/SMS, webhooks — confirm arrival there: query the connected
tool or API for the event, never just the browser's network tab. No
connector available → the item is `Left to human — <reason>`, not assumed.

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

## Cleanup

Kill the listeners, processes, and temp state the run started; leftovers
poison the next run's evidence.
