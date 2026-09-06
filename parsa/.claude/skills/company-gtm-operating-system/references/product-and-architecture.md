# Product And Architecture

### 5. Define Product Thesis And Workflow

Translate market research into product principles.

Capture:

- primary user workflow
- MVP wedge
- supported formats/surfaces
- review/approval needs
- auditability needs
- data model concepts
- product quality metrics
- what not to build yet
- public claims to avoid

**Success criteria**: A product brief exists with workflow, ICP, MVP direction, technical direction, and product capabilities that matter.

### 6. Define Domain Experiment Docs

Create a standard schema for each domain experiment.

Recommended files per domain:

```text
docs/<domain-slug>/
  README.md
  one-pager.md
  analogies.md
  angle.md
  seo-gtm.md
  product-surface.md
  experiments.md
```

Each domain should capture:

- ICP
- thesis
- voice
- keywords
- CTA
- product surface
- analogies
- page strategy
- experiments
- success metrics

**Success criteria**: Every domain has a routed folder with the same schema and clearly distinct positioning.

### 7. Define Architecture Foundations

Capture the technical operating model without prematurely overbuilding.

Include:

- target repo structure
- app/library boundaries
- frontend strategy
- docs strategy
- API/worker split
- data schemas to define later
- compute/model providers
- storage and queue assumptions
- portability boundaries
- Docker/container direction
- infra-as-code direction
- deployment constraints
- cost/egress guardrails

For provider-heavy products, define adapter boundaries and benchmark criteria.

**Success criteria**: Architecture docs explain how the company can build the first product without locking itself into fragile provider assumptions.

### 8. Define GTM Ops And Vendor Stack

Capture the operational stack needed to test demand.

Include:

- Google Search Console
- Bing Webmaster Tools
- analytics, usually PostHog
- support/chat, such as Crisp
- docs framework, such as Nextra
- docs path strategy, usually `/docs`
- billing, usually Stripe
- transactional email, such as Resend
- error tracking, such as Sentry
- database
- queue
- object storage
- DNS/CDN/WAF
- observability
- conversion events
- setup order

**Success criteria**: GTM ops and vendor assumptions are documented with open decisions separated from defaults.
