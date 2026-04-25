---
name: create-spec
description: Creates a high-level specification with a phases table that maps to implementation plans. The spec is stateful — phases are checked off as plans are created from them. Use when scoping a feature large enough to need multiple plans, or when you want a human-readable architectural artifact above implementation.
argument-hint: "[feature or system to spec]"
allowed-tools: Read, Grep, Glob, WebFetch, WebSearch, Write, Edit, Task
---

# Create Spec Agent

## Feature: $ARGUMENTS

Generate a complete specification: a human-readable artifact capturing problem, approach, architectural decisions, and a phases table where each row becomes its own implementation plan.

## CRITICAL: No Implementation Details

Specs are the layer **above** plans. They must NOT contain:
- File lists or directory trees
- Pseudo-code or code snippets
- Task sequences or step-by-step instructions
- Library version numbers or dependency lists

Those belong in the downstream plans produced by `/create-plan` from each phase row. The spec captures *what and why*; the plan captures *how*.

## Step 1: Research (Only If Needed)

If the approach is **genuinely unclear**, ask the user 1-3 targeted design questions. Otherwise, proceed.

### Codebase Analysis (light)
- Identify existing patterns and tech choices the spec must respect
- Note system boundaries the spec will affect

### External Research
- Library / approach docs only when introducing new tech
- Skip implementation specifics — they belong in plans, not specs

## Step 2: Write the Spec

Use `./spec_base.md` (in this skill's directory) as the template.

### Spec Guidelines

- **Audience is human-first** — a teammate or future-you should understand what's being built and why without scanning code
- **Phases must be independently plannable** — each row of the phases table needs enough scope info that a fresh-context `/create-plan` run can produce a working plan from it alone
- **Phase dependencies are explicit** — if Phase 3 needs Phase 1's output, the "Depends on" cell says so
- **Flag uncertainty** — `[NEEDS CLARIFICATION]` markers must be resolved before phases are picked up

## Step 3: Save the Spec

Save as: `./tmp/specs/YYYY-MM-DD-description.md`

Specs live in `./tmp/specs/` permanently. They are stateful — checkboxes track which phases have had plans created from them. Specs are never moved between folders.

## Step 4: Review and Present

Spawn one automatic review pass.

1. **Spawn a plan-reviewer sub-agent** with spec-specific guidance:

```
Task tool:
  subagent_type: "plan-reviewer"
  prompt: "Review the SPEC at [path]. This is a high-level spec, not an
    implementation plan. Focus on:
    - Are problem, approach, and architectural decisions clear?
    - Are non-goals / no-gos explicit?
    - Are unresolved [NEEDS CLARIFICATION] markers flagged?
    - **Phases table:** Are phases independently plannable from this spec
      alone? Are dependencies between phases explicit? Is scope balanced
      across phases? Are any phases too large or too small?
    - Does anything in the spec leak implementation detail (file paths,
      pseudo-code, task sequences) that should be deferred to plans?
    Produce a numbered list of specific, actionable recommendations."
```

2. **Triage and apply.** Split reviewer recommendations into two buckets:
   - **Auto-fixable** — Apply silently to the spec.
   - **Needs user input** — Surface to the user.

3. **Present:**

   **a) Spec Summary** — 3-5 bullets covering what the spec is and how many phases it breaks into.

   **b) Questions for You** — Only reviewer recommendations needing user input. For each: the question + brief context.

   If feedback was minor and auto-fixed: "Reviewer feedback was minor and has been incorporated."

   **c) Spec Link:**
   ```
   Spec: ./tmp/specs/[filename]
   ```

   **d) Next step prompt** — Always end with: "Want to run another review pass, or is this ready to plan from?"

4. **If user wants changes:** apply, spawn fresh reviewer, repeat.

5. **If user says ready** → proceed to Step 5.

## Step 5: Return — DO NOT IMPLEMENT, DO NOT PLAN

Once approved, tell the user:

```
Spec finalized! To start working from this spec:

1. Clear context: /clear
2. Run: /create-plan
   (auto-detects the spec, picks the first unchecked phase, marks it,
    and produces a plan for it)

To target a specific phase: /create-plan "Phase N"
To target a specific spec:  /create-plan ./tmp/specs/[filename]
```

**CRITICAL: Your job ends here.** Do NOT start writing plans. Do NOT spawn `/create-plan`. Do NOT write or modify application code. The `/create-spec` skill only produces a spec file.

## Quality Checklist

- [ ] Problem is concrete (a specific scenario, not abstract)
- [ ] Appetite is set (S/M/L or week-count)
- [ ] Approach captures key technologies and system boundaries
- [ ] Architectural decisions documented with rationale and trade-offs
- [ ] No-gos are explicit
- [ ] Phases table present with all columns (`✓`, `#`, Phase, Goal, Scope, Out of scope, Depends on, Key files/modules, Size)
- [ ] Every phase row's `✓` cell is `[ ]` (unchecked at creation time)
- [ ] Each phase row contains enough scope to be planned independently
- [ ] Phase dependencies are marked
- [ ] No unresolved `[NEEDS CLARIFICATION]` markers
- [ ] No implementation details leaked (file lists, pseudo-code, task sequences)

## Spec Lifecycle

- **All specs**: `./tmp/specs/` (single folder, no moving — specs are stateful)
- Checkboxes in the phases table track which phases have had plans created
- A "complete" spec has all phases checked, but the file stays for reference
