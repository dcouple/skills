# Writing Skills — Definitive Guide

> Audience: agents editing or creating skills in `dcouple/skills` (`*/​.claude/skills/<name>/SKILL.md` and the `.codex` mirror).
> This guide is authoritative for *how a skill should be shaped*. When it conflicts with a specific skill's own local README, prefer the local README, then this guide.

---

## 1. What a skill is (and is not)

A **skill** is a reusable *procedure*: a `SKILL.md` file (plus optional supporting files) that tells a model **when to act, what it may touch, and the ordered steps to produce a defined artifact.**

- A skill is **the procedure**. A sub-agent (see `writing-subagents.md`) is **who runs it or a piece of it**. A `CLAUDE.md` (see `writing-claude-md.md`) is **the standing rules the procedure must obey**.
- A skill exists to **wrangle determinism out of a stochastic system** — the value is a *predictable process every run*, not a predictable output. If a task is already reliable ad-hoc, it does not need a skill.

**Do not write a skill when:** the task is a one-off, the "procedure" is a single obvious action, or the instructions would just restate what any competent model already does. Skills are for the moments that *repeat* and where *drift is costly*.

---

## 2. Anatomy of a SKILL.md

Two parts: **frontmatter** (controls discovery, invocation, permissions) and **body** (the procedure). This is the dcouple house template, derived from `skillify`:

```markdown
---
name: cherry-pick-release
description: "One-line summary of what this skill does."
when_to_use: "Use when <trigger>. Examples: '<phrase 1>', '<phrase 2>', '<phrase 3>'."
allowed-tools:
  - Read
  - Edit
  - Bash(git:*)
  - Bash(gh:*)
user-invocable: true
disable-model-invocation: false
argument-hint: "[PR number] [release branch]"
arguments:
  - pr_number
  - release_branch
context: fork          # omit for inline; set 'fork' for self-contained runs
---

# Cherry-Pick to Release

One or two sentences on the goal and shape of this workflow.

## Inputs
- `$pr_number`: the merged PR to cherry-pick
- `$release_branch`: the target release branch

## Goal
A clearly stated goal with a **defined completion artifact** — e.g.
"an open cherry-pick PR against $release_branch with CI green," not
just "cherry-pick the commit."

## Steps

### 1. Locate the merge commit
What to do, specifically. Include the exact command.

**Success criteria**: the commit SHA is identified and confirmed to be on main.

### 2. Create the cherry-pick branch and apply
...

**Success criteria**: commit applies cleanly (or conflicts are surfaced to the human).
**Human checkpoint**: pause here if there are merge conflicts.

### 3a. Open the PR    ### 3b. Post the link to Slack   # sub-numbers = parallel
...
```

---

## 3. Frontmatter field reference

| Field | Required | Purpose & rules |
|---|---|---|
| `name` | ✅ | Kebab-case, matches the directory name. This is the `/name` invocation. |
| `description` | ✅ | One line, third person, what it does. Kept short — it's always-in-context metadata. |
| `when_to_use` | ✅ (critical) | **The trigger.** How the model decides to auto-invoke. Start with `"Use when…"` and include concrete trigger phrases and example user messages. A skill nobody triggers is dead weight. |
| `allowed-tools` | ✅ | **Least privilege, as patterns.** Prefer `Bash(gh:*)` over raw `Bash`. Grant only what the steps actually use. This bounds the blast radius. |
| `user-invocable` | optional | `true` if a human runs it as a `/command`. |
| `disable-model-invocation` | optional | `true` on skills a human must launch deliberately (release, destructive ops, skillify) so the model never fires them itself. |
| `argument-hint` | optional | Shown at invocation, e.g. `"[PR number]"`. Include only if the skill takes args. |
| `arguments` | optional | List of arg names; reference as `$name` in the body. |
| `context` | optional | `fork` = run as a self-contained sub-agent with its own context (no mid-run steering). Omit (inline) when the user should steer as it goes. **Decision rule below.** |

### `context: fork` vs inline — the decision

- **fork** when the task is self-contained, deterministic, and needs no human input mid-run (e.g. a review sweep, a research pass, a codegen batch). Keeps the work out of the main context window.
- **inline** when the user wants to steer, approve, or redirect partway (e.g. discussion, spec drafting, anything with judgment calls or irreversible actions).

---

## 4. Body rules

### 4.1 Every step earns a **Success criteria** — non-negotiable
This is the single most important dcouple convention. Each step states *how we know it's done and can move on*. It defeats **premature completion** — the model declaring victory before the real artifact exists (a merged PR with green CI, not just "code written"). Prefer artifact-based criteria over effort-based ones.

### 4.2 Leave an artifact behind
Each phase should write something the next phase reads — a ticket, a spec in `./tmp/specs/`, a plan, a `context.md`, a `.business/` note, a teach-back. **No model should carry the whole project in its head.** Skills are links in a filesystem relay.

### 4.3 Per-step annotations — use only where they carry information
- **Execution**: `Direct` (default) · `Task agent` (straightforward sub-agent) · `Teammate` (true parallelism / inter-agent comms) · `[human]` (user does it).
- **Artifacts**: data a later step depends on (PR #, commit SHA, file path). Include only when there's a real dependency.
- **Human checkpoint**: pause before irreversible actions (merge, send, delete), on error judgment (conflicts), or for output review.
- **Rules**: hard musts/must-nots for this workflow. Corrections a human made during the reference session are gold here.

### 4.4 Keep simple skills simple
A two-step skill does not need annotations on every line. Add structure only where it earns its keep. Sub-numbered steps (`3a`, `3b`) mark work that can run concurrently; `[human]` in a step title marks user action.

### 4.5 Respect altitude
Do not let a high-level skill leak low-level detail. A **spec** skill produces *what & why + phases*; a **plan** skill produces *how* (files, ordered tasks, verification). From `create-spec`: specs must **not** contain file lists, pseudo-code, task sequences, or version numbers — those belong one layer down. A skill that respects its own altitude beats three that blur it.

### 4.6 Progressive disclosure
Keep `SKILL.md` lean (aim well under ~500 lines). Push heavy detail — long references, big examples, lookup tables — into sibling files in the skill directory (`reference.md`, `template.md`, `scripts/`), loaded only when needed. Ship deterministic work as **scripts to be executed, not prose to be read into context.**

---

## 5. Writing style

- **Imperative voice.** "Extract the SHA", "Run the typecheck" — not "you might want to."
- **Explain the *why* where it matters.** A model that understands *why* a rule exists ("migrations are handled by `/implement` after review, so don't run `db:diff` yourself") holds up on edge cases better than one following a bare command. Reserve hard "NEVER"s for genuine failure modes; a page full of ALL-CAPS musts is a yellow flag and burns trust and tokens.
- **Trust the model on mechanics, constrain it on process.** Frontier implementers do not need line-level code. They need the decisions, constraints, the ordered shape, and the success bar. Give those; omit boilerplate.
- **Leading words.** Anchor behavior with tight, pretraining-resident concepts (a *tight* loop, *red* before green, a *tracer bullet*, a *seam*) instead of long paragraphs.

---

## 6. Cross-harness (Codex) mirror

Skills we run through Codex ship a tiny interface file alongside them:

```yaml
# .codex/skills/<name>/agents/openai.yaml
interface:
  display_name: "PR Test Automation"
  short_description: "Automate first-pass PR manual QA"
  default_prompt: "Use $pr-test-automation to validate this PR as much as possible before manual human testing."
```

Keep `.claude` and `.codex` variants in sync in shape; the body procedure should be equivalent.

---

## 7. Quality checklist (run before saving)

- [ ] `name` matches the directory; kebab-case.
- [ ] `when_to_use` starts with "Use when…" and lists real trigger phrases.
- [ ] `allowed-tools` is minimal and uses patterns (`Bash(gh:*)`), not blanket grants.
- [ ] `disable-model-invocation` set correctly for human-only / destructive skills.
- [ ] `context: fork` only on self-contained, no-steering skills.
- [ ] **Every step has a Success criteria**, and criteria are artifact-based where possible.
- [ ] Human checkpoints exist before every irreversible action.
- [ ] The skill leaves a durable artifact for the next phase.
- [ ] Altitude respected — no implementation detail leaking into a high-level skill.
- [ ] `SKILL.md` is lean; heavy detail is in sibling reference/script files.
- [ ] Simple skills stayed simple — no ceremony that carries no information.
- [ ] `.codex` mirror updated if this skill runs in both harnesses.

---

## 8. Common mistakes

1. **Weak `when_to_use`** → the skill never fires. Most common failure. Fix the trigger first.
2. **Effort-based success criteria** ("wrote the code") → premature completion. Make them artifact-based ("PR open, CI green").
3. **Over-granular bodies** → line-level pseudo-code that a capable implementer doesn't need and that rots when the codebase moves. State decisions and shape, not keystrokes.
4. **Blanket tool grants** → `Bash` instead of `Bash(git:*)`. Widens blast radius for no reason.
5. **Altitude bleed** → a spec that lists files, a plan that re-argues the why. Keep layers clean.
6. **Bloated SKILL.md** → everything inline. Move detail to references; ship deterministic logic as scripts.
7. **No artifact left behind** → the next phase has to reconstruct context. Always write the handoff.

---

## 9. dcouple house rules (quick reference)

- The workflow is a **filesystem relay**: discussion → ticket → plan → implement → review → teach-back, each leaving an artifact.
- The governing question at every gate: **"Is this clear enough to delegate?"** If no, discuss. If yes, capture, then execute.
- **Model routing is a first-class concern** — skills may delegate steps to specific models (Sonnet for legwork: explore / research / app-driving; GPT-5.5 **high** via `codex exec` for review & investigation; GPT-5.5 **medium** for implement; Fable for orchestration & judgment). See `writing-subagents.md` §5.
- Never route customer-facing copy through Codex; that's a Claude job.
