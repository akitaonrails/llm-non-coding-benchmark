# Single-B300 campaign — 2026-10-23

User authorized configuring and running pod `8xf2fy90y9pfjg` for this suite.
This replaces the four-GPU shortlist, not the unfinished Strix campaign.
Strix is idle: Flash-Next completed three ungraded engagements; Ornith Q8
timed out after two hours; seven configurations have admission only.

## Priority queue

1. GLM 5.3 Flash NVFP4 — `RedHatAI/GLM-5.3-Flash-NVFP4`.
2. Qwen3.8 Flash-Next NVFP4 — `nvidia/Qwen3.8-Flash-Next-NVFP4`.
3. Swift 1.5 27B BF16 — `ukisai/Swift-1.5-Qwen3.8-27b`.
4. ThinkingCap 3.8 27B BF16 — `bottlecapai/ThinkingCap-Qwen3.8-27B`.

Selection uses the previous coding campaign's single-B300 results (92.5,
92.5, 88.0, 83.0 respectively), not assumed legal/accounting quality.
DeepSeek V4.1 Flash FP8 (~510 GB) is excluded from this single-GPU plan.
Qwen3.5 397B's tight fit and lower previous result do not justify prioritizing
it over these four. MiniMax is not retained without a validated single-GPU
configuration. Kimi remains excluded by the user's earlier decision.

## Execution and verification

Controller owns all evidence checks. Run one model at a time, TP=1; pin weight
revisions and record installed packages and launch arguments. Preserve default
reasoning. Use the existing networkless OpenCode harness, 64K agent context,
16,384-token per-response cap, and the same frozen fixtures/client protocol.
Admission requires enforced output cap, actual tool write/read, session resume,
complete provider accounting, and a warm decode probe >=100 tokens/sec.
Do not conflate per-response limits with total agent-turn budgets.

First run BRLAW-01, BRACC-01, USACC-03 on each admitted model, matching Flash's
measured Strix subset. Broader 16-case coverage follows only after assessing
this pilot's completion and runtime. Execution verification is not accuracy
grading. Failed or timed-out attempts remain in the record.

Record setup, loading, active inference, controller wait, and total pod elapsed
time separately. API charge is zero but pod rental is not; the current hourly
rate has not been supplied. Do not reuse the previous pod's rate as a bill.
Stop owned inference processes when done; stopping a process does not stop
RunPod billing. No RTX 5090 or unrelated Strix service is touched.

## Observed infrastructure

One NVIDIA B300 SXM6 AC, 275,040 MiB VRAM, initially unused. Driver 595.91.07.
The supplied SSH proxy requires an interactive PTY and ignores remote commands.
Direct SSH to the same verified container works via its advertised port.
Model API will bind loopback and use SSH transport, not a public unauthenticated
endpoint. `/workspace` is currently on the container overlay, NOT a separately
mounted persistent volume: export all evidence locally and do not promise
weights survive pod replacement. About 2 TB space is available.

Initial runtime install: separate `/workspace/noncoding-venv`, vLLM 0.32.0.
No existing system Python environment is overwritten.

Initial GLM startup was interrupted to correct the venv PATH. The next failed
because pip selected nvcc/CRT/NVVM 13.4 alongside runtime headers 13.0. Pinned
these three compiler packages to 13.0.88 (no compatibility-check bypass), set
CUDA_HOME to the wheel toolkit, and added missing lib64/libcudart linker aliases
inside that isolated venv. Launch metadata and server logs retain each attempt.
ThinkingCap is gated: the existing local HF token demonstrated access to the
pinned config and was transmitted only via SSH stdin to the downloader's env;
no token file or account-permission change was made on the pod.

## Live state

All four pinned weight downloads completed. GLM became ready around 03:29 UTC
after first-use compilation/autotuning. Warm probe: 148.45 output tokens/sec,
above the 100-token/sec gate. Tool write/read/resume, eight-token output cap,
network isolation, and provider accounting all passed in
`results/preflight-b300-glm53-flash-20261023`.
The measured three-case GLM run completed in
`results/b300-glm53-flash-subset-20261023`: 25.80 minutes wall, 24.10 active,
1.68 controller wait. Execution verification passed (3 cases, 10 required
artifacts, 8 provenance contexts, 786 frozen files). Active case minutes:
BRLAW 7.39; BRACC 8.43; USACC 8.28. GLM was stopped after the run; Flash-Next
NVFP4 is next. No hidden facts were released because GLM wrote no client
question files; this is observed behavior, not a quality endorsement.
Setup evidence is retained in `results/b300-setup-20261023`.
No correctness score is implied by these checks.

GLM BRLAW-01 completed ungraded: 443.69 active seconds, 485.08 elapsed seconds,
41.00 controller-wait seconds, 3 turns, 53,384 output tokens including 32,715
provider-reported reasoning tokens.
This vLLM response configuration does not report cached-input detail; the
harness's zero cached-input field must not be interpreted as proof of no cache
hits. Prefix caching is enabled in the recorded launch arguments.

Flash-Next startup completed around 04:01 UTC. Its pinned checkpoint is 123.57
GiB on disk; vLLM defaults to an FP8 PLE embedding table in pinned CPU memory
(Engram cpu_offload=True), with 75.18 GiB model load on GPU. This is explicitly
not an all-weights-on-GPU configuration. Warm decode probe passed at 194.30
tokens/sec; retain the admitted serving default rather than adding an unneeded
placement-tuning restart. The attention implementation falls back from FA4 to
FA2 for its selected head/cache-block geometry; preserved in server logs.
All admission checks passed in `results/preflight-b300-flash-next-20261023`;
the measured run completed in `results/b300-flash-next-subset-20261023`.
Execution verification passed: 3 cases, 10 required artifacts, 9 provenance
contexts, 786 frozen files. Wall 21.98 minutes; active 18.59; controller wait
3.38. Active case minutes: legal 3.05, BR accounting 7.88, US tax 7.66.
Only the April pro-labore fact was requested/released in BRACC; its later
question-file revisions explicitly archived unknowns and received no extra
client turns. Flash-Next was stopped; Swift 1.5 BF16 is next.

Swift 1.5 BF16/MTP3 became ready around 04:27 UTC. Warm decode passed at
200.27 tokens/sec; all tool/read/write/resume/isolation/accounting checks passed
in `results/preflight-b300-swift15-20261023`. Its matched three-case run is
completed in `results/b300-swift15-subset-20261023`.
Execution verification passed: 3 cases, 10 artifacts, 9 contexts, 786 frozen
files. Active time 13.56 minutes; controller waits 29.57 minutes; wall 43.15
minutes. Controller delay is not model inference time. Swift was left loaded
idle after completion; this was an orchestration failure, not ongoing work.

Resumed 2026-10-24 00:46 UTC: Swift stopped and ThinkingCap BF16/MTP3 launched
from its previously pinned complete download. Admission passed at 204.77 warm
output tokens/sec. All 12 attempts are finished: 11 completed ungraded;
ThinkingCap US tax failed during final-review compaction at the 64K context
ceiling. Final logs were copied locally and the server stopped.
See `B300_PILOT_RESULTS.md` for timing, failure evidence and cost caveats.
