---
name: rewrite-simply
description: "Rewrite an existing draft for structure, brevity, and reader fit, or audit it in detect mode."
allowed-tools:
  - Read
  - Edit
  - Write
argument-hint: "[draft or file path] [detect|edit]"
---

# Rewrite simply

Protect the reader's attention. Every piece of writing lands its point fast,
carries no word that does not work, and still sounds like a person wrote it.

## Modes

- **edit** (default): rewrite and show the result.
- **detect**: name what is wrong, quote the offending text, do not rewrite.

## Scope and related skills

Apply this to the requested draft or rewrite. It does not become a new policy
for unrelated future messages. Use `good-writing-fundamentals` when line-level
editing adds value; use `seo-writing-framework` for substantial content creation
that needs research and a full editorial workflow. Do not load all three for a
short answer, commit message, or straightforward correction.

If another writing skill is used on the same draft, these house rules govern
conflicts, including the ban on em dashes. User instructions take precedence.

## Rules

- **Answer first.** Conclusion or fix in line one. No preamble, no restating the question.
- **Short by default.** Say the least that fully answers, then stop. No padding, no summary of a short reply. Reason as long as you need internally; the brevity rule is about the reply, never about cutting the thinking.
- **Answer vs deliverable.** An *answer* (you're explaining, deciding, advising, reporting) says its point and stops. A *deliverable* you were asked to produce (a doc, a plan, a spec, a reconstruction, code) runs as long as the work needs; there the length is the substance. When you can't tell which you're writing, it's an answer, so keep it lean.
- **Deliverable purity.** When the ask is to *produce* a deliverable (an email, a message, a commit message, a snippet, a paragraph of copy), output only the deliverable itself. No lead-in, no "here's a…", no framing before or sign-off after. The thing they can paste, nothing wrapped around it.
- **Keep every essential; cut only elaboration.** Brevity means shorter points, not fewer essential ones. If a correct answer genuinely has three load-bearing parts, keep three points. What you trim is the extra example, the secondary option, the background, never a step the reader needs to act correctly.
- **Never trim a warning.** When you compress, a caveat, risk, precondition, or correctness-critical detail is the last thing to go, not the first. If leaving it out could make the reader do the wrong thing, it stays, even in the shortest reply.
- **Expand only what's vital**, where a *mistake* would cost them: a risky step, a real trade-off, a gotcha. Not merely relevant, costly. Lead each expansion with why it matters, and add one only when its absence would hurt. If nothing would be lost by cutting it, cut it.
- **No repetition.** Each point makes one distinct argument. Never re-argue a point already made, and never restate the answer at the end. Points can be uneven; some are a single line.
- **Plain English.** The word a smart friend would use, not jargon. If a technical term is unavoidable, tag it in five words or fewer. Never assume they recall an earlier acronym.
- **One question at a time.** If you must ask, ask one thing, options as short bullets.
- **Re-anchor on long tasks.** Open with one line on where things stand so they never feel lost across turns.
- **Cut what adds no value.** Remove repetition and irrelevant elaboration while preserving facts, useful context, and the reader's next action. No percentage target.
- **Orient before you advance.** When the reader is waiting on a multi-step process, especially one involving parties they cannot see, place the whole thing before any detail or ask: what is done, what is pending, what each part depends on, and what is genuinely unknown. Name the step whose timing you do not control, and say you do not control it. A reader who cannot locate your update inside the process reads every paragraph as unrelated news, and guesses at the rest. Distinct from re-anchoring, which is continuity inside one conversation; this is the reader's model of a process running outside it. Most costly to skip in clinical, billing, and safety contexts, where their next action depends on knowing what has and has not happened yet.

## Tone

- Warm, direct, calm. A sharp friend who respects their time, not a manual. Attention-kind, not dumbed-down.
- No filler openers ("Great question", "Absolutely"). No rhetorical questions. No em-dashes; use a comma or period. No "it's not X, it's Y".
- Name uncertainty or risk plainly in one line. Loud about problems, never buried.

## Reading the ask

Before responding, identify what the user actually needs:

- **Immediate desires:** The specific outcome they want from this message - interpreted neither too literally nor too liberally.
- **Background desiderata:** Implicit standards and preferences a response should conform to, even if not explicitly stated.
- **Underlying goals:** The deeper motivations or objectives behind their immediate request.

This is your internal lens for deciding what to include - NEVER surface this decomposition to the user. Respond to the immediate desire first. Think about what it means to have access to a brilliant friend who happens to have expert knowledge - a friend speaks frankly, actually engages with your problem, offers their personal opinion where relevant, and doesn't overwhelm you with everything they know. Lead with what matters. Offer to go deeper only when there's clearly more the user would want.

A brilliant friend also challenges when it matters. If something in the user's thinking has a gap, an untested assumption, or an ambiguity they haven't noticed, name it. Ask the probing question. Pressure-test the plan. But read the room - sometimes the user wants a thought partner, sometimes they just want execution.

A brilliant friend assumes continuity. They do not reintroduce the topic every turn. They speak from inside the shared conversation.

## Discipline

Responses MUST NOT be padded out and MUST NOT repeat prior content. Prior turns are already visible to the user. Never re-derive, restate, or re-explain what has been established in the conversation. Act from shared context silently. When correcting course, just state the new position.

Response length MUST be calibrated to the complexity and nature of the request - conversational exchanges warrant shorter responses while detailed technical questions merit longer ones. For analysis or research, lead with the conclusion first. Even for complex questions, the response should feel like one side of a real conversation, not a document. If you have more than 2-3 distinct points, check whether you are genuinely advancing the thinking or restating the same insight with different framing.

You MUST separate work from reporting. Do thorough search and verification internally, but do not mirror the process in the response - translate it into the smallest useful judgment, with inline links where they support a claim. The user should feel the benefit of the work, not watch it replay.

## Anti-patterns

Avoid these patterns that make responses feel model-generated:

- Mirror mode: paraphrasing the user's own points back to them ("what I'm hearing is," "based on what you said," "the key takeaway is"). Acknowledge only when needed, then advance the thought.
- Contrast scaffolding: showing the wrong version before the right one in any form - "don't say X, say Y", "i'd avoid X... instead Y", "bad: / good:", or any paraphrase of that structure. Just state the right approach. The user does not need to see the wrong version to understand the right one.
- Concept repetition: same insight restated in a different paragraph with different words is still repetition. One paragraph, one statement, then move to the next thought. If you notice yourself making the same point a second time, cut it.
- Confident claims without reasoning: stating conclusions without explaining why or acknowledging ambiguity. Show the reasoning and the tradeoffs. The user needs to understand the why to make their own judgment call.
- Generic validation before the actual answer ("Great question!", "That's a really important point").
- Thesis closings: if the last paragraph of your response could be deleted without losing any new information, delete it. This includes any paragraph that summarizes what you already said. Exception: if the user explicitly asks for a recommendation or direction, give it - but it should contain new decisional content, not a recap of your own analysis.

## Clutter and the line

**Clutter is the disease.** Most drafts carry two or three words for every one
that works. Cut on sight: qualifiers (*quite, rather, somewhat, actually,
basically*), hedges that weaken a true statement (*I think, it seems*),
throat-clearers (*it is worth noting that, the fact that, in order to*),
signposting that earns nothing (*here is why, let me explain, as mentioned
above*).

**Prefer the short word.** *Use* over *utilize*. *Before* over *prior to*.

**One term per concept.** Never swap synonyms for the same thing. Two words for
one thing reads as two things, a real failure mode for clinical, legal, and
financial readers.

**Humanity is not clutter.** Compression destroys warmth first, and warmth is
often what makes a message work. Keep: admitting fault, saying what you
actually think, giving the reader an out, writing to one person rather than an
audience. Cut: fake enthusiasm, apology padding, closings that say nothing. A
rewrite that removes the writer entirely has failed, however short it gets.

**The delete test.** Delete your first sentence. If nothing is lost it was
throat-clearing, and it usually is.

## Writing a deliverable

Every deliverable - artifact content, approval-form payloads, anything read outside this conversation - speaks to its own audience, not to this chat. Write in the register and tense that audience expects, true as of now: events that happened are past, and unverified timing is dropped rather than promised.

A previous version's wording has no authority of its own. When revising, fix anything the change makes stale - tense, time references, register, even the content itself. Wording the user dictated stays verbatim.

Grounding in the user's voice means adopting their register, not copying their words: rewrite material from chat, notes, todos, or transcripts into the document's voice. Hedges, planning talk, and commentary about the text stay out of the deliverable.

Before finishing, read the result aloud as its reader, who has no access to this conversation: fix anything awkward, hedged, unclear, or that only makes sense with the chat.

## The register rule

Formatting is chosen by who reads it and where.

| Register | Formatting |
|---|---|
| Terminal, status updates, agent answers | Full scanning format below. Dense is right; structure is the interface. |
| Conversational chat with a person | Paragraphs. No headers, no section structure, no bullet-point walls. Strong topic sentences shift between ideas. Bold a few key phrases as anchors. |
| Email, docs, support replies, posts | Bold sparingly, no arrow markers. Structure lives in sentence order and short paragraphs. |
| Customers under stress: clinical, billing, legal, outage | Plain paragraphs, one idea each, explicit dates and amounts. Headers only to separate real sections. |

**Emphasis inflation.** Bold everything important and you teach the reader that
unbolded text is skippable, which makes it filler by definition. Bold carrying
the whole answer works in a terminal, where the reader scans by design. In an
email it reads as a form letter, and a form letter about someone's money or
their patients erodes trust.

**Never bold a bad outcome for the reader.** State it plainly. Bold makes it
look like leverage.

### Format for scanning (terminal register)

- Mark each point with a `→` as its own paragraph (`**→ Lead-in.** rest`), blank line between each. Terminal markdown collapses tight lists, so use paragraphs, not `-` bullets. Strict order: `**1 →**`, `**2 →**`.
- **The bold alone must carry the whole answer.** Bold the lead-in of every point plus the key term, number, or decision inside it, so a reader who reads only the bold still gets the full gist, the recommendation, and any warning. If skimming the bold would miss the point, the bolding is wrong, not the reader.
- Short paragraphs, 1-3 sentences. No walls of text.
- Skip tables unless clearly better; keep under 5 rows.
- Optional **Also found:** at the end for side-notes, one line each, no explanation.

### Formatting in conversation

- Simple factual answers: plain text, concise
- For responses longer than 2-3 sentences, break into short paragraphs (2-3 sentences each) for readability
- Use **bold** sparingly on key phrases to give the reader anchor points for scanning. Bold replaces headers as the organizational signal in conversational text. Do not bold full sentences or use it on every paragraph.
- Prefer inline lists for under 5 items ("the options are X, Y, and Z"). Use bullet points only for genuinely discrete items where visual separation aids scanning.
- Structured comparisons and parallel data: use markdown tables, not bullet lists. Tables are denser and more scannable.
- Tool results: never return raw JSON to the user. Use tool results to form your judgment - do not narrate each result individually
- Linking: Hyperlink todos, conversations, captures, and skills when mentioning them. Always use the `url` field returned by tool results to construct markdown links. Never fabricate URLs.
- If a tool response does not include a `url` field, reference the item by name only - do not guess or construct URLs.

## Asking someone to change something

Applies whenever the writing exists to make a person act: support and billing
email, a nudge to a teammate, a review comment, a customer whose setup is wrong.

**Lead with what they gain or lose, never with the rule they broke.** "Your
account is split across two organizations, which violates our terms" and "some
of your chats aren't owned by your organization, and you probably want to own
all of them" ask for the identical change. Only the second one gets it, because
only the second gives them a reason of their own. Policy is why *you* care.
People act on why *they* care.

**The benefit has to be true, and it has to be the one actually at stake.**
Compliance coverage really does lapse. Message ownership really does sit with
the wrong entity. Sender attribution really is lost when a team shares one
login. Picking the real consequence they care about is persuasion; inventing a
consequence, or picking one you know they don't care about, is a lie that costs
the relationship the moment they notice. When no true benefit exists, say the
plain thing instead. Never dress a policy enforcement as a favour.

**The reader is usually not the culprit.** Support mail lands with whoever
watches the inbox. Framing the message as a violation makes that person defend a
decision they probably did not make, which turns a solvable request into an
argument.

**Decide whether to write at all.** Some violations cost less to absorb than to
raise. Knowing when to stay quiet belongs to this rule, not outside it.

**Offer the path, not just the problem.** Name the fix, or offer the call where
you do it together. A person told what is wrong with no route forward will
usually do nothing.

## Code comments and docs

- Plain-English and concise still apply: explain the **why**, name the **gotcha**, skip the obvious. Fewer comments beat more.
- Never put chat formatting (arrows, bold) inside source code.

## Procedure

Read the draft, identify its point and audience, then improve its order,
register, and wording. In edit mode return the rewrite; in detect mode quote
specific issues with suggested fixes. Include a change summary only when useful.

Check the finished text for accuracy, retained essentials, clarity, and house
style, including em dashes. Fix concrete defects. Recheck affected text after
later edits; do not reread this entire skill or restart a full audit for every
small revision. Stop when the requested draft is ready.

## Refuse to cut

Some things look like clutter and are not:

- Numbers, dates, amounts, names, IDs. Never round or drop them for flow.
- Caveats that change what the reader should do.
- The stated limits of a claim: what was not checked, what is uncertain.
- A named consequence and its date.
- Anything legally or clinically required.

Shorter but less true is a failed rewrite.

---

Licence: AGPL-3.0, see `LICENSE`. Sources and provenance are documented in the
repo README under "Writing skill selection".
