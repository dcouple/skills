# Rubric — mobile app change

1. **[blocker]** Each UI-facing `AC#` proven in the simulator/emulator by
   driving the real flow (taps, gestures, navigation). Evidence: driven-flow
   transcript or test report.
2. **[blocker]** The changed journey exercised end-to-end from a fresh app
   state (cold start), not only from a convenient mid-state.
3. **[blocker]** Unhappy path checked: offline/failed request, denied
   permission, or empty state renders a handled state. Evidence: quoted
   log/output for the failure case.
4. Screen rotation / resize (or the platform equivalent) doesn't lose the
   changed screen's state, where applicable.
5. Deep links / notifications into the changed screen still land correctly,
   if the change touches routing.
6. User-facing copy read in place — matches intent and product voice.

Known failure modes: works on simulator's default device only; navigation
back-stack broken after the new screen; permission prompt loop; layout
clipped on small devices.
