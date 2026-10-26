# Passivo fiscal com a União — via de solução (Sessão 3)

**Objeto:** R$ 2.700.000,00 de débitos federais (relação de credores, `workspace/documents/relacao_credores.csv`,
linha "União"). A minuta de plano promete "deságio de 50%, 180 parcelas" **incluindo a União no plano**
(`workspace/documents/plano_minuta.md`, cláusula 4). **Essa cláusula não produz efeito** e é preciso substituí-la por
uma via legal antes da assembleia — o caminho está abaixo, com prazos e valores.

Todas as citações são de `workspace/library/INDEX.md`. O que não está na biblioteca está marcado
**NÃO VERIFICADO** e não é citado como direito.

---

## 1. Por que a cláusula da minuta não resolve (recapitulando a Sessão 2)

Três fundamentos independentes:

1. **Crédito tributário não entra em concurso de credores.** CTN art. 187: a cobrança judicial do crédito tributário
   "não é sujeita a concurso de credores ou habilitação em falência, recuperação judicial, concordata, inventário ou
   arrolamento" (`library/ctn_187_191a.md`). Na relação de credores da Atlas a própria União já aparece como
   "NÃO SUJEITO" — a minuta contraria a própria lista.
2. **O art. 68 da LRF reserva a negociação tributária à lei específica** (`library/lei11101_excertos.md`), e a lei
   específica da recuperação é a **Lei 10.522/2002, arts. 10-A a 10-C** (`library/lei10522_parcelamento_rj.md`).
   Ou seja: a via existe, mas **não é o plano**.
3. **Execução fiscal continua correndo.** Art. 6º, §7º-B: as execuções fiscais **não se suspendem** pelo deferimento
   da recuperação — "ressalvada a competência do juízo da RJ sobre atos constritivos sobre bens de capital
   essenciais" (`library/lei11101_excertos.md`). Os 2.700.000 estão cobráveis agora, e a única proteção para a
   **linha de separação de pedidos** (bem de capital essencial, ver `deliverable/sessao2/analise_plano.md` §6.4) é
   a competência do juízo da recuperação sobre o ato constritivo.

Consequência prática que trava tudo: **art. 57 da LRF e CTN 191-A** exigem certidões negativas de débitos tributários
para a concessão da recuperação — **ou positivas com efeito de negativa (CND-E), obtidas justamente por
parcelamento/transação** nos arts. 10-A a 10-C da Lei 10.522 (`library/lei11101_excertos.md` e
`library/ctn_187_191a.md`). **Sem adesão a uma dessas vias, não há CND-E e não há homologação**, por melhor que o
plano seja aprovado em assembleia.

---

## 2. As três vias legais, com prazos e valores

Base de cálculo: **2.700.000,00**. Os valores abaixo são **nominais, antes dos juros/encargos de cada modalidade** — a
biblioteca não informa a taxa de juros nem a forma de consolidação dos parcelamentos federais
(**NÃO VERIFICADO** → perguntar à PGFN/Receita no ato da simulação; ver §6).

### Via A — Parcelamento ordinário da RJ: Lei 10.522, art. 10-A (até 120 parcelas)

```
2.700.000,00 ÷ 120 parcelas = 22.500,00 por mês
```

| Item | Valor |
|---|---|
| Total parcelado | 2.700.000,00 (sem desconto de principal) |
| Prazo máximo | **120 meses** |
| Parcela mensal | **22.500,00** |
| Alternativa em 84 parcelas | 2.700.000,00 ÷ 84 = **32.142,86/mês** |
| Redução de dívida | **zero** |
| CND-E | sim, gera certidão positiva com efeito de negativa (art. 57/CTN 191-A) |

É a via mais simples e menos contestável. **Não gera ganho contábil nem tributário** (não há redução de dívida — ver
`deliverable/sessao3/lancamentos_novacao.json`, lançamento L4).

### Via B — Parcelamento com pagamento parcial em prejuízo fiscal: Lei 10.522, art. 10-A, §1º-B

A biblioteca permite "liquidar **até 30% com prejuízo fiscal/base negativa** e o restante em **84 parcelas**":

```
30% de 2.700.000,00 = 810.000,00  → liquidados com prejuízo fiscal / base negativa de CSLL
saldo a parcelar     = 2.700.000,00 − 810.000,00 = 1.890.000,00
1.890.000,00 ÷ 84 parcelas        = 22.500,00 por mês
```

Sensibilidade à disponibilidade de prejuízo fiscal (**a Atlas ainda não informou se tem** — pergunta nº 8):

| Prejuízo fiscal/base negativa disponível | Liquidado sem caixa | Parcelado em 84x | **Parcela mensal** |
|---|---|---|---|
| 0 (hipótese atual) | 0 | 2.700.000,00 | **32.142,86** |
| 400.000,00 | 400.000,00 | 2.300.000,00 | **27.380,95** |
| 810.000,00 (teto de 30%) | 810.000,00 | 1.890.000,00 | **22.500,00** |

Com prejuízo fiscal suficiente, a Via B **custa o mesmo 22.500,00/mês da Via A, mas abate 810.000,00 do passivo** — é
melhor que a Via A e melhor que a cláusula ilegal da minuta (que prometia 50% = 1.350.000,00, valor que a Via B não
alcança sozinha). Sem prejuízo fiscal, a Via B é **pior que a Via A** (32.142,86 contra 22.500,00 por mês), porque
encurta o prazo para 84 meses. **Não aderir à Via B antes de confirmar o prejuízo fiscal.**

### Via C — Transação com a PGFN: Lei 10.522, art. 10-C (desconto até 70%, até 120 meses)

A biblioteca registra transação "com a PGFN (desconto até 70%, 120 meses)" — e o prazo da transação **alcance os 120
meses**, exatamente o que a minuta prometia ilegalmente em 180:

```
desconto máximo 70% de 2.700.000,00 = 1.890.000,00 (redução de dívida)
saldo transacionado = 810.000,00  ÷ 120 parcelas = 6.750,00 por mês
```

| Cenário de desconto | Dívida final | **Parcela em 120x** | Economia nominal vs 2.700.000 |
|---|---|---|---|
| 70% (teto da biblioteca) | 810.000,00 | **6.750,00** | **1.890.000,00** |
| 50% (o que a minuta prometia) | 1.350.000,00 | **11.250,00** | 1.350.000,00 |
| 30% | 1.890.000,00 | 15.750,00 | 810.000,00 |

**O ponto que o diretor financeiro precisa entender:** a transação legal entrega **mais desconto (até 70%) do que a
cláusula ilegal do plano (50%)**, em prazo **mais curto (120 em vez de 180 parcelas)** e **sem risco de o plano ser
rejeitado**. A cláusula 4 da minuta é, além de ilegal, desnecessária.

A transação é **negociada** (Lei 13.988/2020 e Portaria PGFN 2.382/2021, citadas em
`library/lei10522_parcelamento_rj.md`): o percentual efetivo de desconto não é garantido, e os critérios de
aptação/limites **não constam da biblioteca** → **NÃO VERIFICADO**. Não prometer 70% ao conselho; apresentar 50%
como cenário de trabalho e 70% como teto.

---

## 3. Recomendação (sequência e prazo)

**Recomendação: Via A como piso imediato + tentativa simultânea de Via C (transação), com Via B apenas se houver
prejuízo fiscal confirmado.**

| Passo | Ação | Por quê / quando |
|---|---|---|
| 1 | **Simular o parcelamento do art. 10-A hoje** e aderir na faixa de 120 parcelas (22.500,00/mês) | Aderir **antes** de pautar a assembleia: é o que gera a CND-E exigida pelo art. 57/CTN 191-A. Sem isso, a homologação é negada mesmo com plano aprovado. |
| 2 | **Pedir transação individual à PGFN** (art. 10-C) sobre o mesmo saldo | Reduz o esforço mensal de 22.500,00 para 6.750,00–11.250,00 e abate 810.000,00–1.890.000,00 do passivo. Aderir à transação **não depende** de o plano ser aprovado. |
| 3 | Confirmar **prejuízo fiscal / base negativa** (pergunta nº 8) | Só com saldo confirmado a Via B faz sentido (tabela do §2). |
| 4 | **Reescrever a cláusula 4 da minuta**: retirar a União do plano e declarar adesão a parcelamento/transação com os números da via escolhida | A cláusula atual é ineficaz (CTN 187; art. 68) e dá argumento a impugnações. |
| 5 | Pedir ao juízo da RJ que **qualquer ato constritivo sobre a linha de separação** em execução fiscal seja submetido à competência do juízo da recuperação | Art. 6º, §7º-B, in fine; art. 49, §3º, in fine (a proteção contra venda/retirada de bens de capital essenciais vale até o fim da suspensão — 08/09/2026, prorrogável até 07/03/2027, sob a premissa P2). |

---

## 4. Efeito no caixa e no plano (números, sem forçar reconciliação)

Esforço federal mensal comparado, dentro do esforço total do plano (trabalhistas 53.333,33 nos meses 1–18;
quirografário 21.566,67 nos meses 25–120; geração de caixa informada de 5.000,00/mês):

| Modalidade federal | Parcela/mês | Meses 1–18 (trab.+fed.) | Meses 25–120 (quiro+fed.) | Déficit acumulado em 120 meses* |
|---|---|---|---|---|
| Cláusula ilegal da minuta (50% em 180x) | *não produz efeito — valor inexistente* | — | — | — |
| **Via A** — 10-A, 120x | **22.500,00** | 75.833,33 | 44.066,67 | **5.130.400** |
| Via B — 10-A §1º-B, sem prejuízo | 32.142,86 (84x) | 85.476,19 | 21.566,67 (após o mês 84) | 5.130.400 |
| Via B — com prejuízo 810.000 | 22.500,00 (84x) | 75.833,33 | 21.566,67 (após o mês 84) | 4.320.400 |
| **Via C** — transação 70% | **6.750,00** (120x) | **60.083,33** | **28.316,67** | **3.240.400** |
| Via C — transação 50% | 11.250,00 (120x) | 64.583,33 | 32.816,67 | 3.780.400 |

\* déficit = soma das parcelas (trabalhistas + plano quirografário + federal) menos a geração de 5.000,00/mês,
**sem** a amortização do CCB do Banco Beta e **sem** a venda do galpão. Aritmética em
`workspace/documents/calculos_sessao2.txt`.

A economia nominal aparece exatamente no déficit: Via A 5.130.400 → Via C 3.240.400 = diferença de **1.890.000,00**.
Arredondando para o caixa: **a transação compra fôlego, mas não salva o plano sozinha** — com qualquer uma dessas
vias o déficit de 10 anos continua acima dos 4.500.000,00 esperados do galpão, e o caixa de 840.000,00 se esgota
entre o mês 3 e o mês 12 uma vez servido o CCB do Beta (`deliverable/sessao2/analise_plano.md` §6.3). **Não
apresentar a solução fiscal como resposta à insuficiência do plano.**

---

## 5. Consequências tributárias da via escolhida (ligação com Sessão 2)

1. **Trava de 30%: não se aplica.** Como a biblioteca define a trava, citamos exatamente assim: o ganho com a redução
   da dívida na RJ **não se sujeita ao limite percentual dos arts. 42 e 58 da Lei 8.981/95 e 15 e 16 da Lei 9.065/95**
   (art. 50-A, II — `library/lei11101_excertos.md`). Não atribuímos a trava a outro dispositivo: a numeração que a
   doutrina/legislação ordinária lhe dá **não consta da biblioteca** → NÃO VERIFICADO.
   Ver `deliverable/sessao2/efeito_tributario_desagio.json`.
2. **PIS/COFINS sobre o ganho do deságio: não incidentes** (art. 50-A, I — "excluídas da base de cálculo").
3. **Despesas com a recuperação judicial: dedutíveis** no IRPJ/CSLL (art. 50-A, III). Incluir honorários de
   recuperação, administrador judicial e custos do plano na escrituração — os valores não foram informados
   (pergunta aberta).
4. **Atenção ao art. 50-A, parágrafo único:** o tratamento favorecido **não** alcança obrigações com **pessoas
   ligadas** à devedora. Se houver fornecedores/intermediários controlados pelos sócios na classe III (há
   "pessoas físicas" com 460.000,00, 210.000,00 e 170.000,00 na relação de credores), separar essa parcela para o
   tratamento fiscal comum → pergunta nº 14.
5. **O desconto obtido em transação (Via C) não é alcançado pelo art. 50-A** — o artigo trata da renegociação de
   dívidas **no âmbito da recuperação judicial**, e o crédito tributário está fora do plano (CTN 187). Entendimento
   nosso, **NÃO VERIFICADO na biblioteca**: tributar o ganho da transação como receita do período. Não embutir essa
   economia como "ganho livre de imposto" no fluxo.

---

## 6. O que não está na biblioteca (NÃO VERIFICADO) e perguntas abertas

**NÃO VERIFICADO** (não citado como direito, precisa de confirmação fora da biblioteca):
- taxa de juros, forma de consolidação e percentual de entrada dos parcelamentos federais (a biblioteca só dá prazo
  e percentual de prejuízo fiscal);
- regras de **caducidade** do parcelamento e o que acontece com a CND-E em caso de inadimplência;
- critérios, modalidades e limites da transação da PGFN (Lei 13.988/2020 e Portaria PGFN 2.382/2021 são citadas no
  índice da biblioteca, mas o conteúdo não está nos excertos);
- se é possível **combinar** transação (art. 10-C) com a liquidação por prejuízo fiscal (art. 10-A, §1º-B);
- possibilidade de garantir/parcelar débitos **não federais** (estaduais/municipais) — a Atlas tem apenas débito
  federal informado;
- quais dispositivos **criam** a trava de 30% fora do que o art. 50-A, II nomeia (arts. 42 e 58 da Lei 8.981/95 e 15 e
  16 da Lei 9.065/95): qualquer outra numeração da trava é NÃO VERIFICADA;
- responsabilidade de sócios, administradores e avalistas por débitos tributários e pelo CCB (encaminhar ao jurídico);
- requisitos de homologação e regime de recuperação simplificada.

**Perguntas em aberto** (`deliverable/QUESTIONS.md`): nº 8 (prejuízo fiscal/base negativa), nº 14 (pessoas ligadas),
nº 15 (se o galpão da UPI é o imóvel onde a linha de separação está instalada), nº 16 (prestação do CCB do Beta),
nº 17 (ônus sobre o galpão), nº 18 (data do despacho de homologação / status da assembleia), nº 19 (composição do
saldo de fornecedores extraconcursais de 1.480.000,00 do extrato de março), nº 20 (se há débitos tributários
estaduais/municipais ou garantias sobre eles), nº 21 (valor contábil do galpão) e nº 22 (despesas da recuperação:
honorários do AJ e dos administradores, advogados da empresa).

---

## 7. Frase de apoio para o conselho

> A União não está no plano e não pode estar (CTN art. 187; LRF art. 68). A lei da recuperação abre outra porta —
> parcelamento em até 120 parcelas, abatimento de até 30% com prejuízo fiscal, ou transação com a PGFN com desconto
> de até 70% em 120 meses. É por essa porta que saem os 2.700.000,00 e, sobretudo, é por ela que sai a **certidão
> positiva com efeito de negativa sem a qual a recuperação não é concedida** (LRF art. 57; CTN art. 191-A).
