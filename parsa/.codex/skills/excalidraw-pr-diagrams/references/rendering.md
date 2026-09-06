# Rendering reference

Paths written as `references/...` resolve from the skill directory.

## JSON Structure

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [...],
  "appState": {
    "viewBackgroundColor": "#ffffff",
    "gridSize": 20
  },
  "files": {}
}
```

## Element Templates

See `references/element-templates.md` for copy-paste JSON templates for each element type (text, line, dot, rectangle, arrow). Pull colors from `references/color-palette.md` based on each element's semantic purpose.

---

## Render & Validate (MANDATORY)

You cannot judge a diagram from JSON alone. After generating or editing the Excalidraw JSON, you MUST render it to PNG, view the image, and fix what you see — in a loop until it's right. This is a core part of the workflow, not a final check.

### How to Render

```bash
cd .claude/skills/excalidraw-pr-diagrams/references && uv run python render_excalidraw.py <path-to-file.excalidraw>
```

For Codex installs, use the matching `.codex/skills/excalidraw-pr-diagrams/references` directory.

This outputs a PNG next to the `.excalidraw` file. Then use the available image viewer on the PNG to actually inspect it, such as the Read tool, `view_image`, or a browser screenshot.

### The Loop

After generating the initial JSON, run this cycle:

**1. Render & View** — Run the render script, then Read the PNG.

**2. Audit against your original vision** — Before looking for bugs, compare the rendered result to what you designed in Steps 1-4. Ask:
- Does the visual structure match the conceptual structure you planned?
- Does each section use the pattern you intended (fan-out, convergence, timeline, etc.)?
- Does the eye flow through the diagram in the order you designed?
- Is the visual hierarchy correct — hero elements dominant, supporting elements smaller?
- For technical diagrams: are the evidence artifacts (code snippets, data examples) readable and properly placed?
- For PR diagrams: does the rendered image tell a non-redundant before/after story through structure, not just labels?
- Would the image still communicate the main change if the prose paragraphs were removed?

**3. Check for visual defects:**
- Text clipped by or overflowing its container
- Text or shapes overlapping other elements
- Arrows crossing through elements instead of routing around them
- Arrows landing on the wrong element or pointing into empty space
- Arrowheads, dashed loops, or feedback paths visually sitting on top of boxes or labels
- Labels floating ambiguously (not clearly anchored to what they describe)
- Uneven spacing between elements that should be evenly spaced
- Sections with too much whitespace next to sections that are too cramped
- Text too small to read at the rendered size
- Overall composition feels lopsided or unbalanced
- Any part of the title, subtitle, truth statement, or major region clipped by the screenshot bounds
- A horizontally sprawling image whose important content is hard to scan in a GitHub PR
- PR-specific defects: the published image URL 404s, the PR body image does not render, or Markdown formatting collapses into a single paragraph.

**4. Fix** — Edit the JSON to address everything you found. Common fixes:
- Widen containers when text is clipped
- Adjust `x`/`y` coordinates to fix spacing and alignment
- Add intermediate waypoints to arrow `points` arrays to route around elements
- Reposition labels closer to the element they describe
- Resize elements to rebalance visual weight across sections
- Shrink titles and labels before enlarging the diagram further.
- Replace long labels with a diagrammatic construct: boundary, queue, gate, loop, timeline, or swimlane.

**5. Re-render & re-view** — Run the render script again and Read the new PNG.

**6. Repeat** — Keep cycling until the diagram passes both the vision check (Step 2) and the defect check (Step 3). Typically takes 2-4 iterations. Don't stop after one pass just because there are no critical bugs — if the composition could be better, improve it.

### When to Stop

The loop is done when:
- The rendered diagram matches the conceptual design from your planning steps
- No text is clipped, overlapping, or unreadable
- Arrows route cleanly and connect to the right elements
- Spacing is consistent and the composition is balanced
- You'd be comfortable showing it to someone without caveats
- For PR diagrams, the before and after are visually different in a way that reflects the actual code change.
- The diagram would not be equally useful as a plain bullet list.

### First-Time Setup
If the render script hasn't been set up yet:
```bash
cd .claude/skills/excalidraw-pr-diagrams/references
uv sync
uv run playwright install chromium
```

For Codex installs, use `.codex/skills/excalidraw-pr-diagrams/references`.

---

## Quality Checklist

### Depth & Evidence (Check First for Technical Diagrams)
1. **Research done**: Did you look up actual specs, formats, event names?
2. **Evidence artifacts**: Are there code snippets, JSON examples, or real data?
3. **Multi-zoom**: Does it have summary flow + section boundaries + detail?
4. **Concrete over abstract**: Real content shown, not just labeled boxes?
5. **Educational value**: Could someone learn something concrete from this?

### Conceptual
6. **Isomorphism**: Does each visual structure mirror its concept's behavior?
7. **Argument**: Does the diagram SHOW something text alone couldn't?
8. **Variety**: Does each major concept use a different visual pattern?
9. **No uniform containers**: Avoided card grids and equal boxes?
10. **Non-redundant**: The image is not just the PR description repeated in boxes.
11. **Before/after story**: The old failure path and new success path are visibly different.
12. **Metaphor fit**: The chosen metaphor matches the change type (boundary, lifecycle, race, permission, ownership, etc.).

### Container Discipline
13. **Minimal containers**: Could any boxed element work as free-floating text instead?
14. **Lines as structure**: Are tree/timeline patterns using lines + text rather than boxes?
15. **Typography hierarchy**: Are font size and color creating visual hierarchy (reducing need for boxes)?

### Structural
16. **Connections**: Every relationship has an arrow or line
17. **Flow**: Clear visual path for the eye to follow
18. **Hierarchy**: Important elements are larger/more isolated

### Technical
19. **Text clean**: `text` contains only readable words
20. **Font**: `fontFamily: 3`
21. **Roughness**: `roughness: 0` for clean/modern (unless hand-drawn style requested)
22. **Opacity**: `opacity: 100` for all elements (no transparency)
23. **Container ratio**: <30% of text elements should be inside containers

### Visual Validation (Render Required)
24. **Rendered to PNG**: Diagram has been rendered and visually inspected
25. **No text overflow**: All text fits within its container
26. **No clipping**: Screenshot bounds include every title, label, arrow, and shape
27. **No overlapping elements**: Shapes and text don't overlap unintentionally
28. **Even spacing**: Similar elements have consistent spacing
29. **Arrows land correctly**: Arrows connect to intended elements without crossing others
30. **Readable at export size**: Text is legible in the rendered PNG
31. **Balanced composition**: No large empty voids or overcrowded regions
32. **GitHub readable**: The image is understandable when embedded in a PR without opening it full-size
