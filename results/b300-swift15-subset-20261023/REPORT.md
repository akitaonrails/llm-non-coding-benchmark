# swift-1.5-27b — RunPod 1xB300; BF16 MTP3 diagnostic run

Execution and timing only; task correctness is not graded.

- Harness: opencode 2.1.2; 1 worker.
- Wall time: 43.15 minutes.
- Active agent time: 13.56 minutes.
- Controller waits: 29.57 minutes.
- API charge: $0. Electricity, hardware and pod rental cost: not included.
- Different agent harness from Sol; not a model-only controlled comparison.

| Case | Agent min | Turns | Input tokens | Cached input | Output tokens | Status |
|---|---:|---:|---:|---:|---:|---|
| brlaw_01_prazos_processuais | 4.34 | 3 | 1,006,330 | 0 | 49,270 | completed_ungraded |
| bracc_01_das_fator_r | 4.81 | 3 | 1,238,730 | 0 | 54,555 | completed_ungraded |
| usacc_03_household_1040 | 4.42 | 3 | 682,864 | 0 | 52,062 | completed_ungraded |

Input includes cached input. Output/reasoning accounting is limited to provider-reported fields.
Provider request logs include background title generation and are retained per case.
