---
name: reality-check
description: Compare a project's documented promises with current evidence and report what works, is missing, or remains unproven.
---

# Reality check

## Establish the promises

- Use the supplied project/plan, or the current project when none is given.
- Read relevant briefs, documentation, roadmaps, and PR descriptions; extract concrete, falsifiable promises.
- Example: “Installs with one command” is testable; “modern architecture” is not.
- Record the current branch/commit and document versions. Check what exists now, not what future work might deliver.

## Test and classify

Use the cheapest honest, authorized check; inspect commands before running them and isolate test artifacts.

- Works: evidence demonstrates the promised behavior.
- Exists but unproven: implementation is present but proof is missing.
- Partial: identify the exact missing portion.
- Absent: no implementation found within the stated search scope.
- Contradicted: behavior conflicts with the promise, including stale documentation.
- Untestable here: name missing credentials, hardware, or other prerequisites; this is not a soft pass.

Also look for meaningful functionality or abandoned scaffolding that the documents do not mention.

## Report

- Lead with a plain-language assessment, not an invented completion percentage.
- List promises, verdicts, evidence, and gaps; put contradictions first.
- Explain the most consequential next gaps and claims the documents should stop making.
- Produce a chat summary and an HTML report using `html-explainer`; use a verdict map or cards where they help scanning.
- If a separate writer is used, give it the complete findings and verify that none were dropped or softened.

## Boundaries and artifacts

- Report findings without fixing code, updating docs, or creating tickets unless separately requested.
- Use the supplied output location, or `tmp/`; if Grain is connected, also save the report and evidence in the task folder, or `Development Artifacts/YYYY-MM-DD-<task>`.
- Pass the storage rule to helpers, keep needed local files and privacy limits, and fall back locally silently without Grain.
