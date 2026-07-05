# Format Templates — index

The templates drafted here **moved to their live homes** (single copy each —
no duplicates to drift). This file is the index.

Two kinds of format, three live locations:

- **Skill-specific document formats** (persisted files written to `./tmp/<id>/`,
  produced by exactly one skill) → that skill's own `references/` folder.
- **Agent output formats** (structured returns handed back *in-conversation* —
  NOT written to disk) and **shared blocks** (referenced by more than one skill,
  or by any agent) → `tyler/.claude/references/` (synced to
  `~/.claude/references/`).

Guiding principles (from `../plan/build-plan.md`):
- Work items are **lean and high-signal**. Optional raw sources live in `refs/`, linked not inlined.
- `/do` **starts fresh** and pulls refs as it works — we trust the model's capability.
- Files are for **durable handoffs between phases**; agent outputs are for **transient work inside a phase**.

## Shared conventions (all templates)

- **Severity scale (reviews):** `Must Fix / Should Fix / Nice to Have` — one vocabulary everywhere; the `/do` loops branch on the Must-Fix count.
- **Confidence scale:** `confirmed | likely | hypothesis` — words, never emoji.
- **Status-first:** every agent return opens with a one-line machine-parseable verdict/status the Overseer can branch on without reading the body.
- **Evidence:** findings cite `file:line`; a Pass quotes its supporting evidence; use the `⚠️ Cannot verify` lane instead of guessing.
- **Anti-padding:** omit optional sections when empty. Write a literal "none" only where absence is ambiguous (Plan deltas, Blockers, Not found). "TBD" in a plan is a plan failure.
- **IDs, cited across docs:** decisions `D1…`, acceptance criteria `AC1…`, review findings `MF-1`/`SF-1`. Re-reviews mark prior findings `fixed | persists | new`.
- **Frontmatter:** work items carry `id:`; derived docs (plan/wrapup/postmortem) carry `item:`. Status enum is `draft | ready | done` everywhere; every work item carries `pr:` (filled when `/do` opens it).

## Map (live locations, relative to repo root)

| Producer | Kind | Live template |
|---|---|---|
| `/create-feature` | doc | `tyler/.claude/skills/create-feature/references/feature-ticket.md` |
| `/create-epic` | doc | `tyler/.claude/skills/create-epic/references/epic-spec.md` |
| `/create-issue` | doc | `tyler/.claude/skills/create-issue/references/bug-report.md` |
| `/do` | doc | `tyler/.claude/skills/do/references/implementation-plan.md`, `wrap-up-report.md` |
| `/postmortem` | doc | `tyler/.claude/skills/postmortem/references/postmortem.md` |
| Plan Reviewer | output | `tyler/.claude/references/agents/plan-reviewer/review-report.md` |
| Code Reviewer | output | `tyler/.claude/references/agents/code-reviewer/review-report.md` (security findings tagged `(security)` inside Must/Should Fix) |
| Code Researcher | output | `tyler/.claude/references/agents/code-researcher/codebase-findings.md` |
| Web Researcher | output | `tyler/.claude/references/agents/web-researcher/research-dossier.md` |
| Investigator | output | `tyler/.claude/references/agents/investigator/root-cause-finding.md` |
| App user | output | `tyler/.claude/references/agents/app-user/verification-result.md` (verify + reproduce modes) |
| Implementer | output | `tyler/.claude/references/agents/implementer/implementation-result.md` |
| shared blocks | block | `tyler/.claude/references/verification-criteria.md`, `system-analysis.md` |
