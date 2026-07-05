# Model Routing: Claude Fable 5 vs Lower Tiers (+ GPT-5.5/Codex) — Research Summary

**Date:** 2026-07-05
**Scope:** When to route work to Claude Fable 5 (Mythos-class, Claude 5 family) vs Opus 4.8 / Sonnet 5 / Haiku 4.5, and where GPT-5.5 via `codex exec` fits as an implementer in a Fable-orchestrated workflow.

**Source-confidence legend used throughout:**
- **[SOURCED]** — from Anthropic official docs/announcement or the `claude-api` skill (authoritative, cached 2026-06-24).
- **[COMMUNITY]** — third-party practitioner writeups; directionally useful, benchmark numbers unverified against Anthropic.
- **[INFERENCE]** — my reasoning/opinion applied to your specific setup. Fable is new (GA 2026-06-09), so third-party coverage is thin and some is likely SEO-generated; treat community benchmark numbers as indicative, not exact.

---

## Executive Summary

Claude Fable 5 is Anthropic's most capable widely-released model, priced at **2× Opus 4.8** ($10/$50 vs $5/$25 per MTok) and positioned specifically for **long-horizon, autonomous, hard-to-specify agentic work** — not as a general Opus replacement. Anthropic's own "choosing a model" guidance says to **default to Opus 4.8** and reach for Fable only "for workloads that need the highest available capability" [SOURCED].

The right mental model for routing is **cost-per-successful-result, not cost-per-token**. Fable's per-step accuracy edge compounds across a long autonomous job — fewer dead ends, retries, and human rescues — which is exactly where 2× per-token cost pays for itself. On short, well-specified, mechanical, or high-throughput work, that edge doesn't compound and Fable is wasted spend [COMMUNITY + INFERENCE].

For your setup: **keep Fable as the orchestrator/judge/planner, push well-specified implementation down to GPT-5.5 via Codex, and push research fan-out and mechanical work down to Sonnet 5 / Haiku 4.5.** That is textbook "strong orchestrator + cheap workers," which practitioners report cuts cost 40–60% (some claim 5–10×) with minimal quality loss [COMMUNITY].

---

## What Fable 5 Is — and How It Differs From Mythos 5

**[SOURCED]** — Anthropic announcement + docs:

- **Fable 5** (`claude-fable-5`) = "a Mythos-class model that we've made safe for general use." Generally available on Claude API, Claude Platform on AWS, Bedrock, Vertex, and Foundry since **June 9, 2026**.
- **Mythos 5** (`claude-mythos-5`) = the *identical underlying model* with certain safety classifiers lifted, restricted to cybersecurity partners (Project Glasswing) and select biomedical researchers. Same specs, same pricing. **Invitation-only; no self-serve.** For your workflow, Fable 5 is the relevant model — everything below applies to both.
- **The one behavioral difference that matters for integrations:** Fable 5 runs **safety classifiers that can decline requests** (cyber, bio/chem, model-distillation domains). A decline is a *successful HTTP 200* with `stop_reason: "refusal"`, and Anthropic says these "trigger, on average, in less than 5% of sessions." Mythos 5 does not have these classifiers.

### Pricing & capability vs the lower tiers **[SOURCED]** (`claude-api` skill, cached 2026-06-24)

| Model | Input $/MTok | Output $/MTok | Context | Max out | Notes |
|---|---|---|---|---|---|
| **Claude Fable 5** | **$10.00** | **$50.00** | 1M | 128K | Thinking always on; raw CoT never returned; refusal classifiers; 30-day retention required (no ZDR) |
| Claude Opus 4.8 | $5.00 | $25.00 | 1M | 128K | Default recommendation; supports ZDR |
| Claude Sonnet 5 | $3.00 ($2 intro thru 2026-08-31) | $15.00 ($10 intro) | 1M | 128K | Near-Opus quality on coding/agentic at ~⅗ the cost |
| Claude Haiku 4.5 | $1.00 | $5.00 | 200K | 64K | Fastest; classification/extraction/simple tasks |

- Fable is **2× Opus, ~3.3× Sonnet 5 (intro), 10× Haiku** on input; **2× / ~5× / 10×** on output.
- **Key API differences on Fable [SOURCED]:** adaptive thinking is *always on* (omit the `thinking` param; `{type:"disabled"}` returns 400); control depth with `output_config.effort` (`low`→`max`, `xhigh` recommended for agentic); no assistant prefill; **30-day data retention required — ZDR orgs get a 400 on every request** (Opus 4.8 supports ZDR, a real routing constraint if you have ZDR workloads); refusals need explicit `fallbacks` handling.

### Anthropic's positioning **[SOURCED]**

- Models-overview description: *"Next-generation intelligence for long-running agents."* "Anthropic's most capable widely released model, built for the most demanding reasoning and long-horizon agentic work."
- Announcement claims: "state-of-the-art on nearly all tested benchmarks"; "exceptional performance in software engineering, knowledge work, vision, scientific research." Stripe reportedly "compressed months of engineering into days"; highest score of any model on a finance benchmark; new SOTA on vision.
- **Choosing-a-model guidance is explicit: "start with Claude Opus 4.8… For workloads that need the highest available capability, use Claude Fable 5."** Fable is the exception, not the default.

### Community benchmark color **[COMMUNITY]** (unverified against Anthropic)

Multiple third-party comparisons cite the same rough figures — treat as indicative:
- SWE-bench Pro: **Fable 5 ~80.3% vs Opus 4.8 ~69.2–69.4%** (~11-point gap).
- FrontierCode Diamond: 29.3% vs 13.4%.
- The gap is **largest on tasks requiring codebase exploration** and **shrinks on constrained/simple coding** where both models are already capable.
- One writeup: a "codebase-wide Ruby migration across 50M lines, estimated 2+ months for a full team, completed by Fable 5 in a single day."
- **Counter-signal:** on *code review*, a CodeRabbit-cited comparison shows **Opus 4.8 ahead** (actionable-review precision 35.5% vs 32.8%; full precision 26.5% vs 19.4%) — Fable's extra exploration adds noise in precision-sensitive interactive tasks. Also: Fable "produced 19 timeouts" in one test due to unbounded exploration without step limits.

---

## The Core Routing Principle

**[INFERENCE, grounded in COMMUNITY consensus]** Do not compare models on cost-per-token. Compare on **cost-per-successful-result.**

An 11-point single-step pass-rate edge looks modest. But across a long autonomous job with hundreds of steps, a higher per-step success rate **compounds**: fewer dead ends, fewer retries, fewer human rescues. If Fable resolves a long-horizon task in one pass where Opus needs two or three attempts, Fable is *cheaper per completed task* even at 2× per-token price. Conversely, on a short well-specified task both models nail on the first try, the compounding never happens and you just paid 2×.

So the routing question is really: **"Does this task have enough steps / ambiguity / cost-of-being-wrong for a per-step accuracy edge to compound?"** If yes → Fable. If no → push down.

---

## Concrete Routing Rubric: Task Type → Model Tier

**[INFERENCE synthesizing SOURCED positioning + COMMUNITY practice]**

| Task type | Recommended tier | Reasoning |
|---|---|---|
| **Orchestration & multi-step planning** (the top-level agent loop) | **Fable 5** | Decisions here steer everything downstream; a wrong routing/sequencing call cascades. Highest cost-of-being-wrong, longest horizon. This is exactly Anthropic's "long-running agents" sweet spot. |
| **Architecture / spec writing** | **Fable 5** | Cross-cutting, underspecified, expensive to get wrong; must hold the whole system in context. Fable's exploration-first behavior is an asset here. |
| **Judging & plan review** (grading another model's plan/output) | **Fable 5** | The judge must be at least as capable as what it judges — a weaker judge rubber-stamps weak work. Verification is where frontier capability earns its keep. |
| **Deep debugging / root-cause on gnarly bugs** | **Fable 5** | Ambiguous, requires holding many hypotheses, high cost of a wrong "fix." Anthropic + community both flag hard debugging as a Fable strength. |
| **PR review / code review** | **Opus 4.8** (not Fable) | Precision-sensitive and interactive; CodeRabbit data shows Opus *ahead* on review precision, and Fable's extra exploration adds noise. Lower latency also matters for interactive review. |
| **Code implementation from a good plan** | **GPT-5.5 via Codex** (or Sonnet 5 / Opus 4.8) | Once the plan is solid, implementation is well-specified execution — the exact case where Fable is wasted. See Codex section below. |
| **Research fan-out / summarization** | **Sonnet 5** (Haiku 4.5 for bulk) | Parallel, independent, verifiable-after-the-fact. Near-Opus quality at ~⅗ cost; run many in parallel. |
| **Mechanical edits / formatting / codemods** | **Haiku 4.5** (or Sonnet 5) | Deterministic, low ambiguity, high volume. No compounding accuracy benefit from a frontier model. |
| **Classification / extraction / routing decisions** | **Haiku 4.5** | Fast, cheap, single-shot. 10× cheaper than Fable with no meaningful quality loss on structured tasks. Use with `strict` tool schemas / structured outputs. |

**A scoreable heuristic [COMMUNITY, DevelopersDigest]:** +1 toward Fable if the task spans 10+ files or ~5,000+ lines, is underspecified (needs discovery), runs async without human steering, prioritizes quality over speed, or *previously failed on a cheaper model*. +1 toward Opus/lower for interactive, review, high-throughput, or cost-sensitive work. Use Fable only if it scores ~2+ points higher; otherwise default down.

---

## When Fable Is NEEDED vs When It's Wasted

**[INFERENCE + SOURCED positioning]**

**Signals Fable is genuinely needed:**
- **Ambiguity / underspecification** — the model must explore to discover requirements before acting (Fable is trained to ground itself in the environment first).
- **Long horizon** — dozens-to-hundreds of dependent steps, multi-hour or overnight autonomous runs that must hold context the whole way.
- **Cross-cutting decisions** — architecture, migrations touching many files, choices that constrain everything downstream.
- **High cost of being wrong** — a bad call is expensive to detect and unwind (production migration, security-adjacent logic, financial modeling).
- **Judging/verifying other models' work** — the verifier should be your strongest model.

**Signals Fable is wasted (push down):**
- **Well-specified mechanical tasks** — the plan already says exactly what to do; execution is deterministic.
- **Bulk parallel work** — many independent, individually-cheap items (extraction over N documents, formatting N files). Parallelism + a cheap model beats one expensive model.
- **Interactive/latency-sensitive turns** — Fable is explicitly "Slower" in Anthropic's own latency column; its minutes-long turns hurt tight human-in-the-loop loops.
- **High-precision filtering** (e.g., review) — where extra exploration adds noise rather than signal.
- **ZDR-required workloads** — Fable can't run under zero data retention at all; this is a hard constraint, not a preference **[SOURCED]**.
- **A guardrail:** Fable's unbounded exploration caused timeouts in testing — always pair Fable agentic runs with step/`task_budget` limits **[COMMUNITY + SOURCED]** (`task-budgets-2026-03-13` beta is supported on Fable).

---

## Cost Math: What Routing Saves

**[INFERENCE, illustrative — real numbers depend on your token mix]**

Assume a task with ~1M input + 200K output tokens of model work.

| Run entirely on… | Input cost | Output cost | Total |
|---|---|---|---|
| Fable 5 | $10.00 | $10.00 | **$20.00** |
| Opus 4.8 | $5.00 | $5.00 | **$10.00** |
| Sonnet 5 (intro) | $2.00 | $2.00 | **$4.00** |
| Haiku 4.5 | $1.00 | $1.00 | **$2.00** |

**The orchestrator pattern:** in a real agentic job the *orchestrator* consumes a small slice of total tokens; the bulk is implementation, research, and mechanical work. If Fable-orchestration is ~15% of tokens and the other 85% runs on Sonnet/Haiku/Codex instead of all-Fable:

- All-Fable: ~$20 (illustrative)
- Fable orchestrator (15%) + cheap workers (85% at ~Sonnet rates): ~**$3 + $3.4 ≈ $6.4** → roughly **65–70% cheaper**, matching the community-reported 40–60% (and up to 5–10× when workers drop to Haiku) savings **[COMMUNITY]**.

**The completion-rate caveat that flips it back [COMMUNITY]:** if a long-horizon task *fails or needs 2–3 retries on the cheaper model* but Fable one-shots it, Fable is cheaper per *completed* task despite 2× tokens. So: cheap models for work that's reliably one-shot; Fable for work where retries/rescues are the real cost.

---

## Specific Guidance for Your Setup (Fable orchestrates + Codex implements + Sonnet researches)

**[INFERENCE tuned to your workflow]** Your architecture is already the recommended shape ("strong orchestrator + cheap workers"). Refinements:

### Stays on Fable
- **The orchestrator loop itself** — routing, sequencing, deciding what to delegate and when.
- **Plan/spec authoring** — the artifacts everything downstream depends on.
- **Judging** — reviewing plans, grading Codex's output, verifying research. Keep the judge = your strongest model; this is the one place *not* to economize, because a weak judge silently approves weak work.
- **Hard debugging / root-cause** when a delegated task is stuck (the "rescue" role).

### Push down to GPT-5.5 via `codex exec`
- **Implementation from a finalized plan.** GPT-5.5 is built for agentic coding and is "where it operates the way OpenAI intended" in Codex **[COMMUNITY]**. Community benchmarks: GPT-5.5 leads on Terminal-Bench 2.0 (82.7%) and long-context/DevOps, while Claude leads on SWE-bench Pro and MCP multi-tool orchestration — i.e., **"terminal-first" execution favors GPT-5.5; "codebase-first" reasoning favors Claude** [COMMUNITY, benchmarks vs Opus 4.7, slightly stale]. Given a *good plan from Fable*, Codex is a strong, cost-effective executor.
- **Keep the plan/spec detailed** — the better-specified the handoff, the more implementation becomes deterministic execution where GPT-5.5 shines and Fable would be wasted. This is the crux of "plan with Claude, implement with Codex."

### Push down to Sonnet 5 / Haiku 4.5
- **Sonnet 5:** research legwork, summarization, medium-complexity subtasks, first-pass code where Codex isn't the fit. Near-Opus quality at ~⅗ cost; run fan-out in parallel.
- **Haiku 4.5:** classification, extraction, mechanical edits, routing/triage of incoming items, and Fable-subagent work where `low` effort suffices.

### Operational cautions **[SOURCED + INFERENCE]**
- **Bound Fable's runs** with `task_budget` / explicit step limits — its exploration-first behavior can time out or over-spend if unbounded.
- **Handle Fable refusals** — wire the `fallbacks` parameter (Fable → Opus 4.8) so a classifier decline doesn't just stop the orchestrator; false positives on benign security/life-sciences-adjacent work do happen. You are not billed for a pre-output refusal, and fallback credit refunds the cache-switch cost.
- **Watch the ZDR constraint** — if any workload requires zero data retention, it cannot run on Fable; route it to Opus 4.8.
- **Don't route interactive/review turns to Fable** — its "Slower" latency and lower review precision make Opus 4.8 the better pick there, even though it's your "lower" tier.

---

## Gaps & Limitations

- **Fable benchmark numbers are all [COMMUNITY]** — Anthropic's announcement makes qualitative SOTA claims but I could not verify the specific SWE-bench Pro / FrontierCode figures against a primary Anthropic benchmark table. Multiple third-party sites cite identical numbers, which suggests a common (possibly Anthropic-derived) source, but I treat them as indicative.
- **GPT-5.5 benchmark comparisons cite Opus 4.7, not 4.8** — slightly stale; the *direction* (terminal-first→GPT-5.5, codebase-first→Claude) is the reliable takeaway, not the exact deltas.
- **GPT-5.5 pricing [COMMUNITY, unverified vs OpenAI]:** reported ~$5 input / $30 output per MTok (GPT-5.5 Pro ~$30/$180), with OpenAI reportedly claiming ~40% fewer output tokens per Codex task vs 5.4. Confirm against OpenAI's official pricing before using in cost models.
- **No independent long-run reliability data yet** — Fable is ~4 weeks GA as of this writing; claims about multi-day autonomous runs are largely vendor/early-adopter reports.

---

## Sources

**Anthropic (primary, [SOURCED]):**
- [Introducing Claude Fable 5 and Claude Mythos 5 — announcement](https://www.anthropic.com/news/claude-fable-5-mythos-5)
- [Introducing Claude Fable 5 — platform docs](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5.md)
- [Models overview / choosing a model](https://platform.claude.com/docs/en/about-claude/models/overview)
- `claude-api` skill (pricing/API-behavior table, cached 2026-06-24)

**Community / practitioner ([COMMUNITY]):**
- [Fable 5 vs Opus 4.8 — Developers Digest (routing framework, timeouts, migration example)](https://www.developersdigest.tech/blog/fable-5-vs-opus-48-when-to-use-which)
- [Fable 5 vs Opus 4.8 — TrueFoundry (benchmarks, when-to-use)](https://www.truefoundry.com/blog/claude-fable-5-vs-opus-4-8-benchmarks-pricing-when-to-use-each)
- [Fable 5 vs Opus 4.8 for coding agents — Verdent](https://www.verdent.ai/guides/claude-fable-5-vs-opus-4-8-coding)
- [AI model orchestration: smart model + cheaper sub-agents — MindStudio](https://www.mindstudio.ai/blog/ai-model-orchestration-smart-model-cheaper-sub-agents)
- [Token cost optimization with multi-model routing — MindStudio](https://www.mindstudio.ai/blog/ai-agent-token-cost-optimization-multi-model-routing)
- [AI model routing guide for coding agents — Augment Code](https://www.augmentcode.com/guides/ai-model-routing-guide)
- [The /codex plugin for Claude Code: GPT-5.5 + Opus — BuildMVPFast](https://www.buildmvpfast.com/blog/codex-plugin-claude-code-gpt-5-5-opus-multi-model-2026)
- [Multi-agent orchestration with Codex — Firecrawl](https://www.firecrawl.dev/blog/codex-multi-agent-orchestration)
- [Opus 4.8 vs GPT-5.5 for long-running agentic tasks — MindStudio](https://www.mindstudio.ai/blog/claude-opus-4-8-vs-gpt-5-5-agentic-tasks)
- [GPT-5.5 review: benchmarks & pricing — BuildFastWithAI](https://www.buildfastwithai.com/blogs/gpt-5-5-review-2026)
