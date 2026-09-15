# Code Review Criteria

## 0. Discover the project's standards

- Read applicable repository instructions, lint/compiler configuration, manifests, and CI.
- Apply only relevant criteria; explain material conflicts with the project's rules.
- Judge observable risk and behavior, not a preferred language, framework, component size, or folder layout.

## 1. Correctness — must fix

- Logic and boundary errors, invalid state transitions, and broken contracts.
- Unhandled failure paths, races, cancellation, retries, and partial side effects.
- Missing runtime wiring: unreachable features, unused outputs, or success reported before the operation succeeds.
- Evidence that required behavior or regression coverage is missing.

## 2. Security — must fix

- Missing authentication, authorization, or tenant/resource isolation.
- Injection paths, unsafe output rendering, or untrusted data treated as instructions.
- Exposed secrets or sensitive data in client code, logs, artifacts, or public uploads.
- Validate against the actual trust boundary; do not require one named sanitizer or error-handling pattern everywhere.

## 3. Architecture and framework use — assess impact

- Clear ownership, coherent boundaries, and reuse of suitable existing patterns.
- Resource lifetimes and cleanup; avoid unnecessary shared state or abstraction.
- Apply framework-specific rules only when that framework is present.
- React examples: valid hook order, correct dependencies and cleanup, stable keys, and explicit loading/error/empty states.
- Recommend memoization, code splitting, or state-management changes only when evidence justifies them.

## 4. Types and contracts — assess impact

- Types accurately represent runtime values and public contracts.
- Unsafe casts or unchecked dynamic values do not conceal a real mismatch.
- Follow project conventions for imports, aliases, interfaces, and naming.
- A TypeScript `any` or assertion needs scrutiny, not an automatic rewrite unrelated to behavior.

## 5. User experience — assess impact

- Is the action discoverable where the user needs it, with understandable feedback?
- Does placement match the information's scope and the product's existing navigation?
- Are loading, failure, empty, permission, and accessibility states handled where relevant?
- Does progressive disclosure reduce clutter without hiding necessary controls?
- Example: item-specific actions usually belong near the item; account-wide settings may belong in an account surface. Verify against the actual product.

## 6. Conventions — suggestions unless project policy says otherwise

- Follow local naming, formatting, logging, and organization conventions.
- Identify in-scope dead code or confusing duplication; avoid unrelated cleanup.
- Do not duplicate findings already explained by a failed automated check.
- Prefer a few evidence-backed findings over a checklist of stylistic preferences.
