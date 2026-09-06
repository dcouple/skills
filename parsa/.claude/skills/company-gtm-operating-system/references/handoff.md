# Handoff

### 9. Create The Docs Knowledge Base

Write a routed `docs/README.md` and focused foundation docs.

Recommended root docs:

```text
docs/README.md
docs/product-brief.md
docs/market-foundation.md
docs/competitor-and-industry-map.md
docs/keywords.md
docs/gtm-foundation.md
docs/gtm-ops-and-vendor-stack.md
docs/strategic-analogies.md
docs/repo-structure.md
docs/cost-and-portability-foundation.md
docs/open-questions-and-decisions.md
docs/next-steps.md
docs/research-index.md
```

Add domain folders from Step 6.

**Success criteria**: `docs/README.md` routes by intent and all important decisions are reachable from it.

### 10. Review For Missed Nuance

Do a final pass for:

- user corrections
- named analogies
- competitor references
- domain decisions
- keyword priorities
- infra constraints
- vendor decisions
- open questions
- docs routing
- duplicate or redundant domain docs
- claims that are too strong
- decisions that belong in root docs but are buried in a domain doc

**Success criteria**: The docs preserve the actual reasoning and tradeoffs, not just a sanitized summary.

### 11. Commit And Push If Requested

If working in a Git repo and the user wants the foundation saved:

1. Run `git status --short --branch`.
2. Review the diff.
3. Stage only relevant docs.
4. Commit with a scoped docs message.
5. Push to the requested branch or default branch.
6. Confirm clean status.

**Success criteria**: The docs foundation is committed and pushed, with commit SHA reported to the user.
