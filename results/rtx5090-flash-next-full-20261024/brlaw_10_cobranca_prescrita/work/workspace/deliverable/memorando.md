# Memorando — Técnica Forte × Metalúrgica Boa Vista (cobrança de R$ 180.000, 2020/2021)

**Data:** 12/10/2026 · **Referências:** somente `library/INDEX.md` (CC arts. 189, 202, 206 §5º I; CPC arts. 700, 784 III; Súmulas 299, 385, 503 STJ; REsp 1.438.263; REsp 1.792.700; Lei 9.492/97; CDC art. 43 §5º por analogia; Tema 1.264 STJ; CC arts. 389, 406 / Lei 14.905/2024)

---

## 1. Resumo executivo

- O cliente **não pode executar**: o contrato não tem as 2 testemunhas do CPC art. 784 III e boleto não é título executivo. A via correta é a **ação monitória** (CPC art. 700), com alternativa de cobrança pelo procedimento comum.
- **Prescrição (5 anos, CC art. 206 §5º I), parcela a parcela:**
  - **Parcelas 1–4 (R$ 120.000): NÃO prescritas.** O e-mail de 15/09/2022 é reconhecimento inequívoco (CC art. 202 VI) e interrompeu a prescrição, reiniciando o prazo (CC art. 202, parágrafo único) **até 15/09/2027**. O PIX de 02/08/2023 renova o reconhecimento, **mas não interrompe de novo** (interrupção única, CC art. 202 caput).
  - **Parcelas 5–6 (R$ 60.000): PRESCRITAS** em 10/02/2026 e 10/03/2026 — não foram reconhecidas (foram contestadas) e nunca houve interrupção quanto a elas; reconhecimento parcial interrompe apenas o reconhecido.
- **Principal exigível: R$ 110.000** (120.000 − 10.000 do PIX de 02/08/2023). Estimativa de encargos até 12/10/2026, **sem IPCA** (série de índices indisponível no workspace): multa 2% = R$ 2.400 + juros 1% a.m. ≈ R$ 80.857 → **total ≈ R$ 193.257 + IPCA a apurar**.
- **Negativação de R$ 180.000 (12/08/2026) está errada:** regular quanto a R$ 110.000; **indevida quanto a R$ 70.000** (R$ 60.000 prescritos + R$ 10.000 já pagos). **Corrigir já** para R$ 110.000 + encargos. Risco de dano moral **mitigado pela Súmula 385/STJ** (3 inscrições legítimas preexistentes), mas o dever de cancelar subsiste.
- **Protesto: recomendado, só quanto às parcelas 1–4.** Protestar dívida prescrita (5–6) é indevido e gera responsabilidade.
- **Urgência:** prazo final 15/09/2027 e **não haverá segunda interrupção** — ajuizar e viabilizar a citação com folga (idealmente ainda em 2026).

---

## 2. Cronologia (dos documentos)

| Data | Evento |
|---|---|
| 01/09/2020 | Contrato de manutenção industrial; 6 × R$ 30.000, dias 10 de out/2020 a mar/2021, boleto; multa 2%, juros 1% a.m., IPCA; foro Sorocaba/SP; assinado pelas partes, **sem testemunhas** |
| 10/10/2020–10/03/2021 | Vencimentos das parcelas 1–6 (comprovante de execução: relatórios assinados pelo encarregado da Boa Vista) |
| 15/09/2022 | E-mail da Boa Vista: **reconhece parcelas 1–4 (R$ 120.000)**; **contesta parcelas 5–6** (serviço de fev/mar interrompido por greve) |
| 02/08/2023 | PIX de R$ 10.000 "por conta da parcela 1" |
| 12/08/2026 | Negativação no Serasa por **R$ 180.000** (as seis parcelas) |
| hoje (12/10/2026) | Consulta Serasa: **3 negativações anteriores legítimas** (2024–2025, não contestadas) |

---

## 3. Prescrição — análise parcela a parcela

**Regra:** pretensão de cobrança de dívida líquida de instrumento particular prescreve em **5 anos** (CC art. 206 §5º I); nasce com o vencimento não adimplido (CC art. 189). A interrupção **só pode ocorrer uma vez** (CC art. 202 caput) e, interrompida, o prazo **recomeça da data do ato** (parágrafo único). Reconhecimento inequívoco extrajudicial interrompe (art. 202 VI); **reconhecimento parcial interrompe apenas as parcelas reconhecidas**.

| P | Vencimento | Termo se não houvesse interrupção | Interrupção | Novo termo | Situação hoje |
|---|---|---|---|---|---|
| 1 | 10/10/2020 | 10/10/2025 | 15/09/2022 (e-mail, art. 202 VI) | **15/09/2027** | Exigível |
| 2 | 10/11/2020 | 10/11/2025 | 15/09/2022 | **15/09/2027** | Exigível |
| 3 | 10/12/2020 | 10/12/2025 | 15/09/2022 | **15/09/2027** | Exigível |
| 4 | 10/01/2021 | 10/01/2026 | 15/09/2022 | **15/09/2027** | Exigível |
| 5 | 10/02/2021 | **10/02/2026** | nenhuma (contestada) | — | **PRESCRITA** |
| 6 | 10/03/2021 | **10/03/2026** | nenhuma (contestada) | — | **PRESCRITA** |

*Leitura da tabela: "Novo termo" é o **termo final** do prazo recontado. No `analise.json`, a chave `novo_termo` tem o mesmo sentido (2027-09-15); o termo inicial da recontagem é o ato interruptivo (15/09/2022 — art. 202, parágrafo único).*

Verificações de data (aritmética):

- Em 15/09/2022, nenhuma das parcelas 1–4 estava prescrita: faltavam 3 anos e 25 dias para a P1 completar 5 anos (10/10/2020 → 10/10/2025). Logo a interrupção incidiu validamente sobre 1–4.
- O e-mail de 15/09/2022 **não reconhece** 5–6 — ao contrário, as impugna expressamente ("não reconhecemos"). Contestar não é ato inequívoco de reconhecimento (art. 202 VI). Prazo de 5 anos corrido do vencimento: P5 completou em 10/02/2026 e P6 em 10/03/2026, **antes da negativação de 12/08/2026**.
- O PIX de 02/08/2023 (R$ 10.000, "por conta da parcela 1") é **novo reconhecimento, mas não interrompe novamente** — a liberação legal é de uma única interrupção (CC art. 202 caput; a library registra expressamente essa consequência). Nada disso salva as parcelas 5–6: o pagamento foi afetado à parcela 1.
- Consequência crítica: como a interrupção única já foi consumida em 15/09/2022, o novo prazo **corre até 15/09/2027 sem possibilidade de nova interrupção** pelo despacho de citação (art. 202 I também está submetido ao caput "somente poderá ocorrer uma vez"). É preciso ajuizar cedo e garantir a citação antes de 15/09/2027. *(Como a data exata do vencimento da pretensão caso a citação caia depois do ajuizamento depende de regra que não consta da library — efeito do ajuizamento vs. despacho quando a interrupção única já se esgotou — fixo a diretriz conservadora: ajuizar idealmente ainda em 2026 e, em todo caso, até março/2027. Item sinalizado como não verificado.)*

**Resultado:** dívida viva = parcelas 1–4; dívida extinta pela prescrição = parcelas 5–6.

---

## 4. Via processual — por que não execução

- O contrato é documento particular assinado pelas partes, **sem as 2 testemunhas** exigidas pelo CPC art. 784 III → **não é título executivo extrajudicial** (library: `cpc_titulo_executivo_monitoria.md`, com o REsp 1.438.263; a exceção de contrato eletrônico com assinatura digital — Tema 1.247/STJ — a própria library indica não aplicável aqui: o contrato é físico, assinado "em 01/09/2020").
- **Boleto bancário não é título executivo** (library, idem).
- Logo, a "execução" pretendida pelo cliente seria extinta/embargável por ausência de título. A via correta:
  - **Ação monitória (CPC art. 700)** — proveito da prova escrita sem eficácia de título executivo: contrato bilateral assinado + relatórios de serviço assinados pelo encarregado da Boa Vista + e-mails de reconhecimento. Prazo quinquenal (CC art. 206 §5º I; por analogia, Súmulas 299/503 do STJ — prazo quinquenal da monitória fundada em documento sem força executiva).
  - Alternativa: **ação de cobrança** pelo procedimento comum (indicada na própria library). A monitória é preferível **estrategicamente**: a mesma prova escrita, insuficiente como título executivo, já autoriza a inicial monitória (CPC art. 700), enquanto na cobrança haveria cognição plena desde o início. *O andamento posterior da monitória (mandado de pagamento inicial e sua conversão em título executivo judicial, embargos) **não está descrito na library** — preferência declarada como juízo prático, não como citação.*
- Pedido: parcelas 1–4, com multa 2%, juros 1% a.m. e correção IPCA (encargos contratuais; CC arts. 389 e 406 com a Lei 14.905/2024, e a library de encargos manda calcular **só as parcelas exigíveis, abatido o pagamento parcial**).

**Risco de mérito nas 1–4:** baixo — há reconhecimento escrito (15/09/2022) e pagamento parcial (2023), além de relatórios assinados pelo encarregado. Nas 5–6, além da prescrição, a devedora alega serviço não concluído por greve — defesa de mérito que **não verifiquei na library** (não citarei; apenas a registro como risco fático). O cliente confirma a greve e diz que a equipe "fez o que deu", com relatórios do encarregado cobrindo fev/mar/2021: discussão **ociosa**, porque a prescrição extingue 5–6 antes do mérito — e por isso esses relatórios não vão ao pedido.

---

## 5. Números — aritmética

### 5.1 Principal

| Componente | Valor |
|---|---|
| Parcelas reconhecidas (1–4): 4 × 30.000 | 120.000 |
| (−) PIX 02/08/2023, "por conta da parcela 1" | (10.000) |
| **Principal exigível** | **110.000** |
| Parcelas prescritas (5–6): 2 × 30.000 — não cobráveis | 60.000 |
| Nominal total apresentado pelo cliente | 180.000 (= 110.000 exigível + 10.000 pago + 60.000 prescrito) ✔ reconcile |

### 5.2 Encargos estimados (até 12/10/2026) — parcelas exigíveis apenas

Metodologia declarada: multa contratual 2% aplicada uma vez sobre o valor de cada parcela vencida; juros de 1% a.m. desde o vencimento; meses inteiros + fração de dias/30; **sem IPCA** — a série do índice não existe na library e não há internet, então a correção é item aberto (fórmula: aplicar IPCA acumulado do vencimento ao pagamento sobre cada saldo).

| P | Base × período | Juros |
|---|---|---|
| 1 | 30.000 × 1% × 33,767 m (10/10/2020→02/08/2023: 33 m + 23 d) = 10.130,00; + saldo 20.000 × 1% × 38,333 m (02/08/2023→12/10/2026: 38 m + 10 d) = 7.666,67 | 17.796,67 |
| 2 | 30.000 × 1% × 71,067 m (10/11/2020→12/10/2026: 71 m + 2 d) | 21.320,00 |
| 3 | 30.000 × 1% × 70,067 m (10/12/2020→12/10/2026: 70 m + 2 d) | 21.020,00 |
| 4 | 30.000 × 1% × 69,067 m (10/01/2021→12/10/2026: 69 m + 2 d) | 20.720,00 |
| **Total juros** | | **80.856,67** |
| Multa 2% × 4 parcelas × 30.000 | 4 × 600 | **2.400,00** |

**Total estimado sem IPCA (12/10/2026): 110.000 + 80.856,67 + 2.400 = R$ 193.256,67** (+ IPCA do período, a apurar).

Premissas sinalizadas: (i) o PIX de 10.000 foi tratado como **amortização do principal da parcela 1**, porque o e-mail diz "por conta da parcela 1"; as regras legais de imputação do pagamento (CC) **não constam da library** e por isso não as apliquei — se imputadas a encargos, o saldo de principal muda levemente (item aberto); (ii) multa de 2% contada cheia sobre a P1 (30.000) no vencimento, ainda que depois pago parte; (iii) fração de mês por dias/30. Os juros correm **até o pagamento efetivo** — o valor acima é fotografia de hoje.

### 5.3 Parcelas 5–6

Não se calculam encargos: a pretensão está extinta; o valor nominal de R$ 60.000 é **irrecuperável** via judicial (prescrição — e, subsidiariamente, haveria litígio fático sobre a greve).

---

## 5-bis. Tréplica à impugnação do cliente (Sérgio, 12/10/2026: "pagaram em 2023!" / "tenho relatório assinado das 5 e 6")

### (i) "Pagamento interrompe a prescrição, qualquer um sabe" — meio certo, e por isso mesmo nada muda

O instinto vem do próprio art. 202 VI (reconhecimento inequívoco interrompe, e pagar é reconhecer). Mas o **caput do art. 202 diz: "A interrupção da prescrição, que somente poderá ocorrer uma vez..."**. A cota única de interrupção já foi gasta pelo **e-mail de 15/09/2022** (reconhecimento das parcelas 1–4). A library registra a consequência literalmente: *"o pagamento parcial posterior é novo reconhecimento, mas **não interrompe novamente** (uma única vez)"*.

Efeito real do PIX de 02/08/2023, medido:

| | Prazo que valeria se houvesse 2ª interrupção | Prazo que vale (interrupção única) |
|---|---|---|
| Parcelas 1–4 | até 02/08/2028 | **até 15/09/2027** |

Diferença: ~10 meses e meio a mais (02/08/2028 − 15/09/2027) — que a lei não dá. O PIX rendeu duas coisas boas e nenhuma delas é prazo: **−R$ 10.000** no saldo e **prova extra** (admite a dívida com dinheiro). Para as 5–6 o PIX jamais ajudaria: pago expressamente "por conta da parcela 1", e reconhecimento parcial interrompe apenas o reconhecido.

Ironia que convém ao cliente conhecer: **sem o e-mail de 15/09/2022, as parcelas 1–4 já estariam prescritas** (termos out/2020→out/2025 … jan/2021→jan/2026, todos anteriores a hoje). Foi a Boa Vista, ao confessar por escrito, quem manteve vivas as 1–4 — argumento forte na negociação.

### (ii) "Tenho relatório assinado das parcelas 5 e 6" — prova da dívida ≠ interrupção da prescrição

Relatórios assinados pelo encarregado provam o **serviço executado** — são ótima prova escrita para uma monitória (CPC art. 700) e reforçam as 1–4. Mas a prescrição **não se interrompe com papel do credor**: as causas de interrupção verificadas no excerto do art. 202 da library são atos de fora do credor — despacho do juiz que ordena citação (I) ou ato inequívoco **do devedor** importando reconhecimento (VI); o resto do rol vem truncado no excerto ("…") e nenhuma causa lavrada pelo credor aparece nele *(não se constrói sobre causa não verificada)*. Documento próprio prova a pretensão; não segura o relógio dela.

E mesmo lendo os relatórios da forma mais generosa possível — como ato do devedor assinado ao tempo do serviço (fev/mar/2021), o que não são, pois nessa data a dívida nem estava vencida, e em 15/09/2022 a Boa Vista os repudiou ("não reconhecemos") — a aritmética não salva:

- P5: recontagem desde ~fev/2021 → termo **~fev/2026**; P6: desde ~mar/2021 → termo **~mar/2026**.
- Hoje: **12/10/2026**. Passados 7–8 meses dos termos, em qualquer leitura. **Prescritas de qualquer jeito.**

Dívida prescrita não revive com prova nova — e prova de dívida prescrita na mesa só agrava: é exatamente o valor que **não** pode estar no Serasa nem no protesto (library: negativacao_prescrita_sumula385.md — STJ Tema 1.264; REsp 1.792.700; Lei 9.492/97). Manter os 60k nesses instrumentos transforma a defesa deles em **ação deles contra nós**.

**Traduzindo para a mesa de negociação:** temos R$ 110.000 que eles próprios confessaram por escrito e pagaram em parte; temos R$ 60.000 sobre os quais eles escreveram "não reconhecemos" e o prazo venceu. Por isso o piso do acordo é 110k e o pedido não menciona 5–6.

---

## 6. Negativação (já feita em 12/08/2026 por R$ 180.000)

- **Regular quanto a R$ 110.000**: parcelas 1–4 ainda exigíveis; a inscrição não pode ultrapassar o prazo prescricional (CDC art. 43 §5º por analogia; STJ Tema 1.264; REsp 1.792.700) — aqui o termo é **15/09/2027**.
- **Indevida quanto a R$ 70.000**:
  - R$ 60.000 (parcelas 5–6): **inscrição de dívida prescrita é indevida** (library `negativacao_prescrita_sumula385.md`), gerando dever de exclusão;
  - R$ 10.000 já pagos (PIX 2023): valor extinto por pagamento — mantê-lo no cadastro extrapola o débito real.
- **Dano moral:** em tese a inscrição indevida o ensejaria, mas **Súmula 385/STJ**: havendo **inscrição legítima preexistente** (a consulta de hoje mostra 3 negativações de fornecedores, 2024–2025, não contestadas), **não cabe indenização por dano moral**, ressalvado o direito ao cancelamento. Ou seja: o risco indenizatório é baixo hoje, mas **não é estável** — decorre de inscrições de terceiros que a Boa Vista poderia contestar. A correção imediata é a conduta segura.
- **Ação devida:** retificar o Serasa para **R$ 110.000 + encargos** (excluir P5–P6 e os 10.000 pagos). Manter 180.000 é litigar com a mão errada: entrega à devedora uma demanda contra o cliente exatamente na semana em que ele pretende ajuizar.

---

## 7. Protesto

- O cliente quer "executar e, se não pagarem, protestar". Ordem invertida e em parte sem objeto: a execução não cabe (item 4) e o protesto **não depende** de tentativa executiva anterior.
- **Protesto de documento de dívida** (sem força executiva) é **admitido** — Lei 9.492/97, art. 1º (library) — e pode ser dirigido ao contrato + boletos das parcelas exigíveis: **recomendado, limitado a R$ 110.000 + encargos**.
- **Vedado** protestar as parcelas 5–6: protesto de dívida prescrita é igualmente indevido e gera responsabilidade (library). E **não se conte com o protesto para interromper prescrição**: o excerto do art. 202 na library lista como causas o despacho que ordena a citação (I) e o reconhecimento pelo devedor (VI), e o restante do rol vem truncado ("…") — não verifiquei causa interruptiva relacionada a protesto, logo ele não é "salvo-conduto" *(ponto não verificado na library)*.
- Utilidade prática do protesto quanto às parcelas exigíveis: valor probatório e pressão de cobrança, a custo baixo de cartório. *(Efeito de "constituição em mora" do protesto não consta da library — não o invoco.)* Se a devedora pagar/em acordo antes, sustar.

---

## 8. Estratégia — ação × acordo

**Calendário duro:** termo final 15/09/2027 (interrupção única já consumida). Recomendo: (1) corrigir Serasa **esta semana**; (2) protestar P1–P4 em novembro/2026; (3) notificação extrajudicial com planilha (110.000 + encargos) e proposta; sem resposta em 30 dias, **ajuizar a monitória até dezembro/2026–março/2027** com pedido de citação célere.

**Ancoragem da negociação (números de hoje):**

- Aspiration (causa de pedir): **R$ 193.256,67 + IPCA** (estimado; encargos correm até o pagamento — a cada mês de demora, +R$ ~1.100 só de juros sobre o saldo de principal de R$ 110.000, a 1% a.m., ainda sem IPCA).
- Piso técnico: **R$ 110.000** de principal (o que a própria devedora reconheceu, líquido do PIX). Aceitar abaixo disso significa doar capital reconhecido por escrito.
- A devedora pagou R$ 10.000 em 2023 e "o restante em breve": perfil de caixa apertado, não de calote contencioso. Acordo realista: **R$ 120–150k em 6–12 parcelas** com garantia (aval, fiança ou caução… *instrumentos de garantia não estão na library — tratar como opção a desenhar*) ou sinal + monitória suspensa. Abaixo de R$ 110k à vista pode valer ajuizar: a prova escrita é forte e o custo de risco nas 1–4 é baixo.
- **Não cobrar judicialmente as 5–6**: pedir o que está prescrito contamina a estratégia (reconvenção, má-fé processual, e a negativação indevida já é um flanco aberto).

**Cenário judicial provável (1–4):** procedência com multa + juros + IPCA + honorários; defesa provável: prescrição das 5–6 (acolhida — já admitida na nossa própria planilha) e, nas 1–4, nada robusto além de pedidos de repactuação.

---

## 9. Premissas e itens abertos (atualizado com a resposta do cliente de 12/10/2026)

1. **IPCA não calculável** no workspace (sem série de índices na library/internet) **e o cliente não a possui**. Fórmula pronta em 5.2; totais acima permanecem rotulados **sem IPCA**. Obter a série (IBGE) via contador antes do ajuizamento/protesto.
2. ~~Assumido: nenhum outro pagamento/reconhecimento após 02/08/2023~~ — **confirmado pelo cliente** ("pagaram R$ 10 mil em agosto de 2023… depois sumiram"). Com isso, a prescrição das parcelas 5–6 está **consolidada**: nunca houve reconhecimento quanto a elas antes dos termos de 10/02/2026 e 10/03/2026.
3. PIX afetado ao principal da P1 — premissa mantida: o devedor mesmo escreveu "por conta da parcela 1"; as regras legais de imputação (CC) **não constam da library** e por isso não foram aplicadas.
4. Não verificado na library (declarado, não citado): regras de imputação de pagamento, exceção de contrato não adimplido (alegação da devedora sobre as 5–6 — ociosa pela prescrição), efeitos do ajuizamento com citação após exaurida a interrupção única (diretriz conservadora: ajuizar até mar/2027), instrumentos de garantia para acordo.
5. Honorários/sucumbência e custas não quantificados (sem parâmetros na library).
6. Assumido (arquivo silencioso e cliente sem informação adicional): não existem nota promissória, termo de confissão ou garantia autônoma assinada por sócio da Boa Vista.

---

## 10. Citações utilizadas (todas em `library/INDEX.md`)

| Afirmação | Fonte |
|---|---|
| Prescrição quinquenal de dívida líquida de instrumento particular; início pelo vencimento; interrupção única; reconhecimento inequívoco; reconhecimento parcial só alcança o reconhecido; pagamento parcial posterior não reinterrompe | `cc_prescricao_202_206.md` (CC 189, 202 caput/VI/par. único, 206 §5º I) |
| Contrato sem 2 testemunhas não é título executivo; boleto não é título executivo; monitória por prova escrita sem eficácia executiva; prazo quinquenal (Súmulas 299/503); alternativa de cobrança | `cpc_titulo_executivo_monitoria.md` (CPC 700, 784 III; REsp 1.438.263) |
| Inscrição de dívida prescrita é indevida; registro não ultrapassa o prazo prescricional; Súmula 385 (sem dano moral com inscrição legítima preexistente, ressalvado cancelamento); protesto de dívida prescrita indevido; protesto de documento de dívida admitido (Lei 9.492/97) | `negativacao_prescrita_sumula385.md` (Súmula 385; REsp 1.792.700; Lei 9.492/97; CDC 43 §5º analogia; Tema 1.264) |
| Multa 2%, juros 1% a.m. desde o vencimento, IPCA contratual; cálculo só das parcelas exigíveis com abatimento do pago | `juros_correcao.md` (CC 389, 406 — Lei 14.905/2024; contrato) |
