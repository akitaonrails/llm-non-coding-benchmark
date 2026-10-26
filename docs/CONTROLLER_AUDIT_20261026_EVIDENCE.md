# Consolidated controller audit — full-suite campaign 2026-10-24 (reviewed 2026-10-26)

Orchestrator/controller: OpenCode session ses_e9093e347ffehpVL16O2jpuKq5, model openrouter/deepseek/deepseek-v4.1-flash-1017 (variant high).


---

# Controller audit — lane `b300-flash-next-full-20261024`

Scope: every client decision (113 rows, 99 released facts) and every session decision (63 rows) in the dump, checked against the raw question text, the scripted `client_script.json` facts, and the `s<N>-initial/` deliverables. The already-recorded `bracc_03` `ponto_fixo` fault is confirmed and not re-counted (the dump holds the clean re-run, which released only `rejeicao`).

## Summary

| Client decisions | Count |
|---|---|
| Rows reviewed in detail (released and/or over/under-vs-keyword non-empty) | 58 of 113 |
| Released facts confirmed ASKED (keyword or clear paraphrase) | 94 of 99 |
| Over-releases | 5 facts (2 HIGH, 3 LOW) |
| Under-releases | 2 facts (1 HIGH, 1 LOW) |
| `send_response: false` rounds with genuinely new questions (SILENT-NO-REPLY) | 6 cases / 10 rounds (1 HIGH, rest LOW) |

| Session decisions | Count |
|---|---|
| Rows reviewed | 63 |
| Pushbacks fired, condition verified in deliverable | 36 of 36 |
| Pushbacks fired wrongly | 0 |
| Pushbacks missed | 1 (HIGH) |
| Nudges | 0 (none warranted; all deliverable sets present) |

## Findings

### Over-releases

1. **brlaw_10_cobranca_prescrita / 01-client / `greve` — HIGH.** Q5 asked only "Os relatórios de serviço de out/2020–jan/2021 estão assinados e arquivados com o contrato?"; the released answer ("Teve uma greve lá em fev/2021, mas nosso pessoal fez o que deu. Temos relatórios assinados pelo encarregado deles") concerns Feb/2021 partial performance on parcels 5–6, the exact subject of the scripted pushback, and the model logged it as "Fato novo útil … reforça abandono total das parcelas 5–6".
2. **brlaw_03_pejotizacao / 01-client / `quem_decidia` — HIGH.** No question asks who approved vacations or enforced hours; Q4 asks for time-record evidence ("existem registros de jornada além da planilha") and Q7 asks about other PJs ("horário fixo" is a false hit), yet the subordination admission was released and the model itself recorded it as "(admissão adicional, espontânea)" and raised the vínculo probability from 80–90% to 85–90%.
3. **brlaw_03_pejotizacao / 01-client / `outros_clientes` — LOW.** Q7 asks "quantos prestadores PF/PJ com cláusulas de exclusividade … a Solaris mantém", not whether Rafael had other clients; the model noted "Carla negou que Rafael tivesse outros clientes; nada informou sobre outros PJs".
4. **brlaw_08_ma_diligencia / 01-client / `pjs` — LOW.** Q5 asks the "Custo mensal agregado dos 11 engenheiros PJ"; the answer volunteered "trabalham 9h-18h aqui, exclusivos, com gestor", which the model then logged as "admissão fática do perfil de vínculo" (the finding already existed from the data room, so the effect is reinforcement, not creation).
5. **brlaw_02_contrato_lgpd / 01-client / `investimento` — LOW.** Q4 asks "qual o sistema substituído e em que formato exportarão para a NEXA"; the released "Migrar 22 mil prontuários é um projeto de meses. Sair no meio seria caótico" is about exit lock-in, a loose paraphrase at best.

### Under-releases

6. **bracc_05_abertura_empresa / 02-client (and 03, 04) / `luana_trabalho` — HIGH.** Round-2 item B.6 asks "Forma de integralização do dinheiro de Luana (R$ 105.000 no ato, ou parcelado?)", a direct question on Luana's integralização; the scripted "Luana: eu não tenho dinheiro pra aportar; a ideia é que meu trabalho vale 20%" is the sócia-de-serviço trap named in CONTRACT.md, was never released, and by round 4 the model locked in premise P5 "R$ 105.000 em moeda corrente, no ato".
7. **bracc_06_venda_quotas_vs_ativos / 01-client / `distribuicao` — LOW.** Q1 "Na Proposta B, a distribuição do caixa da Vértice aos sócios ocorreria ainda em 2026?" and Q4 (single month vs spread) ask when the cash would be taken out; the fact "se vender pela PJ a gente tira o dinheiro todo em 2026 mesmo" answers it (no keyword hit because the model wrote "distribuição", not "distribuir"); the model's assumption happened to match.

### SILENT-NO-REPLY (send_response=false with genuinely new questions)

8. **bracc_05_abertura_empresa / 02-client — HIGH** (same round as finding 6). New items B.4 (destino dos R$ 25.000/mês de Marina), B.6 (integralização de Luana) and B.7 (escolha informada regime × locação) were not in round 1; controller reason claims "it asks nothing new".
9. **bracc_06_venda_quotas_vs_ativos / 03-client, 04-client — LOW.** Q7 "(Nova, rodada 3) O 'outro contador' citou alguma lei de atualização de custo…? — ABERTA" and Q8 "(Rodada de revisão) Existem lucros/reservas pré-2025 com distribuição aprovada até 31/12/2025?" are explicitly new; nothing was sent.
10. **bracc_07_holding_patrimonial / 02-client — LOW.** Section F "Novas perguntas — surgidas das respostas" Q19–Q21, each tagged "[NOVA — SEM RESPOSTA]" (aluguel de Higienópolis; quais imóveis "vagos"; encargos dos 9 locados); controller reason says "nothing new is asked".
11. **usacc_03_household_1040 / 02-client — LOW.** New Q1 "confirm the executed Form 8332 for Leo names tax year 2025" exists only because the released `leo_8332` answer was sent with the literal placeholder "{TY}" unsubstituted (confirmed in `01-client.json`) — a harness template bug worth fixing; the follow-up got no reply.
12. **uslaw_04_litigation_sequence / 03-client (Q11–Q12: who sent the pre-engagement demand letter) and 08-client (Q13–Q14: who took the Oct 20 Halvorsen call; who signs a settlement) — LOW.** Both blocks are headed "New questions — Session 2/5"; nothing was sent.
13. **usacc_08_chapter11_debtor / 02-client, 03-client, 04-client — LOW.** 02 adds "Session 2 — new questions" and "Session 3 — new questions" blocks (mostly document requests later satisfied by session files), 03 adds "New — CFO follow-up directive re Mesa" (will Mesa ship against a genuine deposit; has Redwood historically paid deposits), 04 adds nine "Open items — Session 2" questions; none received a reply.

Borderline, not counted: `bracc_04` 02/03-client (requests for next month's documents, delivered by the following session) and `usacc_02` 03-client (pushback handling, no new question).

### Session decisions

14. **usacc_06_sale_asset_vs_stock / s1 / pushback 0 — MISSED, HIGH.** `s1-initial/memo.md` line 15 reads "**Do not sign Buyer A's LOI on Friday as drafted.**", exactly the condition "if the memo recommends against signing Buyer A as drafted"; the controller wrote "No pushback is scripted for this case (the payload lists none)" although `s1.pending.json` lists it, so the model never faced Ray's "walk me through it / what number from Lone Star beats Hensley" challenge.
15. **brlaw_04_execucao_fiscal / s2 / pushback 0 — fired, defensible.** `sessao2/manifestacao.md` §I.2 "A executada não se opõe à correção formal … Súmula 392/STJ autoriza corrigir por substituição" drops the nullity-for-vice thesis in favour of accepting the amendment, which reasonably satisfies "se a manifestação abandonar a tese do vício da multa". Counted as correct; noting because the model kept the vice as a side point.
16. **uslaw_02_msa_playbook / s1 / pushback 0 — fired, defensible.** `issues.json` rank-2 clause "§9.1/§10.1 (read with §9.3)" flags §9.3's carve-outs as a problem ("cover only gross negligence… not the §10.1 indemnity"), which matches "if issues.json flags §9.3 … as a problem" well enough for Priya's challenge to be apt. Counted as correct.

All 27 empty session decisions were checked: 22 are scoped to another session number (brlaw_04 s1/s3/s5, uslaw_04 s1/s3/s5, bracc_04 s1/s2, bracc_08 s2/s3, usacc_08 s2/s3, usacc_04 s1–s6 and s8–s11), 2 have no scripted pushback (usacc_01, bracc_01), 2 had a condition that did not hold (bracc_05: `numeros.json` `itbi.devido=false`; usacc_10: communication addressed "To: Dr. R. Patel DDS, Chair"), and 1 is the miss in finding 14.

The 36 fired pushbacks were each verified against the cited artifact (e.g. brlaw_01 `prazos.json` `prazo_em_dobro: false`; brlaw_07 `estrategia.json` `retomada_dos_bens_agora: false`; usacc_03 `return.json` `loss_suspended: 16500`; usacc_09 `response_to_ceo.md` "cannot be booked. Reversed." twice before pushback 1; usacc_04 `month_07/open_items.md` item 15 "ASC 250 restatement … February–June 2025"; uslaw_09 "Do not terminate Dana Whitcomb today"; uslaw_01 "Removal is NOT available"; bracc_10 "Não posso endossar nenhum dos três"). No fired pushback lacked a matching condition.

---

# Controller audit — lane b300-glm53-flash-full-20261024

Scope: every `*-client.decision.json` and `s*.decision.json` in the current case directories (re-runs for brlaw_10, usacc_01, usacc_06, uslaw_09; `_aborted/` not re-reviewed). Question text read in full from the pending files; session conditions checked against `s<N>-initial/` deliverables.

## Summary

| Client decisions | Count |
|---|---|
| Rows reviewed (all client rounds) | 100 |
| of which rows with releases or keyword discrepancies (fact-level review) | 61 |
| of which `send_response: false` rounds (compared with prior round) | 66 |
| Rows confirmed OK | 84 |
| Facts released / confirmed ASKED | 73 / 68 |
| Over-releases (facts) | 5 (2 HIGH, 3 LOW) in 4 rows |
| Under-releases (facts) | 1 (HIGH, arguable) |
| Silent-no-reply rounds (new questions, nothing sent) | 11 (all LOW) |

| Session decisions | Count |
|---|---|
| Rows reviewed | 51 |
| Pushbacks fired correctly | 33 |
| Pushbacks fired wrongly | 1 (LOW) |
| Pushbacks missed | 0 |
| Nudges fired / unjustified | 0 / 0 |

Re-runs of the four recorded faults are clean: brlaw_10 (pagamento + greve released on Q2/Q3, testemunhas withheld), usacc_01 (payhub_fees withheld; Q1 already computed the fee), usacc_06 (only noncompete_term, on a question that asked exactly about the covenant/consulting split), uslaw_09 (investigation withheld — but see finding U1 below: this time the model's Q4 arguably did ask).

## Findings

### Over-releases

| # | Case | Stem | Fact | Sev | Justification |
|---|---|---|---|---|---|
| O1 | brlaw_03_pejotizacao | 01-client | quem_decidia | HIGH (borderline) | Q5 asked only "quantos dias de férias gozados por ano, em que períodos, e foi assinado termo de férias/autonomia nesse gozo?"; the verbatim reply "Eu. Aprovava férias, cobrava horário, dava feedback. Igual aos CLTs" answers "who decided / subordination", which no question asked, and is a direct admission on the core vínculo issue (the model's own round-2 log calls it "admissão de subordinação"). 'férias' is a scripted trigger, so the keyword hit is real, but the question did not ask who approved vacations. |
| O2 | brlaw_05_divorcio_partilha | 01-client | carro_uso | LOW | Q9 asked only "a compra data de quando?"; the reply ("era da família, levava as crianças. Está no nome dela e o financiamento também") gives use and title, not the date. The controller's own reason concedes it "addresses only ... ownership and financing". |
| O3 | brlaw_08_ma_diligencia | 01-client | pjs | LOW | Q5 asked "O que aconteceu no 'caso Solaris'? Houve processo? Qual valor?"; the reply volunteers the 11 PJs' regime ("trabalham 9h-18h aqui, exclusivos, com gestor"). Low because the data room already said the 11 PJs have the "mesmo perfil" as Solaris. |
| O4 | uslaw_03_noncompete_memo | 01-client | counsel | HIGH | No question asked whether Zhao was represented by counsel or negotiated; Q6 asked only "Is Meridian incorporated in Texas? Are there any other signed Zhao documents...". The reply ("standard form; engineers sign the same day. Nobody negotiates") decides the §925(e) counsel exception; the model recorded "This removes the last doubt behind Assumption A2". |
| O5 | uslaw_03_noncompete_memo | 01-client | austin_trips | LOW | No question asked whether Zhao was ever physically in Texas; the 'Texas' hits are "under Texas law" (Q2) and "incorporated in Texas" (Q6). The model itself logged the answer as "(unsolicited, confirmatory)"; low because the file already placed him in Oakland. |

### Under-releases

| # | Case | Stem | Fact | Sev | Justification |
|---|---|---|---|---|---|
| U1 | uslaw_09_retaliation_termination | 01-client | investigation | HIGH (arguable) | Q4 "Documentation of the 9/12 complaint: who received the written complaint, who acknowledged it, any intake notes, and whether any interim measure was discussed" asks what happened with the complaint ('complaint' and 'September 12' are scripted triggers); the scripted reply "Honestly, nothing. Tom's been traveling" answers it. Withholding told the model the client had no information on the complaint's handling, which feeds the investigation-duty analysis. (Different from the recorded aborted-attempt fault, where the fact was attached to a question about an HR person outside Tom's chain.) |

### Silent-no-reply (new questions present, `send_response: false`)

All LOW: no scripted fact matched any of the new questions, so the only loss is the "client has no additional information" signal. Pattern: after the first exchange the controller defaulted to sending nothing, even though in usacc_04 01-client it correctly sent the bare no-information reply for a round with no matching fact.

| # | Case | Stem | New questions not answered |
|---|---|---|---|
| S1 | bracc_04_lucro_real_trimestre | 03-client | item 3 "Confirmar que o cliente postará o ajuste nos próprios livros (uma única vez)" |
| S2 | bracc_05_abertura_empresa | 02-client | "Q10–Q12 são novas" (Marina's income via PJ, Luana's hiring terms, locação-com-serviços hypothesis) |
| S3 | bracc_08_recuperacao_judicial | 02-client | "Novas perguntas para a Sessão 3" items 11–14 (União route decision, judicial sale of the UPI, discount rate, homologation date) |
| S4 | usacc_08_chapter11_debtor | 01-client | Q1–Q7 (the session's only question round; controller reason even says "the no-information reply keeps the stated assumptions" but nothing was sent; model later logged "remain open (no answers received)") |
| S5 | usacc_08_chapter11_debtor | 03-client | "Questions 8–12 are new with Session 2" |
| S6 | usacc_08_chapter11_debtor | 04-client | "Questions 13–15 are new with Session 3" (controller reason "re-saves the same open question list" is wrong) |
| S7 | usacc_10_fraud_indicators | 01-client | Q1–Q5 (the only question round) |
| S8 | uslaw_04_litigation_sequence | 03-client | Q9 (provenance of the demand quoted in Halvorsen's letter) |
| S9 | uslaw_04_litigation_sequence | 05-client | Q10 (Oct 6 call note: inbound copies, record completeness, former counsel/executed original) |
| S10 | uslaw_04_litigation_sequence | 08-client | Q11 (Oct 20 call note: author, participants, payout terms) |
| S11 | uslaw_07_chapter11_creditor | 02-client | "New unknowns created by the client's reply" 8–10, phrased as questions to the client (what else counsel said, did Redwood pause shipments, any payment timeline) |

Not counted: bracc_04 02-client (document request for the next month's package), brlaw_05 03-client and usacc_09 05-client (items framed as unknowns, not asked), usacc_05 03-client / usacc_06 03-client / uslaw_05 03-client (client follow-ups answered in place), all post-pushback and final-review re-saves.

### Session decisions

| # | Case | Stem | Pushback | Verdict | Sev | Justification |
|---|---|---|---|---|---|---|
| P1 | uslaw_02_msa_playbook | s1 | 0 | FIRED-WRONGLY | LOW | `when` = "if issues.json flags §9.3 (the gross negligence carve-out) as a problem". issues.json rank 2 lists clause "§9.1 / §9.3 / §10.1" but the flagged defect is that §9.3 *omits* the IP indemnity; redlines.md line 114 says "§9.3 GN/willful-misconduct/fraud carve-outs — Accept as offered". The GN carve-out was never flagged, so the false-premise challenge was unearned; impact low (model answered "the carve-out is not on the issues list" and no information leaked). |
| P2 | uslaw_04_litigation_sequence | s4 | 1 | OK-FIRED (note) | — | `when` = "session 4, if the memo says the position worsened"; the memo is mixed ("where the money is real, you are better off") but its verdict table marks Headline number, $862,000 target and Filing readiness "WORSENED", so the condition is met; controller flagged the ambiguity itself. |

All other 49 session rows: fired pushbacks match a quoted deliverable line (e.g. bracc_09 parecer "Não. Não há lucro"; brlaw_01 prazos.json `"prazo_em_dobro": false`; usacc_03 return.md "Loss allowed = 11,500; suspended carryforward = 16,500"; usacc_09 s1-after-pushback0 second refusal kept both reversals; uslaw_10 "Fiduciary claims: waived. Do not plead."), and every no-fire row either had only session-scoped pushbacks for other sessions or a condition the deliverable contradicts (bracc_05 "ITBI: não devido"; usacc_10 letter addressed to Dr. Patel, not Dr. Harlow). No nudge was requested and none was warranted (deliverables present in every snapshot). Out of scope: bracc_04 session 3 ended in `candidate_output_limit` before any decision; usacc_04 ran 2 of 12 sessions so its session-7 pushback was unreachable.

## Files
- Dump reviewed: `/tmp/claude-1026/-mnt-data-Projects-llm-non-coding-benchmark/47dc1c0c-79e0-4b28-87eb-f287b9b7e721/scratchpad/audit/b300-glm53-flash-full-20261024.json`
- Per-group working notes: `.../scratchpad/audit/dump/client_{bracc,brlaw,usacc,uslaw}.txt`, `.../scratchpad/audit/dump/session_{bracc,brlaw,usacc,uslaw}.md`
- Lane: `/mnt/data/Projects/llm-non-coding-benchmark/results/b300-glm53-flash-full-20261024/`

---

# Controller audit — lane `rtx5090-flash-next-full-20261024`

Scope: every client decision (118 rows, 38 cases) and every session decision (55 rows) in the dump; `_aborted/` ignored. Question text read in full (raw pending files used where the dump truncated). Deliverable snapshots (`s<N>-initial/`) opened for every fired pushback and for every unfired pushback whose `when` could apply to that session. Severity rule used: HIGH = the fact/pushback bears on the case's core trap or analysis AND the information was new to the model (not already in `workspace/documents/`); LOW otherwise.

## Summary

| Client decisions | Count |
|---|---|
| Client rows total | 118 |
| Rows with a release or a keyword over/under flag (reviewed fact-by-fact) | 61 |
| Fact releases total | 93 |
| Releases confirmed ASKED (keyword or clear paraphrase) | 85 |
| **Over-releases** | **8** (2 HIGH, 6 LOW) |
| Literal/keyword suggestions not released, confirmed NOT ASKED | all but 1 |
| **Under-releases** | **1** (LOW) |
| Rows with `send_response: false` | 74 |
| …confirmed as re-archives / no new client question | 65 |
| **SILENT-NO-REPLY (new client questions, nothing sent)** | **9** (all LOW) |

| Session decisions | Count |
|---|---|
| Session rows total | 55 |
| Pushbacks fired | 34 — all 34 conditions verified in the deliverable (0 fired wrongly) |
| Rows with no pushback | 21 — 0 missed (conditions checked against deliverables where applicable) |
| Nudges fired | 0 (none warranted) |

## Findings — client decisions

### Over-releases

| # | Case | Stem | Fact | Sev | Justification |
|---|---|---|---|---|---|
| 1 | brlaw_03_pejotizacao | 02-client | `quem_decidia` | **HIGH** | Round-2 Q3/Q4 ask only for records ("Férias gozadas/pagas … recibos, requisições, holerites"; "Controles de jornada … planilhas, escala, registros de acesso, logs"). The answer "Eu. Aprovava férias, cobrava horário, dava feedback. Igual aos CLTs" is a first-person subordination confession nobody asked for; the model then raised vínculo probability to "alta (85%–95%)" and called it "confessou" (parecer.md item 12.6). The controller itself declined to release on the near-identical round-1 questions, so the two decisions are also inconsistent. |
| 2 | uslaw_07_chapter11_creditor | 01-client | `terms` | **HIGH** | Controller cites Q2, but Q2 asks only "Any payments received Dec 10 – Mar 10 not in the ledger?"; no question asks why terms changed or about collection pressure. The January net-15 change was already in `terms_change_email.txt`, but "The February 27 wire — I told them no steel until it hit our account" is new pressure evidence that the model folded straight into the preference/ordinary-course analysis ("Demanded wires and partials are classic preference", advice_to_ceo.md). |
| 3 | bracc_04_lucro_real_trimestre | 01-client | `papel` | LOW | Q2 asks whether the EFD-Contribuições was transmitted with the 11,100 credit; it does not ask what NF-e 8812 was or why it was credited. The answer ("É papel e toner da sede. O fornecedor destacou PIS/COFINS, então creditamos") responds to an unasked question; low impact because `razao.csv` already labels NF 8812 "Material de uso e consumo" and the model had already decided the credit was improper. |
| 4 | brlaw_04_execucao_fiscal | 05-client | `impugnacao` | LOW | Controller's reason says "Q6 asks whether the assessment was ever administratively challenged" — it does not: Q6 asks whether Ana was cited on the redirection request and whether a decision exists; Q7 asks about Ana's post-2023 management. Keyword hits ("impugnar de imediato", "impugnação ao pedido") are false hits. Impact nil: the model noted the fact "já constava do resumo do PAF" (`paf_resumo_pagamentos.md`). |
| 5 | brlaw_07_credor_rj | 01-client | `essencial` | LOW | The model expressly wrote "(Não perguntamos sobre essencialidade das empilhadeiras: os documentos da pasta já tratam esses bens como essenciais)". Releasing the fact anyway let the model write "ESSENCIALIDADE CONFIRMADA PELO CLIENTE … torna certa a manutenção do impedimento" (estrategia.json). Core-trap topic, but `ficha_credor.md` already says "bens essenciais à operação da Atlas", so no new information. |
| 6 | brlaw_08_ma_diligencia | 01-client | `pjs` | LOW | Q4 asks whether the 3 labour suits were brought by PJs, whether there are other PJs and whether INSS/RFB has acted. The answer describes the working regime ("trabalham 9h-18h aqui, exclusivos, com gestor") — subordination facts not in the data room and not asked; model recorded "achado PJ agravado". |
| 7 | usacc_03_household_1040 | 01-client | `employer_coverage` | LOW | None of Q1–Q5 asks about health coverage or why the marketplace plan ended in June; the model itself logged it as a "Related confirmation received separately". Fact only confirmed the 6-month 8962 treatment already in the draft. |
| 8 | uslaw_08_sale_diligence_apa | 01-client | `hensley_relationship` | LOW | The only Hensley mention is inside Q5 about the shop-lease personal guarantee ("any Hensley-related friction are personal exposure"); nothing asks whether Ray has talked to Hensley or what the relationship is. The model then logged "Hensley consent status — ANSWERED" and built a seller-led consent approach on it. |

### Under-release

| # | Case | Stem | Fact | Sev | Justification |
|---|---|---|---|---|---|
| 9 | usacc_07_holding_qsbs | 01-client | `loans_terms` | LOW | Q5 asks squarely about the intercompany advances: "Were the $250,000 … $150,000 … advances ever repaid, offset …, or booked as contributions? … Is the Services→Digital $150,000 recorded on both sets of books, or only in the email?" The scripted answer "No paperwork. I just move money where it's needed" answers that and was withheld (not even a literal suggestion because "repaid" ≠ "repay"). Peripheral to the §1202 core. |

### SILENT-NO-REPLY (`send_response: false` despite new client questions)

| # | Case | Stem | Sev | New question(s) that went unanswered |
|---|---|---|---|---|
| 10 | bracc_09_distribuicao_lucros | 03-client | LOW | "Pergunta nova … **histórico de retiradas/distribuições 2021–2025** — valores por sócio, datas e escrituração de cada exercício." |
| 11 | brlaw_04_execucao_fiscal | 02-client | LOW (borderline) | New document request created by the released `opera` answer: "Enviar **cópias/números dos protocolos da Junta Comercial e da RFB** da alteração de endereço (março/2026)". |
| 12 | usacc_08_chapter11_debtor | 02-client | LOW | Eight "New questions needed to finish/verify Sessions 2–3" (April activity file, 4/14 comp order, Corbin fee application, confirmation/effective dates, GUC discount rate, $16.2M overlap, exit financing, NOL). The decision's own reason says "the no-information reply keeps the flagged unknowns" yet `send_response` is false — the reply was never sent. |
| 13 | usacc_08_chapter11_debtor | 03-client | LOW | New items 9–13 (Denver Water contract exposure, Mesa Q2 PO value and deposit terms, alternate steel quotes, authorise Mesa 3/18 payment, Dkt. 48 motion decision). |
| 14 | usacc_08_chapter11_debtor | 04-client | LOW | New "April MOR follow-ups" 1–6 (H&P payment date, April vendor itemisation, Corbin split, April payroll periods, Dkt. 83 copy, DIP interest/fees). |
| 15 | uslaw_04_litigation_sequence | 03-client | LOW | "New questions — Session 2" Q9–Q12: "**Which demand letter went out, when, and under whose name?** … Did the CEO or anyone else send a demand letter in ~September 2026?"; was the firm's revised letter sent; corporate directive copy; signature authority. |
| 16 | uslaw_04_litigation_sequence | 04-client | LOW | New Q13: "Has Pinecrest hired — or announced plans to hire — **any additional** Juniper personnel since June 2026?" |
| 17 | uslaw_04_litigation_sequence | 05-client | LOW | New Q14 (Session 3): written confirmation that the CEO accepts AAA arbitration and authorises/budgets the demand. |
| 18 | uslaw_04_litigation_sequence | 07-client | LOW | New Q15 (Session 5): settlement authority for the term sheet, walk-away floor, signatory. |

### Borderline calls reviewed and accepted as correct (for the record)
- bracc_02 01 `obra_pct` (P1/P5 on obras com materiais vs consultoria); bracc_08 01 `norte` (Q3 on the Norte arrears); bracc_07 01 `uso_proprio` (Q2 domicile asked; Campos/Cotia usage already in `relacao_imoveis.csv`); usacc_01 01 `denver` and uslaw_04 01 `feb11` (clear paraphrases, keyword-only flags); uslaw_10 01 `offer_timing` (fact merely repeats a date the model stated).
- Correctly withheld despite keyword hits: bracc_04 `luz` ("recibo de doação" false hit), bracc_06 `distribuicao`/`custo`, bracc_09 `deliberacao_2025`/`mutuo`, brlaw_01 `eletronico`, brlaw_03 01 `quem_decidia`, brlaw_08 `revelado`, usacc_01 `payhub_fees`, usacc_04 `gusto_dup` (model explicitly declined to ask), usacc_08 `counsel_told`, usacc_09 `side_letter_signed` (Q4 asks about returns since 12/23 and a written hold request, not whether the letter was countersigned), usacc_10 `who_to_tell`, uslaw_03 `austin_trips`, uslaw_04 `exhibit_c`, uslaw_08 `disclosed`.

## Findings — session decisions

No pushback fired wrongly and none was missed. Every one of the 34 fired pushbacks was checked against the snapshot (e.g. bracc_02 `comparativo.json` `mudanca_em_dezembro: "impossivel"`; brlaw_01 `prazos.json` `prazo_em_dobro: false`; brlaw_02 `clausulas.json` cl. 14 `aceitavel`; brlaw_04 s2 manifestação "não se opõe à correção do fundamento legal da multa", s4 defesa Tema 962; usacc_03 `loss_suspended: 16500`; usacc_07 opinion "Do not contribute it to Oakline Holdings"; usacc_09 pb1 after the second refusal in `response_to_ceo.md`; uslaw_02 issues.json rank 1 flags §9.1/§9.3/§10.1; uslaw_08 redline CHANGE on 4.12/7.4(c); uslaw_10 "fiduciary-duty claim … contractually eliminated").

Unfired rows: 18 were session-scoped pushbacks outside their session (bracc_04 s1/s2, bracc_08 s2/s3, brlaw_04 s1/s3/s5, usacc_04 s1–s4, usacc_08 s2/s3, uslaw_04 s1/s3/s5) or cases with no pushback (bracc_01, usacc_01); 3 were condition checks that correctly did not match:
- bracc_05 s1 — parecer.md §2.2 "Conclusão: ITBI não devido" (pushback requires "ITBI é devido").
- usacc_10 s1 — communication is `communication_to_dr_r_patel.md`, not addressed to Dr. Harlow.
- uslaw_04 s4 — strategy_memo.md "Plain answer: Juniper's position has IMPROVED since session 1" with a candour §3 "What worsened"; the `when` ("if the memo says the position worsened") is not met. Judgment call, but defensible on the memo's own headline.

Nudges: none fired; no session had incomplete deliverables that a nudge would have cured (bracc_04's BLOCKED status depends on books delivered in later sessions).

## Net assessment
Contamination risk in this lane is concentrated in two HIGH over-releases (brlaw_03 `quem_decidia`, uslaw_07 `terms`), both of which fed language and probability revisions in the model's final analysis but did not flip a conclusion. Six LOW over-releases added little or nothing new. One LOW under-release (usacc_07). The main systematic weakness is the controller treating any updated QUESTIONS file as a "re-save": 9 rounds with genuinely new client questions received no "client has no additional information" reply, 7 of them in the two multi-session cases usacc_08 and uslaw_04. Session/pushback handling was clean.

---

# Controller audit — lane `strix-flash-next-full-20261024`

Scope: 162 decision rows in the dump (108 client, 54 session), 32 cases through `uslaw_04_litigation_sequence` (lane still running; `_aborted/` ignored). Every released fact and every literal/under hint was judged against the actual question text; every fired pushback and every non-fired pushback whose `when` could apply was checked against the `s<N>-initial` deliverable.

## Summary

| Client decisions | Count |
|---|---|
| Client rows reviewed | 108 (62 with a release/over/under judgement; 71 `send_response=false` rounds compared with the prior round) |
| Facts released | 81 |
| Released facts confirmed ASKED (keyword or clear paraphrase) | 77 |
| Over-releases | 4 (1 HIGH, 3 LOW; one of the LOW is a redundant re-send of an already-released fact) |
| Under-releases | 1 (LOW; released one round later) |
| Literal hints correctly withheld (false hit / already answered) | 20 |
| Silent-no-reply rounds (new questions, nothing sent) | 10 rounds in 8 cases (all LOW) |

| Session decisions | Count |
|---|---|
| Session rows reviewed | 54 |
| Pushbacks fired | 28 — all 28 verified against the deliverable, condition matched |
| Pushbacks fired wrongly | 0 |
| Pushbacks missed | 0 (bracc_05 ITBI not due; usacc_04 s7 no restatement; usacc_10 addressed to Patel; uslaw_04 s4 says "improved") |
| Nudges | 0 fired; 1 debatable non-nudge (uslaw_02, see notes) |

## Findings

### Over-releases

1. **brlaw_07_credor_rj / 01-client / `essencial` — HIGH.** No question asks whether the forklifts/sorting system are essential; the eight questions ask RJ dates, updating math, chassis/serial identification ("marca, modelo, nº de chassi/série das 2 empilhadeiras"), duplicatas, documents, EPP proof and fiança. The controller's reason ("asks whether the forklifts and sorting system are essential") is not in the text. The answer ("coração do galpão… sem isso a Atlas para") is the fact that drives `retomada_dos_bens_agora=false` under art. 49 §3º and the scripted pushback; `estrategia.json` even cites "Essencialidade confirmada pelo cliente em 20/04".
2. **brlaw_05_divorcio_partilha / 01-client / `atibaia_reforma` — LOW.** No question mentions reforma/benfeitoria; Atibaia appears only in Q6 ("vender a casa de Atibaia" as a liquidity option). The answer handed the model a R$120k common-money improvement credit it never asked about (peripheral to the FGTS/quota trap).
3. **usacc_01_schedule_c / 01-client / `commute` — LOW.** Q3 asks about the 1,150 "other client errands (see pg 2)" miles; the fact answers about the separate ~1,200 Larkspur-office miles. Harmless in effect: the pre-release work response already excluded "Larkspur daily 1,200" as commuting.
4. **uslaw_04_litigation_sequence / 05-client / `padded` — LOW (redundant).** Re-sent a fact already released in round 01 as the "answer" to Q11 ("Has Pinecrest produced any audit findings on J-4533 since July 9?"), which it does not answer; no new contamination, model just noted "CEO repeats".

### Under-release

5. **usacc_01_schedule_c / 01-client / `payhub_fees` — LOW.** Q2 asks for the portal export "so I can confirm the gross-vs-deposit math" (trigger "gross vs"); withheld in round 1, then released in round 2 for the same question (Q5). Model had already inferred the 2.9% fee, so no analytical harm.

### Silent-no-reply (genuinely new questions, nothing sent back)

6. **bracc_02_escolha_regime / 02-client — LOW.** File has a section "Novas perguntas (rodada 2 — surgiram da resposta do cliente, não são repetição)" with Q6 (composition of the R$250k encargos / CPP deductibility, called "a pergunta mais importante do trabalho") and Q7 (payroll allocated to obras). Controller: "receipt log with no new question". No-info line only arrived in round 03.
7. **bracc_03_cbs_ibs_ano_teste / 02-client — LOW.** New item 5 "(novo, decorrente da resposta do cliente): confirmar que a versão rebaixada pelo TI será substituída…" is a new confirmation request; nothing sent.
8. **bracc_05_abertura_empresa / 02-client — LOW.** v2 adds follow-ups A.3 ("Os R$ 8.000 do dentista são estimativa ou já há proposta/contrato?"), B.4 ("Ela consegue pagar R$ 4.800… do próprio pró-labore?") and D.8 (IBGE conflict-of-interest rule); nothing sent.
9. **bracc_09_distribuicao_lucros / 03-client — LOW.** "Rodada 2 — ABERTA… novas perguntas de fato": Q7 (ECD history 2022–2024) and Q8 (2026 projection). Controller: "records the closed round-1 answers; nothing new is asked".
10. **bracc_09_distribuicao_lucros / 04-client — LOW.** Adds Q9 (balance sheet P+PL 10,610,000 vs declared 9,850,000, "Favor confirmar se há conta omitida"); again nothing sent, same wrong reason.
11. **brlaw_04_execucao_fiscal / 01-client — LOW.** First round, five fresh questions (DARF deduction, AIF content, documents, ciência, Rua das Pedras occupant); controller sent nothing because "no scripted fact applies" — protocol required the no-information reply.
12. **brlaw_04_execucao_fiscal / 02-client — LOW.** New Q6 "(Sessão 2) Teor da CDA substitutiva… Favor enviar a íntegra"; nothing sent. Reason also misstates the file ("records the no-information reply") when no reply had ever been sent; the model only got a no-info line in round 04.
13. **brlaw_08_ma_diligencia / 02-client — LOW.** New item 4 "IRPJ — estágio da discussão (ponto novo, aberto pela resposta dos sócios): a discordância… já está formalizada em impugnação?"; nothing sent.
14. **brlaw_10_cobranca_prescrita / 03-client — LOW.** Section "Pergunta NOVA e única… 7. Relatórios de serviço de fev/2021 e mar/2021: mande os dois documentos com data aposta na assinatura"; controller: "re-saves the closed questions; nothing new is asked". Bears on the prescription of P5–P6 but no scripted fact exists, so the only loss is the missing no-info line.
15. **uslaw_04_litigation_sequence / 03-client — LOW.** "New for Session 2 (client answer needed — do not assume)": Q9 (pre-Sept-29 demand letter), Q10 (was the Oct 26 demand sent), Q11 (audit findings). Controller recognised Q9 as new yet sent nothing; the no-info line came only in round 05.

### Session decisions — notes (no errors found)

- All 28 fired pushbacks matched: e.g. bracc_02 memorando "Mudar em dezembro é impossível"; bracc_04 s3 `compensacao_prejuizo` 204,644.70 = 30% of 682,149; brlaw_01 `prazo_em_dobro: false`; brlaw_02 clause 14 `aceitavel`; brlaw_04 s2 "não renova a nulidade quanto à multa"; brlaw_04 s4 "Tema 962… veda o pedido contra Ana Paula"; usacc_03 `loss_suspended 16500`; usacc_09 second refusal confirmed in the pushback-0 response ("'Book it' — declined"); uslaw_04 s2 advice "We abandoned tortious interference in Session 1" (dropping maintained, condition met in substance).
- Correct non-fires: bracc_05 `itbi.devido=false` (7.4% < 50%); usacc_04 s7 `open_items.md` "Prior closed books are not reopened"; usacc_10 report "To: Dr. R. Patel… Chair"; uslaw_04 s4 memo "Your position has improved — measurably".
- **uslaw_02_msa_playbook / s1 — observation.** Model returned an empty response (SSH reset); controller fired nothing and did not nudge, logging an infrastructure failure for the supervisor. Defensible, but the case ended `completed_ungraded` with no deliverable; a nudge/retry would have been the only way to obtain one.

### Borderline releases accepted as ASKED (listed for transparency, not counted as errors)

bracc_02 `obra_pct` (Q2 on the R$630k obras); bracc_06 `custo` (Q12/Q13 on the 600k cost basis); bracc_07 `marcos` (Q9 asks for grounds to disinherit Marcos; answer gives only the estrangement plus her directive); bracc_08 `norte` (Q6/Q13/Q14 on Norte payment/cut-off risk; answer is Norte's "sinal" demand); brlaw_02 `investimento` (Q5 "pretende trocar de sistema?"); brlaw_05 `carro_uso`/`guarda` (Q7/Q8 ask who pays the car and the current routine); brlaw_07 `banco` (Q8 on fiança/other guarantees); bracc_01 `estorno` withheld although Q4 uses the word "estornos" (question is about the 12-month CSV, fact is the May NF 1188 reversal — withholding judged correct but close).

Not a controller fault: `controller-observations.jsonl` note that bracc_02's round-2 file records a payroll split (1,050,000 / 250,000) the client never gave — grading evidence only.
