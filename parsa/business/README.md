# Business Agent Skills

Business agents need the same kind of infrastructure that software agents need.

For software, the repo is the system of record: code, docs, tests, conventions, plans, and review artifacts all live somewhere the agent can inspect.

For business work, the equivalent is a task-local filesystem context base: a `.business/` folder of markdown files generated from connected apps, MCP/tool calls, local files, user-provided context, and research.

If it is not in the business context base, it does not exist to the agent.

For the longer explanation, read: [Effectively Tackling Business Work With Agents](https://runpane.com/blog/business-deliverable-factory)

## The normal flow

The business workflow should feel like the engineering workflow.

For engineering, the high-attention human work happens in the initial conversation and `/discussion`. Then `/plan`, `/implement`, and PR review run with as much automation as possible.

For business, use the same shape:

```txt
captured conversation / task
  -> business-discussion
  -> business-spec
  -> business-artifact
  -> business-prepare-release, only when shipping/finalizing
```

The user should not manually run every support skill. Support skills exist so the primary skills can pass work through fresh-context filesystem artifacts.

## Human attention model

Human attention should be concentrated in:

1. the initial captured conversation / todo / ticket
2. `business-discussion`, where the agent probes for goal, audience, decision, constraints, and risk
3. human gate only when review says the artifact is high-stakes, underspecified, or risky

Everything after discussion should run as automatically as possible through the skill stack.

## Primary skills to call

### `business-deliverable-factory`

Use this when you need the map or orchestration. It tells you which primary stage to run next and enforces the file-handoff structure.

### `business-discussion`

Use this as the main human-in-the-loop step. Start here for most serious business work after a conversation/todo has been captured.

It should clarify:

- real business goal
- audience / stakeholders
- desired reader transformation
- constraints
- objections
- artifact type
- what not to do

It writes `.business/discussion/brief.md`.

### `business-spec`

Use this after discussion. It should coordinate the heavy lifting automatically:

- run or refresh `business-context` if context is missing/stale
- run `business-research-adversary` for serious business work
- create `.business/specs/ready/spec.md`
- run or request `business-spec-reviewer`
- stop and ask for human input only if context/spec gaps block progress

This is the business equivalent of `/plan`.

### `business-artifact`

Use this after the spec is ready. It should coordinate:

- artifact creation from the approved spec
- claim/evidence ledger creation
- `business-artifact-reviewer`
- anti-sycophancy review
- human gate if required

This is the business equivalent of `/implement` plus implementation review.

### `business-prepare-release`

Use this only when sending, publishing, presenting, or handing off. It packages the final artifact, verifies review patches, and writes the release checklist.

## Support skills

These are normally invoked by the primary skills, not manually by the user.

### `business-context`

Builds `.business/context/*` from internal/app/file context.

### `business-research-adversary`

Captures external stakeholder reality: niche objections, buyer anxieties, competitor praise/complaints, category language, recent discourse, expert disagreement, and naive-sounding claims to avoid.

For regulated work, use authoritative-source research instead of recent discourse.

### `business-spec-reviewer`

Attacks the spec before artifact creation.

### `business-artifact-reviewer`

Reviews the artifact when it seems done. This is where anti-sycophancy belongs. The default stance is: assume the artifact is not done.

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

## Fast paths

### Tiny edit

```txt
business-artifact-reviewer
```

### Medium internal memo

```txt
business-discussion
business-spec
business-artifact
```

### External customer proposal

```txt
business-discussion
business-spec
business-artifact
business-prepare-release
```

`business-spec` should coordinate context, research-adversary, and spec review internally.

### Compliance, legal, security, pricing, or regulated artifact

```txt
business-discussion
business-spec
business-artifact
human gate
business-prepare-release
```

Use authoritative-source research inside the spec stage.

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
