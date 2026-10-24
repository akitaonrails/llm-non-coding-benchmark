# qwen3.8-flash-next — RunPod 1xB300; default CPU PLE table diagnostic run

Execution and timing only; task correctness is not graded.

- Harness: opencode 2.1.2; 1 worker.
- Wall time: 21.98 minutes.
- Active agent time: 18.59 minutes.
- Controller waits: 3.38 minutes.
- API charge: $0. Electricity, hardware and pod rental cost: not included.
- Different agent harness from Sol; not a model-only controlled comparison.

| Case | Agent min | Turns | Input tokens | Cached input | Output tokens | Status |
|---|---:|---:|---:|---:|---:|---|
| brlaw_01_prazos_processuais | 3.05 | 3 | 518,854 | 0 | 30,879 | completed_ungraded |
| bracc_01_das_fator_r | 7.88 | 3 | 1,496,044 | 0 | 82,452 | completed_ungraded |
| usacc_03_household_1040 | 7.66 | 3 | 1,170,031 | 0 | 80,974 | completed_ungraded |

Input includes cached input. Output/reasoning accounting is limited to provider-reported fields.
Cached-input detail is not reported by this vLLM response configuration; zeros
do not establish zero cache hits. PLE embeddings use the default pinned CPU
placement. This is not an all-weights-on-GPU run or a hardware-only comparison
with Strix's IQ3_S/Strata configuration. Correctness remains ungraded.
Provider request logs include background title generation and are retained per case.
