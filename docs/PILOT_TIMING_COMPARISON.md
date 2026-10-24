# Matched three-case timing comparison

All entries below completed BRLAW-01, BRACC-01 and USACC-03 and passed execution
verification. **Correctness is ungraded.** These are single observed runs, not
averages or quality-adjusted speed rankings. Sources are the case `result.json`
files in the run directories listed below.

## Active time, minutes

| Model / hardware | BR legal | BR accounting | US tax | Sum |
|---|---:|---:|---:|---:|
| Sol 6 medium / Codex | 2.47 | 4.54 | 3.67 | 10.68 |
| Flash-Next NVFP4 / single B300 | 3.05 | 7.88 | 7.66 | 18.59 |
| Flash-Next IQ3_S / RTX 5090, reserved | 25.12 | 11.38 | 9.84 | 46.33 |
| Flash-Next IQ3_S / Strix Halo | 17.73 | 96.59 | 43.35 | 157.68 |

Sums use unrounded seconds. Active time excludes controller waits and includes
candidate reasoning, tool work, client-response revisions, scripted pushback
and fixed final review. Sol's three cases were part of a concurrent 16-case run;
their summed active time is not a separate three-case wall-time measurement.

## Reported output tokens

| Model / hardware | BR legal | BR accounting | US tax |
|---|---:|---:|---:|
| Sol 6 medium / Codex | 8,445 | 18,479 | 13,662 |
| Flash-Next NVFP4 / single B300 | 30,879 | 82,452 | 80,974 |
| Flash-Next IQ3_S / RTX 5090, reserved | 245,468 | 112,976 | 100,638 |
| Flash-Next IQ3_S / Strix Halo | 43,545 | 224,945 | 102,165 |

The 5090 legal engagement took longer than the Strix engagement despite faster
decoding, while producing far more output. This illustrates why a short decode
probe cannot predict engagement runtime. It does not establish the cause of
the output-length difference or which answer is better.

## Limits and cost

- Open-weight runs use OpenCode 2.1.2, 64K context and a 16,384-token response
  cap; Sol uses Codex with medium reasoning. Local providers retain their
  default reasoning behavior. Harness and reasoning differences remain.
- B300 uses NVFP4 and vLLM, including Flash-Next's CPU-offloaded FP8 PLE table.
  Strix uses resident experts; the 5090 uses expert offload, MTP4 and its
  default route-tail skipping. These are distinct serving configurations.
- The 5090 was configured with a 4GiB reserve and guarded at 3GiB. Its 54
  periodic samples bottomed at 3,522MiB free; the faster guard reported no
  breach. Its benchmark server stopped automatically after the pilot.
- Provider output/cache counters have different reporting capabilities.
  Unreported reasoning or cache counters must not be interpreted as zero use.
- Local API charge is zero, but electricity, hardware and controller cost are
  unmeasured. B300 rental is additional and the actual rate remains unknown;
  its full bill includes setup and substantial earlier orchestration idle time.
- Sol's full 16-case baseline has a $5.3239 API-equivalent estimate, not a
  subscription invoice and not the cost of only these three cases.
- Failed/interrupted attempts are preserved separately. Known fixture defects
  remain unchanged and require adjudication before correctness scoring.

Evidence:

- `results/sol6-medium-core-20261022-r2`
- `results/b300-flash-next-subset-20261023`
- `results/rtx5090-flash-next-reserved-subset-20261024`
- `results/strix-flash-next-iq3s-numeric-20261022`

See [B300_PILOT_RESULTS.md](B300_PILOT_RESULTS.md) for the other three B300
models and [CAMPAIGN_STATUS.md](CAMPAIGN_STATUS.md) for the continuing Strix queue.
