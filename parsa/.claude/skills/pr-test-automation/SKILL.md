---
name: pr-test-automation
description: Test a PR's product journeys with reproducible evidence, identify bugs and blocked checks, and prepare a human QA handoff.
---

# PR test automation

## Scope and authority

- Identify the repository, PR, branch/worktree, companion changes, requested journeys, and permitted environments.
- Testing does not authorize source fixes, rebasing, pushing, PR edits, real messages/payments, or production mutations. Honor explicit parent-workflow grants without asking again.
- Prefer test accounts, sandbox providers, local inboxes, and isolated app/browser profiles; never bypass MFA or use real customer profiles.
- Default bounds: 90 minutes total and at most two retries per journey. Report `blocked-timeout` when time expires.

## Preflight

1. Read the PR's current manual-test checklist and relevant diff/review notes. Pass the explicit PR selector to every GitHub query.
2. Check mergeability and the intended base. Report conflicts rather than testing a head that needs resolution.
3. Confirm the tested checkout contains the PR head; for companion PRs, verify ancestry and record the composite SHA.
4. Check configured CI, services, ports, authentication, and provider mode. Explain absent/path-filtered CI rather than assuming it passed.
5. Finish any already-authorized refactor or PR-body clarification before QA. Never launch extra reviews/refactors just to satisfy this skill.

## Drive the journeys

- Use the available project/browser tooling; Playwright is one option, not a required dependency. Keep temporary tooling isolated from the repository.
- Map each acceptance criterion to a journey and expected result. Include relevant failure, permission, empty, and responsive states.
- Use stable user-visible selectors and a unique marker such as `agent-e2e-<timestamp>`.
- Capture ordered screenshots, for example `01-form.png` and `02-validation-error.png`, with environment and state labels.
- Record video alongside screenshots when the driver supports it; export recordings before closing their owning session.
- Verify downstream effects using recipient/provider readback, database state, or logs. A network request or send-side 200 alone does not prove delivery or ingestion.
- If the preferred readback lacks scope, try an authorized read-only alternative; report unavailable proof as blocked, not passed or a product bug.

## Conditional checks

- Analytics: verify the actual project, host, identity, event properties, and ingestion. Allow the system's normal ingestion delay before concluding an event is absent.
- Headless analytics: distinguish SDK bot filtering from product failure. In authorized local tests, use the SDK's supported test configuration or a controlled browser context; disclose any altered browser signals.
- Identity changes: group by the provider's canonical person/user ID, not mutable event-time properties. For PostHog, inspect `person_id` and raw `distinct_id`.
- Shared-device or identity-stitching changes: test account switches in one browser and verify both analytics separation and functional session/auth state.
- Navigation events: verify delivery across unloads using the SDK's supported transport, not a prescribed transport for every SDK.
- Cross-surface flows: test companion surfaces together, valid/invalid or stale tokens, and visible versus copied values where attribution is appended.
- Native apps: isolate app data; match mocks to real contracts, including subscription cleanup behavior.
- Rechecking fixes: verify the served bundle includes the new commit. Separate extension interference, sandbox throttling, and stale builds from product bugs.

## Durable evidence

- Save scripts, screenshots, recordings, report Markdown, and `pr-assets-manifest.json` in the supplied location, or `tmp/pr-<number>-qa/`.
- Classify files before upload. Keep secrets, PHI, real inboxes, payment/MFA data, and private customer/admin evidence out of shared artifacts; redact only when the result can be verified.
- For PR images, reuse a suitable repository-owned published long-lived release, such as `pr-assets`; do not use a temporary host or create one release per PR.
- Creating the release requires an exact grant, for example `{"action":"create_release","repo":"owner/name","tag":"pr-assets"}`. Use the actual default branch and `--latest=false`; PR/upload permission alone does not grant creation.
- Without publication authority, save exact intended create/upload commands and marked Markdown, and report the blocker.
- Name assets with PR/branch, tested SHA, content hash, and step; for example `pr-42-a1b2c3d-<sha12>-02-error.png`.
- Reuse identical assets only after verifying their digest. Never clobber different bytes under an existing name; extend the hash or use a deterministic suffix.
- After upload, verify release/asset metadata and directly GET the bytes, checking size, SHA-256, and decoded type. A login page or HEAD response is not proof.
- Record repository, release tag/URL, PR, head, source path, step, filename, hash/size, API/download URLs, upload/reuse status, timestamp, and verification result in the manifest. Exclude credentials.

## PR handoff, when authorized

- Update only `<!-- pr-test-automation-summary:start -->` through `<!-- pr-test-automation-summary:end -->` in the body.
- Use one detailed comment bounded by `<!-- pr-test-automation-detail:start -->` / `<!-- pr-test-automation-detail:end -->` for longer evidence.
- Migrate legacy `<!-- codex-pr-test-automation-summary -->` and `<!-- codex-pr-test-automation -->` sections once; preserve all other author text.
- Include status, tested commits, journeys, safe markers, provider evidence, and remaining human checks.
- Show safe screenshots inline, ordered by journey, with a short explanation of what each proves. Use a compact gallery for larger sets.
- Write bodies as data using body-file/JSON inputs, then read back identity, content, formatting, and image URLs. Do not interpolate external text into shell source.

## Cleanup and freshness

- Stop only processes started by this test. Delete test objects only in a verified non-production environment, scoped by this run's marker, with existing authorized credentials.
- Otherwise register each remaining object with its system, marker, and cleanup reason. Production analytics and live billing are register-only by default.
- Record tested SHAs and checklist version. After changes, revalidate affected journeys on the new head; expand coverage only where the impact warrants it or the parent requires it.
- QA does not add review loops. Return bugs to the implementation authority and honor the parent's bounded revalidation sequence.

## Report

- Verdict: `all-proven`, `partial`, `blocked-env`, `blocked-auth`, `blocked-timeout`, or `product-bug-found`.
- Journey table: expected result, pass/fail/blocked, and quoted or linked evidence.
- Artifact links, test markers, intentional mocks, skipped checks with reasons, and remaining human work.
- Cleanup table: created object, marker, system, disposition; include “none created” when applicable.

## Grain handoff

- If connected, read/update all safe QA artifacts in the supplied task folder, or `Development Artifacts/YYYY-MM-DD-<task>`; pass this rule to helpers and sync their outputs.
- Keep required local files and privacy limits; without Grain, continue locally silently. A Grain copy does not replace durable PR-image verification or grant publication authority.
