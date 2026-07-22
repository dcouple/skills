# Writing Framework

How to write anything that a customer, user, or reader will actually read.
This applies to pricing emails, blog posts, landing pages, docs, support
replies, and any other writing where the words matter.

All SEO copy skills (`seo-readability-pass`, `seo-authority-pass`,
`seo-content-drafting`) must follow this framework.

## The problem with LLMs and writing

LLMs generate things that look good. But when you read them, they often
don't land right. The sentences are grammatically correct but don't say the
right things. The structure looks professional but leaves the reader confused
or without the right picture.

The scary part: in order to catch this, you have to have your own perspective
on what good communication means. You can't outsource that to the LLM.

## The framework

### 1. Research real examples first

Before writing anything, find real examples of how good companies communicate
the same type of thing.

- Pricing change email? Find 3-5 pricing emails from SaaS companies you respect.
  Look at how they structure the message, how much information they reveal, how
  they frame the change.
- Blog post? Find the top-ranking posts for the target keyword. Read them as a
  reader, not a writer. What works? What's missing?
- Support reply? Look at previous replies to the same type of ticket. What
  actually resolved the issue?

Never let the LLM draft from nothing. LLM output without research input is
generic at best, wrong at worst.

### 2. Draft with examples as reference

Give the LLM the real examples and ask it to draft based on them. The examples
are the source of truth for tone, structure, and what information to include.

Also give it:
- The voice guide (how your brand sounds)
- The specific context (what's actually changing, who's reading this)
- What the reader needs to walk away understanding

The draft will look good. That's the trap. Looking good is not the same as
being good.

### 3. Switch hats to the reader

This is the step most people skip. Read the draft as if you're the person
receiving it. Not as the person who wrote it.

- If it's a pricing email: read it as the customer who's about to pay more.
  Do they understand why? Do they know what to do? Are they going to be
  angry about something that could have been said better?
- If it's a blog post: read it as someone who googled this topic. Do they
  get the answer in the first paragraph? Or do they have to wade through
  filler?
- If it's docs: read it as someone who's never seen this product. Does every
  sentence make sense? Would a first-timer understand it?

If you can't put yourself in the reader's shoes, the writing won't work.
No amount of LLM iteration fixes this. It requires human judgment about
what the reader needs to hear.

### 4. Edit with your own voice

The LLM draft will have phrases that don't make sense. Not grammatically
wrong, just... off. Phrases that no human would write. Words that sound
impressive but say nothing. Sentences that fill space without adding meaning.

Edit these out. Replace them with how you'd actually say it.

Read it out loud. Not in your head. Out loud. 90% of the time, reading
out loud catches where it's awkward or feels wrong. If a sentence sounds
weird when you say it, rewrite it.

### 5. Run the slop gate

Run `good-writing-fundamentals` in detect mode. It names each AI pattern it finds with the
quoted line, so you can check the call yourself instead of trusting a verdict.
Fix what it names, re-run, repeat until it comes back clean.

This is the step that catches the patterns your own ear misses, because they're
grammatical and confident: colon reveals, binary contrasts, "highlighting the
team's commitment," "experts agree." Nothing proceeds to the final check with
findings outstanding.

### 6. Final check: does it land?

One more pass as the reader. Does the writing:
- Say what it needs to say? (not more, not less)
- Sound like a person wrote it? (not a committee, not an AI)
- Respect the reader's time? (short sentences, no filler)
- Leave the reader knowing what to do next? (clear next step)

If yes, ship it. If any of these fail, go back to step 4.

### Which craft rules apply: pick the register

Some moves work on a landing page and read as slop in a support reply. Before
drafting, decide whether the piece is **persuasive** (landing pages, launch
emails, marketing copy) or **explanatory** (docs, support replies, changelogs,
pricing emails, technical posts). Curiosity gaps and a deliberate ending belong
to the first. The second ends on the last concrete point or the next action.
Banned words and the hard-banned patterns apply to both. See
`seo-writing-framework` for the full rules.

## How this maps to the skill workflow

```
Research (step 1)    →  seo-data-pull, WebSearch, competitor analysis
Draft (step 2)       →  LLM writes with voice guide + examples as context
Reader hat (step 3)  →  the humanity pass from seo-readability-pass
Edit (step 4)        →  human edits, or LLM rewrites with specific corrections
Slop gate (step 5)   →  good-writing-fundamentals detect, fix, re-run until clean
Final check (step 6) →  read out loud, ship or iterate
```

## Rules for LLM-assisted writing

1. **Never draft from nothing.** Research first. Examples first. Context first.
2. **Never ship a first draft.** Even if it looks good. Especially if it looks good.
3. **Read it out loud.** If it sounds weird when spoken, rewrite it.
4. **The LLM is a research tool and a drafting tool.** It is not the writer. You are.
5. **Looking good is not being good.** A polished email that says the wrong things is worse than a rough email that says the right things.

## Common LLM writing failures to watch for

- Phrases nobody would say out loud ("it's worth noting that", "in this regard")
- Hedging that weakens the point ("it might be worth considering")
- Filler sentences that don't add information
- Overly formal tone where casual is appropriate (and vice versa)
- Listing benefits without naming the pain they solve
- Generic enthusiasm ("exciting", "thrilled", "game-changing")
- Em dashes used as a crutch for weak sentence structure
- Confident patterns your ear skips because they're grammatical: binary
  contrasts ("it's not X, it's Y"), colon reveals, "highlighting the team's
  commitment," "experts agree." The full inventory is in `good-writing-fundamentals`.
