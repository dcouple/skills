# skills

Personal Claude Code and Codex configurations for the Pane team. Each contributor has their own folder. Start in `parsa/` for one take.

## Why this repo exists

I wrote about our workflow [here](https://runpane.com/blog/a-turing-award-winner-just-described-our-exact-workflow). That post is the pitch. This repo is the implementation, and it has drifted from the post in ways worth naming.

## What changed

The blog frames it as one loop: spec, read, verify. In practice each phase wanted its own tools, its own prompts, and often its own model. The repo grew accordingly.

Spec became three tiers. A typo fix and a migration are not the same kind of thinking, and one prompt cannot serve both without making the small thing slow or the big thing reckless.

Verify stopped meaning tests. Tests only check what you remembered to check. The interesting verification is a fresh agent reading the diff against the docs with no memory of how it got written.

Review became adversarial by default. Same agent reviewing its own output is theater. The reviewers in this repo run with no shared context, and the strongest version runs them across both Claude and Codex. Disagreements between the two are usually exactly where the bugs live.

The fix loop closed. Bugs that get fixed once should not get rewritten next session, so fixes turn into notes, notes turn into skills, and the repo is partly the residue of that.

## Layout

```
parsa/
  .claude/   skills, commands, agents, hooks, settings
  .codex/    skills, config
```

Skills are the atoms. Commands compose them. Agents are who the commands hand off to. Hooks keep any of them from doing something irreversible.

## Using these

Copy `parsa/.claude` and `parsa/.codex` into a project root and read the `SKILL.md` files. They are written to be edited. The shape of the workflow generalizes. The contents should not.
