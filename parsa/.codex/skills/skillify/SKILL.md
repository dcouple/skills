---
name: skillify
description: Capture this session's repeatable process into a reusable Codex skill. Run at the end of a workflow you want to automate.
argument-hint: "[description of the process you want to capture]"
---

# Skillify

You are capturing this session's repeatable process as a reusable Codex skill.

## Inputs

- `$ARGUMENTS`: Optional description of the process the user wants to capture. May be empty.

## Goal

Produce a new `SKILL.md` file under `parsa/.codex/skills/<skill-name>/SKILL.md` (or another path the user picks) that captures the workflow from this session in a form another Codex run can re-execute.

## Session Context

You have the full conversation history available. Analyze it directly — do not ask the user to re-explain what they just did. Pay special attention to places where the user corrected your approach during the session; those become rules in the new skill.

If `$ARGUMENTS` is non-empty, treat it as the user's hint about which process to capture.

## Steps

### 1. Analyze the session

Before asking any questions, work out from the transcript:
- What repeatable process was performed
- The inputs/parameters
- The distinct steps in order
- The success artifacts/criteria for each step (e.g. "open PR with CI green," not "wrote code")
- Where the user corrected or steered you (these become rules)
- What tools and commands were needed
- What the overall goal and success artifact is

**Success criteria**: a clear, concise mental model of the workflow that the user can confirm in one or two sentences.

### 2. Interview the user

Codex does not have AskUserQuestion. Ask the user via plain text, one short round at a time. Wait for an answer before proceeding to the next round. Keep questions tight — do not over-ask.

**Round 1 — high-level confirmation**
- Propose a skill `name` (kebab-case) and a one-line `description`.
- Propose the overall goal and the success artifact.
- Ask: "Confirm or edit."

**Round 2 — shape**
- Present the high-level steps as a numbered list.
- Propose arguments if the workflow needs them.
- Ask where to save the skill. Default options:
  - **This repo** (`./.codex/skills/<name>/SKILL.md`) — repo-specific
  - **Personal** (`~/.codex/skills/<name>/SKILL.md`) — follows you across repos
  - **Pane skills repo** (`parsa/.codex/skills/<name>/SKILL.md` inside `dcouple/skills`) — shared across the team

**Round 3 — per-step detail (only if non-obvious)**
For each major step, ask the smallest set of questions needed to disambiguate:
- What does this step produce that later steps depend on?
- What proves the step is done?
- Should the user be asked to confirm before irreversible actions (merging, pushing, deleting)?
- Can any steps run in parallel?
- Hard constraints: things that must or must not happen.

**Round 4 — invocation triggers**
- Confirm when this skill should be invoked.
- Suggest trigger phrases (e.g. "cherry-pick to release", "CP this PR", "hotfix").

Stop interviewing as soon as you have enough. Do not pad rounds for simple workflows.

**Rule**: never edit, write, or run anything during the interview rounds. Only do the file write after Step 4 in Step 3 below.

### 3. Write the SKILL.md

Create the directory and file at the location chosen in Round 2.

Codex SKILL.md frontmatter is minimal — only these fields:

```yaml
---
name: kebab-case-name
description: one-line description of what the skill does and when to use it
argument-hint: "[optional argument hint shown in autocomplete]"
---
```

Do **not** add Claude-specific fields like `allowed-tools`, `when_to_use`, `user-invocable`, `disable-model-invocation`, or `context`. Codex ignores them.

Body structure:

```markdown
# <Skill Title>

One- or two-sentence purpose.

## Inputs
- `$ARGUMENTS`: what the user passes (omit if no args)

## Goal
The artifact or end state that proves the skill succeeded.

## Rules
- Hard constraints distilled from user corrections during the reference session.

## Steps

### 1. Step name
What to do. Be specific. Include the exact command when relevant.

**Success criteria**: REQUIRED on every step. Concrete and checkable.

### 2. Next step
...
```

**Step annotations** (use only when needed):
- **Success criteria** — required on every step.
- **Artifacts** — data this step produces that later steps consume (PR number, commit SHA, file path).
- **Human checkpoint** — pause-and-ask for irreversible actions or judgment calls. Mark with `[human]` in the title.
- **Parallel** — steps that can run concurrently get sub-numbers: `3a`, `3b`.

**Style rules**:
- Keep simple skills simple. A 2-step skill does not need annotations on every step.
- Prefer concrete commands over prose. "Run `git rebase origin/master`" beats "rebase against the trunk."
- Lead the rules with the user's actual corrections from the reference session — those are the highest-signal constraints.

### 4. Confirm and save

Before writing the file, output the complete SKILL.md content in your reply as a fenced markdown code block so the user can review it. Then ask one short question: "Save this to `<chosen path>`?"

After the file is written, tell the user:
- The exact path written
- How to invoke: `/<skill-name>` (or `codex --skill <skill-name>` depending on their setup)
- That they can edit the SKILL.md directly to refine it

## Differences from the Claude version

This skill is a Codex adaptation of `parsa/.claude/skills/skillify/SKILL.md` (which is in turn extracted from Anthropic's internal `/skillify`). Two intentional changes:

1. Interview rounds use plain-text Q&A instead of `AskUserQuestion`.
2. Frontmatter is trimmed to fields Codex understands (`name`, `description`, `argument-hint`). The full Claude-style frontmatter is preserved in the Claude version.

Everything else — the four interview rounds, the per-step annotation grammar, the bias toward capturing user corrections as rules — is the same on purpose. A skill captured here should be re-executable by either runtime with minimal porting.
