# Business Agent Skills

Turn a captured task into a reviewed deliverable using sourced context and fresh-context handoffs.

## Workflow

1. `business-context` gathers facts, sources, constraints, and unknowns.
2. `business-research-adversary` researches stakeholder objections before serious work.
3. `business-discussion` settles the goal, audience, decisions, and risks with the user.
4. `business-spec` writes the specification and requests independent spec review.
5. `business-artifact` drafts the deliverable, maintains the claim/evidence ledger, and requests independent artifact review.
6. `business-prepare-release` performs a fresh final review when preparing delivery.

Use `business-agent-skills` to coordinate the sequence. Individual stages can also be invoked directly; missing context sends the workflow back to context-building.

## Handoffs

- Claude support agents live in `.claude/agents/`; Codex support skills run in fresh subagent contexts when available.
- Pass saved inputs and output locations so each stage works without the full conversation.
- Default local layout: `.business/context/`, `discussion/`, `specs/`, `artifacts/`, and `reviews/`.
- If Grain is connected, keep all task artifacts in the supplied folder, or `Development Artifacts/YYYY-MM-DD-<task>`. Pass its ID and storage rule to every stage; sync outputs from agents without access.
- Keep needed local copies and privacy limits. Without Grain, use the filesystem silently.

## Human gates

- Concentrate discussion on the goal, audience, constraints, and important decisions.
- Continue approved work autonomously; return for material unknowns or required high-stakes judgments.
- Legal, compliance, pricing, security, ROI, contract, and enterprise-stakes claims require human review.
- Preparing a deliverable does not authorize sending or publishing it.

## Examples

- Tiny wording edit: a focused artifact review may be enough.
- Internal decision memo: context → discussion → spec → artifact and review.
- External proposal: the full sequence, including release preparation.
- Regulated work: authoritative research before the spec and required human approval before release.

Keep the full context, discussion, spec, and review sequence for high-stakes external work.
