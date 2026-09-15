---
name: excalidraw-diagram
description: Create and visually validate editable Excalidraw diagrams for workflows, architecture, or before/after PR explanations.
---

# Excalidraw diagrams

Show a relationship that is easier to understand visually. Do not turn a paragraph into decorative boxes.

## Understand and sketch

- Read the relevant code, diff, or source material. Verify technical details against actual implementation and primary documentation when needed.
- Identify the audience and the one relationship or change the diagram should explain.
- For PR overviews, show explicit **Before** and **After** paths grounded in the diff. Do not assume every change fixes a failure or makes the system safer.
- Include real example inputs, outputs, or event names when they help; remove secrets and avoid fabricated evidence.

Choose the structure that fits:

| Relationship | Useful structure |
|---|---|
| Ordering or a race | Timeline |
| Ownership or trust boundary | Labeled regions/swimlanes |
| State changes or retries | State machine or loop |
| One source, many consumers | Fan-out |
| Several inputs, one result | Convergence |
| Hierarchy or containment | Tree/nesting |

Use short labels, clear actors, and a one-line takeaway. Explain unfamiliar terms when the audience needs it; metaphors must preserve the real relationships.

## Build the source

- Read `references/element-templates.md` and `references/json-schema.md` before authoring JSON.
- Use `references/color-palette.md` as a default, or the requested brand style. Do not rely on color alone for meaning.
- Use descriptive unique IDs, valid reciprocal bindings, and intentional line breaks. Keep text dimensions large enough for the renderer.
- Add containers where they convey grouping, action, or boundaries; no mandatory container ratio, canvas size, or layout variety.
- Build large diagrams in manageable sections and check cross-section bindings. Small diagrams do not need an artificial multi-step generation process.

## Render and inspect

From this skill's `references/` directory, use the supplied renderer:

```bash
uv run python render_excalidraw.py /path/to/diagram.excalidraw --output /path/to/diagram.png
```

See `README.md` for setup and network requirements. View the exported PNG; JSON validation alone is insufficient.

- Check labels, clipping, overlaps, arrow endpoints, whitespace, and contrast.
- Inspect at the size the recipient will see, including embedded PR size.
- Confirm the visual matches the evidence and makes the before/after difference clear.
- Fix material issues and re-render. Stop when it is accurate and readable; report unavailable rendering rather than claiming visual validation.

## Storage and sharing

- Use a task-specific temporary directory for PR working files unless tracked assets were requested. Keep the editable source and rendered image together.
- If Grain is connected, save sources, renders, and manifests in the shared task folder and pass its ID/storage rule to delegated work. Use a branch/ticket name initially, then the PR title once created. Local working copies are fine; otherwise continue normally.
- Grain storage does not authorize public publication. Before hosting assets or updating a PR, read `references/pr-publishing.md` and confirm that action is authorized.
- Return artifact links, source/render locations, and validation or publication blockers.
