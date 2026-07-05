# Skill Library Comparison — Five Reference Corpora

Comparative analysis of the five skill libraries copied into `tmp/reference/`:
obra/superpowers, anthropics/skills, mattpocock/skills, ComposioHQ/awesome-claude-skills,
and alirezarezvani/claude-skills.

## Core similarities (what they all share)

1. **The SKILL.md + progressive-disclosure pattern is universal.** Every library uses a
   folder-per-skill with a `SKILL.md` at its root, and every one leans on the same
   three-tier loading model: lightweight `name`+`description` metadata always in context →
   the body loaded on trigger → heavier `scripts/`, `references/`, `assets/` pulled in only
   when needed. This is now a de facto standard (the [agentskills.io](https://agentskills.io)
   spec), and even the aggregator repos inherit it.

2. **Minimal frontmatter, `description` as the load-bearing field.** All five treat the
   `description` string as the highest-leverage surface — it's the trigger mechanism — and
   keep required frontmatter tiny (`name` + `description`, sometimes `license`).
   Descriptions are consistently written as "Use when…" and deliberately keyword-stuffed to
   fire reliably, because models tend to *under*-trigger.

3. **Imperative voice + progressive disclosure of code.** All prefer imperative
   instructions and the "black-box script" convention — deterministic executables meant to
   be *run*, not read into context — to keep token cost down.

4. **Composition into workflows, not just isolated commands.** The serious ones
   (Superpowers, mattpocock, alirezarezvani) chain skills into pipelines with
   router/orchestrator skills, and ship a meta-skill for *authoring skills*
   (skill-creator / writing-skills / writing-great-skills).

5. **Multi-harness ambitions.** Nearly all now publish plugin manifests for several agents
   (Claude Code, Codex, Gemini, Cursor…), treating skills as portable across harnesses.

## Core differences

The sharpest axis is **authored corpus vs. aggregation**, and orthogonally **how much they
trust the model**.

| Dimension | obra/superpowers | anthropics/skills | mattpocock/skills | ComposioHQ | alirezarezvani |
|---|---|---|---|---|---|
| **What it is** | Opinionated dev *methodology* | Official *reference exemplars* | Personal engineering *doctrine* | *Aggregation* (Anthropic core + 832 auto-gen) | Sprawling *multi-domain marketplace* |
| **Scale** | 14 deep skills | 17 curated | ~20 promoted | 864 (96% generated) | ~350 (× sync copies = 772 files) |
| **Trust in model** | Lowest — hard gates, "Iron Laws" | Highest — "explain the why, avoid MUSTs" | Judgment yes, process no | N/A (generated boilerplate) | Low — tight rails, mandated output formats |
| **Granularity** | Very prescriptive, 300–700 lines | Medium; flexes by domain | Bimodal (thin routers / dense concepts) | Uniform 90-line template | Prescriptive, 150–460 lines |
| **Signature idea** | Persuasion-engineered, eval-tested "behavior code" | Progressive disclosure + description-optimization loop | "Leading words" + composable flow, anti-framework | Runtime tool discovery via Rube MCP | "Virtual company" (C-suite advisors) + deterministic Python CLIs |
| **Domain** | SW-dev process only | Broad exemplars (docs, design, code) | SW-engineering fundamentals | 800+ SaaS integrations | Engineering → business → compliance → exec |

**The most important philosophical split is on model trust.** Anthropic's official guidance
is explicitly *anti-MUST*: "explain the why… today's LLMs are smart… if you're writing
ALWAYS/NEVER in all caps, that's a yellow flag." Superpowers deliberately does the
**opposite** — it engineers skills using persuasion psychology, anticipates the model's
rationalizations and pre-refutes them in tables, and enforces hard gates ("write code before
the test? Delete it."). It openly acknowledges diverging from Anthropic's guidance and
defends it with an LLM-judge eval harness. mattpocock and alirezarezvani sit in between:
trust *judgment*, constrain *process*.

**The second split is authored depth vs. breadth-by-generation.**
Superpowers/mattpocock/Anthropic are hand-crafted, coherent, and small. ComposioHQ and
alirezarezvani chase scale — ComposioHQ by machine-generating one near-identical skill per
SaaS app (inflating count more than capability), alirezarezvani by spanning 18 domains and
duplicating skills into per-agent sync trees. Both show "count inconsistency" (README
numbers don't match file counts) that signals SEO/star optimization.

## Strengths & weaknesses per library

**obra/superpowers** — *Strength:* the only library that treats skills as empirically-tuned
behavior, adversarially tested against pressure scenarios; the Rationalizations/Red-Flags
pattern genuinely defeats the "model talks itself out of process" failure mode; excellent
auto-triggering via a session-start bootstrap. *Weakness:* heavy-handed and token-hungry
(300–700-line skills with ALL-CAPS Iron Laws), dogmatic (assumes greenfield, TDD-friendly
work), narrow (dev-process only), and dependent on harness plumbing to work at all.

**anthropics/skills** — *Strength:* the cleanest authoring philosophy (humane,
explain-the-why), rigorous progressive disclosure, the only one shipping an eval +
description-optimization loop, and production-proven document skills. *Weakness:* it's a
curated *showcase* (17 skills), not a catalog; no enforced schema/metadata/permissions;
implicit environment dependencies (pandoc, playwright, LibreOffice) with no manifest; mixed
licensing on the best examples.

**mattpocock/skills** — *Strength:* the deepest *theory* of skill-writing (context vs.
cognitive load, "leading words," completion criteria), grounded in real engineering canon
(Ousterhout, DDD, Beck), terse high-signal prose, strong governance, model-agnostic.
*Weakness:* high buy-in (the engineering flow assumes issue-tracker/CONTEXT.md/ADR setup),
personal/branded (`ask-matt`, newsletter funnel), abstract vocabulary that may over-tax
weaker models, little turnkey tooling breadth.

**ComposioHQ/awesome-claude-skills** — *Strength:* unmatched integration breadth (800+
apps), consistent template, and a runtime-discovery design that won't rot; the curated head
re-hosts genuinely high-quality Anthropic skills. *Weakness:* 96% is shallow auto-generated
boilerplate that just re-points to `RUBE_SEARCH_TOOLS`; hard vendor lock-in to Composio's
Rube MCP; two incompatible frontmatter dialects under one roof; inflated/contradictory
counts.

**alirezarezvani/claude-skills** — *Strength:* the widest domain span (engineering →
finance → compliance → C-suite), 567 dependency-free deterministic Python CLIs ("algorithm
over AI") for reproducible outputs, clean packaging, genuine cross-agent portability via a
shared standard. *Weakness:* breadth-over-depth credibility risk (a scoring script standing
in for the expert it roleplays), verbose SKILL.md files that fight context-efficiency,
format/nesting drift, "13 tools" compatibility that's really file duplication, and
marketing-heavy inconsistent counts — a heavy solo-maintained surface.

## Net takeaway

The two most useful reference points for *how to write skills* are **anthropics/skills**
(the humane, eval-driven, trust-the-model baseline — closest to the "frontier implementer
needs decisions, not line-level steps" framing) and **obra/superpowers** (the opposite
pole — when you need to *guarantee* a process against a model that would otherwise cut
corners). mattpocock is the best-articulated *theory* to borrow vocabulary from. The two
large aggregations are better as breadth catalogs than as models of craft.

All five repos are on disk under `tmp/reference/` for direct inspection.
