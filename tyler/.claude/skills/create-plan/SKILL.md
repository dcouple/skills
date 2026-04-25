---
name: create-plan
description: Creates an implementation plan with thorough codebase and web research. Auto-detects active specs in ./tmp/specs/ and picks the next unchecked phase if no feature description is given. Auto-reviews the plan after creation and iterates with user feedback. Use when planning a new feature or significant change.
argument-hint: "[feature description, ticket reference, spec path, or empty for auto-spec mode]"
allowed-tools: Read, Grep, Glob, WebFetch, WebSearch, Write, Edit, Bash, Task
---

# Create Plan Agent

## Feature: $ARGUMENTS

Generate a complete plan for feature implementation with thorough research. The plan must contain enough context for an AI agent to implement the feature in a single pass.

## Step 0: Detect Spec Mode

Before treating `$ARGUMENTS` as a feature description, check whether a spec drives this plan.

1. **List specs:** Run `ls ./tmp/specs/*.md 2>/dev/null` to find available specs.

2. **Routing:**
   - **`$ARGUMENTS` is a path to a file in `./tmp/specs/`** → spec mode, that spec, first unchecked phase.
   - **`$ARGUMENTS` looks like `Phase N` or `phase N`** → spec mode. If exactly one spec exists with that phase unchecked, use it. If ambiguous, ask the user.
   - **`$ARGUMENTS` includes both a spec path AND a phase reference** (e.g. `./tmp/specs/2026-04-25-foo.md "Phase 2"`) → spec mode, that spec, that phase.
   - **`$ARGUMENTS` is empty AND exactly one spec exists with at least one unchecked phase** → spec mode, that spec, first unchecked phase.
   - **`$ARGUMENTS` is empty AND multiple specs have unchecked phases** → list them, ask the user to pick.
   - **`$ARGUMENTS` is empty AND no spec has unchecked phases** → ask the user what to plan.
   - **Otherwise** (clear feature description that isn't a spec path or phase reference) → direct mode, proceed to Step 1 with `$ARGUMENTS` as the feature.

3. **In spec mode:**

   a. **Read the full spec.** You need its problem, approach, architectural decisions, and the target phase row + its `### Phase N: <name>` notes (if present).

   b. **Identify the target phase.** Find the row in the phases table where the `✓` column is `[ ]` (or the explicitly-named phase).

   c. **Mark the checkbox immediately**, before writing the plan, to prevent double-picking if interrupted. Use the Edit tool:
      - `old_string`: `| [ ] | <phase#> |` (the leading cells of that row — phase number makes it unique)
      - `new_string`: `| [x] | <phase#> |`

      If the unique-string match fails (e.g. the row was hand-edited), include more of the row in `old_string` to disambiguate. Do not skip this step.

   d. **Construct the "feature" for downstream steps** as: the phase's Goal + Scope + the spec's Problem and relevant Architectural Decisions. Treat the spec as the source of truth for *why* and *what*; your plan answers *how* for this one phase.

   e. **The plan file MUST reference the source spec at the top**, e.g.:
      ```
      > Plan for **Phase N: <name>** of [spec](../specs/YYYY-MM-DD-name.md).
      ```

   Then continue with Step 1.

## Step 1: Research (Only If Needed)

If the approach is **genuinely unclear**, ask the user 1-3 targeted design questions. Otherwise, proceed directly.

### Codebase Analysis
- Search for similar features/patterns in the codebase
- Identify files to reference in the plan
- Note existing conventions to follow

### External Research
- Library documentation (include specific URLs)
- Implementation examples
- Best practices and common pitfalls

## Step 2: Write the Plan

Using `./plan_base.md` (in this skill's directory) as template.

### Critical Context to Include

The AI agent only gets the context in the plan plus codebase access. Include:
- **Documentation**: URLs with specific sections
- **Code Examples**: Real snippets from codebase
- **Gotchas**: Library quirks, version issues
- **Patterns**: Existing approaches to follow

### Implementation Blueprint

- Start with pseudocode showing approach
- Reference real files for patterns
- Include error handling strategy
- List tasks in implementation order

### Plan Guidelines

- **Required Sections** (never leave empty): Files Being Changed (tree with ← NEW / ← MODIFIED markers), Architecture Overview (proportional to complexity), Key Pseudocode (hot spots and tricky logic only), and Tasks (concrete file-level steps in order).

- **No Backwards Compatibility**: Replace things completely. No shims, fallbacks, re-exports, or compatibility layers unless user explicitly requests it.
- **Deprecated Code**: Include a section at the end to remove code we no longer use as a result of this plan.
- **No Unit/Integration Tests**: Do not include test creation in the plan.
- **Flag Uncertainty**: When uncertain about a requirement, design decision, or implementation detail, do NOT guess or assume. Insert a `[NEEDS CLARIFICATION]` marker with a brief explanation of what's unclear and why it matters. These markers must be resolved with the user before the plan is finalized.

## Step 3: Save the Plan

Save as: `./tmp/ready-plans/YYYY-MM-DD-description.md`

## Step 4: Review and Present

After saving the plan, run **one** automatic review pass. Do not skip this step.

1. **Spawn a plan-reviewer sub-agent** to review the plan:

```
Task tool:
  subagent_type: "plan-reviewer"
  prompt: "Review the plan at [path]. Produce a numbered list of specific,
    actionable recommendations covering gaps, simplification opportunities,
    correctness issues, and better alternatives."
```

2. **Triage and apply.** Split reviewer recommendations into two buckets:
   - **Auto-fixable** — Straightforward suggestions (missing details, small corrections, obvious improvements) that don't require a design decision. Apply these directly to the plan.
   - **Needs user input** — Questions about requirements, design trade-offs, ambiguous scope, or anything where multiple valid approaches exist.

   Apply all auto-fixable changes to the plan file silently.

3. **Present to the user:**

   **a) Plan Summary** — 3-5 bullet points covering what the plan does.

   **b) Questions for You** — Only reviewer recommendations that need the user's input. For each one:
   - The reviewer's question or concern
   - **Context**: What the surrounding functionality does and why this matters. Reference specific files, patterns, or behaviors.

   If there are no questions (all feedback was auto-fixed), just say "Reviewer feedback was minor and has been incorporated."

   **c) Plan Link:**
   ```
   Plan: ./tmp/ready-plans/[filename]
   ```

   **d) Next step prompt** — Always end with: "Want to run another review pass, or is this ready to implement?"

4. **If the user wants changes or another review pass:**
   - Apply any changes the user requested.
   - Spawn a **fresh plan-reviewer** and repeat from step 1.
   - Each review pass must use a fresh reviewer so it evaluates the current state without bias.

5. **If the user says it's ready** → proceed to Step 5.

## Step 5: Return the Plan — DO NOT IMPLEMENT

Once the user confirms the plan is ready, tell them:

```
Plan finalized! To implement, run:

/implement ./tmp/ready-plans/[filename]
```

**If this plan was generated from a spec (Step 0 spec mode), also tell them:**

```
After implementing, continue with the next phase:

/clear
/create-plan
  (auto-picks the next unchecked phase from ./tmp/specs/[spec-filename])
```

**CRITICAL: Your job ends here.** Do NOT start implementing the plan. Do NOT spawn implementer agents. Do NOT write or modify any application code. The `/create-plan` skill only produces a plan file — implementation is a separate step that the user will trigger themselves with `/implement`.

## Quality Checklist

- [ ] All necessary context included
- [ ] Validation gates are executable by AI
- [ ] References existing patterns
- [ ] Clear implementation path
- [ ] Error handling documented
- [ ] Files Being Changed tree is filled in
- [ ] Architecture overview explains the big picture
- [ ] Key pseudocode covers hot spots
- [ ] No unresolved [NEEDS CLARIFICATION] markers

Score the plan 1-10 (confidence for one-pass implementation success).

## Plan Lifecycle

- **Active plans**: `./tmp/ready-plans/`
- **Completed plans**: `./tmp/done-plans/` (moved after successful implementation)
- **Cancelled plans**: `./tmp/cancelled-plans/` (moved if abandoned)
