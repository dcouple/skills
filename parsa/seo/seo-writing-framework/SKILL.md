---
name: seo-writing-framework
description: (foundational) Research, draft, reader-hat, edit, slop-gate, score process for any customer-facing deliverable.
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
argument-hint: "[what to write] [audience] [register]"
arguments:
  - deliverable
  - audience
  - register
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
- `$register`: `persuasive` or `explanatory` (see below). If not given, infer it and say which one you picked.

## Register

Some craft moves work on a landing page and read as slop in a support reply.
Pick the register before drafting, because it decides which ones are allowed.

**Persuasive**: landing pages, launch emails, marketing copy, headlines,
comparison pages. The reader hasn't decided to care yet. Curiosity gaps and a
deliberate ending are allowed, within the limits in `no-ai-slop`.

**Explanatory**: docs, support replies, changelogs, pricing and policy emails,
technical posts, announcements of changes. The reader already has a question.
No curiosity gaps, no kicker. End on the last concrete point or the next action.

The banned words and hard-banned patterns apply in both.

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
- The register (persuasive or explanatory), which decides the craft rules
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

The full pattern list lives in `no-ai-slop` (words to cut, patterns to cut).
That skill is the canonical inventory. The table further down this file is the
short version for drafting; don't maintain a second copy of the long one.

**Success criteria**: No LLM-isms remain. Sounds like a person wrote it.

### 5. Run the slop gate

Run `no-ai-slop` on the draft in detect mode with the register you picked.
It returns named patterns with quoted lines, not a score.

Fix everything it names, then re-run until it comes back clean. This is a
pass/fail gate, not a judgment call: a draft that still trips patterns does not
proceed to scoring.

Two things the gate is not allowed to do:
- Cut character to hit a word-count target. Cutting is proportional to the
  actual slop.
- Rewrite a weak ending into a better metaphor. Weak endings get deleted, and
  the piece ends on the clearest concrete sentence already in it.

**Success criteria**: `no-ai-slop` detect returns no findings.

### 6. Score and revise loop

Score the deliverable against the rubric (see below). If it scores below
90%, identify the weakest criteria, revise targeting those, and re-score.
Repeat until 90%+.

This is the step that makes the framework a loop, not a one-shot process.
Most first revisions land around 70-80%. Two to three revision passes
usually get to 90%+.

**Success criteria**: Deliverable scores 90%+ on the rubric.

## Craft principles

These go beyond "don't use LLM-isms." They're what separates writing that
works from writing that's just correct.

### Write the way you talk

The test: read it back. Does it sound like someone talking inside your head?
Not a press release. Not a committee. A person. If it reads like corporate
communications, rewrite it in the voice you'd use explaining it to a friend.

### Vary sentence length

Don't just write short sentences. Monotonous length in either direction is
bad. Some sentences should be longer and descriptive, painting a picture, and
others should be much shorter. The variation creates rhythm. Without it, the
reader's brain turns off.

The limit: never stack three or more fragments in a row. Two consecutive
one-word sentences read as emphasis. Four read as AI drama.

### Cut what doesn't earn its place

After your draft is done, remove every word that isn't doing work. No
redundancy, no waste. If a sentence doesn't add information or advance the
point, delete it.

A bloated first draft usually loses about 30%, which is where the old "cut 30%"
rule came from. Treat that as a typical yield, not a quota. A draft that's
already tight loses almost nothing, and cutting to hit a number is how voice
gets stripped out.

### Headlines do 80% of the work

Formula: action verb + specific outcome + timeframe or contrast.
"Ship your startup in days, not weeks." Write at least five headlines
before picking one. One will outpull the others by 2-10x.

### Opening lines have one job

Get them to read the second sentence. Lead with a direct challenge,
a scene-setting story, a specific result, or a confession. Never open
with "In today's fast-paced world." Never open with "Let's dive in."

### The So What Chain

Go three levels deep until you hit something emotional or financial.
"Fast database" > "queries load fast" > "users don't bounce" >
"you stop waking up stressed about churn." Write from the bottom.

Most copy dies at level one. The feature, not the outcome. Always ask
"so what?" until you can't anymore.

### Pain quantification

Vague problems feel unsolvable. Specific ones feel fixable. Do the math.
"4 hrs for emails + 6 hrs for landing page = 22+ hours of headaches"
beats "launching is hard."

### Open loops (persuasive only)

Tease without revealing. "But that's not even the best part." Open loops keep
readers moving because the brain wants to close them.

Rules: persuasive copy only, two per page maximum, and every one gets closed on
the same page. An open loop you don't close is a bait line. Never phrase one as
a faux-insight setup ("here's what nobody tells you") — that's slop in any
register.

In explanatory copy, zero. The reader already has a question; withholding the
answer is just friction.

### Conflict and context

All great writing alternates between opening a question (conflict) and
answering it (context). The pattern is: "this happens, therefore this
happens, but then this happens." Not: "and then... and then... and then..."
which just piles on detail and loses attention.

### Your lens

What's your unique perspective on this topic? The less common it is, the
more the reader engages. "Here's how to do SEO" is boring. "Every agent
manager is macOS only, we fixed that" is a lens.

### The last dab

Don't trail off with a summary paragraph that restates what they just read. The
reader was just there.

In persuasive copy, end with something the reader remembers, and keep it
concrete: a callback to a specific thing you named earlier, a real result, a
clear action. Not a metaphor, not an aphorism, not a mic drop. If the ending you
wrote is "deep," delete it rather than polishing it, and end on the clearest
concrete sentence already in the draft.

In explanatory copy, end on the last concrete point or the next action. No
kicker at all.

### Testimonials (when using them)

Structure: before state + action + specific outcome + timeframe + emotion.
"I wanna cry" beats "Great product!" A good testimonial has the
transformation visible in one sentence.

## Rules

1. **Never draft from nothing.** Research first. Examples first. Context first.
2. **Never ship a first draft.** Even if it looks good. Especially if it looks good.
3. **Read it out loud.** If it sounds weird when spoken, rewrite it.
4. **The LLM is a research tool and a drafting tool.** It is not the writer.
5. **Looking good is not being good.** Polish doesn't fix wrong messaging.
6. **Em dashes are rationed.** None in short copy. One or two in a long draft, and only when they clearly beat a comma, colon, period, or parentheses. Never as a rhythm crutch.
7. **No generic enthusiasm.** "Exciting" and "thrilled" say nothing.
8. **Banned words.** The full list is in `no-ai-slop`. If it sounds like a textbook, rewrite it.
9. **Vary sentence length.** Short is good. Monotonous is bad. Same-length paragraphs scream AI. Three or more fragments in a row is its own kind of slop.
10. **Name the pain.** Describe the problem the thing solves, not the thing itself.
11. **Cut what doesn't earn its place.** Usually about 30% of a first draft. That's a typical yield, not a quota, and never a reason to cut character.
12. **Be authentic.** "You are getting it from the engineer who built it, not the marketing person." A little tongue in cheek is good.
13. **Write 5 headlines, pick 1.** One will outpull the others by 2-10x. Never go with the first one.
14. **Go three levels deep.** Feature > outcome > emotional/financial impact. Write from the bottom.
15. **Pick the register first.** Persuasive and explanatory copy get different craft rules.
16. **Pass the slop gate before scoring.** `no-ai-slop` detect has to come back clean.

## Common LLM failures to watch for

| Failure | What it looks like | Fix |
|---------|-------------------|-----|
| Filler phrases | "It's worth noting that" | Delete. Just say the thing. |
| Hedging | "It might be worth considering" | Either say it or don't. |
| Generic enthusiasm | "We're thrilled to announce" | Say what changed and why it matters. |
| Feature listing | "Includes X, Y, and Z" | Run the So What Chain. What problem do they solve? |
| Passive voice | "The update was deployed" | "We deployed the update." |
| Vague benefits | "Improved performance" | Quantify: "Pages load 2x faster." |
| Level-one copy | "Fast database" | Go deeper: "you stop waking up stressed about churn." |
| Textbook opening | "In today's fast-paced world" | Lead with a challenge, story, result, or confession. |
| Same-length paragraphs | Every paragraph is 3 sentences | Vary the length. One short sentence, then a longer one. Rhythm is the tell. |
| Audience mismatch | Using jargon for non-technical readers | Use the words the reader would use. |
| Binary contrast | "It's not a tool. It's a system." | State the second half directly. |
| Faux-insight setup | "What nobody tells you about X" | Cut the setup, make the claim stand alone. |
| Colon reveal | "The best part: it learns." | Rewrite as a plain sentence. |
| Superficial analysis | "...highlighting the team's commitment" | Say the actual consequence for the reader. |
| Importance puffery | "marks a pivotal moment" | State the fact, let the reader judge. |
| Weasel attribution | "experts agree," "studies show" | Name the source or cut the claim. |
| Fake-strong verbs | "serves as a centralized hub for" | "Tracks sponsors, drafts, and due dates in one place." |
| Synonym cycling | agent, then assistant, then tool | Repeat the right word. |
| Fake-profound kicker | A metaphor as the last line | Delete it. End on the clearest concrete sentence. |

`no-ai-slop` holds the full inventory with before/after rewrites. This table is
the drafting-time short list.

## Scoring rubric

After writing (and after each revision), score the deliverable against this
rubric. Must hit 90%+ to ship.

Criteria are split into two tiers:
- **Universal (2x weight)**: applies to every deliverable, always matters
- **Craft (1x weight)**: matters for good writing but some are more relevant
  to certain deliverables than others

### Universal criteria (0-10 each, weighted 2x)

These are non-negotiable for any deliverable.

| # | Criterion | Weight | What 10/10 looks like | What 0/10 looks like |
|---|-----------|--------|----------------------|---------------------|
| 1 | **Research-derived** | 2x | Draft built from 3-5 real examples, not from nothing | LLM drafted from zero context |
| 2 | **Sounds human** | 2x | Reads like someone talking inside your head | Reads like a committee or AI wrote it |
| 3 | **Reader perspective** | 2x | Reader walks away knowing exactly what to do | Reader finishes confused |
| 4 | **No LLM-isms** | 2x | `no-ai-slop` detect returns zero findings | Filler, hedging, generic enthusiasm, or any named slop pattern |
| 5 | **Clarity** | 2x | A first-timer understands every sentence | Jargon without context |
| 6 | **Every word essential** | 2x | Nothing left to remove without losing meaning or voice | Filler, hedging, redundant points |

Criterion 4 is a gate, not a dial. If the step 5 slop gate is still returning
findings, the draft isn't ready to score at all. Go back to step 5.

### Craft criteria (0-10 each, weighted 1x)

These elevate writing from correct to compelling.

| # | Criterion | Weight | What 10/10 looks like | What 0/10 looks like |
|---|-----------|--------|----------------------|---------------------|
| 7 | **Hook** | 1x | First sentence grabs, makes you want the next | Opens with throat-clearing |
| 8 | **Sentence rhythm** | 1x | Short lines mixed with longer ones, no stacked fragments | Monotonous length, or three-plus fragments in a row |
| 9 | **Conflict/context flow** | 1x | "Therefore... but then..." momentum | "And then... and then..." |
| 10 | **Authentic voice** | 1x | Sounds like the person who built it | Generic corporate tone |
| 11 | **The ending** | 1x | Ends on a concrete point, result, or action the reader can take | Trails off with a summary, or lands on a metaphor |
| 12 | **Diverse options presented** | 1x | 2-3 distinct options shown before picking one | Single option, take it or leave it |

### How to score

```
Universal (6 criteria x 10 pts x 2 weight = 120 max):
  Research-derived:     9/10 x2 = 18
  Sounds human:         8/10 x2 = 16
  Reader perspective:   7/10 x2 = 14  ← needs work
  No LLM-isms:          9/10 x2 = 18
  Clarity:              8/10 x2 = 16
  Every word essential:  6/10 x2 = 12  ← needs work

Craft (6 criteria x 10 pts x 1 weight = 60 max):
  Hook:                 9/10 x1 = 9
  Sentence rhythm:      8/10 x1 = 8
  Conflict/context:     7/10 x1 = 7
  Authentic voice:      8/10 x1 = 8
  The ending:           7/10 x1 = 7
  Diverse options:      8/10 x1 = 8

Total: 141 / 180 = 78% → not ready

Focus: cut more words (criterion 6), sharpen reader
perspective (criterion 3)
```

### The revision loop

1. Score every criterion after each draft
2. If below 90%, identify the lowest-scoring criteria
3. Revise targeting those weaknesses specifically
4. Re-score
5. Repeat until 90%+

Most first revisions land 70-80%. Two to three passes get to 90%+.

### Presenting diverse options

Before finalizing any deliverable, present 2-3 distinct options. Not
variations of the same thing: genuinely different approaches, angles, or
framings. Let the user (or the calling skill) pick the strongest one,
or combine elements from multiple options.

This applies to: headlines, opening hooks, email framings, page structures,
blog angles, comparison approaches. If there's only one obvious way to write
it, you haven't explored enough.
