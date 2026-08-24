---
name: reality-check
description: Assess where a project actually stands against what its README, plan, or pitch promises, with every claim tested against the artifact itself rather than the docs. Use when someone asks "where are we", "are we on track", "what's missing", "does this actually work", or before a demo, a handoff, or a decision that assumes the project is further along than it might be.
argument-hint: "[project path, repo, or plan to check against]"
allowed-tools: Read, Grep, Glob, Bash
---

# Reality Check

## Task: $ARGUMENTS

A project's documents describe the project its authors intended. The
project that exists is whatever survives being run, read, and poked at
today. This skill measures the distance between the two, and it never
takes the documents' word for anything.

## Establish the promise

Collect every place the project says what it is: README, plan, brief,
pitch, roadmap, open PR descriptions, the landing page if there is one.
Distill them into a numbered list of concrete promises, each one
falsifiable. "Users can install with one command" is a promise.
"Modern, fast architecture" is not; drop vagueness rather than grading
it.

## Test the promise

For each promise, go find out, in the artifact, not the docs:

- **Works**: you ran it, read it, or traced it end to end, and it holds.
  Name the evidence (the command and its output, the file:line, the
  passing test).
- **Exists but unproven**: the code or page is there, and nothing
  demonstrates it works. Say what proof is missing.
- **Partial**: some of the promise holds; state exactly which part does
  not.
- **Absent**: nothing implements it. Note whether anything even refers
  to it.
- **Contradicted**: the artifact does the opposite of the promise. These
  outrank everything else in the report.

Run the cheapest honest test first: the install one-liner in a clean
temp directory, the quickstart verbatim, the demo path as a stranger
would walk it. A promise you could test in two minutes and didn't is a
finding about the check, not the project.

## Find the unpromised

Walk the artifact once in the other direction: what exists that no
document mentions? Undocumented features, half-built directions,
abandoned scaffolding. These are either wins nobody is claiming or
weight nobody is admitting, and the report says which.

## The report

Open with one paragraph a stakeholder could forward: how far along this
project actually is, in plain words, no percentages invented from
nothing. Then:

- the promise list with verdicts and evidence, contradictions first
- the unpromised findings
- the three gaps most worth closing next, each with why it is the one
  blocking the story the docs tell
- what the docs should stop claiming today, if anything

## Boundaries

- Evidence over inference: every verdict cites something you ran or
  read. If you could not test a promise, say so and say why; never
  downgrade it to a guess.
- Check the artifact as it is on the branch you were pointed at, not as
  in-flight work will make it.
- This skill reports; it does not fix. Turning gaps into work items is a
  separate step the user asks for.
- No em dashes.
