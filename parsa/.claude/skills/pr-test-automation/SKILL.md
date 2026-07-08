---
name: pr-test-automation
description: Run first-pass automated manual testing for PRs that are reviewed or nearly ready to merge. Use when the user asks Claude to test a PR/branch/worktree, validate product flows, exercise browser or CLI workflows, map changed UI journeys with screenshots, verify analytics/webhooks/payments/email/SMS behavior through connected tools, or produce manual QA notes before human testing.
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
   - Discover verification tools before assuming a manual check is required. If Composio is available, use `composio search` to find candidate inbox, SMS/phone, payment, CRM, support, or provider-log tools, then inspect schemas with `--get-schema` before executing.
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
   - When UI changes are in scope, map each touched surface area and user journey to screenshots in a temporary, easy-to-observe folder such as `tmp/pr-<number>-qa/` or `tmp/<branch>-qa/`. Use ordered filenames that describe the journey step, such as `01-signup-account.png` and `02-dropdown-expanded.png`.
   - Capture meaningful UI states, not only final pages: empty/default, filled/selected, expanded menus, modals, validation errors, loading/success states, and at least one narrow viewport when responsive layout is likely affected.
   - Reuse the same screenshot artifact pattern for local/dev validation and, when the user asks for post-merge production verification, for production paths. Keep local and production artifacts separated by folder or filename.
   - Prefer the app's built-in test/simulation path for external effects: local inboxes, Mailhog-style UIs, fake SMS numbers, test OTP logs, sandbox payment modes, webhook listeners, or provider test keys.
   - Parse local email/SMS verification links or codes from container logs when the local environment emits them.
   - Add small human-paced waits around analytics or step-transition tests so effects and batched events have time to fire in the same order a user would experience.

5. Verify externally, not just locally:
   - Network requests prove the browser tried to send data; connector/API queries prove the product received it.
   - When simulation is unavailable, use connected recipient/provider readback: Gmail/Outlook/IMAP or email-service activity for email; Twilio/Dialpad/OpenPhone/Google Voice/test-number services or provider logs for SMS/voice; Stripe/provider dashboards for payments.
   - Query by the unique marker, test email, phone number, org ID, subscription ID, webhook event ID, request ID, or other stable test value.
   - For webhooks, confirm both CLI/listener output and backend logs, then verify downstream data.
   - For analytics dashboards, query the exact project and call out the date range and filters used.

6. Report results:
   - State what was tested, the exact test identity/marker, and the observed outcome.
   - List screenshot paths for changed UI and explain the user journey, surface area, environment, and UI state each screenshot covers.
   - When screenshots are safe to share, upload them to a true temporary host that returns direct image URLs, or to the app/repo's own temporary upload endpoint if one exists. Prefer retention that comfortably covers review, record the provider and expiration/retention policy, and avoid hosts that delete after the first download.
   - For GitHub PR targets where the user asked for PR testing, post or update one durable QA comment on the PR with tested flows, evidence, screenshot links, and remaining human-review items. Use an HTML marker so reruns update the same comment instead of spamming the thread.
   - Include connector/query evidence with event names, identifiers, timestamps, and important properties.
   - Separate passed automated checks from remaining manual checks.
   - Call out artifacts caused by the test harness, such as intentionally prevented navigation or mocked browser properties.

## PostHog And Browser Analytics

PostHog JavaScript drops capture events from likely bots. Headless Playwright can still fetch PostHog config and run `identify`, while `capture` events are silently dropped because `navigator.webdriver` is `true`, the user agent looks automated, or `navigator.userAgentData.brands` includes `HeadlessChrome`.

When the explicit goal is to validate product analytics in local automation:

- Use a normal browser user agent.
- Mask only the automation bot signals for the test context. Setting `userAgent` is not enough if `navigator.userAgentData` still exposes headless Chrome:

```js
const context = await browser.newContext({
  userAgent:
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' +
    '(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
})

await context.addInitScript(() => {
  const brands = [
    { brand: 'Chromium', version: '125' },
    { brand: 'Google Chrome', version: '125' },
    { brand: 'Not.A/Brand', version: '24' },
  ]
  const fullVersionList = brands.map((brand) => ({
    ...brand,
    version: `${brand.version}.0.0.0`,
  }))

  Object.defineProperty(navigator, 'webdriver', { get: () => undefined })
  Object.defineProperty(navigator, 'userAgentData', {
    get: () => ({
      brands,
      mobile: false,
      platform: 'Windows',
      getHighEntropyValues: async () => ({
        brands,
        mobile: false,
        platform: 'Windows',
        architecture: 'x86',
        bitness: '64',
        model: '',
        uaFullVersion: '125.0.0.0',
        fullVersionList,
      }),
      toJSON: () => ({ brands, mobile: false, platform: 'Windows' }),
    }),
  })
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

## Multi-Surface Attribution Flows

Some PRs only work when a marketing site, API route, installer, desktop app, or mobile client is tested as one product flow. When attribution or install/download analytics cross those boundaries:

- Test companion PRs together in the worktree or preview environment that actually serves each surface.
- Validate route-level behavior directly before browser testing. For install/download flows, assert fresh tokens are accepted, stale or malformed tokens are dropped, invalid files or inputs are rejected, and crawler-facing routes are excluded when needed.
- Browser clipboard tests should compare visible UI text with clipboard text. It is common for the visible command/link to stay clean while the copied value includes a hidden `ref`, `utm`, or attribution token.
- If client-side analytics must create a distinct id but production capture is not part of the test, use a dummy public key and intercept analytics endpoints. If production verification is requested, use a unique marker and query the analytics project afterward.
- Use temporary app data directories for native app tests so config migrations, attribution files, cookies, and local databases do not touch the user's real profile.
- For Electron, Tauri, React Native, or similar native-shell mocks, event subscription APIs must return cleanup functions. Promise-returning mocks for `on*` or `subscribe*` APIs can create false crashes that look like product regressions.
- Direct captures that fire before an analytics SDK is fully initialized need explicit host, token, and distinct-id assertions. A request falling back to the SDK vendor default host before app config loads is usually a product bug, not enough evidence that the event will reach the intended project.
- Capture both the happy path and one negative path: accepted/refreshed attribution, stale or malformed attribution, user opt-in or opt-out, and any server-side invalid-input analytics.

## External Integrations

For payment, email, SMS, analytics, and other third-party integrations:

- Confirm the account/project/mode before running tests.
- Prefer test-mode objects and fake/test cards.
- Prefer recipient/provider-side evidence over send-side success. A 200 response from the app or provider is useful but not enough when the PR's behavior depends on actual delivery, ingestion, webhook receipt, or downstream processing.
- Use plus-addresses, reserved fake phone numbers, sandbox identities, metadata, notes, UTM values, or request IDs so every external artifact can be found without ambiguity.
- Respect production stop boundaries. Do not bypass MFA, consume one-time tokens, send real calls/SMS, create paid subscriptions, charge cards, or mutate customer data unless the user explicitly approved that production action.
- Check for duplicate listeners before starting a new webhook listener.
- Record IDs that let the user or future agent find the test again: email, phone number, org key, customer ID, subscription ID, message ID, webhook event type, dashboard URL, event marker, or screenshot path.
- If a provider key lacks read scopes, try another non-destructive readback source such as a connected mailbox, recipient-side tool, provider dashboard export, app database row, webhook table, logs, or analytics event. Report the scope limitation rather than treating it as product failure.
- Never expose secrets in the final answer. Public analytics tokens are not the same as private API keys, but still describe them carefully.

## PR QA Comments And Screenshots

When testing an open PR, preserve the result where reviewers will look first:

- Create a local artifact folder such as `tmp/pr-<number>-qa/` containing raw screenshots, scripts, manifests, and notes.
- Upload safe UI screenshots after testing. Do not upload PHI, secrets, private customer data, real inbox contents, payment details, or anything that would be inappropriate in a public/shared PR context.
- Prefer direct image links with enough retention for the expected review window. `x0.at` is acceptable for non-sensitive QA screenshots when a longer-lived temp host is needed; it returns direct URLs and uses size-based retention between 3 and 100 days. If a repo or company has a preferred temporary upload API, use that instead.
- Write a local upload manifest with provider, uploaded timestamp, retention/expiration expectation, original local path, URL, and a quick verification that each URL resolves as the expected content type.
- Post or update one PR comment with marker `<!-- codex-pr-test-automation -->`. Include:
  - summary of automated manual QA outcome;
  - test account/org/marker identifiers;
  - user journeys and surface areas tested;
  - screenshots in collapsed `<details>` sections when there are many;
  - connector/provider evidence such as PostHog, Stripe, email, SMS, logs, or database readback;
  - what remains for human review and what was intentionally skipped.
- If PR commenting is not authorized or a connector is unavailable, write the exact Markdown comment body into the artifact folder and report the path.

## Stop Conditions

Stop and ask the user before:

- Running real production payments or destructive production mutations.
- Rebasing, force-pushing, or modifying an open PR if the user has not authorized it.
- Posting comments, sending emails, toggling flags, or changing dashboards unless the user asked for that action.

Otherwise, keep going through setup, execution, verification, cleanup, and a concise result summary.
