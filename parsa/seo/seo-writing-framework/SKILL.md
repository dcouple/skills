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

### 5. Score and revise loop

Score the deliverable against the rubric (see below). If it scores below
90%, identify the weakest criteria, revise targeting those, and re-score.
Repeat until 90%+.

This is the step that makes the framework a loop, not a one-shot process.
Most first revisions land around 70-80%. Two to three revision passes
usually get to 90%+.

**Success criteria**: Deliverable scores 90%+ on the rubric.

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

## Scoring rubric

After writing (and after each revision), score the deliverable against this
rubric. Each criterion is 0-10. The writing isn't ready to ship until it
scores 90% or higher overall.

Different deliverables weight criteria differently. A pricing email weighs
"reader perspective" and "every word essential" heavily. A blog post weighs
"hook" and "lens" heavily. A docs page weighs "clarity" and "reader
perspective" heavily. Use judgment on which criteria matter most, but score
all of them.

| # | Criterion | What 10/10 looks like | What 0/10 looks like |
|---|-----------|----------------------|---------------------|
| 1 | **Sounds human** | Reads like someone talking inside your head | Reads like a committee wrote it |
| 2 | **Reader perspective** | Reader walks away knowing exactly what to do | Reader finishes confused or without the right picture |
| 3 | **Hook** | First sentence grabs, makes you want the next | Opens with throat-clearing or generic context |
| 4 | **Every word essential** | 30%+ cut from first draft, nothing left to remove | Filler sentences, hedging, redundant points |
| 5 | **Sentence rhythm** | Varies: short punchy lines mixed with longer descriptive ones | Monotonous length throughout |
| 6 | **Conflict/context flow** | "Therefore... but then..." creates forward momentum | "And then... and then..." piles on without direction |
| 7 | **Authentic voice** | Sounds like the person who built it, not marketing | Generic corporate or AI-generated tone |
| 8 | **No LLM-isms** | Zero filler phrases, zero hedging, zero generic enthusiasm | "It's worth noting," "we're thrilled," "in this regard" |
| 9 | **Clarity** | A first-timer understands every sentence | Jargon without context, assumed knowledge |
| 10 | **The ending** | Lands memorably, reader knows what's next | Trails off with a restated summary |

### How to use the rubric

After each draft or revision:

1. Score each criterion 0-10
2. Calculate the percentage: total / 100
3. If below 90%, identify the lowest-scoring criteria
4. Revise targeting those specific weaknesses
5. Re-score after revision
6. Repeat until 90%+

```
Example scoring:
  Sounds human:        8/10
  Reader perspective:  7/10  ← needs work
  Hook:                9/10
  Every word essential: 6/10  ← needs work
  Sentence rhythm:     8/10
  Conflict/context:    7/10
  Authentic voice:     8/10
  No LLM-isms:         9/10
  Clarity:             8/10
  The ending:          7/10
  ---
  Total: 77/100 = 77% → not ready, revise

  Focus: cut more words (criterion 4), sharpen reader
  perspective (criterion 2), strengthen ending (criterion 10)
```

### Deliverable-specific weights

Not all criteria matter equally for every deliverable. Here's a rough guide
for which to prioritize:

| Deliverable | Top priorities |
|-------------|---------------|
| Pricing/change email | Reader perspective, every word essential, clarity, sounds human |
| Blog post | Hook, lens, conflict/context, the ending, sentence rhythm |
| Landing page | Hook, clarity, reader perspective, authentic voice |
| Docs page | Clarity, reader perspective, every word essential |
| Support reply | Reader perspective, sounds human, clarity |
| Announcement | Hook, reader perspective, every word essential, the ending |
| Comparison page | Clarity, authentic voice, reader perspective |

Prioritize doesn't mean ignore the others. It means if you're at 85% and
need to get to 90%, focus revision effort on the criteria that matter most
for this type of deliverable.
