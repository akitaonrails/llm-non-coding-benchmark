# llm-non-coding-benchmark

Can an AI model do real, day-to-day accounting and legal work — in the United States and in
Brazil — well enough that a professional would sign the result? And can the open-weight models a
firm is allowed to run on its own hardware get close to the frontier commercial ones?

Status: **v1 — 38 case packs structurally validated (2026-10-22). Sol 6 medium completed the 16-pack timing baseline in 22.26 minutes at four-way concurrency; correctness grading remains pending.** Sibling of
[`llm-coding-benchmark`](../llm-coding-benchmark), from which it inherits the harness, isolation,
nudge and scoring discipline.

A new **full-suite campaign is now running**: Sol 6 medium and four hardware/model
configurations, each with all 38 cases / 63 sessions. See
[full scope, estimates, and exclusion rationale](docs/FULL_SUITE_CAMPAIGN.md) and
[live coverage](results/full-suite-coverage-20261024.json), and the
[controller audit and re-run registry](docs/CONTROLLER_AUDIT_20261026.md), with execution-level results in the
[full-suite execution summary](docs/FULL_SUITE_EXECUTION_SUMMARY.md) and the
**correctness grading** in the [full-suite grading findings](docs/FULL_SUITE_GRADING_20261027.md)
(blind AI grading per [the grading protocol](docs/GRADING_PROTOCOL_20261027.md); human spot-check pending). The completed pilots
below are historical coverage, not completion of this new campaign.

The October 24 pilot execution is complete: single B300 **11/12 engagements
completed**, guarded RTX 5090 **3/3**, and Strix **8/11 across nine configurations**
(three turn timeouts). These are execution outcomes, not correctness scores.
See [campaign status](docs/CAMPAIGN_STATUS.md),
[Strix results](docs/STRIX_PILOT_RESULTS.md), and
[matched-case timing comparison](docs/PILOT_TIMING_COMPARISON.md).
The broader model/case matrix remains pending.

## Read in this order

1. [docs/METHODOLOGY.md](docs/METHODOLOGY.md) — what is tested and how it is graded. Written for a
   CPA / contador / attorney / advogado; no engineering background needed.
2. [docs/TASKS_V1.md](docs/TASKS_V1.md) — the forty engagements as case files: client, documents,
   deliverable, how it is checked, and (reviewer-only) the planted problems.
3. [docs/MODEL_ROSTER.md](docs/MODEL_ROSTER.md) — which models run where (RTX 5090, Strix Halo,
   rented B300/H200, frontier anchors) and why.

## The suite in one table (38 engagements)

| | US accounting & tax | Brazil contabilidade & fiscal | US law | Brazil direito |
|---|---|---|---|---|
| **L1 floor** | Schedule C from 1099s + bank feed | DAS with Fator R on the boundary | Deadlines from a served complaint | Prazos from a DJe intimação |
| **L2** | Close with an unexplainable gap · Entity choice & S election (incl. formation law) | Regime memo · Abertura (ITBI, pró-labore, societário) | MSA vs. playbook | Contrato + LGPD |
| **L3** | Household 1040 · Asset vs stock sale · Holding & QSBS · Revenue & going concern under CEO pressure · Fraud indicators | CBS/IBS 2026 test year · Venda de quotas vs ativos · Holding patrimonial · Distribuição de lucros 2026 · Provisões & covenant | Non-compete memo w/ planted authorities · Divorce split & child support · Chapter 11 creditor · Sell-side M&A diligence · Retaliation termination · LLC squeeze-out | Pejotização · Divórcio & alimentos · Credor na RJ · Diligência M&A · Justa causa de gestante/CIPA · Cobrança prescrita |
| **L4 multi-session** | 12 closes w/ restatement · Chapter 11 debtor (3) | Lucro Real quarter (3) · Recuperação judicial (3) | 5-session litigation | 5-session execução fiscal |

Every engagement is built around a **wrong conclusion the file invites** — one the client,
management or the other side is usually pushing for — and the evidence that should make a
careful professional reverse. See the trap tables in `docs/TASKS_V1.md`.

Every engagement: closed reference library (no internet), scripted client that only answers what
is asked, at most two fixed generic nudges, a final "review before delivery" turn weighted at 40%,
deterministic oracle first, fabricated citation or plugged number = failed run.

## Core run (`config/suite_core.json`)

16 packs / 20 session-units, chosen to fit **≤ 2 h wall-clock for Fable/Astra** (4 concurrent
sessions, 1 run). The other 22 packs stay built as a reserve. See the summary in the roster.

## Layout (as built)

```
docs/                 methodology, case files, roster, sources
tasks/<quadrant>/<id>/
  CONTRACT.md         the engagement letter the model sees
  workspace/          documents/ (PDF, CSV, XML, txt) · library/ (closed, with INDEX.md) · deliverable/
  client_script.json  withheld facts (triggers → answers) and scripted pushback turns
  sessions.json       only for multi-session packs: what is revealed per session and the per-session prompt
  reviewer/           🔒 manifest.json (traps, oracle, rubric, library verification), reference/ (computed answers)
fixtures/generators/  core toolkit: double-entry ledger, PDF renderers (statements, IRS-style forms, pleadings), NF-e XML, date rules
fixtures/cases/       one generator module per pack — rebuild everything with `python scripts/build_cases.py`
scripts/              build_cases.py · check_pack.py (validator + inventory table)
```

**Shield before any run:** the isolated Codex runner mounts only the candidate workspace,
so reviewer keys, fixtures, other runs and future documents are physically inaccessible.
For runners without this namespace isolation, move every `tasks/*/*/reviewer/` directory and the whole `fixtures/` tree
outside the repo (the generators contain the answers), exactly as the coding benchmark moves its rubric
and sibling results; restore after. `client_script.json` and `sessions.json` are read by the runner,
never mounted into the model's workspace.

**Timing runner:** `scripts/run_codex_baseline.py` handles isolated workspaces, shell network
denial, scripted client replies, conditional pushbacks, staged documents, review snapshots,
timing and token accounting. `scripts/report_baseline.py` summarizes measurements.
See [docs/BASELINE_RUN.md](docs/BASELINE_RUN.md) for the protocol and known limitations.

The [completed baseline report](results/sol6-medium-core-20261022-r2/REPORT.md)
records 67.33 summed active minutes and $5.32 estimated API-equivalent candidate
cost (ChatGPT subscription authentication, not an invoice). Setup, the invalidated
preflight attempt and Astra controller usage are excluded. All 16 executions
finished, with zero infrastructure failures; this is not a correctness pass rate.
[Observed fixture issues](results/sol6-medium-core-20261022-r2/OBSERVATIONS.md)
must be adjudicated before scoring.

**Still pending:** general model/harness adapters and validated correctness graders against
`reviewer/reference/`. A finished timing run is not a passing correctness result.
