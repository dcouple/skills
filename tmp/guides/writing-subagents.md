# Writing Sub-Agents — Definitive Guide

> Audience: agents editing or creating sub-agent definitions in `dcouple/skills` (`*/​.claude/agents/<name>.md`).
> Companion docs: `writing-skills.md` (procedures), `writing-claude-md.md` (standing rules).

---

## 1. What a sub-agent is

A **sub-agent** is a `.claude/agents/<name>.md` file: **frontmatter** + a **system prompt**. When a skill or the main session calls it (via the Task tool), it runs in **its own context window**, does **one job**, and returns a **result** to the caller.

The purpose is separation of concerns and context hygiene:
- **Keep specialized work — and its token cost — out of the main session.** The orchestrator gets the conclusion, not the file dumps.
- **Put fresh eyes on the work.** A reviewer that didn't write the code has different blind spots.
- **Route the job to the right model.** Cheap models for legwork, expensive models for judgment.

If a job is a quick lookup you're confident about, don't spawn an agent — just do it. Sub-agents are for work that is *substantial, self-contained, or benefits from a fresh/different reader*.

---

## 2. Anatomy of an agent file

```markdown
---
name: plan-reviewer
description: Reviews implementation plans for gaps, simplification opportunities, architectural soundness, and brief fidelity. Automatically invoked by the plan skill after plan creation.
tools: Glob, Grep, Read
model: opus
color: yellow
---

You are a plan reviewer. Your job is to evaluate reconciled implementation
plans and produce a numbered list of specific, actionable recommendations.

You are **not** the user-facing coordinator. Do not ask the user direct
questions mid-review; surface unresolved decisions as labeled recommendations
for the parent workflow to aggregate.

## What You Review
1. Repo accuracy — do referenced files actually exist?
2. Completeness — missing error handling, edge cases, integration points?
3. Correctness — will this approach actually work?
...

## Output Format
Return a numbered list. Each item: **What** · **Where** · **Suggestion**.
Order by severity.
```

---

## 3. Frontmatter field reference

| Field | Required | Rules |
|---|---|---|
| `name` | ✅ | Kebab-case, matches the filename. This is the `subagent_type`. |
| `description` | ✅ | **Written as a trigger** — *when to use me*, not a feature list. Include "Automatically invoked after…" if a skill calls it on a fixed cadence. This is how the orchestrator selects it. |
| `tools` | ✅ | **Least privilege.** List only what the job needs. Reviewers get read-only (`Glob, Grep, Read`); explorers get read tools; only implementers get write/execute. |
| `model` | ✅ | Route to the task — see §5. `sonnet` / `opus` / (Fable in the main seat). |
| `color` | optional | UI affordance; pick a stable color per role. |

---

## 4. The four decisions that make an agent good

### a. One job, sharp edges
Each agent does a single thing — explore, research, implement, review, adversary. A narrow charter is what lets the caller trust the output without re-reading everything it touched. If you're tempted to give an agent two jobs, make two agents.

### b. Model to the task (§5)
Don't spend Opus/Fable on legwork; don't spend Sonnet on the judgment that changes the outcome.

### c. Least-privilege tools
Grant only what the job needs. **Reviewers must be read-only** (`Glob, Grep, Read`) so they physically cannot "fix" what they're meant to critique — separation of implementing and judging is the whole point.

### d. A described trigger + a fixed output contract
- The `description` tells the orchestrator *when* to call it.
- The body must end with a **fixed output format** so the calling skill can consume the result deterministically. Our reviewers all return "a numbered list ordered by severity."

---

## 5. Model routing (dcouple)

Route by *what the job demands*, not by habit. This is our real differentiator — most public libraries never pick a different model per stage.

| Role | Model | Why |
|---|---|---|
| Orchestrate / judge (Overseer: discussion, spec, plan judgment, running `/do`) | **Fable** (main session) | Best for ambiguous, open-ended reasoning. Opus is an acceptable fallback. |
| Legwork: explore codebase, web research, drive the running app (Code Researcher, Web Researcher, App user) | **Sonnet** | Cheap, fast; returns file:line refs / cited findings / verification evidence. |
| Review & investigation (Plan Reviewer, Code Reviewer, Investigator) | **GPT-5.5 high via `codex exec`** | Sharper reading where it changes the outcome; independent (non-Claude) eyes on Claude-authored plans. Opus placeholder until Phase 2. |
| Implement | **GPT-5.5 medium via `codex exec`** | The engineering workhorse — strong enough for a well-planned diff, cheap enough for long windows. High effort is the review lane, not the implement lane. Opus placeholder / Claude-side fallback. |

**Spend the expensive lanes sparingly** — save Fable for judgment and Codex high for the review/investigation loops where sharper reading changes the outcome. Never route customer-facing copy through Codex.

---

## 6. Body structure (system prompt)

A good agent body has a repeatable shape:

1. **Role line** — "You are a plan reviewer." One sentence.
2. **Boundaries** — what it is *not* (e.g. "not the user-facing coordinator"), and whether it may spawn its own sub-agents (default: **no, unless the parent explicitly said so** — depth explosions run away with context and cost).
3. **Methodology** — what to do, in order. Number it. For reviewers, an ordered checklist of what to inspect.
4. **Rules** — hard musts/must-nots; the failure modes to avoid.
5. **Output format** — the exact structure the result must take, so the caller can parse it.

---

## 7. The dcouple review pattern (important)

The highest-leverage pattern in our loop is **fresh-context readers who did not write the code**:

- A read-only GPT-5.5 **high** Code Reviewer reviews the diff (correctness + security); Fable — which conducted but didn't write — judges the report and runs the loop until **zero Must Fix** (cap 3 passes).
- Different model → different blind spots: Codex reviews Claude-planned work, Fable arbitrates Codex-implemented work.
- Review **loops back to implementation** until intent, plan, diff, and runtime behavior all agree.
- Parsa's variant adds a `business-research-adversary` — an agent whose entire job is to argue *against* the artifact.

When writing a reviewer agent: make it read-only, make it fresh-context (it reads the issue/plan/diff cold), and make it return severity-ordered findings — never let it "fix and move on."

---

## 8. Return-value discipline

The agent's final message *is* the tool result the caller receives — the user does not see it directly. So:
- **Return the conclusion, not the transcript.** Share file paths (absolute), load-bearing snippets only, and the structured output the caller expects.
- **Don't write report `.md` files** as the deliverable unless asked — the parent reads your text output.
- Match the output contract in your body exactly.

---

## 9. Quality checklist

- [ ] `name` matches the filename; kebab-case.
- [ ] `description` reads as a *trigger* ("Use when…" / "Automatically invoked after…").
- [ ] `tools` is least-privilege; reviewers/explorers are read-only.
- [ ] `model` routed to the task per §5 (cheap for legwork, expensive for judgment).
- [ ] Body has: role line · boundaries · ordered methodology · rules · **fixed output format**.
- [ ] Agent is told whether it may spawn sub-agents (default: no).
- [ ] Reviewer agents are fresh-context and cannot write.
- [ ] Output contract matches what the calling skill parses.

---

## 10. Common mistakes

1. **Two jobs in one agent** → untrustworthy output. Split it.
2. **Write access on a reviewer** → it "helpfully" fixes instead of flagging; you lose the independent read.
3. **Vague `description`** → the orchestrator can't decide when to call it.
4. **No output contract** → the calling skill can't reliably consume the result.
5. **Over-spending models** → Opus/Fable on legwork, or Sonnet on the judgment that decides the outcome.
6. **Uncontrolled sub-agent spawning** → depth explosions; cost and context blow up. Default to no self-spawning.
7. **Returning the transcript** → dumping everything read into the caller's context defeats the point of a sub-agent.

---

## 11. Our target roster (the Orchestra — Phase 1 builds Claude placeholders)

Overseer = **Fable**, in the main session (not an agent file). Target model per the
roadmap diagram; "placeholder" = the Claude model standing in until the Phase-2
`codex exec` swap.

| Agent | Target model | Placeholder | Tools | Job |
|---|---|---|---|---|
| `code-researcher` | Sonnet | — | Read, Grep, Glob, LS | Locate files & patterns; return file:line refs |
| `web-researcher` | Sonnet | — | web + read | Cited research dossiers for new tech |
| `app-user` | Sonnet | — | computer-use | Drive the running app; verify against criteria |
| `implementer` | GPT-5.5 **medium** | Opus | all tools | Write the diff per the plan; update plan.md |
| `plan-reviewer` | GPT-5.5 **high** | Opus | Glob, Grep, Read | Audit plans for gaps & brief fidelity |
| `code-reviewer` | GPT-5.5 **high** | Opus | read-only | Diff review incl. security; Must/Should/Nice findings |
| `investigator` | GPT-5.5 **high** | Opus | read + run | Reproduce & root-cause bugs |
| `business-*` (Parsa) | Claude | — | varies | Business context, spec/artifact review, research adversary |
