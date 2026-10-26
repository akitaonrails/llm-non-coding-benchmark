# Pendências — fevereiro/2026 (sessão 2/3)

**Status da sessão: BLOCKED.** Não há razão analítico nem balancete de fevereiro no workspace. `documents/`
contém apenas `mes_01/`, `balancete_abertura.csv`, `saldos_fiscais_abertura.md` e `email_diretor.txt`.
Na rodada 3 (26/10/2026) o cliente informou que *não tem informação adicional*.

Por isso, os entregáveis de fevereiro (`ajustes.json`, `pis_cofins.json`) foram entregues **com a estrutura
do contrato e valores `null`**, acompanhados do roteiro de cálculo e dos testes que serão rodados no minuto
em que os arquivos chegarem. **Nenhum número de fevereiro foi estimado, simulado ou "carregado" de janeiro**:
`null` significa "não apurado", não "zero".

---

## 1. O que bloqueia (e é uma única coisa)

**Pedido único e suficiente:** `documents/mes_02/razao.csv`, `documents/mes_02/balancete.csv`,
`documents/mes_03/razao.csv`, `documents/mes_03/balancete.csv`, no mesmo layout dos de janeiro.

Com esses quatro arquivos, fevereiro e março fecham com os mesmos procedimentos que fecharam janeiro
(tie-out, débito por 9,25%, teste de crédito insumo × uso e consumo, varredura do art. 13) e o trimestre
apura no e-LALUR. Sem eles, nada há o que apurar — e é também a causa das lacunas U-01, U-02, U-14 e U-15
de `deliverable/UNKNOWN.md`.

Não vamos repetir perguntas já fechadas: brindes, doação, Associação Luz e NF-e 8812 já foram
respondidos pelo cliente e estão consolidados em `deliverable/UNKNOWN.md`.

## 2. Roteiro de fechamento de fevereiro (pronto para executar)

| # | Teste | Regra / fórmula | Fundamento na biblioteca |
|---|---|---|---|
| T1 | Tie-out razão × balancete | soma por conta do razão = saldo do balancete; Σ D = Σ C; abertura de fevereiro = balancete ajustado de 31/01/2026 (`mes_01/ajustes.json`: 2.1.03 = 997.683,00 C; 1.1.04 = 0,00) | regra de números do CONTRACT.md |
| T2 | Débito PIS/COFINS | receita bruta tributável × 9,25% (PIS 1,65% + COFINS 7,60%), confrontado com a conta 3.1.02 | `library/pis_cofins_uso_consumo.md` (alíquotas usadas em janeiro) |
| T3 | Crédito válido × crédito indevido | só gera crédito o insumo da atividade; uso e consumo administrativo **não** gera. Procurar CFOP 1556, "uso e consumo", papel/toner/escritório/limpeza/EPI, e qualquer crédito destacado em despesa | Lei 10.637/2002, art. 3º; Lei 10.833/2003, art. 3º; IN RFB 2.121/2022, art. 176; REsp 1.221.170/PR — `library/pis_cofins_uso_consumo.md` |
| T4 | Baixa contábil do crédito | crédito válido compensado com a obrigação: D 2.1.03 / C 1.1.04 (padrão AJ-02/2026-01) | idem T3 |
| T5 | Indedutíveis do art. 13 | brindes e doações identificadas nas descrições de 4.2.02/4.2.03/4.2.04 viram **adição no e-LALUR** do trimestre (sem lançamento societário) | Lei 9.249/95, art. 13, VI e VII; § 2º — `library/lei9249_art13.md` |
| T6 | Depreciação | comparar taxa contábil com a tabela fiscal; diferença vai ao e-LALUR | **não verificável**: a biblioteca não tem tabela fiscal (U-10) |
| T7 | Provisão de IRPJ/CSLL | não deve haver provisão mensal: a apuração é trimestral | `library/irpj_csll_trimestral.md` |

Em janeiro, T1 a T5 produziram ajustes reais: estorno de **R$ 11.100,00** (AJ-01) e compensação de
**R$ 155.067,00** (AJ-02). A probabilidade de repetição em fevereiro é alta porque se trata da rotina de
compras da mesma sede (uma única ocorrência no razão de janeiro, refs `NF8812`, linhas 36-38 de
`documents/mes_01/razao.csv`).

## 3. Limite do que a biblioteca permite afirmar

A biblioteca reproduz do art. 13 da Lei 9.249/95 **apenas os incisos VI (doações) e VII (brindes)** e o
§ 2º; o texto vem truncado ("[...]"). Logo:

- podemos afirmar a indedutibilidade de **brindes e doações**;
- **não** podemos afirmar que "não há outras indedutíveis no mês", porque os demais incisos do caput não
  estão na biblioteca. Se aparecer no razão uma despesa tipicamente vedada (multa, despesa pessoal,
  representação), o item será marcado como **não verificável com a biblioteca fornecida** e submetido ao
  cliente, nunca tratado como conformidade.

Da mesma forma, continuam fora do escopo verificável: ICMS/IPI (inclusive o "7% líquido de créditos" de
R$ 177.800,00 e eventual crédito na NF-e 8812), dedutibilidade de juros de empréstimo e partes
relacionadas, depreciação fiscal, acréscimos legais e tributação diferida (`library/INDEX.md` — U-07,
U-09 a U-13 de `UNKNOWN.md`).

## 4. Alertas que atravessam o trimestre

1. **"Compensar todo o prejuízo" não será atendido.** A compensação tem teto de **30% do lucro líquido
   ajustado pelas adições e exclusões** (Lei 9.065/95, arts. 15 e 16; Lei 8.981/95, arts. 42 e 58;
   RE 591.340/Tema 117 — `library/lei9065_art15_trava.md`). Com o único mês conhecido (R$ 128.483,00),
   o teto demonstrável é 128.483,00 × 30% = **R$ 38.544,90**; para consumir os R$ 900.000,00 seria
   preciso lucro líquido ajustado trimestral de **R$ 3.000.000,00** (23,35× janeiro).
2. **Saldos de abertura sem comprovação.** Prejuízo fiscal e base negativa de R$ 900.000,00 cada
   (`documents/saldos_fiscais_abertura.md`) serão carregados na Parte B **como declarados**, com ressalva,
   até que venha a ECF anterior (U-08).
3. **Brindes e doação permanecem sem valor.** Serão adicionados ao e-LALUR quando quantificados; enquanto
   não forem, a linha fica `null` no `mes_03/lalur.json` (não omitida), com exposição por teto em
   `mes_01/brindes_doacoes.md` (U-03 a U-05).

## 5. Consequência para o status

Fevereiro: **BLOCKED** (falta dado de entrada). Janeiro: **COMPLETE WITH OPEN ITEMS**. Trimestre:
**BLOCKED** — a apuração de IRPJ/CSLL de um trimestre não pode ser feita com 1 mês de 3; o e-LALUR
entregue em `deliverable/mes_03/` é estrutural (chaves do contrato, fundamentos e fórmula), com
`simulações` rotuladas como simulação. Ver `deliverable/STATUS.md`.
