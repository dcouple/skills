---
name: seo-readability-pass
description: (foundational) Audit and rewrite website copy for voice consistency, readability, and first-timer comprehension.
allowed-tools:
  - Read
  - Edit
  - Write
  - Bash
  - Agent
  - WebSearch
  - WebFetch
when_to_use: >
  Use when the user wants to improve the readability, voice, or comprehension
  of product website copy. Examples: 'do a readability pass', 'fix the copy',
  'rewrite the docs to match my voice', 'the docs sound too technical',
  'do a comprehension audit', 'humanity pass on the website'.
model: claude-opus-4-6
---

# Content Readability Pass

Audit and rewrite all product-facing website copy so it reads like the founder
wrote it and a first-time reader can understand every page.

**Important**: Run this skill with Claude Opus 4.6. It performs significantly
better than 4.7 or 4.8 at copywriting and writing in specific voice styles.

## Goal

Every product page, docs page, landing page, and blog post should:
1. Match the voice guide (short sentences, contractions, no jargon, name the pain)
2. Pass the humanity test: a person who knows nothing about this space should understand it on first read
3. Use simple words to describe complex topics. Good writing explains complex things simply. If it sounds like a spec, rewrite it.

## Steps

### 1. Find the voice guide

Check for a voice guide in the repo: look in `AGENTS.md`, `VOICE.md`, `CLAUDE.md`,
or similar files for a "Writing Voice" or "Voice" section.

If no voice guide exists:
- Find the best-written pages in the repo (homepage, FAQ, founder-written copy)
- Derive voice rules from them
- Create a voice guide section in `AGENTS.md` (or `VOICE.md` if no AGENTS.md exists)

The voice guide should include:
- Sentence structure rules (short, active, second-person)
- Jargon blacklist with plain-language replacements
- A good example and a bad example from the actual site
- Tone markers (contractions, casual confidence, etc.)

**Success criteria**: A voice guide exists in the repo that any agent can reference.

### 2. Audit all product-facing pages

Spawn Explore agents to read every content page, docs page, landing page, and blog post.
Flag pages that have:
- Passive voice ("is distributed", "are provisioned", "has been tested")
- Jargon without context (technical terms used but never explained)
- Complex sentences (comma + semicolon in one sentence, nested clauses)
- Spec/architecture language instead of conversational language
- Feature dumps instead of problem/solution framing
- Sentences a first-timer wouldn't understand

Produce a severity-ranked list: NEEDS WORK > MINOR ISSUES > FINE.

**Success criteria**: A complete list of flagged pages with specific excerpts and line numbers.
**Human checkpoint**: Present the audit results and get confirmation on which pages to rewrite.

### 3. Rewrite flagged pages

For each page marked NEEDS WORK or MINOR ISSUES:
- Rewrite the copy following the voice guide
- Preserve all technical content and accuracy (same information, better language)
- Replace jargon with plain language or add immediate context
- Break long sentences into short ones
- Switch passive voice to active ("Pane does X" not "X is done by Pane")
- Use numbered steps for any workflow descriptions
- Name the pain: describe the problem the feature solves, not the feature abstractly

Work through pages in priority order: most-visited/important pages first.

**Success criteria**: All flagged pages rewritten. No jargon without context. No passive voice in explanatory sections.
**Rules**:
- Never lose technical accuracy while simplifying language
- Preserve all links, code blocks, and interactive components
- Don't add emojis
- Don't use em dashes (use commas, colons, periods, or sentence breaks)
- "Simple words for complex topics" is the north star
- If a sentence sounds like it came from a spec or architecture doc, rewrite it

### 4. Identify comprehension gaps (humanity pass)

Read through the rewritten pages as if you know nothing about the product or its domain.
For each page ask: "Would someone who has never heard of this product understand every sentence?"

Flag every term or concept that a first-timer would need explained:
- Technical terms (daemon, worktree, CLI, SSH, etc.)
- Product-specific terms (pane, panel, orchestrator, etc.)
- Multi-word concepts (worktree isolation, agent loop, agent-agnostic, etc.)
- Industry terms that sound obvious to insiders but aren't

Produce a list of terms that need either:
- Inline definition (a popover or parenthetical)
- A dedicated explainer page

**Success criteria**: A list of terms needing definitions, categorized by inline vs dedicated page.
**Artifacts**: This term list feeds into the content-authority-pass skill.

### 5. Verify and commit

Run the project's build command to verify nothing is broken.
Commit all changes with a descriptive message.
Push and create a PR.

**Success criteria**: Build passes. PR is open with a clear summary of what was rewritten and why.
