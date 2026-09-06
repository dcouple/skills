# External Integrations

## External Integrations

For payment, email, SMS, analytics, and other third-party integrations:

- Confirm the account/project/mode before running tests.
- Prefer test-mode objects and fake/test cards.
- Prefer recipient/provider-side evidence over send-side success. A 200 response from the app or provider is useful but not enough when the PR's behavior depends on actual delivery, ingestion, webhook receipt, or downstream processing.
- Use plus-addresses, reserved fake phone numbers, sandbox identities, metadata, notes, UTM values, or request IDs so every external artifact can be found without ambiguity.
- Respect production stop boundaries. Do not bypass MFA, consume one-time tokens, send real calls/SMS, create paid subscriptions, charge cards, or mutate customer data unless the user explicitly approved that production action.
- Check for duplicate listeners before starting a new webhook listener.
- Record IDs that let the user or future agent find the test again: email, phone number, org key, customer ID, subscription ID, message ID, webhook event type, dashboard URL, event marker, or screenshot path.
- If a provider key lacks read scopes, try another non-destructive readback source such as a connected mailbox, recipient-side tool, provider dashboard export, app database row, webhook table, logs, or analytics event. Report the scope limitation rather than treating it as product failure.
- Never expose secrets in the final answer. Public analytics tokens are not the same as private API keys, but still describe them carefully.

## Browser-Extension and Vendor Interference

- Password-manager extensions (1Password) steal focus into extension frames on
  credential-like fields; afterwards ALL automation on the tab fails with
  "Cannot access a chrome-extension:// URL". Prefer setting form values by element
  reference over click+type, dismiss popovers by clicking neutral page areas (Escape may
  feed the popover), and recover a wedged tab only by opening a fresh one (hosted
  checkout URLs resume by URL).
- Export GIF recordings BEFORE closing their tab — recordings die with the tab group.
- Vendor sandboxes rate-limit (e.g. Dropbox Sign test API throttles after ~6 signature
  requests/day, stalling embeds ~10 min). Budget signature-heavy passes and report
  throttling as an environment limit, not a product bug.
