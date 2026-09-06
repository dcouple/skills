# Working on Skills

`parsa/` contains the active Claude, Codex, business, and SEO workflows.
`tyler/` is a frozen ancestor; Orchestra's canonical source is dcouple/orchestra.
Edit active sources here, preserving harness-specific tools and invocation
metadata. Shared variants that are identical should remain identical.

## Authoring and completion

Keep descriptions concise and discriminating. Put conditional detail in linked
references with a read condition. Preserve output formats, caller names,
explicit authorization boundaries, and the evidence that determines readiness.
Load only the affected skills, callers, and relevant supporting material.

For implementation requests, continue through scoped changes, checks, fixes,
and the requested PR. Local branches, worktrees, and disposable verification
fixtures are part of that work. Existing authorization persists across routine
stage boundaries; planning-only requests and explicit review pauses still stop
before implementation. Merge, release, deployment, production/destructive
changes, and external posting require their own matching authorization.

Validate changed metadata, local reference links, and install/sync behavior.
Run scripts only against disposable fixtures for this audit, not the user's
installed skills or consumer repositories. Reuse passing results while inputs
remain unchanged. Read back pushes and PR state before reporting success.

Keep `./tmp/` scratch and unrelated changes out of commits. Discover repository
commands and target environments instead of hardcoding a consumer's stack.
Do not use em dashes in new instructions or PR prose.
