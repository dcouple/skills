---
name: postmortem
description: Runs a postmortem after /do finished and the human reviewed the PR, when the result fell short of intent. Use when the user says a /do run missed the mark, the PR needed rework, the delivered feature didn't match the ticket, or asks "why did /do get this wrong" — or when any workflow skill (/discussion, /create-*) produced the wrong outcome. Root-causes the gap in our system and proposes one concrete improvement.
argument-hint: "[PR url/# or work-item id]"
---

# Postmortem

## Target: $ARGUMENTS

Compound learning: when a `/do` run fell short of intent — or another workflow
skill produced the wrong outcome (a ticket the gate should have killed, a skill
that fired at the wrong moment) — find the root cause in **our system** — the
skills, agents, templates, and criteria — not just the code. The completion
artifact is `./tmp/<id>/postmortem.md` plus one proposed (not applied) system change.

This skill changes nothing: no code fixes, no skill edits. If the code itself needs
fixing, that goes through `/create-issue` then `/do`; the proposed system change is
presented for the human to approve, not applied.

## Steps

### 1. Load the record
Resolve `<id>` from $ARGUMENTS (a work-item id directly, or match a PR to the `pr:` field
across `./tmp/*/item.md`). Then read:
- `./tmp/<id>/item.md` — what we asked for
- `./tmp/<id>/plan.md` — what `/do` planned
- `./tmp/<id>/wrapup.md` — what `/do` claims it delivered and verified
- PR feedback — `gh pr view <pr> --comments` and the review threads, or ask the user to
  paste it if it lives outside GitHub

**Success criteria**: all four sources loaded (or their absence noted — a missing wrapup
is itself a finding).

### 2. Establish the gap [human]
Discuss with the human what fell short: delivered vs intended, concretely. Anchor on the
item's intent and ACs — did `/do` miss the ticket, or did the ticket miss the intent?

**Success criteria**: the gap is stated in one or two concrete sentences the human agrees
with.

### 3. Root-cause it in OUR system
Trace the gap upstream through the pipeline and name where it entered:
- **Thin ticket** — intent or end state under-specified, so `/do` optimized the wrong thing
- **Weak AC** — verification criteria passed while the intent failed (untestable or
  mis-aimed criteria)
- **Missing direction** — a decision the model shouldn't have made alone wasn't locked
- **Review blind spot** — a reviewer should have caught it and the report shows it didn't
- **Skill/agent gap** — a pipeline stage lacks an instruction this failure needed

The code defect (if any) is a symptom here. Note it, and route the fix through
`/create-issue` then `/do` — not this skill.

**Success criteria**: one primary system-level cause identified, with evidence from the
step-1 documents (quote the thin section, the weak AC, the review miss).

### 4. Write the postmortem
Write `./tmp/<id>/postmortem.md` following this skill's `references/postmortem.md` —
emit the filled-in frontmatter and body only; the template's "— format" header and
guidance quotes are authoring notes, not output.

**Success criteria**: `postmortem.md` exists and the "why the gap happened" section names
the system cause, not just the code defect.

### 5. Propose ONE system change [human checkpoint]
Propose exactly one concrete change to one specific file — a skill, sub-agent, template,
or criteria block, named by its path in the skills repo (`dcouple/skills`, under
`tyler/` — e.g. `tyler/.claude/skills/discussion/SKILL.md`,
`tyler/references/verification-criteria.md`, `tyler/.claude/agents/code-reviewer.md`).
The synced copies under `~/.claude` and `~/.references` are mirrors — the edit lands in
the repo and re-syncs. Quote the file path and show the proposed edit.

Do **not** apply it. Present it for the human to approve; record the proposal (and the
verdict, if given now) in postmortem.md's "What to change so it doesn't recur" section.
One change per postmortem — the highest-leverage one — so each fix is attributable.

**Success criteria**: proposal names an exact file and shows the concrete edit; nothing
outside `./tmp/<id>/` was modified.

```
Suggested next steps:
- `/create-issue [defect]` then `/do ./tmp/<id>/item.md` — fix the code gap itself
- Apply the approved system change in a normal editing session, then commit it
```
