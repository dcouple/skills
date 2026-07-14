---
name: idea-duel
description: Lean dueling-wizards ideation tournament — the two model stacks independently study a project, generate and winnow ideas, blind cross-score each other's, and probe for shared blind spots; the orchestrator synthesizes a consensus matrix whose winners become draft work items. Use when the user wants the strongest next ideas for a project ("what should we build next", "run an idea duel", "most valuable improvements"). Four dispatches, discretionary quota spend — an upstream generator feeding the capture pipeline, typically offered from /discussion; never part of /do.
argument-hint: "[project or area to ideate on, plus any focus or constraints]"
---

# Idea Duel — lean dueling wizards

Single-model brainstorming has one flaw that matters: the model that generates
an idea also evaluates it. The duel splits those jobs across the two stacks
and makes **convergence the quality signal** — where two differently-biased
models agree blind, the idea is probably good; where they trash each other's,
it's suspect. Four dispatches, ~100k tokens at the pinned efforts — about one
review pass.

## Wizards (pinned)

- **Claude wizard**: sub-agent, `model: opus`, thinking/high effort.
- **Codex wizard**: dispatched directly via Bash (timeout 600000 ms) —
  `codex exec -m gpt-5.6-sol -c model_reasoning_effort="low" --sandbox
  read-only --ephemeral --skip-git-repo-check -C <repo root> -o
  <scratchpad>/codex-idea-wizard-<n>.md "<prompt>"`. Each dispatch is a fresh
  session that knows nothing of this conversation — the prompt carries the
  brief and names both files below by **absolute path**; Codex reads them
  itself.
- Both follow `references/instructions.md` (stack-neutral) and write the
  formats in `references/idea-wizard-output.md` — both under this skill's
  base directory.
- If a participant degrades (fallback model, truncated output), retire it and
  report a single-wizard result honestly — never contaminate scoring.

## Phases

0. **Frame** (orchestrator, no dispatch): one-paragraph brief — the project,
   the focus, and the ACTUAL constraints (scale, maturity, appetite); artifact
   dir `./tmp/idea-duel/<slug>/`. An honest brief is most of the value: omit
   the real constraints and you buy ideas tuned to someone else's context.
1. **Generate** (2 dispatches, parallel, blind): each wizard independently
   studies the project → generates ~10 candidate ideas → self-winnows to a
   top 3, self-ranked with reasoning → writes `ideas-<stack>.md`. Neither
   sees the other.
2. **Cross-score + blind-spot probe** (2 dispatches, parallel): each wizard
   gets the brief and BOTH idea files, and — before seeing any scores —
   scores the opponent's 3 (0–1000, one-line verdict each; the number is a
   commitment device, not a measurement) and nominates blind spots: the
   strongest idea NEITHER list contains. Writes `scores-<stack>.md`.
3. **Synthesis** (orchestrator, no dispatch): assemble the matrix — idea ×
   self-rank × opponent score × verdict — and classify:
   - **consensus** (opponent score ≥ 800, or both stacks listed the same
     theme): winners;
   - **contested** (score delta from self-rank expectation ≥ 250): resolve by
     staging ("yes, but v1 first") or, when genuinely zone 0–1, flag for the
     `dialectic` skill rather than settling it here;
   - **killed**: neither side defends it — drop with one line of why.
   Check the blind-spot nominations for convergence — two stacks
   independently nominating the same missing idea is the strongest signal the
   duel produces; promote it to the winners regardless of the matrix. Emit
   `DUEL_REPORT.md`: the matrix, the reasoning, and a dependency-ordered
   sequence (enablers first). Winners become `status: draft` work items under
   `./tmp/<idea-slug>/item.md`, each carrying its duel evidence — both
   scores, the verdict line, and what it beat — pre-seeded into the item's
   Justification and `refs/` (link `DUEL_REPORT.md`). The Socratic gate then
   serves as the tournament's third adversarial filter, and calibrates down
   accordingly: an item with documented duel evidence earns a fast pass
   unless its premise has a hole the duel never tested.

## Rules

- Wizards are read-only toward the repo: cite, never edit. No dispatch sees
  the opponent's scores before its own are written.
- The orchestrator never adds its own ideas to the matrix — it frames,
  synthesizes, and judges; generation belongs to the wizards.
- Every idea in the report carries its origin, both numbers, and the verdict —
  survivors must be traceable back through the duel.
