# Rubric — frontend web change

1. **[blocker]** Each UI-facing `AC#` proven by natural navigation or a
   behavior-level test: real interaction sequence (click/type via role-based
   locators), assertion on user-visible outcome. Evidence: interaction
   transcript + assertion output.
2. **[blocker]** The changed flow starts from a known state and was exercised
   end-to-end — not just the component in isolation. Evidence: the flow steps
   as driven.
3. **[blocker]** Unhappy path checked: invalid input, empty state, or failed
   request renders a handled state, not a blank screen or console error.
   Evidence: quoted console output for the failure case.
4. Accessibility scan (axe-style) on changed screens: 0 critical violations.
   Evidence: violation report.
5. No new console errors/warnings during the driven flow. Evidence: console
   excerpt.
6. Layout-sensitive change → visual before/after diff captured.
7. User-facing copy read in place — matches the item's intent and the
   product's voice.

Known failure modes: control renders but handler not wired (click does
nothing); route added but not mounted; state persists across navigation when
it shouldn't; works only with seeded data.
