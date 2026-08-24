---
name: eli5
description: Explain one topic to a smart person who knows nothing about it, as a single HTML page that leads with a picture and earns every word, rendered per the html-explainer standards. Use when the user types /eli5 <topic>, asks for a dead-simple explainer of how something works, or wants to start learning about the code they are sitting in without a lecture.
argument-hint: "<topic, question, or path to explain>"
model: claude-opus-4-6
allowed-tools: Read, Grep, Glob, Bash, Write
---

# ELI5

## Task: $ARGUMENTS

The reader is not five. The reader is sharp, busy, and new to exactly
this. Respect both halves: no jargon they have not been given, and no
padding they have to wade through. One page, one topic, picture first.

## The writer

The page is written by Opus 4.6; it writes better. The frontmatter pins
it for direct invocation. When an orchestrator or a session on another
model runs this skill, it hands the writing to an Opus 4.6 session
(`claude -p --model claude-opus-4-6` with this skill and the grounding
facts) rather than writing the page itself; the grounding below can be
done by whoever is cheapest, the prose and drawings cannot.

## Ground it

Before writing a word, find the truth of the topic in what is actually
here. A topic inside this repo means reading the real code and tracing
the real flow; a general topic means working from what you know and
saying so. Collect the three to five facts the whole explanation hangs
on. If the honest answer to "how does this work" is "it does not", the
page says that; an explainer that flatters a broken thing teaches the
wrong lesson.

## The three floors

The page renders per the html-explainer skill (tokens, components,
diagram rules, quality bar), structured as three floors the reader
descends by choice:

1. **The picture.** Masthead, then the opening diagram, then at most a
   hundred words: the one metaphor or plain-language mechanism that
   makes the topic click. A reader who stops here leaves with the right
   intuition and no vocabulary.
2. **The mechanism.** How it actually works, still in plain words, with
   one or two more diagrams or panel pairs (before/after, request/
   response, cause/effect). Each new term is introduced at the moment
   it pays for itself. A reader who stops here could explain it to
   someone else.
3. **The real names.** Inside `details` blocks: the proper terminology
   mapped to the plain words used above, the file:line anchors when the
   topic is code, the two or three things people commonly get wrong,
   and where to go deeper. A reader who opens these is ready for the
   real documentation.

## Metaphors

One metaphor, carried all the way through, beats three abandoned ones.
Pick it for mechanical honesty (the parts must correspond) rather than
charm, and drop it the moment it would mislead; some topics are best
explained literally, and a plain diagram of the actual parts is always
an acceptable metaphor. For an abstract topic with no visual shape,
diagram the relationship (what talks to what, what depends on what)
rather than forcing an object.

## Words

- Floor 1 under a hundred words; the whole page under six hundred.
  The budget counts every word the reader sees with `details` closed,
  captions, masthead, and SVG labels included; markup and style count
  nothing.
- Short declarative sentences. No "simply", no "just", no "magic".
- Numbers over adjectives: "answers in about 7 seconds" beats "fast".
- Every sentence survives the question "does the reader need this to
  understand the next one?"

## Boundaries

- Accuracy outranks simplicity: simplify by omission, never by
  distortion, and name the biggest thing you left out in floor 3.
- The page is the deliverable; the chat reply is one line saying where
  it is and what it covers.
- No em dashes.
