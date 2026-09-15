---
name: product-compare
description: "Research a product category, compare options against requirements, and publish an interactive Grain comparison artifact with decision matrices, product images, feature checklists, day-in-the-life simulations, and hover previews. Use when the user wants to compare products for a purchase decision: 'compare X', 'help me pick a Y', 'what Z should I buy'."
argument-hint: "<product category> + <requirements or use case>"
model: claude-opus-4-6
allowed-tools: Read, Grep, Glob, Bash, Write, Edit, WebSearch, WebFetch, Agent, ToolSearch
---

# Product Compare

## Task: $ARGUMENTS

Build an interactive product comparison in Grain that helps the user
and their team make a purchase decision. The artifact is the
deliverable, not the chat. Do the writing yourself; do not delegate
it to a subagent. You need to see the full page to know if it reads
well.

## Reading order and progression

The page tells a story from wide to narrow. A reader who stops at
any level leaves oriented:

1. **Matrices first.** The 2-3 scatter plots are the page's opening
   argument. A reader who sees only these leaves knowing the shape
   of the market and where each product sits.
2. **Category callouts.** Products split into fundamentally different
   categories (e.g., display vs waveguide, portable vs desktop).
   Name these categories after the matrices, before the cards. The
   comparison is between categories first, products second.
3. **Glossary for newcomers.** Before the cards, add a callout
   defining every term the reader needs. Use relatable comparisons
   ("your phone at arm's length is roughly 30 degrees" for FOV;
   "you need at least ~800 nits for comfortable outdoor reading" for
   brightness). Expand every abbreviation on first use. The reader
   may know nothing about this product category.
4. **Product cards by category.** Grouped into tiers, best-fit-first.
5. **The honest answer.** After showing all options, a section that
   honestly answers "can you actually use this for your stated
   purpose?" This is where marketing meets reality. It is often the
   turning point in the decision.
6. **Finalists head-to-head.** The top 2-3 side by side with
   detailed tables, not just spec chips.
7. **Day-in-the-life simulations.** Timeline narratives of a real
   day with each finalist for the user's use case.
8. **Brand deep dives.** Added on demand when the user zooms into a
   specific brand. Compare ALL models from that brand.
9. **Recommendations.** Frame as approaches or trade-offs. "Or get
   both" is a valid recommendation when two products serve different
   conditions (rain vs dry, weekday vs weekend, travel vs desk).

## The process

### 1. Understand the decision

Extract from the user's message (or ask):
- Product category
- Use case / context (how, where, how long, what environment)
- Must-have requirements
- Nice-to-haves
- Budget range (or "no budget")
- Who is deciding (solo, cofounder, team)
- **Location and climate** (rain, sun, temperature affect many
  product categories: wearables, outdoor gear, vehicles, electronics)

### 2. Research the market

Use WebSearch and WebFetch to build a complete picture:
- Search for "[category] comparison [year]", "[category] best [year]",
  "[category] all models specs"
- Visit official product pages for exact specs
- Visit review sites for real-world findings
- **Find ALL models from each brand**, not just the flagship
- Note contradictions between sources; use manufacturer specs as
  baseline, reviewer measurements as reality check
- Search for durability, water resistance (IP rating), warranty
- **Manufacturer claims vs reviewer reality:** Battery life is almost
  always overstated. Find reviewer measurements. Call out the gap
  prominently. A product card that says "48h battery" when real
  active use is 12-15h misleads the buyer. Show the real number
  prominently, the marketing number in parentheses.

Cross-check every number. A price or spec that differs between
sections destroys trust in the whole document.

### 3. Discover categories

Products almost always split into fundamentally different types that
serve the use case differently. Discover these categories during
research:
- Name each category plainly (e.g., "Display Cinema" vs "All-Day
  Wearable HUD" vs "Polished Companion")
- Identify the core trade-off between categories (not products)
- The first matrix visualizes this split

This is the most important analytical step. The user thinks they're
choosing between products. They're actually choosing between
categories. Help them see that.

### 4. Collect product images

For each product, download 3-6 images to the Grain checkout's `img/`
folder:
- **First image must be a person using the product** (wearing,
  holding, in context). This is how the user judges "will I look
  dumb?"
- Then: product shots from different angles, close-ups, accessories
- Download from official product pages (Shopify CDN, Sanity CDN,
  manufacturer sites)
- **Always download locally with curl.** Never use external URLs in
  the HTML. Grain's CSP blocks external images. Every image must be
  a local path like `img/brand-model-1.jpg`.
- Size images at 400-600px width for thumbnails
- Verify: `grep -c 'https://' index.html` must return 0 (only local
  paths in the HTML; external URLs live only in the JS product data
  object, and those should also be local)

### 5. Build the comparison artifact

Create as a Grain workspace (`grain_new` with template `html`, then
edit `index.html` and `grain_push`). The HTML is self-contained:
inline CSS, inline SVG for charts, inline JS for interactivity,
local images from `img/`.

#### Design tokens

```css
:root {
  --paper: #FAF8F5; --ink: #1F2328; --ink-soft: #5A5F66;
  --line: #E4DFD7; --panel: #FFFFFF;
  --accent: #0E7569; --accent-soft: #E3F0EE;
  --warn: #B45309; --warn-soft: #F7EBDD;
  --bad: #9F3A38; --bad-soft: #F6E8E7;
  --mono: ui-monospace, "SF Mono", SFMono-Regular, Menlo, Consolas,
          monospace;
  --serif: Georgia, "Iowan Old Style", "Times New Roman", serif;
  --sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
          sans-serif;
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

Use `--accent` for good/yes/winner, `--warn` for caution/partial,
`--bad` for no/fail/dealbreaker.

#### Decision matrices (SVG)

Each matrix is a 2-axis scatter plot. Three matrices cover the
decision space:

**Matrix 1: The primary category trade-off.** The x-axis is the
dimension most aligned with the user's top priority. Products on the
right are better fits. Zone labels name the clusters. An "IDEAL ZONE"
dashed box marks where the user wants to be.

**Matrix 2: Physical constraints.** Weight, battery, size, comfort.
Add threshold lines for hard requirements (e.g., a dashed red "8
HOURS" line across a battery axis). Products above the line meet the
requirement; below do not.

**Matrix 3: Ecosystem / integration.** Compatibility, app support,
dev platform, customizability. Tier lines separate different levels
(e.g., "USB-C MIRROR" tier vs "BLE COMPANION" tier).

**Matrix construction rules:**
- Every dot shows the all-in price (including required accessories).
- Wrap each product in `<g class="dot">` with data attributes:
  `data-name`, `data-price`, `data-breakdown` (pipe-separated),
  `data-battery` (pipe-separated scenarios), `data-note`.
- **Overlap check:** For every pair of dots, verify
  `sqrt((cx1-cx2)^2 + (cy1-cy2)^2) > r1 + r2 + 4`. If not,
  separate them. Labels alternate above/below and left/right to
  avoid text overlap.
- Zone labels: soft colored `<rect>` backgrounds with mono uppercase
  labels and a one-line description below.
- Sweet-spot / interesting-middle zones: dashed border rectangles
  with accent/warn color.
- Threshold lines: dashed lines with a label at one end.
- Mark one dot with a thicker stroke or larger radius when it leads
  a dimension.
- Each matrix sits inside a `<div style="position:relative">` with
  a tooltip div (see interactivity below).
- Add `<p>` instruction text above: "Hover or tap any dot for price
  breakdown and details."

#### Product cards

One card per product, grouped by category. Each card:
- **Image gallery** (`.gal` class): horizontal scroll of 3-6 local
  images, first image slightly taller. All clickable for lightbox.
- **Product name** wrapped in `<a>` linking to official product page,
  styled with `border-bottom: 1.5px solid var(--accent)`.
- **Badge** for category-winners: mono uppercase on soft background
  (`.badge .ba` for accent, `.bw` for warn).
- **All-in price** in mono accent, with breakdown note if accessories
  required.
- **Spec chips** (`.spec`): 4-6 key numbers in small mono pills.
- **Description** (`.co`): 2-4 lines explaining what this product is
  and what makes it different.
- **Feature checklist** (`.fl`): items relevant to the user's use
  case (not generic specs). Each item shows check (`--accent`),
  cross (`--bad`, dimmed), or partial (`--warn`), with a one-line
  note. Include use-case-specific features: for wearables, add
  "rain-safe", "8-hour comfort"; for desk gear, "cable management",
  "noise level".
- **Verdict** (`.cv`): "Pros: ... Cons: ..." in a soft accent box.

#### Reality check section

After all cards, an honest callout about the fundamental trade-off.
Structure:
- "Can you actually use [category A] for [stated use case]?"
- What the marketing implies vs what reviewers consistently report
- Side-by-side cards: category A ("what it's like") vs category B
  ("what it's like"), written as felt experience not specs
- "For [your use case], [category] is the right category because..."
- The callout that reframes the decision

This section is where the user often realizes they've been looking
at the wrong category. It should be plainly written, not hedged.

#### Finalists head-to-head

When the decision narrows to 2-3 options, add a detailed comparison:
- Side-by-side cards with product images
- Spec comparison table (row per feature, winner highlighted with
  accent color and bold)
- "The real trade-off in one sentence" at the bottom (e.g., "Even G2
  is the glasses you forget you're wearing; Meta is the glasses
  you're glad you're wearing.")
- An "or get both" callout when two products serve different
  conditions

#### Day-in-the-life simulations

For the top 3-5 products, write a timeline of a realistic day:
- Start with **"What is this?"** intro (2-3 sentences explaining the
  product for someone who didn't read the card above)
- Timestamps from morning to end of use period (match the user's
  stated duration)
- At each timestamp: what you do, what works, what doesn't
- **Highlight friction points** in `--warn` or `--bad` color spans
- At key intervals, note battery percentage, comfort level, and
  whether anyone gave you a weird look
- End with a verdict box summarizing the experience in 2 sentences
- If a simulation references an accessory or feature not explained
  earlier (charging case, companion app), explain it inline
- Never say "you built [something]" as if it happened that morning;
  if custom dev was needed, say "you spent a weekend beforehand
  building..."

#### Brand deep dives

Added when the user zooms into a brand. Include:
- ALL current models from that brand (not just the flagship)
- A weight-vs-feature scatter plot specific to the brand
- Mini-cards for each model with image, price, key specs
- Head-to-head table comparing the top 2 within the brand
- Callout: "For [your criteria], [model] is the sweet spot because..."
- Link every model name to its official product/shop page
- Note any brand-wide limitations (e.g., "no water resistance on any
  model")

#### Glossary callout

Place early, after the matrices and before the cards. Define every
term the reader needs using this structure:
- **Term** = plain-language definition with a relatable comparison
- Cover: units of measurement, acronyms, technology names, category
  names
- If a threshold matters ("you need at least X for Y"), state it
- Example: "**Nits** = brightness. You need at least ~800 nits to
  read comfortably in direct sunlight. Under 400 is hard to see
  outdoors."

#### Sleekest/lightest/cheapest section

When the user cares about a non-feature dimension (looks, weight,
aesthetics, price), add a focused section ranking products by that
dimension alone, with images and one-line specs. This reframes the
comparison around what the user actually cares about, which may not
be the "best" product on features.

### 6. Interactivity

#### Tooltip system (matrix dots)

Each matrix wrapper (`position:relative`) contains a tooltip div
(`position:absolute`, hidden by default). On `mouseenter` of a
`.dot` group:
- Fill the tooltip from data attributes (name, price, breakdown,
  battery, note)
- Format breakdown and battery as labeled bullet lists
- Position near the hovered dot using SVG coordinate math:
  `cx * (svgRect.width / viewBox.width) + offset`
- Check viewport overflow (left, right, top) and flip position
- Touch support: `touchstart` triggers `mouseenter`, auto-hides
  after 4 seconds
- Reset `nameRe.lastIndex = 0` before any `RegExp.test()` call
  in a TreeWalker filter (the `g` flag advances lastIndex as a
  side effect, causing random misses)

#### Product name hover previews

JS at the bottom of the page:
1. Define a `products` object with every product: `img` (local
   path), `url` (official page), `price`, `breakdown`, `weight`,
   `battery`, `conn` (connection type), `display`, `sdk`, `note`.
   Include short aliases (e.g., "XREAL" for "XREAL One Pro").
2. Create a fixed-position preview card (`#pc`) with image, linked
   name, price, breakdown, stats table, and one-liner.
3. Build a regex from product names (longest first, word boundaries).
4. Walk text nodes with TreeWalker, wrap matches in
   `<span class="pn" data-glass="...">` with dotted underline and
   `cursor:help`.
5. On `mouseover`: populate and position the card. On `mouseout`:
   hide with a 200ms delay. The card itself has `mouseenter` (clear
   hide timer) and `mouseleave` (hide) so the user can hover over
   it and click the product link.
6. `pointerEvents: 'auto'` on the card so links are clickable.
7. Exclude text inside `.dot`, `.cn`, `.gal`, `#pc`, tooltips,
   `script`, `style`, and `svg` from the walk.

#### Image lightbox

A fixed overlay (`#lb`) with a single `<img>`. Gallery images have
`data-full` attributes pointing to the same local file (or a larger
version). Clicking shows the full image. Click or Escape closes.
The lightbox fallback (when no `data-full`): use the `src` as-is.

### 7. Quality checks before pushing

Run these before every push:

- [ ] `grep -c 'https://' index.html` returns 0 (all images local)
- [ ] Every price matches across matrices, cards, tooltips, hover
  data, recommendations, and simulations (search for each price
  string)
- [ ] Every pair of matrix dots has enough spacing (no visual
  overlap)
- [ ] Every product card name is a hyperlink to the official page
- [ ] Heading counts match content ("Three" heading above three
  items, not five)
- [ ] Feature checklists are honest (partial is not yes)
- [ ] Battery numbers show real-world usage prominently, marketing
  claim in parentheses
- [ ] All-in prices include required accessories
- [ ] Simulations start with "What is this?" context
- [ ] The glossary defines every term used in the feature checklists
- [ ] The page renders with JavaScript disabled (matrices and cards
  still readable; interactivity is enhancement)

### 8. Cold read

After the first complete version, **always** run a cold-read review.
Launch a general-purpose agent with instructions to read the full
HTML file as a newcomer to the product category. Ask it to flag:
- Price contradictions between sections
- Matrix dot overlaps
- Unexplained jargon
- Missing "What is this?" context in simulations
- Heading/count mismatches
- JS bugs (regex lastIndex, tooltip positioning, unclamped values)
- Claims that differ from specs in the cards
- Anything confusing for someone who has never looked at this
  product category

Fix every finding before reporting the artifact as ready. The cold
read catches what the author cannot see.

### 9. Iterate with the user

The first push is a starting point. The comparison grows with the
conversation:
- User asks for more brands/models -> add brand deep dives
- User asks "but can I actually use it for X?" -> add reality check
- User converges on 2 options -> add finalists head-to-head
- User decides -> update the page to reflect the decision and note
  what tipped it, for the team's reference

Each iteration: edit the checkout, push, one-line chat summary of
what changed.

### 10. Adapt features to the product category

The feature checklist and simulation details must match the category:

- **Wearables:** weight, battery, rain-safe, comfort over hours,
  "does it look dumb"
- **Kitchen appliances:** noise level (dB), footprint, heat-up time,
  cleaning effort, drink quality
- **Electronics/computers:** performance, thermals, ports, weight,
  battery, repairability
- **Furniture/fixtures:** dimensions, weight capacity, noise (motors),
  materials, assembly
- **Vehicles:** range, charging, cargo, drive feel, total cost of
  ownership

The matrices, glossary, and simulations adapt too. A noise-vs-price
matrix for espresso machines is the same pattern as a weight-vs-battery
matrix for glasses. The skill is the structure, not the content.

For the "three approaches" pattern, always name them with plain,
memorable labels. "Quiet by Engineering" / "Quiet by Design" /
"Brief & Loud" is the right caliber. Not "Category A" / "Category B".

### 11. Common failure modes to avoid

These broke trust or confused readers in real sessions:

- **Price listed differently in two places.** The #1 trust killer.
  Search for each price string before pushing.
- **Battery/noise/performance headline number is the marketing
  claim, not the real-world number.** Always lead with the reviewer
  measurement. Put the manufacturer claim in parentheses.
- **Heading says "Three" but the section has five items.** Match
  counts exactly.
- **Matrix dots overlap.** Check distance > sum of radii + buffer.
- **Product appears in one matrix but nowhere else.** Either include
  it fully or remove it from all charts.
- **Jargon used in feature checklists but not in glossary.** Every
  term in a checklist must be in the glossary.
- **"You built a custom app" in a morning simulation.** Custom dev
  work happened beforehand, not that morning.
- **Regex lastIndex bug.** When using a `g`-flag regex in a
  TreeWalker `acceptNode`, reset `lastIndex = 0` before `test()`.

## Boundaries

- The artifact is the deliverable. Chat replies after each push are
  brief summaries (what changed, what the page now shows).
- Facts come from research, never from memory. Every spec is sourced.
- Be honest. If a product is bad for the use case, say so plainly.
  The user is spending real money.
- Do not recommend a single winner unless one product genuinely
  dominates every dimension. Frame as trade-offs and approaches.
- Download images locally. Never external URLs in HTML.
- Grain is the destination. `grain_new` + `grain_push` or
  `grain_artifact`. Docs folder unless told otherwise.
- Do the writing yourself. Do not delegate to a subagent. You need
  to see the full page to know if it reads well.
