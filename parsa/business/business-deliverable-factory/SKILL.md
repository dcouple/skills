---
name: business-deliverable-factory
description: Orchestrate the business deliverable workflow from context base to discussion, spec, artifact, review, and release.
---

Rules: Do not do all work in one context. Business work must pass through filesystem artifacts so each stage gets fresh context.

Principle: software agents need a repo. Business agents need a filesystem context base generated from connected apps, MCP/tools, files, and research. If it is not in the business context base, it does not exist to the agent.

Workflow:
1. business-context -> build `.business/context/*`
2. business-research-adversary -> write `.business/context/research-adversary.md`
3. business-discussion -> write `.business/discussion/brief.md`
4. business-spec -> write `.business/specs/ready/spec.md`
5. business-spec-reviewer -> write `.business/reviews/spec-review.md`
6. business-artifact -> write `.business/artifacts/draft.md` and `.business/artifacts/claim-evidence-ledger.md`
7. business-artifact-reviewer -> write `.business/reviews/artifact-review.md`
8. business-prepare-release -> write `.business/artifacts/final.md` and `.business/reviews/release-checklist.md`

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
