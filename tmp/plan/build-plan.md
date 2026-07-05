# Build Plan — Dcouple Software Development Orchestra

> Living tracker for building the agents, skills, and document formats from
> `tmp/assets/agent-overview-roadmap.png`. Check items off as we land them.
> Status: **Planning** · Started 2026-07-05.

---

## What we're building

The "Orchestra": an orchestrated software-development workflow where **Fable (Overseer)** conducts, sub-agents do specialized work, and a single **`/do`** skill runs the full plan → review → implement → verify → clean up → review → wrap-up pipeline autonomously against a work item, then opens a PR for human review.

> **Locations:** this plan lives in `./tmp/plan/`. Drafted format templates live in
> `./tmp/templates/`, with a folder per skill or sub-agent (`skills/…`, `agents/…`).

## Principles (from the roadmap)

1. Humans are responsible for all work completed by their agents.
2. If humans aren't continually learning, the business stagnates.
3. Humans maintain control of the system — conductor of an orchestra.

---

## Locked decisions (2026-07-05)

- **Build order:** Claude-first core spine now (Phase 1); Codex integration second (Phase 2).
- **Sub-agent models (Phase 1):** built as **Claude placeholders** with the *target* Codex model noted in each file, so Phase 2 is a mechanical swap.
- **`/do` opens the PR** at the end.
- **`/do` does NOT create a branch** — it assumes the user has already checked out / set up the working branch before running `/do`.
- **Verify:** the work item (ticket/spec) **must** carry explicit verification criteria. The verify step confirms the feature is *actually done and verified*, via one or more of: writing manual tests, computer-use navigation of the app + recording a video, or running verification scripts.
- **Clean up:** defensive, not opportunistic. Look for ways to simplify the feature/code, combine with existing functionality, and confirm deprecated code is removed. Nothing comprehensive.
- **PR review includes a security review.**
- **Epics run sequentially** (one phase's channel completes before the next starts).
- **GitHub:** used **only for PRs** for now. GitHub Metadata template is **out of scope**. All work-item / plan / review / report docs are generated **locally in `./tmp`**.
- **Scheduled loops (Production Error / Code Quality / Security) are deferred** to a later phase.

## Resolved decisions (2026-07-05, round 2)

- **Terminology:** renaming principles accepted (Feature Ticket, Bug Report, Epic Spec, Review Report, Postmortem; umbrella = "work item"). Confirm Feature Ticket vs Feature Brief.
- **`/do` exit criteria:** loop until reviewers report **zero "Must Fix"**, hard cap **3 passes** at the plan stage and **3** at the final-review stage; on cap-out, proceed to wrap-up and flag unresolved items. ✅
- **Postmortem:** stays a **local `./tmp` doc** for now; defer the auto-created improvement issue. ✅
- **Epic PR shape:** **one PR for the whole epic**; phases commit sequentially to the pre-set branch. ✅
- **Wrap-Up assets (video/screens):** add later; start text-only. ✅

## Work-item content principle (2026-07-05, round 3) — LOCKED

- **Keep work items lean; leverage the model's inherent capability.** Do not over-load a `/do` loop with pre-chewed research or exhaustive detail.
- **A work item carries only high-signal core:** intent + desired end state, **verification criteria**, the few *locked* architecture directions, and out-of-scope.
- **Preliminary research lives as the work item itself or in optional reference docs** — not as long distilled narratives inside the ticket.
- **Optional reference sources** (discussion transcript, error traces, mock-ups, images/videos, web references, System Analysis) are stored in `./tmp` and **linked, not inlined**.
- **`/do` starts fresh** each run: it reads the work item, then pulls reference docs *as it works*. Sources are there to help the loop (and future loops), not to spoon-feed it.

## Output-format conventions (2026-07-05, round 4) — LOCKED

Applied across all templates after a 3-researcher pass over `tmp/reference/` +
`tmp/research/` (full change list: `./template-improvements.md`):

- **Severity:** `Must Fix / Should Fix / Nice to Have`, with calibration prose in both review reports.
- **Status-first returns:** every agent output opens with a one-line parseable verdict/status (Implementer uses `DONE | DONE_WITH_CONCERNS | BLOCKED | NEEDS_CONTEXT`).
- **Countable loops:** review reports carry a counts line + stable finding IDs (`MF-1`/`SF-1`); re-reviews mark priors `fixed | persists | new`; Must-Fix items cite the `D#`/`AC#` they violate or say "new issue".
- **Security folded in:** `(security)` tags inside Must/Should Fix — no separate section outside the Must-Fix gate.
- **Evidence:** `file:line` on findings, quoted evidence on passes, `⚠️ Cannot verify` lane instead of guessing.
- **Anti-padding:** empty optional sections omitted; literal "none" only where absence is ambiguous; "TBD" in a plan = plan failure.
- **Confidence:** `confirmed | likely | hypothesis` (words, no emoji).
- **Plan:** opens with a Files-changed table (file · new/modify/delete · one clause); wrap-up reports only deltas vs it.
- **Frontmatter:** `id:` on items / `item:` on derived docs; status `draft | ready | done`; `pr:` on every item type.

## Still open

- [ ] Confirm "Feature Ticket" vs "Feature Brief" wording.
- [x] Draft the templates (task 1a) using the lean model below. *(drafted + revised per round-4 conventions)*

---

## Document taxonomy & naming (PROPOSED — pending confirmation)

| Roadmap term | Proposed name | What it is | Produced by |
|---|---|---|---|
| Bug Ticket | **Bug Report** | One defect: summary, repro, desired fixed-state, **verification criteria**, prevention | `/create-issue` |
| Implementation Ticket | **Feature Ticket** | One feature: intent, desired end state, key architecture directions, **acceptance + verification criteria**, out-of-scope, reference docs | `/create-feature` |
| Epic | **Epic Spec** | Multi-phase workstream: problem, goals, key decisions, **phases table**, per-phase verification | `/create-epic` |
| Implementation Plan | **Implementation Plan** *(keep)* | Per issue/phase: context recap, ordered file-level tasks, verification steps, out-of-scope | `/do` |
| PR review | **Review Report** | Findings as **Must Fix / Should Fix / Optional-Notes**; used for both plan review and PR/security review | reviewers inside `/do` |
| PR Wrap-Up Report | **Wrap-Up Report** *(keep)* | `/do`'s self-report: what was built, verification evidence (screens/video), residual risks | `/do` |
| compound engineering doc | **Postmortem** | Post-mortem: why `/do` missed, what to change so it doesn't recur | `/postmortem` |
| System Analysis doc | **System Analysis** | Supporting deep-dive on current-state code/system, used as reference input | researchers / investigator |
| — | **umbrella: "work item"** | Any of Bug Report / Feature Ticket / Epic Spec — the input `/do` consumes | — |

**Proposed `./tmp` layout — one folder per work item, sources travel with it:**
```
./tmp/<id>/
  item.md            the work item (bug / feature / epic) — LEAN, high-signal
  refs/              OPTIONAL sources, linked from item.md, pulled by /do as needed
    discussion.md      LLM discussion transcript
    error-trace.txt    (bugs)
    mockup.png         (features)
    system-analysis.md (optional current-state deep-dive)
  plan.md            Implementation Plan (per issue; per phase for epics)
  wrapup.md          Wrap-Up Report (posted to PR)
  postmortem.md      Postmortem (optional, local for now)
```
> Review Reports are **NOT** files. Reviewers run in multiple loops; each pass's
> findings are returned **in-conversation** to the Overseer, consumed immediately,
> and the final review's outcome is folded into `wrapup.md`.

**Core vs. references:** everything in `item.md` is *required, minimal, high-signal*.
Everything in `refs/` is *optional* and *linked* — `/do` starts fresh and reads
refs only as the work calls for them.

---

## Template registry (what we author in task 1a)

There are **two kinds of template**: persisted **document formats** (files on disk) and
**agent output formats** (structured returns a sub-agent hands back in-conversation).

### A. Document formats (persisted files)

| Template | File | Produced by | Notes |
|---|---|---|---|
| **Bug Report** | `item.md` | `/create-issue` | Spine: root cause → correct behavior. |
| **Feature Ticket** | `item.md` | `/create-feature` | Lean core + linked refs. |
| **Epic Spec** | `item.md` | `/create-epic` | + sequential phases table. |
| **Implementation Plan** | `plan.md` | `/do` (plan stage) | Updated with progress / plan-deltas during implement. |
| **Wrap-Up Report** | `wrapup.md` | `/do` | Posted to the PR; folds in final review outcome. |
| **Postmortem** | `postmortem.md` | `/postmortem` | Optional; local for now. |
| **System Analysis** | `refs/system-analysis.md` | researchers / investigator | Optional reference source. |
| **Verification-criteria block** | (embedded) | the `/create-*` skills | Shared EARS-style block reused by items + the verify stage. |

### B. Agent output formats (in-conversation returns — NOT files)

| Output | Returned by | Shape | Consumed by |
|---|---|---|---|
| **Review Report** | Plan Reviewer · Code Reviewer | verdict + counts first; Must Fix / Should Fix / Nice to Have with `MF-n`/`SF-n` IDs; each what·where·fix·violated `D#`/`AC#`; failure scenarios for bugs; security tagged `(security)` inside Must/Should | Overseer (loops back to plan/implement) |
| **Codebase findings** | Code Researcher | file:line refs, patterns, boundaries | plan stage |
| **Research dossier** | Web Researcher | cited findings (inline; persist to `refs/` only if durable) | plan / item authoring |
| **Root-cause finding** | Investigator | reproduction + cause + suggested resolution path | Bug Report authoring |
| **Verification result** | App user | what was exercised, pass/fail vs criteria, evidence | verify stage → wrap-up |
| **Implementation result** | Implementer | what was built, plan-deltas, blockers | updates `plan.md`, review stage |

---

## Authoring hygiene — required reading before writing any agent/skill file

Every file authored in 1b–1e follows the house guides (checklists included in each):

| When writing… | Follow | Backed by research |
|---|---|---|
| `SKILL.md` files (1c, 1d) | `../guides/writing-skills.md` | `../research/skill-files.md`, `../research/skill-library-comparison.md` |
| Sub-agent files (1b) | `../guides/writing-subagents.md` | `../research/agent-files.md` |
| `CLAUDE.md` / `AGENTS.md` touch-ups | `../guides/writing-claude-md.md` | — |
| Model choice per agent | routing table in the guides | `../research/model-routing-fable.md` |
| Output contracts | `../templates/README.md` Shared conventions + `./template-improvements.md` | round-4 pass |

Key hygiene rules to hold ourselves to: description field is the trigger — "Use when…" +
keywords, written for the model that *hasn't* loaded the body; body <500 lines, push depth
to `references/`; explain the why, no ALL-CAPS unless safety-critical; each sub-agent is
self-contained (fresh context) with an explicit output contract and least-privilege tools.

> ✅ Routing reconciled 2026-07-05: guides, field-manual artifact, and memory now all
> carry the roadmap-diagram routing — Codex 5.5 **high** for Investigator/reviewers,
> **med** for Implementer, Sonnet for researchers/App user, Fable as Overseer.

## Phase 1 — Claude-first core spine

### 1a. Templates (see registry above) — ✅ drafted + revised (round-4 conventions)
Document formats (persisted):
- [x] Bug Report · [x] Feature Ticket · [x] Epic Spec
- [x] Implementation Plan · [x] Wrap-Up Report · [x] Postmortem
- [x] System Analysis (optional ref) · [x] Verification-criteria block (shared)

Agent output formats (in-conversation contracts):
- [x] Review Report ×2 (Must / Should / Nice to Have) · [x] Codebase findings · [x] Research dossier
- [x] Root-cause finding · [x] Verification result · [x] Implementation result

### 1b. Sub-agents (8)
Built as Claude placeholders; target Codex model noted in each file.

Authoring conventions (from the reference sweep — obra/mattpocock):
- Dispatch prompts live in sibling `*-prompt.md` files next to the skill: fenced prompt + `**Placeholders:**` legend + one-line `**Returns:**` contract — keeps SKILL.md lean.
- Fan-out briefs carry a word cap (~400) and a quote-the-source rule; the caller presents parallel reports side-by-side, never merges/reranks them.
- Template bodies use content-describing prose inside the skeleton, not bare `[TODO]` slots.
- No emoji/box-drawing chrome; no mandated pseudo-precise fields (offer the ⚠️ can't-verify lane instead); ALL-CAPS only for genuinely safety-critical rules.

- [x] **Overseer** — Fable (main session; conducts `/do` — no agent file by design)
- [x] **Investigator** — target Codex 5.5 high · placeholder Opus (reproduce + root-cause)
- [x] **App user** — Sonnet (verify + reproduce modes; browser MCP tools pinned, no Edit/Write)
- [x] **Code Researcher** — Sonnet (codebase exploration; file:line refs)
- [x] **Code Reviewer** — target Codex 5.5 high · placeholder Opus (diff + security; Bash noted as deliberate read-only-charter exception)
- [x] **Implementer** — target Codex 5.5 med · placeholder Opus (writes the diff)
- [x] **Plan Reviewer** — target Codex 5.5 high · placeholder Opus (audits the plan)
- [x] **Web Researcher** — Sonnet (external docs/best practices)

### 1c. `/do` skill (the pipeline) — ✅ `tyler/.claude/skills/do/SKILL.md`
- [x] Input handling: accept a Bug Report / Feature Ticket / Epic Spec by path (frontmatter `type` selects mode; refuses non-`ready` items)
- [x] Plan stage → Plan Reviewer loop (≤3, zero Must-Fix) → improve plan
- [x] Implement stage (Implementer)
- [x] Verify stage (App user / scripts / manual tests; own ≤3 verify-fix cap)
- [x] Clean up stage (defensive simplify + dedupe + remove deprecated)
- [x] PR review stage incl. security → fix-issues loop back to Implement (≤3, zero Must-Fix)
- [x] Open PR + run pr-test-automation (if available)
- [x] Wrap-Up Report → posted to PR
- [x] Fully autonomous until done (only stop: on default branch at preflight)

### 1d. Workflow skills *(restructured 2026-07-05, round 5 — see progress log)*
- [x] `/discussion <topic>` → pure clarify/understand/figure-out; dispatches code-researcher / web-researcher / investigator (+ app-user) as the question demands; produces NO artifacts
- [x] `/create-feature <title>` → captures the conversation into a Feature Ticket → learning gate
- [x] `/create-epic <title>` → captures the conversation into an Epic Spec → learning gate
- [x] `/create-issue <title>` → Bug Report; runs investigator itself if no root cause established yet → learning gate
- [x] `/postmortem <PR>` → human feedback → gap root-caused in our system → Postmortem + ONE proposed (not applied) system change
- [x] ~~`/investigate`~~ — removed; folded into the `investigator` sub-agent, dispatched from `/discussion` and `/create-issue`

### 1e. Epic handling
- [x] `/do` detects Epic Spec and runs each phase's channel **sequentially** (Step 7; per-phase `plan-<n>.md`; phase ✓ ticked in spec table)
- [x] Epic PR shape: one PR after the last phase; phases commit as they complete

---

## Phase 2 — Codex integration

- [x] Swap Implementer, Code Reviewer, Plan Reviewer to `codex exec` via the Claude-side **`codex` dispatch skill** (`tyler/.claude/skills/codex/`) — role table pins model/effort/sandbox (implementer: gpt-5.5 medium, workspace-write, `resume --last` across fix loops; reviewers: gpt-5.5 high, read-only, ephemeral). Claude agents remain as fallback (implementer) / dual lane (reviewers).
  - [ ] Investigator swap — deferred: stays a Claude Opus sub-agent for interactive dispatch from `/discussion` and `/create-issue`.
- [x] **Dual reviewers (locked 2026-07-05):** every review spawns **two reviewers in parallel — Codex 5.5 high + Claude Opus** — for both the plan-review and PR-review stages. The Overseer considers both reports before proceeding: the Must-Fix gate is the **union** of both reviewers' Must Fix items (deduped by the Overseer; `D#`/`AC#` citations are the dedup key), so the loop doesn't proceed until *both* report zero Must Fix. Different vendor, different blind spots — the reports are considered side-by-side, never merged by rerank. Wired into `/do` Steps 2 and 6.
- [x] `.codex/skills/` role skills (implementer, plan-reviewer, code-reviewer) — **thin pointers** into `~/.claude/agents/` charters + `~/.claude/references/` formats, not a full skill mirror: Claude stays the only orchestrator, so `/do` and the workflow skills are not mirrored into Codex.
- [x] `agents/openai.yaml` interface files (one per `.codex` role skill)
- [ ] Validate cross-harness parity (same pipeline, equivalent results) — needs a real `/do` test-drive

---

## Deferred (later)

- [ ] Production Error loop (daily: Sentry / crash logs / complaints → Bug workflow)
- [ ] Code Quality loop (weekly: Grafana / patterns / compound docs → refactor)
- [ ] Security loop (weekly: dep updates / vuln scan → patches)
- [ ] GitHub Metadata context; local items → real GitHub issues

---

## `/do` pipeline (reference)

| Stage | What it does | Agent (target model) |
|---|---|---|
| Plan | Produce Implementation Plan from the work item | Overseer + Code Researcher (Sonnet) |
| Plan review ⟲ | Audit plan; loop until zero Must-Fix (≤3) | Plan Reviewer (Codex high) |
| Implement | Write the diff per plan | Implementer (Codex med) |
| Verify | Prove it's done: tests / computer-use + video / scripts, against the item's verification criteria | App user (Sonnet) |
| Clean up | Defensive simplify, dedupe, remove deprecated | Implementer / Code Reviewer |
| PR review ⟲ | Correctness + **security** review; loop back to Implement until zero Must-Fix (≤3) | Code Reviewer (Codex high) |
| Wrap-up | Open PR, run pr-test-automation, post Wrap-Up Report | Overseer (Fable) |

---

## Progress log

- **2026-07-05** — Plan created. Locked build order, `/do` behavior, verify/cleanup/review scope, epic sequencing, GitHub-for-PRs-only, deferred scheduled loops.
- **2026-07-05** — Task 1a drafted: all templates written to `./tmp/templates/`; `/fix-and-improve` renamed `/postmortem`.
- **2026-07-05** — Round-4 output-format pass: 3 researchers audited templates against `tmp/reference/` + `tmp/research/`; 23 changes applied (see `./template-improvements.md`). Files-changed table restored to the plan format; shared conventions documented in `templates/README.md`. 1a checked off pending Tyler's final skim.
- **2026-07-05** — **Phase 1 built.** 7 agent files (5 new + implementer/plan-reviewer upgraded in place; legacy codebase-explorer/researcher/implementation-reviewer untouched for the legacy skills), `/do` with epic handling, `/discussion` + `/investigate` rewritten to the Orchestra, `/postmortem` new; templates copied into each skill's `references/`; `tyler/README.md` fronted with the Orchestra roster. Fresh-context Opus review: **Approve, 0 Must Fix, 5 Should Fix — all 5 applied** (app-user tools pinned + reproduce mode added; /do verify-loop cap fixed; code-reviewer Bash noted as deliberate exception; allowed-tools added to the three interactive skills). Remaining before merge: Tyler skims, rsyncs, and test-drives `/discussion` → `/do` on a real item.
- **2026-07-05 (round 5)** — **Clarity/capture split (Tyler's direction).** `/discussion` is now pure clarify/understand/figure-out (no work items, no verification criteria) and dispatches the investigator directly for defect questions; artifact creation moved to three manually invoked capture skills — `/create-feature`, `/create-epic`, `/create-issue` (which runs the investigator itself when no root cause exists). `/investigate` skill removed. Legacy skills retired: `/implement`, `/simple-plan`, `/create-plan`, `/create-spec`, `/create-ticket` (superseded by `/do` + the capture skills), plus legacy agents codebase-explorer / researcher / implementation-reviewer. Templates redistributed to the capture skills' `references/`; taxonomy "Produced by" updated.
- **2026-07-05 (round 6)** — **All utilities retired (Tyler's direction).** `/commit`, `/prepare-pr`, `/release`, `/research-web`, `/review` removed: web research is the `web-researcher` agent, review is the `code-reviewer` agent, and all commit/PR prep (selective staging, secret scan, `type:` messages, rebase + force-with-lease, PR body format) was folded into `/do` Step 8. The six Orchestra skills — `/discussion`, `/create-feature`, `/create-epic`, `/create-issue`, `/do`, `/postmortem` — are the entire skill surface.
- **2026-07-05 (round 7)** — **Single-copy references (Tyler's direction, informed by Pocock's "context pointer" pattern + Claude Code docs).** Agents can't be folders (flat `.md` only, per official docs), so a new `tyler/.claude/references/` tree (synced to `~/.claude/references/`) now holds every doc referenced by >1 skill or by any agent: the shared blocks (verification-criteria, system-analysis — previously duplicated ×3 across the capture skills) and all 7 agent output formats. Agent bodies replace their inlined formats with a Read-pointer plus a short non-negotiables safety net; capture skills point at `~/.claude/references/…`. `tmp/templates/` content moved to the live homes; its README is now the index. Skill-specific doc formats stay in each skill's `references/` (exactly one consumer, so no duplication).
- **2026-07-05 (round 8)** — **Phase 2 wired.** New Claude-side `codex` dispatch skill wraps `codex exec` per role; `/do` implement stage runs on Codex gpt-5.5 medium (Claude implementer fallback), both review loops run dual lanes (Codex high + Claude Opus, union Must-Fix gate). `tyler/.codex/skills/` role skills are thin pointers into the single-copy charters/formats, each with `agents/openai.yaml`. Investigator swap deferred (interactive dispatch). Remaining: parity test-drive of `/do` on a real item.
