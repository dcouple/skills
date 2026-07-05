# Template & Output-Format Improvements — proposed change list

> Synthesized 2026-07-05 from three local-research passes: (A) skill document
> templates vs. `tmp/research/` + `tmp/sample docs/`, (B) the seven agent return
> formats, (C) an output-convention sweep of the five reference libraries in
> `tmp/reference/`. Status: **APPLIED 2026-07-05** — all 23 changes are in the
> templates; shared conventions documented in `../templates/README.md`; the 1b
> authoring conventions carried into `build-plan.md`.

## Cross-cutting (do these first — they touch everything)

1. **One severity scale everywhere: `Must Fix / Should Fix / Nice to Have`.**
   Applies to both review reports and the wrap-up's "Review outcome". Obra pairs it
   with short calibration prose defining what earns each level — add that once, in
   the review templates. Kills the current Must-Fix vs blocking/important/nit split
   that would misroute the /do loop's "zero Must Fix" rule.
2. **Every agent return opens with a one-line machine-parseable status.** The two
   reviewers already do; extend to the other five with small closed enums the
   Overseer can branch on, e.g. implementer `DONE | DONE_WITH_CONCERNS | BLOCKED |
   NEEDS_CONTEXT` (obra), app-user `Verdict: pass | fail — <blocker>`, investigator
   `Root cause: <one line> · Confidence: …`. Add obra's framing rule verbatim to
   review-type returns: *"Your final message is the report itself: begin with the
   verdict. Every line is a verdict, a finding with file:line, or a check you ran —
   no preamble, no process narration, no closing summary."*
3. **Counts line + stable finding IDs in both review reports.** Under the verdict:
   `Must Fix: N · Should Fix: N · pass k/3`; findings numbered `MF-1`, `SF-1`;
   re-review passes must mark each prior ID `fixed | persists | new`. This is what
   makes the 3-pass loop countable and dedupable.
4. **Evidence rules, stated in the contract:** every finding cites `file:line`;
   every PASS quotes its supporting evidence; and add obra's escape hatch — a
   `⚠️ Cannot verify` lane — so agents flag uncertainty instead of guessing.
5. **Anti-padding rule in all seven agent templates:** omit optional sections when
   empty (Praise, Notes, Gotchas); only sections where absence is ambiguous (Plan
   deltas, Blockers) write a literal "none". Plans additionally ban placeholder
   content: "TBD", "add appropriate error handling" are plan failures (obra
   writing-plans).
6. **One confidence vocabulary, words not emoji:** `confirmed | likely | hypothesis`
   for investigator and web-researcher (currently two different scales, one emoji).
7. **Normalize skill-template frontmatter:** document the `id` vs `item` key split in
   README, unify the status enum across feature/bug/epic, and add `pr:` to
   feature-ticket + bug-report (every item ends in one PR) instead of epic-only.
8. **One checkbox convention:** single-line checklist tasks in the plan
   (`- [ ] <task — what & why, where>`), replacing the two-line task+done shape;
   also fixes the stray backtick in the plan header.

## Per-template

**skills/investigate/bug-report.md**
9. Add **Steps to reproduce** (numbered, from a known state) between "Expected vs
   actual" and "Root cause" — without it the verify stage can't prove the fix.
10. Add a one-line **Environment** field (version/build, runtime).

**skills/discussion/epic-spec.md**
11. Slim the phases table to `# | Phase | Desired end state | Depends on | Size | ✓`
    and move per-phase Scope / Out-of-scope / Verification into short subsections —
    EARS blocks can't live in table cells.
12. Number the key decisions (`D1`, `D2`…), each as decision + rationale + rejected
    alternative — the sample docs cross-cite by ID and reviewers dedup against them.

**skills/discussion/feature-ticket.md**
13. Add **Starting points (non-exhaustive)**: 2–4 file/module pointers, one clause
    each — cheapest way to save /do an exploration pass.
14. Add **Open questions** using the same `[NEEDS CLARIFICATION]` convention as the
    epic spec.

**skills/do/implementation-plan.md**
15. Verification section: restate the EARS criteria **verbatim** plus the exact
    commands to run — the plan must be self-sufficient for Codex, not point back at
    the item.

**skills/do/wrap-up-report.md**
16. Replace its "Files changed" section with **"Deltas vs plan's Files-changed
    table"** — the full list now duplicates the plan and the PR diff.

**agents/code-reviewer/review-report.md**
17. Dissolve the standalone **Security** section into Must Fix / Should Fix with a
    `(security)` tag per finding — otherwise Must-level security findings sit outside
    the counted bucket the loop branches on.
18. Each Must Fix names the plan decision / acceptance criterion it violates
    (`violates D3`), or is tagged `new issue`. (Also plan-reviewer.)

**agents/app-user/verification-result.md**
19. Each failing row carries its own evidence pointer; `Pass`/`Fail` words in the
    Result column, not ✅/❌.

**agents/implementer/implementation-result.md**
20. Add `tests` to Quality checks; every check reports exact command + exit result,
    not bare pass/fail. Cap the return at ~15 lines (obra) — detail lives in the
    plan's deltas section.

**agents/code-researcher/codebase-findings.md**
21. Add a required **"Not found / open questions"** section — silence must be
    distinguishable from absence.

**agents/web-researcher/research-dossier.md**
22. Move the date/version requirement into the finding-bullet contract:
    `<finding> — <source, date/version>`.

**shared/verification-criteria.md**
23. Make the criterion→method mapping explicit (`criterion | method | command`
    table) and state that checkboxes are state, ticked by the verify stage. Add one
    good/bad criterion pair (mattpocock triage style: a runnable command vs "should
    work correctly").

## For task 1b (skill/agent authoring, not templates)

- **Dispatch prompts as sibling `*-prompt.md` files** (obra subagent-driven-development):
  fenced prompt + `**Placeholders:**` legend + one-line `**Returns:**` contract —
  keeps SKILL.md lean and the contract co-located.
- **Word caps + quote-the-source rules in fan-out briefs** (mattpocock code-review:
  "Under 400 words", "Quote the spec line for each finding"); parent presents
  parallel reports side-by-side, never merges/reranks.
- **Template bodies as content-describing prose** inside the skeleton (mattpocock
  to-prd), not bare `[TODO]` slots.

## Do NOT copy (from the reference sweep)

Box-drawing rules and emoji-chrome section labels (alirezarezvani); mandated
pseudo-precise fields models will confabulate ("Cost per week: $X") — offer an
unknown/can't-verify lane instead; giant JSON output schemas for human-read reports
(anthropics grader is for scripted evals); ALL-CAPS shouting outside genuinely
safety-critical rules.

## Considered and rejected (so we don't overdo it)

- Postmortem: leave lean; no SRE timeline sections.
- Feature-ticket "Scope" section: Desired end state + Out of scope already bound it.
- Praise sections: keep (regression-prevention), but empty-omittable per rule 5.
- Third verdict state ("approve with reservations"): blurs the zero-Must-Fix branch.
- Full Conventional-Comments label grammar: second taxonomy, no new Overseer branch.
- GitHub YAML issue forms: they constrain human reporters; Fable authors these.
- system-analysis.md and the "— format" template chrome: fine as is.
