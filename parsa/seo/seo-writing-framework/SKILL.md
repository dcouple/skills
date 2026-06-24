---
name: seo-writing-framework
description: (foundational) Research, draft, reader-hat, edit, read-aloud process for any customer-facing deliverable.
allowed-tools:
  - Read
  - Edit
  - Write
  - Bash
  - Agent
  - WebSearch
  - WebFetch
when_to_use: >
  Use when producing any customer-facing deliverable: pricing emails, blog
  posts, landing pages, docs, support replies, announcements, PR descriptions,
  onboarding copy, or any writing where the words matter. Can be invoked
  standalone or called by other SEO skills (readability, authority, drafting)
  as their writing process. Examples: 'write this email', 'draft this
  announcement', 'help me write this', 'writing framework', 'apply the
  writing process'.
model: claude-opus-4-6
argument-hint: "[what to write] [audience]"
arguments:
  - deliverable
  - audience
---

# SEO Writing Framework

The process for producing any deliverable that a real person will read.
Works for pricing emails, blog posts, landing pages, docs, support replies,
announcements, or anything where the words matter.

**Important**: Run with Claude Opus 4.6.

## The core problem

LLMs generate things that look good. But looking good is not the same as
being good. A polished email that says the wrong things is worse than a rough
email that says the right things.

The output will be grammatically correct, professionally structured, and
completely miss the point. You can't catch this unless you know what the
reader needs to hear.

## Inputs

- `$deliverable`: What you're writing (pricing email, blog post, landing page, etc.)
- `$audience`: Who's reading it (customers, developers, first-time visitors, etc.)

## Steps

### 1. Research real examples

Before writing anything, find 3-5 real examples of how good companies
or people have written the same type of thing.

- Pricing email? Look at pricing update emails from SaaS companies you
  respect. How do they structure the message? How much do they reveal?
  How do they frame the change?
- Blog post? Read the top-ranking posts for the target topic. What works?
  What's missing? What would you want to read?
- Support reply? Look at previous replies to the same type of request.
  What actually resolved it?
- Landing page? Look at competitors and best-in-class pages in the category.
  What do they say first? What do they leave out?

Use WebSearch to find examples. Use the codebase to find previous versions
if they exist. If the user has a voice guide in `AGENTS.md` or `VOICE.md`,
read it.

**Never draft from nothing.** LLM output without research input is generic
at best, wrong at worst.

**Success criteria**: 3-5 real examples collected. Voice guide loaded if it exists.

### 2. Draft with examples as reference

Give the examples to the LLM as context alongside:
- The voice guide (how the brand sounds)
- The specific context (what's actually happening, what changed, what's new)
- Who's reading this and what they need to walk away understanding
- What the reader should do next (clear call to action)

The draft will look good. That's the trap.

**Success criteria**: First draft exists. Do not ship it.

### 3. Switch hats to the reader

Read the draft as the person receiving it. Not as the person who wrote it.

Ask:
- Does the reader understand the main point in the first 2 sentences?
- If it's a change (pricing, feature, policy): do they know what changed,
  why, and what to do about it?
- If it's educational (blog, docs, explainer): does every sentence make
  sense to someone who's never seen this product?
- Is anything confusing, vague, or leaving the reader with questions?
- Would the reader feel respected? Or talked down to? Or marketed at?

If you can't answer these, the draft needs work.

**Success criteria**: You can articulate what the reader walks away understanding.
**Human checkpoint**: If the deliverable is high-stakes (pricing, legal, public announcement), present the draft and your reader-hat analysis to the user before proceeding.

### 4. Edit with your own voice

The LLM draft will have:
- Phrases nobody would say out loud ("it's worth noting that", "in this regard")
- Hedging that weakens the point ("it might be worth considering")
- Filler sentences that don't add information
- Generic enthusiasm ("exciting", "thrilled", "game-changing")
- Em dashes used as a crutch for weak sentence structure
- Overly formal tone where casual is appropriate

Edit these out. Replace with how the founder or brand actually sounds.

**Read it out loud.** Not in your head. Out loud. 90% of awkward phrasing
is caught by hearing it. If a sentence sounds weird when spoken, rewrite it.

**Success criteria**: No LLM-isms remain. Sounds like a person wrote it.

### 5. Final check

One more pass as the reader:
- Does it say what it needs to say? (not more, not less)
- Does it sound like a person wrote it? (not a committee, not an AI)
- Does it respect the reader's time? (short sentences, no filler)
- Does the reader know what to do next? (clear next step)

If all four pass, the deliverable is ready.

**Success criteria**: Deliverable passes all four checks.

## Rules

1. **Never draft from nothing.** Research first. Examples first. Context first.
2. **Never ship a first draft.** Even if it looks good. Especially if it looks good.
3. **Read it out loud.** If it sounds weird when spoken, rewrite it.
4. **The LLM is a research tool and a drafting tool.** It is not the writer.
5. **Looking good is not being good.** Polish doesn't fix wrong messaging.
6. **No em dashes.** Commas, colons, periods, or sentence breaks.
7. **No generic enthusiasm.** "Exciting" and "thrilled" say nothing.
8. **Short sentences.** If it has a comma and a semicolon, split it.
9. **Name the pain.** Describe the problem the thing solves, not the thing itself.

## Common LLM failures to watch for

| Failure | What it looks like | Fix |
|---------|-------------------|-----|
| Filler phrases | "It's worth noting that" | Delete. Just say the thing. |
| Hedging | "It might be worth considering" | Either say it or don't. |
| Generic enthusiasm | "We're thrilled to announce" | Say what changed and why it matters. |
| Feature listing | "Includes X, Y, and Z" | Say what problem X, Y, Z solve. |
| Passive voice | "The update was deployed" | "We deployed the update." |
| Vague benefits | "Improved performance" | "Pages load 2x faster." |
| Audience mismatch | Using jargon for non-technical readers | Use the words the reader would use. |
