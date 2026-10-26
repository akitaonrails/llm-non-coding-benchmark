# Memorando — Técnica Forte × Metalúrgica Boa Vista (R$ 180 mil, 2020/2021)

**Data:** 12/10/2026 · **Para:** Sérgio (Técnica Forte) · **Foro do contrato:** Comarca de Sorocaba/SP

## 1. Resumo executivo

1. **Execução do contrato NÃO é possível**: o contrato é particular **sem duas testemunhas** → não é título executivo extrajudicial (CPC art. 784 III); boleto bancário não é título executivo. Fonte: `library/cpc_titulo_executivo_monitoria.md`.
2. **Via correta: AÇÃO MONITÓRIA** (CPC art. 700), fundada no contrato assinado pelo devedor **+ relatórios de serviço assinados pelo encarregado da Boa Vista** (prova escrita sem eficácia de título executivo). REsp 1.438.263 admite monitória contra signatário de contrato sem testemunhas. Mesma fonte.
3. **Prescrição (5 anos, CC art. 206 §5º I):** o e-mail de 15/09/2022 (reconhecimento das parcelas 1–4, CC art. 202 VI) interrompeu a prescrição **uma única vez** → novo termo 15/09/2027 para as parcelas 1–4. O PIX de 02/08/2023 foi novo reconhecimento, mas **não interrompe novamente** ("somente poderá ocorrer uma vez", CC art. 202 caput). **Parcelas 5 e 6 estão PRESCRITAS** (10/02/2026 e 10/03/2026) — nunca foram reconhecidas: foram **contestadas** no mesmo e-mail.
4. **Negativação (Serasa, 12/08/2026, R$ 180.000):** indevida em **R$ 70.000** (R$ 60 mil das parcelas 5–6 prescritas + R$ 10 mil já pagos) — inscrição de dívida prescrita é indevida e enseja cancelamento e, em tese, dano moral; a indenização tende a ser **afastada pela Súmula 385/STJ** porque há 3 inscrições legítimas anteriores (2024–2025) não contestadas. Corrigir a inscrição imediatamente.
5. **Protesto: NÃO recomendado** pela via do contrato inteiro: seria feito sobre dívida em parte prescrita → indevido e gera responsabilidade (REsp 1.792.700; Lei 9.492/97). Protesto do exigível é possível, mas não agora (ver §6).
6. **Números-chave** (aritmética no §4): principal exigível **R$ 110.000**; parcelas prescritas (intocáveis) **R$ 60.000**; já pago **R$ 10.000**; soma 110.000 + 60.000 + 10.000 = **R$ 180.000** ✓ (fecha com o dito "R$ 180 mil").
7. **Regra de ouro: nada cobrar das parcelas 5 e 6** — pretensão extinta por prescrição. Quem cobrar dívida prescrita em cadastro/protesto assume risco de dano moral.

## 2. Fatos considerados (e lacunas assumidas)

- Contrato assinado em 01/09/2020 por ambas as partes, **sem testemunhas**; 6 × R$ 30.000, venc. dia 10, out/2020–mar/2021; multa 2%, juros 1% a.m., correção IPCA (`documents/contrato_prestacao_servicos.md`).
- Cada parcela com relatório de serviço **assinado pelo encarregado da Boa Vista**, incluindo parcelas 5 e 6 (`documents/boletos_e_comprovantes.csv`) — atentar: a Boa Vista alega que o serviço de fev/mar/2021 foi **interrompido pela greve** e não concluído (`documents/emails_reconhecimento.txt`); para o presente estudo **não silencio sobre isso**: como as parcelas 5–6 estão prescritas, a questão do serviço incompleto ficou **sem efeito prático** (não pode ser cobrada de qualquer forma). Não vou avaliar mérito do "greve" — desnecessário para as conclusões.
- E-mail de 15/09/2022: Boa Vista **reconheceu parcelas 1–4 (R$ 120.000)** e **contestou 5–6**.
- E-mail de 02/08/2023: PIX de **R$ 10.000 "por conta da parcela 1"**.
- Serasa: inscrição de 12/08/2026 por **R$ 180.000** (as 6 parcelas) — nota: o e-mail do cliente fala "mês passado", o documento diz 12/08/2026; **adoto 12/08/2026** (documentos prevalecem sobre e-mail verbal). Em qualquer das datas as conclusões não mudam (P5–6 já prescritas desde fev/mar/2026; PIX já efetuado em 2023).
- Consulta Serasa de hoje: **3 inscrições anteriores (2024–2025) não contestadas** — fato central para a Súmula 385 (§5).
- **Assunções declaradas** (não há dado no workspace para além disto — se algum fato abaixo estiver errado, o recálculo é trivial):
  a. Não existem **outros pagamentos** ou atos de reconhecimento do devedor além do PIX de R$ 10.000 (02/08/2023).
  b. O PIX é abatido do **principal** da parcela 1 (não de juros/multa primeiro).
  c. Juros: **1% a.m. simples pro rata die** (mês de 30 dias), desde o vencimento. O contrato não prevê capitalização; **não adoto juros compostos** — mostrar também a variante composta no §4 (R$ 229.944,48) só para referência.
  d. Multa **2% aplicada uma única vez** por parcela em mora, sobre o valor de face (R$ 600/parcela). (2% sobre saldo remanescente da P1 seria R$ 400; diferença irrelevante para o quadro.)
  e. **Correção IPCA não quantificada** — não há série do índice no workspace e a biblioteca não traz índices (ver STATUS.md, item aberto 1). Os números do §4 são principal + multa + juros, **sem correção monetária**.

## 3. Análise parcela a parcela (datas)

Base legal: pretensão de cobrança de dívida líquida em instrumento particular **prescreve em 5 anos** (CC art. 206 §5º I); vencimento = marco inicial (CC art. 189). Interrupção **somente uma vez**, por **ato inequívoco extrajudicial de reconhecimento do devedor** (CC art. 202 caput e VI); interrompida, recomeça **da data do ato** (art. 202 parágrafo único). Reconhecimento **parcial** interrompe **apenas quanto às parcelas reconhecidas**; o pagamento parcial posterior é novo reconhecimento, mas **não interrompe novamente** (`library/cc_prescricao_202_206.md`).

| # | Vencimento | Reconhecido? | Interrupção | Termo prescricional | Hoje 12/10/2026 |
|---|---|---|---|---|---|
| 1 | 10/10/2020 | Sim (e-mail 15/09/2022) | 15/09/2022 | **15/09/2027** | **Exigível** (saldo 20.000 após PIX) |
| 2 | 10/11/2020 | Sim | 15/09/2022 | **15/09/2027** | **Exigível** |
| 3 | 10/12/2020 | Sim | 15/09/2022 | **15/09/2027** | **Exigível** |
| 4 | 10/01/2021 | Sim | 15/09/2022 | **15/09/2027** | **Exigível** |
| 5 | 10/02/2021 | **Não** (contestada) | — | 10/02/2026 | **PRESCRITA** (há 8 meses) |
| 6 | 10/03/2021 | **Não** (contestada) | — | 10/03/2026 | **PRESCRITA** (há 7 meses) |

- **Sobre o e-mail de 15/09/2022**: no mesmo documento a Boa Vista **reconheceu 1–4** e **contestou 5–6**. Contestar não é reconhecer → **não interrompe** quanto a 5–6. Este ponto desmonta a premissa do cliente ("reconheceram a dívida por e-mail"): **reconheceram duas parcelas em quatro; as outras duas estão prescritas.**
- **Sobre o PIX de 02/08/2023 (R$ 10.000, parcela 1)**: pagamento parcial é reconhecimento, mas a interrupção **somente ocorre uma vez** — não recomeça o prazo novamente (`library/cc_prescricao_202_206.md`). Exatamente por isso o prazo das 1–4 termina em 15/09/2027 e **não depois**. E não "salva" 5–6: o pagamento foi **atribuído à parcela 1** pelo próprio devedor.
- **Sobre a inscrição no Serasa (12/08/2026)**: ato do **credor** não é reconhecimento do devedor (CC 202 VI exige ato do devedor); não interrompe.
- **Prazo fatal: monitória com despacho que ordena a citação até 15/09/2027** (CC art. 202 I e caput: despacho do juiz é modalidade de interrupção — recomendo não apostar numa "segunda interrupção", que a lei vedaria; ajuizar cedo).

## 4. Encargos e números (aritmética visível)

Método (assunções do §2, itens b–d): juros = saldo × 1% × (dias/30); multa 2% × valor de face, uma vez por parcela; **somente parcelas exigíveis (1–4)**, pago parcial abatido do principal (`library/juros_correcao.md`: "Cálculo parcela a parcela, apenas das parcelas exigíveis, abatido o pagamento parcial"; multa contratual 2%; juros contratuais 1% a.m. desde o vencimento; correção pelo índice contratual → CC arts. 389, 406).

| # | Saldo principal | Dias corridos (juros) | Juros (1% × dias/30) | Multa | Subtotal |
|---|---|---|---|---|---|
| 1 | 20.000 | 1.026 (até 02/08/2023, sal. 30.000) + 1.167 | 10.260,00 + 7.780,00 = 18.040,00† | 600,00 | **38.640,00** |
| 2 | 30.000 | 2.162 | 21.620,00 | 600,00 | **52.220,00** |
| 3 | 30.000 | 2.132 | 21.320,00 | 600,00 | **51.920,00** |
| 4 | 30.000 | 2.101 | 21.010,00 | 600,00 | **51.610,00** |
| **Σ exigível** | **110.000** | — | **81.990,00** | **2.400,00** | **194.390,00** |
†Detalhe da parcela 1: 30.000 × 1% × (1.026/30) = 10.260,00 até o PIX; depois 20.000 × 1% × (1.167/30) = 7.780,00. Variantes não adotadas, apenas registradas: cobrar juros também sobre os R$ 10.000 já pagos, até a data do pagamento, somaria +3.420,00.

- **Sensibilidade (transparência):** com juros **compostos** 1% a.m. (não adotado), o subtotal de principal+encargos das 1–4 seria **229.944,48** (juros ~117.544,48) + multa 2.400. **Não pedirei isso**: anatocismo sem cláusula expressa é questionável; o número simples (194.390,00) é defensável e provavelmente o que um juízo fixaria. A diferença de ~R$ 35 mil entre as duas bases define a zona de negociação em eventual acordo.
- **Correção IPCA: valor aberto.** Não há série IPCA no workspace, e a biblioteca não traz índices. Manter no **pedido** (contrato prevê IPCA; CC art. 389) e **quantificar na liquidação** com a tabela oficial; sem isso não invento número.
- **O que NÃO entra na conta:** parcelas 5–6 (60.000) — prescritas, pretensão extinta, **zero encargos sobre elas**.

## 5. Vias processuais

| Via | Viável? | Por quê |
|---|---|---|
| **Execução** | ❌ | Contrato particular **sem 2 testemunhas** não é título (CPC 784 III); exceção eletrônica (Tema 1.247) **não aplicável** — assinaturas simples, conforme documento do cliente; **boleto não é título**. `library/cpc_titulo_executivo_monitoria.md` |
| **Monitória** | ✅ **recomendada** | CPC art. 700 — prova escrita sem eficácia de título: **contrato assinado + relatórios de serviço assinados pelo encarregado** + e-mail de reconhecimento de 15/09/2022. REsp 1.438.263: monitória contra signatário de contrato sem testemunhas. Súmulas 299 e 503/STJ (mesma fonte) admitem a monitória e cavam o quinquenal; aqui, contudo, o termo vem diretamente do CC art. 206 §5º I (5 anos, ver §3). Pedido: pagamento de R$ 110.000 + encargos, com expedição de mandado e formação de título executivo judicial se não houver embargos (art. 701, CPC). |
| **Cobrança (comum)** | ✅ alternativo | Sem eficácia de título, procedimento comum com dilação; só se preferir custo menor ou questões probatórias. Monitória domina aqui pela qualidade da prova escrita. |

**Foro:** Comarca de Sorocaba/SP (contrato).

## 6. Negativação e protesto

**Negativação (12/08/2026, R$ 180.000):**
- Regular quanto a: **R$ 110.000** (saldo principal exigível). Indevida quanto a: **R$ 70.000** = parcelas 5–6 prescritas (60.000) + parcela 1 paga (10.000). 70.000 + 110.000 = 180.000 ✓ (fecha com a inscrição feita).
- Risco: inscrição de **dívida prescrita é indevida** — texto: "a pretensão está extinta; o registro não pode ultrapassar o prazo prescricional" (CDC art. 43 §5º por analogia; STJ Tema 1.264; REsp 1.792.700) — `library/negativacao_prescrita_sumula385.md`. Dano moral **em tese** configurado, **mas** a indenização tende a ser **afastada (Súmula 385)** por 3 inscrições legítimas anteriores (2024–2025) não contestadas; **ressalvado o direito ao cancelamento** (que é dever imediato).
- **Ação: corrigir JÁ.** Manter R$ 110.000 (encargos documentáveis à parte, se o cadastro comportar com liquidação mínima); excluir tudo que exceda. Isso corta a vantagem processual de Boa Vista e reduz risco de ação por dano moral — que hoje é mitigada pela Súmula 385, mas não única (custas, pedido de cancelamento, publicidade do erro, eventual abertura para discussão sobre a parte exigível).

**Protesto (contrato inteiro, como pede o cliente): ❌ NÃO.**
- Protesto sobre dívida **prescrita** é **indevido e gera responsabilidade**; protesto pressupõe **dívida exigível** (Lei 9.492/97; art. 1º admite protesto de documento de dívida sem força executiva, "mas sempre quanto a dívida exigível"). `library/negativacao_prescrita_sumula385.md`.
- O documento a protestar (contrato de R$ 180.000 carrega **R$ 70.000 indevidos** dentro de si) não separa sozinho o exigível do prescrito. Protestar o todo = risco de responsabilidade análogo ao do cadastro.
- **Se o cliente insistir em protesto depois** da correção da inscrição: possível protestar o exigível (impacto: intimação formal; revérsia psicológica), mas prefiro a monitória, que produz título judicial e penhora com mais eficácia; protesto adiciona frente de vala sem vantagem prática aqui.

## 7. Estratégia: ação × acordo

**Proposta (from quadrilha mais forte a mais comoda):**
1. **D7:** corrigir inscrição Serasa (manter 110.000; excluir 70.000) — antes de qualquer novo gesto.
2. **D7–D30:** pre-notícia da Boa Vista (carta/e-mail): reconhecimento de 15/09/2022 + PIX + relatórios assinados; prazo 10 dias para proposta de acordo; sem acordo, ajuizamento.
3. **Ação:** monitória em Sorocaba/SP, valor da causa **R$ 110.000 + R$ 84.390 (multa 2.400 + juros 81.990, sem correção) = R$ 194.390** (+ IPCA a liquidar). Prazo interno: despacho de citação **até 15/09/2027** (prazoTableRow seria de mora internar demais).
4. **Acordo (alvo):** proposta de **R$ 130.000–150.000** à vista ou parcelado curto (não invento índice): recupera todo o principal exigível (110.000) + parte dos encargos; **descarta as 5–6 prescritas com quitação geral daquelas** — troca o risco procesal por liquidez. Se Boa Vista pedir mais desconto, o ponto mínimo interno é **principal + multa (112.400)**; abaixo disso, prefiro monitória.
5. **Nunca** incluir 5–6 em pedido, cadastro ou protesto; **nunca** aceitar acordo que "baixe" a 5–6 sem **cláusula de renúncia geral e exclusão do cadastro** quanto a tudo.

## 8. Citações (todas em `library/INDEX.md`)

- `library/cc_prescricao_202_206.md` — CC arts. 189, 202 (caput, VI, ¶ único), 206 §5º I (reconhecimento parcial; pagamento parcial posterior não interrompe novamente).
- `library/cpc_titulo_executivo_monitoria.md` — CPC arts. 700, 784 III; Súmulas 299, 503/STJ; REsp 1.438.263.
- `library/negativacao_prescrita_sumula385.md` — Súmula 385/STJ; REsp 1.792.700; Lei 9.492/97; CDC art. 43 §5º (por analogia); STJ Tema 1.264.
- `library/juros_correcao.md` — CC arts. 389, 406 (Lei 14.905/2024); multa 2%, juros 1% a.m., correção IPCA; cálculo parcela a parcela • exigíveis • abatido o pago parcial.

*Tudo que não está no INDEX foi omitido; onde a biblioteca silencia (ex.: índices IPCA), declaro lacuna em vez de citar.*
