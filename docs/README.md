# Workflow visuals

The current Parsa workflows live in `parsa/`. Current Orchestra is maintained
in [dcouple/orchestra](https://github.com/dcouple/orchestra). The two historical
images below retain the old design for context and carry visible archive
labels so they cannot be mistaken for installation or execution instructions.

| Visual | Status and scope | Source | Render |
| --- | --- | --- | --- |
| Parsa workflow | Current software stages, continuation, model selection, and business handoffs | [Excalidraw](readme-workflow-map.excalidraw) | [PNG](readme-workflow-map.png) |
| Skill legend | Current primary skills and supporting roles; installation can add a `p-` prefix to collisions | [Excalidraw](readme-skill-legend.excalidraw) | [PNG](readme-skill-legend.png) |
| SEO workflow | Campaign strategy, focused page work, writing-skill selection, and publication boundaries | [Excalidraw](seo-workflow-map.excalidraw) | [PNG](seo-workflow-map.png) |
| Software-factory story | Conceptual evolution; paired with Orchestra's copy in this overhaul | [Excalidraw](software-factory-story.excalidraw) | [PNG](software-factory-story.png) |
| Tyler workflow | Historical snapshot of the frozen ancestor; old capture names and model routes are retained as history | [Excalidraw](tyler-workflow-map.excalidraw) | [PNG](tyler-workflow-map.png) |
| Software Orchestra sketch | Historical early design, including proposed loops and templates | [Excalidraw](software-orchestra.excalidraw) | [PNG](software-orchestra.png) |

The software-factory story describes a direction for configured intake. It
does not imply that every pictured schedule or deployment is running. Use
[Orchestra's workflow guide](https://github.com/dcouple/orchestra/blob/main/WORKFLOW.md)
for its current executable contracts.

## Regenerate

From the repository root, install the renderer dependencies once:

```bash
uv sync --project parsa/.claude/skills/excalidraw-pr-diagrams/references
uv run --project parsa/.claude/skills/excalidraw-pr-diagrams/references playwright install chromium
```

Render each changed source and inspect its PNG at README size. Fix clipping,
overlap, or wrong connections, then commit the source and PNG together:

```bash
uv run --project parsa/.claude/skills/excalidraw-pr-diagrams/references python parsa/.claude/skills/excalidraw-pr-diagrams/references/render_excalidraw.py "$PWD/docs/readme-workflow-map.excalidraw"
```

Replace the input filename for the other maps. The `.codex/` variant carries
the same rendering tools. Historical content stays historical; refresh its
archive label or links if needed without presenting it as today's workflow.
