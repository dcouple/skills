# Socratic Challenge — agent output format

> Returned **in-conversation** by Socrates to the Overseer — **not a file**.
> Runs before publish in every `/create-*` skill: round 1 challenges the draft,
> round 2+ judges the user's answers. The Overseer relays questions to the user
> verbatim and brings answers back. Cap: two judged rounds, then final verdict.
> **Your final message IS the report: begin with the verdict.** No preamble, no
> process narration, no closing summary.

---

## Round 1 — Challenge

**Verdict:** `<pass | press | rethink>` — `<one-line rationale>`
**Questions:** `<n>` (max 5; a straightforward, well-justified draft gets 0–2 —
depth follows the item, never a quota)

- **Q1** *(`necessity | root-cause | simpler-alternative | shape | assumption | consequence | completeness`)*
  - **Targets:** `"<quoted line or claim from the draft>"`
  - **Question:** `<the open question, addressed to the author>`
  - **Stake:** `<what changes about the item if the answer is weak — cut, split, redirect, abandon>`
  - **Alternative:** `<the concrete cheaper path, if this is a simpler-alternative question — omit otherwise>`

`<repeat per question, ordered by how much of the item hangs on each>`

**Verdict calibration:** `rethink` = the premise itself looks wrong (symptom not
root cause, no evidence of need, obviously wrong shape) — say so plainly in the
rationale. `press` = premise plausible but load-bearing claims are unargued.
`pass` = the draft already carries its justification; ask only what genuinely
remains (may be zero questions).

## Round 2+ — Judgment

**Verdict:** `<pass | press | rethink>` — `<one-line rationale>`
**Round:** `<k>`/2

- **Q1** — `answered | partial | evasive` — `<one line: the reasoning you're accepting, or what's still missing>`
  - **Press:** `<the sharper follow-up — only for partial/evasive, only in round 2>`

**Distilled justification:** *(only when the verdict is `pass`, or on the final
round regardless)* one line per question worth keeping, in the form the item
records: `<claim challenged> — <the reason that held>`. Mark anything still
open as `OPEN: <what remains unargued>` so the Overseer can carry it into the
item's Open questions.

---

**Grading:** `answered` = a reason that could have come out differently
(evidence, named trade-off, accepted cost, rejected alternative with a why).
`partial` = engages but leaves the load-bearing part unargued. `evasive` =
restates the request or appeals to authority without the reasoning.
Acknowledged uncertainty with a reason to proceed anyway is `answered`.
