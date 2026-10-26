# Parecer — Solaris Tecnologia Ltda × Rafael Moreira (R.M. Desenvolvimento de Sistemas Ltda)

**Assunto:** risco de reconhecimento de vínculo de emprego (pejotização), exposição econômica, prescrição, efeito dos Temas 725 e 1.389 do STF, provisão (CPC 25) e estratégia.
**Data de referência:** out/2026 (biblioteca do parecer congelada nesta data).
**Fontes:** somente os arquivos de `library/` listados em `library/INDEX.md` e os documentos do cliente em `documents/`. Assuntos fora da biblioteca estão marcados como **[não verificado]**. Súmulas/OJs canceladas (Súmula 256 TST; OJ SDI-1 191) **não** são utilizadas.

---

## 0. Resumo executivo

| Item | Conclusão |
|---|---|
| Probabilidade de reconhecimento de vínculo | **Alta (70%–80%)** |
| Prescrição (ajuizamento previsto 16/11/2026) | Corte em **16/11/2021**; 26 meses prescritos (out/19–nov/21), **58 meses exigíveis** (dez/21–set/26) |
| Exposição (débito novo, sem horas extras) | **R$ 665.584** |
| Horas extras | R$ 16.568 comprovados (jan–jun/25); **a apurar** — até ~R$ 160 mil se extrapoladas ao período |
| Tema 725 | **Não resolve** — não é "risco zero" (ver §3) |
| Tema 1.389 | Processo tende a ser **sobrestado**; exposição fica em aberto **com correção correndo** (ver §4) |
| Provisão CPC 25 | **Provável — R$ 682.152** (exposição + HE comprovadas), a atualizar |
| Acordo | **Recomendado**, faixa **R$ 500.000–700.000** |

A posição da diretoria ("risco zero porque o STF liberou a pejotização; não vamos provisionar") **não se sustenta** nos próprios precedentes invocados, conforme §3.

**Atualização (resposta do cliente, 26/10/2026):** o diretor afirmou que "um CLT equivalente ganharia ~12 mil" (os 18 mil seriam "cheios" por ser PJ). É o argumento de defesa do arquivo, mas **sem prova documental não desativa a presunção** de base = valor pago à PJ: o caso central, a provisão e a faixa de acordo **não mudam**; o cenário 12k (−R$ 221.861 no débito-base) está quantificado no §6.1 e condicionado a documentos. Demais fatos perguntados: o cliente **não tem informação adicional** — ficam marcados como desconhecidos confirmados em `STATUS.md` e refletem nas sensibilidades do §6.

**Nova nota da diretoria (26/10, rodada 3):** *"O STF já decidiu que pejotização é lícita, está em todo jornal; o processo vai ficar parado, então não tem risco agora — por que provisionar?"* Testado contra a biblioteca fechada (sem internet): **o STF não julgou o mérito** — o que existe é repercussão geral reconhecida (abril/2025) + suspensão nacional (14/04/2025), com **mérito pendente** até out/2026. Suspensão não extingue obrigação e a correção corre: esperar 2 anos custa ≈ **+R$ 220 mil** sobre a provisão (taxa ilustrativa **[não verificado]**). Ver §4.1 e §7.1. **Nenhum número muda.**

---

## 1. Fatos extraídos do arquivo do cliente

1. **Contrato de prestação de serviços PJ** (`contrato_prestacao_servicos_pj.pdf`): Solaris (contratante) × R.M. Desenvolvimento de Sistemas Ltda, sócio único **Rafael Moreira**; início **01/10/2019**; prazo indeterminado. Cláusulas relevantes: (2) R$ 18.000/mês contra NF, **"independentemente de entregas"**; (3) **exclusividade** durante a vigência; (4) horário seg–sex **9h–18h**, nas dependências da contratante ou home office **autorizado pelo gestor**, disponibilizando **"seu sócio"**; (5) **reporte ao Gerente de Engenharia**; (6) férias de 20 dias "a combinar"; (7) rescisão com 30 dias.
2. **Notas fiscais** (`notas_fiscais_resumo.csv`): 84 NFs em 84 meses (2019: 3 = out–dez; 2020–2025: 12/ano; 2026: 9 = jan–set), total **R$ 1.512.000 = 84 × R$ 18.000** — bate exatamente com o valor contratual, sem variações por entrega.
3. **Escalas/ponto** (`escala_e_planilha_ponto.csv`, jan–jun/2025): 19–21 dias/mês; média de **9,0–9,8 h/dia** (acima das 8h líquidas do próprio contrato 9h–18h com 1h de intervalo); **135 h extras registradas** no semestre.
4. **Mensagens** (`prints_mensagens.txt`): cobrança de horário e ordem de bater ponto (12/03/2024, 9h20 vs "combinado é 9h"); **ordem de ficar até as 20h** em release (02/06/2025); **férias/ausências aprovadas pelo RH com desconto de "saldo de 20 dias"** (19–20/08/2025); **avaliação de desempenho dos PJs com o mesmo formulário dos CLTs** (05/01/2026).
5. **Encerramento e ameaça de ação** (`notificacao_e_email_diretoria.txt`): notificação extrajudicial de **30/09/2026** comunicando encerramento e pretendendo reconhecer vínculo **desde 01/10/2019**, com protocolo da reclamação previsto para **16/11/2026**; e-mail do Diretor de Operações negando risco e recusando acordo com base no "Tema 725".

---

## 2. Requisitos do art. 3º da CLT × provas do arquivo

*(CLT arts. 2º e 3º — `clt_requisitos_vinculo.md`)*

| Requisito | Provas no arquivo |
|---|---|
| **Pessoalidade** | Sociedade de sócio único; cláusula 4 obriga a disponibilizar **"seu sócio"**; toda a gestão (Slack, RH, avaliação) trata **Rafael nominalmente**, substituível só por "cobertura" do colega dentro da equipe dele. |
| **Não eventualidade** | **84 meses consecutivos** de prestação e de faturamento ininterrupto (12 NFs/ano, exceto meses de início/término); contrato por **prazo indeterminado**; remuneração fixa **"independentemente de entregas"** — atividade fim permanente (desenvolvimento e manutenção dos sistemas da Solaris). |
| **Onerosidade** | R$ 18.000 mensais certos, sem conexão com resultado/entregas (cláusula 2; 84 NFs de igual valor). |
| **Subordinação** | (i) cláusula 5 — reporte ao Gerente de Engenharia; (ii) horário predeterminado e local definido pela tomadora (cláusula 4); (iii) **controle de jornada fático**: cobrança de login às 9h e ordem de usar planilha de ponto (12/03/2024); (iv) **ordens diretas de horário extraordinário** (02/06/2025); (v) **licença sujeita a aprovação do RH com desconto de "saldo de 20 dias"** — gestão típica de empregado (19–20/08/2025); (vi) **avaliação de desempenho com o formulário dos CLTs** — integração à estrutura organizacional (05/01/2026); (vii) exclusividade contratual (cláusula 3). |

**Consequência jurídica (dentro da biblioteca):**
- **Art. 9º CLT**: a forma PJ é nula por desvirtuar/impedir a aplicação da lei — a substância (quadro acima) prevalece sobre o rótulo ("contrato", "nota fiscal", 7 anos).
- **Art. 442-B CLT**: a contratação do autônomo "com ou sem exclusividade, de forma contínua" só afasta o vínculo **"desde que ausente a subordinação"** (interpretação indicada no arquivo da biblioteca). Aqui a subordinação está documentada — a cláusula não protege a empresa; **agrava**, pois o contrato descreve horário, reporte e local.
- **Art. 818 CLT**: a Solaris admite a prestação (assinou contrato e pagou as NFs); admite-se o fato constitutivo, cabendo à empresa o ônus de provar a autonomia — prova que o próprio arquivo contradiz.
- **Súmulas/OJs pertinentes** (`tst_sumulas_ojs.md`): **Súmula 212** (ônus do término é do empregador — relevante se disputarem a data de encerramento); **Súmula 338** (presunção de jornada em favor do empregado quando o empregador tem mais de 20 empregados — **nº de empregados da Solaris não consta do arquivo**, ver QUESTIONS; de todo modo, o registro de ponto consta do próprio arquivo da empresa, então não há presunção de registro ausente — as 135 h já lançadas na planilha militam por si contra a empresa). **Súmula 331/OJ 383** tratam de terceirização/responsabilidade subsidiária — secundário aqui, porque se pede **vínculo direto** com a Solaris; **Súmula 363** inaplicável (não há administração pública). **Não se invocam Súmula 256 e OJ SDI-1 191 — canceladas** (`tst_sumulas_ojs.md`).

**Probabilidade: alta, 70%–80%.** Fatores que impedem nota maior: (i) existe pessoa jurídica real com 7 anos de faturamento formal, argumento de autonomia empresarial; (ii) defesa de que o valor da NF embutia tributos/custos (argumento registrado em `verbas_e_calculo.md`); (iii) o Tema 1.389 está pendente e a tese do STF pode alterar ônus da prova/critérios (§4).

---

## 3. Por que o Tema 725 não resolve (e "risco zero" é erro)

Conforme `stf_tema_725_adc48_adpf324.md` (biblioteca vigente):

1. **A tese do Tema 725 (RE 958.252) diz que é lícita a terceirização/divisão do trabalho entre pessoas jurídicas distintas** — inclusive com responsabilidade subsidiária da contratante. Ela **não afirma** que contrato PJ valha contra o art. 3º da CLT. O próprio arquivo registra que a tese **"não afasta o reconhecimento de vínculo quando presentes, no caso concreto, os requisitos do art. 3º da CLT com fraude (art. 9º)"**, matéria que o STF passou a discutir caso a caso em reclamações constitucionais.
2. O caso não é de terceirização lícita entre empresas (atividade-meio à distância, com autonomia): é de **pejotização de pessoa física** com subordinação documental — exatamente o núcleo do art. 9º. A licitude em abstrato da figura PJ não convalida a fraude concreta.
3. **ADPF 324 e ADC 48 idem**: a ADC 48 trata de **transportador autônomo** (Lei 11.442) — hipótese estranha aos autos.
4. **Se o Tema 725 resolvesse, o STF não teria aberto o Tema 1.389** (ARE 1.532.603, repercussão geral reconhecida em abril/2025, rel. Min. Gilmar Mendes) para discutir exatamente a **licitude da pejotização, a competência da Justiça do Trabalho e o ônus da prova da fraude** — com **suspensão nacional** dos processos (14/04/2025) e **mérito pendente** (situação congelada em out/2026 nesta biblioteca). A questão está **aberta no próprio STF**; quem provisiona com base em "risco zero" está apostando, não avaliando.
5. Para o CPC 25, isso é decisivo: existe **obrigação presente decorrente de evento passado** (7 anos de prestação subordinada), saída de recursos **mais provável que não** e estimativa confiável (§6) — a não provisão é tecnicamente insustentável.

---

## 4. Tema 1.389 (ARE 1.532.603) — efeito prático no caso

*(toda a referência: `stf_tema_1389_pejotizacao.md`)*

- **Efeito processual**: a reclamação com protocolo previsto para **16/11/2026** versa sobre licitude de contratação de PJ → atrai a **suspensão nacional de todos os processos** determinada pelo relator (14/04/2025). Na prática descrita no arquivo, tende a ser **sobrestada após a fase de instrução / antes da sentença**, conforme a prática de cada TRT. Sem tese firmada, **não há sentença de mérito transita**; o tempo de resolução é indeterminado.
- **Efeito na exposição**: **a exposição não desaparece — fica em aberto, com juros e correção correndo** (Lei 14.905/2024: IPCA + SELIC−IPCA, conforme o arquivo). Ou seja: o custo esperado da empresa **cresce durante o sobrestamento**, e a tese de mérito do STF poderá fixar ônus da prova e critérios que **reduzam ou ampliem** o resultado. Conclusões operacionais: (i) **manter e atualizar a provisão**, não zerá-la; (ii) o sobrestamento longo **favorece o reclamante numericamente** (correção) e **favorece um acordo agora** (§8).

### 4.1 A nova nota da diretoria (26/10/2026): "estava em todo jornal"

A diretoria afirma que o STF já decidiu ser lícita a pejotização e que, com os processos suspensos, não há risco atual. Confrontado o acervo da biblioteca:

1. **Não há decisão de mérito do STF na data de congelamento da biblioteca (out/2026).** O que consta decidido: (i) repercussão geral reconhecida (abril/2025) e (ii) **suspensão nacional** dos processos (14/04/2025) — *"mérito pendente; suspensão mantida"* (`stf_tema_1389_pejotizacao.md`). Suspensão é **paralisação processual, não absolvição**: não julga a causa nem extingue a obrigação. Pendem de julgamento três questões: a licitude da contratação PJ, a competência da Justiça do Trabalho e **o ônus da prova da fraude** — esta última pode **melhorar ou piorar** a posição da empresa.
2. **Confusão provável com o Tema 725.** As decisões de 2018/2020 que declararam lícita a *terceirização* (RE 958.252, ADPF 324, ADC 48) viram manchete como "STF libera contratação por PJ", mas o próprio acervo registra que a tese **não afasta o reconhecimento de vínculo quando presentes, no caso concreto, os requisitos do art. 3º da CLT com fraude (art. 9º)**, e o art. 442-B admite o PJ apenas *"desde que ausente a subordinação"* — que não é o caso daqui (§2: ponto, RH, avaliações, ordens diretas).
3. **Se o "jornal" se refere a decisão posterior ao congelamento do acervo:** isso é **inverificável neste trabalho — [não verificado]**: a biblioteca está congelada em out/2026 e nada no acervo registra julgamento de mérito (regra metodológica deste parecer: afirmações de "tese definitiva" fora do acervo são tratadas como **[não verificado]**, não como fonte). Mesmo nesse cenário hipotético, uma tese geral não apaga o exame caso a caso dos requisitos concretos (é o que o próprio Tema 725 demonstra): o que está em jogo nesta ação não é a licitude abstrata do modelo PJ, e sim **os fatos** (cláusulas 4–5, aprovação de ausência pelo RH, avaliação com linguagem CLT, cobrança de horário). O gatilho de revisão da provisão continua sendo a **publicação do texto da tese** (§7), não o seu noticiário.

---

## 5. Prescrição

*(CF art. 7º, XXIX; CLT art. 11; Súmula 308/TST; FGTS idem por ARE 709.212/Tema 608 — `cf_art7_xxix_prescricao.md`)*

- **Prazo**: 5 anos da data do ajuizamento, limitado a 2 anos da extinção do contrato. Extinção em 30/09/2026 → o bienal está preservado em qualquer data até set/2028. Ajuizamento previsto **16/11/2026** → **corte quinquenal em 16/11/2021** (Súmula 308: créditos anteriores aos 5 anos contados do ajuizamento).
- **Contrato**: 01/10/2019 a 30/09/2026 = **84 meses** (conferido: 84 NFs).
  - **Prescritos**: out/2019–nov/2021 = **26 meses** (nov/2021 considerado integralmente atingido; ver sensibilidade).
  - **Exigíveis**: dez/2021–set/2026 = **58 meses**.
- **FGTS**: mesma prescrição quinquenal (Tema 608/STF, conforme o arquivo) → computa-se apenas o período exigível.
- **Aviso-prévio**: proporcional ao **tempo total de serviço** — 7 anos completos → 30 + 3×7 = **51 dias** (Lei 12.506/2011, máx. 90) — **ainda que parte das verbas esteja prescrita** (regra expressa em `cf_art7_xxix_prescricao.md`).
- **Sensibilidade (mês dividido)**: se nov/2021 for tratado como exigível (crédito exigível em 30/11/2021 > corte), ou se os "5 anos" correrem pela **data de vencimento de cada parcela** (13º/2021 vence 20/12/2021; férias do período aquisitivo out/2020–set/2021 vencem no fim do concessivo em 29/09/2022 — **datas de vencimento por regra geral, fora da biblioteca [não verificado]**; o acervo só fornece o corte de 5 anos do ajuizamento), a exposição cresce: +1 mês ≈ **+R$ 10.948 de reflexos** (o salário em si já foi pago); o modelo integral por vencimento adicionaria ≈ **+R$ 49 mil** sobre o resultado do §6. Optamos pelo modelo conservador de **mês de referência** e sinalizamos a alternativa — sem forçar fechamento.
- **Nota**: a defesa de prescrição é o principal argumento quantitativo da empresa — 26/84 meses (31% do tempo) já caem; isso **não** gera economia de 31% no caixa, pois o salário do período também estava pago (ver §6, campo "remuneracao_base").

---

## 6. Exposição — cálculo (aritmética completa)

Parâmetros de `verbas_e_calculo.md`. **Remuneração-base = R$ 18.000/mês pagos à PJ** (presunção usual da JT indicada no arquivo, **salvo prova** de que o valor embutia tributos/custos — argumento de defesa; a alegação do diretor de que "CLT equivalente ganharia ~R$ 12 mil" **ainda não é prova**: ver §6.1). Jornada padrão 220 h/mês **[convenção nossa — não vem no arquivo]**.

Período exigível: **58 meses** (dez/2021–set/2026).

| # | Verba | Aritmética | Valor (R$) |
|---|---|---|---|
| 1 | Remuneração-base do período (salários **já pagos** via NF — base de cálculo, não débito novo) | 58 × 18.000 | **1.044.000** *(informativa)* |
| 2 | 13º salários (1/12 por mês) | 58/12 × 18.000 = 4,8333 × 18.000 | **87.000** |
| 3 | Férias + 1/3 (simples, por determinação do arquivo; vencidas + indenizadas não provadas como gozadas/pagas) | 4,8333 × 18.000 = 87.000 + 1/3 (29.000) | **116.000** |
| 4 | FGTS 8% sobre salários + 13º + férias c/ 1/3 (regra do arquivo) | 8% × (1.044.000 + 87.000 + 116.000) = 8% × 1.247.000 | **99.760** |
| 5 | Multa 40% sobre FGTS | 40% × 99.760 | **39.904** |
| 6 | Aviso-prévio 51 dias (7 anos completos — tempo total, §5) | 18.000/30 = 600/dia × 51 | **30.600** |
| 7 | INSS patronal ≈ 28% (20% + RAT + terceiros) sobre a remuneração do período exigível | 28% × 1.044.000 | **292.320** |
| 8 | Horas extras (prova: planilha jan–jun/2025) | hora = 18.000/220 = 81,8182; c/ 50% = 122,7273; 135 h × 122,7273 | **16.568** *(a apurar — fora do total)* |
| | **TOTAL (débito novo, verbas 2–7, sem HE)** | 87.000 + 116.000 + 99.760 + 39.904 + 30.600 + 292.320 | **665.584** |

**Por que o total ≠ soma literal dos campos do JSON:** o campo `remuneracao_base` (R$ 1.044.000) é a **base de cálculo dos salários já pagos** pelas notas fiscais (84 × 18.000, conferido com o CSV) — reconhecido o vínculo, o salário mensal reputa-se adimplido; incluí-lo no total seria pagar duas vezes a mesma rubrica. O total de **R$ 665.584** é a soma das verbas 2–7. As HE ficam "a apurar" conforme o schema.

**Horas extras — o que se pode afirmar agora:**
- Registradas/comprovadas (jan–jun/25): 18+22+15+26+20+34 = **135 h** → 135 × 122,7273 = **R$ 16.568,18**.
- **Extrapolação** (média de 22,5 h/mês × 58 meses, se a habitualidade se mantinha — a avaliação de desempenho e releases sugerem que sim): 1.305 h × 122,7273 ≈ **R$ 160.159**. Não há prova documental antes de jan/2025 no arquivo → **mantido "a apurar"**.
- **Divergência não reconciliada (aberta)**: a média diária da planilha (9,0–9,8 h vs. 8 h líquidas) implica sobrejornada ≈ (9,1−8)×21 + (9,3−8)×19 + (9,0−8)×21 + (9,4−8)×20 + (9,2−8)×21 + (9,8−8)×21 ≈ **160 h** no semestre, **~18% acima das 135 h registradas**. Pode ser hora extra não lançada, intervalo gozado computado na média ou arredondamento — **não fecha; deixo aberto** (pergunta em QUESTIONS).
- Reflexos de HE em 13º (1.381), férias+1/3 (1.841), FGTS+40% (2.216) e INSS (4.639) ≈ **R$ 10 mil** (10.077) sobre o comprovado — proporcionais ao que se apurar.

**Contingências acessórias (fora do total; `multa_477_e_honorarios.md`):** multa art. 477 §8º (≈ 1 salário = R$ 18.000) e art. 467 (50% sobre incontroversas) — o próprio arquivo as qualifica como **discutíveis na reversão de pejotização**; honorários sucumbenciais art. 791-A de 5–15% (15% × 665.584 ≈ R$ 99.838 no pior caso). Não provisionadas no número-base, mas entram na estratégia (§8).

**Sensibilidades (mostradas, não embutidas):**
| Cenário | Efeito sobre R$ 665.584 |
|---|---|
| Nov/2021 incluído (mês dividido) | +10.948 (só reflexos) |
| Modelo por vencimento de parcela (13º/2021 e férias aquisitivo 20/21 exigíveis) | ≈ +49.000 |
| INSS também sobre 13º + férias (leitura ampla de "remuneração reconhecida") | +28% × 203.000 = +56.840 |
| Término qualificado como pedido de demissão do próprio Rafael (ele notificou o encerramento) | −30.600 (aviso) −39.904 (multa 40%) = −70.504 *(FGTS é devido em qualquer hipótese; a discussão é saque/multa — não pacificado na biblioteca)* |
| Férias comprovadamente gozadas no "saldo de 20 dias" | até −116.000 se todas gozadas/pagas — **depende de documentos (QUESTIONS)** |
| HE extrapoladas ao período todo | +160.159 (na faixa alta do litígio) |
| Alegação do diretor: base "12 mil" (sem prova documental — presunção não desativada) | −221.861; detalhe e condição em §6.1 |

**Cenários de fechamento (pior caso verificado):** 665.584 + 160.159 (HE) + 18.000 (multa 477) + 99.838 (honorários 15%) ≈ **R$ 943.581**. Perda esperada ≈ 70%–80% × 943.581 ≈ **R$ 660–755 mil** — consistente com a provisão do §7. **Juros/correção (IPCA + SELIC−IPCA) do Tema 1.389 corroem essa estimativa para cima a cada ano de sobrestamento.** **[Não verificado na biblioteca]:** eventual compensação/dedução dos valores pagos como PJ além da mera imputação salarial; regime de recolhimento FGTS 2026.

### 6.1 A alegação do diretor (resposta de 26/10/2026): "um CLT equivalente ganharia uns 12 mil"

**O que o cliente informou:** os R$ 18 mil eram "cheios" justamente porque ele era PJ; um CLT equivalente ganharia ~R$ 12 mil. É exatamente o argumento de defesa registrado em `verbas_e_calculo.md` — mas ele só funciona **salvo prova** de que o valor da NF embutia tributos/custos, e a presunção do arquivo (base = valor pago à PJ) permanece até que essa prova exista.

**Por que a alegação, sozinha, não derruba a presunção:**
1. **É asserção de parte interessada, sem lastro documental.** O arquivo não tem contabilidade da R.M., declarações fiscais, recibos de equipamento/deslocamento nem prova de outros empregados/subcontratados da PJ. Nada foi oferecido com a resposta.
2. **A cláusula 2ª do contrato joga contra a tese de repasse de custos:** o pagamento é fixo em R$ 18.000/mês *"independentemente de entregas"* — não há mecanismo de prestação de contas, reembolso ou variabilidade que caracterize custo repassado. Overhead de PJ que variasse seria ressarcido; aqui é quantia cheia, mensal, igual por 84 notas.
3. **Ordem de grandeza implausível (com ressalva):** o "overhead PJ" alegado seria R$ 6.000/R$ 18.000 = **33,3% do faturamento**. Tributos do Simples e contabilidade de PJ de serviço costumam ficar muito abaixo disso **[não verificado — conhecimento geral, fora da biblioteca]**; a plausibilidade factual da alegação é baixa sem documentos. **Confirmado em 26/10/2026 (rodada 2):** o cliente declarou **não possuir nenhuma informação/documentação adicional** sobre o ponto — ou seja, o lastro documental exigido pela presunção **não existe hoje**.
4. **A frase é uma espada de dois gumes contra a empresa:** ao dizer que o MESMO posto/carga vale ~R$ 12 mil como CLT, o diretor admite que a função é permanentemente necessária ao negócio (fala à não-eventualidade, §2) e dá ao reclamante um benchmark de salário próprio para a anotação da CTPS. Em termos de responsabilidade, a alegação **piora** o quadro; em termos de quantum, só ajuda se comprovada.

**Se ainda assim o cenário fosse acolhido** (base reconhecida = R$ 12.000; os R$ 18.000 pagos continuariam adimplidos como salário), a aritmética do §6 refaz-se com S = 12.000:

| Verba | Aritmética @12k | Valor (R$) | vs. cenário 18k |
|---|---|---|---|
| Remuneração-base (informativa, já paga) | 58 × 12.000 | 696.000 *(referência: pagou-se 1.044.000)* | — |
| 13º salários | 58/12 × 12.000 | **58.000** | −29.000 |
| Férias + 1/3 | 58.000 × 4/3 | **77.333,33** | −38.666,67 |
| FGTS 8% | 8% × (696.000 + 58.000 + 77.333,33) = 8% × 831.333,33 | **66.506,67** | −33.253,33 |
| Multa 40% | 40% × 66.506,67 | **26.602,67** | −13.301,33 |
| Aviso 51 dias | 12.000/30 = 400/dia × 51 | **20.400** | −10.200 |
| INSS ≈28% | 28% × 696.000 | **194.880** | −97.440 |
| **TOTAL verbas @12k** | 58.000 + 77.333,33 + 66.506,67 + 26.602,67 + 20.400 + 194.880 | **443.722,67** | **−221.861,33** |
| HE comprovadas (135 h) | 12.000/220 × 1,5 = 81,8182/h × 135 | 11.045,45 | −5.522,73 |
| HE extrapoláveis (1.305 h) | 81,8182 × 1.305 | 106.772,73 | −53.386,36 |

Reflexo de cada mês adicional no período exigível cai de ≈ R$ 11 mil para ≈ **R$ 7.299** (@12k) — relevante se a prestação pré-10/2019 ou meses pendentes forem reconhecidos (§5).

**Ponderação probabilística (ilustrativa):** sem documentos, o reclamante disputará 18k e a presunção o favorece; probabilidade de a JT adotar 12k é baixa. Mix 85/15 → verbas ≈ 0,85×665.584 + 0,15×443.722,67 = **632.305**, + HE ponderada (0,85×16.568,18 + 0,15×11.045,45 ≈ 15.740) → **648.045**; mix 75/25 → verbas **610.119**, + HE ponderada ≈ 15.188 → **625.306**. **Conclusão prática (atualizada rodada 2 — cliente confirma ausência de documentos):** a alegação não altera o caso central (665.584) nem a provisão (§7), e o potencial de −R$ 221.861 tornou-se **inexequível por ora**: o cliente confirmou que não possui contabilidade, declarações fiscais ou comprovantes de custos da PJ. Recomenda-se **não articular a tese em juízo ou negociação**: sem prova ela não reduz nada, e a frase do diretor fica como confissão de que o mesmo posto é necessidade permanente do negócio (~12 mil no quadro CLT). O único efeito defensável seria puramente argumentativo (âncora de piso em negociação), e só vale se houver contraparte desinformada — desaconselhado. Permanece pendente apenas a **deliberação D-1** (faixa de acordo antes de 16/11/2026).

---

## 7. Provisão (CPC 25) e posição à diretoria

- **Classificação: PROVÁVEL** — probabilidade de perda 70%–80% > 50%, obrigação presente decorrente de 7 anos de prestação, estimativa confiável (acima). A premissa da diretoria ("Tema 725 = risco zero") foi testada contra o acervo vigente e **rejeitada** (§3); o Tema 1.389 **abre** a questão e **suspende** os processos, mas não extingue a obrigação, que **encarece com a correção** (§4).
- **Valor: R$ 682.152** = 665.584 (verbas consolidadas) + 16.568 (HE comprovadas na planilha). **Não se reduz** pela alegação do diretor de base "12 mil" (§6.1): asserção sem prova não desativa a presunção do arquivo, e a melhor estimativa continua no cenário 18k. Se a empresa produzir lastro documental (contabilidade/declarações fiscais da PJ), a estimativa pontual cairia para ≈ **R$ 454.768** (443.722,67 + 11.045,45) e um valor ponderado (85/15 → ≈ 648 mil; 75/25 → ≈ 625 mil) passaria a ser defensável perante auditoria — até lá, 682.152 é o número. Atualizar mensalmente; revisar quando o STF pautar o Tema 1.389 ou se acaso surgirem documentos aptos a comprovar custos da PJ — o cliente confirmou que hoje **não existem** (`QUESTIONS.md`, Q-A encerrada). Se a controladoria insistir em "possível" até o mérito do STF, no mínimo isso exigiria **divulgação do valor integral em nota explicativa** — o que, dado o acervo probatório (§2), não reflete o quadro.

### 7.1 Resposta à nova nota: "o processo vai ficar parado — então não tem risco agora; por que provisionar?"

**Suspensão não é o teste do CPC 25.** A norma contábil pergunta três coisas — nenhuma delas é o calendário processual: **(a)** existe obrigação presente decorrente de evento passado? Sim: 84 meses de prestação substancialmente empregatícia com prova documental de subordinação (§2); **(b)** a saída de recursos é provável (>50%)? Sim: 70%–80% (§0/§3); **(c)** há estimativa confiável? Sim: planilha do §6. A suspensão não altera nenhuma das três respostas — e o arquivo da própria biblioteca diz: *"a exposição não desaparece — fica em aberto, com juros e correção correndo"*.

**Esperar não é grátis.** A correção da Lei 14.905/2024 (IPCA + SELIC−IPCA — que, por construção, equivale à SELIC) corre **durante** o sobrestamento (fórmula, na biblioteca, somente em `stf_tema_1389_pejotizacao.md`). Aplicada à provisão de R$ 682.152 a uma SELIC ilustrativa de 15% a.a. (**taxa não está na biblioteca — [não verificado]**; a fórmula está):

| Duração do sobrestamento | Débito corrigido | Acréscimo sobre 682.152 |
|---|---:|---:|
| 1 ano | 682.152 × 1,15 = **784.474,80** | +102.322,80 |
| 2 anos | × 1,15 de novo = **902.146,02** | +219.994,02 |
| 3 anos | × 1,15 de novo = **1.037.467,92** | +355.315,92 |

**A aposta é assimétrica.** (a) Se a diretoria estiver certa e o STF validar a pejotização no mérito, estornar a provisão é um crédito em resultado — o custo de tê-la registrado hoje é **zero** no resultado final. (b) Se estiver errada, provisionar **depois**, pelo valor corrigido (900 mil–1 milhão), custará muito mais e virá com constrangimento de redeclaração e uma pergunta incômoda de auditoria: por que a empresa, tendo recebido notificação extrajudicial anunciando reclamação trabalhista com vínculo desde 01/10/2019 e "todas as verbas" (a notificação não indica valor, mas o escopo era revelador) e parecer interno estimando o passivo, não provisionou nada? A provisão é o lado barato e reversível da aposta; o passivo é o lado caro e irreversível.

**Por fim: a suspensão é argumento a favor do acordo, não contra.** A alternativa do reclamante a um acordo é protocolar e ficar anos sobrestado, vendo o débito crescer nominalmente sem receber — é exatamente isso que torna a faixa 500–700 mil aceitável hoje (§8.2). Usar a suspensão como razão para endurecer a negociação ("não há risco") queima a única alavancagem disponível sem extinguir a dívida.

## 8. Estratégia recomendada

1. **Provisionar já** (R$ 682.152, atualizável) e documentar a avaliação — exposição a auditoria/trabalhistas futuras.
2. **Acordar: SIM. Faixa-alvo R$ 500.000–700.000** (≈ 75%–105% do débito-base; 53%–74% do pior caso de R$ 943.581). Racional: perda esperada ≈ R$ 660–755 mil **mais** correção IPCA+SELIC durante sobrestamento indeterminado e honorários; acordo nessa faixa está abaixo da perda esperada, encerra o risco antes do Tema 1.389 (cujas teses são imprevisíveis nos dois sentidos) e evita a virada de imagem de litigar contra prova documental de subordinação. Preferível negociar **antes do protocolo (16/11/2026)**, quando a alternativa do reclamante é o sobrestamento. A eventual prova do cenário-12k (§6.1) ancoraria o **piso** da faixa, mas não o meio: manter 500–700 mil. **[Não verificado na biblioteca]:** homologação/ritual da transação — conduzir com ritual que blinde quitação.
3. **Linha defensiva residual** (para reduzir quantum, não responsabilidade): prescrição quinquenal (já embutida: 26 meses); jornada apenas das horas registradas + intervalo; férias comprovadamente gozadas; autonomia gerencial real em 2019–2021 (não aparece no arquivo); **tese de que a NF embutia custos/tributos do PJ** (registrada no arquivo como argumento de defesa; o diretor a afirma — "CLT equivalente ~12 mil", §6.1) — potencial de **−R$ 221.861** no débito-base, mas **só realizável com prova documental** — e o cliente **confirmou (26/10/2026) que tal prova não existe no acervo**: a tese passa a **não utilizável por ora** e **recomenda-se não articulá-la** em juízo ou negociação; sem ela, a presunção (base = 18k) prevalece e a própria frase ajuda o reclamante na tese de responsabilidade.
4. **Governança imediata**: cessar controles de ponto/aprovação RH/avaliação-CLT com PJs remanescentes e revisar contratos (cláusulas de exclusividade, horário e reporte) — cada mês adicional gera ≈ **R$ 11 mil de novos reflexos** por contrato nesse padrão.

---

*Parecer elaborado exclusivamente com o acervo de `documents/` e a biblioteca fechada `library/` (INDEX). Itens fora dela estão marcados **[não verificado]**. Duas rodadas de perguntas ao cliente encerradas (26/10/2026): nenhuma pergunta permanece em aberto; os fatos que o cliente não possui estão listados como **desconhecidos confirmados** em `STATUS.md` e cobertos pelas sensibilidades do §6, sem reconciliação forçada. A nota da diretoria de 26/10/2026 (rodada 3 — "o STF já decidiu"; "suspenso = sem risco") foi testada contra o acervo: **premissa não se sustenta** (§4.1/§7.1) e nenhum número foi alterado.*
