---
name: skillify
description: "Capture this session's repeatable process into a reusable skill. Call at end of a process you want to automate."
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - AskUserQuestion
  - Bash(mkdir:*)
user-invocable: true
disable-model-invocation: true
argument-hint: "[description of the process you want to capture]"
arguments:
  - description
---

# Skillify

Capture the session's repeatable work as a skill. Use the conversation's inputs,
outcomes, user corrections, and observed tool behavior; do not ask the user to
restate what is already clear.

## Choose what to capture

Identify the repeatable task, required inputs, completion evidence, non-obvious
constraints, and external actions needing authorization. A correction becomes
a reusable rule only when it generalizes to this task. Omit incidental model
workarounds and steps the next agent can infer from the goal.

Use the user's chosen location and name. Otherwise propose a repo-local skill
for a project workflow or a personal skill for a cross-project workflow. Ask a
focused question only when ownership, location, or scope is materially unclear.
An explicit request to create/update the skill authorizes writing it; a request
for a draft or review pauses before installation or publication.

## Write the reusable contract

Keep the description short and specific enough to distinguish neighboring
skills. Preserve an existing skill's name, invocation policy, tool boundaries,
and caller contracts unless the requested change requires updating them.

Keep the outcome, essential constraints, and completion boundary in `SKILL.md`.
Move substantial conditional procedures to linked references with a clear read
condition. A short self-contained skill needs no extra reference files. Use
scripts for repeated deterministic mechanics, not generic boilerplate.

Include only supported frontmatter for the target harness. The description
owns discovery; avoid a second long trigger list. Add arguments, tools, or fork
metadata only when the actual workflow requires them. A minimal entrypoint is:

```markdown
---
name: skill-name
description: Perform a specific task when its defining condition applies.
---

# Task

State the intended result and the non-obvious constraints that change decisions.
Link optional procedures where their read condition becomes relevant.
Define the evidence of completion and where existing authorization ends.
```

Do not require full-repo reading, repeated clean reviews, a fixed number of
examples, or confirmation at every stage. A planning-only task ends at its
plan; an authorized implementation task continues through relevant checks and
fixes. Keep real output schemas, fragile commands, and external-action grants
exact. No skill can bypass the active harness's permissions.

## Validate and save

Check frontmatter, names, local links, and any scripts. For complex changes,
exercise representative requests with raw artifacts and observable outcomes,
including a nearby request that should not invoke the skill. Update affected
harness variants, callers, and the repository catalog when contracts change.

Save in the requested location and use the repository's requested commit/PR
workflow. Report what the skill does and how to invoke it. A local file is not
an installed or published skill until the relevant save operation is verified.
