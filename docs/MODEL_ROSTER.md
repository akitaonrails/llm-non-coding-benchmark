# Model roster for v1 — who gets tested, where

Selection made 2026-10-21 from the coding benchmark's latest standings
(`llm-coding-benchmark/docs/success_report.v4.combined.md`, `docs/b300-cost-quality-comparison.md`,
`docs/b300-4x-overnight-campaign.md`, `docs/open-weight-serving-capacity.md`). Scores quoted are
the coding v4 "vigilance" score (0–100, tiers A ≥ 83 · B 73–82 · C 51–72 · D ≤ 50) and are
**priors, not predictions** — one purpose of this suite is to find out whether coding rank predicts
accounting/legal usability at all.

## A different token profile than the coding bench — and why it matters for local runs

A v4 coding sprint burned 5–12 M tokens per sprint and ran for hours; a single engagement here is
expected to be **20–150 K tokens** per session (documents in, a deliverable out), with L4 multi-session
cases adding up to maybe 1 M across all sessions. Consequences:

- **The 30 tok/s consumer gate can be relaxed to ~15 tok/s for this suite.** A dense 27B at Q8 on
  the Strix Halo (~8–12 tok/s) was unusable for a 10 M-token coding sprint but is tolerable for a
  40 K-token return — a 1-hour engagement, which is what a human would take anyway. Report actual
  speed; do not hard-fail on it locally.
- **Quantization accuracy becomes a first-class variable.** Arithmetic and table lookup are
  exactly what low-bit quantization degrades. The Strix can hold Q8 of a 27B; the 5090 can only
  hold Q4 with context. Running the **same weights at Q4 (5090) and Q8 (Strix)** on the numeric
  engagements (USACC-1/-3, BRACC-1/-2) is a cheap, novel A/B that the coding benchmark could never
  do. Treat it as a planned comparison, not a footnote.
- **Context is less of a wall.** 64–128 K context is enough for every single-session engagement;
  only the L4 cases need care, and those are multi-session by design.
- The B300 ≥ 100 tok/s admission rule stays as-is (it's about not wasting pod dollars).

## Tier 1 — local, RTX 5090 (32 GB GDDR7, 91 GB RAM)

| Model | Serving | Coding prior | Why it's in |
|---|---|---|---|
| **Qwen 3.8 27B** Q4_K_M | ollama / llama-swap, q8 KV, 128 K | 80.0 B (strix), 80.5 B (B300) | The local baseline everyone else is measured against; also the Q4 arm of the quant A/B |
| **Swift 1.5 27B** Q4_K_M | same | 88.0 A (B300) | Highest-scoring dense model that fits a 5090; Qwen3.8 fine-tune |
| **ThinkingCap 3.8 27B** Q4_K_M | same | 83.0 A (B300) | Second A-tier dense 27B; reasoning-tuned, interesting for legal memos |
| **Ornith 1.5 35B-A3B** Q8 | Strata (expert offload), 128 K — already validated at ~80 tok/s | 81.0 B (B300 BF16) | MoE that runs *fast* on the 5090 at Q8 — the one local config with no quant penalty |
| **Qwen3.8 Flash-Next 125B MoE** IQ3_S | Strata | 92.5 A (B300 NVFP4) | The strongest open model that runs locally at all; the IQ3 quant gap vs. its NVFP4 result is the story |
| **Muse Glimmer 30B** | llama-swap, DFlash spec-decode | 81.0 B | Cheap and very fast; good "is speed the trade-off" datapoint |
| GLM-4.7 Flash (control) | llama-swap | 24.0 C/D | Known-weak floor — keeps the grader honest (it must fail) |

## Tier 2 — local, Strix Halo (64 GB UMA + GTT, 61 GB RAM, 256 GB/s)

| Model | Serving | Why it's in |
|---|---|---|
| **Qwen 3.8 27B** Q8_0 | fresh ollama container, 128 K | Q8 arm of the quant A/B against the 5090's Q4 |
| **Swift 1.5 27B** Q8_0 | same | Same A/B on the strongest dense local model |
| **Qwen3.8 Flash-Next** IQ3_S | Strata `linux-amd-strixhalo` build | Does the AMD build match the NVIDIA one? (serving-stack check) |
| **Ornith 1.5 35B-A3B** Q8 | Strata | MoE on the bandwidth-starved box — expected to be the usable one there |

Dense 27B on the Strix is slow (~8–12 tok/s) but *admissible* under the relaxed gate; the quant A/B
justifies the wall-clock. Skip DeepSeek V4.1 Flash locally — 1-bit only, borderline load, not a
quality-representative run.

## Tier 3 — rented datacenter GPU (B300 if available again; else 4×H200 SXM)

**2026-10-23 override:** the user provisioned **one B300**. The active queue is
GLM 5.3 Flash NVFP4, Qwen3.8 Flash-Next NVFP4, Swift 1.5 27B BF16, and
ThinkingCap 3.8 27B BF16. See [B300_RUN.md](B300_RUN.md) for admission gates,
the matched three-case pilot, and observed pod configuration. The four-GPU
shortlist below is historical, not the current execution plan.

Pod time is $9–36/hr. Kimi K2 is excluded per user decision (2026-10-22). and the previous campaign showed cloud APIs are cheaper for everything that
*has* a cloud API. The justification for renting here is the benchmark's own premise — **private
infrastructure for confidential data** — so the roster is the models a firm would actually
self-host, not everything that exists. Shortlist of **four** for v1, in priority order:

| # | Model | Serving (from the B300 runbook) | Coding prior | Why it's in |
|---|---|---|---|---|
| 1 | **DeepSeek V4.1 Flash** FP8 (`-1017`) | vLLM TP=4, ~510 GB | 92.5 A (self-hosted), 92.5 cloud | Top self-hosted result; same weights ran on both B300 and H200 so the hardware comparison is already calibrated |
| 2 | **GLM 5.3 Flash** NVFP4 (B300) / FP8 (H200) | vLLM, glm47 parsers | 92.5 A | Equal-quality "light" counterpart (198 GB) — the cost-efficient self-host candidate |
| 3 | **Qwen3.5 397B-A17B** NVFP4 | vLLM modelopt, 251 GB | 68.5 C | Flagship-scale Qwen; C on coding partly for vigilance reasons — legal/accounting may read differently |
| 4 | **MiniMax M3.1 Flash** | vLLM | 89.5 A | Third A-tier open model; completes the top-of-field picture |

Second wave if budget allows: GLM 5.3 full (76.0 B), Ornith 1.5 122B (73.0 B), Step-5-Preview
(72.5 C), Muse Spark Open 816B (69.5 C — needs the gated NVFP4 repo and a vLLM build from PR #61879),
MiMo V2.6 Pro (67.0 C). Deprioritized: Nex N2.5 Pro (27.0 D), Laguna-S (65.5 C), Command A Plus
(reviewer-blocked last time), Nemotron 3.5 Super VL (gamed a regression test).

Operational reminders carried from the coding campaign: pin HF revisions; ≥ 100 tok/s warm-probe
admission; persistent `/workspace` volume (stop/restart wipes `/root`); test an actual file fetch
on gated repos, not just metadata; keep keys in env, never argv; one model at a time with the
shield on; weights are the only thing allowed to be deleted for space.

## Tier 4 — frontier anchors (cloud API / subscription CLIs)

These run first (ceiling check, §7a of the methodology) and define the gap.

| Model | Harness | Role |
|---|---|---|
| **Claude Fable 5.1** | Claude Code | Primary reviewer *and* a candidate (blind-graded by the other reviewer for its own runs) |
| **GPT-6 Astra (high)** | Codex CLI | Second reviewer and candidate |
| Claude Opus 5.5 | Claude Code | Fallback reviewer; cost-efficient A-tier anchor ($16.63 on the coding v4) |
| GPT 5.6 Sol | Codex CLI | Fallback reviewer |
| Gemini 3.8 Flash (high) | opencode (OpenRouter) or agy | Cheap-frontier anchor |
| Claude Sonnet 5 | Claude Code | "What a mid-priced commercial model does" anchor |
| Genesys PI House | opencode (LUA Vision) | Brazilian regulated-market model — the obvious comparator for the BR quadrants; expensive, run the BR cases only |

Synthetic data only, so sending fixtures to cloud APIs is fine; still strip any real statute PDF
metadata that could carry an identifying watermark.

## Harness per model (the "kit")

Mirror the coding bench: the kit is model × harness, pinned. `opencode run --agent build` over an
OpenAI-compatible endpoint for every local and self-hosted model (llama-swap / ollama / Strata /
vLLM all expose `/v1`); Claude Code and Codex for the Anthropic/OpenAI anchors; Kimi CLI if K2 is
served via Moonshot for a cloud-vs-self-host check. The workspace is a folder, the tools are read /
write / shell / python — identical surface for everyone. XDG isolation, git-sandboxed workspace,
`GIT_CEILING_DIRECTORIES`, shield moved out of the repo before every run, post-run ndjson scan for
shield/rubric/sibling reads — all unchanged from `run_benchmark_v2.py`.

## Core run — time budget (user cap: ≤ 2 h for Fable/Astra)

Core = 16 packs, 20 session-units (`config/suite_core.json`). Per session: frontier 10–15 min incl. client turns, pushback and the review turn; 5090 ≈ 15 min serial; datacenter ≈ 6 min; Strix ≈ 60 min.

| Tier | Concurrency | Runs | Wall-clock per model |
|---|---|---|---|
| Fable / Astra / Opus 5.5 / Sonnet 5 / Gemini Flash | 4 | 1 (runs 2–3 only on numeric packs if run 1 disagrees) | **~75–100 min** |
| Astra-low resolvability pass | 4 | 1 | ~60 min |
| Datacenter vLLM (4 models) | 4 | 2 | ~1 h each → ~1 pod-day incl. setup |
| RTX 5090 (7 models) | 1–2 | 1 (+1 on numeric packs) | ~5 h each → ~2 days unattended |
| Strix (Q4-vs-Q8 A/B) | 1 | 1 | 3 numeric packs × 2 models ≈ 6 h |
| Reviewer grading | parallel | — | ~4 min per deliverable; ~300 deliverables ≈ 20 API-hours, overlapped |

## Full-matrix estimate (reference only — not the plan)

| Tier | Models | Engagements × runs | Sessions ≈ | Cost driver |
|---|---|---|---|---|
| Local 5090 | 7 | 38 × 3 | ~840 + L4 extra sessions ≈ 1,300 | Wall-clock only; ~2–4 days unattended |
| Local Strix | 4 | 12 numeric/legal subset × 3 | ~150 | Wall-clock; slow |
| Datacenter | 4 | 38 × 3 | ~860 | ~50–70 pod-hours at $9–36/hr → **$600–2,500** incl. setup |
| Frontier | 7 (BR-only for Genesys) | 38 × 3 | ~860 | API/subscription; Fable/Astra reviewer passes dominate |

**Resolvability pass first (user instruction 2026-10-22):** every engagement is run once on GPT-6 Astra at *low* reasoning effort (Codex, `model_reasoning_effort=low`) before any open-weight model. Astra-low is a deliberately weakened frontier candidate: if it still passes the deterministic layers, the case is resolvable; where it falls into a trap, the reviewer (Fable) confirms the trap is real and gradeable, not an ambiguity. No run starts until the user has reviewed the built cases.

Then a pilot: 4 engagements (one per quadrant, L1–L2), 2 frontier + 2 local models, 2 runs each.
That is enough to shake out fixtures, the client script mechanics and the grader before the
expensive tiers run.
