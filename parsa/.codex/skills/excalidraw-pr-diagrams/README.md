# Excalidraw diagrams

Creates editable diagram sources and visually checked PNGs. See [SKILL.md](SKILL.md) for design, Grain storage, and PR handoff rules.

## Setup

Install this directory in a supported skill location for your agent. From the installed skill's `references/` directory:

```bash
uv sync
uv run playwright install chromium
uv run python render_excalidraw.py /path/to/diagram.excalidraw
```

- Requires Python 3.11+, `uv`, and Playwright Chromium.
- The browser template loads Excalidraw 0.18.0 from `esm.sh`; rendering needs network access and runs third-party code. Use an approved offline renderer for restricted material.
- The default output is a PNG beside the source; `--output`, `--scale`, and `--width` customize it. Inspect the actual image afterward.

## References

- [Palette](references/color-palette.md): optional default colors.
- [Element templates](references/element-templates.md): editable JSON examples.
- [Format notes](references/json-schema.md): fields and bindings used by the bundled renderer.
- [PR publication](references/pr-publishing.md): authorization, durable assets, verification, and PR markers.

Example: “Show the old retry path and the new deduplicated path for this PR.” Publishing the result requires separate authorization for the applicable actions.
