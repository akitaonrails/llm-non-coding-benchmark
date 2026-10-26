# MEMORIA — e-LALUR do 1º trimestre de 2026 (Atlas Distribuidora S.A.)

**Aviso de escopo, logo no topo.** Este memorial documenta a apuração de IRPJ/CSLL do trimestre. A
apuração **não foi concluída**: só existe razão/balancete de janeiro (`documents/mes_01/`), e o cliente
declarou em 26/10/2026 (rodada 3) não ter informação adicional. Portanto `mes_03/lalur.json` está
entregue com as **chaves obrigatórias do contrato preenchidas com `null`** (= não apurado, não zero) e
este memorial entrega o que é produzível sem dado: o fundamento linha a linha, a fórmula executável, os
limites demonstráveis com o que há, e cenários **rotulados como simulação**. Nada aqui é estimativa
disfarçada de apuração.

Fontes: **somente** `library/INDEX.md` e os quatro arquivos nele listados. Tudo que extrapola essa
biblioteca está marcado **[NÃO VERIFICÁVEL]**.

---

## 1. Base factual disponível

| Item | Valor | Fonte |
|---|---|---|
| Resultado contábil ajustado de janeiro/2026 | R$ 128.483,00 (antes do estorno: 139.583,00) | `deliverable/mes_01/ajustes.json` |
| Lucro operacional de janeiro/2026 | R$ 156.483,00 | `deliverable/mes_01/ajustes.json` |
| Prejuízo fiscal em 31/12/2025 (Parte B) | R$ 900.000,00 — **declarado**, sem ECF | `documents/saldos_fiscais_abertura.md` |
| Base negativa de CSLL em 31/12/2025 (Parte B) | R$ 900.000,00 — **declarado**, sem ECF | idem |
| Fevereiro e março | **não entregues** | `documents/` (só há `mes_01/`) |

Regime: Lucro Real **trimestral** — IRPJ/CSLL apurados e recolhidos no fechamento do trimestre
(Lei 9.430/96, arts. 1º e 2º — `library/irpj_csll_trimestral.md`). PIS/COFINS têm fato gerador **mensal**
e por isso foram apurados mês a mês, independentemente do trimestre.

## 2. Parte A — `lucro_liquido_contabil`

Soma dos resultados contábeis dos três meses. Janeiro: **R$ 128.483,00**. Fevereiro e março: `null`.
Não se projeta fevereiro e março a partir de janeiro para compor a base tributável — isso seria inventar
fato gerador (regra de números do CONTRACT.md).

O resultado de janeiro já reflete o único ajuste societário do trimestre até agora (AJ-01, abaixo).
As adições do art. 13 **não** passam pela contabilidade: `library/irpj_csll_trimestral.md` é explícito —
despesas indedutíveis são adições na Parte A e "não se altera a contabilidade societária (CPC), apenas a
apuração fiscal".

## 3. Parte A — adições

### 3.1 Brindes (vinho + canivete gravado, 400 melhores clientes) — devido, valor ausente
**Fundamento:** Lei 9.249/95, art. 13, **VII** — "das despesas com brindes" é dedução vedada, para IRPJ
**e** CSLL (`library/lei9249_art13.md`). A resposta do cliente ("Marketing, ora.") não muda o resultado:
a vedação é por **natureza da despesa**, não por plano de contas. Valor: **não informado** → linha
`brindes_vinho_e_canivete_gravado_400_clientes: null` (U-03). Teto material demonstrável em janeiro:
R$ 85.000,00 (saldo da conta 4.2.02) — exposição por cenário em `mes_01/brindes_doacoes.md`.

### 3.2 Doação à Associação Luz — devido, valor ausente
**Fundamento:** art. 13, **VI** ("das doações, exceto as referidas no § 2º"). A exceção do **§ 2º, II**
exige entidade civil sem fins lucrativos **reconhecida como de utilidade pública federal ou qualificada
como OSCIP**, prestadora de serviços gratuitos à comunidade ou a empregados/dependentes do doador. O
cliente respondeu em 26/10/2026 que é "ONG do bairro, não tem título nenhum" → **nenhum dos dois
requisitos** está presente, então a doação cai na regra geral do inciso VI e é **indedutível**, e o limite
de 2% do lucro operacional nem chega a ser discutido. Valor: não informado → linha `null` (U-04).

Registro do limite, para o caso de a empresa regularizar a qualificação: 2% × lucro operacional de
janeiro (156.483,00) = **R$ 3.129,66** por mês/trimestre conforme a base mensal aqui apurada; com os
três meses, 2% × lucro operacional trimestral — ainda não calculável.

### 3.3 Estorno do crédito indevido de PIS/COFINS (NF-e 8812) — **NÃO é adição**
Correto tratá-lo aqui porque é a dúvida óbvia. O crédito indevido não é despesa indedutível: ele foi
**lançado a débito de um ativo (1.1.04)** que não existia. A correção (AJ-01/2026-01) estornou o crédito e
transferiu o tributo para o **custo do material** (4.2.04: 120.000,00 → 131.100,00), o que **reduziu o
resultado contábil** de 139.583,00 para 128.483,00. Ou seja, o efeito no lucro real já está dentro de
`lucro_liquido_contabil`; adicionar de novo seria tributar duas vezes o mesmo fato.
**Fundamento do estorno:** Lei 10.637/2002, art. 3º; Lei 10.833/2003, art. 3º; IN RFB 2.121/2022, art.
176; REsp 1.221.170/PR — uso e consumo não é insumo e não gera crédito (`library/pis_cofins_uso_consumo.md`).
O argumento do cliente ("o fornecedor destacou PIS/COFINS, então creditamos") foi refutado: o que gera
crédito é o bem ser **insumo da atividade**, não o destaque na nota.

### 3.4 Demais incisos do art. 13 — **[NÃO VERIFICÁVEL]**
`library/lei9249_art13.md` reproduz apenas os incisos VI e VII e o § 2º; o caput vem truncado ("[...]").
Consequência metodológica, que precisa ficar escrita: **não podemos afirmar que não há outras adições**
no trimestre, e também não podemos afirmar que há. Se a varredura dos razão de fevereiro/março mostrar
despesa típica de vedação (multa, despesa pessoal, representação), o item será submetido ao cliente como
**não verificável com a biblioteca fornecida**, nunca tratado como conformidade.

## 4. Parte A — `exclusões`

Entregue vazio (`{}`) porque nenhuma exclusão é identificável com o que há. Isso **não** é afirmação de
inexistência: depreciação fiscal maior que a contábil geraria exclusão, e não há tabela de depreciação
fiscal na biblioteca (**[NÃO VERIFICÁVEL]**, U-10). Também não há participação em coligadas, juros
dedutíveis/exclusões de receitas financeiras etc. documentados — porque não há razão de fevereiro/março.

## 5. Parte A — compensação de prejuízo (a trava de 30%)

**Fórmula executável** (Lei 9.065/95, arts. 15 e 16; Lei 8.981/95, arts. 42 e 58; STF RE 591.340, Tema
117 — `library/lei9065_art15_trava.md`):

```
lucro_antes_compensacao = lucro_liquido_contabil + adicoes − exclusoes
teto                    = 30% × lucro_antes_compensacao        (só se positivo)
compensacao             = MIN(teto; saldo_de_abertura − compensações de trimestres anteriores)
lucro_real              = lucro_antes_compensacao − compensacao
```

O texto legal fixa o teto sobre o **lucro líquido ajustado pelas adições e exclusões** — ou seja, 30% do
`lucro_antes_compensacao`, não 30% do lucro contábil antes das adições (o que daria teto **menor**) e não
30% do próprio lucro real (o que daria conta circular). A mesma trava se aplica à base negativa da CSLL
(art. 16), com o mesmo saldo de R$ 900.000,00: como os dois saldos são iguais e não há exclusões, a
compensação das duas é igual neste trimestre.

**A instrução do diretor ("fecha o trimestre com o prejuízo fiscal todo compensado") não será atendida.**
Demonstração aritmética, sem apelação:

```
compensar tudo exige:  900.000,00 ≤ 0,30 × lucro_antes_compensacao
                    ⇔  lucro_antes_compensacao ≥ 900.000,00 / 0,30 = R$ 3.000.000,00
comparação:            3.000.000,00 / 128.483,00 = 23,35× o resultado de janeiro
```

Ou, pelo lado do aproveitamento: com o único mês conhecido, o teto é 128.483,00 × 30% = **R$ 38.544,90**,
apenas **4,28%** do saldo. No ritmo de janeiro repetido três vezes, o teto do trimestre seria
385.449,00 × 30% = **R$ 115.634,70** (**12,85%** do saldo), e levaria ≈ **7,8 trimestres** (~2 anos) para
absorver os R$ 900.000,00. A trava **não elimina** o crédito fiscal — apenas o difere; a biblioteca nada
diz sobre prazo de expiração (**[NÃO VERIFICÁVEL]**).

**Ressalva sobre a base:** os R$ 900.000,00 de abertura são **declarados** pela empresa; nenhum ECF/DIRPJ
anterior foi entregue (U-08). Carregamos a Parte B com esse valor **com ressalva** — se a ECF divergir,
mudam o saldo, a compensação e o tributo.

## 6. Parte A — IRPJ, adicional e CSLL

```
irpj_15       = 15% × lucro_real
adicional_10  = 10% × MAX(0; lucro_real − 60.000,00)      (limite de R$ 60.000 NO TRIMESTRE)
csll          = 9%  × lucro_real
```
(Lei 9.430/96, arts. 1º-2º; Lei 9.249/95, art. 3º; IN RFB 1.700/2017, arts. 29 e 310 —
`library/irpj_csll_trimestral.md`.)

**Leitura adotada e sinalizada:** o adicional incide sobre o `lucro_real` **já reduzido** pela compensação,
porque o texto da biblioteca define o adicional sobre "a parcela que exceder R$ 60.000 no trimestre" em
relação ao lucro real. A biblioteca não detalha a ordem compensação → adicional; isso é **interpretação
nossa**, não fato verificado. Se o cliente quiser a outra leitura (adicional sobre a base antes da
compensação), o adicional cresce — calculamos na hora se for solicitado.

## 7. Parte B — controle de saldos a compensar

```
prejuizo_fiscal_saldo_final          = 900.000,00 − compensacao_prejuizo
base_negativa_csll_saldo_final       = 900.000,00 − compensacao_csll   (art. 16, mesma trava)
```
Valores `null` porque a compensação depende da apuração do trimestre inteiro. A abertura de R$ 900.000,00
para cada saldo está registrada no arquivo como **`_abertura_declarada_pela_empresa`**, com a ressalva da
ausência de ECF.

## 8. Cenários (SIMULAÇÃO — não é apuração)

Hipótese única e declarada: fevereiro e março repetem o resultado ajustado de janeiro (R$ 128.483,00).
Serve para dimensionar a trava e o custo de não quantificar brindes/doação. **Não** preenche as chaves
`null` do `lalur.json`.

| Cenário | Lucro antes da compensação | Teto 30% | Compensação | Lucro real | IRPJ 15% | Adicional 10% | CSLL 9% | **Tributo total** | Parte B (saldo) |
|---|---|---|---|---|---|---|---|---|---|
| **A** — 3 × jan, sem adições | 385.449,00 | 115.634,70 | 115.634,70 | 269.814,30 | 40.472,15 | 20.981,43 | 24.283,29 | **85.736,87** | 784.365,30 |
| **B** — A + brindes 85.000 | 470.449,00 | 141.134,70 | 141.134,70 | 329.314,30 | 49.397,15 | 26.931,43 | 29.638,29 | **105.966,87** | 758.865,30 |
| **C** — A + brindes e doação 181.000 | 566.449,00 | 169.934,70 | 169.934,70 | 396.514,30 | 59.477,15 | 33.651,43 | 35.686,29 | **128.814,87** | 730.065,30 |
| **D** — só janeiro (1 mês conhecido) | 128.483,00 | 38.544,90 | 38.544,90 | 89.938,10 | 13.490,72 | 2.993,81 | 8.094,43 | **24.578,96** | 861.455,10 |

Carga efetiva sobre o lucro contábil: A 22,24% · B 22,61% · C 22,74% · D 19,13%.

**Convenção de arredondamento** (para que qualquer total daqui seja reproduzível): arredondamos **cada
linha** em 2 decimais (half-up) e somamos as linhas arredondadas — é o formato do e-LALUR e da DAS. O
desvio em relação à soma dos valores exatos é de até R$ 0,01 (no cenário A o total exato é 85.736,865).

Aritmética do cenário A, passo a passo (para conferência manual): 

```
lucro antes        3 × 128.483,00            = 385.449,00
teto               0,30 × 385.449,00         = 115.634,70   (menor que 900.000,00 → compensa o teto)
lucro real         385.449,00 − 115.634,70   = 269.814,30
IRPJ               0,15 × 269.814,30         =  40.472,145 → 40.472,15 (2 dec.)
adicional          0,10 × (269.814,30 − 60.000,00 = 209.814,30) = 20.981,43
CSLL               0,09 × 269.814,30         =  24.283,287 → 24.283,29 (2 dec.)
total                                        =  85.736,87   (22,24% do lucro antes da compensação)
```

Quanto custa a trava (cenário A, três estados possíveis — a diferença entre eles é toda de **tempo**, não
de valor definitivo):

| Estado do 1T2026 (cenário A) | Compensado | Lucro real | IRPJ | Adicional | CSLL | Tributo agora | Parte B (saldo) |
|---|---:|---:|---:|---:|---:|---:|---:|
| sem compensar nada | 0,00 | 385.449,00 | 57.817,35 | 32.544,90 | 34.690,41 | 125.052,66 | 900.000,00 |
| **devido: trava de 30%** | 115.634,70 | 269.814,30 | 40.472,15 | 20.981,43 | 24.283,29 | **85.736,87** | 784.365,30 |
| sem trava (ilegal; e ainda assim limitado ao lucro do trimestre) | 385.449,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 514.551,00 |

Leituras: (i) compensar o que a lei permite economiza **R$ 39.315,79** agora (125.052,66 − 85.736,87) e
preserva R$ 784.365,30 para os trimestres seguintes; (ii) a trava de 30% custa **R$ 85.736,87** de tributo
pago agora, mas preserva R$ 269.814,30 de saldo (784.365,30 − 514.551,00) — **é diferimento, não
perda**, desde que haja lucro nos trimestres seguintes (a biblioteca não trata de prazo/decadência do
prejuízo fiscal: U-17); (iii) o pedido do diretor ("compensar todo o prejuízo", R$ 900.000,00) é
impossível **mesmo sem a trava**, porque a compensação não pode passar do lucro do trimestre: no ritmo de
janeiro o teto seria o próprio lucro, R$ 385.449,00. Aritmética: IRPJ 0,15 × 385.449,00 = 57.817,35;
adicional 0,10 × (385.449,00 − 60.000,00 = 325.449,00) = 32.544,90; CSLL 0,09 × 385.449,00 = 34.690,41.

**Sensibilidade marginal (por que o valor dos brindes importa):** cada R$ 1.000,00 de adição não lançada
eleva o lucro antes da compensação em 1.000,00, o teto em 300,00 e o lucro real em **700,00** → tributo
extra de **R$ 238,00** no regime com adicional (R$ 168,00 se o lucro real ficasse abaixo de R$ 60.000).
Sem trava e sem saldo a compensar seria R$ 340,00 (R$ 240,00); sem trava **com** saldo suficiente, o tributo
não muda no trimestre — só se consome mais saldo (o tributo sai dos trimestres futuros). Traduzindo: a
ausência do valor de brindes e da doação — teto demonstrável de R$ 181.000,00 em janeiro — é diferença real
de tributo (cenário A → C: +R$ 43.078,00), não um detalhe de documentação.

## 9. O que a biblioteca **não** permite afirmar (lista fechada, repisada aqui para o revisor)

- ICMS e IPI (inclusive o "7% líquido de créditos" de R$ 177.800,00 e eventual crédito na NF-e 8812) —
  não há norma de ICMS/IPI na biblioteca; não revisado (**U-09**).
- Dedutibilidade dos juros da conta 2.1.04 (principal declarado 2.400.000,00; juros do mês 28.000,00;
  credor não identificado) — capitalização, subcapitalização e juros entre partes relacionadas não estão
  na biblioteca (**U-12**).
- Depreciação fiscal × contábil (**U-10**); tributos sobre a remessa de brindes/doação de bens (**U-11**);
  acréscimos legais sobre o R$ 11.100,00 estornado (**U-07**); tributação diferida sobre o saldo de
  prejuízo a compensar (**U-13**); status de transmissão/pagamento da EFD/DAS de 01/2026 (**U-06**).
- Existência e exatidão dos R$ 900.000,00 de abertura, por falta de ECF anterior (**U-08**).
- **Prazo/decadência do prejuízo fiscal** e da ordem de uso dos saldos: não há uma linha na biblioteca sobre
  isso (**U-17**). Por isso os saldos de abertura são tratados como compensáveis sem limite de prazo, e os
  R$ 784.365,30 do cenário A pressupõem lucro nos trimestres seguintes — sem lucro futuro, o crédito não vira
  tributo pago, simplesmente deixa de ser usado.

Registro integral e formas de encerrar cada item: `deliverable/UNKNOWN.md` (U-01 … U-17).

## 10. Roteiro para fechar o e-LALUR quando chegarem os dados

1. Rodar T1–T7 de `deliverable/mes_02/ajustes.json` sobre fevereiro e março (tie-out, 9,25% sobre a
   receita, caça a crédito de uso e consumo, baixa do crédito válido, varredura do art. 13, depreciação,
   ausência de provisão mensal).
2. Somar os resultados contábeis dos três meses → `lucro_liquido_contabil`.
3. Quantificar brindes e doação — pelo detalhamento de 4.2.02/4.2.03, por valor declarado, ou por
   instrução escrita de não apurar por insuficiência de registro (custo de cada caminho em
   `deliverable/QUESTIONS.md` § 4) → `adicoes`; confirmar a competência (1T2026 × 4T2025 — se 2025, a
   adição sai deste LALUR e vai para e-LALUR/ECF de 2025).
4. Rodar a fórmula das seções 5 e 6; preencher `compensacao_prejuizo` = MIN(30% × lucro antes; 900.000,00).
5. Preencher a Parte B com os saldos remanescentes e manter a ressalva da abertura até ver a ECF anterior.
6. Registrar em `mes_03/ajustes.json` (AJ-03) a provisão do IRPJ/CSLL do trimestre no passivo de março —
   prática usual de regime de competência, **sinalizada como não verificável** porque a biblioteca não traz
   norma contábil; e **não** lançar brindes/doação na escrita societária (só no e-LALUR).
