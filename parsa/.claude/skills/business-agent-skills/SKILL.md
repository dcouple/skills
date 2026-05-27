---
name: business-agent-skills
description: Orchestrate business work from a captured task through context, discussion, spec, artifact, review, and release — each stage in fresh context via filesystem handoff.
---

Rules: You MUST NOT do all the work in one context. Each stage MUST run fresh and hand the next stage a file under `.business/`.

Principle: software agents need a repo. Business agents need a filesystem context base built from connected apps, MCP/tools, files, and research. If it is not in the context base, it does not exist to the agent.

Human attention model:
- Human attention concentrates in two places: the initial captured conversation/ticket, and `business-discussion`.
- After discussion, spec -> artifact -> release should run with as much automation as possible.
- Return to the human only at the gate, and only when review says the work is high-stakes, underspecified, or risky.

Context comes before discussion (REQUIRED):
- `business-context` and `business-research-adversary` build the context base. They MUST run BEFORE `business-discussion`, and MUST NOT be run inside `business-spec`.
- NEVER discuss or spec on an empty context base. A discussion with no assembled context is the agent guessing.
- `business-research-adversary` is a context step (external stakeholder reality), NOT a spec step. It writes into `.business/context/` and feeds both discussion and spec.

What the human runs:
- Aspiration: a conversation, then `business-discussion`, then one look at the gate. The stack runs context -> spec -> artifact -> release for you.
- Manual / full control: `business-discussion` -> `business-spec` -> `business-artifact` -> `business-prepare-release`.

Internal sequence (the order stages actually execute):
1. business-context            -> `.business/context/*` (auto, before discussion)
2. business-research-adversary -> `.business/context/research-adversary.md` (auto, before discussion)
3. business-discussion         -> `.business/discussion/brief.md` (human-in-the-loop; ensures 1-2 ran first)
4. business-spec               -> `.business/specs/ready/spec.md` (+ business-spec-reviewer)
5. business-artifact           -> `.business/artifacts/draft.md` + ledger (+ business-artifact-reviewer)
6. business-prepare-release    -> fresh adversarial pass + `.business/artifacts/final.md` + checklist (only when shipping)

Primary skills (human-facing):
- `business-discussion`: main human stage; ensures the context base exists, then clarifies goal/audience/decision/risk.
- `business-spec`: business `/plan`; consumes context + brief, writes the spec, runs spec review.
- `business-artifact`: business `/implement` + review; drafts the artifact, builds the claim/evidence ledger, runs artifact review.
- `business-prepare-release`: business PR review + ship; runs a fresh adversarial pass, then packages the final output and release checklist. Only when sending, publishing, presenting, or handing off.

Support stages (fresh-context; in Claude these are sub-agents in `.claude/agents/` for true context isolation, in Codex they are skills; invoked by the primary stages, not run by hand):
- `business-context`            -> builds `.business/context/*`
- `business-research-adversary` -> writes `.business/context/research-adversary.md`
- `business-spec-reviewer`      -> writes `.business/reviews/spec-review.md`
- `business-artifact-reviewer`  -> writes `.business/reviews/artifact-review.md`

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

You MUST NOT skip context/discussion/spec/review for high-stakes external work. Use a fast path only for trivial edits or exact copy/paste work.
