# Strix Halo diagnostic campaign — 2026-10-22

## Resumed 2026-10-24

Earlier Ornith Q8 legal run ended at its two-hour initial-turn timeout, not a
completed engagement. Flash-Next's three cases remain the only completed Strix
pilot from Oct 22. The seven remaining configurations were not measured then.

Ollama now reports 0.40.10 (previously 0.40.8), bound to 192.168.0.90:11434,
not loopback. Qwen27 Q4 passed fresh cap/isolation/tool/write/read/resume admission
at `results/preflight-strix-qwen38-q4-20261024`. Its first resumed legal attempt,
`results/strix-qwen38-q4-legal-20261024`, was interrupted as described below. Existing nomic embedding service remains
untouched. Continue legal-first coverage before expanding numeric cases, per the
latency-driven campaign order below. Record the server upgrade as a comparison
limitation, not an identical runtime rerun.

The first resumed Qwen Q4 attempt ended with unexplained SIGTERM (exit 143),
before its own two-hour timeout. It is retained as interrupted infrastructure
evidence, not a candidate score. A fresh admission passed after unloading only
the owned alias. Retry: `results/strix-qwen38-q4-legal-20261024-r2`, running as
transient user service `noncoding-strix-qwen38-q4-20261024-r2.service`.
The service retains journal and exit information and is independent of terminal
session lifetime; its outer safety limit is eight hours, while candidate turns
retain their original two-hour limit. No automatic restart/retry loop is enabled.

Queue advancement now runs independently in transient user service
`noncoding-strix-legal-queue-20261024.service`, configured by
`config/strix_legal_queue.json`. Live state and the frozen supervisor source are
in `results/strix-legal-queue-20261024`. It attaches to the current Qwen Q4 case,
then runs fresh admission and one legal engagement for each remaining model,
serially. It unloads only its own Ollama aliases and never the embedding model or
the entire llama-swap service. Infrastructure/admission failures stop the queue
for diagnosis; candidate output limits and confirmed turn timeouts are retained
as failed attempts rather than automatically retried.

The supervisor automates only the exact `citacao.prazo_em_dobro` boolean branch,
after checking all three required files are nonempty and JSON is valid. Missing,
malformed, unexpected or out-of-workspace artifacts require review, as do every
client question and nudge decision. Decisions never overwrite existing reviews.
Nine focused tests cover this behavior; all 23 project tests pass. This does not
change candidate prompts, model settings, cases, or the two-hour turn limit.
Queue-level safety limit is 48 hours, with no automatic restart policy.

Qwen Q4 retry ended at 04:48 UTC on October 24: initial work completed in
55.50 minutes, pushback in 18.88 minutes, but final review reached its 120-minute
turn timeout (return code -9). Total active time 194.38 minutes; reported output
112,009 tokens. Raw status is `infrastructure_failed`; the confirmed cause is
the turn timeout, not a server crash. Drafts and pre-review snapshots remain,
but no completed final snapshot exists, so execution verification fails.
The supervisor advanced automatically to fresh Qwen Q8 admission.

Qwen Q8 passed admission, then its initial legal turn hit the two-hour timeout
at approximately 06:49 UTC (return code -9), with 50,476 reported output tokens.
The first long response reached the 16,384-token response cap; OpenCode continued
under the same turn budget. No completed engagement/final snapshot exists.
The queue preserved the failed attempt and advanced to Swift Q4, whose fresh
admission passed and measured legal case started.

Swift Q4 completed ungraded and passed execution verification (one case, three
required artifacts, three provenance records, 786 frozen files). Initial turn:
53.10 minutes; pushback: 14.64; final review: 73.87; total active: 141.62 minutes.
Reported output: 78,199 tokens. Controller wait was one second; the supervisor
handled the exact scripted boolean branch without a missing-deliverable nudge.
The queue advanced to Swift Q8 admission. Intermediate chat updates briefly
misidentified final review as the initial turn; the turn logs and these totals
are authoritative, and the monitor now reads the active prompt and completed
turn records explicitly. Candidate execution was unaffected.

Swift Q8 completed all three turns and passed execution verification: 114.72
active minutes, 114.76 wall minutes, 47,364 reported output tokens. Its initial
turn took 62.41 minutes and pushback 23.47 minutes. Correctness remains ungraded.
The supervisor advanced to ThinkingCap Q4 admission automatically.

ThinkingCap Q4 completed all three turns and passed execution verification:
117.33 active minutes, 117.36 wall minutes, 69,132 output tokens. Initial work
took 44.20 minutes and pushback 14.82 minutes. The supervisor advanced to Muse
Glimmer Q8 admission. Correctness remains ungraded.

Muse Glimmer Q8 completed all three turns and passed execution verification:
128.03 active minutes, 128.05 wall minutes, 55,763 output tokens. Initial work
took 104.95 minutes and pushback 5.43 minutes. The supervisor advanced to the
final configuration, GLM 4.7 Flash Q8, for admission. Correctness is ungraded.

GLM 4.7 Flash Q8 completed and passed execution verification: 32.30 active
minutes, 34.24 wall minutes, 32,267 output tokens. Initial work: 3.63 minutes;
pushback: 9.16; final review: 19.51. Two question-file checkpoints contained
analysis archives with no actual client questions, so no facts were released.
The queue reached `complete` and its service exited successfully. All nine
legal configurations now have preserved outcomes: six completed, three turn
timeouts. Including Flash-Next's accounting cases, eight of eleven engagements
completed. See [STRIX_PILOT_RESULTS.md](STRIX_PILOT_RESULTS.md).

The initial Oct 22 scope used only `192.168.0.90` while the desktop GPU was
unavailable. The user subsequently authorized parallel RTX 5090 testing and
stopping Strata, with at least 3 GiB VRAM reserved. That guarded three-case
Flash-Next pilot is now complete; see [RTX5090_RUN.md](RTX5090_RUN.md).
The remaining queue described here still targets only Strix.

## Verification plan

Owner: campaign controller. Before collecting case results:

- Prove candidate host paths are absent and direct internet connections fail.
- Verify the gateway refuses arbitrary routes, other model IDs and remote images.
- Run a live tool/write/read/resume probe against each selected serving configuration.
- Record actual model ID, quantization/inventory, harness version, wall time and
  token counters. Preserve failed probes separately from valid runs.
- Check frozen pack hashes and deliverable presence after each core suite.

The new runner uses OpenCode 2.1.2, a fresh private home per case, and Bubblewrap
`--unshare-all`. A Unix-socket gateway exposes only the selected model's chat
endpoint and a fixed model listing. It does not mount personal configuration,
credentials, answer keys, other cases or future session documents. Candidate
shell commands share the networkless namespace. Only the gateway can contact
the explicitly configured remote host. Read-only runner configuration sits
outside the candidate's writable home.

The scripted-client and conditional-pushback controller is shared with the Sol
baseline. Answers remain verbatim. Core packs are unchanged despite known
fixture issues in the Sol run's OBSERVATIONS.md. Results remain diagnostic and
ungraded. Different harnesses mean this is not an isolated model-only comparison.

## Initial inventory

Ollama has Qwen3.8 27B Q4 and Q8, Swift1.5 27B Q4, and ThinkingCap3.8 27B Q4.
Swift Q8 is not installed. The four aliases reference the same weights as their
Hugging Face aliases; do not benchmark duplicate aliases as different models.
Strata HIP-Halo and Flash-Next IQ3_S weights/pack are installed but need a live
preflight. Ornith35B weights were not found in the inspected Strata directory.
llama-swap also advertises GLM4.7 Flash Q8, the roster's weak control.

Port 8080 on this host is an unrelated application, not a model server. Its
services must not be stopped. Ollama is on 11434; llama-swap on 11435.

## Measurement limits

Local API charge is zero; electricity cost is unknown, not zero. Report inference
request time and engagement wall time separately from controller waits. Token
counters come directly from provider SSE usage events. The first probe exposed
missing final step-finish events in OpenCode's CLI, so those events are only a
fallback and verification rejects a run that needs that fallback. Background
title-generation requests are also counted. Cache and reasoning fields are
only as complete as the local provider reports. Live probe evidence must precede
claims about successful tool use or resume. Initial loading is part of cold
probe timing; subsequent suites normally use warm weights.

Qwen Q4 preflight r2 passed tool/write/read/resume and network isolation. The
initial probe is retained as an invalid accounting preflight, not a candidate
failure. Nine unit tests cover shared-client matching, gateway isolation and
stream forwarding/final-usage preservation.

## Historical campaign state — October 22

Latest: all nine configurations passed tool/write/read/resume admission. The
three-case Flash-Next run completed in `results/strix-flash-next-iq3s-numeric-20261022`.
Execution verification passed: 3 cases, 10 required artifacts, 11 provenance
records, 786 frozen files. Wall time 161.20 minutes; active agent 157.68 minutes;
controller waits 3.50 minutes. USACC-03 took 43.35 active minutes and 102,165 output
tokens. Its five scripted facts were requested and released verbatim; the extra
request for an unavailable prior-year document received only the neutral reply.
The owned Strata scope was stopped. Ornith Q8's legal test was launched in
`results/strix-ornith15-q8-legal-20261022`; it subsequently reached its two-hour
initial-turn timeout. See the resumed state above and the queue's `status.json`
for current progress.
Order: BRLAW-01, BRACC-01, USACC-03. No correctness score is implied by admission.

Flash-Next BRLAW-01 completed ungraded: 1,064.08 active seconds, 1,094.29 elapsed,
30.00 controller-wait seconds, three turns, 651,152 input tokens (599,849 cached),
43,545 output tokens. The matching Sol case took 148.21 active seconds and 8,445
output tokens; different harnesses and ungraded outputs prevent a model-only or
quality conclusion. BRACC-01 also completed ungraded: 5,795.62 active seconds,
5,877.00 elapsed, 81.01 controller-wait seconds, 5,961,141 input tokens
(5,547,795 cached), and 224,945 output tokens. Its initial turn took
808.02 seconds, its client-response revision 1,522.60 seconds, and final review
3,464.99 seconds. For BRACC-01, only
`prolabore_abril` and `estorno` were released. The revised questions explicitly
archived unknowns, so no redundant client turn was sent. Several automatic
compactions and repeated source checks contribute materially to runtime.

After observing the 96.6-minute BRACC engagement, campaign order was adjusted:
finish Flash-Next's current three cases, then run BRLAW-01 on each of the eight
remaining configurations before expanding numeric coverage. This prioritizes a
shared measured engagement across all admitted models; the full 27-engagement
numeric matrix has **not** been completed or silently claimed as complete.

Flash-Next required `--resident-experts` to avoid a duplicate ~47 GiB CPU arena.
Because the user cgroup's memory-controller files are unavailable, the engine
falls back to mmap expert storage; all 24,576 experts still fit the GPU cache.
Available host RAM was ~44 GiB after admission. A temporary watchdog stops only
the owned Strata scope if MemAvailable drops below 8 GiB. Earlier full-arena
attempts were stopped and must not be used as performance measurements.

SSH TCP forwarding is administratively disabled. No SSH/firewall policy was
changed and no LAN port was opened. Flash requests use fixed HTTP operations via
authorized SSH exec, with JSON data on stdin and framed responses on stdout.
The server remains loopback-only. The unused forwarding process was stopped.

Muse's final admitted alias is `noncoding-muse-glimmer-30b-q8-64k-atem:20261022`.
Its autogenerated stop list cut off message headers; the benchmark alias uses
only `<|eot|>`. Automatic title generation is disabled for measured runs using a
fixed OpenCode session title, avoiding asynchronous request-accounting ambiguity.
All earlier failed probes remain as setup evidence, not scored model failures.

- Qwen3.8 27B Q4/Q8: corrected 64K preflights passed.
- Swift1.5 27B Q4/Q8: corrected 64K preflights passed.
- ThinkingCap3.8 27B Q4: corrected 64K preflight passed.
- Ornith1.5 35B Q8: corrected 64K preflight passed using full-resident Ollama.
- Muse Glimmer Q8: corrected `-atem` alias and fixed-title preflight passed.
- Flash-Next IQ3_S: mmap/full-GPU-cache Strata preflight passed.
- GLM4.7 Flash Q8: existing llama-swap configuration preflight passed.

The invalidated dense Qwen Q4 pilot showed about 11–12 decode tokens/sec. Flash-Next
has shown roughly 47–63 decode tokens/sec in early measured requests. The controller asked
whether to prioritize the already-declared three-case Strix subset across models
or extend to full 16-case suites; current work continues pending that preference.
The original roster budgets about one hour per Strix engagement. Do not imply
that a full eight-configuration core matrix is a short run.

Controller default after measuring latency: use `strix_numeric_subset` (BRACC-01,
USACC-03, BRLAW-01) across configurations first. The first measured subset is
running. The extra full-core pilot was **invalidated and stopped**, not scored: its
declared output cap was not enforced. It also overlapped weight downloads. Its
manifest records the intended 16 cases, not completed cases; see its INVALIDATED.md.
The transcript and exported session messages were retained; the private temporary
home was moved to trash. No unrelated inference service was stopped.

The corrected gateway converts `max_completion_tokens` into the upstream
`max_tokens` and caps individual responses at 16,384 tokens. Each admission test
first proves the backend stops after exactly eight requested tokens with reason
`length`. The gateway unit test covers translation and clamping. Actual agent
requests log requested/effective limits. Reaching the cap without completing a
turn is recorded as `candidate_output_limit`, not a transport failure or a
professional correctness verdict.

Swift Q8, Ornith Q8 and Muse Glimmer Q8 (ggml-org) downloads completed, expanding
admission to nine configurations.
The existing llama-server advertises `draft-dflash`, but no speculative-decoding
compatibility or speed claim is made before a live test.

`prepare_strix_models.py` creates **new** dated aliases listed in
`config/strix_models.json`, with 65,536-token server context to match the agent's
limit. It never overwrites existing aliases or modifies the user's source tags.
The pilot used the original 262,144-token server default. New aliases require new
preflights. Reasoning remains provider-default, not disabled for speed.

`config/strix_flash_next.json` passed Strata's plan validation and was staged under
the remote user's `~/.local/state/noncoding-benchmark/`. It uses a separate log,
loopback-only port 18081 and the nonsecret local-test token `local`; it does not
reuse or modify existing service credentials. This original full-arena profile
was superseded by `config/strix_flash_next_resident.json` after memory testing.
