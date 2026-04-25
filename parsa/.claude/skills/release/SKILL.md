---
name: release
description: Creates or updates a staging → main release PR with a summary of all merged PRs and a prioritized four-tier testing checklist. Use when preparing a release for production.
argument-hint: "[optional: PR title]"
disable-model-invocation: true
---

# Release Agent

Create (or update) a pull request merging `staging` into `main` with a full release summary and prioritized test checklist.

## Step 1: Identify What Changed

### Fetch latest refs

```bash
git fetch origin main staging
```

### Get the list of PRs merged into staging since main

Use the commit log between main and staging to identify individual PRs:

```bash
git log origin/main..origin/staging --oneline --merges
```

Also get the full diff summary for context:

```bash
git diff origin/main...origin/staging --stat
```

### Extract PR numbers

From the merge commits, extract PR numbers (they typically appear as `(#1234)` in merge commit messages). For each PR number, fetch its details:

```bash
gh pr view <number> --json title,body,number,author,files,labels
```

If there are commits that don't correspond to a PR (direct pushes to staging), group them separately as "Direct commits."

### Read the actual diff

For each PR, understand what changed:

```bash
git log origin/main..origin/staging --oneline --no-merges
```

Read the full diff to understand all changes:

```bash
git diff origin/main...origin/staging
```

## Step 2: Build the Release Summary

For each PR merged into staging, write a concise summary covering:
- What the PR implemented or fixed
- What areas of the app are affected (API, webapp, shared, infra)
- Any notable technical details (schema changes, new endpoints, new dependencies)

Order PRs chronologically (oldest first).

## Step 3: Generate the Testing Checklist

Analyze all changes across every PR and produce a **single consolidated testing checklist** with four tiers. Tests should be specific to what actually changed — not generic app tests.

### Tier definitions

**🔴 Must Test** — Things that will break the app or lose data if wrong. Includes:
- Data mutations (create, update, delete flows)
- Auth and permission changes
- Database schema changes and migrations
- Payment/billing logic
- API breaking changes (changed request/response shapes)
- Security-sensitive code

**🟡 Important to Test** — Significant user-facing changes that should work correctly. Includes:
- New UI pages or flows
- Modified business logic
- New or changed API endpoints
- State management changes
- WebSocket / real-time changes
- Third-party integration changes

**🔵 Nice to Test** — Lower-risk changes worth a quick check. Includes:
- Styling and layout changes
- Copy/text updates
- Sort order or display logic
- Minor UX improvements

**⚪ Not Important** — Changed but very low risk. Skip unless you have time. Includes:
- Refactors with no behavior change
- Dev tooling and config changes
- Documentation updates
- Dependency bumps with no API changes
- Code cleanup

### Test format

Each test item should include:
- A specific, actionable description of what to verify
- Which PR introduced the change (by number)
- Brief steps if the test isn't self-explanatory

## Step 4: Identify Pre-Deploy Requirements

Scan the full diff for anything that needs to happen **before or during** the production deploy. This section is critical — missing an ops requirement can cause the deploy to fail or the app to break.

### 4a: Schema Changes

Check if `apps/api/src/shared/db/schema.ts` was modified:

```bash
git diff origin/main...origin/staging --name-only | grep schema.ts
```

If schema.ts changed:
1. Run `npm run db:diff:prod` and capture the generated SQL.
2. Wrap it in a transaction block (`BEGIN; ... COMMIT;`).
3. Include the actual SQL in the PR description under the Schema Changes section.
4. If destructive SQL appears (DROP, ALTER type), flag it prominently.

If schema.ts was NOT changed, omit the Schema Changes section.

### 4b: Environment Variables & Secrets

Search the diff for new `process.env.*` references, changes to `config/`, or new entries in `config/secrets-mapping.json`:

```bash
git diff origin/main...origin/staging -- '*.ts' '*.json' | grep -E 'process\.env\.' | grep '^\+'
git diff origin/main...origin/staging --name-only | grep -E '(config/|\.env)'
```

For each new environment variable or secret found:
- Note the variable name and which service needs it (API, webapp)
- Check if it already exists in `config/secrets-mapping.json` — if not, flag it
- Indicate whether it needs to be set in Cloud Run, Firebase, or GCP Secret Manager

### 4c: Infrastructure Changes

Check for Terraform or infra changes:

```bash
git diff origin/main...origin/staging --name-only | grep -E '(infra/|\.tf$|Dockerfile|\.github/workflows/)'
```

If infra files changed:
- Summarize what changed (new resources, modified configs, workflow changes)
- Flag if `terraform plan` / `terraform apply` needs to run before deploy
- Flag any CI/CD workflow changes that affect the deploy process itself

### 4d: New Dependencies & Third-Party Services

Check for new package dependencies or third-party service integrations:

```bash
git diff origin/main...origin/staging -- package.json package-lock.json
```

Also search the diff for new API client instantiations, SDK imports, or webhook URLs that suggest a new external service dependency.

### 4e: Data Backfills & One-Time Scripts

Check if any PR descriptions or commit messages mention backfills, data migrations beyond schema changes, or one-time scripts that need to run. Also look for new files in scripts/ or similar directories:

```bash
git diff origin/main...origin/staging --name-only | grep -iE '(script|backfill|migrate|seed)'
```

### Compile the Pre-Deploy Requirements

Gather all findings from 4a–4e into a single **Pre-Deploy Requirements** section. If nothing was found in a sub-step, omit it. If NO pre-deploy requirements were found at all, include a simple "No pre-deploy requirements — this is a clean code-only release." note.

## Step 5: Run Automated Checks

Run these and record results:

```bash
npm run typecheck
npm run lint
```

## Step 6: Create or Update the PR

### Check for existing release PR

```bash
gh pr list --base main --head staging --json number,title,url,state
```

### PR Description Template

Use this exact structure for the PR body:

```markdown
## Release Summary

**Staging → Main** | [X] PRs | [Y] files changed

### PR #[number]: [title]
[2-3 sentence summary of what this PR implemented and why]
- **Areas affected:** [API / Webapp / Shared / Infra]

### PR #[number]: [title]
[2-3 sentence summary]
- **Areas affected:** [areas]

<!-- Repeat for each PR -->

<!-- If there are direct commits not associated with a PR -->
### Direct Commits
- `[sha]` [commit message] — [brief explanation]

---

## Testing Checklist

### 🔴 Must Test
- [ ] **[Specific test scenario]** (PR #[number])
  _Steps: [how to verify]_
- [ ] ...

### 🟡 Important to Test
- [ ] **[Specific test scenario]** (PR #[number])
  _Steps: [how to verify]_
- [ ] ...

### 🔵 Nice to Test
- [ ] **[Specific test scenario]** (PR #[number])
  _Steps: [how to verify]_
- [ ] ...

### ⚪ Not Important
- [ ] **[Specific test scenario]** (PR #[number])
- [ ] ...

### Areas Not Affected
[List major app areas with NO changes so the team can skip them]

---

## Pre-Deploy Requirements

<!-- If no requirements found: -->
<!-- No pre-deploy requirements — this is a clean code-only release. -->

<!-- Include only the sections that apply: -->

### Schema Changes
- [ ] Migration SQL reviewed
- [ ] Migration applied to staging
- [ ] Migration applied to production

#### Production Migration SQL
⚠️ Run this SQL against the production database BEFORE deploying:
```sql
BEGIN;
-- actual SQL here
COMMIT;
`` `

### Environment Variables & Secrets
- [ ] `[VAR_NAME]` added to [Cloud Run / Firebase / GCP Secret Manager] for [service]

### Infrastructure
- [ ] Terraform plan reviewed for [description]
- [ ] Terraform applied via CI

### New Dependencies
- [ ] [dependency/service] — [what it's used for, any API keys needed]

### Data Backfills
- [ ] [description of backfill/script and when to run it]

---

## Automated Checks
- [x/fail] TypeScript compilation
- [x/fail] Linting

---
*Generated by `/release`. To regenerate after new changes land on staging, run `/release` again.*
```

### Create or update

If no release PR exists:
```bash
gh pr create --base main --head staging --title "<title>" --body "$(cat <<'EOF'
<body>
EOF
)"
```

If a release PR already exists, update it:
```bash
gh pr edit <number> --body "$(cat <<'EOF'
<body>
EOF
)"
```

Use `$ARGUMENTS` as the PR title if provided, otherwise use: `Release: [date] — [brief summary of key changes]`

## Step 7: Report

Present the result:

```
Release PR ready.

PRs included:
- #1234: [title]
- #1235: [title]
- ...

Tests generated:
  🔴 Must test: X items
  🟡 Important: X items
  🔵 Nice to test: X items
  ⚪ Not important: X items

Automated checks:
  Typecheck: PASS/FAIL
  Lint: PASS/FAIL

PR: <url>
```

## Rules

- Be SPECIFIC — every test must trace back to an actual change in the diff, not generic app behavior
- Keep the total checklist practical — aim for 10-20 test items total, not 50
- The summary should help someone who hasn't seen any of the PRs understand what this release contains
- If the diff between staging and main is empty, tell the user there's nothing to release and stop
- Do not push any code — the PR is created directly from the existing staging and main branches on the remote
