# Status do engajamento — Atlas Distribuidora S.A. (recuperação judicial)

**Status global: COMPLETE WITH OPEN ITEMS.**
Os 7 entregáveis das 3 sessões previstas no `CONTRACT.md` estão escritos e validados tecnicamente. O que resta
aberto é **falta de dado do cliente** (o cliente afirmou não ter informação adicional), tratado como premissa
declarada — não como número inventado. Nenhuma reconciliação foi forçada.

## Entregáveis

| Sessão | # | Arquivo | Situação |
|---|---|---|---|
| 1 | 1 | `deliverable/sessao1/resposta_diretor.md` | completo — resposta ao CFO (pagar a Norte fora do plano é ilegal; rota legal para o tributo federal) |
| 1 | 2 | `deliverable/sessao1/classificacao_creditos.json` | completo — 7 credores, 13.540.000,00, esquema do contrato validado, confere com `documents/relacao_credores.csv` |
| 1 | 3 | `deliverable/sessao1/demonstrativo_mensal_aj.md` | completo — contas mensais do art. 52, IV (caixa, pós-pedido, concursais, UPI) |
| 2 | 4 | `deliverable/sessao2/analise_plano.md` | completo — cláusula a cláusula, teste de cabimento (runway de caixa), 9 riscos, ramos do galpão |
| 2 | 5 | `deliverable/sessao2/efeito_tributario_desagio.json` | completo — 7 chaves do esquema + `_notas`; artefato irmão `efeito_tributario_desagio_sensibilidade.md` |
| 3 | 6 | `deliverable/sessao3/lancamentos_novacao.json` | completo — 9 lançamentos L1–L9 (todos D == C, L5 em **memorando**, L9 sem importe por falta de valor contábil), 6 itens **não lançáveis**, 6 reconciliações abertas |
| 3 | 7 | `deliverable/sessao3/passivo_fiscal_solucao.md` | completo — nulidade da cláusula 4ª, Vias A/B/C da Lei 10.522/2002 com aritmética, sequência recomendada |

Perguntas: `deliverable/QUESTIONS.md` (numeração fixa 1–22, usada de forma consistente nas três sessões).

## Números que sustentam o trabalho (todos com conta aberta nos arquivos)

- Passivo total **13.540.000,00**; concursais **7.430.000,00** (trabalhista 960.000,00 / quirografário 6.050.000,00 /
  ME-EPP 420.000,00); extraconcursais **3.410.000,00** (Beta fiduciário 3.100.000,00 + Norte pós-pedido 310.000,00);
  tributário não sujeito ao plano **2.700.000,00**.
- Base do deságio **6.470.000,00** → passivo nominal renegociado **2.588.000,00** (120 × **21.566,67**, carência 24 m).
  Valor presente a 1,5% a.m. (premissa P9): **837.295,77** → ganho contábil **5.632.704,23**; teste dos 10% do CPC 48
  = **87,1%** → novação/extinção, não mera modificação.
- Classe trabalhista isolada: teste dos 10% dá **4,60%** (a 0,5% a.m.) e **8,90%** (a 1,0% a.m.) → **não** atinge o
  limite → baixa apenas com pagamento/revogação da obrigação; sem ganho autônomo (L2).
- IRPJ/CSLL corrente sobre a base fiscal prudente (deságio **nominal** 3.882.000,00 × 34% parâmetro) = **1.319.880,00**;
  tributo diferido passivo **595.239,44**.
- Passivo após a homologação, mantido o plano da minuta: **9.822.415,21**.
- Tributário federal: Via A (art. 10-A) **22.500,00/mês** por 120 meses; Via C (transação, art. 10-C, até 70% de
  desconto) **6.750,00/mês** e economia de **1.890.000,00**; Via B (§1º-B, 30% com prejuízo fiscal) só faz sentido com
  prejuízo confirmado. A transação legal dá **mais** desconto (70% / 120x) que a cláusula ilegal do plano
  (50% / 180x).

## Gaps não reconciliados (deliberadamente não lançados)

| Gap | Valor | Onde está registrado |
|---|---|---|
| Caixa 840.000,00 em 31/03/2026 × 5.750.000,00 de "pagamentos_pos_pedido" declarados | **4.910.000,00** de desembolso não explicado | `sessao1/demonstrativo_mensal_aj.md` §2; QUESTIONS nº 6 |
| Fornecedores extraconcursais do extrato de 31/03/2026 (1.480.000,00) × 310.000,00 pós-pedido da relação | **1.170.000,00** sem classificação pré/pós | `lancamentos_novacao.json` → `reconciliacoes_abertas`; QUESTIONS nº 19 |
| Fonte de recursos do plano (sem o CCB): parcelas de 120 meses = 5.130.400,00 × galpão previsto de 4.500.000,00 | **630.400,00** de gap já no cenário benigno | `sessao2/analise_plano.md` §6.2; `reconciliacoes_abertas` |
| Servir o CCB do Beta (3.100.000,00, em qualquer prazo) e ainda honrar o plano | esforço de **8.230.400,00** em 120 meses → **3.730.400,00** descobertos mesmo contando o galpão inteiro | `sessao2/analise_plano.md` §6.3 e tabela de cenários do CCB; `reconciliacoes_abertas` |
| Débito federal: Via A 5.130.400,00 × Via C 3.240.400,00 de déficit em 120 meses | economia nominal de **1.890.000,00** só pela escolha da via legal | `sessao3/passivo_fiscal_solucao.md` §4 (tabela comparativa) |
| Despesas da recuperação (AJ, advogados) e débitos estaduais/municipais | valor **desconhecido** — não lançado | QUESTIONS nº 20 e nº 22 |
| Valor contábil do galpão | **desconhecido** → L9 sem importe; ganho/perda da venda não mensurável | QUESTIONS nº 21; L9 |

## Premissas assumidas (numeração única nas três sessões)

P1 pedido entre 03/02/2026 e 12/03/2026 · P2 suspensão 12/03/2026→08/09/2026 (prorrogável até 07/03/2027) ·
P3 nenhum credor do plano é pessoa ligada · P4 geração de caixa +5.000,00/mês · P5 parcelas contadas da homologação ·
P6 prejuízo fiscal e base negativa = 0 · P7 alíquotas de 34% como parâmetro (**NÃO VERIFICADO**) · P8 galpão não
vendido até a homologação · P9 taxa de desconto 1,5% a.m. · P10 juros/encargos dos parcelamentos federais
(**NÃO VERIFICADO**) · P11 base concursal = classes III + IV = 6.470.000,00.

Tabela completa em `deliverable/sessao2/analise_plano.md` e no bloco `premissas` de
`deliverable/sessao3/lancamentos_novacao.json`.

## Itens NÃO VERIFICADOS (acreditamos ser direito, mas não constam da biblioteca — por isso não citamos)

Regime de UPI e art. 66-A da LRF · conteúdo integral dos arts. 41 e 58 e quóruns da assembleia · detalhe do art. 54,
§2º além do que está no excerto · alíquotas e regime de apuração de IRPJ/CSLL e a sede legal da trava de 30% fora dos
dispositivos nomeados pelo art. 50-A, II · responsabilidade de sócios,
administradores e avalistas · classificação como "mantido para venda" (IFRS 5) · juros, encargos e caducidade dos
parcelamentos federais · critérios e requisitos de transação tributária · procedimento de habilitação de créditos ·
base legal da classe IV (ME/EPP) · requisito de divulgação de incerteza significativa sobre continuidade.

Cada um aparece marcado no texto onde seria necessário; nada disso é base de lançamento nem de conclusão.

## Riscos que o cliente ainda precisa decidir (não são itens de informação)

1. **Retirar a União do plano e a cláusula 4ª** e aderir a parcelamento/transação antes da assembleia, para obter a
   CND-E (art. 57 da LRF; art. 191-A do CTN).
2. **Renegociar o CCB do Beta por acordo**, com carência longa, protegendo a linha de separação de pedidos — não
   brigar com o fiduciário.
3. **Não promover o pagamento do sinal de 925.000,00 à Norte** (ilegal; leva a destituição/convolação) e levar o
   risco de desabastecimento ao juízo e à administradora judicial.
4. **Resolver a essencialidade do galpão × linha de separação** antes de oferecer a venda no plano: se for o mesmo
   imóvel, a fonte de recursos do plano destrói a operação.

## Como os números foram produzidos

- `workspace/documents/gen_lancamentos_sessao3.py` é a **fonte única** dos valores de
  `deliverable/sessao3/lancamentos_novacao.json` (rodar `python3 workspace/documents/gen_lancamentos_sessao3.py` para
  regenerar; valida D == C em cada lançamento).
- `workspace/documents/calculos_sessao2.txt` guarda a aritmética da Sessão 2 (PV, teste dos 10%, sensibilidade por
  taxa, imposto).
- Nenhuma fonte fora de `library/` foi utilizada; `library/INDEX.md` foi conferido item a item.
