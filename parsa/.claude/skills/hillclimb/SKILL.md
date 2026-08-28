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
the bar is a model lab's — every core, as many instances as limits allow.

- Per-item time first, then a target wall-clock; prove the rate on a 50-item dry run.
- I/O-bound → asyncio plus a bounded worker queue (64, then 128–256 within
  resource and rate limits). CPU-bound →
  ProcessPoolExecutor at os.cpu_count(). Mixed → async front, process pool back.
  Beyond one machine → say so; ray/dask, never hand-rolled.
- Enforce real keyed caps for each scarce resource — host, provider, API key,
  database partition — and evict idle keys. A comment is not a limiter.
- Stream input through O(concurrency) resident tasks. Never create one task per
  item; that fails before a million-item run starts.
- Every item idempotent and checkpointed with an atomic commit (temp file plus
  rename, or one database transaction). One item's crash and its error logging
  never escape the worker; the run resumes, never restarts.
- Bulk cheap pre-filters before expensive work: dedupe and validate first; for
  HTTP, DNS pre-resolve and HEAD before GET when they actually save work.
- A progress line every N items — rate, ETA, success %, error classes — to a
  log the orchestrator can read without a screen.
- Paid or rate-limited calls: the provider's published limits and a hard spend
  cap bound concurrency; back off only on transient errors.

The toolkit, not a mandate — the generic I/O-bound shape (`cap_for` is a real
keyed, idle-evicting limiter; `items` is a stream):
```python
STOP = object()
async def one(item):
    try:
        if (out := DONE / f"{item.id}.json").exists(): return
        async with cap_for(item.resource_key):
            result = await run(item)
        tmp = out.with_suffix(".tmp")
        tmp.write_text(json.dumps(result)); tmp.replace(out)  # atomic, same filesystem
    except Exception as exc:
        with contextlib.suppress(Exception): record_error(item, exc)
async def worker(queue):
    while (item := await queue.get()) is not STOP:
        try: await one(item)
        finally: queue.task_done()
    queue.task_done()
async def main(items, concurrency=64):
    queue = asyncio.Queue(maxsize=2 * concurrency)
    workers = [asyncio.create_task(worker(queue)) for _ in range(concurrency)]
    for item in items: await queue.put(item)
    for _ in workers: await queue.put(STOP)
    await queue.join(); await asyncio.gather(*workers)
```

## Report

A table of attempts — hypothesis, before, after (metric and wall-clock),
verdict — then the accepted wins and what each rejected hypothesis ruled out.
