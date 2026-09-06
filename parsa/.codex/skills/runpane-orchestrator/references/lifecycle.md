# Lifecycle

## Lifecycle State Machine

Use these durable states and transition only on recorded evidence:

1. `queued`: resolve exact repo/issue/scope and authorization.
2. `investigating`: use `investigate` when behavior/root cause is unknown.
   When complete, route the evidence to `discussion`, then select the lane
   and run the planner that lane names.

3. `planning`: require a factually clean approved plan/brief. If implementation
   through PR readiness is already authorized, the clean plan advances without
   another approval prompt. Use an available `arena` only when independent candidates would resolve
   material design uncertainty; record that decision in the plan.
4. `implementing`: use `implement` in the implementation panel. Keep feeding
   missing plan tasks or recoverable blockers back until complete. A work item
   naming one metric and a target runs `hillclimb` as the implementation loop:
   baseline first, then one change per measurement, accept or revert.
5. `implementation_review`: use a fresh `implementation-reviewer` panel. Return
   legitimate fixes to the implementation authority and repeat on the new head.
6. `preparing_pr`: use `prepare-pr` in the implementation authority to create
   scoped commits, safely rebase, check, push, publish the authorized visual,
   and create/update a non-draft PR. A semantic conflict is a blocker.
   Post-PR order is fixed: review, then QA.
7. `pr_open`: heavy only, satisfied inside the orchestra handoff by its zone
   reviews and Must-Fix gate. Light and medium skip this state. Where it runs
   here: fresh current-head post-PR review panels, observed to completion;
   actionable feedback routes through the interrupt below, and only a completed
   clean review advances to QA.
8. `pr_qa`: once the PR exists — reviewed, where the lane runs state 7 — use a
   fresh `pr-test-automation`
   panel. Store reproducible current-head evidence and remaining manual gaps.
9. `ci_rereview`: heavy only, satisfied inside the orchestra handoff. The wait
   for current-head required checks survives in every lane through the PR-ready
   gate; the independent re-review is what light and medium skip.
10. `ready_to_merge`: enter only when every readiness predicate in the entrypoint's Exact PR-Ready Gate is true.
11. `blocked`: record the exact missing decision/grant/conflict and keep
    monitoring other streams. When it clears, resume by deriving the earliest
    incomplete gate from live state.

### Review Feedback Interrupt

From any post-PR state, actionable review feedback interrupts the normal next
transition. Invoke `gh-address-comments` in the implementation authority. If a
fix changes the head, return through implementation review, PR update, QA, and
required checks — and, in the heavy lane, independent re-review. If feedback requires only an authorized explanation/resolution,
verify the GitHub readback and resume. Never stall waiting for a review that has
not arrived.

Normal whole-tree sync supplies the repo-owned `gh-address-comments` skill. If
Pane's raw-download fallback lacks it, record that degraded condition and run
this complete fallback without claiming the skill was invoked:

1. Query all paginated GitHub GraphQL `reviewThreads`, reviews, and top-level PR
   comments plus `reviewDecision`, including resolution, review states, anchors,
   commit OIDs, and bodies/replies, then recheck the PR head.
2. Cluster unresolved actionable, informational, duplicate, outdated, resolved,
   and conflicting thread and top-level feedback. Outdated does not mean
   resolved; bind reviews to the current commit and treat actionable top-level
   comments as open until evidence or an authorized response addresses them.
3. Send authorized code fixes to the implementation authority. Serialize any
   authorized reply/resolution as JSON input, read it back, and re-query all
   pages until both unresolved-thread counts and the actionable top-level count
   are zero and no effective change request remains.
