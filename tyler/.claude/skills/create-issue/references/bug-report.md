# Bug Report — format

> Produced by `/create-issue`. Saved as `./tmp/<id>/item.md`.
> Spine: intent = **root cause**, desired state = **correct behavior**. Keep it lean.

---
```yaml
---
type: bug-report
id: <id>
status: draft         # draft | ready | done
severity: <critical | high | medium | low>
pr: <url or # — filled when /do opens it>
---
```

# Bug: `<one-line title>`

## Summary
`<what's broken, in the observed behavior — 1–2 sentences>`

**Environment:** `<version/build · runtime · where observed (prod / staging / local)>`

## Expected vs actual
- **Expected:** `<correct behavior>`
- **Actual:** `<observed behavior — stated as observation, not assumed cause>`

## Steps to reproduce
1. `<numbered steps from a known starting state — deterministic enough that the`
   `verify stage can re-run them to prove the fix>`
2. `<step>`

## Root cause
`<the identified cause. If not yet confirmed, prefix "Hypothesis:" and note confidence`
`(confirmed | likely | hypothesis).>`

## Business impact
`<who / what is affected, how widespread, why it matters now>`

## Suggested resolution path
`<the locked direction for the fix — high level, not code. Omit detail /do can decide.>`

## Verification criteria
`<embed shared/verification-criteria.md — acceptance in EARS + how verify proves the fix.`
`The repro steps above double as the failing case AC1 must flip.>`

## Prevention criteria
`<what stops this class of bug recurring: a regression test, a guard, an invariant>`

## Justification
- `<claim challenged in the Socratic gate>` — `<the reason that held>`

`<distilled from the socrates Q&A: why this cause is the root and not a symptom,`
`why fix now, why this resolution path. On a fast pass, socrates' one line naming`
`what convinced it; if the user waived the gate: "Socratic gate waived by user.">`

## References (optional, in refs/)
- `refs/error-trace.txt`
- `refs/discussion.md`
