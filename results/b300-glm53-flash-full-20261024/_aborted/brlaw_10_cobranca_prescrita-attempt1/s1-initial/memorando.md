# MEMORANDO — Técnica Forte Ltda. × Metalúrgica Boa Vista Ltda.

**Data:** 12/10/2026 · **Assunto:** cobrança de R$ 180.000,00 (contrato de 01/09/2020) · **Preparado com:** exclusivamente os documentos recebidos e a biblioteca `library/`

## 1. Resposta rápida às três teses do cliente (Sérgio)

| Tese do cliente | Veredicto | Em uma frase |
|---|---|---|
| "Não prescreveu nada" | **Falso** | O e-mail de 15/09/2022 salvou **só as parcelas 1–4** (novos termos: **15/09/2027**); as parcelas 5–6 (R$ 60.000), expressamente **contestadas**, nunca foram interrompidas e **prescreveram em 10/02/2026 e 10/03/2026**. |
| "Quero EXECUTAR o contrato" | **Impossível** | O contrato foi assinado **sem testemunhas**: CPC art. 784, III exige devedor + **2 testemunhas**; boleto também não é título executivo. A via é **monitória** (CPC art. 700). |
| "Vou protestar" | **Não, por ora** | Protesto de **dívida prescrita** é indevido e gera responsabilidade (Lei 9.492; STJ). Para o exigível (R$ 110.000) protesto é tecnicamente possível, mas recomenda-se guardá-lo como medida de pressão **posterior**, jamais incluindo os R$ 60.000 prescritos. |

**Ação imediata obrigatória:** a inclusão no Serasa de **12/08/2026 por R$ 180.000** está **inflada em R$ 70.000** (60.000 prescritos + 10.000 já pagos) e **contém dívida prescrita**: corrigir hoje, para exclusão dos R$ 60.000 e ajuste do valor para **R$ 110.000**.

## 2. Fontes de fato usadas (todas do arquivo do cliente)

- `documents/contrato_prestacao_servicos.md`: 6 × R$ 30.000, venc. dia 10 de out/2020 a mar/2021; multa 2%; juros 1% a.m.; correção IPCA; **sem testemunhas**.
- `documents/emails_reconhecimento.txt`: (i) 15/09/2022 — Boa Vista **reconhece parcelas 1–4 (R$ 120.000)** e **contestou expressamente as parcelas 5–6** (serviço de fev/mar interrompido pela greve); (ii) 02/08/2023 — PIX de **R$ 10.000 "por conta da parcela 1"** ("restante em breve").
- `documents/boletos_e_comprovantes.csv`: as 6 parcelas têm relatório de serviço assinado pelo encarregado da Boa Vista (prova da execução).
- `documents/negativacao_e_consulta.md`: Serasa de 12/08/2026 por R$ 180.000; a Boa Vista já tem **3 inscrições anteriores (2024–2025), não contestadas**.

## 3. Raciocínio parcela a parcela (prescrição)

Regra da biblioteca: pretensão de cobrança de dívida líquida em instrumento particular prescreve em **5 anos** (CC art. 206, §5º, I); a interrupção se dá por **qualquer ato inequívoco, extrajudicial, de reconhecimento do direito pelo devedor** (CC art. 202, VI) e **só pode ocorrer uma vez**, **recomeçando** o prazo da data do ato (CC art. 202, parágrafo único). Nota expressa da biblioteca: **reconhecimento parcial interrompe apenas quanto às parcelas reconhecidas; o pagamento parcial posterior é novo reconhecimento, mas NÃO interrompe novamente**.

| Parcela | Vencimento | Termo original (+5 anos) | Ato interruptivo | Novo termo | Prescrita? |
|---|---|---|---|---|---|
| 1 | 10/10/2020 | 10/10/2025 | 15/09/2022 (e-mail) | **15/09/2027** | **Não** |
| 2 | 10/11/2020 | 10/11/2025 | 15/09/2022 (e-mail) | **15/09/2027** | **Não** |
| 3 | 10/12/2020 | 10/12/2025 | 15/09/2022 (e-mail) | **15/09/2027** | **Não** |
| 4 | 10/01/2021 | 10/01/2026 | 15/09/2022 (e-mail) | **15/09/2027** | **Não** |
| 5 | 10/02/2021 | 10/02/2026 | nenhum (contestada) | — | **Sim (10/02/2026)** |
| 6 | 10/03/2021 | 10/03/2026 | nenhum (contestada) | — | **Sim (10/03/2026)** |

Verificações:
- O reconhecimento de **15/09/2022** ocorreu **dentro do prazo prescricional de cada parcela reconhecida** (antes de 10/10/2025 … antes de 10/01/2026) → interrupção **válida** (CC art. 202, VI, e p. único).
- O e-mail interrompeu **somente parcelas 1–4**; as 5–6 foram **expressamente reconhecidas como não devidas** → termo original correu sem interrupção.
- Hoje, **12/10/2026** > **10/02/2026** e > **10/03/2026** → parcelas 5–6 **prescritas**.
- O PIX de **02/08/2023** (R$ 10.000, "por conta da parcela 1") é *novo reconhecimento*, mas **não interrompe pela segunda vez** (CC art. 202: "somente uma vez"; nota da biblioteca). Ele **não estende** o novo termo: **15/09/2027** permanece. O que ele faz: **abate R$ 10.000 do principal** da parcela 1.
- Sem o e-mail de 2022, todas as parcelas estariam prescritas desde 10/10/2025; contudo, **poupa-se só a metade reconhecida**: a contestação expressa das parcelas 5–6 custou **R$ 60.000**.

## 4. Números (contas demonstradas; script em `deliverable/calculo.py`)

### 4.1 Principal exigível

```
Parcela 1: R$ 30.000 − R$ 10.000 (PIX 02/08/2023) = R$ 20.000
Parcela 2: R$ 30.000              Parcela 3: R$ 30.000
Parcela 4: R$ 30.000
Principal exigível = 4 × 30.000 − 10.000               = R$ 110.000,00
Parcelas 5–6 (prescritas) = 2 × 30.000                 = R$  60.000,00  (excluídas)
```

### 4.2 Juros de mora — 1% a.m. contratuais, até 12/10/2026 (simples, 30 dias/mês, sem capitalização; começam no vencimento)

| Parcela | Base | Meses + dias* | Fórmula | Juros |
|---|---|---|---|---|
| 1 | 20.000 | 72 m + 2 d (72,0667) | 20.000 × 0,01 × 72,0667 | **14.413,33** |
| 2 | 30.000 | 71 m + 2 d (71,0667) | 30.000 × 0,01 × 71,0667 | **21.320,00** |
| 3 | 30.000 | 70 m + 2 d (70,0667) | 30.000 × 0,01 × 70,0667 | **21.020,00** |
| 4 | 30.000 | 69 m + 2 d (69,0667) | 30.000 × 0,01 × 69,0667 | **20.720,00** |
| | | | **Total juros** | **77.473,33** |

\* Ex.: parcela 1: 10/10/2020 + 72 meses = 10/10/2026; faltam 2 dias p/ 12/10/2026 → 72 + 2/30. Convenção declarada: mês comercial de 30 dias, juros **simples** (o contrato não autoriza capitalização).

### 4.3 Multa contratual de 2%

- Base adotada (conservadora): **saldo residual em mora** → 110.000 × 0,02 = **R$ 2.200,00** (p1: 20.000 × 2% = 400; p2–p4: 30.000 × 2% = 600 cada).
- Alternativa (parcela cheia no vencimento): 4 × 30.000 × 0,02 = R$ 2.400,00 → mudaria o total para **R$ 189.873,33**. Escolha a tese na inicial; a diferença é pequena.

### 4.4 Total estimado (sem correção)

```
Principal exigível            R$ 110.000,00
+ Juros (4.2)                 R$  77.473,33
+ Multa 2% (base residual)    R$   2.200,00
= TOTAL hoje                  R$ 189.673,33
```

- **Impossível quantificar aqui a correção pela IPCA** (índice contratual): a biblioteca NÃO traz a série do índice — nenhuma tabela de IPCA existe em `library/` ou `documents/`. O valor acima está **subestimado**; a correção será requerida na inicial com índice oficial (item aberto — ver §8 e `QUESTIONS.md`).
- Rol cresce ≈ **R$ 1.100/mês** em juros simples (0,01 × 110.000), mais correção. Cada mês de esperar custa isso.
- Reconciliação dos R$ 70.000 de excesso na negativação: 180.000 (lançado) − 110.000 (correto) = **70.000** = 60.000 prescritos + 10.000 já pagos.

## 5. Via processual — por que MONITÓRIA (e não execução, nem cobrança comum)

1. **Execução: descartada.** O contrato particular só é título executivo extrajudicial se assinado **pelo devedor E por 2 testemunhas** (CPC art. 784, III); este tem **apenas representantes das partes, sem testemunhas**. Tema 1.247/STJ (contrato eletrônico com assinatura digital) **não é aplicável** — o instrumento aqui é contrato comum em papel, assinado em 2020. Boleto bancário **não é título executivo**. Logo, "executar o contrato" como quer o cliente é tecnicamente inviável com o acervo atual.
2. **Monitória: possível e recomendada** (CPC art. 700): há **prova escrita sem eficácia de título executivo** — o próprio contrato assinado pelo devedor, os **relatórios de serviço assinados pelo encarregado da Boa Vista** (parcelas 1–4) e os **e-mails de reconhecimento e de pagamento parcial** da própria devedora. A celeridade e a possibilidade de converter-se em título executivo judicial tornam-na preferível à cobrança comum (plano B, se a monitória for contestada ou se o juízo assim orientar).
3. **Alcance da monitória: R$ 110.000 + encargos, tudo relativo às parcelas 1–4.** Incluir parcela prescrita na inicial = pedido de cobrança de pretensão extinta: risco de improcedência parcial, sucumbência e **reforço** da tese de inscrição indevida. Não incluir.
4. **Contrato sem testemunhas ≠ obstáculo à monitória:** REsp 1.438.263 da biblioteca trata exatamente do cenário de contrato sem testemunhas. O reconhecimento por e-mail (CC art. 202, VI) reforça a certeza do débito, mas **não cria** título executivo extrajudicial.

## 6. Negativação (Serasa) e protesto — correção e riscos

### 6.1 Saldo da negativação atual: o que é regular e o que é indevido

- **Lançado em 12/08/2026: R$ 180.000 (as 6 parcelas).**
- **Regular quanto a R$ 110.000**: parcelas 1–4, exigíveis (novos termos 15/09/2027), reconhecidas pela própria devedora. (Nota: ainda assim, o **valor lançado** está errado também aqui — a baixa do PIX de R$ 10.000 não foi feita; o valor *correto* de inscrição seria R$ 110.000.)
- **Indevido quanto a R$ 60.000**: parcelas 5–6, **prescritas** (10/02/2026 e 10/03/2026, antes da inscrição de 12/08/2026). Inscrição de dívida prescrita é **indevida** — a pretensão está extinta e o cadastro não pode ultrapassar o prazo prescricional (CDC art. 43, §5º **por analogia**; Tema 1.264/STJ; biblioteca: negativacao_prescrita_sumula385.md) → direito à **exclusão/cancelamento** e, em tese, responsabilidade.

### 6.2 Dano moral — risco para o cliente (Técnica Forte)

- A consulta Serasa revela **3 inscrições anteriores da Boa Vista (fornecedores diversos, 2024–2025), não contestadas**. Se legítimas, aplica-se a **Súmula 385/STJ**: *da anotação irregular em cadastro de proteção ao crédito, não cabe indenização por dano moral quando preexistente legítima inscrição, ressalvado o direito ao cancelamento*. Ou seja, a exposição a indenização por dano moral é **em tese baixa**, **mas resta intacta a obrigação de cancelar a porção indevida (R$ 60.000)** — e insistir no erro depois de apontado agrava o risco jurídico e enfraquece o cliente na eventual contestação da monitória.
- **Correção recomendada (hoje):** no Serasa, excluir as parcelas 5–6 e ajustar o valor de inscrição para **R$ 110.000**, documentando a baixa do PIX (02/08/2023). Comunicação escrita à Boa Vista, em tom conciliatório, junto com a proposta de acordo (§7) — a correção parcial vira gesto de boa-fé e blindagem.

### 6.3 Protesto

- **Protestar dívida prescrita: NUNCA.** É indevido e gera responsabilidade como a inscrição de dívida prescrita (mesma lógica da biblioteca: negativacao_prescrita_sumula385.md; Lei 9.492/97).
- **Protesto do exigível (R$ 110.000): tecnicamente admissível** — a biblioteca admite protesto de *documento de dívida* **sem força executiva** (Lei 9.492, art. 1º), mas **sempre quanto a dívida exigível**. Documentos que sustentariam o aponte: o contrato + relatórios assinados + e-mails de reconhecimento.
- **Recomendação: NÃO protestar agora.** Motivos: (i) o devedor **reconheceu** e **pagou parcialmente** — protestar quem já se confessou devedor endurece a relação e cria denúncia fácil de excesso de cobrança; (ii) a inscrição no Serasa **já é a pressão** existente; (iii) correção da negativação + trilha de boa-fé + monitória valem mais que o choque extra do protesto; (iv) protesto prévio expõe o cliente ao mesmo debate de dano moral/abuso que se quer evitar (apesar da Súmula 385). Protesto fica como **medida de pressão reservada**, a avaliar somente se: (a) o acordo fracassar; (b) a Boa Vista reincidir em irregularidade; (c) sempre **limitado ao exigível** (110.000 + encargos documentáveis), com base documental limpa.
- **Protesto não interrompe a prescrição**: não é ato judicial nem reconhecimento pelo devedor (CC art. 202, incisos — nenhum deles cobre protesto unilateral do credor); nada na biblioteca sugere o contrário — **não conte com eventual efeito interruptivo**.

## 7. Estratégia — ação × acordo (com números)

**Leitura de força:** o cliente tem **R$ 110.000 de principal blindado** (reconhecido por escrito e R$ 10.000 pagos) contra uma devedora que contesta o restante e **já está suja no Serasa** (3 inscrições). A defesa da devedora quanto às parcelas 5–6 provavelmente **vence por prescrição consumada**, sem discutir mérito (greve/serviço). Logo:

| Cenário | Valor esperado p/ hoje | Observação |
|---|---|---|
| **Acordo global** (alvo sugerido) | **120.000 − 135.000** | Quitação dos 110.000 + fatia dos encargos; parcelas curtas (não > 6 meses); plano escrito com reconhecimento da dívida 1–4 (lembrete técnico: **a prescrição só pode ser interrompida uma vez** — um acordo não alonga o termo de 15/09/2027; um *pagamento* em acordo, sim, abate principal); **baixa total do Serasa** como contrapartida. Isso tangibiliza as parcelas 5–6 por goodwill, sem depender de tese de renúncia à prescrição. |
| **Ajuizar monitória já (R$ 189.673,33 + IPCA)** | até **~190 mil** | Valor nominal máximo, mas: tempo, execução incerta, contestação provável (greve no mérito das 5–6 e discussão dos encargos), honorários. Rende título executivo judicial se ganhar. |
| **Ajuizar e ainda negociar** | combinado | A monitória desarma a defesa "só tática"; a citação em 2026 mata o risco de termo vencido e melhora a alavanca de negociação. |
| **Esperar/renegociar sem ação** | ruína | Custo de esperar: +R$ 1.100/mês (juros) e prazo fatal **15/09/2027**; se passar, TODOS os créditos caem (principal exigível → prescrito: −R$ 110.000). |

**Cronograma sugerido (12/10 → 15/09/2027):**
1. **Esta semana:** corrigir a inscrição no Serasa (excluir R$ 60.000; valor → R$ 110.000); documentar prova da correção.
2. **Até 20/10/2026:** notificação extrajudicial cordativa com proposta de acordo (R$ 120.000–135.000) e prazo de 10 dias.
3. **Se recusa/silêncio:** ajuizar **monitória** pelas **parcelas 1–4** (R$ 110.000 + multa 2% + juros 1% a.m. + correção IPCA) **ainda em 2026** — restam ~11 meses até o novo termo, mas ajuizar antes evita consumir mais juros e preserva a alavanca do acordo.
4. **Contingência:** protesto do exigível **só depois** de monitória e acordo fracassados, e **jamais** sobre parcela prescrita.

Sobre a contestação provável (parcelas 1–4): o reconhecimento escrito de 15/09/2022 e o pagamento parcial de 02/08/2023 fecham essa frente — não há o que discutir quanto à existência da dívida; resta eventual controvérsia sobre encargos (base da multa, capitalização) e da correção. A defesa de mérito (greve) tem suporte apenas para as 5–6, e essas já caíram por prescrição.

## 8. Hipóteses assumidas, lacunas e itens abertos

*Atualização 12/10/2026 — resposta do cliente recebida nesta rodada. Itens 1 e 3 revisados; só o item 1 alterou de premissa para fato (nenhuma cifra mudou).*

1. **[CONFIRMADO PELO CLIENTE]** não há pagamento após o PIX de R$ 10.000 de 02/08/2023: "Pagaram R$ 10 mil em agosto de 2023 por conta da primeira parcela. Depois sumiram." O principal exigível permanece **R$ 110.000** e o novo termo **15/09/2027** (um pagamento novo **abateria o principal**, mas **não reiniciaria a prescrição** — interrupção já usada uma única vez; CC art. 202, p. único).
2. **IPCA não quantificável:** não existe série do índice no acervo (biblioteca + documentos). A estimativa de R$ 189.673,33 é juros + multa **sem correção**; o valor real da correção será maior. Item aberto para a petição inicial/liquidação.
3. **[SEM INFORMAÇÃO ADICIONAL DO CLIENTE]** Sérgio diz "negativei mês passado", o documento da negativação indica **12/08/2026** (2 meses antes). Indagado (`PERGUNTAS.md`, item 2), o cliente declarou **não ter informações adicionais** — o desconhecido permanece, flagado. Adota-se a data **documentada: 12/08/2026**; nada muda em números nem no confronto "lançado R$ 180.000 × correto R$ 110.000".
4. **Não coberto pela biblioteca:** (a) "reviviscência"/efeito de reconhecimento de dívida JÁ prescrita (não se conta com ele de forma alguma); (b) eventual renúncia expressa à prescrição; (c) o detalhamento da taxa legal do CC art. 406 pós-Lei 14.905/2024 (a biblioteca cita o artigo sem especificar a taxa) — irrelevante aqui enquanto o contrato fixar 1% a.m., que prevalece como pactuado.
5. **Contrato silente sobre capitalização** → assumidos juros simples (sem anatocismo); a base da multa (residual × vencimento cheio) é uma escolha conservadora, explicitada no §4.3.

## 9. Citações (todas de `library/INDEX.md`)

- `cc_prescricao_202_206.md` — CC art. 202, VI (interrupção por reconhecimento extrajudicial; "somente uma vez"); CC art. 202, parágrafo único (recomeço do prazo); CC art. 206, §5º, I (5 anos, dívida líquida em instrumento particular); nota da própria biblioteca sobre reconhecimento parcial e sobre pagamento parcial como novo reconhecimento **sem** nova interrupção.
- `cpc_titulo_executivo_monitoria.md` — CPC art. 784, III (2 testemunhas para documento particular; contratos sem testemunhas não são executáveis; Tema 1.247 inaplicável; boleto não é título); CPC art. 700 (monitória); REsp 1.438.263 (contrato sem testemunhas); Súmulas 299 e 503 (monitória fundada em cheque prescrito é admissível; prazo quinquenal para ajuizamento de monitória contra emitente de cheque sem força executiva).
- `negativacao_prescrita_sumula385.md` — inscrição de dívida prescrita é indevida (CDC art. 43, §5º por analogia; Tema 1.264/STJ); direito ao cancelamento; Súmula 385/STJ (preexistência de inscrição legítima afasta dano moral, salvo cancelamento); REsp 1.792.700; Lei 9.492/97 (protesto; documento de dívida sem força executiva é protestável, mas somente dívida exigível).
- `juros_correcao.md` — CC art. 389 (mora, desde o inadimplemento); CC art. 406 c/ Lei 14.905/2024 (juros, se não pactuados — aqui pactuados); contrato (multa 2%, juros 1% a.m., correção IPCA), conforme `documents/contrato_prestacao_servicos.md`.
