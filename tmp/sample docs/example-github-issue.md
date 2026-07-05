# Example GitHub Issue (issue-form style)

This example shows the **issue-form** structure: a set of labeled, ordered fields where each field asks for exactly one thing an implementer needs. The YAML form definition is shown first (what lives in `.github/ISSUE_TEMPLATE/bug_report.yml`), followed by a filled-in example of the resulting issue.

## Form definition — `.github/ISSUE_TEMPLATE/bug_report.yml`

```yaml
name: Bug Report
description: Report a defect so we can reproduce and fix it
title: "[Bug]: "
labels: ["bug", "triage"]
body:
  - type: markdown
    attributes:
      value: |
        Thanks for filing a bug. Please fill in each field — a complete
        report is the fastest path to a fix. Do not include secrets or
        full request bodies.

  - type: textarea
    id: summary
    attributes:
      label: Summary
      description: What is broken, in one or two sentences?
    validations:
      required: true

  - type: textarea
    id: repro
    attributes:
      label: Steps to reproduce
      description: Numbered steps starting from a known state, with exact inputs.
      placeholder: |
        1. ...
        2. ...
        3. ...
    validations:
      required: true

  - type: textarea
    id: expected-actual
    attributes:
      label: Expected vs. actual
      description: What should happen, and what actually happens (observed, not assumed cause).
    validations:
      required: true

  - type: input
    id: version
    attributes:
      label: Version / build
      description: Service version, commit, or build number.
    validations:
      required: true

  - type: dropdown
    id: severity
    attributes:
      label: Severity
      options:
        - "Critical — data loss / outage"
        - "High — major function broken, no workaround"
        - "Medium — function broken, workaround exists"
        - "Low — minor / cosmetic"
    validations:
      required: true

  - type: textarea
    id: evidence
    attributes:
      label: Logs / screenshots
      description: Paste relevant logs (redacted) or attach screenshots.
    validations:
      required: false

  - type: checkboxes
    id: checks
    attributes:
      label: Pre-submission checks
      options:
        - label: I searched existing issues for a duplicate
          required: true
        - label: I can reproduce this on the latest version
          required: true
```

And the chooser config — `.github/ISSUE_TEMPLATE/config.yml`:

```yaml
blank_issues_enabled: false
contact_links:
  - name: Security disclosure
    url: https://example.com/security
    about: Please report vulnerabilities privately, not as a public issue.
```

## Resulting filled-in issue

> **[Bug]: Delivery status API returns 500 when an endpoint has zero attempts**
>
> **Summary**
> `GET /v1/deliveries/{id}` returns HTTP 500 for deliveries that are still `pending` and have no `delivery_attempts` rows yet. It should return the delivery with an empty attempts list.
>
> **Steps to reproduce**
> 1. Emit an event so a fresh `delivery` row is created (`status = pending`, no attempts yet).
> 2. Immediately call `GET /v1/deliveries/{that_id}` before the first attempt runs.
> 3. Observe the response.
>
> **Expected vs. actual**
> Expected: `200` with the delivery object and `"attempts": []`.
> Actual: `500 Internal Server Error`; the serializer throws when the attempts relation is null.
>
> **Version / build:** `webhook-api` v2.4.1 (commit `a1b2c3d`)
>
> **Severity:** High — major function broken, no workaround
>
> **Logs / screenshots**
> ```
> TypeError: Cannot read properties of null (reading 'map')
>     at serializeDelivery (api/serializers/delivery.ts:41)
> ```
>
> **Pre-submission checks:** ☑ searched duplicates · ☑ reproduced on latest

---

## Why this format works

Issue **forms** beat free-text because the structure does the reporter's thinking for them — every field maps to a question the implementer would otherwise have to chase down.

- **Each field asks for exactly one thing** (summary, repro, expected/actual, version, severity, evidence), and required-field validation makes it impossible to submit a report missing the load-bearing parts. This is GitHub issue forms' core advantage: "ask only for the information a specific type of issue actually needs."
- **The dropdown for severity** normalizes triage into a fixed vocabulary instead of ad-hoc adjectives.
- **`blank_issues_enabled: false` + a chooser** forces reporters into structure and routes security reports to a private channel rather than a public issue.
- **Pre-submission checkboxes** cheaply cut duplicate and stale-version noise.
- The filled example shows the payoff: a report this structured is immediately actionable — an implementer can reproduce and locate it (`delivery.ts:41`) without a single round-trip for clarification.
