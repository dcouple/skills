# skills

Personal Claude Code and Codex configurations for the Pane team. Each contributor has their own folder — start in `parsa/` for one take on the workflow.

## Why this repo exists

I wrote about our development workflow [here](https://runpane.com/blog/a-turing-award-winner-just-described-our-exact-workflow): Pat Hanrahan's *spec, read, verify* loop, the "death loop" that swallows people who hack before they think, and the claim that I haven't written code by hand in six months. That post is the public-facing pitch. This repo is the actual implementation — and the two have diverged in interesting ways.

What follows is a short history of how these skills got here and what each one is actually for.

## The evolution

**v0 — One big prompt.** Early on, a single `CLAUDE.md` did everything: planning, implementing, reviewing. It worked until it didn't. The prompt grew, context bloated, and the agent started drifting halfway through long tasks. The lesson was that "spec, read, verify" isn't one mode — it's three, and they want different instructions, different tools, and different temperatures.

**v1 — Splitting spec from implement.** First real refactor was carving out `discussion` and `plan` from `implement`. Discussion is exploratory: no edits, no commits, just thinking out loud against the codebase. Plan produces a written artifact a human can read in two minutes and either approve or redirect. Implementation only runs against an approved plan. This is where the "no surprises" property came from — by the time code is being written, both sides have already agreed on what it should do.

**v2 — Plan tiers.** Not every change needs the full treatment. `simple-plan` is for one-file edits where the spec fits in a paragraph. `create-plan` (and the older `medium-plan`) handles features that touch multiple files or have subtle cross-cutting concerns. `create-prp` is for the rare changes that need a product-requirements-style document because the *what* itself is unclear. Picking the right tier was the single biggest speed unlock — over-planning a typo fix is as wasteful as under-planning a migration.

**v3 — Adversarial review.** Both sides grew dedicated `plan-reviewer` and `implementation-reviewer` roles — Claude has them as subagents in `.claude/agents/`, Codex as skills in `.codex/skills/`. The point is *different prompt, no shared context, ideally a different model*. A plan reviewed in the same session by the same agent that wrote it is theater. A reviewer with no memory of the original conversation catches the things the author rationalized away. Running the same review across both Claude and Codex is the strongest version — disagreements between them tend to be exactly where the bugs live.

**v4 — Closing the loop with `share-fix`.** Once verification was working, a new failure mode showed up: the same bug kept getting written, fixed, and re-written across sessions. `share-fix` exists to convert a one-off fix into a durable note — either into memory, a CLAUDE.md, or a skill itself. The skills in this repo are partly the residue of that process.

**v5 — Linters and codebase docs.** The `linter/` commands aren't traditional linters; they're agents that audit the codebase against its own documented invariants and flag drift. This is the part of *verify* that the blog under-sells. Most "verification" advice stops at tests, but tests only check what you remembered to check. A linter agent re-reads the docs and asks whether the code still matches them.

## Layout

```
parsa/
  .claude/
    skills/        # Spec/read/verify primitives invoked via skill names
    commands/      # Slash commands — thin wrappers that compose skills
    agents/        # Subagent definitions (researcher, implementer, reviewers)
    hooks/         # PreToolUse guards (e.g. block-terraform-destructive)
    settings.json  # Hook wiring, statusline, co-author toggle
  .codex/
    skills/        # Codex-side counterparts — note the extra reviewer roles
    config.toml
```

Skills are the atoms. Commands are recipes. Agents are the personalities the recipes hand off to. Hooks are the bumpers that keep any of them from doing something irreversible.

## Using these as a starting point

Clone, copy `parsa/.claude` and `parsa/.codex` into your project root (or symlink), and read the individual `SKILL.md` files. They're written to be edited — your codebase, your conventions, your constraints. The shape of the workflow generalizes; the contents shouldn't.

## Other folders

Tyler's setup will live alongside this one. Different skills, different tradeoffs, same loop.
