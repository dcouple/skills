# Wrap-Up Report — format

> Produced by `/do` at the end. Saved as `./tmp/<id>/wrapup.md` and posted to the PR.
> This is `/do`'s self-report and the human's starting point for PR review — it folds
> in the **final** review outcome (individual review passes are not persisted).

---
```yaml
---
type: wrap-up-report
item: <id>
pr: <url or #>
---
```

# Wrap-Up Report — `<item>`

## What was built
`<summary of the change, tied back to the item's intent>`

## Verification evidence
`<what was run / driven and the result vs each acceptance criterion.`
`Text/log evidence for now; screenshots/video deferred.>`

## Review outcome
`<final state after the review loop — "Must Fix: 0 · passes used: k/3". Note any`
`Should Fix / Nice to Have items intentionally deferred, and why.>`

## Residual risks / follow-ups
- `<anything unresolved, deferred, or worth a future work item>`

## Deltas vs plan
`<only where the final diff diverges from the plan's Files-changed table — or "none".`
`The full file list lives in the plan and the PR diff; don't repeat it here.>`
