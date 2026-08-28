---
name: hillclimb
description: Sustained improvement of one named metric toward a target — measure a baseline, then loop hypothesis, implement, re-measure, accept or revert. Use for perf, bundle size, lint count, or test time. A one-off fix is /investigate; this is the loop.
argument-hint: "[metric and target, e.g. 'cold start under 400ms']"
---

# Hillclimb

One change, one measurement, keep or revert. Never stack untested changes,
and never claim a win from reading the diff. No measurement, no claim.

## Set up

1. Name one metric and the direction that counts as better. One, not three.
2. Name the target that ends the run.
3. Write the measurement as one repeatable command, sampled past the noise (a
   median of N runs, not one). Freeze it; a changed method voids every earlier number.
4. Record the baseline and a green run of the checks that must keep passing.

## Loop

Take the live hypothesis with the biggest expected win. Each names a mechanism
("defer X off the boot path; it blocks first paint"), not "try memoizing".

- Implement it alone; re-measure with the frozen method; run the checks.
- Accept only when the metric moves past the noise and the checks stay green.
  Otherwise revert it in full; a tweak that might help does not ride along.
- One commit per accepted win, named with the before and after numbers.
- Log every attempt, kept or reverted, so the search accumulates.
- Stop at the target, or after three consecutive hypotheses with no accepted
  win. Don't relax the target to declare victory.

## Throughput — parallelize by default

Every iteration, ask: is this work throughput-bound, and is it parallelizable?
If both, wall-clock per unit of work is the one exception to "one metric":
climb it alongside the primary. Sequential over N items is a bug when N > ~20;
the bar is a model lab's — every core, as many instances as limits allow. (Why:
a crawl did 863 domains one at a time — 2.8% done in 20 min, one crash killed it.)

- Per-item time first, then a target wall-clock; prove the rate on a 50-item dry run.
- I/O-bound → asyncio + httpx.AsyncClient/aiohttp, one global semaphore (64, then
  128–256 within host and rate limits) plus per-host caps. CPU-bound →
  ProcessPoolExecutor at os.cpu_count(). Mixed → async front, process pool back.
  Beyond one machine → say so; ray/dask, never hand-rolled.
- Every item idempotent and checkpointed (a result file or row); one item's
  crash never escapes the loop; the run resumes, never restarts.
- Bulk pre-filters before expensive work: dedupe, DNS pre-resolve, HEAD before GET.
- A progress line every N items — rate, ETA, success %, error classes — to a
  log the orchestrator can read without a screen.
- Paid or rate-limited calls: the provider's published limits and a hard spend
  cap bound concurrency; back off only on transient errors.

The toolkit, not a mandate — the canonical I/O-bound shape:
```python
sem = asyncio.Semaphore(64)                       # global cap; per-host caps live in the client
async def one(item, client):
    if (out := DONE / f"{item.id}.json").exists(): return   # idempotent → resume, never restart
    async with sem:
        try: out.write_text(json.dumps(await fetch(client, item)))
        except Exception as e: (ERR / f"{item.id}.txt").write_text(f"{type(e).__name__}: {e}")  # never escapes
async def main(items):
    async with httpx.AsyncClient(timeout=10) as client:
        for i, t in enumerate(asyncio.as_completed([one(x, client) for x in items]), 1):
            await t
            if i % 50 == 0: log(f"{i}/{len(items)} {i/elapsed():.1f}/s eta={eta(i)}s ok={ok_pct()}% errs={error_classes()}")
```

## Report

A table of attempts — hypothesis, before, after, verdict — then the accepted
wins and what each rejected hypothesis ruled out.
