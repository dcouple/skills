# Panel Control

## Dispatch And Observe RunPane

Use event-driven waits, not static sleeps. Before every prompt, capture an output
cursor/hash and timestamp. Put the exact prompt in a file, then use the current
CLI's file-input command and composer helper, for example:

```bash
runpane panels input --panel <panel-id> --input-file <prompt-file> --yes --json
runpane panels submit-composer --panel <panel-id> --strategy auto --yes --json
```

Do not mark the stage started until the submit result says
`verifiedSubmitted:true` and a later observation proves either an activity
transition or output delta after the baseline. Idle-without-output, composer text
still present, or `verifiedSubmitted:false` is not success.

When JSON returns `blocked`, `suggestedCommand`, or `nextCommand`, treat it as
structured guidance, never shell source. Allowlist only the expected `runpane
panels` wait/screen/output/submit/submit-composer subcommand and flags; verify the
panel id belongs to the workstream being driven and any choice matches the
blocker; reconstruct an argv call. Reject unknown commands. Never use `eval`,
`sh -c`, or interpolate the returned string. Repeat submit/start verification
after clearing a blocker.

### Verify Delivery

A submit success field means bytes reached a terminal, not that an agent
received a turn. Confirm the instruction appears as a received turn in the
agent's durable session record — the session log the agent's harness keeps on
disk, where it keeps one — or observe an activity transition or output delta
against the baseline. No lifecycle state advances without one.

Unconfirmed is not undelivered. An agent finishing an earlier turn can hold a
received prompt while showing no delta, so resending on absent evidence runs it
twice. Prove non-delivery before any resend: prompt text still in the composer,
or the panel idle over a bounded wait with the screen showing no queued or
running turn. Never resend an instruction carrying an external mutation without
that proof; a double run is unrecoverable. When neither delivery nor
non-delivery can be proven within the wait, escalate to the user instead of
resending.

### Clear Interstitials Before Treating A Panel As Ready

A new panel may come up on an interstitial that accepts keystrokes but blocks
the composer: an update prompt, a resume-or-summarize prompt, a model or profile
picker, a trust confirmation. Detect it from the panel's screen before the first
prompt, clear a routine one — update, resume, model picker — with the
workstream's configured choice, then re-check readiness. A trust or permission
confirmation is not routine: record it as a blocker for the user. A readiness failure does not mean creation failed; reconcile against
the live panel list before creating anything.

### Record Held Input

Record every deliberate hold locally with its reason and release condition.
Capture composer content you did not place before overwriting or clearing it.
