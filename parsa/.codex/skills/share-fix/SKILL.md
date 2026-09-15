---
name: share-fix
description: Find related upstream or downstream issues for a verified fix, draft useful outreach, and post only with explicit approval.
---

# Share a fix

## Rules

- Focus on one fix per run, including a past commit or PR when requested.
- Verify the root cause, affected versions, symptom, and workaround before drafting.
- Public posting requires approval for the targets and content; research or drafting permission is not posting permission.
- Add technical value, not promotion or “me too” comments. Skip weak matches and duplicate outreach.

## Research

1. Read the fix, linked issue, relevant project/upstream source, and verification evidence.
2. Search for matching upstream reports, downstream symptoms, and useful closed discussions; inspect each target's full context.
3. Rank targets by match confidence and check whether the user already replied.
4. Work directly unless the user authorizes research delegation.

## Draft

- Use supplied voice preferences and relevant examples of the user's writing; do not scan unrelated personal memory.
- Match the audience's register without forced slang, invented emotions, or claims of experience the user did not have.
- State the symptom, explain the cause, show the fix or link it, and credit prior contributors.
- Distinguish confirmed fixes, workarounds, and untested alternatives.
- Example shape: “This appears related to [verified cause]. [Change] fixed it in [tested environment]; here's the patch and its limitations.”
- Upstream issues can use headings for reproduction, versions/environment, root cause, impact, and proposed fixes.

## Approve, post, record

1. Present the ranked targets and full drafts for approval unless already explicitly approved.
2. Submit approved content using body-file/JSON inputs or a connector; never interpolate bodies into shell source.
3. Read back each post to verify target, author, content, and URL.
4. Save the fix link, posted URLs, skipped targets, and follow-up in the supplied location, or `tmp/outreach/YYYY-MM-DD-topic.md`.

## Grain handoff

- If connected, keep research, drafts, and the outreach record in the supplied task folder, or `Development Artifacts/YYYY-MM-DD-<task>`; pass its ID and rule to any authorized researchers and sync outputs.
- Keep needed local files and privacy limits; without Grain, continue locally silently. Grain storage does not authorize public posting.
