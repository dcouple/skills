# Delivery Lanes

## Delivery Lanes

Three lanes. Choose after `discussion`: the first trigger below becomes
evaluable once the design question is settled or shown to be open. Recommend a
lane by what it buys.

`investigate` and `discussion` run with the user in the orchestrating
conversation. When the work item already specifies the change, they collapse
into the delegated run as a confirmation that settles residual choices and
records them. Delegation starts at planning.

**Light (default).** `simple-plan`, then `prepare-pr` and `pr-test-automation`,
run continuously. `simple-plan` owns its whole arc — it plans, implements on the
approved plan, and runs the implementation reviewer — so states 3-5 run inside
it and the chain names no separate implement stage. A standing run-continuously
grant is the plan approval it waits for.

**Medium.** The same chain with `create-plan` in place of `simple-plan`, adding
a reviewed plan before implementation, with `implement` as its own stage on the
approved plan. One stage apart from light, so a run can move between them
cheaply.

**Heavy.** Hand the work item to the orchestra `/do` pipeline, a different
execution model with zone-based review lanes and Must-Fix gates. `/do` is
Claude-run: a workstream escalating to heavy hands the item to an
orchestra-capable Claude panel through the orchestrator rather than running it
in place. Entering it is a handoff, so escalating late costs more than
escalating early.

Check whether the proposed change addresses the root cause when that premise
is uncertain. Reopen discussion only if evidence changes the premise. Readiness
and evidence requirements apply regardless of lane.

### What Each Lane Buys

Where the repository runs an automated PR review, all three lanes get it. Read
that workflow's triggers before relying on it: one firing on `opened` and
`ready_for_review` alone reviews the version that opened the pull request, and
the version that merges goes unread.

Light adds the implementation reviewer and a QA pass; medium adds the plan
reviewer on top. Their
findings arrive as comments a run may decline to act on. Only heavy re-reviews
the current head behind a gate that blocks. State that difference when you
recommend, and name the lane in the pull request body so the reviewer knows
which checks ran. When the recommendation is medium, also offer heavy and say
what it would buy: heavy is expensive, and the user decides when a medium item
earns it.

### Escalation Triggers

Evaluate after `discussion`, and again whenever new evidence lands.

Risk forces medium; ambiguity forces heavy. A risky change with a testable
outcome is what medium's reviewed plan and gates exist for. Heavy is for work
whose shape is still uncertain, where orchestra's investigation and review
fan-out earns its cost — plus one exception: the charge path goes heavy even
when testable, because its failures are silent and customers are the detection
channel.

Medium or heavier:

- It touches authentication, authorization/permissions, billing-adjacent code,
  PHI or other regulated patient data, or a data migration.
- It changes a public or cross-service contract, or a shared schema: an API
  request/response, an event payload, a published package's exports, or a table
  another service reads.
- The diff exceeds 300 changed lines (added plus deleted, excluding lockfiles,
  generated files, and snapshots) or touches more than 10 files.
- No automated test or required check will exercise the change on the PR head.

Heavy:

- It changes what a paying customer is charged, or whether money moves or their
  service is delivered or cut off: the charge path. Billing-adjacent code and
  trial-scoped limits are medium.
- The design decision is still open after `discussion`, or `discussion` produced
  more than one viable approach with no evidence separating them.
- Investigation contradicts the work item's stated premise.
- The outcome cannot be verified by tests, required checks, or a QA drive within
  the run.

A user asking for a heavier lane is sufficient on its own and needs no trigger.
A user asking for a lighter lane than the triggers select must name the trigger
being overridden.

Escalation is one-way. An agent that hits a trigger mid-run escalates
immediately. Re-enter at the earliest state the trigger invalidates: a
contradicted premise returns to `investigating`, every other trigger to
`planning` — inside the orchestra handoff when the trigger forces heavy. Work
already implemented is re-planned against, not discarded, then
carried through the gates on the current head. Never de-escalate.
