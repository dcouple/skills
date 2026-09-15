---
name: hillclimb
description: Improve one measurable metric toward a target through controlled experiments, retaining only verified gains.
---

# Hillclimb

One change, one measurement, keep or revert. Never stack untested changes,
and never claim a win from reading the diff.

## Set up

1. Name one metric and the direction that counts as better. One, not three.
2. Name the target that ends the run.
3. Write the measurement method as a repeatable command and state it. Sample
   enough to clear the noise — a median of N runs, not one. Freeze it;
   changing the method invalidates every number taken before the change.
4. Record the baseline, plus a green run of the checks that have to keep
   passing.

No measurement, no claim.

## Loop

Rank the live hypotheses by expected win and take the top one. Each
hypothesis names a mechanism ("defer X off the boot path because it blocks
first paint"), not "try memoizing something".

- Implement it alone.
- Re-measure with the frozen method and run the checks.
- Accept only when the metric moves past the noise and the checks stay green.
  Otherwise undo only that experiment's changes, preserving unrelated work.
- One commit per accepted win, named with the before and after numbers.

Log every attempt, kept or reverted, so the search accumulates instead of
circling.

## Throughput

When work has independent units, treat bounded parallelism as a hypothesis, not
a mandate.

- Measure wall-clock and throughput alongside the named metric. Identify the
  constrained resource, increase concurrency one measured step at a time, and
  keep it only when the gain clears the noise and checks stay green.
- Apply appropriate backpressure and resource limits. Stop when gains plateau
  or errors, tail latency, rate limits, quality, or cost worsen.
- Skip this for inherently sequential or dependency-bound work; improve the
  critical path or algorithm instead.

## Stop

At the target, or after three consecutive hypotheses with no accepted win.
Don't relax the target to declare victory.

## Report

The metric trajectory as a table: attempt, hypothesis, before, after,
verdict. The accepted wins. The rejected hypotheses and what each ruled out.

## Grain handoff

- If connected, keep the baseline, experiment log, and report in the supplied task folder, or `Development Artifacts/YYYY-MM-DD-<task>`; update the same artifacts as the run progresses.
- Keep runnable code and needed local evidence in place, preserve privacy limits, and continue locally silently without Grain.
