# Engineering Planning & Communication Artifact Formats — Research Summary

## Context & Framing

These findings target a specific pipeline: a top-tier **orchestrator model** (Claude Fable/Mythos 5 class) authors planning/communication artifacts, and a **strong implementer model** (GPT-5.5 via `codex exec`) implements from them. The central design constraint from the user: with frontier implementer models, artifacts no longer need to be extremely granular. The document must carry **all key decisions, constraints, and context** needed to implement correctly — but should **not** spell out every code-level step. Decisions yes; line-level pseudocode no.

Every established human-authored format below was designed under a related assumption: the reader is a competent engineer who needs the *why* and the *what*, not a keystroke transcript. That makes these conventions unusually well-suited to frontier-model consumers. This document distills the best-regarded formats for each artifact type, then reconciles them into templates calibrated for the orchestrator→implementer workflow.

---

## Executive Summary

- **Two-tier planning is the dominant modern pattern.** A high-level **spec/design doc** captures the stable *what & why* + key architecture decisions + phase breakdown; a per-phase **implementation plan** captures the flexible *how* — files touched, ordered tasks, verification. This split appears in Google design docs, GitHub spec-kit, and Amazon Kiro alike ([spec-kit blog](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/); [Kiro specs](https://kiro.dev/docs/specs/)).
- **Decision-density beats step-density.** Google's own guidance says a design doc should document "trade-offs and key design decisions," and explicitly warns against letting it become an "implementation manual" ([Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/)). This is exactly the right altitude for a frontier implementer.
- **Structured issue forms** (GitHub issue forms, YAML) reliably out-perform free-text because they force the reporter to supply the fields an implementer actually needs ([GitHub Docs: issue forms](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms)).
- **Bug reports converge on a fixed skeleton:** title, environment, numbered repro from a known state, expected vs. actual, evidence, severity ([QA Wolf](https://www.qawolf.com/blog/what-makes-a-great-bug-report); [BrowserStack](https://www.browserstack.com/guide/how-to-write-a-bug-report)).
- **PR reviews are most useful when severity-tagged.** Conventional Comments gives a machine- and human-parseable `label [decorations]: subject` grammar that separates blocking issues from nitpicks ([Conventional Comments](https://conventionalcomments.org/)); Google's code-review standard defines *what* to look for and the bar for approval ([eng-practices](https://google.github.io/eng-practices/review/reviewer/standard.html)).

---

## Key Findings by Artifact Type

### 1. GitHub Issues — Bug Reports & Feature Tickets

**Issue forms (YAML) are the current best practice.** GitHub issue forms are YAML files in `.github/ISSUE_TEMPLATE/` that render as web forms with required fields, dropdowns, checkboxes, and per-field validation, so you "ask only for the information that a specific type of issue actually needs" ([GitHub Docs: syntax for issue forms](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms)). A `config.yml` presents a chooser across multiple templates and can disable blank issues to force structure ([GitHub Docs: configuring issue templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository)). Templates can pre-apply labels, assignees, and projects.

**Bug report skeleton** (converged across QA sources):
1. **Descriptive title** — one line, specific.
2. **Summary** — what's broken, in one or two sentences.
3. **Environment** — OS, browser/runtime, app/build version, region. "Many bugs are environment-specific" ([BrowserStack](https://www.browserstack.com/guide/how-to-write-a-bug-report)).
4. **Steps to reproduce** — numbered, starting from a **known state**, exact inputs/values ([QA Wolf](https://www.qawolf.com/blog/what-makes-a-great-bug-report)). Avoid vague actions like "go to the page and check."
5. **Expected vs. actual result** — expected = what a correct system does; actual = observed behavior described as *observation, not assumed cause*.
6. **Evidence** — logs, screenshots, session recordings.
7. **Severity/priority + impact** — who/what is affected, how widely.

Reporting guidance stresses **objectivity** (facts not opinions), **completeness but concision** ("do not waste engineer time reconstructing missing details"), and **timeliness** (write immediately, before repro steps are forgotten) ([QAwerk](https://qawerk.com/blog/how-to-write-a-good-bug-report-best-practices/)).

**Feature/enhancement ticket skeleton:** move from "I want a thing" to "here is the problem this solves" — description, **use cases / motivation**, proposed solution, alternatives, references/acceptance criteria ([DevToolHub](https://devtoolhub.com/github-templates-pull-requests-issues-discussions/); [GitHub issue-templates collection](https://github.com/stevemao/github-issue-templates)).

### 2. Architecture / High-Level Plan Documents

**Google Design Doc** — the reference format ([Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/)):
- **Context and Scope** — background/landscape, succinct, objective. *Not* a requirements doc.
- **Goals and Non-Goals** — non-goals are reasonable possibilities *explicitly rejected*, not mere negations.
- **The Actual Design** — overview first, then detail; centered on **trade-offs** and why the chosen solution best satisfies the goals.
- **System-context diagram, APIs, Data storage** — sketch design-relevant parts; do **not** paste full schemas/IDL. "Focus on the parts relevant to the design and its trade-offs."
- **Alternatives Considered** — viable alternatives + why rejected.
- **Cross-cutting concerns** — security, privacy, observability.
- *Length:* 1–3 pages (mini) to 10–20 pages (large). *Rule #1:* write it in whatever form fits the project. Skip it entirely when the solution is obvious or when it would become an "implementation manual."

**ADR (Architecture Decision Record)** — one *decision* per record, ideally one page ([adr.github.io](https://adr.github.io/); [Joel Parker Henderson's ADR repo](https://github.com/architecture-decision-record/architecture-decision-record)). Follows inverted-pyramid: decision + rationale first, detail later. Classic sections (Nygard/MADR): **Title, Status** (proposed/accepted/superseded), **Context, Decision, Consequences**. If a decision needs more than a page, link out to a design doc and keep the ADR summary-form.

**RFC / RFD** — a *proposal under discussion*. An RFC is debated and may be withdrawn; an ADR is the *frozen record after* discussion closes ([Candost](https://candost.blog/adrs-rfcs-differences-when-which/); [Bruno Scheufler](https://brunoscheufler.com/blog/2020-07-04-documenting-design-decisions-using-rfcs-and-adrs)). Oxide **RFDs** add a **state machine** in metadata — prediscussion, ideation, discussion, published, committed, abandoned — and deliberately encourage "timely rather than polished" drafts, even questions without answers ([Oxide RFD 1](https://rfd.shared.oxide.computer/rfd/0001)). Rust RFCs use a fixed template: *Summary, Motivation, Guide-level explanation, Reference-level explanation, Drawbacks, Rationale and alternatives, Prior art, Unresolved questions, Future possibilities.*

**When to use which:** ADR = record one closed decision (cheap, one page). RFC/RFD = deliberate an open proposal. Design doc = the full picture for a system/feature before coding. For the orchestrator→implementer pipeline, the **design doc** structure maps directly onto our "spec."

### 3. Spec vs. Implementation Plan — The Core Distinction

Modern spec-driven-development (SDD) toolkits formalize the two-tier split:

**GitHub spec-kit** runs four gated phases ([GitHub blog](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/); [spec-kit repo](https://github.com/github/spec-kit)):
1. **Specify** — goals and user journeys → detailed spec.
2. **Plan** — architecture, stack, constraints → technical plan respecting org patterns.
3. **Tasks** — break into small, reviewable, independently-testable units.
4. **Implement** — agent executes, human verifies at each checkpoint.
> "The spec captures the stable *what*, while the plan and tasks drive the flexible *how*, reducing rework and making changes predictable."

**Amazon Kiro** uses three files ([Kiro specs docs](https://kiro.dev/docs/specs/); [Kiro intro](https://kiro.dev/blog/introducing-kiro/)):
- `requirements.md` — user stories + acceptance criteria in **EARS** format.
- `design.md` — architecture, components, data models, interfaces, sequence diagrams, error handling, testing strategy.
- `tasks.md` — discrete, sequenced, dependency-linked implementation tasks, each traceable back to a requirement.

**EARS (Easy Approach to Requirements Syntax)** — five patterns for unambiguous acceptance criteria ([EARS overview](https://dev.to/sebastian_dingler/ears-the-easy-approach-to-requirements-syntax-39a5)):
- Ubiquitous: `The <system> shall <response>`
- Event-driven: `WHEN <trigger> the <system> shall <response>`
- Unwanted behavior: `IF <condition>, THEN the <system> shall <response>`
- State-driven: `WHILE <state>, the <system> shall <response>`
- Optional: `WHERE <feature included>, the <system> shall <response>`

EARS is valuable in our pipeline because it converts fuzzy acceptance criteria into testable trigger→action statements the implementer can verify against.

#### Spec vs. Implementation Plan — Comparison Table

| Dimension | **Spec / Overview** (the *what & why*) | **Implementation Plan** (the *how*, per phase) |
|---|---|---|
| Answers | Why build it, what "done" means, which architecture we chose | How to build one phase, in what order |
| Stability | Stable — changes rarely | Volatile — one per phase, revised as we learn |
| Scope | Whole feature/system | A single phase of the spec |
| Key content | Problem, goals/non-goals, **key decisions + rationale**, phases table, open questions | Context recap, decisions restated, ordered tasks at **file/module** granularity, verification steps, out-of-scope |
| Granularity | High-level, decision-dense, **no code** | Concrete tasks + acceptance checks, **not line-level code** |
| Audience action | Align, approve architecture | Execute the phase |
| Analogues | Google design doc, Kiro `design.md`, spec-kit *Specify*+*Plan* | Kiro `tasks.md`, spec-kit *Tasks* |
| Lifespan | Lives for the life of the feature | Consumed and closed per phase |

The **spec** is written once and checked off phase by phase; each **plan** is spawned from one phase, drives the implementer, and is discarded. This is exactly the stateful split spec-kit and Kiro converge on.

### 4. PR Review Formats

**Conventional Comments** — a grammar for review feedback ([conventionalcomments.org](https://conventionalcomments.org/)):
```
<label> [decorations]: <subject>

[discussion]
```
Labels: **praise, nitpick, suggestion, issue, todo, question, thought, chore, note** (plus typo/polish/quibble). Decorations: **(non-blocking)**, **(blocking)**, **(if-minor)**. Example:
```
suggestion (security, non-blocking): validate the signature before parsing the body.
Parsing untrusted JSON first widens the attack surface.
```
The value is separating *blocking* from *nitpick* so the author knows what actually gates merge, and making comments parseable by tooling.

**Google's code-review standard** ([eng-practices standard](https://google.github.io/eng-practices/review/reviewer/standard.html); [what to look for](https://google.github.io/eng-practices/review/reviewer/looking-for.html)):
- The bar: **approve once the change definitely improves overall code health**, even if imperfect — don't hold out for perfection.
- Look for: sound **design**, correct **functionality** for users, no **unneeded complexity** / over-engineering, adequate and well-designed **tests**, clear **naming**, updated **docs**.
- Reviewers should be "especially vigilant about over-engineering — solve the problem that needs solving now, not a speculated future one."
- Prefix nits explicitly (Google convention: mark non-blocking comments with `Nit:`), which Conventional Comments generalizes.

**AI review tool conventions** (CodeRabbit, GitHub Copilot review, Graphite): a **verdict summary** up top (approve / request changes + one-line rationale), then **severity-grouped, per-`file:line` findings**, often with a suggested diff and a concrete **failure scenario** for correctness bugs. This "verdict + severity-tagged findings + praise where earned" shape is what our PR-review artifact should adopt.

---

## Right Granularity When a Frontier Model Implements

The recurring lesson across Google, spec-kit, and Kiro is that good planning docs are **decision-dense, not step-dense** — and frontier implementers amplify this. Guidance for our pipeline:

**Always include (the load-bearing content):**
- **Key decisions with rationale** — the choices that are expensive to reverse or non-obvious (storage engine, retry semantics, idempotency strategy, sync vs. async). This is the single most important payload.
- **Constraints & invariants** — must-nots, SLAs, security/privacy boundaries, backward-compat requirements, ordering guarantees.
- **Interfaces & contracts** — the shapes at module boundaries (API signatures, event schemas) *sketched*, not exhaustively specified.
- **Acceptance criteria** — testable, ideally EARS-style, so the implementer can self-verify.
- **File/module-level task ordering** — *which* modules to touch and in what sequence, so work is coherent — not the diff.
- **Out-of-scope / non-goals** — bounds the implementer and prevents gold-plating (Google: guard against over-engineering).

**Deliberately omit (trust the implementer):**
- Line-by-line pseudocode or full code blocks (Google: include code "rarely... except novel algorithms").
- Exhaustive schema/IDL dumps — sketch the design-relevant fields, link the rest.
- Obvious boilerplate, standard error handling, idiomatic patterns the implementer already knows.
- Micro-decisions with no downstream consequence (variable names, local structure).

**The test:** if a detail is *load-bearing* (getting it wrong breaks the design or violates a constraint), it belongs in the doc. If it's a local implementation choice the implementer can make correctly on its own, leave it out. Spell out **decisions and boundaries**; delegate **mechanics**.

---

## Implementation Recommendations (for the artifact templates)

1. **Adopt the two-tier split explicitly:** a stateful **spec** with a phases table, and one **implementation plan** per phase. Mirror spec-kit/Kiro.
2. **Spec = Google-design-doc altitude:** problem, goals/non-goals, key decisions + rationale, phases, open questions. No code.
3. **Plan = Kiro `tasks.md` altitude:** context recap, decisions restated, ordered file/module tasks, verification/acceptance, out-of-scope. No line-level code.
4. **Bug tickets:** fixed skeleton (summary, expected/actual, numbered repro from known state, environment, evidence, suspected area, severity/impact).
5. **Feature tickets vs. plans:** keep a *lightweight delegation ticket* (intent, scope, acceptance, non-goals, starting-file pointers, open questions) distinct from the full plan. The ticket says *what & why + where to start*; the plan says *how, in order*.
6. **PR reviews:** verdict summary + severity-tagged (blocking/important/nit or Conventional Comments) per-`file:line` findings + failure scenarios for bugs + genuine praise.
7. **Use EARS for acceptance criteria** wherever ambiguity is costly.

---

## Potential Issues & Mitigations

- **Under-specification risk:** trusting the implementer too much can drop a load-bearing constraint. *Mitigation:* a mandatory "Key Decisions" and "Constraints/Invariants" section in every spec/plan; treat these as non-negotiable.
- **Over-specification risk:** line-level plans waste orchestrator tokens and constrain a capable implementer into worse local choices. *Mitigation:* the load-bearing test above; cap plans at file/module granularity.
- **Stale plans:** plans are volatile; a spec phase may drift. *Mitigation:* keep the spec as source of truth, regenerate plans per phase, check phases off.
- **Ambiguous acceptance:** "works correctly" is untestable. *Mitigation:* EARS-style criteria.
- **Review noise:** unranked comments bury blockers. *Mitigation:* Conventional Comments decorations; lead with a verdict.

---

## Templates

### Spec / Overview
```
# <Feature> — Spec
## Problem / Context
## Goals
## Non-Goals
## Key Architecture Decisions   (each: decision + rationale + alternatives rejected)
## Phases   (table: phase | scope | status)
## Cross-Cutting Concerns   (security, observability, migration)
## Open Questions
```

### Implementation Plan (one phase)
```
# <Feature> — Phase N Implementation Plan
## Context Summary   (recap from spec; what exists now)
## Key Decisions (restated for this phase)
## Tasks   (ordered, file/module granularity — what & why, not code)
## Verification / Acceptance   (EARS-style, how to prove it works)
## Out of Scope
```

### Bug Ticket
```
# <Title>
## Summary
## Expected vs. Actual
## Steps to Reproduce   (numbered, from known state)
## Environment
## Evidence   (logs, screenshots)
## Suspected Area
## Severity & Impact
```

### Feature / Delegation Ticket
```
# <Title>
## Intent   (why + what)
## Scope
## Acceptance Criteria
## Non-Goals
## Starting Points   (pointers to files/modules — non-exhaustive)
## Open Questions
```

### GitHub Issue Form (YAML skeleton)
```yaml
name: Bug Report
description: Report a defect
labels: ["bug", "triage"]
body:
  - type: textarea   # summary (required)
  - type: textarea   # steps to reproduce (required)
  - type: textarea   # expected vs actual (required)
  - type: input      # environment / version (required)
  - type: dropdown   # severity
  - type: textarea   # logs / evidence
```

### PR Review
```
## Verdict: <Approve | Request changes> — <one-line rationale>
## Blocking
- issue (blocking): <file:line> — <problem> + failure scenario
## Important
- suggestion: <file:line> — <improvement + reasoning>
## Nits
- nitpick (non-blocking): <file:line>
## Praise
- praise: <file:line> — <what was done well>
```

---

## Additional Resources

- [Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/)
- [Google eng-practices: code review](https://google.github.io/eng-practices/review/)
- [GitHub spec-kit](https://github.com/github/spec-kit) · [SDD blog post](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/)
- [Kiro specs docs](https://kiro.dev/docs/specs/)
- [Conventional Comments](https://conventionalcomments.org/)
- [adr.github.io](https://adr.github.io/) · [Joel Parker Henderson ADR repo](https://github.com/architecture-decision-record/architecture-decision-record)
- [Oxide RFD 1](https://rfd.shared.oxide.computer/rfd/0001)
- [GitHub Docs: issue forms syntax](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms)
- [EARS syntax](https://dev.to/sebastian_dingler/ears-the-easy-approach-to-requirements-syntax-39a5)
- Bug reports: [QA Wolf](https://www.qawolf.com/blog/what-makes-a-great-bug-report), [BrowserStack](https://www.browserstack.com/guide/how-to-write-a-bug-report), [QAwerk](https://qawerk.com/blog/how-to-write-a-good-bug-report-best-practices/)

## Gaps or Limitations

- Kiro's public docs don't fully expose the internal `requirements.md`/`tasks.md` section hierarchy or the exact requirement↔task traceability format; structure above is reconstructed from docs + secondary reviews.
- Anthropic's plan-then-implement guidance is reflected indirectly via SDD toolkit conventions rather than a single canonical spec; the two-tier pattern is corroborated across Google, GitHub, and Amazon independently.
- Conventional Comments labels are a de facto standard, not a formal RFC; teams extend the label set freely.

## Version Information

- Research conducted July 2026. GitHub spec-kit and Amazon Kiro are both active in 2025–2026 (spec-kit supports ~29 agent integrations including Codex CLI and Claude Code). Google design-doc and eng-practices guidance are stable/evergreen. Conventional Comments spec is stable at conventionalcomments.org. EARS dates to Mavin et al., RE'09.
