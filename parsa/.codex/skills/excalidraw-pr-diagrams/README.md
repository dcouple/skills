# Excalidraw Diagram Skill

A coding agent skill that generates beautiful and practical Excalidraw diagrams from natural language descriptions. Not just boxes-and-arrows - diagrams that **argue visually**. It also supports PR visual overviews that teach before/after changes to reviewers.

Compatible with any coding agent that supports skills. Use `.claude/skills/` for Claude Code and `.codex/skills/` for Codex.

## What Makes This Different

- **Diagrams that argue, not display.** Every shape/group of shapes mirrors the concept it represents — fan-outs for one-to-many, timelines for sequences, convergence for aggregation. No uniform card grids.
- **Evidence artifacts.** As an example, technical diagrams include real code snippets and actual JSON payloads.
- **Built-in visual validation.** A Playwright-based render pipeline lets the agent see its own output, catch layout issues (overlapping text, misaligned arrows, unbalanced spacing), and fix them in a loop before delivering.
- **PR-ready handoff.** The skill covers shareable reviewer explainers, committed PR assets, raw GitHub image URLs, and PR body preview checks.
- **Brand-customizable.** All colors and brand styles live in a single file (`references/color-palette.md`). Swap it out and every diagram follows your palette.

## Installation

Clone or download this repo, then copy the skill into the right agent directory:

```bash
cp -r parsa/.claude/skills/excalidraw-pr-diagrams ~/.claude/skills/excalidraw-pr-diagrams
cp -r parsa/.codex/skills/excalidraw-pr-diagrams ~/.codex/skills/excalidraw-pr-diagrams
```

## Setup

The skill includes a render pipeline that lets the agent visually validate its diagrams. There are two ways to set it up:

**Option A: Ask your coding agent (easiest)**

Just tell your agent: *"Set up the Excalidraw diagram skill renderer by following the instructions in SKILL.md."* It will run the commands for you.

**Option B: Manual**

```bash
cd .claude/skills/excalidraw-pr-diagrams/references
uv sync
uv run playwright install chromium
```

For Codex installs, use `.codex/skills/excalidraw-pr-diagrams/references`.

## Usage

Ask your coding agent to create a diagram:

> "Create an Excalidraw diagram showing how the AG-UI protocol streams events from an AI agent to a frontend UI"

Or ask for a PR visual overview:

> "Create a shareable PR diagram that explains the before and after behavior, commit the PNG under .github/pr-assets, and update the PR body."

The skill handles the rest — concept mapping, layout, JSON generation, rendering, and visual validation.

## Customize Colors

Edit `references/color-palette.md` to match your brand. Everything else in the skill is universal design methodology.

## File Structure

```
excalidraw-pr-diagrams/
  SKILL.md                          # Design methodology + workflow
  references/
    color-palette.md                # Brand colors (edit this to customize)
    element-templates.md            # JSON templates for each element type
    json-schema.md                  # Excalidraw JSON format reference
    render_excalidraw.py            # Render .excalidraw to PNG
    render_template.html            # Browser template for rendering
    pyproject.toml                  # Python dependencies (playwright)
```
