---
name: html-explainer
description: Render a readable, self-contained HTML explainer with useful visuals, accessible layout, and verified content.
argument-hint: "[what to explain, when invoked directly]"
allowed-tools: Read, Grep, Glob, Bash, Write
---

# HTML Explainer

## Task: $ARGUMENTS

- Lead with the explanation the reader needs; use visuals to clarify relationships rather than decorate.
- Apply the caller's content and design requirements. The tokens and components below are reusable defaults, not a mandatory product identity.

## The file

- Produce one self-contained `.html` file with inline CSS/SVG and system fonts. Avoid external resource dependencies and unnecessary scripts.
- Save to the caller's destination, or `tmp/`; open it with available browser tooling when requested or appropriate.
- If Grain is connected, also save the page and supporting artifacts in the supplied task folder, or `Development Artifacts/YYYY-MM-DD-<task>`.
- Keep needed local files and privacy limits; without Grain, continue locally silently. This does not authorize public hosting.

## Tokens

Use these defaults when the caller supplies no design system; adapt them to the requested identity and accessibility needs.

```css
:root {
  --paper: #FAF8F5; --ink: #1F2328; --ink-soft: #5A5F66;
  --line: #E4DFD7; --panel: #FFFFFF;
  --accent: #0E7569; --accent-soft: #E3F0EE;
  --warn: #B45309; --warn-soft: #F7EBDD;
  --bad: #9F3A38; --bad-soft: #F6E8E7;
  --mono: ui-monospace, "SF Mono", SFMono-Regular, Menlo, Consolas, monospace;
  --serif: Georgia, "Iowan Old Style", "Times New Roman", serif;
  --sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
}
@media (prefers-color-scheme: dark) {
  :root {
    --paper: #15191D; --ink: #E8E6E1; --ink-soft: #9BA1A8;
    --line: #2C3237; --panel: #1C2126;
    --accent: #2FA79A; --accent-soft: #16302D;
    --warn: #D98E3D; --warn-soft: #32271A;
    --bad: #CF6F6C; --bad-soft: #33211F;
  }
}
```

## Drawings

Open with a useful diagram when the explanation depends on a flow, comparison, or relationship. A short factual answer need not acquire a decorative diagram.

- Inline SVG on the tokens: `--panel` fills, `--line` strokes,
  `--accent` for the path that matters, `--warn` and `--bad` where
  verdicts are part of the picture, `--sans` labels at 12 to 14px.
- Sketch energy over precision: slightly rounded corners, imperfect
  widths, dashed strokes for the tentative and solid for the certain,
  arrows with real heads. Boxes and arrows over art; three boxes and an
  arrow beats a mural.
- Warmth comes from the drawing, never from decoration: no gradients,
  no shadows, no icon fonts, no clip art.
- Legible at page width, `viewBox` set, no fixed pixel widths. A simple
  subject needs only a simple drawing when a drawing helps.
- When the user wants a diagram they can edit themselves, that is the
  excalidraw-pr-diagrams skill's job, not an inline SVG.

## Type and layout

- Body: `--sans`, 16px, line-height 1.6, `--ink` on `--paper`, one
  centered column, `max-width: 72ch`, generous vertical rhythm.
- `h1`: `--serif`, weight 500, ~2.1rem, `text-wrap: balance`. One per
  page. Directly under it, a one-sentence standfirst in `--ink-soft`.
- Section headers: a mono uppercase eyebrow (`.72rem`, letter-spacing
  `.1em`, `--accent`) above an `h2` (~1.25rem). Sections are numbered
  when order matters and unnumbered when it does not.
- Code: `--mono` on `--panel` with a `--line` border. Prose lines stay
  under 90 characters; nothing scrolls horizontally except inside a
  `pre` with its own overflow.

## Components

Use these components where they help; adapt or omit them for the deliverable:

- `.badge`: mono, uppercase, `.72rem`, soft background. Accent for
  identity and success, warn for caution, bad for failure. Badges carry
  verdicts; prose carries reasons.
- `.panel`: `--panel` background, `--line` border, 6px radius, padded.
  The unit of grouped content; grids of panels for comparisons
  (before/after, expected/actual).
- `.callout`: a panel with a 3px left border in accent, warn, or bad.
  One-paragraph emphasis, used sparingly.
- `.card`: a panel with a mono eyebrow title, for repeating items
  (a lesson, a promise, a dependency).
- `details > summary`: for depth the reader opts into. The page must
  read complete with every `details` closed.

## The bar

Before opening the page, verify all of these; fix rather than ship:

1. A reader who skims the headings and any visuals leaves oriented; include drawings only when they clarify the material.
2. Renders complete with JavaScript disabled and every `details`
   closed.
3. Nothing is fetched: no `src`, `href`, or `url()` that loads an
   external resource (stylesheet, script, font, image). URLs quoted as
   text or code content are fine; a page about an endpoint must be able
   to print it.
4. Both color schemes hold: readable in light and dark.
5. Every fact on the page came from the caller's material; the page
   adds structure and pictures, never claims.
6. One `h1`, logical heading order, readable narrow-screen layout, and accessible labels for meaningful drawings.

## Boundaries

- This skill owns form. The invoking skill owns content, truth, where
  the file lives, and what the chat reply says; its reply and
  open-in-browser rules override the defaults here.
- Adapt the page to the user's needs without changing this skill or opening an unrelated PR.
