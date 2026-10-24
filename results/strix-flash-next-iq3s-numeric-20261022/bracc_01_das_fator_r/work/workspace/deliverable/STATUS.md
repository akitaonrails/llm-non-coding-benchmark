# STATUS

**COMPLETE WITH OPEN ITEMS**

Apuração do DAS de **maio/2026** concluída e entregue, usando **exclusivamente** os arquivos de
`workspace/library/` (citados por nome) e os documentos do pacote em `workspace/documents/`.
Rodada 2: as respostas do cliente (22/10/2026) foram aplicadas; **o valor não mudou**.
Rodada 3: a entrega foi **revisada item a item contra as fontes** e corrigida em **16 pontos**
(alegações que não constam dos documentos, aritmética de cenários, **a conta indicativa de
junho/2026 refeita**, rotulagem de inferência x texto de lei, e um novo unknown — U9).
**O valor apurado não mudou.** A lista do que mudou e o motivo de cada correção está em `REVISAO.md`.

## Resultado apurado

| Item | Valor |
|---|---|
| RBT12 (mai/25–abr/26) | R$ 1.020.000,00 |
| Folha 12 meses | R$ 284.600,00 |
| Fator R | 27,90% (< 28%) → serviços no **Anexo V** |
| 4ª faixa | nominal 20,50% − PD 17.100,00 → efetiva **18,8235%** |
| Serviços (NFS-e 1181–1187 − estorno 1188) | R$ 78.000,00 → DAS **14.682,35** |
| Locação de notebooks (NF-e 512) | R$ 6.000,00 → Anexo III c/ dedução do ISS, efetiva **8,4415%** → DAS **506,49** |
| **DAS maio/2026** | **R$ 15.188,84** (carga do mês 18,08%) |

Convenção de arredondamento: **cada bloco ao centavo e depois somado** (o valor a recolher é apurado
por anexo); as conferências exatas aparecem em `memoria.md` §6.2.

Extrato de maio/2026 100% conciliado (créditos 88.000,00; débitos 43.180,22; saldo final 86.100,33);
o PDF e o CSV descrevem **exatamente o mesmo extrato** (conferência em `memoria.md` §8.1).

Toda a aritmética foi **repetida em `Decimal` por um validador independente**: **87 verificações**
(RBT12, folha, fator R, efetivas, DAS, repartição, cenários, conciliação do extrato e o bloco indicativo
de junho/2026), **todas PASS**; as somas das fontes `faturamento_12_meses.csv`,
`resumo_folha_12_meses.csv` e `extrato_maio_2026.csv` batem com o `apuracao.json` sem resíduo.

## Open items (não verificados — detalhe em `QUESTIONS.md` / `PERGUNTAS.md`)

1. **U1 (material)** — folha **paga** na janela mai/25–abr/26 não comprovada por documentos de
   pagamento; a linha 2026-03 do resumo tem pró-labore = 0 sem explicação. Se a folha paga for
   ≥ 285.600,00 (margem atual: R$ 1.000,00), os serviços migram para o **Anexo III** e o DAS cai
   para **10.261,08** (−4.927,76).
2. **U2** — composição do RBT12 (bruta / líquida de cancelamentos / inclui locação / outras receitas).
3. **U3** — classificação de consultoria de arquitetura e treinamento: listas de atividades dos
   anexos **não existem na biblioteca** → NÃO VERIFICADO NA BIBLIOTECA (efeito conhecido: −284,30,
   DAS 14.904,54).
4. **U4** — DAS abr/2026 pago (10.480,22 = 12,05% da receita de abril) é incompatível com Anexo V;
   confrontos **indicativos** porque o RBT12 de abr/2025–mar/2026 não consta do pacote: Anexo V
   16.376,47 · Anexo III 10.880,12 · segregado 10.636,25. Apuração anterior não refeita.
5. **U5** — repartição por tributo dos serviços **NÃO APURADA** (tabela do Anexo V ausente da
   biblioteca; só a do Anexo III, 4ª faixa, foi usada — aplicada à locação).
6. **U6** — tabela de repartição da biblioteca soma 99,85%: componentes 505,36 x DAS locação 506,49
   (diferença 1,13). Divergência registrada, não corrigida por ajuste próprio. Sensibilidade: com a
   lacuna imputada ao ISS (redutor 67,35%), locação 505,36 e DAS **15.187,71** (−1,13).
7. **U7** — destaque de PIS/COFINS na NF-e 512 (39,00 + 180,00 = 219,00): a vedação aplicável não
   está na biblioteca; sem efeito sobre o DAS.
8. **U8** — CNAE/PGDAS-D da locação e possíveis retenções de ISS na fonte (lista de serviços do
   município ausente do pacote).
9. **U9** — base de apuração da faixa/alíquota efetiva de **cada bloco** segregado (RBT12 global x
   RBT12 da atividade): a biblioteca **não disciplina**. Adotada a leitura literal do art. 18, §1º-A
   (RBT12 global, premissa P6). Leitura alternativa, não adotada e ilustrativa: locação na 1ª faixa do
   Anexo III → 243,00 e DAS **14.925,35** (−263,49).

Premissas declaradas (**P1–P7**) estão destacadas em `memoria.md` e `apuracao.json`. As duas que
sustentam o bloco da locação são **inferências documentadas**: **P6** (faixa pelo RBT12 global) e
**P7** (redutor de ISS de 67,50% lido da repartição do Anexo III, 4ª faixa — o texto da biblioteca
manda deduzir "a parcela correspondente ao ISS" sem fixar percentual). O comprovante de pagamento do
pró-labore em 30/04/2026 **não** integra `documents/` — a data é alegação do cliente.

Nada foi inventado: itens fora da biblioteca estão marcados como NÃO VERIFICADO NA BIBLIOTECA e os
valores que não reconciliam foram mostrados como divergência, sem forçar fechamento.

## Arquivos entregues

- `workspace/deliverable/apuracao.json` — schema completo do contrato + cenários, premissas, unknowns
- `workspace/deliverable/memoria.md` — memória de cálculo com a aritmética e as citações da biblioteca
- `workspace/deliverable/REVISAO.md` — o que mudou na revisão (rodada 3) e o motivo de cada item
- `workspace/deliverable/QUESTIONS.md` — unknowns restantes (U1–U9), sem repetir o que foi respondido
- `workspace/deliverable/PERGUNTAS.md` — resumo em português dos unknowns
- `workspace/deliverable/STATUS.md` — este arquivo
