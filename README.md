# skills

This repo keeps the LLM workflows we actually use on the Pane team.

The goal is simple: make good work easier to delegate, review, test, and learn
from. These skills help with the moments that repeat: fuzzy ideas, ticket
capture, planning, implementation, review, PR testing, and learning from the
work.

Start in `parsa/` for the current version of the workflow.

## How we work with LLMs

Don't ask an LLM to carry the whole project in its head.

Each phase should leave something behind for the next one: a ticket, a plan, a
PR, a review, a test note, or a learning note. For business work, that handoff
lives in `.business/`.

Most of the time, you're only answering one question:

> Is this clear enough to delegate?

If no, **discuss** it. If yes, **capture** it. If it's captured and clear,
**execute**. If work exists, **review** it. If review finds a gap, **fix** it
and **review** again.

Here is what I am going to walk you through:

```mermaid
flowchart LR
  F[Fuzzy idea] --> D[discussion]
  B[Broken but unclear] --> Inv[investigate]
  Inv --> T
  D --> T[create-ticket]
  V[Vague ticket] --> D
  T --> P{Clear enough?}
  P -->|needs decisions| D
  P -->|yes| Plan[plan]
  Plan --> I[implement]
  I --> R[review]
  R -->|fixes needed| I
  R -->|clean| QA[pr-test-automation]
  QA --> H[human manual test]
  H --> TB[teach-back]
  TB --> Done[done]
```

### A few common software scenarios

#### I have a fuzzy idea

Start with `discussion`. Once the idea has shape, run `create-ticket`.

```text
discussion -> create-ticket
```

#### I already have a ticket, but it's vague

Use the ticket as the starting point for `discussion`. Then update the ticket so
the next agent doesn't need the whole conversation.

```text
create-ticket -> discussion -> create-ticket
```

#### I have a crisp ticket

Go straight into execution.

```text
create-ticket -> plan -> implement -> review -> pr-test-automation -> manual test -> teach-back
```

`plan`, `implement`, and `review` have their own internal checks. You don't
need to think about every reviewer by hand every time; the important thing is
that review loops back to implementation until the work matches the ticket. For
non-trivial changes, use Codex and Claude as independent readers when possible:
one implements, the other reviews, then rerun until the ticket intent, plan,
diff, and runtime behavior agree.

Once the review loop is clean, run `pr-test-automation` before asking the human
to manually test. This is the first-pass QA sweep: local services, browser
automation, product flows, logs, analytics, webhooks, email/SMS, and whatever
else can be checked from tools. The goal is not to replace human testing; it's
to make the human's test pass start from evidence instead of hope. After that,
the human manually tests whatever the automation couldn't confidently prove.

After the task is really done, run `teach-back`. That writes the learning note:
what approach worked, what roads were rejected, what tradeoffs were made, where
the messy parts were, and what lesson transfers to the next project.

If the problem is broken but not understood yet, start with `investigate`
before creating the ticket or plan.

### Model choice

Here is how I choose model effort:

```mermaid
flowchart LR
  Task[What kind of work is this?] --> Impl[Implementation]
  Task --> Disc[Ambiguous discussion]
  Task --> Rev[Review or audit]

  Impl --> Clear{Clear ticket and easy repo context?}
  Clear -->|yes| Med[GPT-5.5 medium fast]
  Clear -->|no, unusually ambitious| XHigh[GPT-5.5 xhigh fast]

  Disc --> Fable[Claude 5 Fable]
  Disc --> Opus[Claude 4.6 Opus fallback]

  Rev --> Strong[GPT-5.5 xhigh fast + Claude 5 Fable]
  Strong --> Loop[Loop until only tradeoffs, rare edge cases, or no issues]
```

This keeps model choice pretty simple. In dcouple/Pane, we use GPT models
through the Codex harness and Claude models through the Claude Code harness.
Most well-scoped implementation work doesn't need the biggest model. Right now,
`GPT-5.5 medium fast` is the everyday implementation default: it is strong
enough for most clear tickets, fast enough to feel like you're flying, and cheap
enough that you can work in long windows without feeling throttled by weekly
limits.

Reach for `GPT-5.5 xhigh fast` when the implementation is unusually ambitious:
lots of moving parts, fuzzy architecture boundaries, or a mistake that would be
expensive to unwind. That should be the exception, not the default.

Review is where we should be more aggressive. The reviewer isn't trying to be
fast; it's trying to catch the thing the implementer missed. It should read the
issue, the plan, and the diff with fresh eyes and ask: did we actually do what
we meant? For non-trivial work, keep Claude and Codex review passes in the loop
until what's left is either an intentional tradeoff, a very unlikely edge case,
or no issue at all.

For that review/audit loop, it is worth spending the expensive models
sparingly: `GPT-5.5 xhigh fast` and `Claude 5 Fable` are not needed for most
implementation, so save them for the places where sharper judgment changes the
outcome. `Claude 5 Fable` is also the nicest model to talk with when the task is
ambiguous and you want to reason through the shape of the work. If the extra
usage cost is not worth it, `Claude 4.6 Opus` is an acceptable fallback. I
would avoid `Claude 4.7` and `Claude 4.8` for this workflow; they tend to feel
too constrained for open-ended discussion and judgment calls.

### Business work

For stakeholder-facing work, build context before drafting. The `.business/`
folder is the handoff.

In practice, that means:

```text
context -> discussion -> spec -> artifact -> review -> release
```

The human attention points are still few: the initial conversation or ticket,
`business-discussion`, and the final gate when the work is high-stakes or ready
to leave the building.

Here's the business workflow as a map:

```mermaid
flowchart LR
  C[business-context] --> A[business-research-adversary]
  A --> D[business-discussion]
  D --> S[business-spec]
  S --> SR[business-spec-reviewer]
  SR -->|revise| S
  SR -->|approved| ART[business-artifact]
  ART --> AR[business-artifact-reviewer]
  AR -->|fixes needed| ART
  AR -->|approved| REL[business-prepare-release]
  REL --> Gate[human gate / release]
```

## What is in this repo

Each contributor has their own folder. Start with `parsa/`.

```text
parsa/
  .claude/   Claude Code skills, commands, agents, hooks, settings
  .codex/    Codex skills and config
```

The skills are meant to be edited. The workflow shape should generalize, but the
exact contents should change as your work changes.

## Keeping skills in sync

Use this repo directly in a project, or copy the skills into your user-level
folders:

- Claude Code: `~/.claude/skills/`
- Codex: `~/.codex/skills/`

The simple sync shape is:

```bash
git -C "$REPO" pull --ff-only
rsync -a "$REPO/parsa/.claude/skills/" "$HOME/.claude/skills/"
rsync -a "$REPO/parsa/.codex/skills/" "$HOME/.codex/skills/"
```

Do not use `--delete` unless you want this repo to remove other local skills.
Restart Codex after new skills sync so the active session can see them.

## Background

This grew out of the workflow described
[here](https://runpane.com/blog/a-turing-award-winner-just-described-our-exact-workflow).
The original frame was spec, read, verify. In practice, we split that into
smaller steps because each moment needs different behavior: discussion, ticket
capture, planning, implementation, review, PR testing, and teach-back.
