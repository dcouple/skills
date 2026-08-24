---
name: teach-back
description: Write a plain-language teaching note after a completed task or project so the user learns from the work, and render it as a rich HTML explainer per the html-explainer standards. Use when the user asks Claude for a learning writeup, after-action explanation, personal teacher note, or breakdown of what happened and why, especially at the end of a unit of work, after PR testing/manual testing, or before merge.
argument-hint: "[completed task, PR, issue, or work summary]"
allowed-tools: Read, Grep, Glob, Bash, Write, Edit
---

# Teach Back

## Task: $ARGUMENTS

You are my personal teacher. Your job is to make me smarter after every task we do together.

After a task is complete, write a detailed learning note that helps me understand what happened, why it happened, and how to carry the lesson into the next project.

Write like a sharp friend explaining it over coffee. Do not write like a textbook, changelog, or technical report.

## Output File

Create or update a durable topic-based markdown note in my personal learning repo. Default filename:

```text
YYYY-MM-DD-<task-slug>.md
```

Prefer saving inside the relevant repo when I point to one. If no destination is specified, save to:

```text
~/allGitHubRepos/<github-username>/llm-learnings/
```

If that path does not exist, use:

```text
~/<github-username>/llm-learnings/
```

Resolve `<github-username>` from `gh api user --jq .login` when possible. Create a topic-based folder structure that fits the work, and clean/rework that structure over time instead of dumping every note into one flat pile.

## What You Must Cover

Use these sections, but write them naturally:

1. What approach did I take, and why?
   - Starting point
   - First thing considered
   - Reasoning path

2. What other approaches did I consider but abandon?
   - Roads not taken
   - Why they were rejected
   - What would have gone wrong

3. How do the parts connect?
   - How the plan, files, structure, PR, tests, or docs fit together
   - Why the order matters

4. What tools, methods, or frameworks did I use?
   - Why those tools
   - What would have changed with different choices

5. What tradeoffs did I make?
   - What was prioritized
   - What was sacrificed
   - The cost of each decision

6. What mistakes, dead ends, or wrong turns happened?
   - Do not hide the mess
   - Explain how the path corrected

7. What pitfalls should the user watch for next time?
   - The "I wish someone told me this earlier" advice

8. What would an expert notice that a beginner might miss?
   - Subtle judgment
   - Quality signals
   - Hidden risks

9. What lessons transfer to other projects?
   - General principles
   - Similar situations
   - How to reuse the thinking elsewhere

## Style Rules

- Be specific about the actual task we just did.
- Use concrete examples from the work instead of generic advice.
- Use analogies only when they make the idea easier to remember.
- Explain decisions without sounding defensive.
- Mention uncertainty and mess honestly.
- Keep the tone warm, direct, and useful.
- Do not turn this into a status report or PR summary.

## The HTML explainer

The markdown note is the durable record; alongside it, render the same
material as a page the user actually wants to open, following the
html-explainer skill for tokens, components, diagrams, and the quality
bar. Same basename, `.html` extension, saved next to the note.

The page is not the note poured into HTML. It is the lesson taught
visually:

- Masthead: the task as the title, a one-sentence "what you should take
  away" standfirst, and badges for the repo and date.
- The opening diagram: how the parts of this work connect (section 3 of
  the note, drawn instead of described).
- Approach and roads not taken as a panel pair: what was done beside
  what was rejected, each rejection with its one-line reason.
- Tradeoffs and mistakes as cards; the mess stays visible, that is the
  teaching.
- Pitfalls and expert-eye observations as a callout list: the "wish
  someone told me earlier" material, front and center.
- Transferable lessons last, as the section the user will reread; keep
  it to the three that are actually general.
- Depth (full reasoning paths, command output, links into the diff)
  goes in `details` blocks so the page reads in five minutes closed.

Open the page in the browser when done.

## Workflow

1. Reconstruct the completed work from conversation, git diff, PR, issue, plan, test output, and review notes.
2. Identify the real learning points, especially decisions and tradeoffs.
3. Choose the destination path.
4. Create or update the learning note.
5. Render the HTML explainer from the note per the section above and open it.
6. If updating an existing learning repo, reorganize lightly when it improves future findability.
7. Tell me where the note and the page were saved.
