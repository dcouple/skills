# Rubric — data / schema migration

1. **[blocker]** Dry run executed on production-like data (in a transaction
   where the engine allows). Evidence: dry-run output.
2. **[blocker]** Pre/post row counts for every touched table. Evidence: the
   counts, quoted.
3. **[blocker]** At least one domain-invariant query passes post-migration
   (e.g. "zero rows where orders.customer_id IS NULL"). Evidence: query +
   result.
4. **[blocker]** Rollback path exists and was executed once against the
   dry-run state. Evidence: rollback output.
5. Expand→migrate→contract phasing: destructive steps (drop/rename) are a
   later phase, not bundled with the expand step.
6. Lock safety considered for large tables (concurrent-safe index creation,
   batched updates). Evidence: the statement used.

Known failure modes: migration passes on empty dev DB and locks production;
`down` never tested; old code writes to the old column mid-deploy; invariant
held by application code only, nothing at the schema level.
