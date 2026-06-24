# SEO Skills

Skills for content quality, readability, and search authority.

**Important**: These skills should be run with **Claude Opus 4.6** (`claude-opus-4-6`), which performs significantly better than 4.7 or 4.8 at copywriting and writing in specific voice styles. Do not use newer models for SEO copy work.

## Skills

- **content-readability-pass**: Audit and rewrite website copy for voice consistency, readability, and first-timer comprehension.
- **content-authority-pass**: Add E-E-A-T signals: explainer pages, glossary, author attribution, structured data, OG images, and SEO metadata.

## Workflow

Run readability first, then authority. The readability pass produces a list of concepts needing explainer pages, which the authority pass consumes.

```
/content-readability-pass   # audit, voice guide, rewrite, humanity pass
/content-authority-pass     # explainers, glossary, author, schema, OG images
```
