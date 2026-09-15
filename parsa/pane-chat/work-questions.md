# Pane Chat Work Questions

Use this shared guide when Pane Chat is asked questions about the user's work
rather than asked to start implementation.

## When To Use This

Use a read-only work question workflow for prompts like:

- "What have I been working on?"
- "What did I finish yesterday?"
- "What should I work on next?"
- "Which PRs are closest to shipping?"
- "What issues are real priority?"
- "What should I ignore for now?"

Do not turn these into implementation panes. Answer from evidence first:
RunPane state, active and archived panes, local repo activity, git branches,
GitHub PRs, GitHub issues, CI, review comments, and agent logs when available.

## Workflow Choice

- Use `pane-work-recap` for memory reconstruction: what happened, what shipped,
  what is still active, and what evidence exists.
- Use `pane-work-prioritizer` for queue judgment: what to do next, what is
  blocked, what is close to shipping, and what should not be started yet.

If the active agent cannot load those skills by name, follow the same behavior
from this guide and the cached skill copies under the Pane skill cache.

## Grounding In The Skill System

Name a useful next action and, when available, a matching skill. Examples from this collection:

- Unknown failure, crash, or regression: `investigate`.
- Fuzzy product idea or broad feature: `discussion`, then `create-ticket`.
- Crisp implementation issue: `plan`/`create-plan` or `simple-plan`, then
  `implement`.
- Completed branch that needs confidence: `implementation-reviewer` in Codex or
  `review` in Claude, then `pr-test-automation`.
- Branch that should become a PR: `prepare-pr`.
- Open PR with review findings: `implement` for fixes, then review again.
- PR that is ready but untested: `pr-test-automation`.
- Public docs, support copy, SEO, or marketing page: `page-strategy`,
  `page-review`, or `site-content-audit` before implementation.
- Business-facing artifact: `business-context -> business-discussion ->
  business-spec -> business-artifact -> business-artifact-reviewer`.
- Finished non-trivial work: `teach-back`; use `share-fix` only after explicit
  approval to post externally.

Prefer finishing work already near merge over starting a new backlog issue,
unless the new issue is a genuine incident, security problem, billing problem,
release blocker, or customer-facing regression.

## Answer Shape

Start with the answer:

```text
I would do <item> first, then <item>. The reason is <signal>.
```

Then include:

- ranked work items with links
- why each item is ranked there
- the next action
- the recommended next skill or workflow
- blockers or missing evidence
- a short "probably not next" section for noisy backlog

End with the evidence used and any gaps. Do not imply something shipped unless
the claimed stage is directly evidenced. Passing checks do not prove a merge, and a merge does not prove deployment.

If a saved recap or recommendation is requested and Grain is connected, keep it in the supplied task folder, or `Development Artifacts/YYYY-MM-DD-<task>`. Preserve privacy and needed local copies; otherwise use the normal handoff silently.
