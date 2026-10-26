# QUESTIONS — Atlas Distribuidora S.A. (rodada 3, 26/10/2026)

O cliente informou que **não tem informação adicional** e pediu para **não repetir perguntas já
respondidas**. Este arquivo foi reduzido ao que ainda é preciso pedir. **Uma única pendência de
execução**: os dados de fevereiro e março. Todo o resto deixou de ser pergunta e passou a registro —
assunções adotadas (§ 3) e desconhecidos fechados em `deliverable/UNKNOWN.md` (U-01 … U-17).

**Não repetiremos** perguntas já respondidas sobre: brindes, doação à Associação Luz, NF-e 8812 / crédito
de PIS/COFINS, compensação do prejuízo.

---

## 1. Único pedido em aberto — os arquivos que destravam as sessões 2 e 3

`documents/` contém **somente** `mes_01/` (razão, balancete, NF-e 8812), `balancete_abertura.csv`,
`saldos_fiscais_abertura.md` e `email_diretor.txt`. Não fabricamos razão nem balancete.

| # | Arquivo | Observação |
|---|---|---|
| 1.1 | `documents/mes_02/razao.csv` | mesmo layout de `documents/mes_01/razao.csv` (data, ref, conta, histórico, débito, crédito) |
| 1.2 | `documents/mes_02/balancete.csv` | posição em 28/02/2026 |
| 1.3 | `documents/mes_03/razao.csv` | idem |
| 1.4 | `documents/mes_03/balancete.csv` | posição em 31/03/2026 — é a base do e-LALUR do trimestre |

Com esses quatro arquivos, fevereiro e março fecham com os mesmos procedimentos que fecharam janeiro e o
trimestre apura no e-LALUR. O roteiro já está escrito e testado em janeiro: testes **T1–T7** de
`deliverable/mes_02/ajustes.json` e § 10 de `deliverable/mes_03/memoria.md`.

Utilidades opcionais, que aceleram mas **não bloqueiam**: detalhamento por documento das contas 4.2.02
(*Despesas comerciais*) e 4.2.03 (*Despesas administrativas*) dos três meses, e a ECF do exercício anterior
(comprova os R$ 900.000,00 de prejuízo fiscal e os R$ 900.000,00 de base negativa de abertura).

## 2. Perguntas novas: nenhuma

As duas perguntas da rodada 2 (competência dos brindes e da doação; existência de documento de suporte)
foram feitas e encerradas pela resposta "não tem informação adicional". Tratamos como **desconhecido
registrado** (U-03, U-04, U-05 em `deliverable/UNKNOWN.md`) e seguimos o engajamento com a linha de adição
criada e sem valor no e-LALUR — nunca omitida.

## 3. Assunções adotadas para o que ficou sem resposta (registro, não pergunta)

| Item sem resposta | Tratamento adotado |
|---|---|
| Brindes (vinho + canivete, 400 clientes) e doação à Associação Luz | **Indedutíveis por existência** (Lei 9.249/95, art. 13, VII e VI; a entidade não tem utilidade pública federal nem qualificação de OSCIP, então o § 2º, II não se aplica). Valor ausente → linha `null` no `lalur.json`; exposição por teto demonstrável em `mes_01/brindes_doacoes.md`. Nenhuma estimativa entrou na apuração |
| Competência dos brindes/doação | Assunção declarada: 1T2026. Se forem de 4T2025, a adição correta é de e-LALUR/ECF de 2025 (modelo de correção em `mes_03/ajustes.json`, AJ-04) |
| Situação da EFD-Contribuições/DAS de 01/2026 | Apuração correta entregue (a recolher **R$ 79.883,00** vs. R$ 68.783,00 da empresa). Se já transmitida/paga: EFD retificadora + recolhimento de R$ 11.100,00. Acréscimos **não calculados** — norma ausente na biblioteca (U-06/U-07) |
| Saldos de abertura (R$ 900.000,00 × 2) | Carregados na Parte B **como declarados**, com ressalva, até vir a ECF anterior (U-08) |
| Compensação integral do prejuízo pedida pelo diretor | **Não atendida.** Teto de 30% do lucro líquido ajustado (Lei 9.065/95, arts. 15-16; RE 591.340/Tema 117). Compensar R$ 900.000,00 exigiria lucro ajustado trimestral de R$ 3.000.000,00 (23,35× janeiro) |
| "Não mexer" no crédito da NF-e 8812 | **Não atendida** em janeiro (AJ-01/2026-01, R$ 11.100,00). O destaque do fornecedor não gera crédito; uso e consumo não é insumo (`library/pis_cofins_uso_consumo.md`) |
| Provisão de IRPJ/CSLL do trimestre em março | Recomendada como modelo (AJ-03, contas novas 4.3.02/2.1.05), rotulada **não verificável**: a biblioteca não traz norma contábil (U-13) |
| ICMS/IPI, juros de 2.1.04, depreciação fiscal, tributação diferida | **Não verificáveis** com a biblioteca fornecida (`library/INDEX.md`) → U-07, U-09 … U-13; nenhum ajuste, nenhuma afirmação de conformidade |

## 4. Custo de decidir cada caminho (números para a decisão, sem repetir pergunta)

Se o valor de brindes/doação nunca vier (U-03, U-04, U-05), o e-LALUR sai com a adição não quantificada. O efeito por
R$ 1.000,00 de adição omitida, com o saldo de R$ 900.000,00 disponível (a trava de 30% absorve parte):

| Situação | Acréscimo de IRPJ+CSLL por R$ 1.000,00 omitido |
|---|---|
| Com trava de 30% e adicional de 10% incidindo (é o caso da Atlas) | **R$ 238,00** |
| Com trava de 30%, lucro real abaixo de R$ 60.000 no trimestre | R$ 168,00 |
| Sem saldo a compensar, com adicional | R$ 340,00 |
| Sem saldo a compensar, sem adicional | R$ 240,00 |
| Sem a trava, mas com saldo suficiente (ilegal; serve só para medir o diferimento) | R$ 0,00 no trimestre — a adição consome 1.000,00 do saldo e o tributo sai dos trimestres futuros (U-17: a biblioteca não dá prazo ao crédito) |

Aritmética: a adição eleva o lucro antes da compensação em 1.000,00, o teto em 300,00 e o lucro real em
700,00 → 0,34 × 700,00 = 238,00 (Lei 9.249/95, art. 13; Lei 9.065/95, arts. 15-16; Lei 9.430/96, arts.
1º-2º — `library/lei9249_art13.md`, `library/lei9065_art15_trava.md`, `library/irpj_csll_trimestral.md`).
No teto demonstrável de janeiro (R$ 85.000,00 a R$ 181.000,00), isso significa **R$ 20.230,00 a
R$ 43.078,00** de diferença de tributo no regime aplicável à Atlas (trava de 30% + adicional de 10%); se o
lucro real trimestral ficasse abaixo de R$ 60.000,00, a forquilla seria de R$ 14.280,00 a R$ 30.408,00.
Memória completa em `deliverable/mes_03/memoria.md` § 8.
