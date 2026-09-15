---
name: idea-duel
description: Generate and cross-evaluate project ideas with independent Claude and Codex participants, producing a ranked report and local draft work items.
argument-hint: "[project or area to ideate on, plus any focus or constraints]"
---

# Idea Duel - lean dueling wizards

Single-model brainstorming has one flaw that matters: the model that generates
an idea also evaluates it. The duel splits those jobs across the two stacks
and makes **convergence the quality signal** - where two differently-biased
models agree blind, investigate that agreement alongside their evidence. Agreement is a signal, not proof. The normal workflow uses four dispatches.

## Wizards (pinned)

- **Claude wizard**: sub-agent, `model: opus`, thinking/high effort.
- **Codex wizard**: dispatched directly via Bash (timeout 600000 ms) -
  `codex exec -m gpt-5.6-sol -c model_reasoning_effort="low" --sandbox
  read-only --ephemeral --skip-git-repo-check -C <repo root> -o
  <scratchpad>/codex-idea-wizard-<n>.md "<prompt>"`. Each dispatch is a fresh
  session that knows nothing of this conversation - the prompt carries the
  brief and names both files below by **absolute path**; Codex reads them
  itself.
- Both follow `references/instructions.md` (stack-neutral) and write the
  formats in `references/idea-wizard-output.md` - both under this skill's
  base directory.
- If a participant degrades (fallback model, truncated output), retire it and
  report a single-wizard result honestly - never contaminate scoring.

## Phases

0. **Frame** (orchestrator, no dispatch): one-paragraph brief - the project,
   the focus, and the ACTUAL constraints (scale, maturity, appetite); artifact
   dir `./tmp/idea-duel/<slug>/`. An honest brief is most of the value: omit
   the real constraints and you buy ideas tuned to someone else's context.
1. **Generate** (2 dispatches, parallel, blind): each wizard independently
   studies the project → generates ~10 candidate ideas → self-winnows to a
   top 3, self-ranked with reasoning → writes `ideas-<stack>.md`. Neither
   sees the other.
2. **Cross-score + blind-spot probe** (2 dispatches, parallel): each wizard
   gets the brief and BOTH idea files, and - before seeing any scores -
   scores the opponent's 3 (0–1000, one-line verdict each; the number is a
   commitment device, not a measurement) and nominates blind spots: the
   strongest idea NEITHER list contains. Writes `scores-<stack>.md`.
3. **Synthesis** (orchestrator, no dispatch): assemble the matrix - idea ×
   self-rank × opponent score × verdict - and classify:
   - **consensus** (opponent score ≥ 800, or both stacks listed the same
     theme): winners;
   - **contested** (self-ranking and the opponent's reasoning materially disagree): resolve by
     staging ("yes, but v1 first") or, for a consequential design fork, flag for the
     `dialectic` skill rather than settling it here;
   - **killed**: neither side defends it - drop with one line of why.
   Check the blind-spot nominations for convergence - two stacks
   independently nominating the same missing idea is the strongest signal the
   duel produces; promote it to the winners regardless of the matrix. Emit
   `DUEL_REPORT.md`: the matrix, the reasoning, and a dependency-ordered
   sequence (enablers first). Winners become `status: draft` work items under
   `./tmp/<idea-slug>/item.md`, each carrying its duel evidence - both
   scores, the verdict line, and what it beat - pre-seeded into the item's
   Justification and `refs/` (link `DUEL_REPORT.md`). Use an existing work-item format when provided. Drafts do not authorize ticket creation or implementation; pass them through the project's normal decision gate.

## Rules

- Wizards are read-only toward the repo: cite, never edit. No dispatch sees
  the opponent's scores before its own are written.
- The orchestrator never adds its own ideas to the matrix - it frames,
  synthesizes, and judges; generation belongs to the wizards.
- Every idea in the report carries its origin, both numbers, and the verdict -
  survivors must be traceable back through the duel.

## Grain handoff

- If connected, save briefs, idea files, scores, reports, and drafts in the supplied task folder, or `Development Artifacts/YYYY-MM-DD-<task>`; pass its ID/storage rule without revealing peer ideas or scores early.
- Sync outputs for participants without access, keep needed local files and privacy limits, and continue locally silently without Grain.
- Pass CLI prompts as data, not interpolated shell source; verify requested models are available before dispatch.
