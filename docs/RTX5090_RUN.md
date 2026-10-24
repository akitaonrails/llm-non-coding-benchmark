# RTX 5090 pilot — 2026-10-23

## Completed retry — October 24

`results/rtx5090-flash-next-reserved-subset-20261024` completed all three cases.
Execution verification passed: 3 cases, 10 required artifacts, 11 provenance
records and 786 frozen files. Correctness remains ungraded.

| Case | Active minutes | Reported output tokens |
|---|---:|---:|
| BRLAW-01 | 25.12 | 245,468 |
| BRACC-01 | 11.38 | 112,976 |
| USACC-03 | 9.84 | 100,638 |

Pilot wall time: 52.57 minutes; active time: 46.33 minutes; controller waits:
6.22 minutes. The 54 periodic VRAM samples have a minimum of **3,522 MiB free**.
The independent 0.5-second guard reported no reserve breach. Automatic cleanup
stopped the owned benchmark server after completion, leaving about 28 GiB free;
the old personal Strata session was not restarted. Full server, pilot and cleanup
journals were exported to `results/rtx5090-setup-20261024`.

This closes the Flash-Next matched three-case pilot, not the entire seven-model
desktop roster. Strix's legal-first queue continues independently.

## Retry history — October 24

The reserved three-case pilot ended with **zero completed cases**. The model
endpoint disappeared during the first case; all three results are retained as
infrastructure failures in `results/rtx5090-flash-next-reserved-subset-20261023`.
The exact server shutdown cause is unconfirmed: no matching OOM/core evidence
was found, and the guard's terminal output was not retained. Do not attribute
the shutdown to the reserve guard without evidence.

A newer personal Strata session started at 05:13 UTC on October 23, after the
benchmark server disappeared. The controller initially asked unnecessary repeat
permission, then resumed under the user's existing authorization to stop Strata.
That session was stopped on October 24 at approximately 06:07 UTC; no desktop
apps or personal configuration were changed. The guarded retry server runs in
`noncoding-rtx5090-server-20261024.service`, with configuration and engine log in
`results/rtx5090-setup-20261024`. Fresh admission precedes measured cases.
The guard's stdout/stderr and service exit status are now retained in the user
journal. B300's pilot has completed; the independent Strix legal queue is active.

Fresh admission passed in `results/preflight-rtx5090-flash-next-reserved-20261024`.
Warm 1,024-token probe: 190.94 tokens/sec; 3,698 MiB free VRAM after admission.
The fresh three-case run is `results/rtx5090-flash-next-reserved-subset-20261024`,
unit `noncoding-rtx5090-pilot-20261024.service`. Both server and runner retain
service journals and have no automatic restart policy. Periodic headroom samples
are saved in `results/rtx5090-setup-20261024/vram-samples.jsonl`; the guard checks
more frequently (every 0.5 seconds) and stops its own server on a reserve breach.
`noncoding-rtx5090-cleanup-20261024.service` watches that exact pilot unit and
stops only `noncoding-rtx5090-server-20261024.service` when the pilot exits,
whether successfully or with a failure. It does not stop unrelated processes.

## Mandatory desktop safety

All RTX 5090 tests must leave at least 3 GiB VRAM headroom for Hyprland and other
applications. Configure a 4 GiB reserve (`--vram-reserve-mib 4096` in Strata),
launch through `scripts/guard_gpu_reserve.py`, and verify free VRAM under load.
The guard checks every 0.5 seconds and stops only its owned server process group
on a reserve breach or telemetry failure. This is reactive protection, not an
OS-level memory reservation: unrelated apps can allocate between samples.
Never stop desktop applications to make a model fit. Reduce the model allocation
or skip a configuration if the reserve cannot be maintained.

The original unreserved pilot was interrupted and must not be counted as a
completed result. Its initial speed probe does not characterize the reserved run.

Reserved configuration admission passed (tool/write/read/resume, cap, isolation).
Warm decode probe: 170.97 tokens/sec. Observed free VRAM after load and checks:
3568–3722 MiB. Three guard tests cover refusal before launch, runtime reserve
breach, and telemetry failure, with termination limited to the owned group.
Failed measured pilot: `results/rtx5090-flash-next-reserved-subset-20261023`.

User released the desktop GPU and explicitly authorized stopping its existing
Strata session. The original wrapper (2680556) restarted its engine after TERM;
the wrapper was killed and its replacement engine (2719794) terminated. No model
files or personal configuration were removed. Other desktop processes remain.

Flash-Next IQ3_S starts first, using installed weights and a separate configuration
at `config/rtx5090_flash_next.json`, loopback port 18082, 65,536 context, INT8 KV,
32K resident KV, expert offload, MTP4 and the serving engine's default routing.
The engine explicitly reports default route-tail skipping; this is not identical
to B300 NVFP4 serving or full-resident Strix serving.

Verification owner: campaign controller. Require live token-cap, network isolation,
tool/write/read/resume and usage-accounting admission before measured cases.
Then run BRLAW-01, BRACC-01 and USACC-03, with the unchanged scripted-client
protocol. Verify frozen input hashes and required artifacts afterward; correctness
grading remains separate. B300 proceeds independently, not on this GPU.

Warm 1024-token speed probe: 205.83 output tokens/sec (first: 183.18).
This short decode probe is not an engagement-speed prediction. The desktop pilot
threshold was 40 tokens/sec; B300's default remains 100. Probe unit tests pass.
Admission passed at `results/preflight-rtx5090-flash-next-20261023`.
The original unreserved three-case pilot was interrupted at
`results/rtx5090-flash-next-subset-20261023`; this is historical setup evidence.
Server log: `results/rtx5090-setup-20261023/flash-next.engine.log`.
Local API charge is zero; electricity and controller cost are unmeasured.
