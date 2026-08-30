---
name: runpane-orchestrator
description: Orchestrate persistent RunPane workstreams from issue to ready-to-merge PR. Drives investigation, planning, implementation, review, PR prep, QA, and CI without stealing focus or repeating already-granted authorization. Use when Claude Code or Pane Chat should manage one or many engineering workstreams end to end.
---

# RunPane Orchestrator

Use RunPane as the control plane. Drive every authorized workstream until
it is ready to merge or reaches a genuine blocker. Do not end a turn
merely because an agent became idle.

For "what did I work on?" or "what should I do next?", use
`pane-work-recap` or `pane-work-prioritizer`. Do not create a workstream
unless the user authorizes work.

## Persist intent, re-derive state

Write decisions and holds to the work tracker. Query everything else:
lifecycle position, check results, review counts, mergeability. Never
cache what you can re-read.

## Authorization boundary

An explicit request to finish named work through PR readiness authorizes
the reversible lifecycle stages. Record grants once and continue without
asking again. "Finish" or "do not stop" increases persistence, not scope.

Hard stops (never without an explicit grant for the exact action):

- Merge, deploy, release, publish, version bump
- Cancel an issue or delete data
- Any production or destructive mutation
- Scope expansion beyond the named work

Continue other unblocked streams when one is stopped.

## Ownership

One implementation authority per workstream. It owns all source edits,
fix commits, rebases, pushes, and PR updates. Use fresh panels for
review and QA on every new head. Reviewers never edit source.

## Delivery lanes

Choose after `discussion`. When discussion converges, send this probe
before selecting a lane: "is this addressing the root cause or a
symptom? dig deep." A premise-changing answer reopens discussion.

**Light (default).** `simple-plan`, then `prepare-pr` and
`pr-test-automation`, run continuously.

**Medium.** `create-plan` in place of `simple-plan`, adding a reviewed
plan before implementation, with `implement` as its own stage.

**Heavy.** Hand the work item to the orchestra `/do` pipeline. `/do` is
Claude-run: escalating to heavy hands the item to an orchestra-capable
Claude panel. Escalating late costs more than escalating early.

### Escalation triggers

Evaluate after discussion, and again when new evidence lands. Risk forces
medium; ambiguity forces heavy. Escalation is one-way.

Medium or heavier:

- Touches auth, permissions, billing-adjacent code, PHI, or a data migration
- Changes a public or cross-service contract, shared schema, or published exports
- Diff exceeds 300 lines or 10 files (excluding lockfiles/generated)
- No automated test exercises the change on the PR head

Heavy:

- Changes what a customer is charged, or whether money moves or service is cut
- Design decision is still open after discussion
- Investigation contradicts the work item's stated premise
- Outcome cannot be verified by tests or a QA drive within the run

A user asking for a different lane overrides the triggers.

## Lifecycle

Transition only on recorded evidence:

1. `queued` - resolve repo, issue, scope, and authorization
2. `investigating` - use `investigate` when root cause is unknown, then route to discussion
3. `planning` - require a clean approved plan. More than one defensible shape runs `arena`
4. `implementing` - use `implement`. A metric-goal item runs `hillclimb`
5. `implementation_review` - use `implement`'s fresh implementation-reviewer subagent
6. `preparing_pr` - use `prepare-pr`. Post-PR order is: review, then QA
7. `pr_open` - heavy only (orchestra's zone reviews and Must-Fix gate). Light and medium skip this
8. `pr_qa` - use `pr-test-automation`. Store current-head evidence
9. `ci_rereview` - heavy only. All lanes wait for required checks through the PR-ready gate
10. `ready_to_merge` - enter only when all readiness predicates are true. Never merge without separate authorization
11. `blocked` - record the exact missing decision/grant/conflict. Resume by deriving the earliest incomplete gate from live state

### Review feedback interrupt

From any post-PR state, actionable review feedback interrupts the normal
transition. Use `gh-address-comments` in the implementation authority. If
a fix changes the head, return through implementation review, PR update,
QA, and required checks.

## Report

While authorized work remains, rotate fairly across workstreams and
advance every eligible transition. Report a dashboard per workstream:
issue/PR URL, state, checks, review counts, blocker, and next action.
