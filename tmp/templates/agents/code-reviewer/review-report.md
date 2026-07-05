# Review Report (Code + Security) — agent output format

> Returned **in-conversation** by the Code Reviewer to the Overseer — **not a file**.
> Runs 1+ times in the final-review loop; Must-Fix items loop back to Implement until
> zero Must-Fix (cap 3). The security review is mandatory: security findings live in
> Must Fix / Should Fix with a `(security)` tag — never a separate section, so they
> always count toward the loop's Must-Fix gate. Final outcome folds into `wrapup.md`.
> **Your final message IS the report: begin with the verdict.** Every line is a verdict,
> a finding with `file:line`, or a check you ran — no preamble, no process narration,
> no closing summary.

---

**Verdict:** `<Approve | Request changes>` — `<one-line rationale>`
**Counts:** Must Fix: `<n>` (security: `<m>`) · Should Fix: `<n>` · pass `<k>`/3

## Must Fix  *(blocks merge; loop back to Implement)*
- **MF-1** `(security)` — `<what>` · `<file:line>` · `<fix>` · violates `<D# / AC# | "new issue">`
  - **Failure scenario:** `<concrete way this breaks in production>`   *(required for correctness/security findings)*
- **MF-2** — `<what>` · `<file:line>` · `<fix>` · violates `<…>`

## Should Fix  *(important, non-blocking)*
- **SF-1** — `<what>` · `<file:line>` · `<fix>`

## Nice to Have  *(omit section if empty)*
- `<nit or thought>`

## Praise  *(omit section if empty)*
- `<what the diff got right — specific, so it survives the fix loop>`

## ⚠️ Cannot verify  *(omit if empty)*
- `<requirements you couldn't verify from the diff alone, and what the Overseer should check>`

---
**What a Code Reviewer checks:** correctness vs the plan & item intent · security
(authz, input validation, injection, secrets, unsafe deserialization) — tag findings
`(security)` · missing error handling & edge cases · unneeded complexity /
over-engineering · adequate tests · clear naming · does the diff actually fulfill the
intent (not just the task list). Every finding cites `file:line`.

**Calibration:** Must Fix = ships a bug, a vulnerability, or fails an acceptance
criterion. Should Fix = materially better code, but mergeable without it. Everything
else is Nice to Have — don't inflate severity.

**Re-reviews (pass 2+):** first mark every prior finding by ID as `fixed | persists |
new`, then add anything new. Don't re-litigate what's fixed.
