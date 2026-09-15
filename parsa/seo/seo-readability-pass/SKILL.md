---
name: seo-readability-pass
description: Audit or improve website copy for clear language, audience comprehension, and voice while protecting meaning and established search intent.
---

# Readability pass

Work on the requested pages. An audit returns findings; a rewrite changes only the authorized scope.

## Establish context

- Read existing voice guidance and representative pages. If absent, infer a few provisional traits; do not rewrite repository-wide agent instructions to install a voice guide.
- Identify the audience. Expert documentation can use precise terms that a beginner page needs to explain.
- Use `good-writing-fundamentals` for focused edits and `seo-writing-framework` for substantial new passages.

## Audit

- Read each scoped page, including headings, examples, and surrounding context.
- Flag confusing terms, tangled sentences, repeated setup, unsupported claims, and tone mismatches with excerpts and locations.
- Rank pages as **needs work**, **minor issues**, or **fine**; explain the effect on readers.
- Preserve useful bullets, natural blank lines, links, code blocks, and interactive components.

## Match the edit to the risk

- Follow project-specific SEO protections and approval requirements.
- Treat high-value, high-traffic, regulated, and conversion-critical pages cautiously: propose targeted before/after edits and obtain required approval.
- Use available query/performance data to protect established intent and accurate terminology. Do not retain a false claim merely because it ranks.
- Missing analytics is uncertainty, not evidence that a page is low-risk. Do not require a full data pull for a small copy fix.
- Low-risk or new pages can receive broader edits within the approved scope. Numeric traffic tiers, if used, should come from the project.

## Rewrite and check

- Keep the same facts with clearer wording. Explain necessary jargon rather than banning it.
- Use active voice when it clarifies the actor; keep passive voice where appropriate.
- Match the actual brand voice, not a mandatory founder persona or casual tone.
- Identify concepts needing an inline definition or dedicated explainer; hand that list to `seo-authority-pass` if useful.
- Run relevant project checks, such as content linting, link checks, build, or a rendered-page inspection. Review the final diff for lost keywords, meaning, and components.

## Handoff and artifacts

- Report changed pages, remaining risks, validation, and any approval needed. Commit, push, and prepare a PR only when authorized by the request or parent workflow.
- If Grain is connected, save audits, term lists, before/after notes, and reviews in the shared task folder; pass its ID/storage rule downstream. Source changes stay in project files, with review artifacts shared. Otherwise continue normally; keep sensitive material private.
