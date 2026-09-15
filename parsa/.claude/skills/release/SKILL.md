---
name: release
description: Prepare a release pull request with a change summary, risk-ranked testing, and deployment prerequisites.
argument-hint: "[optional: PR title]"
disable-model-invocation: true
---

# Release preparation

## Scope

- Resolve the release source and destination branches from the request or repository policy; `staging` → `main` is only an example.
- Work from existing remote branches. Do not push code, merge, deploy, publish, or apply migrations.
- If the release range is empty, report that there is nothing to release.

## Inspect changes

1. Fetch the relevant refs and read the full release diff.
2. Associate commits with PRs using repository metadata; do not assume merge-commit messages cover squash/rebase histories.
3. Read related PR descriptions and summarize direct commits separately.
4. Build a chronological summary of outcomes, affected areas, and important contract or operational changes.

## Risk-ranked testing

Every item should name an actual changed behavior, its PR/commit, and a concrete expected result.

- Must test: data integrity, permissions, billing, breaking contracts, and migration risks.
- Important: substantial user-facing flows or integration changes.
- Nice to test: lower-risk presentation or interaction changes.
- Low risk / omitted: explain why a change needs no additional manual test.

These are examples, not fixed classifications: a dependency bump or refactor can be high risk. Keep the list practical and avoid duplicate scenarios.

## Deployment prerequisites

- Discover actual schema/migration locations and project tooling; inspect generated SQL only through an authorized, non-applying generation workflow.
- Report destructive operations, ordering requirements, and required review. Do not assume every database supports transactional migrations.
- Identify new configuration/secret names and the service that needs them, never secret values.
- Check infrastructure, CI, external services, dependency changes, backfills, and one-time operations.
- Distinguish prerequisites from actions completed. Production changes remain subject to project approval policy.

## Create or update the PR

1. Run applicable project checks and record pass/fail/blocked with evidence.
2. Find an existing PR for the exact source/destination pair.
3. Use a supplied title or a concise release title; include summary, testing, prerequisites, and check results.
4. Write the body with a safe file tool and submit using `--body-file` or a connector; never interpolate external text into shell source.
5. Preserve author-owned content and read back the PR identity, branches, content, and state.

## Handoff

- Return the PR URL, included changes, highest-risk checks, and unresolved prerequisites.
- If Grain is connected, save preparation artifacts in the supplied task folder, or `Development Artifacts/YYYY-MM-DD-<release>`; rename it `PR-<number>-<title>` when the PR exists.
- Keep needed local files and privacy limits; without Grain, continue locally silently.
