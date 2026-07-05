# Writing AGENT Definition Files for AI Coding Tools — Research Summary

Research date: 2026-07-05. Covers Claude Code subagents (`.claude/agents/*.md`),
Codex CLI custom agents / `AGENTS.md`, and orchestrator-worker prompt lessons from
Anthropic's multi-agent research work.

Primary sources:
- Claude Code subagents docs: https://code.claude.com/docs/en/sub-agents
- Anthropic engineering, multi-agent research system: https://www.anthropic.com/engineering/multi-agent-research-system
- Codex custom agents / subagents: https://developers.openai.com/codex/subagents
- Codex AGENTS.md guide: https://developers.openai.com/codex/guides/agents-md
- AGENTS.md open standard: https://agents.md/

---

## Executive Summary

A Claude Code subagent is a single Markdown file: YAML frontmatter (config) plus a
Markdown body (the system prompt). Only `name` and `description` are required, and the
`description` is the single most important field — Claude reads it to decide whether to
delegate a task to the agent (https://code.claude.com/docs/en/sub-agents). The body should
define one focused role with an explicit output contract, because the subagent runs in a
**fresh, isolated context window** and sees none of your conversation history
(https://code.claude.com/docs/en/sub-agents). Codex CLI has an analogous but distinct model:
`AGENTS.md` is a single project-instructions file (not a per-agent definition), while Codex
*custom agents* are per-agent TOML files under `~/.codex/agents/` — closer in spirit to
Claude subagents but with explicit-only delegation (https://developers.openai.com/codex/subagents).

---

## 1. Anatomy of a Claude Code Agent File

### Minimal shape

```markdown
---
name: code-reviewer
description: Reviews code for quality and best practices
tools: Read, Glob, Grep
model: sonnet
---

You are a code reviewer. When invoked, analyze the code and provide
specific, actionable feedback on quality, security, and best practices.
```

"The frontmatter defines the subagent's metadata and configuration. The body becomes the
system prompt that guides the subagent's behavior. Subagents receive only this system prompt
plus basic environment details like the working directory, not the full Claude Code system
prompt." (https://code.claude.com/docs/en/sub-agents)

### File locations and precedence

Files live in `.claude/agents/` (project, check into git) or `~/.claude/agents/` (personal,
all projects). When names collide, the higher-priority scope wins
(https://code.claude.com/docs/en/sub-agents):

| Location | Scope | Priority |
| :--- | :--- | :--- |
| Managed settings | Organization-wide | 1 (highest) |
| `--agents` CLI flag | Current session | 2 |
| `.claude/agents/` | Current project | 3 |
| `~/.claude/agents/` | All your projects | 4 |
| Plugin `agents/` dir | Where plugin enabled | 5 (lowest) |

Directories are scanned recursively; identity comes only from the `name` field, not the file
path or subfolder. Keep `name` values unique within a scope, or only one loads
(https://code.claude.com/docs/en/sub-agents).

### Official frontmatter field reference

Only `name` and `description` are required (https://code.claude.com/docs/en/sub-agents):

| Field | Req | Purpose |
| :--- | :--- | :--- |
| `name` | Yes | Unique id, lowercase + hyphens. Also the `agent_type` seen by hooks. |
| `description` | Yes | When Claude should delegate to this subagent (the routing signal). |
| `tools` | No | Allowlist of tools. **Inherits all tools if omitted.** |
| `disallowedTools` | No | Denylist; removed from the inherited/specified set. |
| `model` | No | `sonnet`, `opus`, `haiku`, `fable`, a full id (`claude-opus-4-8`), or `inherit`. Defaults to `inherit`. |
| `permissionMode` | No | `default`, `acceptEdits`, `auto`, `dontAsk`, `bypassPermissions`, `plan`. |
| `maxTurns` | No | Max agentic turns before the subagent stops. |
| `skills` | No | Skills to preload (full content injected at startup). |
| `mcpServers` | No | MCP servers scoped to this subagent (inline or by-name reference). |
| `hooks` | No | Lifecycle hooks scoped to this subagent. |
| `memory` | No | Persistent memory scope: `user`, `project`, or `local` — enables cross-session learning. |
| `effort` | No | `low`/`medium`/`high`/`xhigh`/`max`; overrides session effort. |
| `isolation` | No | `worktree` runs the agent in an isolated git worktree copy. |
| `background` | No | `true` always runs as a background task. |
| `color`, `initialPrompt` | No | Display color; auto-submitted first turn when run as main agent. |

Source for all of the above: https://code.claude.com/docs/en/sub-agents

Notes that matter in practice:
- If both `tools` and `disallowedTools` are set, `disallowedTools` applies first, then
  `tools` resolves against what remains (https://code.claude.com/docs/en/sub-agents).
- Some tools are never available to subagents even if listed: `AskUserQuestion`,
  `EnterPlanMode`, `ExitPlanMode` (unless `permissionMode: plan`), `ScheduleWakeup`,
  `WaitForMcpServers` (https://code.claude.com/docs/en/sub-agents).
- Model resolution order: `CLAUDE_CODE_SUBAGENT_MODEL` env var → per-invocation `model`
  param → frontmatter `model` → main conversation's model
  (https://code.claude.com/docs/en/sub-agents).

### The critical constraint: fresh, isolated context

"Each subagent starts with a fresh, isolated context window. It doesn't see your conversation
history, the skills you've already invoked, or the files Claude has already read."
(https://code.claude.com/docs/en/sub-agents)

A non-fork subagent's initial context contains only: its own system prompt + appended
environment details; the delegation/task message Claude writes; `CLAUDE.md` and the memory
hierarchy; a git-status snapshot; and any preloaded skills
(https://code.claude.com/docs/en/sub-agents). The design implication: **the body must be
self-contained.** Never assume the agent knows what was discussed. If a rule matters (e.g.
"ignore `vendor/`"), it must be in the body or restated in the delegating prompt
(https://code.claude.com/docs/en/sub-agents).

The exception is a **fork** (`/fork`): a fork inherits the entire conversation, system prompt,
tools, and model of the main session, trading isolation for zero re-explanation and a shared
prompt cache (https://code.claude.com/docs/en/sub-agents).

---

## 2. Writing the `description` So Delegation Triggers Correctly

Delegation is driven by the `description`: "Claude automatically delegates tasks based on the
task description in your request, the `description` field in subagent configurations, and
current context. To encourage proactive delegation, include phrases like 'use proactively' in
your subagent's description field." (https://code.claude.com/docs/en/sub-agents)

Practical rules distilled from the docs and community best-practice writeups:

1. **Include an explicit trigger clause.** Say *when* to use it, not just what it is. The
   official code-reviewer example: "Expert code review specialist. Proactively reviews code
   for quality, security, and maintainability. **Use immediately after writing or modifying
   code.**" (https://code.claude.com/docs/en/sub-agents)
2. **Use proactive phrasing** — "Use PROACTIVELY when…", "Use immediately after…", "Use
   proactively for…". The debugger example: "Debugging specialist for errors, test failures,
   and unexpected behavior. **Use proactively when encountering any issues.**"
   (https://code.claude.com/docs/en/sub-agents)
3. **Be specific, not generic.** Community guidance: the description "should be specific
   (e.g., 'Use after writing code,' not just 'reviews code')" so Claude can route reliably; it
   is "a matching signal, not a label"
   (https://www.pubnub.com/blog/best-practices-for-claude-code-sub-agents/,
   https://code.claude.com/docs/en/sub-agents).
4. **Name concrete domains/tasks** the agent covers (e.g. "SQL queries, BigQuery operations,
   and data insights") so overlapping agents don't compete — the data-scientist example does
   exactly this (https://code.claude.com/docs/en/sub-agents).
5. **Escalate control when auto-routing isn't enough.** `@agent-<name>` mentions guarantee a
   specific subagent runs; `--agent <name>` makes the whole session that agent
   (https://code.claude.com/docs/en/sub-agents).

Good description template:
`<Role/expertise in one phrase>. <What it does>. Use PROACTIVELY when <trigger condition / after <event>>.`

---

## 3. Body / System-Prompt Best Practices

The docs' four headline best practices (https://code.claude.com/docs/en/sub-agents):
- **Design focused subagents** — each should excel at one specific task.
- **Write detailed descriptions** — Claude uses them to decide when to delegate.
- **Limit tool access** — grant only necessary permissions for security and focus.
- **Check into version control** — share project subagents with your team.

Expanding each, cross-referenced with the strongest patterns in popular repos:

### Single responsibility
"Each subagent should excel at one specific task" (https://code.claude.com/docs/en/sub-agents).
One agent = one role. If a body tries to be reviewer + implementer + deployer, split it. The
built-in Explore (read-only search) vs general-purpose (search + act) split models this
(https://code.claude.com/docs/en/sub-agents).

### Explicit workflow + output contract
The best agent bodies define (a) a numbered "When invoked" workflow and (b) an explicit output
format. The official code-reviewer body specifies both a review checklist *and* a required
output structure ("Provide feedback organized by priority: Critical issues (must fix) /
Warnings (should fix) / Suggestions") (https://code.claude.com/docs/en/sub-agents). Because the
only thing that returns to the main conversation is the agent's summary, the output contract is
what makes results usable. Community collections converge on the same: role → capabilities →
behavioral traits → response approach → example interactions
(https://github.com/wshobson/agents).

### Assume no inherited context
The body must restate everything it needs. It won't see prior files, tool results, or history
(https://code.claude.com/docs/en/sub-agents). Bodies commonly open with "You are a senior X
specializing in Y" and then a "When invoked: 1… 2… 3…" bootstrap that re-establishes state
(e.g. "Run git diff to see recent changes") (https://code.claude.com/docs/en/sub-agents).

### Tool scoping
Restrict `tools` to what the role needs — for security, focus, and to prevent an
exploration/review agent from mutating code. Read-only reviewers list `Read, Grep, Glob`
(and `Bash` only for `git diff`); agents that fix bugs add `Edit`
(https://code.claude.com/docs/en/sub-agents). Omitting `tools` inherits everything, which is
rarely what you want for a scoped worker.

### Model selection per agent
Match model tier to task difficulty and cost (https://code.claude.com/docs/en/sub-agents):
- **Haiku** — cheap/fast, high-volume or shallow work ("Control costs by routing tasks to
  faster, cheaper models like Haiku").
- **Sonnet** — default for capable analysis; the data-scientist example sets `model: sonnet`
  "for more capable analysis."
- **Opus** — hardest reasoning; wshobson's `python-pro` sets `model: opus`
  (https://raw.githubusercontent.com/wshobson/agents/main/plugins/python-development/agents/python-pro.md).
- **`inherit`** (default) — match the main session; the official code-reviewer uses
  `model: inherit`.
Use `effort` to tune reasoning depth independently of model tier
(https://code.claude.com/docs/en/sub-agents).

---

## 4. Annotated Real Examples

### Example A — Official code-reviewer (read-only, output contract)
Source: https://code.claude.com/docs/en/sub-agents

```markdown
---
name: code-reviewer
description: Expert code review specialist. Proactively reviews code for quality, security, and maintainability. Use immediately after writing or modifying code.
tools: Read, Grep, Glob, Bash
model: inherit
---

You are a senior code reviewer ensuring high standards of code quality and security.

When invoked:
1. Run git diff to see recent changes
2. Focus on modified files
3. Begin review immediately

Review checklist:
- Code is clear and readable
- ... No exposed secrets or API keys ...

Provide feedback organized by priority:
- Critical issues (must fix)
- Warnings (should fix)
- Suggestions (consider improving)
```
Why it's good: proactive trigger in the description; read-only tool set (no `Edit`/`Write`);
a self-bootstrapping "When invoked" workflow that assumes zero inherited context; and a strict
output contract (priority-bucketed feedback) so the returned summary is immediately actionable.

### Example B — wshobson `python-pro` (versioned expertise, opus tier)
Source: https://raw.githubusercontent.com/wshobson/agents/main/plugins/python-development/agents/python-pro.md

```markdown
---
name: python-pro
description: Master Python 3.12+ with modern features, async programming, performance optimization, and production-ready practices. Expert in the latest Python ecosystem including uv, ruff, pydantic, and FastAPI. Use PROACTIVELY for Python development, optimization, or advanced Python patterns.
model: opus
---

You are a Python expert specializing in modern Python 3.12+ development ...

## Purpose
## Capabilities   (Modern Python Features, Tooling, Testing, Performance, ...)
## Behavioral Traits
## Knowledge Base
## Response Approach   (1. Analyze requirements ... 8. Include deployment strategies)
## Example Interactions
```
Why it's good: description pins **specific versions and tools** (Python 3.12+, uv, ruff,
pydantic, FastAPI) so routing is precise; "Use PROACTIVELY for…" trigger; `model: opus` for
hard reasoning; a consistent section skeleton (Purpose → Capabilities → Behavioral Traits →
Response Approach → Example Interactions) that scales across the repo's ~194 agents
(https://github.com/wshobson/agents). Note it omits `tools`, inheriting all — acceptable for a
build-and-fix generalist, but a narrower agent should scope them.

### Example C — VoltAgent `backend-developer` (context-manager bootstrap)
Source: https://raw.githubusercontent.com/VoltAgent/awesome-claude-code-subagents/main/categories/01-core-development/backend-developer.md

```markdown
---
name: backend-developer
description: "Use this agent when building server-side APIs, microservices, and backend systems that require robust architecture, scalability planning, and production-ready implementation."
tools: Read, Write, Edit, Bash, Glob, Grep
model: sonnet
---

You are a senior backend developer specializing in server-side applications ...

When invoked:
1. Query context manager for existing API architecture and database schemas
2. Review current backend patterns and service dependencies
3. Analyze performance requirements and security constraints
4. Begin implementation following established backend standards
```
Why it's good: description leads with "Use this agent when…" (explicit trigger phrasing);
an explicitly scoped tool list appropriate to an implementer (adds `Write`/`Edit`); `sonnet`
tier; and a "When invoked" step 1 that **re-gathers context first**, directly compensating for
the fresh-context-window constraint (https://github.com/VoltAgent/awesome-claude-code-subagents).

Common threads across the best files: a one-line role identity ("You are a senior X"); a
numbered invoked-workflow that re-establishes state; scoped tools matched to read-only vs.
mutating roles; an explicit output/response contract; and a description whose first job is to
answer "when should I be picked?"

---

## 5. Orchestrator-Worker Prompt Lessons (Anthropic Multi-Agent Research)

Anthropic's Research feature uses an orchestrator-worker pattern: a lead agent decomposes a
query and spawns subagents that explore in parallel, each with its own context window, then
compresses findings back to the lead (https://www.anthropic.com/engineering/multi-agent-research-system).
The prompt-engineering lessons transfer directly to authoring worker agent files.

**Give every worker four things.** Each subagent needs "an objective, an output format,
guidance on the tools and sources to use, and clear task boundaries." Without them, "agents
duplicate work, leave gaps, or fail to find necessary information"
(https://www.anthropic.com/engineering/multi-agent-research-system). This is the direct
justification for the description-trigger + body-output-contract + scoped-tools structure above.
Their failure example: the vague instruction "research the semiconductor shortage" caused one
subagent to chase the 2021 auto-chip crisis while others looked at current supply chains, with
no division of labor (https://www.anthropic.com/engineering/multi-agent-research-system).

**Scale effort to query complexity.** Embed explicit resource-allocation rules — e.g. simple
fact-finding: 1 agent, 3-10 tool calls; comparisons: 2-4 subagents, 10-15 calls each; complex
research: 10+ subagents with divided responsibilities. This prevents overinvestment, "a common
failure mode in our early versions" (spawning 50 subagents for a simple query)
(https://www.anthropic.com/engineering/multi-agent-research-system,
https://simonwillison.net/2025/Jun/14/multi-agent-research-system/). The Claude Code `effort`
and `maxTurns` frontmatter fields are the file-level analog.

**The eight principles** (https://www.anthropic.com/engineering/multi-agent-research-system):
1. Think like your agents — build an accurate mental model; simulate to find failure modes.
2. Teach the orchestrator how to delegate — objectives, output formats, tool guidance, boundaries.
3. Scale effort to query complexity — explicit resource guidelines.
4. Tool design and selection are critical — give explicit heuristics (examine available tools
   first; match tool to intent).
5. Let agents improve themselves — models can diagnose failures and suggest prompt fixes.
6. Start wide, then narrow — counter the tendency toward overly specific queries.
7. Guide the thinking process — use extended thinking as a controllable scratchpad.
8. Parallel tool calling transforms speed — 3-5 subagents in parallel, 3+ tools each, cutting
   research time "by up to 90%."

Overall strategy: "instilling good heuristics rather than rigid rules" — encode how a skilled
human researcher decomposes questions, judges sources, and trades depth vs. breadth
(https://www.anthropic.com/engineering/multi-agent-research-system).

---

## 6. Codex CLI & AGENTS.md

Codex has two distinct concepts; don't conflate them.

### `AGENTS.md` — project instructions, not an agent definition
`AGENTS.md` is "a simple, open format for guiding coding agents" — a standard-Markdown file
holding setup/build commands, testing instructions, code style, and conventions
(https://agents.md/). It is **one instructions file per location that works with many agents,
not a file that defines agents.** "Codex reads `AGENTS.md` files before doing any work"
(https://developers.openai.com/codex/guides/agents-md). Discovery is hierarchical: global
(`~/.codex/AGENTS.override.md` then `AGENTS.md`), then walking the project root down to cwd,
checking `AGENTS.override.md` → `AGENTS.md` → configured fallbacks in each directory; closer
files override earlier guidance. Limits: default max 32 KiB (`project_doc_max_bytes`), empty
files skipped, at most one file per directory
(https://developers.openai.com/codex/guides/agents-md). In monorepos, "agents automatically
read the nearest file in the directory tree, so the closest one takes precedence"
(https://agents.md/). The standard is cross-tool: Codex, Google Jules, Cursor, Aider, VS Code,
GitHub Copilot all consume it (https://agents.md/). Rough Claude Code equivalent: `CLAUDE.md`,
not a subagent file.

### Codex custom agents / subagents — per-agent TOML
Closer to Claude Code subagents: standalone TOML files, one agent per file, in `~/.codex/agents/`
(personal) or `.codex/agents/` (project, higher precedence)
(https://developers.openai.com/codex/subagents). Required fields: `name` ("Agent name Codex uses
when spawning"), `description` ("Human-facing guidance for when Codex should use this agent"),
and `developer_instructions` (the behavioral system prompt). Optional (inherited from parent
when omitted): `model`, `model_reasoning_effort`, `sandbox_mode`, `mcp_servers`, `skills.config`,
`nickname_candidates` (https://developers.openai.com/codex/subagents).

Example (verbatim, https://developers.openai.com/codex/subagents):
```toml
name = "pr_explorer"
description = "Read-only codebase explorer for gathering evidence"
model = "gpt-5.3-codex-spark"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Stay in exploration mode.
Trace execution paths and avoid proposing fixes.
"""
```

Global orchestration knobs live under `[agents]` in the main config: `max_threads` (default 6),
`max_depth` (default 1, prevents recursive spawning), `job_max_runtime_seconds`
(https://developers.openai.com/codex/subagents).

### Key differences from Claude Code
- **Format:** Codex uses TOML with `developer_instructions` as a string field; Claude Code uses
  Markdown frontmatter + a Markdown body as the prompt
  (https://developers.openai.com/codex/subagents vs. https://code.claude.com/docs/en/sub-agents).
- **Delegation:** "Codex only spawns a new agent when you explicitly ask it to do so"
  (https://developers.openai.com/codex/subagents) — no automatic description-driven routing.
  Claude Code *auto-delegates* based on the `description`
  (https://code.claude.com/docs/en/sub-agents). So in Codex the `description` is human-facing
  guidance; in Claude Code it is the machine routing signal. (Note: Codex v0.142.0 added
  app-server multi-agent modes — disabled / explicit-request-only / proactive — but the CLI
  default remains explicit; https://developers.openai.com/codex/subagents.)
- **Sandboxing:** Codex bakes `sandbox_mode` into the agent; Claude Code uses `permissionMode`
  + `tools`/`disallowedTools` + hooks.
- **Portability:** wshobson/agents ships one Markdown source consumed by Claude Code, Codex,
  Cursor, OpenCode, Gemini CLI, and Copilot (https://github.com/wshobson/agents), so a
  well-written Markdown role body is broadly reusable even where the config wrapper differs.

---

## 7. Authoring Checklist

Claude Code agent file:
- [ ] `name`: lowercase-hyphenated, unique within scope.
- [ ] `description`: leads with the role, ends with an explicit trigger — "Use PROACTIVELY
      when…" / "Use immediately after…"; names concrete tasks/domains; specific, not generic.
- [ ] `tools`: scoped to the role. Read-only reviewer → `Read, Grep, Glob` (+`Bash` for git);
      implementer → add `Edit`/`Write`. Omit only for deliberate generalists.
- [ ] `model`: matched to difficulty — Haiku (cheap/high-volume), Sonnet (default), Opus
      (hard), or `inherit`. Consider `effort`/`maxTurns` for cost control.
- [ ] Body defines ONE role (single responsibility).
- [ ] Body opens with identity ("You are a senior X specializing in Y").
- [ ] Body has a numbered "When invoked" workflow that re-gathers context (assume nothing is
      inherited — fresh context window).
- [ ] Body states an explicit **output contract** ("return findings as…", priority buckets,
      required sections) — this is the only thing that returns to the caller.
- [ ] Restate any must-follow rule the agent can't otherwise see (e.g. dirs to ignore).
- [ ] Check the file into `.claude/agents/` for team sharing.

Codex custom agent (TOML): `name`, `description`, `developer_instructions` required; set
`model`, `model_reasoning_effort`, `sandbox_mode` explicitly; remember delegation is
explicit-only, so document *how to invoke* it (https://developers.openai.com/codex/subagents).
Keep project conventions in `AGENTS.md` (≤32 KiB), nearest-file-wins in monorepos
(https://developers.openai.com/codex/guides/agents-md, https://agents.md/).

---

## 8. Gaps, Confidence & Version Notes

- **High confidence** on Claude Code frontmatter and Codex TOML fields — both from official
  docs (code.claude.com, developers.openai.com), current as of 2026-07.
- Claude Code docs reference versions through v2.1.200; field set is stable but individual
  behaviors (e.g. background-by-default as of v2.1.198, Explore inheriting model as of
  v2.1.198) are version-gated — verify against your installed version
  (https://code.claude.com/docs/en/sub-agents).
- Codex multi-agent proactive delegation is newer/less mature than Claude Code's; v0.142.0
  introduced configurable delegation modes but CLI default is explicit
  (https://developers.openai.com/codex/subagents).
- Community collections (wshobson/agents ~194 agents; VoltAgent 100+) are strong pattern
  references but are community-maintained, not authoritative specs
  (https://github.com/wshobson/agents, https://github.com/VoltAgent/awesome-claude-code-subagents).
