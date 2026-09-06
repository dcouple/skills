---
name: simple-plan
description: "Plan and complete a straightforward authorized change, or return a short plan when only planning is requested."
argument-hint: "[what the user wants done]"
---

# Simple Plan

Use this for a straightforward change whose scope and success criteria can be
kept in a short plan. Inspect the affected code and its callers, then state the
current behavior, intended result, relevant files, and validation approach.
Expand to `create-plan` when dependencies or unresolved design choices need a
separate implementation contract.

## Authorization and continuation

A request to implement or fix the named work authorizes its ordinary reversible
local steps. A standing run-continuously grant from the coordinating workflow
also supplies plan approval within its recorded scope. Present the short plan
as a progress update and continue; do not ask for the same approval again.
If the user asked only for a plan or explicitly requested a review pause,
return the plan and wait before implementing. Ask when a product decision,
expanded scope, or ungranted external/destructive action is required.

## Complete the change

Keep one implementation owner, integrate the whole requested behavior, and
run the repo's relevant checks. Use `implementation-reviewer` for the final
implementation review; add an independent second lane only when required by
repo policy or when material uncertainty warrants it. Fix actionable in-scope
findings and rerun affected checks. Do not repeat a clean review on unchanged
work or add tests that only restate the implementation.

Continue to `prepare-pr` and requested QA when included in the user's task or
standing workflow grant. Otherwise return the completed change with check
results and remaining limitations. Never infer merge, release, deployment,
production mutation, or additional scope from implementation approval.
