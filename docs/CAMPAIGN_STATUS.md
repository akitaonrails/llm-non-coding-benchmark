# Campaign status

**Superseded by the active full-suite campaign:** see [FULL_SUITE_CAMPAIGN.md](FULL_SUITE_CAMPAIGN.md)
and [live coverage](../results/full-suite-coverage-20261024.json). The snapshot
below records the earlier pilots only.

Snapshot: 2026-10-24 15:50 UTC. Execution coverage is separate from correctness.
The live Strix queue state is `results/strix-legal-queue-20261024/status.json`;
this document is a snapshot, not a heartbeat.

| Lane | Execution coverage | Remaining work |
|---|---|---|
| Sol 6 medium | 16 core cases completed, execution verified | Correctness grading and fixture adjudication |
| Single B300 | Four models × three attempts finished: 11 completed, one output-limit failure | Correctness grading; actual rental rate/bill unknown |
| Strix Halo | Nine legal configurations attempted: six completed and verified, three turn timeouts; Flash-Next also completed two accounting cases (8/11 engagements completed) | Correctness grading and fixture adjudication; full numeric/core expansion not run |
| RTX 5090 | Flash-Next guarded three-case pilot completed and execution verified; benchmark server stopped | Correctness grading; other desktop roster models have not been run in this campaign |

The B300 inference server and owned tunnel were stopped after logs were saved
locally. This does not stop the RunPod pod or its billing. See
[B300_PILOT_RESULTS.md](B300_PILOT_RESULTS.md) for per-model timings and the
ThinkingCap final-review failure.

## Shared legal case: completed or terminated attempts

| Hardware / model | Active minutes | Reported output tokens | Execution outcome |
|---|---:|---:|---|
| Sol 6 medium / Codex | 2.47 | 8,445 | Completed, ungraded |
| B300 / GLM 5.3 Flash NVFP4 | 7.39 | 53,384 | Completed, ungraded |
| B300 / Flash-Next NVFP4 | 3.05 | 30,879 | Completed, ungraded |
| B300 / Swift 1.5 BF16 MTP3 | 4.34 | 49,270 | Completed, ungraded |
| B300 / ThinkingCap 3.8 BF16 MTP3 | 3.83 | 44,333 | Completed, ungraded |
| Strix / Flash-Next IQ3_S | 17.73 | 43,545 | Completed, ungraded |
| Strix / Ornith 1.5 Q8 | 120.00 | 238,877 | Initial-turn timeout; no completed deliverable |
| Strix / Qwen3.8 27B Q4 | 194.38 | 112,009 | Final-review timeout; drafts preserved, no completed final snapshot |
| Strix / Qwen3.8 27B Q8 | 120.00 | 50,476 | Initial-turn timeout; no completed final snapshot |
| Strix / Swift 1.5 27B Q4 | 141.62 | 78,199 | Completed, ungraded; execution verified |
| Strix / Swift 1.5 27B Q8 | 114.72 | 47,364 | Completed, ungraded; execution verified |
| Strix / ThinkingCap 3.8 Q4 | 117.33 | 69,132 | Completed, ungraded; execution verified |
| Strix / Muse Glimmer Q8 | 128.03 | 55,763 | Completed, ungraded; execution verified |
| Strix / GLM 4.7 Flash Q8 | 32.30 | 32,267 | Completed, ungraded; execution verified |
| RTX 5090 / Flash-Next IQ3_S, reserved | 25.12 | 245,468 | Completed, ungraded; execution verified |

Source: each corresponding case's `result.json`. Active minutes exclude
controller waits. Different harnesses, serving stacks, quantizations and output
lengths prevent interpreting these as model-only speed or quality rankings.
Failed/interrupted attempts remain in their original directories and are not
silently replaced by retries. Local API charge is zero; electricity, controller
cost and rental charges are not included.

## Pilot execution complete

The Strix supervisor finished with stage `complete` and exited successfully.
All seven resumed attempts were archived; together with the earlier Flash-Next
and Ornith runs, all nine legal configurations have an outcome. See
[STRIX_PILOT_RESULTS.md](STRIX_PILOT_RESULTS.md) and the matched-case
[PILOT_TIMING_COMPARISON.md](PILOT_TIMING_COMPARISON.md).

The next gate is correctness grading and fixture adjudication before selecting
models for expanded coverage. Preserve this campaign's inputs/results; corrected
fixtures require a versioned follow-up run. The full numeric/core matrix and the
remaining desktop model roster have not been executed.

Every future 5090 benchmark must preserve at least 3 GiB free VRAM, use the
reserve guard and retain durable server logs. See [RTX5090_RUN.md](RTX5090_RUN.md).

## Final resource check

The Strix queue and RTX 5090 server/pilot/cleanup units are inactive with successful
unit results. Ollama on Strix retains only the pre-existing embedding model;
the shared llama-swap service was preserved. The final desktop check showed
28,642 MiB free VRAM. The guarded pilot's minimum sampled free VRAM was 3,522 MiB,
above the required 3,072 MiB floor. B300 server/tunnel cleanup was previously
verified; pod shutdown and billing cessation are not confirmed.
