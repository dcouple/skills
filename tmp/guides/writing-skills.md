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
description: "Cherry-picks a merged PR onto a release branch and opens the PR. Use when a fix needs back-porting — e.g. 'cherry-pick this to release'."
argument-hint: "[PR number] [release branch]"
disable-model-invocation: false
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
| `description` | ✅ | Third person, always-in-context metadata. **For model-invoked skills this is also the trigger**: include "Use when…" plus concrete trigger phrases — a skill nobody triggers is dead weight. For user-invoked skills (`disable-model-invocation: true`) the audience is the human: a one-line summary, **no trigger phrasing** — it can't fire on its own, so trigger text is wasted context. |
| `disable-model-invocation` | optional | `true` on skills a human must launch deliberately (release, destructive ops, the /do pipeline, the /create-* capture skills) so the model never fires them itself. |
| `argument-hint` | optional | Shown at invocation, e.g. `"[PR number]"`. Include only if the skill takes args; reference the input as `$ARGUMENTS` in the body. |
| `allowed-tools` | optional | Least-privilege patterns (`Bash(gh:*)`, not raw `Bash`) when a skill warrants a hard tool boundary. dcouple currently omits this field on all skills — rely on the body's stated boundaries instead; reintroduce per-skill only if a skill proves it needs the fence. |

Anything else (`when_to_use`, `arguments`, `context`, `user-invocable`) is **not** Claude Code frontmatter — don't emit it; fold triggers into `description`.

### Delegating heavy work

A skill runs inline in the caller's context. When a step is self-contained and bulky (a review sweep, a research pass), the skill should dispatch it to a sub-agent (see `writing-subagents.md`) so the exploration stays out of the main window; keep the skill itself inline where the user steers.

---

## 4. Body rules

### 4.1 Every step earns a **Success criteria**
Each step states *how we know it's done and can move on*. It defeats **premature completion** — the model declaring victory before the real artifact exists (a merged PR with green CI, not just "code written"). Prefer artifact-based criteria over effort-based ones.

**Exception — orchestrator-altitude skills.** A skill whose whole job is judgment (e.g. `/do`) states its gates in prose and trusts the orchestrating model to decide when each is met; per-step Success criteria are for procedural skills where drift is the risk.

### 4.2 Leave an artifact behind
Each phase should write something the next phase reads — a ticket, a spec in `./tmp/specs/`, a plan, a `context.md`, a `.business/` note, a wrap-up report. **No model should carry the whole project in its head.** Skills are links in a filesystem relay.

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
- [ ] `description` carries the trigger ("Use when…" + real phrases) on model-invoked skills; is a plain one-line summary on user-invoked ones.
- [ ] `disable-model-invocation` set correctly for human-only / destructive skills.
- [ ] Steps have Success criteria (artifact-based where possible) — except orchestrator-altitude skills, which state gates in prose.
- [ ] Human checkpoints exist before every irreversible action.
- [ ] The skill leaves a durable artifact for the next phase.
- [ ] Altitude respected — no implementation detail leaking into a high-level skill.
- [ ] `SKILL.md` is lean; heavy detail is in sibling reference/script files.
- [ ] Simple skills stayed simple — no ceremony that carries no information.
- [ ] `.codex` mirror updated if this skill runs in both harnesses.

---

## 8. Common mistakes

1. **Weak trigger in `description`** → the skill never fires. Most common failure. Fix the trigger first.
2. **Effort-based success criteria** ("wrote the code") → premature completion. Make them artifact-based ("PR open, CI green").
3. **Over-granular bodies** → line-level pseudo-code that a capable implementer doesn't need and that rots when the codebase moves. State decisions and shape, not keystrokes.
4. **Invented frontmatter** → fields Claude Code doesn't read (`when_to_use`, `context: fork`) silently do nothing.
5. **Altitude bleed** → a spec that lists files, a plan that re-argues the why. Keep layers clean.
6. **Bloated SKILL.md** → everything inline. Move detail to references; ship deterministic logic as scripts.
7. **No artifact left behind** → the next phase has to reconstruct context. Always write the handoff.

---

## 9. dcouple house rules (quick reference)

- The workflow is a **filesystem relay**: discussion → ticket → plan → implement → review → wrap-up, each leaving an artifact.
- The governing question at every gate: **"Is this clear enough to delegate?"** If no, discuss. If yes, capture, then execute.
- **Model routing is a first-class concern** — the canonical routing table lives in `tyler/README.md`; update it there first. In short: Fable orchestrates, Sonnet does legwork, Codex handles backend/ops implementation, backend verification, review & investigation, and the Claude `frontend-implementer` (Opus) / `frontend-verifier` (Sonnet) own frontend code, customer-facing copy, and in-app verification — never route those through Codex (the rule is enforced in the `codex` skill).
- **Don't author or edit a skill instruction without an observed failure behind it** — a postmortem finding, a failed run, or explicit user feedback. Speculative rules accumulate as permanent context tax.
