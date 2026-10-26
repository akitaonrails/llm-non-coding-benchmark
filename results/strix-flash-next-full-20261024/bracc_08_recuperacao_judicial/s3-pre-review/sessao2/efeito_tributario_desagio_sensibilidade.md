# Sensibilidade do efeito tributário do deságio — apoio ao item 5

**Atlas Distribuidora S.A.** — Sessão 2 · arquivo de apoio a `deliverable/sessao2/efeito_tributario_desagio.json`
**Por que este arquivo existe:** o valor enviado no JSON (`ganho_desagio = 3.882.000`) é o **deságio nominal**, que é o
**piso** do ganho. O ganho contábil efetivo depende da taxa de desconto; o imposto depende da alíquota (NÃO VERIFICADA)
e do prejuízo fiscal (dado ausente). Aqui os três eixos são abertos, com a aritmética mostrada.

---

## 1. O que é ganho, e quando ele nasce

`library/cpc_contabil_rj.md`: a homologação do plano opera **novação**; quando os termos são substancialmente
diferentes (**teste dos 10%**), baixa-se o passivo original e reconhece-se o novo **a valor justo (valor presente das
parcelas)**; a diferença é **ganho** no resultado, em rubrica própria ("receita de renegociação de dívidas em RJ").

```
passivo contábil baixado (classes III/IV) .. 6.470.000
novo passivo (PV) ............. 120 parcelas de 21.566,67, a 1ª com 24 meses de carência
ganho = 6.470.000 − PV  →  quanto MAIOR a taxa, MENOR o PV e MAIOR o ganho
```

Teste dos 10% (satisfeito com folga): a diferença entre o passivo original (6.470.000) e o novo (2.588.000 nominal) é
de **60%** → muito acima de 10%, ou seja, há novação/extinção e reconhecimento de ganho, e não mero ajuste de custo
amortizado.

**Momento do reconhecimento:** o ganho nasce na **homologação/aprovação do plano** (ato que opera a novação), não no
mês do pedido nem na venda do galpão. Isso define o período de apuração do IRPJ/CSLL e a data a partir da qual os
créditos concursais deixam de ser apresentados na rubrica própria da RJ.

---

## 2. Eixo 1 — taxa de desconto (o ganho contábil é sempre ≥ 3.882.000)

PV de 120 parcelas de 21.566,67 com primeira parcela em t=25:
`PV = PMT × [1 − (1+i)^−120] / i × (1+i)^−24`

| Taxa | Taxa anual equivalente | PV do novo passivo | **Ganho contábil** | IRPJ/CSLL a 34% |
|---|---|---|---|---|
| 0,00% a.m. (nominal) | — | 2.588.000 | **3.882.000** | 1.319.880 |
| 0,50% a.m. | 6,17% | 1.723.433 | 4.746.567 | 1.613.833 |
| 1,00% a.m. | 12,68% | 1.183.876 | 5.286.124 | 1.797.282 |
| 1,50% a.m. | 19,56% | 837.296 | 5.632.704 | 1.915.119 |
| 2,00% a.m. | 26,82% | 608.146 | 5.861.854 | 1.993.030 |

Leitura: **não existe cenário em que o ganho contábil seja menor que 3.882.000.** Uma correção que fizemos no caminho:
a primeira versão da Sessão 1 (§4 de `deliverable/sessao1/resposta_diretor.md`) dizia que o ganho contábil seria
*menor* que o nominal — está errado, e o §4 está retificado no arquivo. Para a **provisão de imposto** usamos o nominal
(prudente: não antecipa juro como fato gerador); para o **resultado** o ganho é o da tabela.

A taxa de desconto não foi informada (pergunta nº 9). Em recuperação judicial, uma taxa de mercado para uma empresa
assim tende a ser alta, o que aumenta o ganho contábil — é o efeito perverso: **quanto pior o crédito, maior o ganho
tributável**.

---

## 3. Eixo 2 — alíquota (NÃO VERIFICADO: nada sobre IRPJ/CSLL está na biblioteca)

Aplicado sobre o ganho **nominal** de 3.882.000 (piso):

| Parâmetro usado (rotação de sensibilidade) | Imposto |
|---|---|
| 34% (IRPJ 25% + adicional 10% + CSLL 9%) | **1.319.880** |
| 25% | 970.500 |
| 9% | 349.380 |

Sobre o ganho contábil de 1,5% a.m. (5.632.704), o mesmo parâmetro de 34% dá **1.915.119**. Ou seja, a banda de
exposição fiscal do deságio vai de **~R$ 0,35 mi a ~R$ 1,9 mi** — e o número do JSON (1.319.880) é o meio dessa banda,
com o critério prudencial declarado.

---

## 4. Eixo 3 — prejuízo fiscal (dado ausente) e a trava de 30% que o diretor quer

| Cenário de prejuízo fiscal/base negativa | Base tributável | IRPJ/CSLL (34%) |
|---|---|---|
| 0 (hipótese P6, usada no JSON) | 3.882.000 | 1.319.880 |
| 1.000.000 | 2.882.000 | 980.000 |
| 3.882.000 (cobre o ganho nominal) | 0 | 0 |
| ≥ 5.632.704 (cobre o ganho a 1,5% a.m.) | 0 | 0 |

Por que a trava de 30% **não** se aplica e **não** ajudaria: o art. 50-A, II da Lei 11.101/2005 diz que o ganho
auferido com a redução da dívida **não se sujeita à limitação de 30%** (`library/lei11101_excertos.md`). Se a trava
valesse, o uso de prejuízo seria limitado a 30% do ganho:

```
com trava (hipótese rejeitada):  3.882.000 × 30% = 1.164.600 de abate permitido
                                 tributaría 3.882.000 − 1.164.600 = 2.717.400 → imposto 923.916
sem trava (o que a lei determina): o prejuízo abate até o inteiro do ganho
```

Ou seja: a trava de 30% **reduz** a utilidade do prejuízo fiscal. Pedir sua aplicação é pedir para pagar mais imposto
quando o prejuízo é grande. O que o diretor provavelmente quer dizer é o contrário — proteger o ganho — e o instrumento
correto é a compensação integral, que a lei permite aqui.

### Conflito de uso do prejuízo fiscal (decisão a tomar com a Sessão 3)

O mesmo prejuízo fiscal pode ser usado de dois modos, com rendimentos diferentes:

| Uso | Rendimento |
|---|---|
| Abater o ganho do deságio (3.882.000) | economiza **34%** de cada real: 1.000.000 → 340.000 |
| Liquidar débito fiscal na forma do art. 10-A, §1º-B da Lei 10.522/2002 (até 30% do débito) | extingue **1 real de principal por 1 real** de prejuízo: 810.000 de prejuízo → 810.000 do débito da União quitados |

Se o saldo de prejuízo fiscal for ≥ 810.000, **o uso na dívida fiscal rende mais** (810.000 de principal extinto
contra 275.400 de imposto economizado). A escolha depende do dado da pergunta nº 8; a Via B da Sessão 3 assume esse
cenário e está sinalizada como recomendada **apenas se** o prejuízo existir.

---

## 5. O que NÃO entra aqui (e por quê)

| Item | Tratamento |
|---|---|
| Deságio de 40% sobre o Banco Beta (1.240.000) | **Excluído.** Proprietário fiduciário não se submete à RJ (art. 49, §3º) — o corte não produz efeito e, logo, não produz ganho. Reconhecer esse ganho seria inflar o resultado e o imposto. |
| Deságio de 50% sobre a União (1.350.000) | **Excluído.** Crédito tributário não se sujeita ao plano (CTN 187; art. 68) nem à assembleia. Redução de tributo só existe por transação legal (Lei 13.988/2020, Portaria PGFN 2.382/2021, `library/lei10522_parcelamento_rj.md`). |
| PIS/COFINS sobre o ganho | **Zero** por determinação legal (art. 50-A, I), não por estimativa de alíquota. |
| Ganho de capital do galpão/UPI | Não quantificado: valor contábil do imóvel desconhecido. Sem trava de 30% (art. 6º-B). |
| Despesas do plano | Dedutíveis (art. 50-A, III), mas **não lançadas**: não há dado de valores e o regime de amortização não está na biblioteca. |
| Pessoas ligadas | Se algum credor do plano for pessoa ligada, o art. 50-A inteiro é inaplicável àquela parcela (parágrafo único) — o ganho volta à base de PIS/COFINS e a trava volta a valer. Pergunta nº 11. |
| Multa, juros e encargos do passivo fiscal | Não há discriminação nos arquivos (`documents/relacao_credores.csv` traz 2.700.000 agregado): **NÃO VERIFICADO/NÃO DADO**. |

---

## 6. Recomendação de lançamento (detalhe no item 6, `deliverable/sessao3/lancamentos_novacao.json`)

1. Baixar o passivo concursal renegociado pelo **valor contábil** (6.470.000) e registrar o novo passivo ao **valor
   presente** com a taxa documentada — nunca com o valor nominal "seco", porque isso subestima o passivo e o juro
   futuro.
2. Reconhecer o ganho em **rubrica separada** ("receita de renegociação de dívidas em RJ"), com divulgação do teste
   dos 10% e da taxa usada.
3. Provisionar IRPJ/CSLL sobre o ganho (sem PIS/COFINS) e registrar **tributo diferido** para a diferença entre o
   ganho contábil e a base fiscal nominal, se divergirem.
4. **Não** reconhecer ganho de deságio sobre fiduciário, União, e **não** reconhecer nada relacionado ao "sinal" do
   Norte (não há operação lícita possível hoje).

*Todas as autoridades: `library/INDEX.md`. Parâmetros de alíquota e taxas de desconto estão rotulados NÃO VERIFICADO.*
