---
name: rewrite-simply
description: (foundational) Restructure any draft or agent output so the answer comes first, length signals importance, and nothing is said twice. The structural layer above line-level editing.
allowed-tools:
  - Read
  - Edit
  - Write
when_to_use: >
  Use on anything a person has to read and decide from: emails, Slack and
  support replies, PR descriptions, release notes, docs, briefs, status
  updates, or your own answer before you send it. Also use when a draft is
  accurate but buries its point, when someone says a message is too long or
  hard to follow, or when you want your terminal output tightened.
  Examples: 'rewrite this simply', 'this is too long', 'get to the point',
  'make this scannable', 'tighten this before I send it', 'answer first'.
  Not for code, identifiers, logs, or config.
argument-hint: "[draft or file path] [detect|edit]"
---

# Rewrite simply

You are cutting a draft down to the thing it is actually trying to say.

Two sources, merged. **Zinsser** (*On Writing Well*) governs the line: clutter,
plain words, warmth. **Attention-kind** (from
[alexgreensh/attention-span](https://github.com/alexgreensh/attention-span))
governs the shape: answer first, length as signal, no restatement. Both are
restated here in our own words — no rule text is copied.

## Modes

- **edit** (default) — rewrite and show the result.
- **detect** — name what is wrong, quote the offending text, do not rewrite.

## Where this sits

Structure, not lines. It decides what comes first, what gets cut, and what
earns space.

`good-writing-fundamentals` is the line-level layer — active voice, concrete
detail, direct verbs, AI patterns. **Run this one first, then that one.**
Restructuring after a line polish wastes the polish.

If there is no draft yet and it is customer-facing, run
`seo-writing-framework` instead. This skill needs text that exists.

## The rules

### 1. Answer first

The conclusion goes in the first line. No wind-up, no restating the question,
no describing what you are about to do.

The test: delete your first sentence. If nothing is lost, it was throat-clearing
— and it usually is. Sentences beginning *I was reviewing…*, *I wanted to reach
out…*, *Great question…*, *So basically…* are almost always deletable.

Zinsser's version: the most important sentence in the piece is the first one.
Its only job is to make the reader want the second one.

### 2. Length is a signal, not an accident

Say the least that fully answers, then stop. Expand only where it genuinely
matters, so that length itself tells the reader what is important.

This is stricter than "be brief." A uniformly short piece where everything gets
equal space has thrown away a channel of meaning. If one section is three times
longer, the reader should be able to tell why.

### 3. Say it once

Each point makes one distinct argument and never reappears. Summaries that
restate the body, closings that recap the opening, and the same fact in a
header and again in a sentence are all repetition.

Exception: a genuine action or deadline may appear twice — once where it is
explained, once where the reader acts.

### 4. Cut the clutter

Zinsser's core claim: most drafts carry two to three words for every one that
works.

Cut on sight:
- Qualifiers: *quite, rather, somewhat, a bit, fairly, actually, basically*
- Hedges that weaken a true statement: *I think, it seems, which I expect would be*
- Throat-clearers: *it is worth noting that, the fact that, in order to, at this time*
- Signposting that earns nothing: *here is why, let me explain, as mentioned above*
- Adjectives and adverbs the noun or verb already implies

Prefer the short word. *Use* over *utilize*, *before* over *prior to*, *now*
over *at this juncture*.

### 5. Plain English, defined once

Write so a smart reader outside your field follows it. Where a technical term
is genuinely required, define it in about five words, the first time, and never
again.

Never swap synonyms for the same concept. Pick one term and hold it. Two words
for one thing reads as two things — a real failure mode for clinical, legal, and
financial readers.

### 6. One question at a time

If you need something from the reader, ask for one thing. On long or multi-part
work, re-anchor: say where you are before continuing.

### 7. Keep the human in it

Warmth is not clutter. Zinsser's fourth principle is humanity, and it is the one
compression tends to destroy first.

Keep: admitting fault, saying what you actually think, giving the reader an out,
writing to one person rather than an audience.

Cut: fake enthusiasm, apology padding, and closings that say nothing.

Compression that removes the writer entirely has failed, however short it gets.

## The register rule

Sources 1–3 push toward heavy formatting. Zinsser pushes toward flowing prose.
Which wins is decided by **who reads it and where**.

| Register | Formatting | Why |
|---|---|---|
| Terminal / chat output, status updates, agent answers | Bold, arrows, tables, whitespace — dense is fine | Scanned, not read. Structure is the interface. |
| Email, support replies, docs, posts, anything to a customer | Bold sparingly; carry structure in sentence order and short paragraphs | Read as prose by a person deciding something. |
| Anything to a customer under stress — clinical, billing, legal, outage | Plain paragraphs, one idea each, explicit dates and amounts, headers only to separate real sections | Heavy markup reads as a form letter, and a form letter about their money or their patients erodes trust. |

Two cautions on bold, in every register:

**Emphasis inflation.** Bold everything important and you teach the reader that
unbolded text is skippable — which makes it filler by definition. If bold is the
only thing making your point findable, the sentence order is wrong. Fix the
order.

**Never bold a threat or a bad outcome for the reader.** Say it plainly. Bold
makes it look like leverage.

## Procedure

1. **Read the whole draft.** Do not edit while reading.
2. **Find the real answer.** One sentence: what does this actually say? If you
   cannot, the draft has no point yet — say so and stop.
3. **Move it to line one.** Everything else reorders around it.
4. **Set the register** from the table. This decides your formatting budget.
5. **Cut** — throat-clearing, repetition, clutter, hedges.
6. **Check length is doing work.** Does the longest section deserve to be?
7. **Check the human survived.** Would you send this to someone you respect?
8. **Report the cut** — before/after word count, and what you removed.

Then hand off to `good-writing-fundamentals` for the line pass.

## Refuse to cut

Some things look like clutter and are not. Keep them:

- Numbers, dates, amounts, names, IDs — never round or drop them for flow
- Caveats that change what the reader should do
- The stated limits of a claim (what was *not* checked, what is uncertain)
- A named consequence and its date
- Anything legally or clinically required

If cutting would make the piece shorter but less true, stop cutting.

## Self-check

This skill is subject to its own rules. If your output about concise writing is
bloated, you have failed the demonstration.
