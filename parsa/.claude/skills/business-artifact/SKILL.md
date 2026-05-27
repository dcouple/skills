---
name: business-artifact
description: Create the business artifact from an approved spec, then coordinate claim/evidence ledger creation, artifact review, anti-sycophancy review, and human gate.
---

Role: This is the business equivalent of `/implement` plus implementation review. After the spec is ready, this skill should do as much as possible automatically.

Rules:
- MUST read the approved spec first.
- MUST use only grounded facts from context/spec.
- MUST NOT invent claims, numbers, dates, pricing, commitments, or legal/compliance statements.
- MUST maintain a claim/evidence ledger.
- MUST optimize for the artifact type.
- After the draft and claim ledger, you MUST run or request `business-artifact-reviewer`.
- MUST apply required patches when review identifies concrete fixes.
- Stop for human input only when review requires a human gate or the artifact cannot be safely completed from available context.

Read:
- `.business/specs/ready/spec.md`
- `.business/context/*.md`
- `.business/reviews/spec-review.md`

Write:
- `.business/artifacts/draft.md`
- `.business/artifacts/claim-evidence-ledger.md`
- `.business/reviews/artifact-review.md` via `business-artifact-reviewer`

Output:
- draft artifact
- claim/evidence ledger
- artifact-review result
- concise next step: patch / human gate / prepare release

Claim ledger format:
| Claim | Evidence | Status | Risk | Fix |
|---|---|---|---|---|
