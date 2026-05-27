---
name: business-artifact
description: Create the business artifact from an approved spec and write a claim/evidence ledger.
---

Rules:
- Read the approved spec first.
- Use only grounded facts from context/spec.
- Do not invent claims, numbers, dates, pricing, commitments, or legal/compliance statements.
- Maintain a claim/evidence ledger.
- Optimize for the artifact type.

Read:
- `.business/specs/ready/spec.md`
- `.business/context/*.md`
- `.business/reviews/spec-review.md`

Write:
- `.business/artifacts/draft.md`
- `.business/artifacts/claim-evidence-ledger.md`

Output:
- draft artifact
- claim/evidence ledger

Claim ledger format:
| Claim | Evidence | Status | Risk | Fix |
|---|---|---|---|---|
