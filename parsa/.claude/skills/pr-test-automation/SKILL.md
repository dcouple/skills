---
name: pr-test-automation
description: "Test a PR or branch through affected product flows and report reproducible QA evidence and remaining gaps."
---

# PR Test Automation

## Task-specific references

Before the first run, read [preflight](references/preflight.md). Load only the
integration detail needed by the changed behavior:

- Analytics, attribution, signup/session identity: [analytics](references/analytics.md).
- Provider-side effects or vendor interference: [external integrations](references/external-integrations.md).
- Before uploading evidence or editing PR QA sections: [publishing](references/publishing.md).

Preserve the exact target and external-write grants. PR testing alone does not
authorize release creation, release-asset uploads, production mutations, or
messages to real users. Complete local evidence and other authorized checks
while a publication step is blocked. Do not claim an unrun check passed.

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
   - When screenshots are safe to share, publish them on a repository-owned durable asset surface. For GitHub PRs, prefer an existing long-lived release such as `pr-assets`; do not use an arbitrary temporary host when a suitable repository release is available.
   - For GitHub PR targets where the user asked for PR testing, update the PR description with a concise QA summary where reviewers look first. Use a marked section so reruns replace the latest QA summary without overwriting the author-written description. Use a separate marked QA comment for long evidence, logs, and screenshot galleries when the description would become unwieldy.
   - Include connector/query evidence with event names, identifiers, timestamps, and important properties.
   - Separate passed automated checks from remaining manual checks.
   - Call out artifacts caused by the test harness, such as intentionally prevented navigation or mocked browser properties.

## Stop Conditions

Stop and ask the user before:

- Running real production payments or destructive production mutations.
- Rebasing, force-pushing, or modifying an open PR if the user has not authorized it.
- Posting comments, sending emails, toggling flags, or changing dashboards unless the user asked for that action.

Otherwise, keep going through setup, execution, verification, cleanup, and a concise result summary.

## Fix-Verify Loop Hygiene

- Before driving a browser proof of a just-committed fix, verify the SERVED bundle
  contains it (fetch the bundle URL and grep a distinctive marker, or compare the hash in
  page/script URLs). Dev-server rebuild races cost entire proof rounds and mimic "fix
  didn't work".
- Wait ~45-60s before querying an analytics warehouse for just-captured events; an empty
  result inside that window proves nothing.
