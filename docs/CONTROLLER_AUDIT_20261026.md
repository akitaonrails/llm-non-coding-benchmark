# Controller audit and re-run registry — 2026-10-26

Independent review (Claude Fable 5.1) of every scripted-client and pushback
decision made during the full-suite campaign of 2026-10-24/25. Those decisions
were made live by the orchestrating agent, DeepSeek V4.1 Flash (OpenRouter,
OpenCode session `ses_e9093e347ffehpVL16O2jpuKq5`), recorded on each decision
as `controller: opencode-session-agent`. Per-decision evidence with quoted
questions and deliverable lines is in
[CONTROLLER_AUDIT_20261026_EVIDENCE.md](CONTROLLER_AUDIT_20261026_EVIDENCE.md);
each fault is also appended to the lane's `controller-errors.jsonl`.

## What the controller could affect

The harness only lets the controller (a) choose which scripted facts are
released when the model writes client questions and (b) decide whether a
scripted pushback or generic nudge fires. It cannot author text. Faults are
therefore contamination (facts released that were not asked), starvation
(facts asked but withheld), and pushback misfires or misses.

## Findings per lane

| Lane | Client decisions | Over-released facts (HIGH) | Under-released (HIGH) | Pushback errors | Silent rounds |
|---|---:|---:|---:|---:|---:|
| B300 Flash-Next | 113 | 5 (2) | 2 (1) | 1 missed (HIGH) | 10 |
| B300 GLM 5.3 Flash | 100 | 5 (2) | 1 (1, arguable) | 1 fired wrongly (LOW) | 11 |
| RTX 5090 Flash-Next | 118 | 8 (2) | 1 (0) | 0 | 9 |
| Strix Flash-Next (32 cases reviewed) | 108 | 4 (1) | 1 (0) | 0 | 10 |

"Silent rounds": the controller used `send_response: false` although the
model had written genuinely new questions. No facts leaked, but the model was
not told "the client has no additional information" as the protocol requires.
DeepSeek self-detected 5 of the over-releases (1 Flash-Next, 4 GLM) and re-ran
those cases during the campaign; the figures above exclude those re-run
attempts and count only decisions in the current case directories.

The recurring fault is `brlaw_03_pejotizacao`: the `quem_decidia`
subordination admission was released without being asked in three of four
lanes.

## Fixture corrections (pack version 1.1)

Two scripted answers contained unsubstituted template placeholders that were
sent verbatim to the model: `usacc_03_household_1040` fact `leo_8332`
(`{TY}` → 2025; leaked in all four local lanes) and
`bracc_06_venda_quotas_vs_ativos` fact `distribuicao` (`{ANO}` → 2026; leaked
only in the Sol pilot). Both are corrected in `tasks/` on 2026-10-26; the pack
hashes of those two cases change, so any re-run of them is against pack v1.1
and the earlier attempts stay in `_aborted/` under pack v1.0.

## Re-run registry

Rule applied: every case whose retained attempt involved an over-release, an
under-release, a pushback error, or a leaked placeholder is re-run on the same
model and server configuration with Claude Fable 5.1 adjudicating. The
original attempt is preserved under `<lane>/_aborted/<case>-attemptN` and the
reason is in `retries.jsonl`. Silent rounds alone do not trigger a re-run;
they are an inconsistency the harness default should fix going forward.

| Lane | Case | Reason | Status |
|---|---|---|---|
| B300 Flash-Next | brlaw_10_cobranca_prescrita | over-release `greve` (HIGH) | re-run completed_ungraded (16 min) |
| B300 Flash-Next | brlaw_03_pejotizacao | over-release `quem_decidia`, `outros_clientes` (HIGH) | re-run completed_ungraded (20 min) |
| B300 Flash-Next | bracc_05_abertura_empresa | under-release `luana_trabalho` + silent round (HIGH) | re-run completed_ungraded on attempt 3 (two review-turn failures: OpenCode context compaction at the 64K ceiling produced no summary; preserved as attempt1/attempt2) |
| B300 Flash-Next | usacc_06_sale_asset_vs_stock | missed pushback 0 (HIGH) | re-run ended candidate_output_limit (16,384-token cap at the review turn; model outcome, retained) |
| B300 Flash-Next | brlaw_08_ma_diligencia | over-release `pjs` (LOW) | re-run completed_ungraded (15 min) |
| B300 Flash-Next | brlaw_02_contrato_lgpd | over-release `investimento` (LOW) | re-run completed_ungraded (10 min) |
| B300 Flash-Next | bracc_06_venda_quotas_vs_ativos | under-release `distribuicao` (LOW); pack v1.1 | re-run completed_ungraded (9 min), pack v1.1 |
| B300 Flash-Next | usacc_03_household_1040 | `{TY}` placeholder leaked; pack v1.1 | re-run completed_ungraded (11 min), pack v1.1 |
| B300 GLM 5.3 | brlaw_03_pejotizacao | over-release `quem_decidia` (HIGH) | re-run completed_ungraded (23 min) |
| B300 GLM 5.3 | uslaw_03_noncompete_memo | over-release `counsel`, `austin_trips` (HIGH) | re-run completed_ungraded (22 min) |
| B300 GLM 5.3 | uslaw_09_retaliation_termination | under-release `investigation` (HIGH, arguable) | re-run completed_ungraded (14 min) on the 4th attempt slot; investigation fact released on an explicit ask |
| B300 GLM 5.3 | brlaw_05_divorcio_partilha | over-release `carro_uso` (LOW) | re-run completed_ungraded (31 min) |
| B300 GLM 5.3 | brlaw_08_ma_diligencia | over-release `pjs` (LOW) | re-run completed_ungraded (21 min) |
| B300 GLM 5.3 | uslaw_02_msa_playbook | pushback 0 fired without matching condition (LOW) | re-run completed_ungraded (13 min); pushback correctly withheld this time |
| B300 GLM 5.3 | usacc_03_household_1040 | `{TY}` placeholder leaked; pack v1.1 | re-run completed_ungraded (15 min), pack v1.1 |
| RTX 5090 | brlaw_03_pejotizacao | over-release `quem_decidia` (HIGH) | re-run completed_ungraded (14 min) on the 4th attempt slot; attempt 3 lost its first turn to the 15:13 UTC guard stop; `quem_decidia` withheld |
| RTX 5090 | uslaw_07_chapter11_creditor | over-release `terms` (HIGH) | re-run completed_ungraded (9 min); `terms` withheld |
| RTX 5090 | bracc_04_lucro_real_trimestre | over-release `papel` (LOW) | re-run candidate_output_limit (30 min, session 2 work turn); `papel` released on an explicit ask this time |
| RTX 5090 | brlaw_04_execucao_fiscal | over-release `impugnacao` (LOW) | re-run completed_ungraded (27 min); `impugnacao` released on an explicit ask this time |
| RTX 5090 | brlaw_07_credor_rj | over-release `essencial` (LOW) | re-run completed_ungraded (11 min); `essencial` withheld |
| RTX 5090 | brlaw_08_ma_diligencia | over-release `pjs` (LOW) | re-run completed_ungraded (11 min); `pjs` withheld |
| RTX 5090 | usacc_03_household_1040 | over-release `employer_coverage` (LOW); `{TY}`; pack v1.1 | re-run completed_ungraded (14 min), pack v1.1; `employer_coverage` withheld |
| RTX 5090 | uslaw_08_sale_diligence_apa | over-release `hensley_relationship` (LOW) | re-run completed_ungraded (18 min); `hensley_relationship` released on an explicit ask this time |
| RTX 5090 | usacc_07_holding_qsbs | under-release `loans_terms` (LOW) | re-run completed_ungraded (10 min); `loans_terms` released on an explicit ask |
| Strix | brlaw_07_credor_rj | over-release `essencial` (HIGH) | re-run completed 2026-10-26 (attempt 3; original `_aborted/brlaw_07_credor_rj-attempt1`, controller-error attempt `-attempt2`): `essencial` withheld in both client rounds (never asked), `epp`/`banco` released on explicit asks, stay pushback fired |
| Strix | brlaw_05_divorcio_partilha | over-release `atibaia_reforma` (LOW) | re-run completed 2026-10-26: `atibaia_reforma` released because Q8 asked it explicitly this time; `carro_uso` withheld; FGTS/quotas pushback fired |
| Strix | usacc_01_schedule_c | over-release `commute`, late `payhub_fees` (LOW) | re-run completed 2026-10-26: `commute` released on an explicit Q6 ask; `payhub_fees` withheld (never asked); no scripted pushback |
| Strix | usacc_03_household_1040 | `{TY}` placeholder leaked; pack v1.1 | re-run completed 2026-10-26 on pack v1.1: all five facts released on explicit asks, answer verified placeholder-free; basis pushback fired |
| Strix | uslaw_05 … uslaw_10 | adjudicated live by Claude Fable 5.1 from 2026-10-26 02:25 UTC (uslaw_05 round 1 and session-1 pushback were DeepSeek's, reviewed and judged correct); lane finished 07:12 UTC with 38/38 retained (34 completed, 4 output-limit) | no re-run needed |

## Infrastructure events recorded by the audit

- RTX 5090: reserve guard stopped the server at 22:49 UTC 2026-10-24 (3,062 MiB
  free). 25 cases accumulated three fast `infrastructure_failed` attempts each
  before the server and lane were relaunched; all completed on the relaunched
  server. No completed case spans the outage.
- Strix: at 21:29 UTC 2026-10-25 the orchestrator killed a list of PIDs to stop
  four GLM re-runs it had started concurrently; one PID was the Strix lane's
  harness. `uslaw_04_litigation_sequence` attempt 1 was interrupted (preserved)
  and restarted. This was not reported to the user at the time.
- B300 GLM: `b300_sequence.py` aborted on an SSH client timeout; the lane was
  launched manually after a passing admission. Pod server logs for GLM were
  never exported before the pod was stopped.
- New pod for the re-runs (2026-10-26): proxy `m2pf8j74lpj7qc-64410b08@ssh.runpod.io`,
  direct `root@195.26.233.130:17233`, alias `b300-noncoding`. Fresh overlay;
  weights re-downloaded from the pinned revisions.

## B300 re-run phase completed — 2026-10-26 07:48 UTC

All 15 B300 re-runs hold a retained result on the rebuilt pod (Flash-Next: 7
completed, 1 output-limit; GLM 5.3 Flash: 8 completed). Both lanes again hold
38/38 retained results; `lane-summary.json` was rebuilt over the full suite with
`scripts/rebuild_lane_summary.py` and `results/full-suite-coverage-20261024.json`
regenerated. Pod evidence for both models (launch arguments, package list, server
logs) is under `<lane>/pod-evidence-rerun-20261026/`. The vLLM server was stopped
and the GPU drained; the pod itself keeps billing until the user stops it.

Claude Fable 5.1 adjudicated 72 decisions across the B300 re-runs and the
Strix lane's final cases: 54 client rounds (18 with scripted facts
released, 4 answered with the plain no-information reply because the
model asked new questions no scripted fact covers, 32 archived re-saves
with nothing sent) and 18 session decisions (16 pushbacks fired,
2 withheld because the condition was not met, 0 nudges). Every
decision file carries `controller: claude-fable-5.1-session-agent` and a written
reason quoting the question or deliverable.

## Sol 6 medium full suite completed — 2026-10-26 15:16 UTC

The ChatGPT usage limit had lifted early: the runner's own preflight probe
(`results/preflight-sol6-rerun-20261026`, two turns, sandbox checks passed)
succeeded at 14:04 UTC, so the full 38-case suite was launched as a fresh run,
`results/sol6-medium-full-20261026` (codex-cli 0.164.0, gpt-6-sol, medium
reasoning, four workers, all 38 cases passed explicitly). The 2026-10-24
attempt stays untouched as the recorded quota failure. Outcome: 38/38
`completed_ungraded`, 72.9 min wall, 277.5 case-minutes, US$16.72 API-equivalent.

Claude Fable 5.1 adjudicated all 110 decisions of this lane: 46 client rounds
(24 released scripted facts on explicit asks, 51 facts in total; 10 answered
with the plain no-information reply because no scripted fact matched; 12
archived re-saves with nothing sent) and 64 session decisions (36 pushbacks
fired on verified conditions, 28 withheld, 0 nudges). Decisions consistent
with the audit findings: `quem_decidia` (brlaw_03), `essencial` (brlaw_07),
`terms` (uslaw_07), `counsel` (uslaw_03), `atibaia_reforma`/`carro_uso`
(brlaw_05) and `commute` (usacc_01) were withheld because no question asked
for them; the uslaw_02 section 9.3 pushback and the bracc_05 ITBI pushback
were withheld because their conditions were not met; usacc_09 received both
scripted pushbacks in sequence (second refusal verified in the model's reply).

## RTX 5090 re-run phase started — 2026-10-26 15:10 UTC

The user released the desktop at 15:07 UTC. The personal `qwen-strata-ondemand`
wrapper was stopped again (same step as 2026-10-24); the unrelated `rsc2`
process (about 1.1 GB VRAM) was left alone. A fresh guarded server unit,
`noncoding-rtx5090-rerun-server-20261026`, runs the same engine configuration
(`results/rtx5090-full-setup-rerun-20261026/server.json`, IQ3_S, 64K context,
int8 KV, 3,072 MiB guard); admission passed
(`results/preflight-rtx5090-rerun-20261026`). The nine audited cases were
quarantined with `scripts/queue_reruns.py` and are supervised by `run_lane.py`
with `--max-attempts 8`, because seven of them already carried three or more
preserved attempts from the 2026-10-24 guard outage and the default cap would
have skipped them (the first supervisor was stopped after 49 s; brlaw_03's
interrupted first turn is preserved as `_aborted/brlaw_03_pejotizacao-attempt2`).

Infrastructure event: at 15:13 UTC the reserve guard stopped the server again
(3,018 MiB free; desktop baseline had grown from 3.9 to 4.4 GB). The server was
relaunched at 15:15 UTC with the engine's own elastic reserve raised from
4,096 to 5,120 MiB (4,969 MiB free with everything loaded, versus 3,718 before),
and a watchdog relaunches the unit on any further guard stop while the
supervisor is alive (`results/rtx5090-full-setup-rerun-20261026/watchdog.log`).
The reserve only changes how much VRAM the engine leaves free; model, quant,
context and sampling are unchanged. brlaw_03 recorded `infrastructure_failed`
for the turn cut by the outage and is retried by the supervisor.

## RTX 5090 re-run phase completed — 2026-10-26 17:46 UTC

All nine RTX 5090 re-runs hold a retained result (8 `completed_ungraded`,
1 `candidate_output_limit`: bracc_04 hit the 16,384-token output cap in its
session-2 work turn, a final model outcome). The lane again holds 38/38
retained results (35 completed, 3 output-limit); `lane-summary.json` was rebuilt
over the full suite and `results/full-suite-coverage-20261024.json` regenerated
(six lanes, every case accounted for). The supervisor exited at 17:46 UTC and
the watchdog stopped the owned server unit; the GPU returned to the desktop
baseline. Server evidence (config with the 5,120 MiB reserve, engine log, VRAM
samples, watchdog log and script) is under
`results/rtx5090-full-setup-rerun-20261026/`. The user's `qwen-strata-ondemand`
wrapper was not restarted.

Claude Fable 5.1 adjudicated all 41 decisions of the re-runs: 28 client rounds
(9 released scripted facts on explicit asks, 21 facts in total; 3 answered with
the plain no-information reply; 16 archived re-saves) and 13 session decisions
(9 pushbacks fired on verified conditions, 4 withheld because the condition was
session-bound or not met, 0 nudges). The audited over-releases (`quem_decidia`,
`terms`, `essencial`, `pjs`, `employer_coverage`) were withheld because no
question asked for them; `papel`, `impugnacao`, `hensley_relationship` and
`loans_terms` were released this time because the model asked explicitly.

## Strix re-run phase started — 2026-10-26 19:22 UTC

The user released the Strix machine ("you can run strix now") and reported the
B300 pod powered off. The original lane's Strata server (pid 22744 on
192.168.0.90, config identical to `results/strix-full-setup-20261024/server.json`)
was still resident and healthy, so it was reused rather than restarted.
Admission: `results/preflight-strix-rerun-20261026` (passed, artifact 391,
same_session true). The four original attempts were quarantined under
`_aborted/<case>-attempt1` with the audit reason in `retries.jsonl`, and
`scripts/run_lane.py --max-attempts 6` supervises the re-runs with
Claude Fable 5.1 adjudicating every controller decision.

Controller error during the Strix re-run, 19:43 UTC: on brlaw_07 round 1 the
intended release was `epp` and `banco`, but `controller.py decide` takes a
comma-separated `--facts` list and the option was given twice, so only `banco`
was written and the harness consumed the decision within a second. Rather than
let the re-run carry a new under-release, the harness was interrupted at 19:44
UTC; `run_lane.py` preserved that attempt as
`_aborted/brlaw_07_credor_rj-attempt2` (reason also appended to
`retries.jsonl`) and restarted the case at 19:46 UTC. The withheld
`essencial` reasoning for that round stands: the model stated essentiality as an
assumption and asked only where the goods were and whether still in use.

## Strix re-run phase completed — 2026-10-27 00:14 UTC

All four Strix re-runs hold retained `completed_ungraded` results
(brlaw_07 on its third attempt, the others on their second). 14 decisions, all
`claude-fable-5.1-session-agent`: 10 client rounds (4 with facts released, 1
plain no-information reply for a new question without a fact, 5 archived
re-saves/status tables with no response) and 4 session decisions (3 pushbacks
fired on verified conditions: brlaw_07 stay, brlaw_05 FGTS/quota appreciation,
usacc_03 basis limit; usacc_01 has no scripted pushback). Facts the audit had
flagged as over-released (`essencial`, `carro_uso`, `payhub_fees`) were never
asked and stayed withheld; `atibaia_reforma` and `commute` were released this
time because the models asked for them explicitly. The lane summary was rebuilt
(38/38 retained) and coverage regenerated. Infrastructure: one deliberate
interruption (controller CLI error, above); a transient `/tmp` quota exhaustion
on the desktop at ~22:40 UTC briefly blocked the controller console but not the
harness, whose outputs live under `results/`. The Strix Strata server
(pid 22744, session scope) was stopped after the lane finished. Supervisor logs
for every re-run lane are preserved in `results/rerun-supervisor-logs-20261026/`.

With this, every re-run in the registry is complete.

## Post-campaign verification — 2026-10-27

`scripts/verify_full_suite.py` was run over the five completed lanes after the
last re-run. Hard checks all pass: manifests equal the suite, 38 results per
lane, every completed case has all sessions and its review turn complete,
provenance names the lane's model on every turn, released fact ids are valid,
no controller round is undecided, every quarantined attempt is listed in
`retries.jsonl`, and each local lane ran one harness configuration. Pack hashes
drift from `tasks/` only for the two v1.1 client scripts. Three small findings,
none affecting a retained result:

- `bracc_01_das_fator_r/01-client.decision.json` in the B300 Flash-Next, RTX
  5090 and Strix lanes predates the `controller` field (reason present,
  releases match the literal suggestions; reviewed in the audit).
- Two review turns (B300 Flash-Next `brlaw_03`, RTX 5090 `brlaw_04`) logged one
  HTTP error each among ~28 requests; both turns completed.
- The superseded pilot directories (`sol6-medium-core-20261022-r2`,
  `rtx5090-flash-next-reserved-subset-20261024`,
  `strix-flash-next-iq3s-numeric-20261022`) and the quota-failed
  `sol6-medium-full-20261024` still carry the pre-v1.1 placeholder leak; they
  are not part of the full-suite coverage and were not re-run.

Execution-level numbers are in
[FULL_SUITE_EXECUTION_SUMMARY.md](FULL_SUITE_EXECUTION_SUMMARY.md).
