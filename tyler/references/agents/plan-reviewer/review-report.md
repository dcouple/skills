# Review Report (Plan) — agent output format

> Returned **in-conversation** by the Plan Reviewer to the Overseer — **not a file**.
> Runs 1+ times in the plan-review loop; the Overseer feeds Must-Fix items back into the
> plan and re-reviews until zero Must-Fix (cap 3; light lane 1), then implement proceeds.
> **Your final message IS the report: begin with the verdict.** Every line is a verdict,
> a finding with a location, or a check you ran — no preamble, no process narration,
> no closing summary.

---

**Verdict:** `<Approve | Request changes>` — `<one-line rationale>`
**Counts:** Must Fix: `<n>` · Should Fix: `<n>` · pass `<k>`/`<cap>`

## Must Fix  *(blocks; loop back to plan)*
- **MF-1** — `<what>` · `<where: plan section>` · `<concrete fix>` · violates `<D# / AC# | "new issue">`

## Should Fix  *(important, non-blocking)*
- **SF-1** — `<what>` · `<where>` · `<fix>`

## Nice to Have  *(omit section if empty)*
- `<nit or thought>`

## Praise  *(omit section if empty)*
- `<what the plan got right — specific, so it survives revision>`

## ⚠️ Cannot verify  *(omit if empty)*
- `<what you couldn't check from the plan + repo alone, and what the Overseer should confirm>`

---
**What a Plan Reviewer checks:** repo accuracy (referenced files/anchors exist) ·
completeness (gaps, missing integration points, ordering) · correctness of approach ·
simplification opportunities · fidelity to the item's intent, locked decisions & non-goals ·
altitude (no line-level detail; placeholder leakage — "TBD" in a plan — is a Must Fix) ·
dead code (a replacement plan with an empty Deprecated / removed section is a finding).

**Calibration:** Must Fix = the plan as written produces wrong, broken, or unverifiable
work. Should Fix = a materially better plan, but this one can proceed. Everything else
is Nice to Have — don't inflate severity.

**Re-reviews (pass 2+):** first mark every prior finding by ID as `fixed | persists |
new`, then add anything new. Don't re-litigate what's fixed.
