# Root-Cause Finding — agent output format

> Returned **in-conversation** by the Investigator (from `/discussion` or `/create-issue`) — **not a file**.
> Feeds the Bug Report's Root cause + Suggested resolution path sections.
> **Open with the one-line cause + confidence** so the Overseer can branch without
> reading the body.

---

**Root cause:** `<one line>` · **Confidence:** `<confirmed | likely | hypothesis>`
**Introduced:** `<commit / PR / timeframe — via git blame/log — or "unknown">`

## Reproduction
`<numbered steps that reliably reproduce, from a known state>`

## Observed behavior
`<what actually happens — stated as observation>`

## Root cause (detail)
`<the cause, with evidence: file:line, stack trace, or log excerpt>`

## Suggested resolution path
`<direction for the fix — high level, not code>`

## What would confirm it  *(omit only when confidence is `confirmed`)*
`<the specific evidence or experiment that would upgrade the confidence>`

---
Separate observation from diagnosis. If the cause is unconfirmed, say so and state
what evidence would confirm it — don't present a guess as a finding.
