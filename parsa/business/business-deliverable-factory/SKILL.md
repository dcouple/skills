---
name: business-deliverable-factory
description: Convert nontrivial business work from conversation into a context pack, spec, reviewed artifact, and final release gate. Use for decks, memos, proposals, calculators, customer-facing docs, compliance answers, and other stakeholder-facing deliverables.
---

# Business Deliverable Factory

Use this skill for nontrivial business work where a conversation, sprint kickoff, standup, customer call, or rough task needs to become a high-quality business deliverable. This is the business equivalent of the engineering factory: conversation → ticket/context → discussion → spec → spec review → artifact → artifact review → human gate.

This skill is not only a polish checklist. The anti-sycophancy review is the final PR-review stage. The full workflow starts much earlier by turning ambiguous business intent into a reviewable business work ticket, context pack, and deliverable spec before drafting.

## Core philosophy

Software work has a repo, tests, typecheck, lint, implementation reviewers, and PR reviewers. Business work is less deterministic, so we manufacture determinism through structured context, explicit acceptance criteria, claim/evidence audits, adversarial reviewers, and human review gates.

The artifact is not the goal. The goal is to change what a specific stakeholder believes, understands, approves, buys, signs, funds, or does next.

Never jump straight from vague request to polished draft unless the task is trivial. For meaningful deliverables, run the gates.

## When to use

Use for decks, memos, calculators, customer-facing docs, pricing pages, proposals, enterprise implementation plans, compliance/insurance/legal-facing answer sets, investor materials, advisor/customer outreach, and executive summaries for internal or external stakeholders.

Skip the full workflow only for exact copy/paste work, trivial wording edits, or low-stakes internal notes.

## Workflow overview

1. **Business investigate** - assemble the business context pack.
2. **Business discussion** - probe the human and clarify the actual business goal.
3. **Business spec** - create the deliverable brief and acceptance criteria.
4. **Business spec review** - attack the spec before drafting.
5. **Business artifact** - draft the artifact against the approved spec.
6. **Business artifact review** - run self-review, fresh-context review, claim audit, adversarial reviewers, and anti-sycophancy review.
7. **Human gate** - route to domain/legal/sales/security review when stakes require it.
8. **Release checklist** - final send/readiness pass.

If any gate fails, go back to the prior stage. Do not line-edit a fundamentally wrong artifact.

---

# Stage 1 - Business investigate

Equivalent to engineering investigate plus repo orientation.

Business work does not have a default repo. Build one as a **business context pack**.

Gather and organize:

- originating conversation, transcript, capture, ticket, or standup notes
- artifact requested and suspected real goal
- audience and stakeholders
- intended decision, belief change, purchase, approval, signature, funding, or next step
- source docs, customer calls, pricing data, contracts, compliance docs, prior deliverables, examples, screenshots, metrics, and relevant captures
- known facts with evidence
- assumptions and unknowns
- constraints: legal, compliance, product, technical, brand, pricing, timeline, relationship, operational
- likely objections or blockers
- quality bar and deadline
- human reviewers likely needed

Output a **Business Context Pack**:

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
Links, docs, captures, transcripts, metrics, examples.

## Known Facts
Grounded facts only, with source references where available.

## Assumptions
Plausible but unverified beliefs.

## Unknowns
Missing info that may block or weaken the deliverable.

## Constraints
Legal, compliance, product, technical, timeline, relationship, pricing, brand.

## Likely Objections
What a smart reader would push back on.

## Stakes
What happens if this is wrong, sloppy, overclaimed, or late.
```

Rules:

- Do not invent context.
- If the context pack is too thin, say what is missing.
- If the requested artifact seems wrong for the actual goal, call that out.

---

# Stage 2 - Business discussion

Equivalent to engineering discussion. No artifact drafting yet.

Use the context pack to have an implementation-focused business discussion. Probe the human until the deliverable can be specified.

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
Proceed to spec / investigate more / get human input / change artifact type.
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
- does the narrative arc fit the decision?
- are risks and objections addressed?
- is human review required before continuing?

Output:

```md
# Business Spec Review

## Verdict
Approved / revise spec / investigate more.

## Highest-Risk Issue
## Required Spec Changes
## Missing Evidence
## Reviewer Panel Changes
## Human Input Needed
```

Do not draft from a weak spec. Send it back to business discussion or investigate.

---

# Stage 5 - Business artifact

Equivalent to implementation.

Create the artifact from the approved spec, not from vibes or conversation momentum.

Rules:

- Use only grounded facts from the context pack and spec.
- Maintain a claim/evidence ledger while drafting.
- Preserve the reader transformation and narrative arc.
- Make every section do a job.
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

Select 2-4 reviewers based on artifact type.

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
- all links, screenshots, tables, labels, and formatting work
- artifact is appropriately concise
- risks are named instead of hidden
- the ask is specific
- required human review has happened or is explicitly queued

If any item fails, do not call it done.

---

# Quick commands / modes

## business-investigate
Build the context pack only. Do not draft.

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
For smaller deliverables only: context → mini-spec → artifact → artifact-review in one pass. Still include claim/evidence audit and anti-sycophancy if external-facing.

---

# Default response discipline

Be direct. Prefer “not ready because X” over polite ambiguity. If the artifact is built on the wrong goal, say so. If the spec is weak, reject the spec. If the work needs human review, say who and why.

The best outcome is not a nicer draft. The best outcome is a business deliverable that survives the operator, the buyer, the reviewer, and reality.
