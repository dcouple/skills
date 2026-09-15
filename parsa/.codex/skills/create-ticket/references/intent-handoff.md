# Preserve intent at ticket handoff

Read when capturing a discussion as a ticket. Keep the reason the work exists, not only the requested task. A short ticket may compress the following, but should not drop the source-grounded motivation.

## Complete source → concise ticket

Fictional source: “Accountants reconcile every refund manually because our CSV shows it as a positive sale. Keep all rows; show negative refunds. Export only, no invoice rewrites. Missing amounts should be blank.” A proposal to omit refunds was explicitly rejected.

**Intent:** Accountants should receive a complete ledger they can reconcile without correcting refund signs by hand (discussion D-17). Preserve all rows and normal sales; changing saved invoices is out of scope.

**Scope:** Format refund amounts as negative in the export and explain that convention in the export help. Preserve missing amounts as empty cells.

**Acceptance criteria:** A 1,250-cent refund exports as `-12.50`, including when its stored sign is already negative; a normal 1,250-cent sale remains `12.50`; a missing amount is blank; saved invoices are unchanged.

**Decisions and sources:** Omitting refunds was rejected because the ledger must remain complete. D-17 is the available discussion record; do not invent a public URL if none exists.

The ticket explains a checkable outcome without prescribing an unrequested file-by-file implementation. Examples and constraints are source-backed; additional implementation proposals must be labeled as proposals.

## Incomplete source → explicit gap

Source: “Make refund exports negative.”

**Intent:** Requested outcome: negative amounts for exported refunds. The originating problem and reason for prioritizing this change were not supplied.

**Inputs Needed:** Who is affected and what workflow prompted this request? Does it affect exports only? Clarify only the unanswered decisions that matter to scope; preserve known facts while waiting.

Do not borrow the accountant story, invoice constraint or empty-cell rule from the example above. Missing motivation is a gap to capture, not permission to invent impact. Distinguish the user's decisions from your assumptions and preserve available discussion/artifact references so the plan and PR can recover the why.
