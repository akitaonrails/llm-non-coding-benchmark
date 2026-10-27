# llm-non-coding-benchmark

Can an AI model do real, day-to-day **accounting and legal work**, in the United States and in
Brazil, well enough that a professional would sign the result? And can the open-weight models a
firm is allowed to run on its own hardware get close to the frontier commercial ones?

This repository holds the benchmark (38 engagement-style case packs), the isolated runners, the
raw results of a full five-lane campaign, and a blind correctness grading of those results.
It is the sibling of [`llm-coding-benchmark`](https://github.com/akitaonrails/llm-coding-benchmark)
and inherits its harness, isolation, nudge and scoring discipline.

**Status (2026-10-27):** v1.1 packs, five full-suite lanes executed and verified, all 190 runs
blind-graded by an AI grader. Human professional spot-check of the flagged events is still pending,
so treat the numbers below as a first reading, not a certification.

## Headline results

Five configurations, each run once over all 38 cases (63 session-units). Full write-up:
[docs/FULL_SUITE_GRADING_20261027.md](docs/FULL_SUITE_GRADING_20261027.md).

| Lane | Completed /38 | Trust-fatal runs | Medium flags | Oracle strict (graded items) | Vigilance |
|---|---:|---:|---:|---:|---:|
| Sol 6 medium / Codex CLI | 25 | 0 | 0 | 84% | 100.0 |
| Qwen3.8 Flash-Next IQ3_S / RTX 5090 | 27 | 0 | 2 | 91% | 99.6 |
| Qwen3.8 Flash-Next IQ3_S / Strix Halo | 27 | 3 | 1 | 90% | 97.5 |
| Qwen3.8 Flash-Next NVFP4 / B300 | 23 | 2 | 4 | 85% | 99.6 |
| GLM 5.3 Flash NVFP4 / B300 | 23 | 0 | 0 | 93% | 98.8 |

*Completed* = every session and the review turn finished, no trust-fatal event, every gated oracle
item correct. *Trust-fatal* = a fabricated authority, invented client fact, plugged number,
superseded law or false completion claim (a professional would stop trusting the work).
*Vigilance* = how many planted problems the model caught before being told to review.

What the grading found, in short:

- **The trust gate is the only layer that separates models.** Every high-confidence trust failure
  was an invented client fact or fabricated quote, all from Qwen3.8 Flash-Next (three on Strix,
  two on the B300). Nobody cited an authority outside the closed library in a final deliverable.
- **Vigilance saturates.** Every lane caught 97 to 100% of the planted problems unprompted. The
  v1 packs are too easy on that axis to rank models the way the coding benchmark does.
- **The review-before-delivery turn cuts both ways.** It removed fabrications in 113 of 190 runs
  and regressed correct work in about a dozen.
- **Cheap local hardware held up.** A 3-bit build on one RTX 5090 matched or beat every other
  configuration on completion with a clean trust record. The rented B300 bought no quality.
- **The frontier anchor is not ahead on completion.** Sol 6 had no trust events but missed
  numbers on five Brazilian accounting packs and asked the client far fewer questions.

Sections 6 and 7 of the grading report list the harness gotchas and the fixture defects to fix
before a v1.2.

## Read in this order

1. [docs/METHODOLOGY.md](docs/METHODOLOGY.md) — what is tested and how it is graded. Written for a
   CPA / contador / attorney / advogado; no engineering background needed.
2. [docs/TASKS_V1.md](docs/TASKS_V1.md) — the engagements as case files: client, documents,
   deliverable, how it is checked, and (reviewer-only) the planted problems.
3. [docs/FULL_SUITE_GRADING_20261027.md](docs/FULL_SUITE_GRADING_20261027.md) — findings,
   highlights, gotchas and insights from grading the five lanes.
4. [docs/GRADING_PROTOCOL_20261027.md](docs/GRADING_PROTOCOL_20261027.md) — how the blind grading
   was done, the scoring rules and the `grade.json` schema.
5. [docs/FULL_SUITE_EXECUTION_SUMMARY.md](docs/FULL_SUITE_EXECUTION_SUMMARY.md) — execution-level
   results: completion, output-cap hits, active minutes, tokens, throughput per lane.
6. [docs/MODEL_ROSTER.md](docs/MODEL_ROSTER.md) — which models run where and why.

Supporting documents:

- [docs/FULL_SUITE_CAMPAIGN.md](docs/FULL_SUITE_CAMPAIGN.md) — authorized scope, pre-run estimates,
  exclusion rationale.
- [docs/CONTROLLER_AUDIT_20261026.md](docs/CONTROLLER_AUDIT_20261026.md) and its
  [evidence file](docs/CONTROLLER_AUDIT_20261026_EVIDENCE.md) — audit of every scripted-client
  decision and the re-run registry.
- Per-hardware run notes: [Codex / Sol 6](docs/BASELINE_RUN.md), [RTX 5090](docs/RTX5090_RUN.md),
  [Strix Halo](docs/STRIX_RUN.md), [B300](docs/B300_RUN.md).
- Pilot history (October 22 to 24, before the full suite): [campaign status](docs/CAMPAIGN_STATUS.md),
  [Strix pilot](docs/STRIX_PILOT_RESULTS.md), [B300 pilot](docs/B300_PILOT_RESULTS.md),
  [timing comparison](docs/PILOT_TIMING_COMPARISON.md).
- [docs/SOURCES.md](docs/SOURCES.md) — the statutes, forms and rules the closed libraries draw on.

## The suite in one table (38 engagements)

| | US accounting & tax | Brazil contabilidade & fiscal | US law | Brazil direito |
|---|---|---|---|---|
| **L1 floor** | Schedule C from 1099s + bank feed | DAS with Fator R on the boundary | Deadlines from a served complaint | Prazos from a DJe intimação |
| **L2** | Close with an unexplainable gap · Entity choice & S election | Regime memo · Abertura (ITBI, pró-labore, societário) | MSA vs. playbook | Contrato + LGPD |
| **L3** | Household 1040 · Asset vs stock sale · Holding & QSBS · Revenue & going concern under CEO pressure · Fraud indicators | CBS/IBS 2026 test year · Venda de quotas vs ativos · Holding patrimonial · Distribuição de lucros 2026 · Provisões & covenant | Non-compete memo w/ planted authorities · Divorce split & child support · Chapter 11 creditor · Sell-side M&A diligence · Retaliation termination · LLC squeeze-out | Pejotização · Divórcio & alimentos · Credor na RJ · Diligência M&A · Justa causa de gestante/CIPA · Cobrança prescrita |
| **L4 multi-session** | 12 closes w/ restatement · Chapter 11 debtor (3) | Lucro Real quarter (3) · Recuperação judicial (3) | 5-session litigation | 5-session execução fiscal |

Every engagement is built around a **wrong conclusion the file invites**, usually the one the
client, management or the other side is pushing for, and the evidence that should make a careful
professional reverse. Every engagement runs with a closed reference library (no internet), a
scripted client that only answers what is asked, at most two fixed generic nudges, and a final
"review before delivery" turn. A fabricated citation or a plugged number fails the run.

## Repository layout

```
docs/                     methodology, case files, roster, run notes, audit, grading report
config/                   suite definitions (suite_full_20261024.json = the 38 cases) and lane configs
tasks/<quadrant>/<id>/    one case pack per engagement (usacc, bracc, uslaw, brlaw)
  CONTRACT.md             the engagement letter the model sees
  workspace/              documents/ · library/ (closed, with INDEX.md) · deliverable/
  client_script.json      withheld facts (triggers → answers) and scripted pushback turns
  sessions.json           multi-session packs only: what is revealed per session
  reviewer/               🔒 manifest.json (traps, oracle, rubric), reference/ (computed answers)
fixtures/                 generators that build the packs (ledgers, PDF forms, NF-e XML, date rules)
scripts/                  builders, validators, runners, controller, verifiers, grading tools, tests
results/                  every retained run, pilot, preflight and the grading (see below)
```

Results that matter most:

| Path | What it is |
|---|---|
| `results/sol6-medium-full-20261026/` | Sol 6 medium via Codex CLI, 38/38 executed |
| `results/rtx5090-flash-next-full-20261024/` | Flash-Next IQ3_S on one RTX 5090 |
| `results/strix-flash-next-full-20261024/` | Flash-Next IQ3_S on a Strix Halo |
| `results/b300-flash-next-full-20261024/` | Flash-Next NVFP4 on a rented B300 |
| `results/b300-glm53-flash-full-20261024/` | GLM 5.3 Flash NVFP4 on the same B300 |
| `results/grading-20261027/` | blind grades per case, letter→lane mapping, overrides, scores |
| `results/full-suite-coverage-20261024.json` | machine-readable coverage per lane |

Each case directory under a lane keeps the prompts, per-turn responses, raw event logs,
provenance, snapshots (`s<N>-initial`, `s<N>-pre-review`, `final/`), every controller
`*.pending.json` / `*.decision.json`, and `result.json`. Invalidated attempts are quarantined
under `_aborted/` and listed in `retries.jsonl`; nothing is overwritten.

## How to run

Python 3.11+. Building the packs needs the `markdown` package (PDF rendering); the test suite
needs `pytest`; `scripts/b300_prepare.py` needs `huggingface_hub`. Everything else is standard
library. Running a model needs the Codex CLI (frontier lane) or OpenCode plus an
OpenAI-compatible endpoint (local lanes), and `bwrap` for the namespace isolation.

```bash
pip install markdown pytest
```

### 1. Build and validate the packs

```bash
python3 scripts/build_cases.py              # deterministic; --only usacc_01 bracc_01 for a subset
python3 scripts/check_pack.py --table       # structural validation + inventory table
python3 -m unittest discover -s scripts -p 'test_*.py'
```

### 2. Shield the answer keys

The Codex and OpenCode runners mount only the candidate's workspace into a namespace, so
`reviewer/`, `fixtures/`, other runs and unreleased session documents are physically unreachable.
If you use any other runner, move every `tasks/*/*/reviewer/` directory and the whole `fixtures/`
tree outside the repository before the run (the generators contain the answers) and restore them
after. `client_script.json` and `sessions.json` are read by the runner and never mounted.

### 3. Run a lane

Frontier model through the Codex CLI (four concurrent cases):

```bash
python3 scripts/run_codex_baseline.py --run-dir results/<lane> --workers 4 \
    --case usacc_01_schedule_c --case bracc_01_das_fator_r ...   # all 38 ids from config/suite_full_20261024.json
```

Local or rented open-weight model through OpenCode (one case at a time, networkless tools, an
allow-listed socket gateway to the endpoint):

```bash
python3 scripts/run_local_baseline.py --run-dir results/<lane> \
    --endpoint http://127.0.0.1:8000 --model <served-model-name> --hardware "RTX 5090; IQ3_S; Strata" \
    --case usacc_01_schedule_c ...
```

For a full 38-case lane, let the supervisor own it. It restarts the harness after a crash,
quarantines interrupted attempts under `_aborted/` and records every retry:

```bash
setsid nohup python3 scripts/run_lane.py --run-dir results/<lane> \
    --endpoint http://127.0.0.1:8000 --model <served-model-name> --hardware "..." > /dev/null 2>&1 &
python3 scripts/lane_status.py            # one-screen status of every lane
```

Without explicit `--case` arguments both runners default to the 16-case core subset; always
pass all 38 ids for a full run. Per-hardware notes, admission probes,
VRAM guard for a desktop GPU and the systemd units used are in the run docs linked above.

### 4. Act as the scripted client (controller)

The harness blocks on `<stem>.pending.json` until a matching decision file appears. A supervising
person or agent reads the candidate's questions, releases only the scripted facts actually asked
for, and records the reason. The controller never invents answers.

```bash
python3 scripts/controller.py list
python3 scripts/controller.py show results/<lane>/<case>/01-client.pending.json
python3 scripts/controller.py decide results/<lane>/<case>/01-client.pending.json \
    --facts prolabore_abril --reason "Q2 asks the April payment date directly."
```

Re-run one case after a recorded fault without losing the original attempt:

```bash
python3 scripts/rerun_case.py --run-dir results/<lane> --case <case> --reason "..." \
    --endpoint ... --model ... --hardware ...
```

### 5. Verify execution and coverage

```bash
python3 scripts/verify_full_suite.py          # cross-lane checks; non-zero exit on a hard failure
python3 scripts/report_full_coverage.py       # rewrites results/full-suite-coverage-20261024.json
```

### 6. Grade blind and score

Build one bundle per case with the lanes relabelled by random letters, grade each bundle without
ever opening `results/` or the mapping, then score:

```bash
python3 scripts/build_grading_bundles.py --out /path/outside/repo/bundles \
    --mapping /path/outside/repo/mapping.json --seed 20261027
# grade each bundle into results/grading-20261027/grades/<case>.json
# (schema and steps in docs/GRADING_PROTOCOL_20261027.md)
python3 scripts/score_grades.py --grades results/grading-20261027/grades \
    --mapping /path/outside/repo/mapping.json --bundles /path/outside/repo/bundles \
    --overrides results/grading-20261027/overrides.json \
    --out results/grading-20261027/as-keyed
python3 scripts/score_grades.py ... --fixture-demotions --out results/grading-20261027/demoted
```

`overrides.json` records every manual grading decision with its reason. The `demoted` cut
excludes four keyed items that every run failed identically because of a documented pack defect;
the `as-keyed` cut keeps them. Both are committed.

## What this does and does not support

- One run per configuration. Repeating the Flash-Next lanes is the first thing to do before
  claiming a difference between serving stacks.
- Graded by an AI, blind, against a pre-registered key. The five high-confidence trust events,
  seven medium-confidence flags and four demotions should be read by a human CPA, contador,
  attorney or advogado before publication.
- Timing and tokens are measured; rental cost for the B300 was never supplied and is not claimed.
- The v1 packs leak several trap answers in their own libraries. Fix list in the grading report,
  section 7, before v1.2.
