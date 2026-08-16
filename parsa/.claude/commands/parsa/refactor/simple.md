# Simple Refactor

**Read-only code quality analysis for small to medium changes.**

Safe to run anytime. Analyzes the branch against the target repository's own
conventions and writes a refactor plan without modifying files.

## What This Does

Fast, focused code quality analysis that:
1. Classifies your changes (size, type, complexity)
2. Learns the conventions of the repository you are in
3. Identifies code smells and convention violations in the lines you changed
4. Generates a refactor plan with auto-fixable and manual issues
5. Writes the plan to `./tmp/` for review

## When to Use

- **Small changes** (2-5 files, 50-200 lines)
- **Medium changes** (5-10 files, 200-500 lines)
- **Bug fixes** and **enhancements**
- Quick pre-PR quality check

For large features (>10 files, >500 lines), use `/deep` instead. Simple and
deep are the whole set: simple is the cheap pass with the cleanest
signal-to-noise, deep is the one that finds real defects in big diffs. Run
both on a large PR when you want coverage; their findings overlap by about
half and the rest is complementary.

## Process

### 1. Classify Changes

Diff against the merge-base with the remote default branch, never a bare local
`main` — a stale local `main` pulls unrelated commits into the review and every
finding in them becomes a false positive.

```bash
git fetch origin main
git diff origin/main...HEAD --name-status
git diff origin/main...HEAD --numstat
git diff origin/main...HEAD --stat
```

If the branch is behind `origin/main`, note it once as "rebase before merge";
it is not a finding and does not lower the score.

**Determine:**
- **Size**: Tiny (<50) | Small (50-200) | Medium (200-500)
- **Type**: Bug Fix | Enhancement | Refactor
- **Complexity**: Trivial | Simple | Moderate
- **Layers**: Backend | Frontend | Both

Size counts changed source lines. A lockfile, generated file, or vendored
directory can add thousands of lines and no complexity — say so and classify
on the hand-written change.

### 2. Learn the Repository's Conventions

Conventions come from the repository you are in, never from a rule remembered
from another repo. In order:

1. Read `CLAUDE.md` / `AGENTS.md` at the root and in every directory the diff
   touches. These state the conventions the maintainers actually enforce.
2. Read two or three exemplar files that neighbour the changed code — files
   the maintainers clearly consider done — and note how they import, structure,
   handle errors, and document.
3. Before flagging any convention violation, confirm the convention exists
   here. `grep` how many existing files already do the thing. If the codebase
   does it everywhere, it is the convention, not a violation.

Example — Doozy states "zero relative imports" in its `CLAUDE.md`, and a grep
confirms no `../` imports exist, so a `../` there is a real Critical. Pane has
hundreds of `../` imports and no alias, so the same line in Pane is nothing.
The rule is not the pattern; the repository is.

**Pattern Matrix:**
- **Tiny/Bug Fix** → Universal smells only
- **Small/Enhancement** → Universal + the repo's basic architecture rules
- **Medium** → Universal + architecture + documentation for new files

**Universal Smells (any repository):**
- Long functions (>100 lines), deep nesting (>3 levels)
- Magic numbers/strings
- Missing or swallowed error handling on new paths
- Unused imports/variables, commented-out code, TODOs without context
- Duplicate logic: two similar functions, hooks, or types where one with
  options would do
- New public surface without a file-level or symbol-level comment when the
  neighbouring code has them

**Repo-Derived Rules (Small+):** import style, layering (where logic is allowed
to live), state-management and hook patterns, error types, test conventions —
whatever steps 1-3 above surfaced, cited to the file that states them.

### 3. Analyze Files

Read the changed files:
```bash
git diff origin/main...HEAD --name-only
```

**Pre-existing vs introduced:** only issues in lines this branch adds or
changes count against the PR. Pre-existing debt in touched files may be listed
under Info as "pre-existing, not against this PR" and never lowers the score.
Read enough surrounding code to tell the difference — a `git blame` on the
line settles it.

### 4. Generate Report

Write the plan to `./tmp/simple-refactor-plan-[timestamp].md`:

```markdown
# Simple Refactor Plan

## Classification
- Size: [X] ([N] hand-written lines; [M] generated/lockfile lines excluded)
- Type: [X]
- Complexity: [X]
- Diff base: origin/main...HEAD at [sha]
- Conventions sourced from: [files read in step 2]

## Quality Score: X/10

## Issues Found

### Critical (Must Fix)
- [file:line] Description
  → Convention: [file that states it, or "universal"]
  → Fix: How to fix
  → Auto-fixable: Yes/No

### Warnings (Should Fix)
- [file:line] Description
  → Suggestion: Improvement
  → Auto-fixable: Yes/No

### Info (Nice to Have)
- [file:line] Suggestion
- [file:line] Pre-existing, not against this PR: description

## Auto-Fixable Issues: X
## Manual Fixes Required: Y

## Convention Compliance
✓/✗ [each repo-derived rule checked, with its source file]

## Recommendations
1. Run `/refactor-apply --plan=./tmp/simple-refactor-plan-[TS].md --auto-only`
2. Manually fix [specific issues]
3. Re-run `/simple` to verify

## References
- Exemplar files studied: [paths]
- Convention sources: [paths]
```

An empty Critical section is a valid, common result. Do not manufacture
findings to fill the template; "no PR-introduced defects" is the honest
baseline for a clean change and should score accordingly.

### 5. Show Next Steps

```
📊 Analysis complete!
Plan written to: ./tmp/simple-refactor-plan-[timestamp].md
Quality Score: X/10
Auto-fixable: X issues · Manual fixes: Y issues
Issues found: [one line each for criticals and warnings]

Would you like me to run `/refactor-apply` to implement the fixes?
```

**IMPORTANT:** Always ask the user before proceeding with fixes. Do not
automatically run refactor-apply.

## Command Arguments

- `--strict`: Treat Medium as Large (stricter enforcement)
- `--classify-as=<type>`: Override type classification
- `--size=<size>`: Override size classification

## Success Checklist

- [ ] Diffed against `origin/main...HEAD`, not a local branch
- [ ] Changes classified, generated lines excluded from size
- [ ] Conventions read from THIS repo's guidance files and exemplars
- [ ] Every convention finding confirmed by grep before it was written
- [ ] Pre-existing debt separated from PR-introduced issues
- [ ] Auto-fixable vs manual separated
- [ ] Plan written to ./tmp/
- [ ] No files modified (read-only)

---

**This command is read-only and safe.** It analyzes code against the
conventions of the repository you are in and writes a refactor plan for you
to review. Run `/refactor-apply` after reviewing the plan to apply fixes.
