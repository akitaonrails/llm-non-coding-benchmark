# Sol 6 medium timing pilot

Completed result: [REPORT.md](../results/sol6-medium-core-20261022-r2/REPORT.md).
All 16 engagements finished in 22.26 minutes wall-clock, with 67.33 summed
active minutes and $5.32 API-equivalent candidate cost. Provenance/artifact
verification passed; correctness grading remains pending.

Authorized by the user on 2026-10-22, replacing the proposed Astra-low first
pass for this timing pilot. Target: `gpt-6-sol`, reasoning `medium`, standard
service, Codex CLI 0.163.0, four concurrent core engagements, one attempt each.

The original 16-pack core and 20 session-units remain the workload. This pilot
measures runtime and usage; professional validation, preregistered independent
review and full correctness grading are pending. Completion means execution
finished, not that the work product passed.

## Isolation and verification

The outer bubblewrap namespace exposes system binaries, certificate material,
a private per-case Codex state directory and that case's working folder. It
does not mount the repository, fixtures, reviewer keys, other candidates or
unreleased session documents. This provides the intended physical shielding
without moving the source packs. The inner Codex workspace-write sandbox
denies network access to model-generated commands. Web search, apps, plugins,
memory and multi-agent tools are disabled. The CLI itself can reach its model
provider. Per-case credentials and private session state are removed at exit.

Before running cases, preflight checks host path invisibility, network denial,
file writes, exact model/reasoning provenance, session resume and usage capture.
The controller tests verify selective withheld-fact release and repeat handling.
Pack hashes freeze the input version. Raw events, prompts, responses, usage and
model context are retained outside the candidate's mount.

## Interactions

Candidates write QUESTIONS.md or PERGUNTAS.md and finish their turn. The
controller selects the scripted facts actually requested, including clear
paraphrases of triggers, and records its reasons. Keyword matches are advisory
only. The runner sends the selected scripted answers verbatim; the controller
cannot invent client responses. Unmatched questions receive a neutral
no-information reply. Revisions that only archive earlier questions can be
acknowledged without another candidate turn using `send_response: false`.

An initial attempt was invalidated because literal-only matching missed clear
paraphrases. Its artifacts remain under `results/sol6-medium-core-20261022/` as
setup evidence. The corrected baseline is `results/sol6-medium-core-20261022-r2/`.

After each session's first work product, the runner writes a pending control
request. The supervising agent inspects the candidate artifacts and records
which scripted pushback conditions are met, with a reason. The runner sends
only those messages verbatim. This controller delay is measured separately.
The CEO's second-refusal pushback receives its own decision after the first
pushback response. Review-before-delivery occurs once at the engagement end.
Snapshots preserve initial, pre-review and final work for later grading.

## Time and cost

Report elapsed suite wall time, summed active candidate turn time, per-case
runtime, controller waiting, input/cached-input/output tokens and estimated
API-equivalent dollars. Setup and infrastructure preflight are separate.
Rollout cumulative usage counters are differenced across resumed turns to
avoid double counting. CLI usage is a fallback when rollout counters are absent.

Authentication is via the existing ChatGPT login. API-equivalent cost is not a
subscription invoice or an observed charge. Published standard token rates:
$2/M uncached input, $0.20/M cached input, $2.50/M cache writes, $10/M output.
Reasoning tokens are included in output and are not charged twice. Source:
https://developers.openai.com/api/docs/models/gpt-6-sol (checked 2026-10-22).

## Run

```sh
python3 -m unittest discover -s scripts -p 'test_baseline.py'
python3 scripts/run_codex_baseline.py \
  --install /home/akitaonrails/.local/share/mise/installs/codex/0.163.0 \
  --run-dir results/sol6-medium-core-20261022-r2 --workers 4
```

The destination must be new. Resolve each `*.pending.json` by writing a sibling
`*.decision.json` with `pushback_indices`, `nudge`, and an evidence-based `reason`.
Do not put task-specific advice into this file: only the registered messages
can be sent. A failure preserves evidence and is reported as infrastructure
failure, not candidate failure. Never restart over an existing result directory.

## Retention and cleanup

All prompts, candidate events, intermediate/final deliverables, controller
decisions and reports are retained. Temporary candidate credentials and state
were removed after the corrected run; no candidate processes remain. The
invalidated attempt's leftover state was moved to the trash after removing
credential copies, so that noncredential state is recoverable. Original user
authentication and all source packs were untouched.
