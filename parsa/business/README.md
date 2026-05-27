# Business Agent Skills

Business agents need the same kind of infrastructure that software agents need.

For software, the repo is the system of record: code, docs, tests, conventions, plans, and review artifacts all live somewhere the agent can inspect.

For business work, the equivalent is a task-local filesystem context base: a `.business/` folder of markdown files generated from connected apps, MCP/tool calls, local files, user-provided context, and research.

If it is not in the business context base, it does not exist to the agent.

For the longer explanation, read: [Effectively Tackling Business Work With Agents](https://runpane.com/blog/business-deliverable-factory)

## The workflow

```txt
conversation / task
  -> business-context
  -> business-research-adversary
  -> business-discussion
  -> business-spec
  -> business-spec-reviewer
  -> business-artifact
  -> business-artifact-reviewer
  -> business-prepare-release
```

Each skill gets fresh context. Each skill reads prior artifacts from disk and writes the next artifact to disk. Do not put the whole process into one giant prompt.

## Standard `.business/` handoff structure

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

## Which skill to call

### `business-deliverable-factory`

Use this when you need the map or orchestration. It should tell you which stage to run next, not do all the work itself.

### `business-context`

Use this first for almost any nontrivial business task. It pulls internal context from connected apps, MCP/tools, local files, prior deliverables, and user-provided material into `.business/context/`.

Do not draft yet. Do not spec yet. Build the business repo first.

### `business-research-adversary`

Use this before serious spec work. It captures external stakeholder reality: niche objections, buyer anxieties, competitor praise/complaints, category language, recent discourse, expert disagreement, and naive-sounding claims to avoid.

For regulated work, use authoritative-source research instead of recent discourse.

### `business-discussion`

Use this after context exists but before spec. It probes the human to clarify the goal, audience, reader transformation, constraints, objections, and artifact type.

### `business-spec`

Use this before drafting. It creates `.business/specs/ready/spec.md` from context and discussion artifacts.

The spec should be clear enough that a fresh agent can produce the artifact without reading the original conversation.

### `business-spec-reviewer`

Use this before artifact creation. It attacks the spec for goal fidelity, evidence quality, stakeholder realism, acceptance criteria, and human-review needs.

If the spec is weak, do not draft.

### `business-artifact`

Use this only after the spec is ready. It creates the draft artifact and claim/evidence ledger.

The claim/evidence ledger is the business equivalent of typecheck: every important claim needs evidence, status, risk, and a fix.

### `business-artifact-reviewer`

Use this when the artifact seems done. This is the business equivalent of implementation review plus PR review.

This is where anti-sycophancy belongs. The default stance is: assume the artifact is not done.

### `business-prepare-release`

Use this after review passes. It applies required patches, verifies release readiness, and writes the final artifact plus release checklist.

## Fast paths

### Tiny edit

```txt
business-artifact-reviewer
```

### Medium internal memo

```txt
business-context
business-discussion
business-spec
business-artifact
business-artifact-reviewer
```

### External customer proposal

```txt
business-context
business-research-adversary
business-discussion
business-spec
business-spec-reviewer
business-artifact
business-artifact-reviewer
business-prepare-release
```

### Compliance, legal, security, pricing, or regulated artifact

```txt
business-context
business-research-adversary using authoritative sources
business-discussion
business-spec
business-spec-reviewer
business-artifact
business-artifact-reviewer
human review gate
business-prepare-release
```

## Mental model

Business prompts are not enough. Business agents need infrastructure:

1. connected apps / MCP / tools
2. markdown context files
3. fresh-context skill handoffs
4. specs before artifacts
5. claim/evidence ledgers
6. adversarial review
7. human gates
8. release checklists

The goal is not to make the agent write prettier words. The goal is to make business work compile against reality.
