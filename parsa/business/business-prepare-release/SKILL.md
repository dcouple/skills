---
name: business-prepare-release
description: Prepare a reviewed business artifact for release, delivery, or human approval.
---

Role: Final gate before anything leaves the building. The business analog of cloud PR review — a fresh set of eyes, independent of the artifact-stage review.

Rules:
- Run a fresh-context adversarial pass first: read the artifact cold, as if you had never seen it, before touching the checklist.
- Do not materially rewrite unless the fresh pass or prior review requires it.
- Verify required patches are applied.
- Verify human gate status.
- Produce final artifact and release checklist.

Read:
- `.business/artifacts/draft.md`
- `.business/reviews/artifact-review.md`
- `.business/artifacts/claim-evidence-ledger.md`
- `.business/specs/ready/spec.md`

Fresh adversarial pass (cold eyes, distinct from the artifact reviewer):
- Would a hostile or distracted recipient find the hole the earlier review missed?
- Does the core ask survive a 20-second skim?
- Is there any claim, number, or commitment we would be embarrassed to defend out loud?
- What did familiarity with this artifact make us stop noticing?
If the pass finds a real problem, send it back instead of shipping.

Write:
- `.business/artifacts/final.md`
- `.business/reviews/release-checklist.md`

Checklist:
- reader and ask are obvious
- opening makes stakes clear
- no unsupported claims remain
- numbers/names/dates/pricing/commitments are consistent
- research-adversary objections addressed or intentionally excluded
- formatting/links/tables/screenshots work
- risks are named instead of hidden
- required human review is done or queued
