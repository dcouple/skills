---
name: page-review
description: "Review and improve a draft or live content page. Use when the user wants cleanup for usefulness, voice, E-E-A-T, intent match, answer quality, promotional risk, self-promotion fairness, comparison/listicle integrity, proof gaps, CTA placement, or a ship/revise/do-not-ship publishing judgment."
---

# Page Review

Use this skill after a draft or live page exists. The job is to judge whether the page actually satisfies the reader before it tries to convert them.

Core rule: a page should still be useful if every CTA and product promo block is removed. If removing promotion reveals a thin or distorted answer, recommend revision before shipping.

## Inputs To Gather

- Draft text, live URL, exported HTML, or page outline.
- Target query/keyword and intended audience.
- Product or offer being promoted.
- Page goal and funnel stage.
- Competitors or SERP examples if available.
- Any known constraints: claims, compliance, brand voice, required CTAs, or proof assets.

If the target query is missing, infer the likely query from title/H1/body and flag uncertainty.

## Workflow

1. Identify the promised answer and the searcher job.
2. Score usefulness, intent fit, voice, E-E-A-T/proof, freshness, time to value, CTA risk, and answer distortion. Load `references/page-review-rubric.md`.
3. Check whether self-promotion follows the same rules applied to competitors. Load `references/self-promotion-fairness.md` for comparisons, listicles, alternatives pages, and roundup content.
4. Clean up voice: specificity, firsthand judgment, tradeoffs, stale claims, generic phrasing, and fake neutrality. Load `references/editorial-voice.md`.
5. Calibrate against examples. Load `references/good-vs-bad-examples.md` when reviewing listicles, comparisons, product-led informational pages, or pages with heavy CTAs.
6. Produce a publish decision and concrete rewrite priorities.

## Output Format

Return:

- Recommendation: `ship`, `revise`, or `do not ship`
- Scorecard
- Highest-risk issues
- Section-by-section fixes
- Voice cleanup notes
- Missing proof/E-E-A-T
- Product-promotion cuts or repositioning
- Comparison/listicle fairness fixes, if relevant
- Final publish checklist

Prefer direct edits or replacement snippets when the user supplied text. Keep critique actionable and avoid generic SEO advice.

## Handoffs

- Use `$page-strategy` when the page premise, target query, or structure needs to be rethought before editing.
- Use `$site-content-audit` when the issue appears across many URLs or a whole section/template.
