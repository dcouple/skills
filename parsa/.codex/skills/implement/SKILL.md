---
name: implement
description: "Execute an authorized implementation plan through integration, relevant checks, and review."
argument-hint: "[plan file path]"
---

# Implement

Execute the authorized plan through working integration, checks, and review.
Plan approval includes ordinary in-scope local fixes and repeated affected
checks. Continue to the requested PR handoff if the user's task includes it.

## Resolve the work

Execute in this Codex session as the primary implementation owner.

Read the named plan and its intent source. Without a path, use the plan clearly
identified by the current task; ask if several ready plans are plausible.
The brief owns why and locked decisions; the plan owns execution shape; a
research dossier is supporting evidence. Load dossier sections only when an
implementation question or conflict requires them.

## Execution boundaries

Keep one owner for integration, source edits, and fix commits. Delegate only
bounded tasks with disjoint write scopes and a clear integration contract.
Respect the selected executor, repository policy, and active harness permissions.

Local edits, dependency changes needed by the plan, and non-secret local test
configuration are ordinary implementation work, subject to repository install
gates. They are not automatically manual steps. Production/shared environment
writes, destructive operations, secret changes, and additional scope require
a matching grant. Prepare the concrete change and continue independent work
while a blocked action awaits authorization. Never bypass a denied operation.

## Implement and verify

Use existing repository patterns and wire the complete runtime/user-facing path.
Update plan progress only when its completion condition is observable. Record
necessary implementation deltas; ask before weakening a locked requirement.

Discover the repo's validation commands from its instructions, manifests, and
CI. Run checks that cover the affected behavior and required gates, fix failures
caused by the change, and rerun affected checks. Reuse results on unchanged
inputs. Do not require a full suite or repeated builds for a prose-only edit.
Record pre-existing failures and unavailable checks separately from new failures.

For schema changes, discover the repository's migration workflow and generate
reviewable migrations before the dependent validation and final review. Include
all generated SQL, flag destructive statements, and use disposable local/test
fixtures only within the existing authorization. Do not apply a migration to a
shared or production database without a matching grant. Validation that depends
on an unapplied migration remains unverified.

## Review and complete

Use `implementation-reviewer` for a complete review of the finished change.

Reviewers check intent, task completeness, integration, and concrete failure
risks; they return findings to the implementation owner. An additional review
lane needs a repository requirement or an unresolved risk. Do not rerun clean
reviews on unchanged artifacts. Merge findings from active lanes before asking
product questions. Fix in-scope defects, then review the changed portion and
rerun affected checks. Honor any parent workflow's remaining review budget;
if it is exhausted with blockers, report them rather than reset the count.

Move the plan to `./tmp/done-plans/` only after required work and checks are
complete. Leave blocked plans in place with their actual status. Report the
outcome, evidence, and limitations. If PR preparation or QA is already
requested, continue into `prepare-pr` or that stage now; do not merely offer to
finish. Merge, release, deployment, and production changes remain separately
authorized actions.
