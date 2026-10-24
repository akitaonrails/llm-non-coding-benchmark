# Single-B300 matched pilot results

All 12 planned attempts finished: **11 completed ungraded, 1 output-limit
failure**. These are execution and timing results, not quality scores.
Cases: BRLAW-01, BRACC-01, USACC-03; one run each, serial execution.

| Model / format | Completed | Active minutes | Controller wait minutes | Run wall minutes |
|---|---:|---:|---:|---:|
| GLM 5.3 Flash NVFP4 | 3/3 | 24.10 | 1.68 | 25.80 |
| Qwen3.8 Flash-Next NVFP4 | 3/3 | 18.59 | 3.38 | 21.98 |
| Swift 1.5 27B BF16 MTP3 | 3/3 | 13.56 | 29.57 | 43.15 |
| ThinkingCap 3.8 27B BF16 MTP3 | 2/3 | 12.84* | 2.48 | 15.34 |

*ThinkingCap includes time on the failed US tax case, not three completions.
Legal and BR accounting completed in 3.83 and 4.60 active minutes respectively.

ThinkingCap US tax final review failed with OpenCode `compaction.failed`:
"Compaction summary reached the output token limit". The last provider response
used 62,504 prompt plus 3,032 completion tokens, reaching the 65,536 context
ceiling. The harness records `candidate_output_limit`; budgets and fixtures
were unchanged. Drafts and pre-review snapshots remain, but the engagement did
not complete. Aggregate verification correctly fails; its missing-final-artifact
errors refer to the absent final snapshot, not to absent draft files.

GLM, Flash-Next and Swift each pass execution verification: 3 cases, 10 required
artifacts, 786 frozen files. ThinkingCap has two completed cases and one failed.

## Cost and comparison limits

- API charge is zero; **pod rental is not included and is not zero**. Actual rate
  remains unknown. Billing includes setup, controller delays and idle time.
- Swift was left loaded idle after finishing; ThinkingCap started only on
  2026-10-24 00:46 UTC. This orchestration failure is not model work. The table
  excludes between-run idle time and cannot represent the entire pod bill.
- Controller waits are excluded from active time. Controller model cost is
  unrecorded. Final benchmark server was stopped after logs were copied locally;
  stopping vLLM does not terminate the RunPod pod or its charges.
- vLLM cached-input fields are unreported, not evidence of no cache hits.
- Flash-Next uses a CPU-offloaded FP8 PLE table, not entirely GPU-resident weights.
- Sol uses a different agent harness and four workers. Compare matched cases,
  not its full-suite wall time with a serial three-case pilot.
- Known synthetic fixture defects remain unchanged; independent correctness
  grading is still pending. No quality tier is assigned.

Evidence: `results/b300-glm53-flash-subset-20261023`,
`results/b300-flash-next-subset-20261023`,
`results/b300-swift15-subset-20261023`,
`results/b300-thinkingcap38-subset-20261024`, and
`results/b300-setup-20261023`.
