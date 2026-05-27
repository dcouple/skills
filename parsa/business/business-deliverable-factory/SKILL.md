---
name: business-deliverable-factory
description: Convert nontrivial business work from conversation into a filesystem context base, spec, reviewed artifact, and final release gate. Use for decks, memos, proposals, calculators, customer-facing docs, compliance answers, and other stakeholder-facing deliverables.
---

# Business Deliverable Factory

Use this skill for nontrivial business work where a conversation, sprint kickoff, standup, customer call, or rough task needs to become a high-quality business deliverable. This is the business equivalent of the engineering factory: conversation → business context base → discussion → spec → spec review → artifact → artifact review → human gate.

This skill is not only a polish checklist. The anti-sycophancy review is the final PR-review stage. The full workflow starts much earlier by turning ambiguous business intent into a reviewable business work ticket, filesystem context base, and deliverable spec before drafting.

## Simple explanation

Software agents work when they have a repo. Business agents work when they have a context base.

For software, the repo contains the truth: files, dependencies, tests, issues, docs, conventions, and history. For business, the truth is scattered across apps: meetings, docs, tickets, todos, emails, chat, CRM, spreadsheets, prior deliverables, customer calls, files, and the public internet.

The business equivalent of a monorepo is a normalized filesystem context base: markdown files generated from app connections, MCP/tool calls, documents, meetings, todos, messages, prior deliverables, and external research. Any agent harness can use this workflow if it can pull relevant context from apps and write normalized markdown files into a filesystem.

The artifact is not the goal. The goal is to change what a specific stakeholder believes, understands, approves, buys, signs, funds, or does next.

## Core philosophy

Business work is less deterministic than software, so manufacture determinism through:

- a filesystem context base the agent can inspect like a repo
- explicit known facts, assumptions, constraints, and unknowns
- required research-adversary context before spec
- acceptance criteria before artifact creation
- claim/evidence audits
- role-based adversarial reviewers
- anti-sycophancy review as the final PR-style gate
- human review gates when stakes require it

Never jump straight from vague request to polished draft unless the task is trivial. For meaningful deliverables, run the gates.

## When to use

Use for decks, memos, calculators, customer-facing docs, pricing pages, proposals, enterprise implementation plans, compliance/insurance/legal-facing answer sets, investor materials, advisor/customer outreach, and executive summaries for internal or external stakeholders.

Skip the full workflow only for exact copy/paste work, trivial wording edits, or low-stakes internal notes.

## Workflow overview

1. **Build the business context base** - create the filesystem “business repo” from internal app context plus external research-adversary context.
2. **Business discussion** - probe the human and clarify the actual business goal.
3. **Business spec** - create the deliverable brief and acceptance criteria.
4. **Business spec review** - attack the spec before drafting.
5. **Business artifact** - draft the artifact against the approved spec.
6. **Business artifact review** - run self-review, fresh-context review, claim audit, adversarial reviewers, and anti-sycophancy review.
7. **Human gate** - route to domain/legal/sales/security review when stakes require it.
8. **Release checklist** - final send/readiness pass.

If any gate fails, go back to the prior stage. Do not line-edit a fundamentally wrong artifact.

---

# Stage 1 - Build the Business Context Base

Equivalent to opening a software repo and inspecting the codebase before planning.

Business work does not have a default repo. Build one by pulling relevant context from connected apps, MCP servers, tool calls, files, and external research, then writing the normalized output into markdown files the agent can inspect.

## 1A. Internal context pass

Pull internal business truth from available systems into markdown files.

Sources may include:

- originating conversation, transcript, capture, ticket, or standup notes
- docs/files and prior deliverables
- todos/tickets/issues
- email and chat threads
- CRM/customer records
- spreadsheets and analytics
- product docs, contracts, security/compliance docs
- customer calls and meeting notes
- relevant memory or prior decisions

Suggested filesystem structure:

```md
/business-context/
  00-task.md
  01-internal-context.md
  02-external-research-adversary.md
  03-known-facts.md
  04-assumptions-and-unknowns.md
  05-stakeholders-and-objections.md
  06-constraints.md
  07-examples-and-prior-art.md
  08-context-summary.md
```

The exact file names can vary. The requirement is that the context is normalized into inspectable markdown files rather than trapped in scattered apps or chat history.

## 1B. Research-adversary context pass

This is required for serious business work, not an optional polish step.

Research-adversary is the business equivalent of inspecting dependencies, docs, prior art, open issues, and edge cases in software. It captures external stakeholder reality before spec, especially strong opinions that would not appear in internal context.

Look for:

- what stakeholders, buyers, users, competitors, communities, and skeptics actually say
- niche objections and buyer anxieties
- category language and phrases real people use
- competitor praise, complaints, positioning, and pricing reactions
- recent market discourse and timing-sensitive context
- expert disagreement and contrarian takes
- what would make the artifact sound naive to someone deep in the space
- what a smart skeptic would say in one sentence

Use recent-discourse research for fast-moving markets. Use authoritative-source research for legal, compliance, payroll, tax, insurance, HR, security, or regulated work.

## Business Context Pack output

After internal context and research-adversary, produce:

```md
# Business Context Pack

## Origin
Where this came from.

## Real Business Goal
The actual stakeholder decision or behavior this work should cause.

## Audience / Stakeholders
Primary reader, approvers, blockers, influencers.

## Current Reader State
What they likely believe or understand now.

## Desired Reader State
What they should believe, understand, trust, approve, buy, or do after seeing the artifact.

## Source Material
Links, docs, captures, transcripts, metrics, examples, app-exported markdown files.

## Known Facts
Grounded facts only, with source references where available.

## Assumptions
Plausible but unverified beliefs.

## Unknowns
Missing info that may block or weaken the deliverable.

## Constraints
Legal, compliance, product, technical, timeline, relationship, pricing, brand.

## Stakeholder Objections
Internal objections plus external research-adversary objections.

## Niche / External Insights
Specific recent or subcultural insights that a generic reviewer would miss.

## Stakes
What happens if this is wrong, sloppy, overclaimed, or late.
```

Rules:

- Do not invent context.
- If the context base is too thin, say what is missing.
- If the requested artifact seems wrong for the actual goal, call that out.
- Keep internal truth and external research-adversary findings distinguishable.

---

# Stage 2 - Business discussion

Equivalent to engineering discussion. No artifact drafting yet.

Use the business context base to have an implementation-focused business discussion. Probe the human until the deliverable can be specified.

Ask only high-leverage questions. Prefer making a best-effort inference and asking the human to confirm over dumping a long questionnaire.

Probe:

- what decision are we trying to cause?
- who has to be convinced?
- what do they already know?
- what are they skeptical about?
- what would make this obviously successful?
- what would make this embarrassing?
- what facts/numbers are real vs guessed?
- what are we afraid to say directly?
- what should be excluded?
- what is the smallest artifact that moves the decision?
- who needs to review before external send?

Output:

```md
# Business Discussion Output

## Confirmed Goal
## Confirmed Audience
## Confirmed Artifact
## Key Decisions Made
## Open Questions
## Risks / Watchouts
## Recommended Next Stage
Proceed to spec / build more context / get human input / change artifact type.
```

---

# Stage 3 - Business spec

Equivalent to engineering plan/spec. This is the most important stage.

Create a **Business Deliverable Spec** before drafting the artifact.

```md
# Business Deliverable Spec

## One-Sentence Job
What this deliverable must accomplish.

## Reader Transformation
Before: what the reader believes/understands now.
After: what the reader should believe/understand/do next.

## Artifact Type / Format / Channel
Deck, memo, proposal, calculator, customer doc, webpage, email, answer guide, etc.

## Audience Priority Stack
What each stakeholder cares about, in order.

## Core Thesis
The main claim the artifact needs to make.

## Narrative Arc
Problem → stakes → solution → proof → ask.

## Required Sections
For each section: section title, job, required content, evidence needed.

## Required Evidence
Numbers, quotes, docs, screenshots, call notes, examples, external benchmarks.

## Claims We Are Allowed To Make
Only grounded claims.

## Claims We Are Not Allowed To Make Yet
Tempting but unsupported or risky claims.

## Objection Handling
Likely objections and where/how the artifact handles them.

## Research-Adversary Inputs
The external opinions, objections, language, and niche insights that must shape the artifact.

## Non-Goals
What the artifact should not try to do.

## Acceptance Criteria
What must be true before an internal or external stakeholder sees it.

## Reviewer Panel
2-4 adversarial roles needed for the final review.

## Human Gate
Who must review before external send, if anyone.
```

The spec should be clear enough that a fresh agent could create the artifact without the original conversation.

---

# Stage 4 - Business spec review

Equivalent to plan-reviewer.

Review the spec before drafting. Attack:

- does the spec match the real business goal?
- is the audience specific enough?
- is the desired reader transformation clear?
- are acceptance criteria testable?
- are required sections justified?
- are required claims supported by available evidence?
- did the spec use research-adversary insights or ignore them?
- does the narrative arc fit the decision?
- are risks and objections addressed?
- is human review required before continuing?

Output:

```md
# Business Spec Review

## Verdict
Approved / revise spec / build more context.

## Highest-Risk Issue
## Required Spec Changes
## Missing Evidence
## Missing Research-Adversary Context
## Reviewer Panel Changes
## Human Input Needed
```

Do not draft from a weak spec. Send it back to business discussion or context-building.

---

# Stage 5 - Business artifact

Equivalent to implementation.

Create the artifact from the approved spec, not from vibes or conversation momentum.

Rules:

- Use only grounded facts from the context base and spec.
- Maintain a claim/evidence ledger while drafting.
- Preserve the reader transformation and narrative arc.
- Make every section do a job.
- Use research-adversary findings to handle real objections and use real stakeholder language.
- Prefer concise, decision-moving content over comprehensive content.
- If the artifact type is a deck, optimize for skim-readability and spoken presentation.
- If it is a memo, optimize for executive clarity and decision logic.
- If it is a proposal, optimize for buyer confidence, scope clarity, value, risk handling, and next step.
- If it is a calculator/model, optimize for trust, assumptions, source visibility, and auditability.
- If it is compliance/legal/insurance-facing, optimize for factual precision and explicit uncertainty.

Always produce a claim/evidence ledger:

```md
# Claim / Evidence Ledger

| Claim | Evidence | Status | Risk | Fix |
|---|---|---|---|---|
| ... | source/context | supported / unsupported / risky / needs source | low/med/high | keep / soften / remove / verify |
```

---

# Stage 6 - Business artifact review

Equivalent to implementation-reviewer plus PR reviewers. Run this when the artifact seems done.

The default stance is: assume it is not done yet. Try to break it.

## 6.1 Spec compliance

Check whether the artifact satisfies the spec:

- intended outcome
- reader transformation
- narrative arc
- required sections
- required evidence
- research-adversary inputs
- non-goals
- acceptance criteria

Mark each as DONE / PARTIAL / MISSING / DEVIATED.

## 6.2 Fresh-context review

Review as if you did not participate in the conversation.

Ask:

- If I only saw this artifact, what would I think the point is?
- Would I know what decision/action is being requested?
- What would confuse me?
- What feels unsupported, salesy, vague, or overconfident?
- What would I challenge in a meeting?
- What is the strongest version of this artifact, ignoring the current structure?

## 6.3 Claim/evidence audit

Audit every meaningful claim:

- supported by source
- plausible but unsupported
- contradicted by source
- overclaimed
- fake-precise
- risky due to legal/compliance/security/pricing implications

Unsupported or risky claims must be sourced, softened, removed, or escalated to human review.

## 6.4 Role-based adversarial reviewer panel

Select 2-4 reviewers based on artifact type and inform them with the research-adversary context.

Default mapping:

| Artifact type | Adversarial reviewers |
|---|---|
| Enterprise proposal | skeptical buyer, economic buyer/CFO, technical buyer/CTO, implementation owner |
| Sales deck | distracted buyer, cynical sales lead, domain expert, confused first-time reader |
| Investor memo/deck | skeptical investor, market expert, traction/numbers reviewer, founder-fit reviewer |
| Pricing calculator/ROI model | skeptical prospect, competitor, spreadsheet auditor, legal/compliance risk reviewer |
| Customer-facing webpage | low-patience buyer, SEO/AEO reviewer, trust/compliance reviewer |
| Compliance/insurance/legal answers | regulator/insurer, factual accuracy reviewer, liability reviewer, missing-evidence reviewer |
| Internal strategy memo | operator, adversarial board member, execution planner |
| Partner/advisor outreach | busy recipient, credibility reviewer, relationship-risk reviewer |

For each reviewer, produce:

- objection
- question they would ask
- risk if ignored
- required fix

## 6.5 Anti-sycophancy review

This is the business PR review final gate.

Explicitly answer:

- what am I tempted to praise because the user wants it to be good?
- what did the conversation make feel obvious that will not be obvious to a fresh reader?
- what structure exists only because we iterated into it?
- what would a sharp internal reviewer immediately call out?
- what would a smart external critic say in one sentence?
- what would make this look amateur?
- what should be cut, reframed, or rebuilt?

Do not soften these points unnecessarily. The goal is fewer preventable mistakes, not encouragement.

## 6.6 Patch list

Produce concrete edits. Do not stop at critique.

Output:

```md
# Business Artifact Review

## Verdict
Not ready / close / ready.

## Highest-Risk Issue
The one thing most likely to hurt the outcome.

## Spec Compliance
DONE / PARTIAL / MISSING / DEVIATED table.

## Fresh-Context Findings
## Claim/Evidence Audit
## Adversarial Reviewer Notes
## Anti-Sycophancy Review
## Required Patches
## Human Review Needed?
Yes/no, who, and why.

## Final Release Checklist
```

---

# Stage 7 - Human gate

Human review is mandatory before external send if any are true:

- legal, tax, payroll, HR, securities, insurance, HIPAA, privacy, security, or regulatory claims are made
- pricing, contract terms, implementation scope, or ROI could materially affect revenue or liability
- the artifact goes to an enterprise stakeholder, investor, attorney, insurer, regulator, or major customer
- the artifact includes technical/security commitments, integration commitments, or compliance statements
- neither the author nor the primary reviewer has strong prior experience with the artifact type
- the AI had to rely on assumptions or unresolved unknowns

Name the specific reviewer needed: company operator, enterprise sales operator, startup CFO, attorney, compliance expert, technical/security reviewer, customer/domain expert, etc.

---

# Stage 8 - Release checklist

Before final delivery, verify:

- reader and next action are obvious
- opening makes the stakes clear
- no unsupported claims remain
- numbers, names, dates, pricing, and commitments are consistent
- research-adversary objections were either addressed or intentionally excluded
- all links, screenshots, tables, labels, and formatting work
- artifact is appropriately concise
- risks are named instead of hidden
- the ask is specific
- required human review has happened or is explicitly queued

If any item fails, do not call it done.

---

# Quick commands / modes

## build-business-context-base
Pull relevant internal app context and external research-adversary context into markdown files. Do not draft.

## research-adversary-context-pass
Capture external stakeholder opinions, niche objections, category language, competitor praise/complaints, recent discourse, and expert disagreement. Feed this into the context base.

## business-discussion
Probe the human and clarify the actual business goal. Do not draft.

## business-spec
Create the deliverable spec and acceptance criteria.

## business-spec-review
Review the spec before artifact creation.

## business-artifact
Create the artifact from the approved spec.

## business-artifact-review
Run the PR-style review, including adversarial reviewers and anti-sycophancy.

## business-fast-pass
For smaller deliverables only: context base → mini-spec → artifact → artifact-review in one pass. Still include research-adversary, claim/evidence audit, and anti-sycophancy if external-facing.

---

# Default response discipline

Be direct. Prefer “not ready because X” over polite ambiguity. If the artifact is built on the wrong goal, say so. If the spec is weak, reject the spec. If the work needs human review, say who and why.

The best outcome is not a nicer draft. The best outcome is a business deliverable that survives the operator, the buyer, the reviewer, and reality.
