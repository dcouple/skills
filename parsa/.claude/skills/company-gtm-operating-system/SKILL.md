---
name: company-gtm-operating-system
description: Turn a company or product idea into researched market, product, go-to-market, and technical foundation documents.
argument-hint: "[idea, audience, competitors, domains, repo, or constraints]"
---

# Company foundations

## Inputs and rules

- Start from the idea, audience, constraints, existing research, and any supplied repository or domain choices.
- Separate evidence, hypotheses, settled decisions, and open questions.
- Preserve user corrections and non-goals; do not infer permission to buy domains, create vendor accounts, publish, or deploy.
- Verify current competitor, pricing, domain, and vendor claims; avoid unsupported public security/compliance promises.

## Research and decide

1. Frame the need: what painful job, for whom, who pays, and why now?
2. Map the category using relevant competitors, pricing, docs, sitemaps, and buyer language.
3. Assess demand and channels. For search-led products, distinguish buyer intent from curiosity and map keyword clusters to useful pages.
4. Evaluate naming/domains where relevant: memorability, audience fit, availability, and distinct experiments. Avoid duplicate sites without a canonical/redirect strategy.
5. Define the product thesis: primary workflow, initial scope, approval/audit needs, quality metrics, and what not to build yet.
6. Outline technical foundations proportional to the product: boundaries, data, integrations, deployment, cost, portability, and operational risks.
7. Select operational capabilities before vendors: analytics, support, documentation, billing, messaging, and observability as needed. Named tools are options to evaluate, not defaults to impose.

## Build a navigable knowledge base

- Use the supplied destination and existing documentation conventions; otherwise start with `docs/README.md` and focused linked documents.
- Separate market/product decisions from technical details while linking their dependencies.
- Create only documents that carry useful decisions or evidence. Example layout:

```text
docs/README.md
docs/product-brief.md
docs/market-and-competitors.md
docs/gtm-strategy.md
docs/technical-foundations.md
docs/decisions-and-next-steps.md
```

- If domain experiments are in scope, record each one's audience, thesis, voice, channels, CTA, and success metric in a consistent small template.
- For developer products, assess which API, SDK, CLI, integration, or documentation surfaces users actually need; do not require every interface.

## Review and hand off

- Check that sources, tradeoffs, user constraints, and open decisions survived the synthesis.
- Remove redundant docs and unsupported claims; verify navigation links.
- Return the index, key decisions, remaining uncertainties, and the next useful step.
- Commit/push only when requested, to the authorized branch, preserving unrelated work.

## Grain handoff

- If connected, read/update every research and foundation artifact in the supplied task folder, or `Development Artifacts/YYYY-MM-DD-<task>`; pass the rule to helpers and sync their outputs.
- Keep requested repository docs and needed local copies in place, preserve privacy limits, and continue locally silently without Grain.
