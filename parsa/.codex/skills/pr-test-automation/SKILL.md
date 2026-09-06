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
   - When a journey is driven by a scriptable browser driver, record it as a video alongside the stills. One video per journey, recorded at the driver level (e.g. Playwright's `recordVideo`) so it is a free byproduct of the drive, not a second pass. Keep the driver's native format (WebM from browser, MP4 from simulator). Videos complement stills, never replace them: per-step captures remain the frame-addressable evidence, the video is the continuity check. Where ffmpeg is available, scan for blank-frame bands (`ffprobe -f lavfi "movie=<video>,fps=5,signalstats" -show_entries frame=pts_time -show_entries frame_tags=lavfi.signalstats.YAVG`; YAVG ~235 is blank white) and report layout jumps, white flashes, or dead time as findings with timestamp ranges.
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

   Open with a verdict, then the evidence. The structure:

   ```
   Verdict: <all-proven | partial | blocked-env | blocked-auth | product-bug-found>

   | Journey / Check | Result | Evidence |
   |-----------------|--------|----------|
   | <flow or check> | Pass / Fail / Blocked / Left to human | <quoted output, screenshot ref, connector readback> |

   Skipped (with rationale):
   - <item>: <why it was skipped, not just "skipped">

   Cleanup disposition:
   | Created | Marker | System | Disposition |
   |---------|--------|--------|-------------|
   | <account, org, record> | <run marker> | <staging / analytics / billing> | deleted · registered (<why not safe>) · none created |
   ```

   A pass without quoted evidence is not a pass. "Blocked" is a terminal
   verdict: when a check cannot be exercised (missing env, service down,
   no credentials), stop trying rather than improvising a workaround.
   Improvised test routes are not evidence.

   Terminal states and what the human should do next:
   - `all-proven`: every check passed with evidence. Ready for human review.
   - `partial`: some checks passed, others left to human. List the gaps.
   - `blocked-env`: environment issue (service down, container missing). Name the blocker.
   - `blocked-auth`: missing credentials or connector scopes. Name what is needed.
   - `blocked-timeout`: wall clock expired before all checks completed. List what finished and what remains.
   - `product-bug-found`: a check failed and the failure is in the product. Describe the bug with evidence.

   Beyond the verdict, the report must include:
   - The exact test identity/marker used for external queries.
   - Screenshot paths for changed UI, organized by journey step with the surface area, environment, and UI state each covers.
   - Video paths for journey recordings, with duration and what each evidences.
   - Connector/query evidence with event names, identifiers, timestamps, and important properties.
   - What was intentionally skipped and why (per item, not a blanket "some things were skipped").
   - Artifacts caused by the test harness (mocked browser properties, prevented navigation, masked automation signals).

   When screenshots are safe to share, publish them on a repository-owned durable asset surface. For GitHub PRs, prefer an existing long-lived release such as `pr-assets`; do not use an arbitrary temporary host when a suitable repository release is available. For GitHub PR targets where the user asked for PR testing, update the PR description with a concise QA summary where reviewers look first. Use a marked section so reruns replace the latest QA summary without overwriting the author-written description. Use a separate marked QA comment for long evidence, logs, and screenshot galleries when the description would become unwieldy.

## Stop Conditions

Stop and ask the user before:

- Running real production payments or destructive production mutations.
- Rebasing, force-pushing, or modifying an open PR if the user has not authorized it.
- Posting comments, sending emails, toggling flags, or changing dashboards unless the user asked for that action.

Otherwise, keep going through setup, execution, verification, cleanup, and a concise result summary.

## Run Bounds

Set a 90-minute wall clock for the entire run. Per-journey, allow at most 2
retry attempts before marking the journey failed or blocked. No combination
of retries extends the wall clock. If the wall clock expires mid-journey,
finalize evidence for what completed, mark in-progress items as
`blocked-timeout`, and report.

## Cleanup Discipline

The run's unique marker names real things that now exist in external systems:
accounts, organizations, records, subscriptions, analytics events. Disclosure
alone is not disposal.

Delete in-run only when all three conditions hold:

1. The surface is **non-production**, established from the environment the drive
   actually reached (the ingestion target, the key, the project id), not
   assumed from the stack you launched.
2. The deletion is **scoped by this run's unique marker**, not a broader query.
3. The drive **already holds** the credentials that perform it.

If any condition fails or is uncertain, do not delete. Register the item:
name the marker, the system, and what remains, precisely enough that a
repo-side reaper can find it by marker alone. Production analytics and
live-mode billing are register-only by default.

Either way the disposition appears in the report's cleanup table. "None
created" is a disposition too, not an excuse to omit the table.

## Fix-Verify Loop Hygiene

- Before driving a browser proof of a just-committed fix, verify the SERVED bundle
  contains it (fetch the bundle URL and grep a distinctive marker, or compare the hash in
  page/script URLs). Dev-server rebuild races cost entire proof rounds and mimic "fix
  didn't work".
- Wait ~45-60s before querying an analytics warehouse for just-captured events; an empty
  result inside that window proves nothing.
