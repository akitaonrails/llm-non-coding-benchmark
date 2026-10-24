# thinkingcap-3.8-27b — RunPod 1xB300; BF16 MTP3 diagnostic run

Execution and timing only; task correctness is not graded.

- Harness: opencode 2.1.2; 1 worker.
- Wall time: 15.34 minutes.
- Active agent time: 12.84 minutes.
- Controller waits: 2.48 minutes.
- API charge: $0. Electricity, hardware and pod rental cost: not included.
- Different agent harness from Sol; not a model-only controlled comparison.

| Case | Agent min | Turns | Input tokens | Cached input | Output tokens | Status |
|---|---:|---:|---:|---:|---:|---|
| brlaw_01_prazos_processuais | 3.83 | 3 | 800,728 | 0 | 44,333 | completed_ungraded |
| bracc_01_das_fator_r | 4.60 | 2 | 759,788 | 0 | 56,473 | completed_ungraded |
| usacc_03_household_1040 | 4.41 | 4 | 913,907 | 0 | 50,648 | candidate_output_limit |

Input includes cached input. Output/reasoning accounting is limited to provider-reported fields.
Provider request logs include background title generation and are retained per case.
