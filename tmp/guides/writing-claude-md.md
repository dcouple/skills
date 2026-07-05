# Writing CLAUDE.md Files — Definitive Guide

> Audience: agents creating or editing `CLAUDE.md` files in dcouple projects.
> Companion docs: `writing-skills.md`, `writing-subagents.md`.

---

## 1. Why this is the highest-leverage document you own

A `CLAUDE.md` is **standing project memory**: the conventions and facts every agent must obey. It matters more than any single skill because:

- **It is always in context.** Every turn pays for it, and every downstream model inherits it.
- **Our agents are told to obey it explicitly.** The `implementer` agent's first quality rule is "Follow conventions from CLAUDE.md files (root + app-specific)." The `plan-reviewer` reads them before judging a plan and flags any plan that violates them.

Get this right once and every implementer and reviewer produces code that looks like one author wrote it. Get it wrong and every agent quietly drifts.

---

## 2. Precedence — where CLAUDE.md sits

Fixed order, highest wins:

1. **The human's explicit words** (this session's instructions).
2. **The project's own system** — existing `CLAUDE.md`, tokens/theme files, established patterns in the code.
3. **The model's defaults.**

`CLAUDE.md` *is* layer 2. Its whole job is to make layer 2 explicit so the model never falls back to layer 3 (guessing). When you edit it, you are encoding the middle layer — do it clearly.

---

## 3. What belongs in it

### 3.1 Commands
The exact lines an agent runs, especially in its quality loop after each section:

```markdown
## Commands
- Typecheck:  `npm run typecheck`
- Lint / fmt: `npm run lint` · `npm run format`
- Test:       `npm run test`
```

Our `implementer` runs typecheck/lint/format after every major section and **won't proceed on errors** — so these must be correct and current.

### 3.2 Conventions (the house rules a stranger couldn't guess)
Short, enforceable, specific:

```markdown
## Conventions
- TypeScript strict — no `any` without justification
- Prefer editing existing files over creating new ones
- Remove deprecated code; don't leave it around
- Use existing patterns rather than inventing new approaches
```

### 3.3 Implementation order & patterns
The build sequence per surface — this is what keeps five different implementers coherent, and it's what the reviewer checks against:

```markdown
## Implementation order
- API:  validator → service → controller → route
- DB:   schema.ts → service integration
        # migrations handled by /implement after review — agents do NOT run db:diff themselves
- UI:   types → API client → hooks → components
```

### 3.4 Map & handoffs
Where things live and where inter-phase artifacts go:

```markdown
## Handoffs
- Specs → ./tmp/specs/    Plans → ./tmp/    Business → .business/
```

### 3.5 Gotchas
The two or three landmines that have bitten before. Point to a detail file rather than inlining a wall of text.

---

## 4. How to write it

- **Keep it lean.** It's loaded on every turn — every line is a permanent context tax. The root file should be **rules and pointers**; push depth into referenced files (`docs/…`, app-specific `CLAUDE.md`s) that load on demand.
- **Explain the *why* where it changes behavior.** "Migrations are handled by `/implement` after review, so don't run `db:diff` yourself" survives edge cases far better than a bare "don't run db:diff." A rule the model understands generalizes; a rule it merely obeys breaks at the boundary.
- **Reserve hard prohibitions for real failure modes.** A `CLAUDE.md` that is all ALL-CAPS "NEVER" reads as noise and gets discounted. Make the few genuine musts stand out by being few.
- **Be specific and current.** Wrong commands or stale conventions are worse than none — agents follow them confidently off a cliff. Update `CLAUDE.md` in the same change that changes the convention.
- **Write from the maintainer's side.** Name things as the team recognizes them; encode what's true about *this* repo, not generic advice any model already has.

---

## 5. Layering

- **Root `CLAUDE.md`** — repo-wide truth: stack, commands, conventions, directory map, handoff locations.
- **App/service-specific `CLAUDE.md`** — placed next to the code it governs; local commands, local patterns, local gotchas.

The `implementer` and `plan-reviewer` **read both** (root + app-specific). Don't duplicate the root rules in every app file — put shared truth at the root and only the local deltas in the app file.

---

## 6. Anti-patterns

1. **Kitchen-sink file** — hundreds of lines of everything. It's always-loaded; bloat is a permanent tax. Trim to rules + pointers.
2. **Stale commands/conventions** — the worst failure, because agents obey confidently. Keep it current with the code.
3. **Generic advice** — "write clean code," "add tests." Adds tokens, changes nothing. Encode only repo-specific truth.
4. **Wall of NEVERs** — undifferentiated prohibitions get discounted. Few, real, explained.
5. **Rules without the why** — brittle at edge cases. Give the reason when it matters.
6. **Duplicated layers** — same rules copy-pasted into every app file. Root holds shared truth; app files hold deltas.

---

## 7. Quality checklist

- [ ] Commands are exact and currently correct (typecheck / lint / format / test).
- [ ] Conventions are specific, enforceable, and repo-specific (not generic).
- [ ] Implementation order / patterns documented for each surface the reviewer checks.
- [ ] Handoff locations (`./tmp/specs/`, `.business/`, etc.) stated.
- [ ] Hard prohibitions are few and each has a reason where the reason isn't obvious.
- [ ] Root vs app-specific layering is clean — no duplicated shared rules.
- [ ] File is lean; deep detail is in referenced files, not inline.
- [ ] Precedence respected — this encodes the project layer, and defers to the human's explicit words.

---

## 8. Skeleton to start from

```markdown
# CLAUDE.md — <service or repo>

## Stack
<language, framework, key libs — one line each>

## Commands
- Typecheck:  <cmd>
- Lint / fmt: <cmd> · <cmd>
- Test:       <cmd>

## Conventions
- <house rule 1>
- <house rule 2>

## Implementation order
- API: <sequence>
- DB:  <sequence>   # note who owns migrations
- UI:  <sequence>

## Handoffs
- Specs → ./tmp/specs/   Business → .business/

## Gotchas
- <landmine> — see <detail file> for the full story
```
