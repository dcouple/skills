---
name: refactor-simple
description: Analyze a small or medium diff against repository conventions and write a prioritized refactor plan without editing source.
---

# Simple refactor analysis

## Scope

- Resolve the intended PR base, or the remote's actual default branch for standalone work.
- Compare its merge-base with the working tree so committed, staged, and unstaged changes are included; explicitly inspect relevant untracked files too.
- Count handwritten changes separately from generated, vendored, and lockfile changes.
- Use `refactor-deep` for larger or cross-cutting changes; the orchestrator may run both independently.

## Read and evaluate

1. Read repository instructions and nearby implementation/test examples.
2. Read the changed code and enough context to distinguish new defects from pre-existing debt.
3. Verify claimed conventions against the repository before flagging a violation.
4. Assess error handling, confusing control flow, unjustified duplication, and missing documentation where the project expects it.

For example, relative imports are not inherently wrong: they are a finding only where this project's rules or boundaries prohibit them.

## Write the plan

Use the supplied output path, or `tmp/simple-refactor-plan-<timestamp>.md`:

- Classification: size, type, complexity, affected areas, base SHA, working-tree scope, and convention sources.
- Quality score with rationale; the score is a judgment, not measured proof.
- `Critical`, `Warning`, and `Info` findings, each with `file:line`, evidence, proposed fix, and `Auto-fixable: Yes/No`.
- Auto-fixable/manual counts and actionable next steps.
- Put pre-existing debt under `Info`, labeled “pre-existing, not against this PR”; do not lower the score for it.

An empty findings list is valid. Do not turn line-count heuristics or personal style preferences into correctness defects.

## Arguments and handoff

- `--classify-as=<type>` and `--size=<size>` override classification.
- `--strict` requests broader scrutiny, not invented findings.
- Return the plan path; do not apply it. The user or `refactor` owns the approval gate.

## Grain handoff

- If connected, save the plan in the supplied task folder, or `Development Artifacts/YYYY-MM-DD-<task>`; do not read other analyses when assigned a blind pass.
- Keep needed local files and privacy limits; without Grain, continue locally silently.
