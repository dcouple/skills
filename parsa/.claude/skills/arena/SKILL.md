---
name: arena
description: Fan out N blind candidates at one task, pick the strongest as the base, graft the best ideas from the losers into it, verify the result. Use when one attempt at a non-trivial artifact — a design, a tricky function, a doc — would lock in the wrong shape.
argument-hint: "[the artifact to produce]"
---

# Arena

One attempt commits to one shape. When the shape is the risky part, produce
several and choose.

## When

A non-trivial artifact whose first draft sets a structure everything later
inherits: a design, a tricky function, a document. Skip it when the shape is
already settled.

## Protocol

1. **Frame** — write the task once, exactly as every candidate will receive
   it, plus the acceptance test the winner has to pass. The prompt is the
   contract; a vague one produces N incomparable artifacts.
2. **Fan out** — spawn N fresh-context subagents (default 3) in one message,
   all with the same task, each writing to its own path. They stay blind to
   each other. Each returns the artifact and a short rationale naming what it
   considered and rejected.
3. **Read** — read every candidate end to end. Skimming picks the most
   familiar surface, not the strongest one.
4. **Pick a base** — the candidate a maintainer can extend most easily.
   Between two that feel tied, take the smaller surface.
5. **Graft** — port the best ideas from the losers into the base by hand,
   usually one or two per candidate. The result stays coherent under one
   mental model.
6. **Verify** — run the repo's checks, or the acceptance test from step 1,
   against the synthesized artifact.

Candidates that converge on one shape are agreement: ship the consensus and
skip the graft. Candidates that wildly diverge mean step 1 was
under-specified: reframe and re-run rather than averaging them.

## Report

Which candidate won and why. What was grafted from which loser, and what was
rejected. The verification evidence.
