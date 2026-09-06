---
name: excalidraw-diagram
description: "Create Excalidraw diagrams for requested visual explanations or PR changes whose relationships benefit from a diagram."
---

# Excalidraw diagrams

Make the relationship visible: a boundary, sequence, comparison, hierarchy, or
change in behavior. Ground technical labels and before/after states in the
source. Choose enough detail for the audience; do not turn a simple explanation
into a comprehensive architecture map.

## Load what the output needs

| Need | Read |
| --- | --- |
| PR visual, reviewer explainer, or media publishing | [Publishing contract](references/publishing.md), before any external write |
| Complex technical layout or unfamiliar composition | [Design guidance](references/design.md), relevant sections only |
| A suitable visual pattern, typography, or color choice | [Pattern reference](references/patterns.md), relevant sections only |
| Producing or changing Excalidraw JSON | [Rendering contract](references/rendering.md) and [element templates](references/element-templates.md) |

The [palette](references/color-palette.md) and [JSON schema](references/json-schema.md)
are available for those details. Resolve `references/...` paths from this skill's
directory. The renderer and its dependencies remain in that folder.

## Completion and permissions

Keep PR working artifacts in scratch. Render edited JSON to PNG, inspect the
actual image, and fix observable errors. Stop after a clear, accurate, legible
render; extra polish passes are not a quota. For a published result, verify
its durable asset and PR readback under the publishing contract.

Creating a diagram does not grant publication, asset overwrite, release
creation, or changes to release metadata. Preserve the caller's exact scope
and the publishing contract's authorization requirements. If publication is
blocked, retain the concrete local artifact and report what remains.
