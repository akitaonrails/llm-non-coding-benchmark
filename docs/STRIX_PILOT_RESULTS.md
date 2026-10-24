# Strix legal-first pilot results

Execution coverage and timing only. Correctness is ungraded. This covers nine
configurations on the shared legal case; Flash-Next additionally ran the two
accounting cases. It does not complete the full core or numeric matrix.

Completed on October 24, 2026. Six of nine legal engagements completed and
passed execution verification; Ornith Q8 and Qwen Q8 timed out in initial work,
and Qwen Q4 timed out in final review. Flash-Next's two accounting engagements
also completed and verified: **8/11 completed engagements** in total.
The supervisor reached `complete` and exited successfully. Its journal and
frozen source/configuration are retained under
`results/strix-legal-queue-20261024`. All benchmark Ollama aliases were unloaded;
the existing embedding model and shared llama-swap service were preserved.

| Configuration | Active min | Output tokens | Outcome | Evidence |
|---|---:|---:|---|---|
| Flash-Next IQ3_S | 17.73 | 43,545 | completed_ungraded; execution verified | [Run](../results/strix-flash-next-iq3s-numeric-20261022/REPORT.md) |
| Ornith 1.5 Q8 | 120.00 | 238,877 | s1-work turn timeout | [Run](../results/strix-ornith15-q8-legal-20261022/REPORT.md) |
| Qwen3.8 27B Q4 | 194.38 | 112,009 | review turn timeout | [Run](../results/strix-qwen38-q4-legal-20261024-r2/REPORT.md) |
| Qwen3.8 27B Q8 | 120.00 | 50,476 | s1-work turn timeout | [Run](../results/strix-qwen38-q8-20261024-queue-legal/REPORT.md) |
| Swift 1.5 27B Q4 | 141.62 | 78,199 | completed_ungraded; execution verified | [Run](../results/strix-swift15-q4-20261024-queue-legal/REPORT.md) |
| Swift 1.5 27B Q8 | 114.72 | 47,364 | completed_ungraded; execution verified | [Run](../results/strix-swift15-q8-20261024-queue-legal/REPORT.md) |
| ThinkingCap 3.8 Q4 | 117.33 | 69,132 | completed_ungraded; execution verified | [Run](../results/strix-thinkingcap38-q4-20261024-queue-legal/REPORT.md) |
| Muse Glimmer Q8 | 128.03 | 55,763 | completed_ungraded; execution verified | [Run](../results/strix-muse-glimmer-q8-20261024-queue-legal/REPORT.md) |
| GLM 4.7 Flash Q8 | 32.30 | 32,267 | completed_ungraded; execution verified | [Run](../results/strix-glm47-flash-q8-20261024-queue-legal/REPORT.md) |

Active time sums model turns and excludes controller waits. Timeouts retain
drafts and pre-review evidence but have no completed final snapshot. Raw
`infrastructure_failed` includes harness turn timeouts; this label alone does
not establish a serving crash. Interrupted setup/retry attempts remain in
their original directories and are excluded from this table.

The resumed Ollama runs used 0.40.10, versus 0.40.8 earlier. Serving stack,
quantization, output volume and agent behavior differ across configurations.
One observed run per configuration does not establish a speed or quality ranking.

Local API charge is zero. Electricity, hardware and controller costs were not
measured. Admission probes and controller time are separate from active case time.

## Remaining gate

Grade correctness and adjudicate the documented fixture defects before choosing
models for broader case coverage. Preserve this campaign unchanged; any fixture
correction belongs to a versioned follow-up run.
