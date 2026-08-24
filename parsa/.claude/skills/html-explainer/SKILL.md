---
name: html-explainer
description: The house standard for any skill that renders an HTML page for a person to read, covering design tokens, typography, components, diagrams, and quality gates so every generated page shares one calm, minimal look. Use when a skill's instructions say to render its output per the html-explainer standards, or when the user asks for an HTML explainer of anything and no more specific skill applies.
argument-hint: "[what to explain, when invoked directly]"
allowed-tools: Read, Grep, Glob, Bash, Write
---

# HTML Explainer

## Task: $ARGUMENTS

A generated page with no standards drifts: every run invents its own
fonts, colors, and structure, and the reader pays for it. This skill is
the one place the look and the bar are defined. Skills that produce
pages (teach-back, reality-check, eli5, and whatever comes next) follow
it; invoked directly, it renders a one-off explainer of whatever the
argument names.

## The file

One self-contained `.html` file. Inline CSS in a single `<style>` block,
inline SVG for every diagram, no external requests of any kind: no CDN,
no web fonts, no remote images, no scripts unless the page genuinely
needs interaction, and then only vanilla inline JS. System font stacks
only. Target well under 200KB. Write it to `./tmp/` (or the caller's
stated destination), then open it in the browser (`open` on macOS,
`xdg-open` on Linux) unless the caller says not to.

## Tokens

Copy this block verbatim as the start of the style sheet. Extend it only
by adding tokens, never by restyling these.

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

The whole vocabulary. A page uses what it needs and invents nothing:

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

## Visual weight

The page is graphic-first: diagrams carry the argument and prose
annotates them, the way an excalidraw sketch carries a PR review. When
drafting, budget the page as pictures interrupted by words, not words
garnished with pictures; if a section has no visual, ask whether it
earns its place or belongs inside a details block. There is no hosting,
no capability layer, no publish step to design for: one local file,
opened in a browser, tuned entirely for reading.

Sketch aesthetic is welcome and cheap in SVG: slightly rounded corners,
imperfect widths, dashed strokes for the tentative, solid for the
certain, arrows with real heads. Warmth comes from the drawing, never
from decoration; no gradients, no shadows, no icon fonts. When the user
wants a diagram they can edit themselves, that is the
excalidraw-pr-diagrams skill's job, not an inline SVG.

## Diagrams

Every explainer opens with one diagram directly after the masthead: the
whiteboard sketch the page then elaborates. Inline SVG drawn on the
tokens (`--panel` fills, `--line` strokes, `--accent` for the path that
matters, `--sans` labels at 12 to 14px). Boxes and arrows over art;
three boxes and an arrow beats a mural. Legible at page width, `viewBox`
set, no fixed pixel widths. A simple subject gets a simple diagram,
never a skipped one.

## The bar

Before opening the page, verify all of these; fix rather than ship:

1. Renders complete with JavaScript disabled and every `details` closed.
2. No external request of any kind (grep the file for `http` and
   `url(`).
3. Both color schemes hold: readable in light and dark.
4. Every fact on the page came from the caller's material; the page adds
   structure and pictures, never claims.
5. The diagram is present and would orient a stranger in ten seconds.
6. One `h1`, sections in reading order, nothing beyond the component
   vocabulary above.

## Boundaries

- This skill owns form. The invoking skill owns content, truth, and
  where the file lives.
- When a caller's needs exceed the vocabulary, extend the vocabulary
  here in a PR, do not fork the style inline.
- No em dashes, on the page and in this file.
