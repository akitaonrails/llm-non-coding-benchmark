# STATUS — engajamento Atlas Distribuidora S.A., 1º trimestre/2026

## Status do engajamento (rodada 3, 26/10/2026): **BLOCKED**

**Motivo único e objetivo**: as sessões 2 e 3 dependem de dados de entrada que não existem no
engajamento. `documents/` contém **somente** `mes_01/razao.csv`, `mes_01/balancete.csv`,
`mes_01/nf_8812_papel_cia.md`, `balancete_abertura.csv`, `saldos_fiscais_abertura.md` e
`email_diretor.txt`. Não há razão nem balancete de fevereiro ou de março, e o cliente declarou em
26/10/2026 **não ter informação adicional**. Não fabricamos saldos, faturamento nem despesas de meses
sem documento.

Situação por sessão: **sessão 1 (01/2026) = COMPLETE WITH OPEN ITEMS** · **sessão 2 (02/2026) =
BLOCKED** · **sessão 3 (03/2026 + e-LALUR) = BLOCKED**.

O bloqueio é de **dado**, não de análise: os entregáveis obrigatórios das três sessões estão **presentes
e estruturados**, com as chaves obrigatórias do `CONTRACT.md` preenchidas com `null` onde falta número
(`null` = não apurado, **não** zero). O trabalho produzível sem dado — fundamentação linha a linha,
fórmula executável, testes prescritos, limites demonstráveis e simulações rotuladas — foi feito.

**Alerta operacional:** `deliverable/mes_03/lalur.json` **não deve ser transmitido** enquanto as chaves
obrigatórias estiverem `null`. Ele é o esqueleto auditável da apuração, não a apuração.

---

## Arquivos entregues (inventário)

| Arquivo | Conteúdo | Estado |
|---|---|---|
| `mes_01/ajustes.json` · `mes_01/pis_cofins.json` · `mes_01/pendencias.md` | janeiro apurado | **numérico** |
| `mes_01/balancete_ajustado.csv` · `mes_01/brindes_doacoes.md` | apoio: balancete quadrado e qualificação fiscal de brindes/doação | numérico |
| `mes_02/ajustes.json` · `mes_02/pis_cofins.json` · `mes_02/pendencias.md` | fevereiro: lançamentos vazios + checklist **T1–T7** + apuração `null` | **estrutural** |
| `mes_03/ajustes.json` · `mes_03/pis_cofins.json` · `mes_03/pendencias.md` | março: modelos AJ-01…AJ-04 + apuração `null` | **estrutural** |
| `mes_03/lalur.json` | e-LALUR do trimestre com as chaves fixas do contrato (Parte A e Parte B), valores `null` onde falta dado, trava de 30% parametrizada e simulações A–D | **estrutural** |
| `mes_03/memoria.md` | memorial: fundamento linha a linha, fórmulas, demonstração da trava, cenários, § 10 roteiro de fechamento | completo |
| `UNKNOWN.md` | **17 desconhecidos (U-01 … U-17)** com efeito `[BLOQUEIA]` / `[VALOR]` / `[RESSALVA]` e a forma de encerrar cada um | completo |
| `QUESTIONS.md` | rodada 3: **um único pedido** (4 arquivos), nenhuma pergunta repetida, assunções adotadas | completo |

Conferência mecânica feita em 26/10/2026: os 7 arquivos `.json` do `deliverable/` carregam sem erro
(mes_01: 2 · mes_02: 2 · mes_03: 3);
todas as chaves obrigatórias de `lalur.json` (inclusive `parte_b.prejuizo_fiscal_saldo_final` e
`parte_b.base_negativa_csll_saldo_final`) e de `pis_cofins.json` (`debito, creditos, estornos,
a_recolher, retificacoes`) estão presentes em todos os meses; `mes_01/ajustes.json` tem partida dobrada
fechada (débitos = créditos = R$ 166.167,00).

## Sessão 1 de 3 — fechamento de 01/2026 (`deliverable/mes_01/`) — COMPLETE WITH OPEN ITEMS

Números conferidos: razão × balancete batem conta a conta (14 contas); balancete original
R$ 19.880.584,00 (D=C) e ajustado R$ 20.046.751,00 (D=C); resultado contábil do mês 139.583,00 →
**128.483,00** após o estorno; lucro operacional R$ 156.483,00 (base do limite de 2% do art. 13, § 2º, II
→ R$ 3.129,66).

- **AJ-01/2026-01** — estorno do crédito indevido de PIS/COFINS da NF-e 8812 (material de uso e consumo
  administrativo, CFOP 1556): R$ 11.100,00 (120.000,00 × 9,25%); custo do material passa a R$ 131.100,00.
  Fundamento: Lei 10.637/2002 art. 3º, Lei 10.833/2003 art. 3º, IN RFB 2.121/2022 art. 176, REsp
  1.221.170/PR (`library/pis_cofins_uso_consumo.md`).
- **AJ-02/2026-01** — compensação do crédito válido de compras (1.676.400,00 × 9,25% = 155.067,00) contra
  2.1.03: só apresentação; 1.1.04 zera e 2.1.03 ajustado passa a R$ 997.683,00.
- **PIS/COFINS 01/2026** — débito R$ 234.950,00; créditos tomados R$ 166.167,00; estornos R$ 11.100,00;
  **a recolher R$ 79.883,00** (a Atlas apurou R$ 68.783,00 → subapuração de R$ 11.100,00); retificação da
  EFD-Contribuições de 01/2026.
- Apoio: `mes_01/balancete_ajustado.csv` e `mes_01/brindes_doacoes.md`.

### Itens abertos desta sessão (IDs em `UNKNOWN.md`)

1. **Brindes e doação: existência confirmada pelo cliente, valor ausente** (U-03, U-04, U-05). Vinho +
   canivete gravado a 400 clientes = **brinde** (Lei 9.249/95, art. 13, VII — a classificação em
   "marketing" não importa); contribuição à Associação Luz, sem título de utilidade pública federal nem
   qualificação de OSCIP = **doação indedutível** (art. 13, VI, fora do § 2º, II). Adição devida no
   e-LALUR, **não lançada por falta de valor** — teto material de janeiro R$ 85.000,00 (4.2.02) ou
   R$ 181.000,00 (4.2.02 + 4.2.03), exposição de R$ 20.230,00 a R$ 43.078,00 de IRPJ/CSLL — 23,8% da
   adição no caso da Atlas (trava de 30% + adicional de 10%), ou 16,8% se o lucro real trimestral
   ficasse abaixo de R$ 60.000,00).
2. **Competência dos brindes/doação desconhecida** (U-05) — se forem de 4T2025, a correção é de
   e-LALUR/ECF de 2025 (modelo AJ-04 em `mes_03/ajustes.json`), não deste trimestre.
3. **Acréscimos legais sobre R$ 11.100,00 não calculados** (U-06, U-07) — a norma de multa/juros não está
   na biblioteca; situação da EFD/DAS de 01/2026 desconhecida.
4. **Saldos de abertura (R$ 900.000,00 × 2) sem ECF que os comprove** (U-08) — carregados na Parte B como
   declarados, com ressalva.
5. **Não verificável por falta de norma na biblioteca** (U-09 … U-13 e U-17): juros de 2.1.04 (R$ 28.000,00/mês,
   credor não identificado), depreciação fiscal × contábil, tributação diferida, ICMS/IPI
   (R$ 177.800,00 "7% líquido de créditos"), desdobramentos de PIS/COFINS/ICMS/IPI em brinde e doação de
   bens e **prazo/decadência do prejuízo fiscal** — os saldos de abertura são tratados como compensáveis sem
   limite de prazo porque a biblioteca não traz regra de prazo alguma (U-17).
6. **Instruções do diretor não atendidas** (U-16) — "não mexer" no crédito de janeiro (o argumento "o
   fornecedor destacou, então creditamos" foi refutado: destaque não gera crédito, insumo gera) e
   "compensar todo o prejuízo" (trava de 30% — Lei 9.065/95, arts. 15-16; RE 591.340/Tema 117; para
   compensar R$ 900.000,00 seria preciso lucro ajustado trimestral de R$ 3.000.000,00 = 23,35× janeiro, e
   mesmo ignorando a trava a compensação não poderia passar do lucro do trimestre).

## Sessão 2 de 3 — fechamento de 02/2026 (`deliverable/mes_02/`) — BLOCKED (entregues em estrutura)

- `mes_02/ajustes.json` — `lancamentos: []` (nenhum lançamento pode ser escrito sem o razão) e o
  **checklist T1–T7** a executar na chegada dos dados: T1 tie-out razão × balancete, T2 PIS/COFINS = 9,25%
  sobre a receita, **T3 caça a crédito de uso e consumo (repetição do erro da NF-e 8812 — U-14)**, T4 baixa
  do crédito válido contra 2.1.03, T5 varredura das vedações do art. 13 (U-15), T6 depreciação
  (U-10), T7 ausência de provisão mensal de IRPJ/CSLL (U-13).
- `mes_02/pis_cofins.json` — campos `debito/creditos/estornos/a_recolher` em `null` e `apurado: false`;
  registrada a herança de janeiro (o crédito de 01/2026 já foi absorvido por AJ-02, então fevereiro não
  recomeça com saldo de 1.1.04).
- Base de continuidade disponível: `mes_01/balancete_ajustado.csv` é o numerário de abertura de fevereiro.

## Sessão 3 de 3 — março/2026 e e-LALUR do 1T2026 (`deliverable/mes_03/`) — BLOCKED (entregues em estrutura)

- `mes_03/lalur.json` — todas as chaves fixas do contrato presentes; `null` em
  `lucro_liquido_contabil`, `lucro_antes_compensacao`, `compensacao_prejuizo`, `lucro_real`, `irpj_15`,
  `adicional_10`, `csll` e nos dois saldos da Parte B. As **linhas de adição existem com valor `null`**
  (brindes; doação; demais incisos do art. 13 não reproduzidos na biblioteca) — criar e não omitir é o
  que permite ao revisor ver que a adição é devida e está não quantificada.
- Trava parametrizada: `compensacao = MIN(30% × lucro_antes_compensacao; saldo_de_abertura)`, com a
  abertura de R$ 900.000,00 × 2 marcada como `_abertura_declarada_pela_empresa` (U-08).
- `mes_03/ajustes.json` — modelos AJ-01 (estorno de crédito indevido, se T3 acusar), AJ-02 (baixa do
  crédito válido), AJ-03 (provisão do IRPJ/CSLL do trimestre — **rotulada não verificável**, a biblioteca
  não traz norma contábil) e AJ-04 (correção de 4T2025, se a competência dos brindes/doação for 2025);
  retificações referenciadas: EFD-Contribuições 01/2026 e e-LALUR/ECF 4T2025.
- `mes_03/memoria.md` — fundamento linha a linha, fórmulas executáveis, a demonstração aritmética de que
  a compensação integral é impossível, os quatro cenários e a sensibilidade marginal.
- `mes_03/pis_cofins.json` — PIS/COFINS **não tem apuração trimestral**; o consolidado está `null` porque
  fevereiro e março não foram apurados.

### Dimensionamento demonstrável (SIMULAÇÃO, não apuração)

Hipótese declarada: fevereiro e março repetem o resultado ajustado de janeiro (R$ 128.483,00).

| Cenário | Lucro antes da compensação | Teto 30% | Lucro real | IRPJ + adicional + CSLL | Parte B |
|---|---|---|---|---|---|
| A — 3 × jan, sem adições | 385.449,00 | 115.634,70 | 269.814,30 | **85.736,87** | 784.365,30 |
| B — A + brindes 85.000 | 470.449,00 | 141.134,70 | 329.314,30 | **105.966,87** | 758.865,30 |
| C — A + brindes e doação 181.000 | 566.449,00 | 169.934,70 | 396.514,30 | **128.814,87** | 730.065,30 |
| D — só janeiro conhecido | 128.483,00 | 38.544,90 | 89.938,10 | **24.578,96** | 861.455,10 |

Leituras úteis: a trava de 30% consome **4,28%** do saldo com o único mês conhecido e **12,85%** no ritmo
de janeiro (absorção completa em ≈ 7,8 trimestres) — ela **difere** o crédito, não o elimina. No cenário A,
três estados do mesmo trimestre: **sem compensar nada** paga 125.052,66 e preserva os 900.000,00;
**com a trava (o devido)** paga **85.736,87** e preserva 784.365,30; **sem trava** (contra legem, e ainda
assim limitada ao lucro do trimestre) pagaria 0,00 agora e preservaria 514.551,00. Compensar o que a lei
permite economiza **R$ 39.315,79** agora; a trava custa **R$ 85.736,87** agora e guarda R$ 269.814,30 de
saldo para os trimestres seguintes — **diferimento, não perda**. Compensar os 900.000,00 é impossível até
sem a trava, porque a compensação não pode exceder o lucro do trimestre (detalhe em `mes_03/memoria.md` § 8).
Cada R$ 1.000,00 de
adição não quantificada custa **R$ 238,00** de IRPJ/CSLL (R$ 168,00 se o lucro real trimestral ficar abaixo
de R$ 60.000,00). Convenção de arredondamento: cada linha arredondada em 2 decimais (half-up) e os totais
somando as linhas arredondadas, como no e-LALUR/DAS; por isso os totais podem diferir até R$ 0,01 da
soma dos valores exatos.

## O que destrava as sessões 2 e 3

1. **Os quatro arquivos** de `QUESTIONS.md` § 1: `documents/mes_02/razao.csv`,
   `documents/mes_02/balancete.csv`, `documents/mes_03/razao.csv`, `documents/mes_03/balancete.csv`
   (mesmo layout de janeiro). Nada mais é necessário para fechar número.
2. Utilidades que aceleram sem bloquear: detalhamento por documento de 4.2.02 e 4.2.03 (fecha U-03/U-04) e
   ECF do exercício anterior (fecha U-08).

Com esses dados, `mes_03/lalur.json` sai com: lucro líquido contábil do trimestre, adições (brindes e
doação quantificados), exclusões, lucro antes da compensação, **compensação limitada a 30%**, lucro real,
IRPJ 15%, adicional de 10% sobre o que exceder R$ 60.000,00 no trimestre, CSLL 9% e Parte B com os saldos
remanescentes. Roteiro executável em `mes_03/memoria.md` § 10. O status final do engajamento só será
`COMPLETE` (ou `COMPLETE WITH OPEN ITEMS`) depois desses números.

**Se os quatro arquivos não existirem, o engajamento permanece `BLOCKED`.** Não há estimativa, run-rate ou
proxy que substitua a apuração de Lucro Real: usar número inventado produziria um e-LALUR transmitível e
falso, o que é pior que entregar em estrutura.
