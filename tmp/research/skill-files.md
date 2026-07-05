# Writing SKILL Files for AI Coding Agents — Research Summary

*Research date: 2026-07-05. Covers Anthropic Agent Skills (SKILL.md), Matt Pocock's skills, popular community skill repos, and OpenAI Codex CLI (AGENTS.md + skills).*

## Executive Summary

A **skill** is a directory with a `SKILL.md` file — YAML frontmatter (metadata) plus a Markdown body of instructions — optionally accompanied by `scripts/`, `references/`, and `assets/` folders. Both Anthropic (Claude Code, claude.ai, API) and OpenAI (Codex CLI) now use essentially the same `SKILL.md` format. The core design idea is **progressive disclosure**: only the `name` + `description` are always loaded; the body loads when the skill triggers; bundled files and scripts load only when referenced. The two highest-leverage things to get right are (1) a **specific, "pushy," third-person `description`** that says what the skill does *and* when to use it, and (2) a **concise body kept under ~500 lines** with detail pushed into reference files. The biggest cross-model nuance: **Claude benefits from intent and the "why"; GPT-5.x/Codex follows literal, prescriptive instructions tightly.**

Primary sources: [Anthropic engineering blog](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills), [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices), [anthropics/skills](https://github.com/anthropics/skills), [mattpocock/skills](https://github.com/mattpocock/skills), [obra/superpowers](https://github.com/obra/superpowers), [Codex AGENTS.md guide](https://developers.openai.com/codex/guides/agents-md), [Codex Skills](https://developers.openai.com/codex/skills).

---

## 1. Anatomy of a Good SKILL.md

### 1.1 Directory shape

```text
skill-name/
├── SKILL.md          # required: YAML frontmatter + Markdown instructions
├── FORMS.md          # optional reference (loaded as needed)
├── reference/        # optional docs read into context on demand
│   ├── finance.md
│   └── sales.md
├── scripts/          # optional executable code (run via bash, output only)
│   └── validate.py
└── assets/           # optional templates, fonts, icons used in output
```

Source: [Agent Skills overview — Skill structure](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview#skill-structure); [skill-creator SKILL.md](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md).

### 1.2 Frontmatter fields and hard rules

Only two fields are **required**: `name` and `description` ([overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview#skill-structure)).

`name`:
- Maximum **64 characters**
- **Lowercase letters, numbers, and hyphens only**
- No XML tags
- Cannot contain reserved words **"anthropic"** or **"claude"**

`description`:
- Must be **non-empty**
- Maximum **1024 characters**
- No XML tags
- Should describe **what the skill does AND when to use it**

Source: [Skill authoring best practices — YAML frontmatter](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).

Optional fields seen in the wild:
- `compatibility` — required tools/dependencies ([skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md)).
- `disable-model-invocation: true` — makes a skill **user-invoked only** (fires only when the user types its name, e.g. `/to-prd`), not auto-triggered by the model. Used throughout [mattpocock/skills](https://github.com/mattpocock/skills/blob/main/CLAUDE.md) (e.g. the [`to-prd` skill](https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/to-prd/SKILL.md)).

### 1.3 The three loading levels (progressive disclosure)

| Level | When loaded | Token cost | Content |
|---|---|---|---|
| **1: Metadata** | Always, at startup | ~100 tokens/skill | `name` + `description` from frontmatter |
| **2: Instructions** | When the skill triggers | Under ~5k tokens | The SKILL.md body |
| **3+: Resources** | As needed | Effectively unlimited | Bundled files read via bash; scripts executed (code never enters context) |

Source: [Agent Skills overview — Three types of Skill content](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview#how-skills-work). Claude reads `SKILL.md` from the filesystem via bash only once the description matches; scripts run via bash and "the script code itself never enters context" ([overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)).

### 1.4 Description: the single most important field

The description is "critical for skill selection: Claude uses it to choose the right Skill from potentially 100+ available Skills" ([best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)). Rules:

**Always write in third person.** The description is injected into the system prompt, and "inconsistent point-of-view can cause discovery problems" ([best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)):
- Good: `"Processes Excel files and generates reports"`
- Avoid: `"I can help you process Excel files"` / `"You can use this to process Excel files"`

**Say what it does AND when to use it, with concrete trigger terms.** Canonical example:
```yaml
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
```

**Avoid vague descriptions:** `"Helps with documents"`, `"Processes data"`, `"Does stuff with files"` ([best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)).

**Make it "pushy" — Claude tends to *under*trigger skills.** From the [skill-creator SKILL.md](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md): instead of `"How to build a simple fast dashboard to display internal Anthropic data,"` write `"...Make sure to use this skill whenever the user mentions dashboards, data visualization, internal metrics, or wants to display any kind of company data, even if they don't explicitly ask for a 'dashboard.'"` And: **all "when to use" context goes in the description, not the skill body.**

### 1.5 Naming conventions

Prefer **gerund form** (verb + -ing) because it names the activity: `processing-pdfs`, `analyzing-spreadsheets`, `managing-databases`, `testing-code`, `writing-documentation`. Noun phrases (`pdf-processing`) and action forms (`process-pdfs`) are acceptable alternatives. Avoid vague/generic names (`helper`, `utils`, `tools`, `documents`, `data`) and reserved words. Source: [best practices — Naming conventions](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).

---

## 2. Core Principles

### 2.1 Concise is key — "the context window is a public good"

> "Not every token in your Skill has an immediate cost... However, being concise in SKILL.md still matters: once Claude loads it, every token competes with conversation history and other context." — [best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

**Default assumption: Claude is already very smart.** Challenge each line: "Does Claude really need this explanation? Can I assume Claude knows this? Does this paragraph justify its token cost?" The docs contrast a ~50-token concise PDF snippet against a ~150-token version that explains what a PDF is and lists five libraries — the concise one wins ([best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)).

### 2.2 Keep SKILL.md under ~500 lines

> "Keep SKILL.md body under 500 lines for optimal performance. If your content exceeds this, split it into separate files using the progressive disclosure patterns." — [best practices — Token budgets](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

Related target: keep the body under ~5,000 words / ~5k tokens (Level 2 budget from the [overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview#how-skills-work)). For large reference files (>100 lines), add a **table of contents** at the top so partial reads (`head`) still reveal the full scope ([best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)).

### 2.3 When to split into references/ and scripts/

Split when the main file gets unwieldy, or when contexts are mutually exclusive. "If certain contexts are mutually exclusive or rarely used together, keeping the paths separate will reduce the token usage." — [engineering blog](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills).

Three documented patterns ([best practices — Progressive disclosure patterns](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)):
1. **High-level guide with references** — quick start in SKILL.md, `See [FORMS.md]`, `See [REFERENCE.md]` for depth.
2. **Domain-specific organization** — e.g. a BigQuery skill with `reference/finance.md`, `reference/sales.md` so a sales question never loads finance schemas.
3. **Conditional details** — show basic content, link advanced (`For tracked changes: See [REDLINING.md]`).

**Keep references one level deep from SKILL.md.** Deeply nested references (SKILL.md → advanced.md → details.md) cause Claude to partial-read (`head -100`) and miss content. All reference files should link directly from SKILL.md ([best practices — Avoid deeply nested references](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)).

**Scripts vs reading code.** Use executable scripts for deterministic/fragile/repetitive operations — they're more reliable, save tokens, and ensure consistency. Make execution intent explicit: `"Run analyze_form.py to extract fields"` (execute) vs `"See analyze_form.py for the extraction algorithm"` (read as reference). Scripts should **"solve, don't punt"** — handle errors explicitly rather than failing and leaving Claude to figure it out — and avoid "voodoo constants" (unexplained magic numbers). Source: [best practices — Advanced: Skills with executable code](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).

### 2.4 Set the right "degrees of freedom" (match specificity to task fragility)

The docs frame this as a robot on a path ([best practices — Set appropriate degrees of freedom](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)):
- **High freedom** (prose instructions) — many valid approaches, context-dependent decisions. e.g. code review steps.
- **Medium freedom** (pseudocode / parameterized scripts) — a preferred pattern with acceptable variation.
- **Low freedom** (exact scripts, no params) — fragile, consistency-critical operations. e.g. `Run exactly: python scripts/migrate.py --verify --backup / Do not modify the command`.

Analogy: **narrow bridge with cliffs** = exact guardrails; **open field** = general direction and trust.

### 2.5 Imperative voice, explain the "why," avoid over-specification

The [skill-creator SKILL.md](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) is explicit about not over-constraining:

> "Try hard to explain the **why** behind everything you're asking the model to do. Today's LLMs are smart... If you find yourself writing ALWAYS or NEVER in all caps, reframe and explain the reasoning so the model understands why the thing you're asking for is important."

Avoid: heavy-handed MUSTs, super-rigid structures, overfitting to specific examples. Prefer: theory-of-mind reasoning, general patterns over narrow examples, explanation over prescription. (Note: this is Claude-specific guidance — see §5 for how it flips for GPT-5.x/Codex.)

Use the **imperative** for the actual steps (`Analyze the code structure`, `Check for edge cases`) and use the **template pattern** / **examples pattern** for output format. For strict output, `ALWAYS use this exact template structure`; for flexible output, `Here is a sensible default format, but use your best judgment`. Input/output example pairs (e.g. commit-message examples) teach style better than description alone. Source: [best practices — Common patterns](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).

### 2.6 Workflows, checklists, and feedback loops

For complex multi-step tasks, give a copy-able checklist Claude ticks off, then number the steps. For quality-critical tasks, build a **validator → fix → repeat** loop (e.g. "Validate immediately: `python validate.py`. If it fails, fix and re-run. Only proceed when validation passes"). The **plan-validate-execute** pattern (write a `changes.json` plan, validate it with a script, then apply) catches errors before destructive batch operations. Source: [best practices — Workflows and feedback loops](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).

### 2.7 Content hygiene anti-patterns

- **No time-sensitive info** in the main body — move deprecated behavior to a collapsed "Old patterns" `<details>` section rather than `"If before August 2025..."`.
- **Consistent terminology** — pick one term (`field`, not `field`/`box`/`element`/`control`).
- **Forward slashes only** in paths (`scripts/helper.py`), never backslashes.
- **Don't offer too many options** — give a default with an escape hatch, not `"use pypdf or pdfplumber or PyMuPDF or..."`.
- **Don't assume packages are installed** — state `pip install ...` explicitly.
- **MCP tools need fully-qualified names** — `ServerName:tool_name` (e.g. `GitHub:create_issue`).

Source: [best practices — Anti-patterns / Content guidelines](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).

### 2.8 Evaluation-driven development

> "Create evaluations BEFORE writing extensive documentation. This ensures your Skill solves real problems rather than documenting imagined ones." — [best practices — Evaluation and iteration](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

Process: run Claude on representative tasks *without* the skill to find gaps → build 3 eval scenarios → establish a baseline → write minimal instructions to close the gaps → iterate. Develop iteratively with **two Claudes**: "Claude A" helps author/refine the skill; a fresh "Claude B" uses it on real tasks; you feed Claude B's failures back to Claude A. Test the skill with **Haiku, Sonnet, and Opus** — what works for Opus may under-guide Haiku. The blog adds: monitor real usage and watch for undertriggering, missed file references, and ignored bundled files.

---

## 3. Matt Pocock's Advice + Annotated Example

Matt Pocock (Total TypeScript; ex-Vercel/Stately) publishes [mattpocock/skills](https://github.com/mattpocock/skills) — "Skills for Real Engineers. Straight from my .claude directory" (MIT-licensed; docs mirrored at `aihero.dev/skills-<name>`).

### 3.1 His organizing conventions ([CLAUDE.md](https://github.com/mattpocock/skills/blob/main/CLAUDE.md))

- **Buckets.** *Promoted* buckets (`engineering/`, `productivity/`) are publicly documented; *non-promoted* (`misc/`, `personal/`, `in-progress/`, `deprecated/`) are internal only. Promoted skills must appear in the README, in `.claude-plugin/plugin.json`, and have a docs page; non-promoted must not.
- **User-invoked vs model-invoked.** Each SKILL.md is either user-invoked only (`disable-model-invocation: true`) or model-invokable. In his words, "user-invoked skills... orchestrate" while "model-invoked skills... hold the reusable discipline."
- **Router must not lie.** His `ask-matt` router skill must stay in sync: "a new skill it never mentions, or a stale one it still routes to, is a router that lies."

### 3.2 His skill-writing principles ([`writing-great-skills`](https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/writing-great-skills/SKILL.md))

Frontmatter:
```yaml
name: writing-great-skills
description: Reference for writing and editing skills well — the vocabulary and principles that make a skill predictable.
disable-model-invocation: true
```

Core thesis:

> "**Predictability** — the agent taking the same *process* every run, not producing the same output — is the root virtue."

Key principles he articulates:
- **Invocation is a tradeoff.** Model-invoked = always loaded, reachable automatically (context load); user-invoked = fires only on its name (cognitive load). Choose deliberately.
- **Descriptions:** frontload the central concept, list distinct trigger branches, eliminate redundancy.
- **Information hierarchy by immediacy:** in-skill steps (ordered actions with completion criteria) → in-skill reference (consulted on demand) → external reference (behind context pointers).
- **Only split a skill to earn one of two loads:** by *invocation* (a distinct trigger word) or by *sequence* (to prevent premature completion).
- **Pruning discipline:** single sources of truth; test every line for relevance; aggressively delete no-op sentences rather than rewrite them.
- **Leading words:** use compact pretrained concepts ("tight," "red") that carry distributed meaning with few tokens.
- **Named failure modes:** premature completion, duplication, sediment (stale layers), sprawl, no-ops.

### 3.3 Annotated example — his [`to-prd` skill](https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/to-prd/SKILL.md)

```yaml
---
name: to-prd
description: Turn the current conversation into a PRD and publish it to the project issue tracker — no interview, just synthesis of what you've already discussed.
disable-model-invocation: true
---
```

Annotations:
- **`disable-model-invocation: true`** — this is a workflow the human triggers on purpose (`/to-prd`), not something the model should silently decide to run. Contrast with Anthropic's default of maximizing auto-trigger.
- **Description leads with the action** ("Turn the current conversation into a PRD") and states the boundary ("no interview, just synthesis") — matching his "frontload the central concept" rule.
- **The body is short and imperative**, a numbered process: (1) Codebase Assessment — read the repo, respect domain terms and existing ADRs; (2) Testing Seam Analysis — find the fewest, highest-level test seams and *confirm with the user before proceeding*; (3) PRD Composition & Publication — write to a fixed template and publish with a `ready-for-agent` label.
- **A fixed output template** (Problem Statement, Solution, User Stories in "As a [actor], I want [feature], so that [benefit]" form, Implementation Decisions, Testing Decisions, Out of Scope, Further Notes) — the "template pattern" from Anthropic's guide, giving predictable structure without over-constraining prose.

This is a compact, high-freedom-where-it-matters / low-freedom-on-output skill: it trusts Claude on synthesis but pins the deliverable shape and inserts a human gate before committing to a test strategy.

---

## 4. Annotated Real Examples from Popular Repos

### 4.1 anthropics/skills — [`skill-creator`](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) (the canonical meta-skill)

```yaml
name: skill-creator
description: Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.
```

Why it's a good model:
- The description is **long, specific, and enumerates triggers** ("create a skill from scratch, edit... optimize... run evals... benchmark... optimize a skill's description") — exactly the "be pushy / list distinct branches" advice.
- Its body encodes a **7-step workflow** (capture intent → interview/research → write SKILL.md → create test cases in `evals/evals.json` → run & evaluate → improve → optimize the description), demonstrating the evaluation-driven approach the docs preach.
- It embeds the **"explain the why / don't over-constrain"** philosophy quoted in §2.5, and a "principle of lack of surprise" (a skill's contents shouldn't surprise the user relative to its description) — a security/trust norm.

### 4.2 obra/superpowers — [`using-superpowers`](https://raw.githubusercontent.com/obra/superpowers/main/skills/using-superpowers/SKILL.md) (a high-star framework)

```yaml
name: using-superpowers
description: Use when starting any conversation - establishes how to find and use skills, requiring skill invocation before ANY response including clarifying questions
```

[obra/superpowers](https://github.com/obra/superpowers) is "an agentic skills framework & software development methodology" — a directory of ~14 single-file skills (TDD, debugging, brainstorming, writing plans, code review, verification) plus a session-start hook (<2k tokens) that tells the agent to invoke a relevant skill before doing anything. Notable conventions:
- **Trigger-first description:** "Use when starting any conversation" makes this a near-always-on bootstrap.
- **Hard gates via ALL-CAPS + checklists:** a 13-row "Red Flags" table of rationalizations to reject (e.g. "This is just a simple question" → "Questions are tasks. Check for skills"), functioning as decision gates.
- **The 1% rule:** "If you think there is even a 1% chance a skill might apply..." — an aggressive anti-undertriggering stance.
- **Precedence hierarchy stated explicitly:** explicit user instructions > skills > default behavior.
- The community docs note each skill body often carries "hard gates, a checklist that becomes TodoWrite tasks, and often a Graphviz DOT graph that Claude reads as executable instructions" ([search summary](https://github.com/obra/superpowers)). It is **multi-host** — the same folder targets Claude Code, Cursor, Codex, Copilot CLI, Gemini CLI, and OpenCode.

> Note: superpowers is a deliberately *heavy-handed* style (ALL-CAPS mandates, hard gates) that partly contradicts Anthropic's "avoid ALL-CAPS MUSTs, explain the why" guidance. It's included as a popular real-world data point, not a purity example — it optimizes for *reliable triggering and process adherence* over token minimalism.

### 4.3 Anthropic's shipped PDF-style skill (the reference pattern from the docs)

```yaml
name: pdf-processing
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
```
Body: a **quick-start code block** (pdfplumber) inline, then pointers — `Form filling: See [FORMS.md]`, `API reference: See [REFERENCE.md]`, `Examples: See [EXAMPLES.md]` — with `scripts/` for deterministic form operations. This is the textbook "Pattern 1: high-level guide with references." Source: [overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) and [best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).

---

## 5. Codex-Specific Guidance (AGENTS.md + Codex Skills)

### 5.1 AGENTS.md — persistent, repo-level instructions

Codex "reads AGENTS.md files before doing any work," loading them automatically **once per run** (in the TUI, once per session) — unlike prompts that reset per turn. Source: [Codex AGENTS.md guide](https://developers.openai.com/codex/guides/agents-md).

**Discovery & precedence:**
1. **Global scope:** `~/.codex/AGENTS.override.md` if present, else `~/.codex/AGENTS.md` (first non-empty file only).
2. **Project scope:** walk from the Git root down to the current working directory, at each level checking `AGENTS.override.md`, then `AGENTS.md`, then fallback names.
3. **Merge order:** files concatenate from root downward; **"files closer to your current directory override earlier guidance."** Loading stops at `project_doc_max_bytes` (default **32 KiB**).

**What goes where:** global file = durable working agreements (test commands, package manager, approval workflow); project file = repo norms (lint requirements, doc standards); nested overrides = team-specific rules. Verify with `codex --ask-for-approval never "Summarize the current instructions."` — Codex should echo guidance in precedence order.

**AGENTS.md vs prompts vs skills** ([best practices](https://developers.openai.com/codex/learn/best-practices)): "Overloading the prompt with durable rules instead of moving them into AGENTS.md or a skill" is a named mistake. Rule of thumb: durable, always-on rules → **AGENTS.md**; reusable *workflows* with richer instructions/scripts → **skills**; one-off asks → **prompt**.

### 5.2 Codex Skills — same SKILL.md shape as Claude

> "A skill is a directory with a `SKILL.md` file plus optional scripts and references." — [Codex Skills](https://developers.openai.com/codex/skills)

Frontmatter is the same two-field shape:
```yaml
---
name: skill-name
description: Explain exactly when this skill should and should not trigger.
---
```

**Invocation, two ways** ([Codex Skills](https://developers.openai.com/codex/skills)):
- **Explicit:** user runs `/skills` or `$`-mentions the skill.
- **Implicit:** "Codex can choose a skill when your task matches the skill description." Because implicit matching depends on the description, **write concise descriptions with clear scope and boundaries, and front-load the key use case and trigger words** so matching survives description truncation.

**Custom prompts are deprecated** — OpenAI now steers reusable instructions into skills ([search summary of Codex custom-prompts docs](https://developers.openai.com/codex/custom-prompts)). Codex also offers **Record & Replay**: it records a demonstrated workflow and drafts a reusable skill from it ([best practices](https://developers.openai.com/codex/learn/best-practices)).

### 5.3 How to write instructions GPT-5.x/Codex follows well

The [Codex prompting guide](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide) is explicit that GPT-5/Codex "follow instructions with high precision" and **interpret directives literally rather than inferring intent**:

- **Be prescriptive and granular.** Spell out exact tool preferences and ordering (e.g. `Default to solver tools: git, rg, read_file, list_dir...`; `Strictly avoid raw cmd/terminal when a dedicated tool exists`). Codex responds better to explicit behaviors, edge cases, and tool precedence than to high-level objectives.
- **Never leave conflicting instructions.** Contradictions degrade output; state exact boundaries (`NEVER use destructive commands like git reset --hard` unless explicitly approved).
- **Be concise and give explicit output/format rules** ("very concise; friendly coding teammate tone"; "avoid heavy formatting for simple confirmations"; "lead with a quick explanation of the change, then more detail").

**The key contrast for authoring:**

| | Claude (Anthropic Skills) | GPT-5.x / Codex |
|---|---|---|
| Instruction style | Explain intent and the **why**; trust the model to generalize | **Literal, prescriptive**; spell out exact tools/steps/edge cases |
| ALL-CAPS MUSTs | Discouraged — "reframe and explain the reasoning" ([skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md)) | Fine and often necessary; the model follows literal constraints tightly |
| Over-specification | An anti-pattern (over-constrains a smart model) | Less risky; granular precision is a feature |
| Durable rules home | Skill body / references | **AGENTS.md** (skills for workflows) |

Practical takeaway: a skill body that works for both should keep the **structure** (short, progressive-disclosure, trigger-rich description) but, if targeting Codex specifically, lean toward **explicit step lists and exact commands** rather than "use your best judgment"; if targeting Claude, add the **rationale** and allow judgment where the task has many valid paths.

---

## 6. Checklist for Authoring a New Skill

Adapted from the [Anthropic best-practices checklist](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) plus Pocock/superpowers/Codex conventions.

**Frontmatter & discovery**
- [ ] `name`: lowercase-hyphenated, ≤64 chars, gerund form preferred, no `anthropic`/`claude`.
- [ ] `description`: third person, ≤1024 chars, says **what it does AND when to use it**, front-loads trigger keywords, "pushy" enough to avoid undertriggering.
- [ ] Decided **model-invoked vs user-invoked** (`disable-model-invocation: true` for human-triggered workflows).

**Body**
- [ ] Under **~500 lines** (split into `references/` if approaching the limit).
- [ ] Concise — no explaining things the model already knows.
- [ ] Imperative steps; for Claude, explain the **why** and avoid gratuitous ALL-CAPS; for Codex, be literal and prescriptive.
- [ ] Right **degrees of freedom** — exact commands for fragile ops, general direction for open-ended ones.
- [ ] Output **template** or input/output **examples** where format matters.
- [ ] Checklists + **validate→fix→repeat** loops for multi-step or high-stakes tasks.
- [ ] Consistent terminology; no time-sensitive claims (use an "Old patterns" `<details>` block); forward-slash paths only.

**Bundled files & scripts**
- [ ] Reference files **one level deep** from SKILL.md; add a table of contents if >100 lines.
- [ ] Organized by domain so unrelated context never loads.
- [ ] Scripts **solve, don't punt** (explicit error handling); no unexplained magic numbers.
- [ ] Execution intent explicit ("Run X" vs "See X for reference"); required packages named; MCP tools fully qualified (`Server:tool`).

**Testing & iteration**
- [ ] ≥3 evaluation scenarios written **before** heavy documentation; baseline measured without the skill.
- [ ] Tested with the actual models you'll run (Haiku/Sonnet/Opus for Claude; the relevant GPT-5.x tier for Codex).
- [ ] Observed real usage; refined description/structure for missed triggers or ignored files.
- [ ] Only from trusted sources; audited for surprising behavior / data exfiltration (skills run code).

---

## 7. Version / Currency Notes

- Frontmatter validation limits (name ≤64, description ≤1024, reserved-word ban) are current as of the [platform.claude.com docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) fetched 2026-07-05.
- Claude API Skills require beta headers `code-execution-2025-08-25`, `skills-2025-10-02`, `files-api-2025-04-14` and have **no network access / no runtime package install**; Claude Code skills have full network access. claude.ai varies by admin settings. Source: [overview — Runtime environment constraints](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).
- Codex: **custom prompts are deprecated** in favor of skills; `AGENTS.md` precedence and the 32 KiB (`project_doc_max_bytes`) cap are current per [Codex AGENTS.md guide](https://developers.openai.com/codex/guides/agents-md) and [Codex Skills](https://developers.openai.com/codex/skills).
- The SKILL.md format is now cross-vendor: Anthropic + OpenAI Codex share it, and multi-host frameworks like [obra/superpowers](https://github.com/obra/superpowers) target six+ agent CLIs from one folder.

## 8. Gaps / Limitations

- Anthropic gives **no built-in eval runner** — "Users can create their own evaluation system" ([best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)); mattpocock and skill-creator roll their own (`evals/evals.json`).
- The "under 500 lines" figure is a soft heuristic, not an enforced limit; word/token budgets (~5k) come from Level-2 loading, not a validator.
- Codex's exact frontmatter field set beyond `name`/`description` is under-documented publicly versus Anthropic's; treat Anthropic's field rules as the superset when authoring cross-vendor skills.
- superpowers' heavy ALL-CAPS/hard-gate style conflicts with Anthropic's "explain the why, avoid rigid MUSTs" guidance — both are in production; the right choice depends on how much you're fighting undertriggering.

## Additional Resources

- [Equipping agents for the real world with Agent Skills — Anthropic engineering](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Agent Skills overview — platform.claude.com](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Skill authoring best practices — platform.claude.com](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [The Complete Guide to Building Skills for Claude (PDF)](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)
- [anthropics/skills — skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md)
- [mattpocock/skills](https://github.com/mattpocock/skills) · [CLAUDE.md](https://github.com/mattpocock/skills/blob/main/CLAUDE.md) · [to-prd](https://raw.githubusercontent.com/mattpocock/skills/main/skills/engineering/to-prd/SKILL.md) · [writing-great-skills](https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/writing-great-skills/SKILL.md)
- [obra/superpowers](https://github.com/obra/superpowers) · [anthropic-best-practices.md](https://github.com/obra/superpowers/blob/main/skills/writing-skills/anthropic-best-practices.md)
- [Codex best practices](https://developers.openai.com/codex/learn/best-practices) · [AGENTS.md guide](https://developers.openai.com/codex/guides/agents-md) · [Codex Skills](https://developers.openai.com/codex/skills) · [Codex prompting guide](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide)
