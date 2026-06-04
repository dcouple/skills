---
name: pr-test-automation
description: Run first-pass automated manual testing for PRs that are reviewed or nearly ready to merge. Use when the user asks Claude to test a PR/branch/worktree, validate product flows, exercise browser or CLI workflows, verify analytics/webhooks/payments/email/SMS behavior through connected tools, or produce manual QA notes before human testing.
---

# PR Test Automation

## Overview

Validate as much of a PR as possible with local services, browser automation, CLIs, logs, and product connectors before the user does final manual testing. Treat this as a first-pass QA workflow: prove what works with evidence, identify what still needs a human, and preserve a reproducible trail.

## Workflow

1. Confirm the test target:
   - Identify PR numbers, branches, worktrees, related companion PRs, and whether the user allowed rebasing/syncing.
   - Check `git status`, current branch, remotes, and whether unrelated local changes exist.
   - Inspect PR descriptions/review notes when they define required manual flows.

2. Check tools and authentication up front:
   - Verify required CLIs and connectors before starting long tests: `gh auth status`, `stripe --version` / active listener state, Docker status, PostHog/GitHub/Gmail connectors, cloud CLIs, or app-specific CLIs.
   - Prefer connected app tools for product data verification. Do not assume credentials are current.
   - Use test-mode accounts, test keys, local containers, and staging-safe endpoints unless the user explicitly asks for production verification.

3. Prepare the environment:
   - Install dependencies only where needed and report anything that changes lockfiles.
   - Start required dev servers or confirm existing sessions, ports, and mounted worktrees.
   - For companion PRs, test the combined state in the worktree/container that actually serves the code.
   - Avoid leaving duplicate background listeners or servers. List and clean up only processes started for the test.

4. Build the automated test path:
   - Use Playwright when browser behavior matters. If the repo lacks Playwright, install it in a temporary directory rather than polluting the repo.
   - Use stable, user-visible selectors first: labels, placeholders, button text, URLs, and route state.
   - Generate unique short test identities and attribution markers such as `agent-e2e-<timestamp>`.
   - Parse local email/SMS verification links or codes from container logs when the local environment emits them.
   - Add small human-paced waits around analytics or step-transition tests so effects and batched events have time to fire in the same order a user would experience.

5. Verify externally, not just locally:
   - Network requests prove the browser tried to send data; connector/API queries prove the product received it.
   - Query by the unique marker, test email, org ID, subscription ID, webhook event ID, or other stable test value.
   - For webhooks, confirm both CLI/listener output and backend logs, then verify downstream data.
   - For analytics dashboards, query the exact project and call out the date range and filters used.

6. Report results:
   - State what was tested, the exact test identity/marker, and the observed outcome.
   - Include connector/query evidence with event names, identifiers, timestamps, and important properties.
   - Separate passed automated checks from remaining manual checks.
   - Call out artifacts caused by the test harness, such as intentionally prevented navigation or mocked browser properties.

## PostHog And Browser Analytics

PostHog JavaScript drops capture events from likely bots. Headless Playwright can still fetch PostHog config and run `identify`, while `capture` events are silently dropped because `navigator.webdriver` is `true` or the user agent looks automated.

When the explicit goal is to validate product analytics in local automation:

- Use a normal browser user agent.
- Mask only the automation bot signal for the test context:

```js
await context.addInitScript(() => {
  Object.defineProperty(navigator, 'webdriver', { get: () => undefined })
})
```

- If the UI branches on OS or desktop/mobile, set the relevant platform signal intentionally and disclose it:

```js
await context.addInitScript(() => {
  Object.defineProperty(navigator, 'platform', { get: () => 'Win32' })
})
```

- Keep the page open long enough for PostHog batching, or trigger an unload only after waiting.
- Query PostHog for the unique marker. Do not treat `flags` or config requests as evidence that capture events were ingested.
- If event order looks wrong under automation, rerun with human-paced waits before treating it as a product bug.

## External Integrations

For payment, email, SMS, analytics, and other third-party integrations:

- Confirm the account/project/mode before running tests.
- Prefer test-mode objects and fake/test cards.
- Check for duplicate listeners before starting a new webhook listener.
- Record IDs that let the user or future agent find the test again: email, org key, customer ID, subscription ID, webhook event type, dashboard URL, or event marker.
- Never expose secrets in the final answer. Public analytics tokens are not the same as private API keys, but still describe them carefully.

## Stop Conditions

Stop and ask the user before:

- Running real production payments or destructive production mutations.
- Rebasing, force-pushing, or modifying an open PR if the user has not authorized it.
- Posting comments, sending emails, toggling flags, or changing dashboards unless the user asked for that action.

Otherwise, keep going through setup, execution, verification, cleanup, and a concise result summary.
