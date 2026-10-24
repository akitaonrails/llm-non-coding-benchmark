# glm-5.3-flash — RunPod 1xB300 diagnostic run

Execution and timing only; task correctness is not graded.

- Harness: opencode 2.1.2; 1 worker.
- Wall time: 25.80 minutes.
- Active agent time: 24.10 minutes.
- Controller waits: 1.68 minutes.
- API charge: $0. Electricity, hardware and pod rental cost: not included.
- Different agent harness from Sol; not a model-only controlled comparison.

| Case | Agent min | Turns | Input tokens | Cached input | Output tokens | Status |
|---|---:|---:|---:|---:|---:|---|
| brlaw_01_prazos_processuais | 7.39 | 3 | 1,205,784 | 0 | 53,384 | completed_ungraded |
| bracc_01_das_fator_r | 8.43 | 2 | 1,179,751 | 0 | 63,740 | completed_ungraded |
| usacc_03_household_1040 | 8.28 | 3 | 1,229,340 | 0 | 61,927 | completed_ungraded |

Input includes cached input. Output/reasoning accounting is limited to provider-reported fields.
Cached-input details are absent from this vLLM response configuration: zeros in
that column mean unreported, not proof of zero cache hits. Prefix caching was
enabled; server logs independently show cache hits. No client-question files
were written, so no hidden facts were released. Runtime alone cannot establish
quality equivalence with the other candidates.
Provider request logs include background title generation and are retained per case.
