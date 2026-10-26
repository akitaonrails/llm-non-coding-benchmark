# Parecer — Solaris Tecnologia Ltda × Rafael Moreira (R.M. Desenvolvimento de Sistemas Ltda)

**Assunto:** risco de reconhecimento de vínculo empregatício ("pejotização") e exposição estimada.
**Data:** 26/10/2026. **Premissa de calendário:** ajuizamento anunciado para **16/11/2026** (notificação extrajudicial de 30/09/2026).
**Autoridade:** somente a biblioteca fechada (`library/INDEX.md`). O que não estiver nela está marcado como *premissa não verificada*.

---

## 1. Resumo executivo

A diretoria está errada: **o Tema 725 não gera "risco zero"**. A tese do STF cuida da *licitude da terceirização entre pessoas jurídicas* e expressamente **não impede** o reconhecimento de vínculo quando, no caso concreto, estão presentes os requisitos do art. 3º da CLT com fraude ao art. 9º (stf_tema_725_adc48_adpf324.md). Aqui o contrato e as provas de chat **documentam subordinação, horário, exclusividade e pagamento fixo mensal "independentemente de entregas"** — exatamente o cenário do **Tema 1.389 (ARE 1.532.603)**, cujo mérito está **pendente com suspensão nacional** na data desta biblioteca (out/2026).

- Probabilidade de reconhecimento de vínculo: **alta (80–90%)**.
- Exposição estimada (sem horas extras, ver §6): **R$ 728.388** na base integral de R$ 18 mil (presunção da biblioteca) — ou **R$ 485.592** se o Judiciário aceitar a tese defensiva de base R$ 12 mil (argumento do diretor; *sem prova documental no arquivo*, ver §6.1). **Melhor estimativa ponderada: ~R$ 655,5 mil.**
- A favor da Solaris há apenas dois atenuantes relevantes: **prescrição quinquenal** (corta 25,5 dos 84 meses) e o **sobrestamento** pelo Tema 1.389 (ganho de tempo, não de mérito; correção segue correndo).
- Recomendação: **reclassificar de "remoto" para "provável" e provisionar ~R$ 655,5 mil** (melhor estimativa entre os dois cenários de base; CPC 25 conforme classificação exigida no schema do contrato — o texto do CPC não integra a biblioteca), e **tentar acordo na faixa de R$ 270–480 mil**.

> Nota de método: este parecer **não cita** a Súmula 256 nem a OJ SDI-1 nº 191 como vigentes — ambas foram **canceladas** (Súmula 256 pela Res. 121/2003; OJ 191 cancelada/convertida — "dono da obra") e usá-las seria erro (tst_sumulas_ojs.md).

---

## 2. Requisitos do art. 3º da CLT × provas do arquivo

Art. 3º (clt_requisitos_vinculo.md): empregado é a **pessoa física** que presta serviço de natureza **não eventual**, **sob dependência** (subordinação) e mediante **salário**; a doutrina/TST soma **pessoalidade**. A prestação foi admitida pela própria contratante → art. 818 + Súmula 212 (tst_sumulas_ojs.md): o ônus de provar autonomia é da Solaris.

| Requisito | Provas no arquivo |
|---|---|
| **Não eventualidade** | Contrato de **prazo indeterminado** (cláusula 7ª) vigente de 01/10/2019 a 30/09/2026; **87 notas fiscais** em 7 anos seguidos (notas_fiscais_resumo.csv: 2019: 3 NFs/R$ 54 mil; 2020–2025: 12 NFs/R$ 216 mil cada ano; 2026: 9 NFs/R$ 162 mil); remuneração "independentemente de entregas" (cláusula 2ª) — continuidade estrutural, não excepcionalidade |
| **Subordinação** | Cláusula 5ª: "reportar-se-á ao **Gerente de Engenharia**" (linha hierárquica); cláusula 4ª: **horário 9h–18h, seg–sex**, nas dependências da contratante ou home office "**autorizado pelo gestor**"; provas materiais: Slack 12/03/2024 — gerente cobra pontualidade ("o combinado é 9h") e **manda marcar planilha de ponto**; DM 02/06/2025 — ordem de ficar até as 20h ("release"); DM 19/08/2025 — folga só "se o Pedro cobrir" e "pedido por e-mail **pro RH aprovar**"; e-mail RH 20/08/2025 — **aprovação de ausência** e desconto de "saldo de 20 dias"; Slack 05/01/2026 — **avaliação de desempenho com o mesmo formulário dos CLTs** (integração funcional) |
| **Onerosidade** | R$ 18.000,00 **fixos mensais** contra NF (cláusula 2ª; 100% das NFs em valor único) |
| **Pessoalidade** | Sócio único nominal: "a CONTRATADA **disponibilizará seu sócio**" (cláusula 4ª); um único CPF por trás da PJ (R.M. Desenvolvimento Ltda, sócio único Rafael Moreira); exclusividade contratual (cláusula 3ª) impedindo prestar serviços a terceiros |

**Art. 442-B não salva:** no entendimento registrado na própria biblioteca, o contrato de autônomo afasta a qualidade de empregado "**desde que ausente a subordinação**" (clt_requisitos_vinculo.md). A subordinação aqui é documental e nasce do próprio contrato. **Art. 9º:** o desenho contratual (PJ unipessoal + exclusividade + horário + reporte + pagamento fixo sem entregas) é o exemplo clássico de ato nulo que desvirtua a CLT.

**Outras súmulas da biblioteca:**
- **Súmula 331** (tst_sumulas_ojs.md): trata de terceirização e responsabilidade subsidiária da tomadora — não legitima pejotização pessoal subordinada; na pior hipótese para o reclamante, restaria a responsabilização da Solaris como tomadora.
- **Súmula 338**: presunção de jornada para empregador com **mais de 20 empregados** — porte da Solaris não consta do arquivo (pergunta em `QUESTIONS.md`); como há planilha de ponto mandada preencher (12/03/2024), a discussão de ônus probatório de horas extras tende a favorecer o reclamante.
- **Súmula 363**: inaplicável (nenhum ente público envolvido).
- **OJ 383 SDI-1**: se houver CLTs em função equiparável, cabe isonomia salarial — risco adicional não quantificado (falta demonstrativo de salários internos; perguntado).

---

## 3. Por que o Tema 725 **não resolve**

A tese fixada no RE 958.252: *"é lícita a terceirização ou qualquer outra forma de divisão do trabalho entre pessoas jurídicas distintas... mantida a responsabilidade subsidiária da contratante"* (stf_tema_725_adc48_adpf324.md). Três razões pelas quais o e-mail do Diretor de Operações está errado:

1. **Objeto diverso.** O tema protege a *divisão de trabalho entre duas pessoas jurídicas reais* (atividades-fim inclusive). Não autoriza **simular** vínculo de pessoa física: a própria biblioteca registra que a tese "**não afasta o reconhecimento de vínculo quando presentes, no caso concreto, os requisitos do art. 3º da CLT com fraude (art. 9º)**".
2. **O contrato admite a fraude.** A cláusula 2ª (pagamento fixo "independentemente de entregas") + exclusividade + horário + reporte ao gerente transformam a PJ em luva de RPG sobre um empregado — não em contratação empresarial de resultados. ADPF 324/ADC 48 protegem modelos de *terceirização/autêntico autônomo*, não a subordinação pessoal documentada.
3. **Quem decide pejotização é o Tema 1.389** — e ele está **pendente**, com suspensão nacional (ver §4). Se o STF firmar tese em termos gerais de licitude *condicionada à ausência de subordinação*, o caso continua perdendo nos fatos; se firmar ônus da prova pró-trabalhador, piora.

---

## 4. Tema 1.389 (ARE 1.532.603/DF, rel. Min. Gilmar Mendes)

- Repercussão geral reconhecida (abr/2025) sobre: licitude da contratação de PJ/autônomo (pejotização), competência da Justiça do Trabalho e **ônus da prova da fraude**; **suspensão nacional de todos os processos** sobre licitude de contratação de PJ/autônomo desde **14/04/2025** (stf_tema_1389_pejotizacao.md).
- **Situação na biblioteca (congelada em out/2026): mérito pendente, suspensão mantida.** Nada neste arquivo autoriza assumir julgamento favorável.
- **Efeito processual prático:** a reclamação protocolada em 16/11/2026 tende a ser **sobrestada após a instrução / antes da sentença**, conforme a prática de cada TRT. O processo congela; não se extingue.
- **Efeito sobre a exposição:** o passivo **continua existindo e corrigindo** (Lei 14.905/2024: IPCA + SELIC−IPCA, conforme a mesma biblioteca). O corte prescricional congela na data do ajuizamento, mas a espera é paga. A tese de mérito pode redesenhar ônus da prova e critérios — vetor de **dois lados**, o que recomenda provisionar hoje e reavaliar no julgamento.

### 4.1 Resposta direta às alegações da diretoria ("o STF já decidiu, está em todo jornal" / "processo parado = sem risco")

**(a) A "decisão do STF" não existe na base documental deste parecer — premissa não verificada (definitiva, rodada 2).** Na bibliografia fechada que fundamenta este trabalho (congelada em out/2026), o mérito do Tema 1.389 está **pendente** (a biblioteca registra apenas o reconhecimento da repercussão geral, sem número de tema autônomo para essa decisão — "Tema 1.388" seria premissa não verificada, não citável aqui) e a suspensão segue mantida. Não há nos autos fornecidos inteiro teor, verbete ou tese publicada. Reportagem de jornal não é fonte verificável: manchete pode resumir julgamento incompleto, embargos pendentes ou outro tema. **Rodada 2 de perguntas (26/10/2026): o cliente confirmou que não possui o inteiro teor nem qualquer documento oficial da alegada decisão (QUESTIONS.md, item 9 — sem resposta).** A alegação fica, portanto, sinalizada como **desconhecido nº 6** no §8 e **não pode fundamentar redução da provisão sem o texto oficial em mãos**. Se o texto oficial vier a ser obtido pela assessoria jurídica (placar/portal do STF — meio fora deste engajamento), o cenário é reavaliado em uma rodada, inclusive a redução que uma tese favorável permitiria. Até lá, a posição contábil e jurídica se apoia no que está provado, não no que foi noticiado.

**(b) Mesmo uma tese de licitude abstrata não zera este caso concreto.** As questões devolvidas no Tema 1.389 incluem a **distribuição do ônus da prova da fraude** — ou seja, o próprio STF admite que o caso a caso sobrevive. E o precedente que a diretoria invoca (Tema 725) expressamente **não impede** reconhecer vínculo quando presentes os requisitos do art. 3º CLT (stf_tema_725_adc48_adpf324.md). Os fatos aqui documentados — exclusividade, 9h–18h no escritório, ordens de superior hierárquico, pagamento fixo "independentemente de entregas" (§2) — são os mesmos que já sustentam a probabilidade alta de vínculo (§1.4). No limite, uma tese pró-empregadora desloca a discussão para *quem prova o quê*; não apaga as provas que já existem.

**(c) "Processo parado" é risco parado e corrigindo — não risco zero.** A própria biblioteca registra que a suspensão "congela o processo; não zera a exposição", porque correção e juros continuam incidindo. E o corte prescricional fica travado na data do ajuizamento: esperar **não encolhe o passivo, só o encarece**. Custo ilustrativo de carregar a suspensão (taxas anuais de referência — premissa não verificada, as taxas reais não constam da biblioteca; base = R$ 728.388 do cenário 18k):

| Suspensão adicional | @10% a.a. | @15% a.a. |
|---|---:|---:|
| +12 meses | +72.839 → **801.227** | +109.258 → **837.646** |
| +24 meses | +152.961 → **881.349** | +234.905 → **963.293** |

**(d) A provisão é reversível; a surpresa, não.** Se o STF decidir a favor da pejotização e o caso sobreviver em termos melhores, a classificação CPC 25 (label do contrato) migra de "provável" para "possível" e o valor é **revertido no resultado** — não há custo em estar provisionado hoje. O assimétrico é chegar ao julgamento sem provisão: se o desfecho for desfavorável (ex.: ônus da prova fixado contra a empregadora), o impacto cai inteiro no exercício da derrota, sobre um número que pode passar de R$ 1 mi com as horas extras (§6.2). Há também o ângulo defensivo: o e-mail interno "risco zero" integra o material que a reclamada teria de confrontar num processo em que **o ônus de provar a validade do contrato é seu** (Súmula 212/TST) — uma provisão fundamentada é a melhor resposta à narrativa de fraude.

**Resumo da resposta à diretoria**: provisionar não é admitir derrota; é precificar o estado atual do mundo (fatos documentados + mérito pendente + suspensão que corrige em vez de extinguir). O caminho para **reduzir** a provisão é (i) trazer o texto oficial do STF para reavaliação imediata, (ii) negociar acordo com desconto antes do julgamento e (iii) corrigir os contratos PJ em vigor — não a inércia.

---

## 5. Prescrição (CF art. 7º, XXIX; CLT art. 11; Súmula 308 — cf_art7_xxix_prescricao.md)

- **Bienal:** contrato encerrado em **30/09/2026** (notificação; última NF em set/2026). Ajuizado em 16/11/2026, está dentro dos 2 anos → **sem barreira total**.
- **Quinquenal (Súmula 308: créditos anteriores a 5 anos contados do ajuizamento):** corte em **16/11/2021**.
  - Vínculo total: 01/10/2019–30/09/2026 = **84 meses** (84 × NF; bate com as 3 NFs de out–dez/2019 e 9 de jan–set/2026).
  - **Prescrito:** out/2019–out/2021 = 25 meses + 15 dias (1–15/nov/2021) = **25,5 meses**.
  - **Exigível:** 16/11/2021–30/09/2026 = 15 dias + 58 meses = **58,5 meses**.
  - Conferência: 25,5 + 58,5 = 84. ✔
- **FGTS:** mesma prescrição quinquenal (STF ARE 709.212/Tema 608, conforme a biblioteca) → segue o corte de 16/11/2021.
- **Aviso-prévio proporcional:** considera o **tempo total de serviço** (7 anos), ainda que parte das verbas esteja prescrita (nota da própria cf_art7_xxix_prescricao.md + Lei 12.506/2011).
- *Timing:* quanto antes a Solaris fechar acordo, melhor — e para o reclamante cada mês de atraso no ajuizamento **reduz** a janela exigível (o corte avança com a data do ajuizamento). O cálculo abaixo usa a data anunciada, 16/11/2026.

---

## 6. Exposição — aritmética completa (parâmetros de verbas_e_calculo.md e multa_477_e_honorarios.md)

Base: **R$ 18.000,00/mês** = valor pago à PJ (presunção usual da JT como remuneração-base; defesa pode tentar provar que embutia tributos/custos — argumento fraco dado o pagamento fixo "independentemente de entregas"). Janela exigível = **58,5 meses**. Simplificações adotadas (marcadas): férias **simples** (a biblioteca manda desconsiderar a dobra da não-concessão), FGTS sobre **salários + 13º + férias com 1/3** (simplificação textual da biblioteca), INSS patronal **≈28%** (20% + RAT + terceiros).

| Verba | Aritmética | Valor |
|---|---|---|
| Remuneração-base da janela *(já paga; linha de cálculo, não débito)* | 58,5 × 18.000 | **1.053.000** |
| 13º salários | (58,5/12) × 18.000 = 4,875 avos → confere ano a ano: 2021 (1,5/12)=2.250 + 2022–2025 (4×18.000)=72.000 + 2026 (9/12)=13.500 = 87.750 | **87.750** |
| Férias + 1/3 (simples) | férias: 58,5/12 × 18.000 = 87.750; terço: 87.750/3 = 29.250 | **117.000** |
| FGTS 8% | 8% × (1.053.000 + 87.750 + 117.000 = 1.257.750) | **100.620** |
| Multa 40% do FGTS | 40% × 100.620 | **40.248** |
| Aviso-prévio proporcional (Lei 12.506) | 7 anos completos → 30 + 3×7 = **51 dias**; 51/30 × 18.000 | **30.600** |
| INSS patronal ~28% | 28% × 1.257.750 | **352.170** |
| **TOTAL (sem horas extras, multas e honorários)** | 87.750 + 117.000 + 100.620 + 40.248 + 30.600 + 352.170 | **728.388** |
| — do qual crédito ao reclamante | 728.388 − 352.170 | 376.218 |
| — do qual INSS (RFB) | | 352.170 |

**Horas extras — "a apurar" (planilha só cobre jan–jun/2025):** registradas 18+22+15+26+20+34 = **135 h** (média 22,5 h/mês). *Premissa não verificada na biblioteca* (divisor/adicional): hora = 18.000/200 = R$ 90,00; hora extra 50% = R$ 135,00 → **135 h × 135 = R$ 18.225** diretas só nos 6 meses registrados. Médias diárias de 9,0–9,8 h confirmam sobra sobre a jornada contratual (8h líquidas). Reflexos sobre 13º/férias/FGTS+40% (Súmula 437) aumentariam ~15–25%. **Extrapolação de risco:** se a planilha representasse todo o período exigível, 22,5 × 58,5 ≈ **1.316 h → ~R$ 177.700** diretas + reflexos (teto da exposição subiria para a casa de **R$ 0,9–1,1 milhão**). Falta a planilha de 2021(11/12)–2024 e 2026 (perguntado).

**Multas e honorários (multa_477_e_honorarios.md):** art. 477 §8º (1 salário = R$ 18.000) e art. 467 (50% sobre incontroversas) — a própria biblioteca registra que são **discutíveis** na reversão de pejotização; não somados ao total. Honorários sucumbenciais (art. 791-A, 5–15%): se sucumbente, **+R$ 36–109 mil** sobre a condenação. Não incluídos no total.

**Premissas materialmente relevantes (destacadas, por contrato):**
1. **Extinção imputável à empregadora (sem justa causa, sem aviso cumprido)** → sustenta aviso-prévio (30.600) e multa de 40% (40.248). A notificação diz apenas "encerramento da prestação" (cláusula 7ª admitia rescisão com 30 dias). Se houver prova de pedido de demissão, **−R$ 70.848** (base 18k; −47.232 na base 12k) e a multa do 477 cai. **Sem resposta do cliente — premissa mantida, desconhecido sinalizado (§8).**
2. Rafael **fruiu 20 dias/ano** de descanso (contrato + e-mail RH). Assumimos, com a simplificação da biblioteca (férias simples), creditar férias integrais + 1/3; a defesa pode arguir abatimento dos 20 dias já gozados (~2/3 de cada período) — cenário otimista reduziria férias a ~R$ 39–58,5 mil (base 18k) / ~R$ 26–39 mil (base 12k) + reflexos, **mas a leitura padrão do passivo trabalhista é a tabela acima**. Não forçamos a reconciliação: deixamos o ponto aberto.

### 6.1 Debate da remuneração-base — resposta à informação do diretor

O diretor informou (rodada de perguntas 1) que **"os 18 mil eram cheios justamente porque ele era PJ; um CLT equivalente ganharia uns 12 mil"**. A biblioteca permite exatamente esse argumento: base = "o valor pago à PJ (presunção usual na Justiça do Trabalho, **salvo prova de que embutia tributos/custos** — argumento de defesa)" (verbas_e_calculo.md). Três observações:

1. **Não há prova documental no arquivo** de custos/tributos da PJ (não há demonstrativo de pró-labore, folha da PJ, recolhimentos, equipamentos). O cliente confirmou não ter mais informação — logo a tese defensiva, hoje, é **alegação vazia**: a presunção da JT (base = 100% da NF, reforçada pela cláusula 2ª "independentemente de entregas") tende a prevalecer.
2. A fala do diretor é **faca de dois gumes**: ao dizer que o valor substituía salário + encargos, admite que os R$ 18 mil eram contraprestação do serviço pessoal (art. 3º/457), e a referência a "CLT equivalente" convida a juntada de holerites internos (angle Súmula 338/OJ 383).
3. Ainda assim, é o principal redutor de preço em negociação. Cenários:

| Cenário de base | Remuneração da janela | 13º | Férias+1/3 | FGTS | Multa 40% | Aviso | INSS 28% | **Total** | Crédito ao reclamante |
|---|---|---|---|---|---|---|---|---|---|
| **R$ 18.000** (presunção; cenário primário) | 1.053.000 | 87.750 | 117.000 | 100.620 | 40.248 | 30.600 | 352.170 | **728.388** | 376.218 |
| **R$ 15.000** (ponto médio possível) | 877.500 | 73.125 | 97.500 | 83.850 | 33.540 | 25.500 | 293.970 | **606.990** | 313.020 |
| **R$ 12.000** (tese defensiva, sem prova) | 702.000 | 58.500 | 78.000 | 67.080 | 26.832 | 20.400 | 234.780 | **485.592** | 250.812 |

(Aritmética idêntica ao §6 trocando S: ex. 12k → 58,5×12.000=702.000; 13º 4,875×12.000=58.500; FGTS 8%×838.500=67.080; aviso 51/30×12.000=20.400; INSS 28%×838.500=234.780.)

**Horas extras por cenário:** hora = S/200 (premissa não verificada, §6): 18k → HE50 R$ 135 → 135 h registradas = R$ 18.225; 12k → R$ 90 → R$ 12.150. Extrapolado aos 58,5 meses: ~R$ 177.700 (18k) / ~R$ 118.500 (12k), + reflexos (Súmula 437).

**Ponderação usada na provisão:** julgo P(base 18k mantida) ≈ 70% e P(redução relevante da base) ≈ 30%, por não haver lastro probatório do custo da PJ — **provisão = 0,7×728.388 + 0,3×485.592 = R$ 655.549** (pesos são juízo profissional, não número do arquivo).

---

## 7. Estratégia e recomendações

1. **Contabilidade:** reclassificar de "remoto" (a posição do e-mail da diretoria não se sustenta com estas provas) para **provável** no CPC 25 *(classificação exigida pelo schema do contrato; o texto do CPC não está na biblioteca — label do contrato)*. **Provisão recomendada: R$ 655.549** (melhor estimativa ponderada dos cenários de base do §6.1; banda R$ 486–728 mil; teto ~R$ 0,9–1,1 mi se as horas extras de todo o período aparecerem). Não provisionar é o risco maior: a reversão tem probabilidade alta e a suspensão do Tema 1.389 só **adiaga** o reconhecimento, não o cancela.
2. **Acordo: recomendado — faixa R$ 270.000 a R$ 480.000.** Ancoragem: crédito esperado do reclamante ponderado ≈ R$ 338,6 mil (0,7×376.218 + 0,3×250.812); litigando, espera-se condenação em torno de R$ 486–728 mil + honorários (+R$ 36–109 mil) + correção durante o sobrestamento + risco das HE não mapeadas. A novidade da rodada de perguntas (alegação de "base real de 12 mil") **baixa a ancoragem da negociação** — ponto de entrada sugerido: R$ 270–330 mil; teto de autoridade: R$ 480 mil. Acima disso, o valor de litigar com sobrestamento é melhor. Atenção: acordo trabalhista não apaga o INSS patronal nem a anotação retroativa da CTPS que o Judiciário determina — estruturar com cautela e assessoria. Não sustentar em juízo, por escrito, a frase "18 mil porque era PJ" sem lastro probatório: ela reforça a natureza salarial do pagamento.
3. **Provas a preservar/levantar:** logs de Slack, fluxo de aprovação de RH, planilhas de ponto **de todos os anos**, eventuais testemunhas de autonomia (não há, no arquivo, nenhuma linha de autonomia real: nem multi-cliente — a exclusividade era contratual — nem gestão de resultados).
4. **Thesis de defesa residual** (para negociar preço, não para negar risco): (i) natureza empresarial do instrumento (art. 442-B) — fraca pelos fatos; (ii) prescrição de 25,5 meses — **forte**, já precificada; (iii) deduzir custos/tributos da PJ da base — fraca; (iv) Tema 1.389 como porta de tese futura — incerta e pendente.
5. **Governança:** responder ao e-mail do Diretor de Operações registrando por escrito que a posição "risco zero" contraria a leitura da própria jurisprudência citada (Tema 725 não cobre pejotização com subordinação) e os fatos do contrato.

## 8. Itens abertos (desconhecidos sinalizados — o cliente não respondeu aos itens abaixo e não tem mais informação)

1. **Causa/modalidade da extinção** (dispensa sem justa causa × pedido de demissão × distrato com aviso de 30 dias): **desconhecido**. O parecer assume extinção imputável à Solaris (pior caso); se foi pedida, **−R$ 70.848** (base 18k) / **−R$ 47.232** (base 12k) e a multa do 477 (§8º) sai.
2. **Planilhas de ponto/escala de 01/11/2021–31/12/2024 e jan–set/2026**: **inexistentes no arquivo e não fornecidas**. HE fica rotulada "a apurar"; impacto potencial de ~R$ 118–178 mil diretas (+reflexos) por extrapolação.
3. **Quadro de empregados da Solaris** (>20 → presunção da Súmula 338) e existência de **CLT equivalente real** com salário ~12 mil (a fala do diretor foi condicional; sem holerite no arquivo) — risco de isonomia (OJ 383) **não quantificado por falta de dados**.
4. **Datas efetivas de gozo dos 20 dias/ano** e eventual termo de distrato/aviso prévio: **desconhecidas** (ver premissa 2 e §6.1).
5. **Lastro probatório dos "custos embutidos" nos R$ 18 mil** (pró-labore, recolhimentos, folha da PJ): **o cliente afirmou não ter mais informação** → a tese de base R$ 12 mil permanece alegação sem prova; por isso o cenário primário segue sendo R$ 18 mil e a provisão usa ponderação 70/30 (§6.1).
6. **Inteiro teor oficial de eventual decisão de mérito do Tema 1.389** (tese, modulação, data de publicação): **o cliente foi perguntado (rodada 2) e não tem o documento** → a alegação da diretoria ("o STF já decidiu, está em todo jornal") permanece **premissa não verificada**, sem valor para rebaixar a provisão. A posição do parecer é a decorrente do estado da biblioteca (mérito **pendente**, suspensão mantida). Recomenda-se à assessoria jurídica consultar o placar/portal do STF fora deste engajamento; se houver decisão, este parecer é revisto em uma rodada.

*Respostas recebidas do cliente (26/10/2026): rodada 1 — alegação de que os R$ 18 mil incluíam o "prêmio PJ" e de que um CLT equivalente ganharia ~R$ 12 mil (incorporada no §6.1); rodada 2 — sem informação adicional sobre o inteiro teor da alegada decisão do STF (item 9 de `QUESTIONS.md`). Demais perguntas ficaram sem resposta e estão sinalizadas como desconhecidos acima; perguntas já respondidas não serão repetidas.*
