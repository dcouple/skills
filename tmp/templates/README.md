# Format Templates

Draft formats for every artifact in the Orchestra workflow. Two kinds:

- **`skills/`** — **document formats** (persisted files written to `./tmp/<id>/`). One folder per skill, holding the doc(s) that skill produces.
- **`agents/`** — **agent output formats** (structured returns a sub-agent hands back *in-conversation* — NOT written to disk). One folder per sub-agent.
- **`shared/`** — blocks reused across several templates (verification criteria, system analysis).

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

## Map

| Producer | Kind | Template(s) |
|---|---|---|
| `/create-feature` · `/create-epic` | doc | `skills/create-feature/feature-ticket.md`, `skills/create-epic/epic-spec.md` |
| `/create-issue` | doc | `skills/create-issue/bug-report.md` |
| `/do` | doc | `skills/do/implementation-plan.md`, `wrap-up-report.md` |
| `/postmortem` | doc | `skills/postmortem/postmortem.md` |
| Plan Reviewer | output | `agents/plan-reviewer/review-report.md` |
| Code Reviewer | output | `agents/code-reviewer/review-report.md` (security findings tagged `(security)` inside Must/Should Fix) |
| Code Researcher | output | `agents/code-researcher/codebase-findings.md` |
| Web Researcher | output | `agents/web-researcher/research-dossier.md` |
| Investigator | output | `agents/investigator/root-cause-finding.md` |
| App user | output | `agents/app-user/verification-result.md` |
| Implementer | output | `agents/implementer/implementation-result.md` |
| shared | block | `shared/verification-criteria.md`, `shared/system-analysis.md` |
