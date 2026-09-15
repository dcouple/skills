---
name: rewrite-simply
description: Rewrite or audit human-facing prose for clarity, brevity, and a natural voice without losing meaning or useful detail.
argument-hint: "[draft or file path] [detect|edit]"
---

# Rewrite simply

Make the point easy to find and the rest easy to skim. Shorter but less true is a failed rewrite.

## Modes

- **Edit** (default): return the rewritten text, or update the requested file.
- **Detect**: quote specific problems and explain their effect; do not rewrite.
- Work on the requested prose, not code, identifiers, logs, or machine-parsed output.

## Structure first

- Lead with the answer, decision, or reader's next action.
- Group related ideas under useful headings. Use short bullets for rules, steps, or options.
- Leave natural blank lines. Avoid compressing a readable list into a dense paragraph.
- Keep examples, distinct questions, and caveats that help someone understand or act.
- Match the format to the destination: a short chat reply may need no heading; a reusable skill usually does.

## Edit the language

- Prefer concrete verbs and familiar words. Name the actor when responsibility matters.
- Remove repeated points, throat-clearing, inflated claims, and commentary about how good the answer is.
- Keep a human voice without inventing feelings, experience, or certainty.
- Use emphasis sparingly. Punctuation and sentence length should serve readability, not a blanket style ban.
- Explain jargon the reader needs; remove jargon they do not.

Examples:

- “In order to facilitate deployment” → “To deploy.”
- “It is important to note that the token expires” → “The token expires.”
- “This is much better” → name the actual benefit, supported by the source.
- Keep a three-item checklist as three bullets when each item is independently actionable.

## Preserve meaning

- Keep names, dates, numbers, IDs, attribution, and explicit commitments accurate.
- Preserve uncertainty, limitations, safety warnings, and legally or clinically required detail.
- Do not add evidence, benefits, motives, or promises the original does not support.
- If shortening creates ambiguity, keep the extra words. There is no required percentage reduction.

## Finish

- Read the result as the intended reader: is the answer clear, complete, and easy to scan?
- Check it against the source for dropped requirements and changed meaning.
- For a deeper line edit, use `good-writing-fundamentals` if available and relevant.
- Return the result with only material changes or unresolved questions worth explaining. Rewriting does not authorize sending or publishing it.

## Saved artifacts

When Grain is connected, save requested drafts and reviews in the shared task folder; pass its ID and this rule to any delegated writer. Local working copies are fine. Otherwise use the requested destination without commentary. Do not upload secrets or publish externally without authorization.

---

Adapted from the sources credited under “rewrite-simply” in the repository README. Licence: AGPL-3.0; see `LICENSE`.
