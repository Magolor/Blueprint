---
name: template-pr-bench
description: Read when an efficiency-related pull request needs benchmark evidence.
---

# Benchmark evidence

## Summary

Required for efficiency-related PRs, including performance, memory, resource,
or cost improvements. Include a GitHub Markdown comparison table in the body,
then link the full benchmark report and raw measurements. Name baseline and
candidate revisions, workload, units, environment, commands, repetitions,
warm-up/cache conditions, and variability in the report; summarize the key
conditions here. Compare equivalent work and verify correctness separately.

## Compare results

The following numbers are illustrative, not measurements to reuse:

| Metric / workload | Better | Before | After | Change | Assessment |
| --- | --- | ---: | ---: | ---: | --- |
| Median latency / fixed batch | Lower | 100 ms | 80 ms | -20% | 🟢 Improved |
| Throughput / fixed batch | Higher | 100 ops/s | 120 ops/s | +20% | 🟢 Improved |
| Peak memory / fixed batch | Lower | 100 MiB | 110 MiB | +10% | 🔴 Regressed |

Compute change as `(after - before) / before × 100%`; when the baseline is zero,
report an absolute change and mark the percentage unavailable. Interpret the
sign against the metric's desired direction. Use 🟢 Improved, 🔴 Regressed,
⚪ No clear change, and ⚪ Not measured with text labels; color is not the only
signal. Use plain table cells and colored markers rather than custom HTML/CSS.
Report variability and explain regressions, tradeoffs, or inconclusive results;
do not select only favorable workloads. Mark missing measurements explicitly
and keep claims provisional until evidence exists or an explicit waiver is given.

Color expresses direction, not statistical significance. For benchmark tooling without a comparable predecessor, include a representative measured run and mark unavailable baseline cells explicitly. Do not invent a speedup.

