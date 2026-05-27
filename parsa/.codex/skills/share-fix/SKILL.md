---
name: share-fix
description: After shipping a non-trivial fix, find related GitHub issues across the ecosystem, draft or post helpful human-sounding comments linking the fix and root cause, and optionally file upstream issues. Always requires explicit user approval before posting unless the user has already clearly approved posting in the current turn.
argument-hint: "[optional: commit SHA, PR number, or description of the fix]"
---

# Share Fix

Use this after a real fix reveals a bug, build-system trap, protocol gotcha, or upstream package issue that other projects are likely hitting too. The goal is to help other maintainers with concrete evidence, not to promote the project.

## Hard Rules

- Public comments and issues are irreversible. Draft first and ask approval unless the user has already explicitly approved posting in the current turn.
- Do not post identical comments across repos.
- Do not sound corporate. No "happy to help", "hope this helps", "wanted to share", or tied-bow summaries.
- First person singular by default: `i hit this`, `i tested`, `my fix`.
- Use the user's voice from memory and recent GitHub comments.
- No em dashes. Use commas, periods, colons, semicolons, or hyphen-minus.
- Do not guess. Read the fix, the emitted code or upstream source, and the target issue before commenting.
- If Codex subagents are not explicitly authorized by the user, do the research locally instead of spawning one.

## Voice Calibration

Before drafting comments:

1. Read relevant memory files from `~/.claude/projects/*/memory/` and project-local memory if present. Prioritize files about comment style, banned punctuation, project positioning, and user preferences.
2. Sample the user's existing comments in target repos when possible:

```bash
gh search issues --commenter <user> --repo <owner>/<repo> --limit 10 --include-prs
gh api repos/<owner>/<repo>/issues/<number>/comments --jq '.[] | select(.user.login == "<user>") | .body'
```

3. Match the user's real register. Lowercase starts, short technical notes, `fwiw`, `rn`, `w/`, and direct links are usually better than polished paragraphs.

## Understand The Fix

Read enough local context to explain the fix without hand-waving:

- commit diff or PR diff
- PR description and linked issue
- failing output, stack trace, or repro
- relevant source in the app
- relevant upstream package source or generated build output

Extract:

- root cause
- affected package and version
- user-visible symptom
- exact workaround or fix
- tested alternatives and their ranking
- validation commands and results

If the user asks for comprehensive outreach, include the ranking. Maintainers deciding between workarounds need to know why the chosen fix is better.

## Find Targets

Search broadly and rank by confidence:

- upstream package issues
- downstream PRs and issues with the same stack trace or symptom
- recent closed issues that future searchers will find
- high-signal discussions where a concrete fix adds value

Useful GitHub searches:

```bash
gh search issues '"exact error text"' --include-prs --limit 100 --json repository,number,title,state,url,body,commentsCount,updatedAt,isPullRequest
gh search issues '"package name" "symptom"' --include-prs --limit 100 --json repository,number,title,state,url,body,commentsCount,updatedAt,isPullRequest
gh search issues '"protocol or internal function" "tool name"' --include-prs --limit 100 --json repository,number,title,state,url,body,commentsCount,updatedAt,isPullRequest
```

Then inspect likely targets:

```bash
gh issue view <number> --repo <owner>/<repo> --comments --json title,state,url,body,comments
gh pr view <number> --repo <owner>/<repo> --comments --json title,state,url,body,comments
```

Skip low-confidence targets. A wrong comment is worse than no comment.

## Draft Or Post

If approval is still needed, present:

- ranked target list with confidence
- full draft comments
- any upstream issue draft
- question: `approve all, approve some, edit any, or skip any?`

If the user already approved posting in the current turn, post with heredocs:

```bash
gh issue comment <number> --repo <owner>/<repo> --body-file - <<'EOF'
fwiw i hit this too...
EOF
```

For PRs, `gh issue comment` works with the PR number.

## Comment Shape

Informal downstream comment:

```text
fwiw i hit this in <project> while debugging <symptom>.

<one or two short paragraphs explaining the root cause and why their workaround is related>

the ranking i found was <best fix>, then <second fix>, then <workaround>. <link to PR>
```

Upstream issue or maintainer-facing technical thread can be more structured, but still keep it human and concise.

## Record Outreach

After posting, create:

```text
tmp/outreach/YYYY-MM-DD-topic.md
```

Include:

- fix PR or commit link
- every comment URL
- skipped targets and why
- any follow-up needed

## Anti-Patterns

- no copy-pasted comments
- no marketing language
- no "me too" without new evidence
- no overclaiming that your fix is universal
- no commenting on every search result just because it matched a keyword
- no posting before approval unless the user already clearly approved posting in the current turn
