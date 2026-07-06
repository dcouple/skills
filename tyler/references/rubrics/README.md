# Verification rubrics

One rubric per change surface. `/do`'s verify stage picks the rubric matching
the change type (see `../verification-methods.md`) and includes it in the
verifier's dispatch alongside the item's `AC#` criteria.

How to read a rubric:
- Every item is **binary** — it passes only on the named observable evidence,
  never on a judgment or an assertion.
- **[blocker]** items gate the verify stage; unlabeled items are reported but
  don't block.
- "Known failure modes" list what has actually bitten on this surface —
  check them even when no AC mentions them.

How rubrics grow: from postmortems and review misses, not speculation. When
a `/postmortem` names a failure a rubric item would have caught, add that one
item (keep each rubric at 5–9 items — encode what's dangerous to skip AND
likely to be skipped; long lists get box-ticked).
