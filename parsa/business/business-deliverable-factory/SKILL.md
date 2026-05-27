---
name: business-deliverable-factory
description: Orchestrate the business deliverable workflow from captured task to discussion, spec, artifact, review, and release.
---

Rules: Do not do all work in one context. Business work must pass through filesystem artifacts so each stage gets fresh context.

Principle: software agents need a repo. Business agents need a filesystem context base generated from connected apps, MCP/tools, files, and research. If it is not in the business context base, it does not exist to the agent.

Human attention model:
- Human attention is concentrated in the initial captured conversation/ticket, `business-discussion`, and human gate only when review says it is needed.
- The user should not manually run every support skill.
- The primary skills should coordinate support skills and stop for the human only when blocked or high-stakes review is required.

Default user-facing workflow:
1. captured conversation / task / todo
2. business-discussion
3. business-spec
4. business-artifact
5. business-prepare-release, only if shipping/finalizing

Primary skills:
- `business-discussion`: main human-in-the-loop stage; writes `.business/discussion/brief.md`.
- `business-spec`: coordinates context, research-adversary, spec creation, and spec review; writes `.business/specs/ready/spec.md`.
- `business-artifact`: coordinates artifact creation, claim ledger, artifact review, and anti-sycophancy; writes `.business/artifacts/draft.md` and review artifacts.
- `business-prepare-release`: packages final output only when sending, publishing, presenting, or handing off.

Support skills:
- `business-context` -> builds `.business/context/*`
- `business-research-adversary` -> writes `.business/context/research-adversary.md`
- `business-spec-reviewer` -> writes `.business/reviews/spec-review.md`
- `business-artifact-reviewer` -> writes `.business/reviews/artifact-review.md`

Standard artifact handoff structure:

```txt
.business/
  context/
    context.md
    source-index.md
    known-facts.md
    assumptions-unknowns.md
    constraints.md
    research-adversary.md
  discussion/
    brief.md
  specs/
    ready/spec.md
    done/spec.md
  artifacts/
    draft.md
    final.md
    claim-evidence-ledger.md
  reviews/
    spec-review.md
    artifact-review.md
    release-checklist.md
```

Do not skip context/spec/review for high-stakes external work. Use a fast path only for trivial edits or exact copy/paste work.
