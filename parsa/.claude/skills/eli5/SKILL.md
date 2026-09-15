---
name: eli5
description: Explain one unfamiliar topic in plain language as a concise, visual HTML page.
argument-hint: "<topic, question, or path to explain>"
model: claude-opus-4-6
allowed-tools: Read, Grep, Glob, Bash, Write
---

# ELI5

## Ground the explanation

- Treat the reader as capable but new to this topic, not as a child.
- For project topics, read the actual code and trace the relevant flow. Verify uncertain external facts with authoritative sources.
- Select the few facts the explanation depends on; say when the thing does not work or evidence is missing.

## Three levels

1. Picture and intuition: one honest diagram or metaphor plus an opening under roughly 100 words.
2. Mechanism: explain how it works, introducing terms when needed; use comparisons where helpful.
3. Optional depth: put technical names, code anchors, misconceptions, limitations, and further reading in `details` blocks.

## Write and deliver

- Use `html-explainer` for the page; aim for under 600 visible words unless the request needs more.
- Prefer concrete detail over adjectives. Keep a metaphor only while its parts correspond to the real mechanism.
- Accuracy outranks simplicity: name important omissions rather than distorting the explanation.
- Use the configured writer when supported; honor any explicit model requirement and report unavailable capabilities honestly.
- Return the page link and a short description.

## Grain handoff

- If connected, save the explanation and supporting artifacts in the supplied task folder, or `Development Artifacts/YYYY-MM-DD-<task>`; pass the storage rule to any writer/helper.
- Keep needed local files and privacy limits; without Grain, use the normal local HTML handoff silently.
