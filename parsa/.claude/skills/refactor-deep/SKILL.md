---
name: refactor-deep
description: Analyze a large or cross-cutting diff for correctness and repository-specific design issues, producing a plan without editing source.
---

# Deep refactor analysis

## Scope and discovery

- Resolve the intended PR base, or the remote's actual default branch for standalone work.
- Compare its merge-base with the working tree, including relevant untracked files; distinguish handwritten change from generated/vendor/lockfile volume.
- Read instructions and representative code/tests for each affected layer. Use the repository's names and boundaries, not a preferred architecture.
- Classify actual complexity; a large mechanical change need not be architecturally complex.

## Correctness first

Read every new or materially changed path far enough to answer relevant questions:

- I/O: what happens on timeout, early exit, partial writes, failed handshakes, or unavailable resources?
- Guards: can another entrypoint bypass validation, permissions, or platform checks?
- Lifecycle: are listeners, timers, processes, and in-flight work cleaned up at the right boundary?
- State: does changing session, account, or resource identity leave stale data or authorization behind?
- Portability: do paths, shells, encodings, or runtime assumptions break supported environments?
- Coverage: which concrete regression would existing or proposed tests need to catch?

Report a concrete failure and `file:line` evidence; reproduce safely when useful. Label unproven concerns and the evidence needed, rather than presenting them as confirmed defects.

## Design and conventions

- Check imports, layering, error propagation, state/data contracts, and documentation against actual project conventions.
- Consolidate similar code only when it shares a real contract; an options parameter is not automatically better than separate functions.
- Keep intended behavior and compatibility requirements explicit.
- Separate new issues from pre-existing debt, which belongs under `Info` without lowering the score.

## Write the plan

Use the supplied path, or `tmp/deep-refactor-plan-<timestamp>.md`:

- Classification, base SHA, working-tree scope, affected layers, and convention sources.
- Quality score with rationale, not a manufactured precision target.
- `Critical`, `Warning`, and `Info` sections; each finding includes `file:line`, failure/evidence, fix, and `Auto-fixable: Yes/No`.
- Preserve reproductions, source references, auto-fixable/manual counts, and priority order.
- An empty section is valid; never manufacture defects to fill the template.

## Arguments and handoff

- `--classify-as=<type>` / `--size=<size>` override classification.
- `--force-all-patterns` includes all applicable repository conventions; `--strict` requests broader scrutiny without changing evidence standards.
- Return the plan path without applying fixes. Under `refactor`, remain blind to other analyses and let the orchestrator merge once.

## Grain handoff

- If connected, save the plan in the supplied task folder, or `Development Artifacts/YYYY-MM-DD-<task>`; preserve blind inputs across analyses.
- Keep needed local files and privacy limits; without Grain, continue locally silently.
