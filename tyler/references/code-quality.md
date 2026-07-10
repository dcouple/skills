# Code quality — reviewer rubric (project-agnostic)

> Read by both code reviewers (Claude + Codex) alongside the diff.
> Correctness and security live in the role instructions; this file covers
> the *house rules* dimension — code that works but doesn't belong here.

## Discover the conventions first

Never assume a stack. Before judging idiom, learn this repo's:

- convention docs — project `CLAUDE.md` / `AGENTS.md` / CONTRIBUTING, lint
  and formatter configs, type-checker strictness;
- the neighbors — the 2–3 existing files most similar to each changed file:
  naming, layering, state management, error idiom, import style;
- shared hubs — where cross-module types/utilities live, and whether the
  diff duplicates one.

The diff is judged against what THIS repo does, not against general taste.
Every house-rule finding cites the convention's source (config line,
neighbor `file:line`, doc section).

## Severity mapping

- **Must Fix** — only what the role instructions already gate: broken
  behavior, security, unverifiable ACs. A house-rule violation is never
  Must Fix on its own.
- **Should Fix** — architecture and idiom: layering the repo consistently
  avoids, a second source of truth for an existing type/utility, state
  managed in the wrong place per the repo's own pattern, type-escape
  hatches (`any`-style) where the repo is strict.
- **Nice to Have** — naming, formatting drift the linter missed, import
  ordering, comment style.

Rule of thumb: if the repo is itself inconsistent about it, it's Nice to
Have at most — don't enforce a convention the codebase doesn't keep.
