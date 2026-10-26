# STATUS

**COMPLETE WITH OPEN ITEMS** — atualizado 26/10/2026 (revisão pré-entrega concluída; nenhuma pergunta em aberto).

## Revisão pré-entrega (26/10) — correções de exatidão, sem mudança de números
- **Verificação integral re-rodada em Python**: verbas 2–7 = 665.584; provisão 682.152; HE 16.568,18/160.159,09; pior caso 943.580,69; cenário 12k 443.722,67; mixes 648.045/625.306; tabela de espera 102.322,80/219.994,02/355.315,92 — **todos conferem**. A divergência planilha (~160 h) × registradas (135 h) foi **re-derivada e confirmada** (159,8 h, +18,4%) — item 3 dos desconhecidos permanece aberto, inalterado.
- **16 correções** aplicadas (detalhe em parecer.md/parecer.json): (1) removida "planilha de R$ 850 mil" da notificação (§7.1) — **a notificação não indica valor**; substituída pelo teor real ("todas as verbas" desde 01/10/2019); (2) removida citação inventada atribuída ao arquivo do Tema 1.389 (§4.1.3) — virou regra metodológica própria; (3) citação do Tema 725 restaurada com "no caso concreto," (§4.1.2); (4) "e-mails de RH" → "aprovação de ausência pelo RH" (§4.1.3); (5) "registro de ponto em poder da reclamante" → registros estão no arquivo da própria empresa (§2); (6) fonte da fórmula de correção restrita a `stf_tema_1389_pejotizacao.md` (§7.1 — `verbas_e_calculo.md` não a contém); (7) datas de vencimento 20/12/2021 e 29/09/2022 marcadas **[não verificado]** (§5 — regra geral fora da biblioteca); (8) taxas de hora com precisão correta (81,8182/122,7273; 81,8182 @12k) e reflexo FGTS+40% de HE 2.210→2.216 (§6/§6.1); (9) mixes 85/15 e 75/25 com HE ponderada nas duas pontas (648.045/625.306 — alinhado ao §7) (§6.1); (10) `horas_extras` do JSON reescrito: ~160 h (≈19.612) implica ~24,8 h (≈3.044) acima das 135 h — não "19.600 não registrados"; (11–16) refs cruzados (§5→§6 na estimativa; acordo §6→§8), typos ("certainos", "a distance").
- **Nenhum número do caso central mudou** (70–80%; 665.584; 682.152; 500–700 mil). D-1 segue como única pendência.

## Nota 3 da diretoria (26/10) — "o STF já decidiu; suspenso = sem risco; por que provisionar?"
- Premissa **testada contra a biblioteca: não se sustenta**. Decisões existentes = repercussão geral + **suspensão nacional (14/04/2025)**; **mérito pendente** até out/2026 (`stf_tema_1389_pejotizacao.md`). Provável confusão com o Tema 725 (terceirização), que não afasta vínculo com requisitos do art. 3º presentes; notícia de "tese definitiva" seria pós-congelamento do acervo → **[não verificado]**, e ainda assim não apagaria o exame caso a caso dos fatos (§2).
- Incorporado a `parecer.md`: **§4.1** (o que o STF decidiu × o que falta) e **§7.1** (suspensão não altera o teste do CPC 25; custo de esperar — fórmula IPCA + SELIC−IPCA corre no sobrestamento: +102.322,80 a 1 ano, +219.994,02 a 2, +355.315,92 a 3 sobre 682.152, a 15% a.a. ilustrativos **[não verificado]**; aposta assimétrica — estorno é crédito em resultado, passivo tardio é redeclaração; suspensão como alavancagem do acordo pré-protocolo). Um item somado ao §0; nono fundamento no `parecer.json`.
- **Nenhum número mudou** (70–80%; exposição 665.584; provisão 682.152; acordo 500–700 mil). **Nenhuma pergunta nova** — a nota foi respondida por verificação de acervo, não por pergunta ao cliente; D-1 segue como única pendência.

## Rodada de fechamento — o que mudou
- Cliente confirmou **não possuir informação/documentação adicional** também sobre a Q-A (lastro da alegação "12k") → nenhuma pergunta permanece em aberto; **nenhum número muda** (exposição 665.584; provisão 682.152; acordo 500–700 mil), pois a presunção de base = valor pago à PJ segue sem prova em contrário.
- Consequência estratégica nova, registrada no parecer (§6.1/§8): a tese de "custos embutidos" é **não utilizável por ora** — recomendo **não** articulá-la em juízo/negociação (sem prova, não reduz nada e a frase do diretor funciona como confissão de posto permanente).
- Desconhecidos flagrados explicitamente na tabela abaixo; única pendência real é **D-1** (decisão de acordo antes de 16/11/2026), que não é informação e sim deliberação do cliente.

## Rodada 2 — o que mudou com a resposta do cliente
- Diretor respondeu à pergunta sobre o conteúdo dos R$ 18.000: *"CLT equivalente ganharia uns 12 mil"* → incorporado em `parecer.md` §6.1 como **alegação sem prova documental**: a presunção da biblioteca (base = valor pago à PJ, "salvo prova") **não** é desativada por asserção; caso central, exposição (R$ 665.584), provisão (R$ 682.152) e faixa de acordo (500–700 mil) **mantidos**.
- Cenário 12k quantificado como sensibilidade: total verbas **R$ 443.722,67** (−R$ 221.861,33); HE comprovada 11.045,45; reflexo mensal @12k ≈ 7.299. Só vira dinheiro com documentos (Q-A em QUESTIONS).
- Alerta registrado no parecer: a frase ajuda a empresa apenas no *quantum*, se provada; na *responsabilidade* ela **piora** (admite posto permanente de ~12 mil no quadro CLT).
- Demais perguntas: cliente **não tem informação adicional** → reclassificadas de "open items" para **desconhecidos confirmados** (não serão re-perguntados).

## Entregáveis (em `deliverable/`)
- `parecer.json` — números do caso central inalterados (probabilidade alta 70–80%; prescrição 58/26 meses; exposição R$ 665.584 + HE a apurar; provisão "provável" R$ 682.152; acordo 500–700 mil); fundamentos acrescidos da nota do cenário 12k e da nota 3 da diretoria (mérito pendente; suspensão ≠ sem risco).
- `parecer.md` — completo, com §6.1 (alegação do diretor), §0 e §§4.1/7.1 (nota 3 da diretoria), §6/§7/§8 atualizados; nenhuma súmula/OJ cancelada invocada.
- `QUESTIONS.md` — **encerrado** (duas rodadas): todas as perguntas respondidas ou negativas (Q-A: documentos da alegação 12k **não existem**); tabela de desconhecidos confirmados + deliberação D-1 (acordo) pendente de decisão.

## Premissas declaradas (inalteradas)
- Ajuizamento em **16/11/2026**; salários reputados pagos via NFs (84 × 18.000 = 1.044.000 conferido com o CSV) — `remuneracao_base` é base de cálculo, não débito novo; férias do período tratadas como não gozadas (simples, por determinação da biblioteca); nov/2021 prescrito (sensibilidade +10.948); dispensa sem justa causa no pior caso; jornada 220 h/mês (convenção); INSS 28% só sobre salários do período (sensibilidade +56.840).

## Desconhecidos confirmados (cliente não tem mais informação; tratado por sensibilidades, sem forçar reconciliação)
1. Nº de empregados da Solaris (>20?) — alcance da presunção de jornada da Súmula 338.
2. Gozo/pagamento efetivo das férias ("saldo de 20 dias") — potencial −116.000 se comprovado.
3. **Divergência não reconciliada**: planilha implica ~160 h extras em jan–jun/25 vs 135 h registradas (~18%) — deixada aberta; HE do período integral (até ~160.159) dependem de ponto pré-2025.
4. Quem decidiu o encerramento (notificação é do reclamante) — sensibilidade −70.504.
5. Prestação anterior a 01/10/2019 — não incluída.
6. Outros PJs no mesmo padrão — risco replicado ≈ 11 mil/mês por contrato, sem contagem.
7. Política de provisão/materialidade da controladoria — recomendação em absoluto.
8. Itens **[não verificados]** na biblioteca: compensação/dedução de valores pagos como PJ além da imputação salarial; ritual de homologação de transação; ordem de grandeza típica de custos de PJ (§6.1); regime FGTS 2026.

## Em aberto de fato
- **Nenhuma pergunta em aberto.** Q-A (documentos da alegação "12k") foi **encerrada em 26/10/2026 (rodada de fechamento)**: o cliente confirmou não possuir documentação adicional → a tese de custos embutidos é **não utilizável por ora** (presunção de 18k prevalece; recomenda-se não articulá-la — confissão embutida). Resta apenas **D-1**, deliberação do cliente sobre o acordo (decisão, não informação): faixa 500–700 mil antes de 16/11/2026.
