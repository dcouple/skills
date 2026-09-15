---
name: good-writing-fundamentals
description: Edit prose for clear, concrete language while preserving voice, or flag specific writing problems without rewriting or guessing AI authorship.
---

# Good writing fundamentals

Preserve the writer's meaning and personality. Make the smallest changes that improve the reader's experience.

Adapted from [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop), MIT; see `LICENSE`. Local guidance adds workflow routing, register, and evidence-based review.

## Choose the job

- **Edit** (default): return the edited draft and a short “What changed” note when useful.
- **Detect**: name the problem, quote the line, and suggest a brief fix. Do not rewrite, score, or claim that AI wrote it.
- If there is no text to inspect, ask for it. If asked to create a substantive new deliverable, use `seo-writing-framework`; a short message with adequate context can be drafted directly.
- Infer audience and format when clear; ask only when the answer changes the edit.

## Preserve what works

- Keep accurate names, numbers, dates, examples, quotations, and commitments.
- Preserve genuine uncertainty, humor, bluntness, cadence, and useful detours.
- Leave strong sentences alone. Do not force identical paragraph shapes or a percentage reduction.
- Keep headings, blank lines, and bullets when they help a human skim.
- Do not invent facts, experience, feelings, testimonials, or benefits.

## Make the language clearer

- Prefer direct verbs: “made a decision” → “decided”; “has the ability to” → “can.”
- Use active voice when it clarifies responsibility; passive voice is useful when the actor is unknown or irrelevant.
- Replace abstraction with supported detail. “Improved performance” can become a measured result only if the source provides one.
- Cut filler such as “it's worth noting” when the sentence works without it.
- Explain necessary jargon for the audience. Do not ban a word that has a precise technical meaning.
- Keep terminology consistent instead of cycling through synonyms for variety.

## Patterns to question

| Pattern | Example | Better direction |
|---|---|---|
| Empty enthusiasm | “A game-changing, seamless solution” | State what changed and who benefits. |
| Inflated importance | “Marks a pivotal moment” | Name the actual milestone. |
| Vague attribution | “Experts agree” | Cite the expert or flag missing support. |
| Faux insight | “What nobody tells you” | Make the supported point directly. |
| Decorative analysis | “Highlighting our commitment” | Explain an actual consequence, if known. |
| Repeated setup | Each section redefines the topic | Keep the definition where it is needed. |
| Dramatic contrast | “Not a tool. A revolution.” | Describe the capability; keep contrasts that genuinely clarify. |
| Empty ending | A metaphor that adds no meaning | End on a useful conclusion or next action. |

These are review prompts, not automatic bans. Keep a sentence when it serves the reader and fits the writer's voice.

## Fit the register

- **Explanatory:** answer promptly; do not hide an answer behind a curiosity gap.
- **Persuasive:** a hook can help, but deliver the promised value and disclose material limitations.
- Use punctuation, emphasis, and sentence-length variation for clarity. No arbitrary dash quota or fragment count.

## Finish

- Read the whole draft before editing; compare the result against the source afterward.
- Check `eval.md`. Fix material issues and report unresolved ambiguity without an endless style loop.
- Editing does not authorize publishing or sending.
- If Grain is connected, save requested drafts/reviews in the shared task folder; pass its ID/storage rule to delegated work. Local copies are fine. Otherwise use the requested destination silently; keep sensitive material private.
