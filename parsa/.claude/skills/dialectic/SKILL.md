---
name: dialectic
description: Adversarial debate between the two model stacks — a Claude advocate vs a Codex opponent — to pressure-test one high-stakes decision before it locks, or to adjudicate a head-on conflict between the two reviewers. Use at zones 0–1 when a design fork resists convergence, when the user asks to "duel"/"debate" a direction, or when Codex and Claude reviews disagree on a Must Fix. Not for zone 2–3 work.
argument-hint: "[the decision or conflict to debate]"
---

# Dialectic — two stacks, one motion

Parallel blind reviews give redundancy; a dialectic gives **rebuttal** — each
side must attack the other's strongest case instead of independently missing
the same thing. What survives solo review is the *plausible-but-mismatched*
direction: a design whose assumptions — scale, maturity, team size, risk
tolerance, reversibility — belong to a different context than the motion's.
It reads as best practice because it is, somewhere else; it rarely survives
an opponent briefed on the actual constraints.

## When

- A zone 0–1 design fork that resists convergence, before the D-decision
  locks — offer it from a discussion or planning session.
- A head-on Must-Fix conflict between the Codex and Claude review lanes —
  one round, then the Overseer rules.
- The user invokes it directly on a motion.

Never for zone 2–3 items: two max-effort stacks arguing about a contained
change costs more than being wrong would.

## Protocol

1. **Motion** — the Overseer writes `./tmp/<id>/refs/dialectic-<slug>.md`
   (standalone runs: `./tmp/dialectic/<slug>.md`): the decision in one
   sentence, the candidate positions, and the constraints that decide it —
   the ACTUAL scale, the zone, reversibility, what the repo already does
   (with `file:line` where checkable). An honest motion is most of the value;
   a motion that omits its real constraints invites answers tuned to someone
   else's context.
2. **Rounds** (default 2, cap 3) — appended to the motion file. **Round 1 is
   blind and parallel**: both sides write their opening position from the
   motion alone, neither seeing the other — agreement despite different
   biases is the quality signal, and a blind opening prevents the second
   mover anchoring on the first. Later rounds are sequential rebuttal. Every
   round is capped at ~400 words — density over coverage; argue the
   load-bearing points only.
   - **Advocate**: a Claude sub-agent (`model: opus`, thinking) argues the
     leading position — strongest case, named tradeoffs, checkable claims
     cited.
   - **Opponent**: a Codex dispatch via Bash (timeout 600000 ms) —
     `codex exec -m gpt-5.6-sol -c model_reasoning_effort="xhigh" --sandbox
     read-only --ephemeral --skip-git-repo-check -C <repo root> -o <out>
     "<prompt>"`; each dispatch is a fresh session, so the prompt names this
     skill's `references/instructions.md` and `references/opponent-round.md`
     by **absolute path**, carries the motion file path, and **names the round
     type** (blind opening / rebuttal / final) so it prints the matching format
     variant. Its job: in round 1, an opening position from the motion alone
     (nothing to rebut); in later rounds, rebut the advocate's specific claims —
     no restating its own case as rebuttal — then present the strongest
     alternative under the motion's constraints.
   - Sides alternate; each round reads everything before it; no side edits
     another's text. A side may concede with reasons — early convergence is
     a valid outcome, including convergence on a third design neither side
     opened with.
   - **Final round, both sides**: end with (a) a steelman — the opponent's
     single strongest point, stated fairly — and (b) a blind-spot line: what
     neither position addresses. Both feed the verdict's grafts and residual
     risks.
3. **Verdict** — the Overseer (never either wizard) closes the file: the
   chosen direction, the points grafted from the losing side, and the named
   residual risks. The verdict lands where the decision lives — the
   discussion decision log, the plan's D-decision, or the review resolution —
   with a link to the transcript.

## Rules

- One motion per dialectic; a second question mid-debate becomes its own run.
- Dispatches are ephemeral; the transcript file is the artifact and travels
  with the item's `refs/`.
- Checkable claims carry evidence (`file:line`, a doc, a measurement); a
  round of pure assertion is a wasted round — the Overseer strikes it and
  re-prompts.
- The Overseer must not signal a preferred side in the motion or between
  rounds; judging happens once, at the end.
