# MEMORANDO — Técnica Forte Ltda. × Metalúrgica Boa Vista Ltda.
**Assunto:** cobrança de R$ 180.000,00 (6 parcelas de out/2020 a mar/2021) — via processual, prescrição, negativação, protesto e estratégia
**Data:** 12/10/2026 · **Foro previsto:** Comarca de Sorocaba/SP (cláusula de foro do contrato) · **Diligência:** respostas do cliente de 12/10/2026 incorporadas (ver §9)
**Referências usadas:** apenas `library/INDEX.md` (biblioteca fechada). Toda citação abaixo aponta para arquivo listado no índice.

---

## 0. Resumo executivo (o que muda o plano do cliente)

| Item | Resposta | Fundamento |
|---|---|---|
| Executar o contrato? | **Não.** O contrato não é título executivo (assinado sem 2 testemunhas; boleto também não é) | `library/cpc_titulo_executivo_monitoria.md` — CPC art. 784 III; REsp 1.438.263 |
| Via correta | **Ação monitória** (CPC art. 700) — prova escrita sem eficácia de título; alternativa subsidiária: cobrança pelo procedimento comum | idem |
| Dívida cobrável | **R$ 110.000,00 de principal** (parcelas 1 a 4, líquidas do PIX de R$ 10.000,00) | `library/cc_prescricao_202_206.md` — art. 202 VI e p.ú. |
| Dívida prescrita | **R$ 60.000,00** (parcelas 5 e 6) — não cobrar, não inscrever, não protestar | art. 206 §5º I; art. 189 |
| Total estimável hoje | **R$ 194.390,00** (principal + multa 2% + juros 1% a.m.), **sem** a correção IPCA, que não pôde ser calculada | `library/juros_correcao.md` |
| Negativação de R$ 180.000,00 feita em 12/08/2026 | **Regular quanto a R$ 110.000,00; indevida quanto a R$ 70.000,00** (R$ 60.000 prescritos + R$ 10.000 já pagos) | `library/negativacao_prescrita_sumula385.md` — Tema 1.264, REsp 1.792.700, CDC art. 43 §5º por analogia |
| Risco de dano moral pela negativação | **Baixo** (Súmula 385/STJ: há 3 inscrições anteriores não contestadas), mas com **risco real de exclusão/rebaixa do registro** e custos de sucumbência | Súmula 385 |
| Protesto | **Recomendado, porém restrito ao exigível** (documento de dívida, Lei 9.492/97 art. 1º). **Protestar as parcelas 5 e 6 é indevido e gera responsabilidade** | idem |
| Prazo fatal | **15/09/2027** para as parcelas 1 a 4 (≈11 meses a partir de hoje). A interrupção do art. 202 **já foi usada uma única vez** — ajuizar não reabre prazo | art. 202, caput e p.ú. |

**O cliente está errado em dois pontos e isso é a parte mais valiosa do trabalho:** (a) "executar" é impossível nesta base documental; (b) "não prescreveu nada" é falso — R$ 60.000,00 já prescreveram e a negativação que ele fez mês passado já contém essa parcela indevida, o que hoje é uma exposição ativa, não um erro inofensivo.

---

## 1. Premissas, limites e o que não pude verificar

1. **Biblioteca fechada.** Só fundamento nos 4 arquivos do índice. O que eu acreditava ser lei e não está lá foi marcado como **não verificado** e não serve de base para conclusão.
2. **IPCA não está no arquivo nem na biblioteca.** Não há série de índices em `workspace/`. **A correção monetária contratada (IPCA) não foi calculada** — é item aberto (`QUESTIONS.md`, Q1). Todos os totais abaixo são **sem correção** e portanto **subestimam** o valor do pedido. Em uma dívida de 2020/2021 com ~6 anos de atraso, a correção costuma ser da mesma ordem de grandeza dos juros; a diferença não é marginal.
3. **Contagem de prazo.** Uso o critério simples "vencimento + 5 anos". A regra de contagem de prazos do CC (art. 132 — excluir o dia do começo, incluir o do vencimento) **não está na biblioteca (não verificado)**. Isso não altera nenhuma conclusão: a contagem alternativa desloca os termos em, no máximo, 1 dia, e as parcelas 5 e 6 já estão **244 e 216 dias** após o termo (ver §3).
4. **Imputação do PIX de R$ 10.000,00.** Assumi que ele abate **principal da parcela 1**, porque a própria devedora o declarou "por conta da parcela 1" (`documents/emails_reconhecimento.txt`) e porque `library/juros_correcao.md` manda calcular "abatido o pagamento parcial". A regra legal de imputação (pagamento em juros antes do principal) **não está na biblioteca (não verificado)**; a alternativa está quantificada no §4.3.
5. **Assinatura do contrato — CONFIRMADA (resposta do cliente, 12/10/2026).** "Foi tudo meio informal": só os dois representantes assinaram, sem testemunhas e sem qualquer certificação digital alegada. A premissa virou fato: a exceção do Tema 1.247/STJ (assinatura eletrônica digital) não incide e **a via permanece monitória** — não há caminho para execução direto desta base documental (§2, §9).
6. **Respostas do cliente incorporadas em 12/10/2026 (§9).** Fecharam: pagamento único de R$ 10.000,00 (sem outros pagamentos); ausência de testemunhas; existência de relatórios assinados pelo encarregado e da greve de fev/2021. Permanecem **desconhecidos, por falta de informação do cliente** (flag explícito, sem suposição): série de IPCA (Q1), legitimidade das 3 negativações anteriores da ré (Q3), originais/carteiras dos boletos e exigências do cartório para protesto (Q5), solvência/RJ/falência da devedora (Q9) e ações em curso + endereço atual para citação (Q10).

---

## 2. Por que NÃO é execução de título extrajudicial

O pedido do cliente ("quero EXECUTAR o contrato") fracassaria na portaria:

- **CPC art. 784 III** só reconhece como título executivo extrajudicial "o documento particular assinado pelo devedor e por **2 (duas) testemunhas**" (`library/cpc_titulo_executivo_monitoria.md`).
- O contrato tem assinatura do representante da contratada e do representante da contratante e está expressamente "**Sem testemunhas**" (`documents/contrato_prestacao_servicos.md`).
- A biblioteca traz exatamente esse caso: "**Contrato particular sem duas testemunhas não é título executivo**", com o REsp 1.438.263, e afasta a exceção de assinatura eletrônica digital para este caso.
- E "**boleto bancário não é título executivo**" — o que derruba a tentativa de executar os boletos de `documents/boletos_e_comprovantes.csv`.

Consequência: não há "título" para o cumprimento de sentença/execução; a petição inicial de execução seria emendada ou extinta, com perda de tempo e honorários — e, o que é pior, **com parte do prazo de prescrição escoando durante o erro** (o ajuizamento de execução equivocada não gera a interrupção do art. 202 I, que depende de despacho que ordena a citação; ver §5.3).

## 2.1 Por que monitória (e não cobrança desde logo)

- **CPC art. 700:** a monitória é a via de quem afirma, "com base em **prova escrita sem eficácia de título executivo**", ter direito a dinheiro. É a descrição literal deste caso.
- A prova escrita é robusta e documental, em três camadas: (i) contrato assinado pelas duas partes; (ii) **relatórios de serviço assinados pelo encarregado da própria Boa Vista** para as 6 parcelas (`documents/boletos_e_comprovantes.csv`); (iii) **confissão de dívida por escrito** das parcelas 1 a 4 no e-mail de 15/09/2022 (`documents/emails_reconhecimento.txt`).
- O ponto que costuma desaconselhar a monitória — necessidade de prova oral/dilação sobre inadimplemento — aqui **não existe quanto ao pedido**: as parcelas 1 a 4 foram reconhecidas pela devedora, e a única controvérsia faticamente relevante (serviço interrompido pela greve em fev/mar) atinge **justamente as parcelas 5 e 6, que ficam de fora do pedido por estarem prescritas**. O pedido nasce "limpo" para julgamento antecipado.
- **Prazo da monitória:** quinquenal, acompanhando a pretensão subjacente. A biblioteca só trata disso para cheque sem força executiva (**Súmula 503:** "o prazo para ajuizamento de ação monitória em face do emitente de cheque sem força executiva é quinquenal"; **Súmula 299:** monitória admissível mesmo com cheque prescrito). Uso como **analogia**, não como norma direta: o prazo da monitória segue o prazo da pretensão material. Logo, a prescrição apurada no §3 vale também aqui.
- Alternativa subsidiária, também prevista na biblioteca: **ação de cobrança pelo procedimento comum**. É mais lenta na formação do título, mas permite discutir perdas e danos/exceção de contrato não cumprido se a defesa abrir frente fática. Recomendo monitória com pedido subsidiário de conversão/procedimento comum apenas se houver obstáculo processual.
- *Não verificado:* os desdobramentos da monitória (expedição de mandado monitório, embargos, conversão em título executivo) não constam do trecho da biblioteca — não uso esses mecanismos como fundamento da estratégia.

---

## 3. Prescrição, parcela a parcela

**Regra:** "Prescreve em **cinco anos**: I – a pretensão de cobrança de dívidas líquidas constantes de instrumento público ou particular" (CC art. 206 §5º I). A pretensão nasce do vencimento não adimplido (art. 189). **Interrupção:** "por qualquer ato inequívoco, ainda que extrajudicial, que importe reconhecimento do direito pelo devedor" (art. 202 VI), **"somente poderá ocorrer uma vez"** (caput), e "**recomeça a correr da data do ato que a interrompeu**" (parágrafo único). Nota da biblioteca: "**Reconhecimento parcial interrompe apenas quanto às parcelas reconhecidas**; o pagamento parcial posterior é novo reconhecimento, mas **não interrompe novamente** (uma única vez)".

**Os dois marcos do caso:**
- **15/09/2022** — e-mail do financeiro da Boa Vista: "Reconhecemos as **parcelas 1 a 4** (out/2020 a jan/2021), total R$ 120.000, e pretendemos quitá-las" + "**As parcelas 5 e 6 nós contestamos** ... não reconhecemos". É ato inequívoco extrajudicial de reconhecimento (art. 202 VI) **das parcelas 1 a 4 apenas** — a própria peça exclui 5 e 6.
- **02/08/2023** — PIX de R$ 10.000,00 "**por conta da parcela 1**". Novo reconhecimento, **sem efeito interruptivo** (a faculdade do art. 202 já foi consumida em 15/09/2022). Vale só como prova adicional e como abatimento.

| Parc. | Vencimento | Termo de 5 anos (sem interrupção) | Interrompida em | Novo termo | Situação em 12/10/2026 |
|---|---|---|---|---|---|
| 1 | 10/10/2020 | 10/10/2025 | 15/09/2022 (art. 202 VI) | **15/09/2027** | **Exigível** (faltam ~11,1 meses) |
| 2 | 10/11/2020 | 10/11/2025 | 15/09/2022 | **15/09/2027** | **Exigível** |
| 3 | 10/12/2020 | 10/12/2025 | 15/09/2022 | **15/09/2027** | **Exigível** |
| 4 | 10/01/2021 | 10/01/2026 | 15/09/2022 | **15/09/2027** | **Exigível** |
| 5 | 10/02/2021 | **10/02/2026** | — (contestada) | — | **PRESCRITA** (244 dias após o termo) |
| 6 | 10/03/2021 | **10/03/2026** | — (contestada) | — | **PRESCRITA** (216 dias após o termo) |

Leitura parcel a parcela:

- **Parcela 1 (venc. 10/10/2020).** O termo original seria 10/10/2025. O reconhecimento de 15/09/2022 é anterior a esse termo, portanto interrupção válida; o novo prazo de 5 anos corre do ato (p.ú.), vencendo em **15/09/2027**. O PIX de 02/08/2023 **não** reabre prazo (art. 202 caput) — quem contabilizar 5 anos a partir de 2023 estará enganado: o termo continua 15/09/2027.
- **Parcelas 2 e 3 (10/11/2020 e 10/12/2020).** Mesma lógica; ambas reconhecidas nominalmente ("parcelas 1 a 4, total R$ 120.000"). Exigíveis até 15/09/2027.
- **Parcela 4 (10/01/2021).** Termo original 10/01/2026 — estaria prescrita **9 meses atrás** se não houvesse o reconhecimento de 2022. Foi interrompida a tempo; exigível até 15/09/2027.
- **Parcela 5 (10/02/2021).** Não reconhecida — pelo contrário, contestada expressamente. Sem interrupção possível (não houve ato do art. 202). Termo em **10/02/2026**; hoje a pretensão está extinta. O PIX de 02/08/2023 ocorreu quando a pretensão ainda viva, **mas** foi declarado "por conta da **parcela 1**" e o e-mail de 15/09/2022 já havia negado as parcelas 5 e 6, de modo que não é "ato inequívoco de reconhecimento" quanto a ela (§3.1).
- **Parcela 6 (10/03/2021).** Idem; termo em **10/03/2026**.

**Total:** principal exigível **R$ 120.000,00 − R$ 10.000,00 = R$ 110.000,00**; principal prescrito **R$ 60.000,00**.

### 3.1 O argumento que o cliente vai querer usar — e por que não deve

Argumento possível: "pagaram R$ 10.000,00 em 2023, quando nenhuma parcela estava prescrita; isso reconheceu **todo** o contrato e teria renovado o prazo de 5 e 6 até 02/08/2028" — o que valeria **+R$ 102.320,00** (R$ 60.000 de principal + R$ 1.200 de multa + R$ 41.120 de juros até hoje). Registro por honestidade, mas a avaliação é **fraca**: (i) o pagamento tem destinação expressa à parcela 1; (ii) o mesmo credor recebeu, 11 meses antes, contestação escrita e específica das parcelas 5 e 6 — não há "inequivocidade" (art. 202 VI exige ato inequívoco); (iii) sustentar essa tese significa litigar a existência do serviço de fev/mar, exatamente onde a devedora tem defesa factual (greve) e onde o ônus documental está menos confortável para o cliente. **Confirmação do cliente (12/10/2026) em ambas as direções:** a greve houve e "nosso pessoal fez o que deu" — admissão de serviço apenas parcial, que daria munição à ré —, mas existem **relatórios assinados pelo encarregado da própria devedora, um por parcela, incluindo fev e mar** (`documents/boletos_e_comprovantes.csv`), que neutralizam a alegação de "não concluído" na mesa de negociação. O cliente **não dispõe** de nenhum outro documento posterior que trate das parcelas 5 e 6 (Q6), então a tese permanece sem matéria-prima nova. **Recomendação: não embutir teses frágeis no pedido**; usar eventuais valores de 5 e 6 apenas como moeda de negociação (ver §6.4 e o alerta sobre obrigação natural).

---

## 4. Encargos e números (aritmética à vista)

Base contratual: **multa 2%, juros 1% a.m. desde o vencimento, correção IPCA** (`documents/contrato_prestacao_servicos.md`; `library/juros_correcao.md`: "Cálculo parcela a parcela, apenas das parcelas exigíveis, abatido o pagamento parcial").

### 4.1 Memória de cálculo (juros simples 1% a.m., apurados por dias/30, até 12/10/2026)

| Parc. | Saldo de principal | Multa 2% | Períodos de juros | Juros | Total (sem IPCA) |
|---|---|---|---|---|---|
| 1 | R$ 20.000,00 | R$ 600,00 | 10/10/2020→02/08/2023: 1.026 d = 34,20 m × 1% × R$ 30.000 = **R$ 10.260,00**; 02/08/2023→12/10/2026: 1.167 d = 38,90 m × 1% × R$ 20.000 = **R$ 7.780,00** | R$ 18.040,00 | R$ 38.640,00 |
| 2 | R$ 30.000,00 | R$ 600,00 | 10/11/2020→12/10/2026: 2.162 d = 72,07 m × 1% × R$ 30.000 | R$ 21.620,00 | R$ 52.220,00 |
| 3 | R$ 30.000,00 | R$ 600,00 | 10/12/2020→12/10/2026: 2.132 d = 71,07 m × 1% × R$ 30.000 | R$ 21.320,00 | R$ 51.920,00 |
| 4 | R$ 30.000,00 | R$ 600,00 | 10/01/2021→12/10/2026: 2.101 d = 70,03 m × 1% × R$ 30.000 | R$ 21.010,00 | R$ 51.610,00 |
| **Total** | **R$ 110.000,00** | **R$ 2.400,00** | — | **R$ 81.990,00** | **R$ 194.390,00** |

- Conferência: 110.000 + 2.400 + 81.990 = **194.390**. (Planilha completa com a memória por período em `calculo_encargos.csv`.)
- A multa de 2% incide sobre o valor de cada parcela (R$ 600,00 cada; também na parcela 1, pois o pagamento parcial não reduz a base da multa).
- **Correr de juros daqui para frente:** 1% a.m. sobre R$ 110.000,00 = **R$ 1.100,00/mês**. Se o caso só for liquidado perto do termo de 15/09/2027 (338 dias ≈ 11,27 meses), entram **+R$ 12.393,33**, projetando **R$ 206.783,33 sem IPCA**.
- **Não fechei o valor do pedido** porque falta IPCA (Q1). Não forcei o fechamento: a linha "correção IPCA" está marcada como **PENDENTE** na planilha.

### 4.2 Nota sobre juros que superam o principal
Os juros (R$ 81.990,00) representam 75% do principal. Isso é consequência aritmética de 1% a.m. contratual por ~72 meses. A biblioteca **não contém** regra de limitação de juros, capitalização ou repetição — **não verificado**; convém examinar teses de limitação antes de fixar o pedido (§7, Q8), e o risco de revisão de encargos deve entrar na conta de expectativa de caixa, não ser tratado como certo.

### 4.3 Sensibilidade: e se os R$ 10.000,00 forem imputados primeiro a encargos?
Se a imputação for a multa/juros da parcela 1 (regra legal não verificada — não está na biblioteca), o principal exigível volta a R$ 120.000,00, os juros da parcela 1 sobem para R$ 21.930,00 (2.193 dias sobre R$ 30.000,00) e o total fica: 120.000 + 2.400 + 85.880 = **R$ 208.280,00**, menos R$ 10.000,00 pagos = **R$ 198.280,00** — **+R$ 3.890,00** sobre o cenário adotado. E, nesse cenário, a negativação passaria a ser indevida só em R$ 60.000,00 (não em R$ 70.000,00). Deixo as duas leituras vivas de propósito; o §5 usa o cenário adotado (imputação à parcela 1, como disse a devedora).

---

## 5. Negativação: o que o cliente já fez e onde ele se expôs

**Fato:** em **12/08/2026** o cliente inscreveu a Boa Vista no Serasa por **R$ 180.000,00**, "as seis parcelas" (`documents/negativacao_e_consulta.md`).

**Análise por valor (regra: inscrição de dívida prescrita é indevida — a pretensão está extinta e o registro não pode ultrapassar o prazo prescricional; STJ Tema 1.264, REsp 1.792.700, CDC art. 43 §5º por analogia — `library/negativacao_prescrita_sumula385.md`):**

| Trecho da inscrição | Valor | Situação |
|---|---|---|
| Parcelas 1 a 4, líquidas do PIX | **R$ 110.000,00** | **Regular** — pretensão viva até 15/09/2027, ou seja, o registro de 12/08/2026 está dentro do prazo prescricional |
| Parcelas 5 e 6 | **R$ 60.000,00** | **Indevida** — prescritas em 10/02/2026 e 10/03/2026, antes da inscrição |
| Parcela 1 (valor já quitado) | **R$ 10.000,00** | **Indevida** — o débito não mais existe nesse montante. *Fundamento: consequência lógica dos documentos (pagamento comprovado em 02/08/2023); a biblioteca trata da dívida prescrita, não da paga — item marcado como inferência própria* |

**Dano moral — risco baixo, mas a exposição não é zero.** A devedora tem **3 outras negativações anteriores (2024–2025), não contestadas** (`documents/negativacao_e_consulta.md`). A **Súmula 385/STJ** é clara: "Da anotação irregular em cadastro de proteção ao crédito, não cabe indenização por dano moral, **quando preexistente legítima inscrição**, ressalvado o direito ao cancelamento." Traduzindo para o caso: **o que o cliente provavelmente vai perder é o registro (exclusão/rebaixa), não uma indenização.**

Ressalvas que sustentam "não zero":
1. A Súmula 385 só protege se as inscrições anteriores forem **legítimas**. Se alguma das 3 for contestada e reconhecida irregular, o óbice desaparece — e aí volta a diretriz da biblioteca de que a inscrição de dívida prescrita "**ensejando exclusão e, em tese, dano moral**".
2. Manter a parcela indevida **depois** de cientificado do erro tende a ser lido como conduta desnecessária/abusiva; o custo aumenta a partir da notificação, não de hoje.
3. A indevidade contamina o **protesto** se o cliente protestar os mesmos R$ 180.000,00 (§6).

**Ação recomendada (imediata, unilateral):** retificar a inscrição — de R$ 180.000,00 para **R$ 110.000,00 atualizados (multa + juros + IPCA)** — e excluir expressamente os R$ 60.000,00 prescritos e os R$ 10.000,00 pagos, juntando comprovante de retificação e comunicando a devedora. Não "renegativar" 5 e 6 em nenhum valor, nem em "negativação simbólica". **Teto temporal:** o registro não pode ultrapassar o prazo prescricional do que é exigível, ou seja, deve cair até **15/09/2027** se não houver pagamento.

---

## 6. Protesto e estratégia: ação × acordo

### 6.1 Protesto — recomendado, com recorte
- A biblioteca admite **protesto de documento de dívida sem força executiva** (Lei 9.492/97 art. 1º), "mas sempre quanto a dívida **exigível**". Nosso contrato+boletos são documento de dívida, então o protesto **é cabível** e é instrumento legítimo de pressão e de prova.
- **Vedação absoluta no caso quanto às parcelas 5 e 6:** "o protesto de título/documento de dívida **prescrita** é igualmente indevido e gera responsabilidade". Protestar R$ 180.000,00 seria duplicar a exposição já criada na negativação, agora com custo de cartório e prova documental contra o cliente.
- Também não incluir os R$ 10.000,00 pagos.
- **Recorte:** protesto de **R$ 110.000,00 + encargos** (parcelas 1 a 4). *Não verificado:* a biblioteca não traz regras de instrução, prazos ou efeitos do protesto. Quanto à prescrição, não conto com o protesto como interrupção: a versão do art. 202 disponível na biblioteca (caput com as incs. I e VI, com as demais elididas) não o menciona — **não verificado** se alguma das incisos omitidos trataria disso — e, em todo caso, a faculdade interruptiva do art. 202 já foi consumida em 15/09/2022. Antes de protocolar: confirmar os originais/carteiras dos boletos e a exigência documental do cartório (Q5).

### 6.2 O relógio manda (ponto mais urgente do caso)
O art. 202 "**somente poderá ocorrer uma vez**". A interrupção foi consumida em **15/09/2022**. Consequências práticas:
1. **Ajuizar a monitória não reabre o prazo**: a interrupção pelo despacho que ordena a citação (art. 202 I) seria uma segunda interrupção, o que a regra não admite. O pedido precisa ser **ajuizado antes de 15/09/2027**.
2. Hoje é 12/10/2026: **sobram ~11 meses**. Distribuir em, no máximo, **junho/julho de 2027** é o teto de prudência; meta realista: **distribuir em até 60 dias** (o que também melhora o cálculo: cada mês custa R$ 1.100,00 de juros, mas a demora ameaça o principal de R$ 110.000,00).
3. Uma **nova confissão de dívida assinada agora** (via acordo) cria **título executivo novo** — não é "reabrir" prescrição velha: é negócio jurídico novo com vencimentos novos. É a diferença entre o §6.3 e o §6.4.

### 6.3 Roteiro A — ação (monitória)
- **Pedido:** R$ 110.000,00 + multa R$ 2.400,00 + juros 1% a.m. (R$ 81.990,00 hoje) + **IPCA a apurar** + custas/honorários. Valor atual da causa, sem IPCA: **R$ 194.390,00**.
- **Provas:** contrato; 6 relatórios de serviço assinados pelo encarregado da devedora; e-mail de 15/09/2022 (confissão de R$ 120.000,00); comprovante PIX de 02/08/2023.
- **Foro:** Comarca de Sorocaba/SP, cláusula de eleição do contrato (fato contratual; a biblioteca não traz regra de foro de eleição — não verificado).
- **Não pedir** as parcelas 5 e 6: pedir dívida prescrita não é só perder — é entregar à ré o enquadramento de má utilização dos cadastros e ampliar a sucumbência.
- Contrapartida de risco: a ré, embargando, vai explorar a tese de serviço não concluído. A confissão escrita das parcelas 1 a 4 e os relatórios assinados são a resposta; ainda assim é onde mora a chance de derrota parcial (§7).

### 6.4 Roteiro B — acordo (racional, e eu recomendo os dois em paralelo)
A devedora **já confessou R$ 120.000,00 por escrito e pagou R$ 10.000,00** — sinal de disposição e de caixa apertado. Para o cliente, o acordo só vale se converter o crédito em **título executivo**, porque hoje ele não tem esse instrumento.

Estrutura mínima do instrumento de confissão de dívida / acordo:
1. **Assinatura do devedor + 2 testemunhas** → passa a ser **título executivo extrajudicial** (CPC art. 784 III; é justamente o requisito que falta no contrato de 2020). Em novo calote, **execução direta**, sem monitória.
2. Reconhecer **apenas o exigível** (R$ 110.000,00 + encargos). Não confessar as parcelas 5 e 6 como dívida exigível — e **não** contar que uma confissão posterior "ressuscita" dívida já prescrita: **a biblioteca não contém fundamento para renúncia ou reconhecimento posterior de prescrição consumada (não verificado)**. Tratar valores de 5 e 6, se a ré os aceitar, como **vantagem econômica de negócio**, jamais como base de execução/registro/protesto.
3. Prazo curto (ex.: 3 a 6 parcelas trimestrais) + garantia (fiança dos sócios ou garantia real/penhor de bem da atividade).
4. **Cláusula de retratação da negativação**: manter a inscrição retilificada (R$ 110.000,00 + encargos) durante o cumprimento e excluí-la no pagamento — assim a pressão continua lícita.
5. Foro de Sorocaba e cláusula de aceleração em caso de atraso.

**Números de negociação (sem IPCA, até 12/10/2026):**

| Cenário de acordo | Valor |
|---|---|
| Teto do pedido em juízo | **R$ 194.390,00** + IPCA |
| Acordo à vista com perdão de 50% dos juros | **R$ 153.395,00** |
| Acordo à vista, só principal + multa (piso duro) | **R$ 112.400,00** |
| Custo de esperar 12 meses (só juros) | **R$ 13.200,00** + IPCA |

Referência de decisão: com o IPCA ainda por computar, **qualquer proposta acima de ~R$ 150.000,00 à vista** é provavelmente melhor que o litígio; entre **R$ 112.000,00 e R$ 150.000,00** depende de garantia + instrumento com 2 testemunhas (abaixo disso, só com garantia forte, porque o desconto equivale a renunciar aos encargos que já estão ganhos documentalmente). A ré ter caixa apertado sugere **parcelar com título executivo** em vez de perdoar valor.

### 6.5 Sequência recomendada
1. **Semana 0:** retificar a negativação (R$ 180.000,00 → R$ 110.000,00 + encargos) e documentar; instruir o cliente a não mencionar as parcelas 5 e 6 em nenhuma peça de cobrança, planilha ou mensagem.
2. **Semana 1–2:** proposta formal de acordo com instrumento de confissão (2 testemunhas) e garantia; prazo de resposta de 15 dias.
3. **Sem acordo (≈60 dias):** distribuir **monitória** (Sorocaba) pelo exigível **e** requerer **protesto** restrito ao mesmo valor.
4. **Agenda:** não deixar a ação entrar em agosto/2027 sem ter sido distribuída; reavaliar se o IPCA e as respostas de `QUESTIONS.md` alteram o valor do pedido.

---

## 7. Riscos, divergências e o que não fechei

| # | Ponto | Natureza |
|---|---|---|
| 1 | **IPCA não calculado** — valor do pedido subestimado; totais são nominais + multa + juros | **Lacuna de dados** (Q1). Deixei em aberto, sem forçar |
| 2 | Imputação do PIX de R$ 10.000,00 (principal × encargos) — diferença de R$ 3.890,00 e do enquadramento da negativação | **Ambiguidade real** (§4.3), dois cenários quantificados. O cliente confirmou (12/10/2026) que não houve outro pagamento nem trouxe regra/documento sobre a ordem de imputação — a regra legal **não está na biblioteca (não verificado)**; cenário principal mantido |
| 3 | Legitimidade das 3 negativações anteriores da ré — condição de aplicação da Súmula 385 | **Fato desconhecido** — o cliente **não dispõe** da informação (Q3 sem resposta). Risco de dano moral mantido como "baixo, **condicionado**" |
| 4 | Prova do serviço de fev/mar (parcelas 5/6) | **Resolvido (12/10/2026):** relatórios assinados pelo encarregado existem, um por parcela; greve de fev/2021 confirmada e serviço admitido como parcial ("fizemos o que deu"). Só interessa à mesa de negociação — as parcelas seguem prescritas |
| 5 | Risco de revisão de encargos / limitação dos juros | **Não verificado** (não há regra na biblioteca) |
| 6 | Detalhes procedimentais da monitória e efeitos do protesto | **Não verificado** (fora do trecho da biblioteca) |
| 7 | Contagem de prazo (CC art. 132) | **Não verificado**; imaterial para as conclusões |
| 8 | Tese de que o PIX reconheceu todo o contrato (+R$ 102.320,00) | Possível, **fraca**; o cliente não dispõe de documento posterior que trate das parcelas 5/6 (Q6, 12/10/2026) — a tese não tem matéria-prima nova e segue fora do pedido (§3.1) |

## 8. Resposta direta ao cliente ("não prescreveu nada, certo?")
**Não.** R$ 120.000,00 foram salvos pelo e-mail de 15/09/2022, que vale até 15/09/2027; o PIX de 2023 não salvou nada — ele só abate R$ 10.000,00. As parcelas de fevereiro e março de 2021, que a própria devedora contestou por escrito, **prescreveram em 10/02/2026 e 10/03/2026**. E a execução que o cliente quer ajuizar não é cabível: sem 2 testemunhas, o contrato não é título — a via é **monitória** (ou cobrança). Por fim: a negativação de R$ 180.000,00 feita em 12/08/2026 tem **R$ 70.000,00 indevidos** dentro dela, e isso precisa ser corrigido antes de o cliente protestar ou ajuizar qualquer coisa.

## 9. Diligência — respostas do cliente (12/10/2026): o que fechou e o que fica aberto

O cliente respondeu em 12/10/2026 e declarou **não dispor de mais informação** para as demais perguntas. Inventário honesto do efeito de cada resposta:

| Tema (pergunta) | Resposta do cliente | Efeito no trabalho |
|---|---|---|
| Assinatura do contrato (Q4) | "Só os dois representantes, sem testemunhas. Foi tudo meio informal" | **Fechado:** premissa virou fato; sem certificação digital, Tema 1.247/STJ fora; **via definitivamente monitória**. A única porta para execução direta é o acordo com 2 testemunhas (§6.4) |
| Outros pagamentos (Q2) | Só os R$ 10.000,00 de ago/2023 "por conta da primeira parcela"; "depois sumiram" | **Fechado:** principal exigível **R$ 110.000,00** e negativação indevida em **R$ 70.000,00** confirmados. Sem contato desde ago/2023, não há ato posterior que altere a prescrição |
| Serviço de fev/mar (Q7) | "Teve uma greve lá em fev/2021, mas nosso pessoal fez o que deu. Temos relatórios assinados pelo encarregado deles" | **Fechado (para nosso uso):** relatórios assinados existem para as 6 parcelas (o arquivo já os listava, um por parcela). Força na negociação; a admissão "fizemos o que deu" é confissão de serviço parcial — reforça **não** litigar as parcelas 5 e 6, hoje prescritas de qualquer modo |
| Renegociações após set/2022 (Q6) | Sem informação; do que relatou ("depois sumiram"), não houve contato após ago/2023 | Upside de R$ 102.320,00 (§3.1) permanece **fraco e sem matéria-prima**; nada muda no pedido |
| IPCA (Q1) | Sem informação | **Permanece aberto e sem solução ao nosso alcance:** totais seguem **sem correção monetária** e materialmente **subestimados**. Se a planilha aparecer, o recálculo é mecânico (a memória por parcela já está pronta em `calculo_encargos.csv`) |
| 3 negativações anteriores (Q3); cartório/boletos (Q5); solvência da ré (Q9); ações/endereço (Q10) | Sem informação | **Desconhecidos sinalizados, sem suposição:** risco de dano moral tratado como "baixo, **condicionado**" à legitimidade das anteriores (§5); antes de protestar, confirmar instrução do cartório (§6.1); estrutura de garantia do acordo e diligências de citação devem ser verificados pelo patrono na distribuição/Sesa |

**Nenhuma resposta alterou as conclusões centrais** — via (monitória), prescrição (1–4 vivas até 15/09/2027; 5–6 prescritas), valores (R$ 110.000,00 exigíveis; R$ 60.000,00 prescritos; R$ 194.390,00 hoje, sem IPCA), retificação da negativação e protesto restrito. O que as respostas fizeram foi **reduzir o campo de hipóteses**: das 10 perguntas, 4 fecharam por fato ou documento (Q2, Q4, Q7, e Q8 — pois o contrato não contém cláusula de capitalização nem limitação de encargos, apenas "Multa 2%, juros 1% a.m., correção IPCA"), 1 fechou em negativo (Q6) e 5 permanecem como lacunas explícitas (Q1, Q3, Q5, Q9, Q10).

---
*Memorando elaborado a partir de `documents/` (arquivo do cliente), das respostas do cliente recebidas em 12/10/2026 e exclusivamente das fontes indexadas em `library/INDEX.md`. Itens marcados "não verificado" não têm suporte na biblioteca fechada e não foram usados como fundamento de conclusão.*
