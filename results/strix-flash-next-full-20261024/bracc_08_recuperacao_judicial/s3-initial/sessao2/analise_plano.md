# Análise do plano de recuperação judicial — cláusula por cláusula

**Atlas Distribuidora S.A.** — Recuperação Judicial (TJSP, 2ª Vara de Falências e Recuperações Judiciais)
**Documento:** `deliverable/sessao2/analise_plano.md` (Sessão 2, item 4 do `CONTRACT.md`)
**Objeto:** minuta de `documents/plano_minuta.md` — para cada cláusula: **LEGAL / ILEGAL / CONDICIONAL /
NÃO AVALIÁVEL** e por quê.
**Autoridades:** exclusivamente `library/INDEX.md`. Ausências de texto legal estão marcadas **NÃO VERIFICADO**.

---

## 0. Premissas (o cliente informou não ter mais informações — itens 1 a 8 seguem como hipóteses rotuladas)

| # | Premissa | Por que é necessária | Efeito se estiver errada |
|---|---|---|---|
| P1 | Pedido ajuizado entre **03/02/2026** e **12/03/2026**; processamento deferido em **12/03/2026** (`documents/decisao_processamento.md`) | marco do art. 49 e do art. 54 | muda quais créditos são concursais e quais trabalhistas entram no teto de prazo |
| P2 | Suspensão do art. 6º, §4º: **12/03/2026 → 08/09/2026**, prorrogável até **07/03/2027** | proteção dos bens de capital essenciais (art. 49, §3º, in fine) | encurta/alonga a janela de proteção da linha de separação |
| P3 | **Nenhum** credor do plano é pessoa ligada | art. 50-A, parágrafo único (`library/lei11101_excertos.md`) | se Banco Alfa/Norte forem pessoas ligadas, o benefício fiscal não vale para essa parcela |
| P4 | Geração de caixa de **+5.000/mês**, extrapolada das 4 semanas preenchidas do fluxo | teste de cabimento do plano | semanas 5–13 ausentes: números podem ser bem diferentes |
| P5 | Parcelas do plano contadas da **homologação** (t=0), como diz a minuta | calendário de caixa | — |
| P6 | **Prejuízo fiscal e base negativa: não informados → admitidos em 0** | efeito tributário do deságio (Sessão 2, item 5) e Via B da Sessão 3 | se houver prejuízo fiscal ≥ 3.882.000, o IRPJ/CSLL sobre o ganho tende a zero |
| P7 | Alíquotas de IRPJ/CSLL usadas apenas como **parâmetro NÃO VERIFICADO** (não constam da biblioteca) | quantificar o imposto | o imposto muda na proporção da alíquota |
| P8 | Venda do galpão **não** realizada até a homologação (não há recebimento no fluxo) | fonte de recursos | — |

---

## 1. Quadro-resumo

| Cláusula da minuta | Veredicto | Motivo central | Valor em jogo |
|---|---|---|---|
| 1. Classe I (trabalhistas): integral em até 18 meses | **CONDICIONAL → ILEGAL como redigida**, salvo as condições do art. 54, §2º | art. 54: prazo máximo de **1 ano** para créditos trabalhistas vencidos até o pedido; até 2 anos só nas condições do §2º | 960.000; parcela 53.333,33/mês (18m) vs 80.000/mês (12m) |
| 2. Classes III (quiro) e IV (ME/EPP): deságio 60%, 120 parcelas, carência 24 meses | **LEGAL em princípio** (para os quirografários; classe IV NÃO VERIFICADA) | não há teto de deságio/prazo para essas classes nos excertos; o art. 50-A pressupõe renegociação com redução de dívida | base 6.470.000 → 2.588.000 (deságio 3.882.000); parcela 21.566,67/mês |
| 3. "Credores com garantia fiduciária sujeitos ao plano, deságio 40%" | **ILEGAL / INEFICAZ** | art. 49, §3º: proprietário fiduciário **não se submete** à RJ | ganho fantasma de 1.240.000; dívida real de 3.100.000 segue fora do plano |
| 4. "União incluída no plano, deságio 50%, 180 parcelas" | **ILEGAL** (três fundamentos independentes) | CTN 187 + art. 68 (crédito tributário não se sujeita ao plano); deságio de tributo fora do poder da assembleia; 180 > **120** parcelas máximas do art. 10-A da Lei 10.522 | ganho fantasma de 1.350.000; dívida real de 2.700.000 |
| 5. Fonte de recursos: operação + galpão (UPI) por 4.500.000 | **NÃO AVALIÁVEL em direito** e **INSUFICIENTE em números** | regime de alienação de UPI não consta da biblioteca; no mérito, o plano não se paga | déficit de 5.130.400 em 120 meses (sem o Beta) / **8.230.400** servindo o CCB, contra 4.500.000 do galpão; o caixa de 840.000 **acaba entre o mês 3 e o mês 12** (§6.3) |

**Armadura financeira da minuta (o ponto central):** a minuta supõe extinguir

```
60% × (4.200.000 + 1.850.000 + 420.000) = 3.882.000   (classes III/IV)  → possível
40% × 3.100.000                        = 1.240.000   (fiduciário)       → impossível
50% × 2.700.000                        = 1.350.000   (União)            → impossível
                                     ------------
total imaginado                        = 6.472.000
realmente disponível                   = 3.882.000   → 3.882.000 ÷ 6.472.000 = 60,0%
```

Do deságio contado na minuta, **só 60% existe juridicamente**. Os 2.590.000 restantes (fiduciário + União)
precisam ser tratados fora do plano — e continuam pesando no caixa (Sessão 3).

---

## 2. Cláusula 1 — Classe I (trabalhistas): "pagamento integral em até 18 meses a partir da homologação"

**Veredicto: a integralidade é correta; o prazo de 18 meses é ILEGAL como redigido, salvo se preenchidas as
condições do art. 54, §2º — que a minuta não prevê.**

- **Integral, sem deságio → correto.** O art. 49 submete os créditos existentes ao pedido; a minuta não reduz o
  principal trabalhista, o que é tecnicamente correto (`library/lei11101_excertos.md`).
- **Prazo.** Art. 54: *"O plano não poderá prever prazo superior a 1 ano para pagamento dos créditos
  trabalhistas vencidos até a data do pedido (§2º permite até 2 anos em condições específicas: garantias,
  aprovação da classe, integralidade)"* — `library/lei11101_excertos.md`.
  18 meses > 1 ano. A minuta **não oferece garantia**, **não registra aprovação da classe** e a carência
  implícita de "até 18 meses" não é integralidade imediata. Logo, na redação atual a cláusula **contraria o
  art. 54**.
- **NÃO VERIFICADO:** o excerto da biblioteca resume o §2º em três condições e **não diz se elas são
  cumulativas ou alternativas**. Não afirmamos que 18 meses será aceito; afirmamos que precisa satisfazer o
  §2º, e isso tem de ser demonstrado na petição do plano.
- **NÃO VERIFICADO:** a definição de classe trabalhista (arts. 41 e 83 da LRF) não está na biblioteca — já
  sinalizado na Sessão 1.

**Aritmética do ajuste:**

```
960.000 ÷ 18 meses = 53.333,33/mês      (minuta)
960.000 ÷ 12 meses = 80.000,00/mês      (conforme art. 54, caput)
diferença          = 26.666,67/mês a mais durante o período
```

**Recomendação:** (i) reenquadrar para **12 meses** (80.000/mês), ou (ii) manter 18 meses **construindo as
condições do §2º** — garantia real/fidejussória expressa, ata de aprovação da classe I e pagamento integral —
e requerer expressamente o §2º na submissão. O custo de caixa adicional da opção (i) é de 26.666,67/mês.

**Pendência que trava o cálculo:** não sabemos quais créditos trabalhistas venceram **antes** e **depois** do
pedido (pergunta nº 5). O teto do art. 54 alcança os **vencidos até a data do pedido**; obrigações trabalhistas
nascidas **durante** a RJ são **extraconcursais** (art. 67) e têm de ser pagas no vencimento, fora do plano —
não entram nos 960.000 "de plano" se forem posteriores ao pedido.

---

## 3. Cláusula 2 — Classes III (quirografários) e IV (ME/EPP): "deságio de 60%, 120 parcelas, carência de 24 meses"

**Veredicto: LEGAL em princípio.** É a única cláusula de corte de dívida da minuta que tem substrato jurídico.

- Os excertos não fixam teto de deságio nem de prazo para quirografários; ao contrário, o **art. 50-A** trata
  justamente de "**renegociação de dívidas no âmbito de processo de recuperação judicial**" com redução de
  dívida, o que pressupõe deságio e prazo alongado (`library/lei11101_excertos.md`).
- **NÃO VERIFICADO:** a existência e o conteúdo da **classe IV (ME/EPP)** não constam da biblioteca (já
  registrado na Sessão 1). O enquadramento do Fornecedor Sul (420.000) vem de `documents/relacao_credores.csv`.
- **NÃO VERIFICADO:** regras de votação/maiorias por classe (assembleia) não constam da biblioteca; não
  opinamos sobre quórum. Como a cláusula corta 60%, a aprovação das próprias classes é o ponto político do plano.

**Efeito numérico (base lícita do plano):**

```
quirografários: Banco Alfa 4.200.000 + Norte (pré-pedido) 1.850.000 = 6.050.000
ME/EPP:         Fornecedor Sul                                 420.000
base                                                                6.470.000
deságio 60%      6.470.000 × 60%                              =  3.882.000
novo passivo     6.470.000 − 3.882.000                        =  2.588.000
parcela mensal   2.588.000 ÷ 120                              =    21.566,67/mês
carência         sem pagamento nos meses 1–24
```

**Atenção fiscal (art. 50-A, `library/lei11101_excertos.md`):**
1. **I** — a receita do devedor **não entra na base do PIS/COFINS** → o deságio não gera PIS/COFINS;
2. **II** — o ganho com a redução da dívida **não** se sujeita à **trava de 30%** → a pretensão do diretor de
   "aplicar a trava de 30% ao ganho do deságio" é exatamente o que a lei afasta (detalhes em
   `deliverable/sessao2/efeito_tributario_desagio.json`);
3. **III** — as **despesas** com as obrigações do plano são **dedutíveis**;
4. **parágrafo único** — nada disso vale para dívidas com **pessoas ligadas** (premissa P3; confirmar).

**Efeito contábil (CPC 48 / IFRS 9, `library/cpc_contabil_rj.md`):** com 60% de corte, o teste dos 10% é
largamente superado → baixa-se o passivo original e reconhece-se o novo **a valor presente**, o que produz ganho
**maior** que o deságio nominal (carência de 24 meses). Ver §7 e o arquivo de sensibilidade.

---

## 4. Cláusula 3 — "Credores com garantia fiduciária sujeitos ao plano, com deságio de 40%"

**Veredicto: ILEGAL / INEFICAZ.** É a cláusula mais grave da minuta depois da da União, e agora tem consequência
operacional direta.

- Art. 49, §3º: o titular da posição de **proprietário fiduciário** de bens móveis **não se submete aos efeitos
  da recuperação judicial**, prevalecendo o direito de propriedade (`library/lei11101_excertos.md`). A assembleia
  não pode cortar 40% (R$ 1.240.000) de quem não é sujeito ao plano: a cláusula é **ineficaz** quanto ao Banco
  Beta.
- Contrapartida legal: **durante o prazo de suspensão do art. 6º, §4º, é vedada a venda ou a retirada do
  estabelecimento dos bens de capital essenciais** à atividade (art. 49, §3º, in fine). Na 2ª rodada a
  administração confirmou que **as máquinas alienadas fiduciariamente são a linha de separação de pedidos e que
  sem elas a operação não funciona** → são bens de capital essenciais. Janela de proteção: **até 08/09/2026**,
  prorrogável até **07/03/2027** (P2).
- Se houver ato constritivo sobre esses bens (inclusive em **execução fiscal**, que não se suspende —
  art. 6º, §7º-B), a competência para apreciar o ato é do **juízo da recuperação** (ressalva do mesmo
  dispositivo). Petição imediata se ocorrer.

**Consequências para o plano:**

```
ganho contado na minuta ............... 3.100.000 × 40% = 1.240.000  → sai da projeção
dívida que continua fora do plano ..... 3.100.000  CCB VENCIDO desde 03/2025 (3ª rodada)
garantias do CCB ..................... alienação fiduciária das máquinas ESSENCIAIS
                                      + garantias reais + aval dos controladores
prestação mensal ...................... NÃO INFORMADA (pergunta nº 16) → serviço de dívida não fechável
   ilustração (apenas ilustração): 3.100.000 ÷ 60m = 51.666,67/mês; ÷ 120m = 25.833,33/mês
```

O crédito estar **vencido desde março de 2025** muda o diagnóstico: a dívida já é vencida há **~1 ano antes do
pedido**, com garantias reais e aval dos controladores. O Beta tem, portanto, incentivo e meios para executar — e a
única barreira temporal é a proteção dos bens de capital essenciais (até **08/09/2026**, prorrogável até
**07/03/2027**). Terminada a suspensão, a regra é a **satisfação do credor fiduciário sobre a própria coisa**: sem
acordo, a operação da Atlas se inviabiliza nesse prazo, e o plano que depende dessa mesma operação cai junto.

**Três saídas legítimas, todas fora do corte de 40%:**
1. **Renegociar o CCB com o Beta, por acordo, preservando a linha de separação** — caminho recomendado. A linha é
   insubstituível (a administração confirma que sem ela não há operação), e o Beta tem interesse no devedor vivo:
   um CCB vencido com garantia sobre ativo essencial vale mais negociado do que executado. Modelos de esforço
   (§6.3) mostram que o plano **só fecha** com prestação mensal baixa. **NÃO VERIFICADO:** se um acordo bilateral
   com credor fiduciário, celebrado no curso da RJ, aproveita os benefícios do art. 50-A (que fala em renegociação
   "no âmbito de processo de recuperação judicial") — não prometemos o benefício fiscal nesse cenário;
2. **Quitar o saldo (3.100.000) e liberar a alienação fiduciária**, consolidando a linha como ativo próprio. É a
   hipótese financeiramente pior no curto prazo: o galpão previsto (4.500.000) equivale a **1,45×** esse saldo, e a
   venda do galpão é justamente o recurso contado para o plano — as duas decisões competem pelo mesmo dinheiro. Se a
   linha estiver **fora** do galpão (ver §6.4), a venda do galpão pode quitar o Beta e **sobram 1.400.000**
   (4.500.000 − 3.100.000), o que deixa o plano descoberto em **5.130.400 − 1.400.000 = 3.730.400** → ver §6.3;
3. **Consolidar a posição dos avalistas/controladores.** Com aval dos controladores sobre o CCB, a execução alcança
   o patrimônio deles; isso deve ser levado ao conselho antes de qualquer decisão de litigar com o Beta. A
   responsabilidade dos sócios/avalistas em RJ **não** está na biblioteca → NÃO VERIFICADO, encaminhar ao jurídico.

**Atenção à venda da UPI:** as máquinas são de **propriedade fiduciária do Beta** — não podem ser transferidas com o
imóvel, e não podem ser **retiradas** durante a suspensão. Ver §6.4.

---

## 5. Cláusula 4 — "União incluída no plano com deságio de 50% e 180 parcelas"

**Veredicto: ILEGAL, por três fundamentos independentes.** A cláusula não sobrevive e a União não fica vinculada
por ela, ainda que a assembleia aprove.

1. **O crédito tributário não se sujeita à RJ nem ao plano.** CTN art. 187: a cobrança judicial do crédito
   tributário **não é sujeita a concurso de credores ou habilitação** em recuperação judicial
   (`library/ctn_187_191a.md`); LRF art. 68: Fazendas Públicas e INSS *poderão* deferir parcelamento especial e
   **o crédito tributário não se sujeita ao plano** (`library/lei11101_excertos.md`).
2. **Deságio de tributo não é decisão da assembleia.** Reduzir tributo é matéria de **transação com a PGFN**,
   nos limites da lei (Lei 13.988/2020 e Portaria PGFN 2.382/2021, citadas em
   `library/lei10522_parcelamento_rj.md`), e não de voto de credores. O desconto de 50% "por plano" é
   inexistente perante a Fazenda.
3. **180 parcelas não existem no regime da RJ.** Para empresário em recuperação, o parcelamento federal é de até
   **120 parcelas** (Lei 10.522, art. 10-A) — ou 84 parcelas com liquidação parcial por prejuízo fiscal
   (§1º-B) — e a transação pode ir a **120 meses** (`library/lei10522_parcelamento_rj.md`). 180 > 120: a
   cláusula extrapola o único regime aplicável.

**Consequências:**

```
ganho contado na minuta ...... 2.700.000 × 50% = 1.350.000  → sai da projeção
dívida que continua devida ... 2.700.000                     → parcelamento/transação (Sessão 3)
execuções fiscais ............ NÃO se suspendem (art. 6º, §7º-B) → bens em risco desde já
certidão para a concessão .... art. 57 da LRF e CTN 191-A exigem quitação/CND-E
                               (library/lei11101_excertos.md; library/ctn_187_191a.md)
```

O ponto é decisivo na homologação: **aprovado o plano, a concessão da recuperação depende da prova de quitação
dos tributos** (CTN 191-A; art. 57). Sem adesão a parcelamento/transação, não há certidão positiva com efeito de
negativa e a recuperação não é concedida — a cláusula 4 não resolve isso, ela agrava.

**NÃO VERIFICADO:** os artigos da LRF/CTN sobre remissão e transação de créditos tributários, e as condições de
rescisão do parcelamento (multa, vencimento antecipado) não constam da biblioteca.

---

## 6. Cláusula 5 — Fonte de recursos: "operação + venda de um galpão (UPI) por R$ 4,5 mi"

**Veredicto em direito: NÃO AVALIÁVEL.** A disciplina da alienação de **UPI/unidade produtiva isolada** **não
consta da biblioteca** — **não citamos art. 66-A** e não damos parecer sobre forma, quórum ou efeitos da venda
(Sessão 1, §4, já registrava). O que a biblioteca permite afirmar: **art. 6º-B** — não se aplica a trava de 30%
ao **ganho de capital na alienação judicial de bens em RJ** (`library/lei11101_excertos.md`), o que favorece o
resultado fiscal da venda, se houver ganho.

**Veredicto em números: o plano não se paga com a geração de caixa informada.** Este é o achado mais importante
da Sessão 2 e está **não reconciliado de propósito** (regra do `CONTRACT.md`).

Encargos mensais de um plano juridicamente correto (premissas P4/P5; parcelamento federal de 120 parcelas da
Sessão 3; **excluído** o CCB do Beta, por desconhecida a prestação):

| Período da homologação | Encargo mensal | Geração de caixa | Déficit mensal | Meses | Déficit acumulado |
|---|---|---|---|---|---|
| 1 a 18 | 53.333,33 (trabalhistas) + 22.500,00 (federal) = **75.833,33** | 5.000,00 | −70.833,33 | 18 | **−1.275.000** |
| 19 a 24 (carência quiro/ME-EPP) | 22.500,00 (federal) | 5.000,00 | −17.500,00 | 6 | **−105.000** |
| 25 a 120 | 21.566,67 (quiro/ME-EPP) + 22.500,00 (federal) = **44.066,67** | 5.000,00 | −39.066,67 | 96 | **−3.750.400** |
| **Total 120 meses** | | | | | **−5.130.400** |

```
aritmética:
geração de caixa/mês = (5.770.000 − 5.750.000) ÷ 4 semanas = 20.000 ÷ 4 = 5.000,00
trabalhistas 960.000 ÷ 18 = 53.333,33      federal 2.700.000 ÷ 120 = 22.500,00
quiro/ME-EPP 2.588.000 ÷ 120 = 21.566,67

déficit = (75.833,33 − 5.000)×18 + (22.500 − 5.000)×6 + (44.066,67 − 5.000)×96
        = 1.275.000 + 105.000 + 3.750.400 = 5.130.400
galpão previsto = 4.500.000  →  GAP = 5.130.400 − 4.500.000 = 630.400  (sem o CCB do Beta)
```

Mesmo antes de qualquer parcela quirografária, os **24 primeiros meses** exigem caixa não operacional:

```
trabalhistas 960.000 + federal 22.500×24 (540.000) = 1.500.000
geração no período 5.000×24 = 120.000  →  necessidade de 1.380.000 em 2 anos
```

E o gap de 630.400 **não inclui** a amortização do CCB do Beta (3.100.000, vencido desde 03/2025) nem as obrigações
extraconcursais em aberto (310.000 do Norte + fornecimentos à vista). Ou seja: a "operação" como fonte de recursos é,
hoje, **neutra** (+5.000/mês), e o plano inteiro depende de um único ativo.

### 6.3 O plano não sobrevive ao CCB do Beta: em quanto tempo o caixa acaba

Como a prestação do CCB não foi informada (pergunta nº 16), invertemos o cálculo e testamos cenários. Encargo mensal
de cada mês = trabalhistas (meses 1–18) + parcelas do plano quirografário (meses 25–120) + federal (22.500,00) +
prestação do CCB, contra geração de 5.000,00/mês. Ponto de partida: **caixa de 840.000 em 31/03/2026**
(`deliverable/sessao1/demonstrativo_mensal_aj.md` §1). A venda do galpão **não** é considerada — é exatamente isso que
está sendo testado.

| Cenário do CCB (3.100.000 vencido desde 03/2025) | Prestação | Encargo mensal de pico | Déficit 12 meses | Déficit 24 meses | Déficit 120 meses | **Caixa de 840.000 acaba no mês** |
|---|---|---|---|---|---|---|
| Beta ignorado (o que a minuta faz) | — | 75.833,33 | 850.000 | 1.380.000 | 5.130.400 | **12** |
| CCB em 120 meses | 25.833,33 | 101.666,67 | 1.160.000 | 2.000.000 | 8.230.400 | **9** |
| CCB em 60 meses com 12 de carência | 51.666,67 | 127.500,00 | 850.000 | 2.000.000 | 8.230.400 | **12** |
| CCB em 60 meses | 51.666,67 | 127.500,00 | 1.470.000 | 2.620.000 | 8.230.400 | **7** |
| CCB em 36 meses | 86.111,11 | 161.944,44 | 1.883.333 | 3.446.667 | 8.230.400 | **6** |
| CCB em 24 meses | 129.166,67 | 205.000,00 | 2.400.000 | 4.480.000 | 8.230.400 | **5** |
| CCB em 12 meses | 258.333,33 | 334.166,67 | 3.950.000 | 4.480.000 | 8.230.400 | **3** |

Três conclusões que o diretor precisa ver:

1. **Esticar o CCB não reduz o buraco de 10 anos — só atrasa a parede.** O déficit acumulado em 120 meses é
   **8.230.400** em todos os cenários com o Beta (5.130.400 se ele for ignorado), porque a dívida é a mesma e a
   operação **não gera folga em mês nenhum**: o que muda é o mês em que o caixa zera (entre o mês 3 e o mês 12).
2. **O melhor cenário possível — ignorar o Beta e pagar a minuta como está — quebra no mês 12**, muito antes de
   existirem as 120 parcelas prometidas. Servindo o CCB em prazos típicos de mercado, quebra entre o **mês 3 e o
   mês 7**.
3. **Logo, a venda do galpão não é um detalhe da fonte de recursos: é a condição de sobrevivência da empresa entre 9
   e 12 meses.** Isso colide com §6.4 (a linha essencial pode estar dentro do galpão) e com §6.5 (ônus sobre o
   imóvel). Se a venda não sair nesse prazo, o desfecho provável é convolação em falência, não recuperação.

As três alavancas possíveis, todas a negociar **antes** da assembleia:

1. **Carência longa no CCB** (ex.: balão de 3.100.000 com 12 meses de carência → PV a 1,5% a.m. = 2.592.801,
   ~259.000 de alívio de passivo presente) mantendo a garantia e a linha em operação — é a linha "mês 12" da tabela;
2. **Venda do galpão em até ~9 meses** (ou de outro ativo), o que exige responder às perguntas nº 15 e nº 17
   imediatamente;
3. **Aporte dos controladores** (pessoa ligada → atentar ao art. 50-A, parágrafo único; a responsabilidade de sócios
   e avalistas em RJ **não** está na biblioteca → NÃO VERIFICADO, encaminhar ao jurídico).

**Recomendação:** não submeter o plano à assembleia sem (a) a prestação real do CCB e (b) uma carta de intenções do
Beta. Submeter sem isso é submeter um plano sabidamente insustentável — e a minuta hoje não demonstra viabilidade
econômica, o que é causa clássica de rejeição (os requisitos de homologação não constam da biblioteca: NÃO VERIFICADO).

### 6.4 Risco novo, com potencial de derrubar a fonte de recursos inteira
A linha de separação de pedidos — **máquinas de propriedade fiduciária do Banco Beta, sem as quais a empresa não
opera** — é bem de capital essencial (art. 49, §3º, in fine). Na 3ª rodada a administração confirmou que a operação
funciona no **imóvel locado**, mas **não disse se o galpão ofertado como UPI é esse imóvel ou outro** (pergunta
nº 15). Os dois ramos:

- **Ramo A — a linha está DENTRO do galpão ofertado:** a venda entrega um imóvel **sem** as máquinas (propriedade de
  terceiro) e **com** proibição legal de retirá-las durante a suspensão (art. 49, §3º, in fine) → o comprador não
  recebe operação e o preço de 4.500.000 provavelmente não se sustenta; se a linha for retirada para viabilizar a
  venda, **a operação da Atlas para**, e a "operação" some como fonte de recursos do plano;
- **Ramo B — o galpão é um imóvel SEPARADO (mais provável, dada a locação):** a UPI vendável é um imóvel vazio e
  **não contém** a linha. A alienação não desmonta a operação — mas levanta duas outras questões: (i) o galpão está
  livre de ônus e é do ativo da Atlas? (pergunta nº 3, e o §6.5 abaixo) e (ii) uma UPI composta só de um imóvel
  atende à finalidade de **preservação da atividade** que justifica o regime? **NÃO VERIFICADO:** o regime da UPI
  não consta da biblioteca, e não afirmamos que a venda seja juridicamente possível nessa configuração.

Em qualquer ramo, **a fonte de recursos da minuta não pode ser validada até a resposta à pergunta nº 15.**

### 6.5 Ónus sobre o galpão (aberto na 3ª rodada, resposta pendente)
Se houver hipoteca, penhora ou alienação fiduciária sobre o galpão, o produto da venda **não** fica livre para o
plano: o credor com garantia real é pago com precedência e a UPI sai onerada. Isso pode significar que a única fonte
de recursos do plano rende **zero** no primeiro ano. É a pergunta nº 17; enquanto não respondida, o teste de esforço
deve ler a venda do galpão como **incerta**, não como garantida.


---

## 7. Consequência contábil e fiscal do deságio (resumo; detalhe nos arquivos do item 5)

```
valor contábil baixado (classes III/IV) ......... 6.470.000
passivo novo a valor presente (carência 24m) .... PV de 120 parcelas de 21.566,67
ganho contábil = 6.470.000 − PV  ≥  3.882.000    (quanto maior a taxa, maior o ganho)
   taxa 0,5% a.m. → PV 1.723.433  ganho 4.746.567
   taxa 1,0% a.m. → PV 1.183.876  ganho 5.286.124
```

- **PIS/COFINS sobre o ganho: zero** (art. 50-A, I).
- **Trava de 30%: não se aplica** (art. 50-A, II) — a pretensão do diretor é legalmente improcedente; sem a
  trava, prejuízo fiscal abate o ganho por inteiro.
- **Despesas com as obrigações do plano: dedutíveis** (art. 50-A, III).
- **Alienação judicial do galpão:** também sem trava de 30% sobre o ganho de capital (art. 6º-B).
- Alíquotas de IRPJ/CSLL: **NÃO VERIFICADO** (não constam da biblioteca) — usadas como parâmetro rotulado.

Números completos em `deliverable/sessao2/efeito_tributario_desagio.json` e
`deliverable/sessao2/efeito_tributario_desagio_sensibilidade.md`.

---

## 8. Minuta revisada — o que precisa mudar

1. **Classe I:** 12 meses (80.000/mês) **ou** 18 meses com as condições do art. 54, §2º demonstradas na
   submissão (garantia + aprovação da classe + integralidade).
2. **Classes III/IV:** manter deságio 60% / 120 parcelas / carência 24 meses (legal em princípio) e **registrar
   o fundamento do art. 50-A** para assegurar o tratamento fiscal (I, II e III).
3. **Excluir a cláusula fiduciária.** Tratar o Banco Beta **fora do plano**: renegociar o CCB por acordo, com
   carência longa, preservando a garantia e a linha em operação (cenários no §6.3); pedir ao juízo da RJ a proteção
   da linha de separação contra atos constritivos (art. 49, §3º, in fine; art. 6º, §7º-B). Quitar 3.100.000 é a
   alternativa, mas compete pelo mesmo dinheiro da venda do galpão.
4. **Excluir a cláusula da União.** Substituir por adesão a parcelamento/transação (Lei 10.522, arts. 10-A a
   10-C) antes da assembleia, para obter a CND-E exigida pelo art. 57/CTN 191-A — ver
   `deliverable/sessao3/passivo_fiscal_solucao.md`.
5. **Reescrever a fonte de recursos** com números que fechem: o buraco é de **8.230.400** em 10 anos servindo o CCB
   (**5.130.400** se o Beta for ignorado) contra 4.500.000 de galpão, e o caixa de 840.000 acaba **entre o mês 3 e o
   mês 12** (§6.3). A resposta sobre a localização da linha de separação (nº 15) e sobre os ônus do imóvel (nº 17)
   define se essa fonte existe. Alternativas a modelar: venda de outro ativo, aporte dos controladores (atentar:
   pessoa ligada → art. 50-A, parágrafo único), ou deságio/prazo diferentes na classe III.
6. **Nada de pagamento a credor concursal fora do plano** (Sessão 1, §2.2): inclusive o "sinal" pretendido pelo
   Norte — art. 172 (favorecimento), art. 64 (afastamento) e convolação em falência
   (`library/lei11101_excertos.md`).

---

## 9. Riscos de impugnação e de aprovação

| Risco | Base | Severidade |
|---|---|---|
| Cláusula fiduciária declarada ineficaz; Beta continua com 3.100.000 **vencido desde 03/2025** e pode buscar as garantias após 08/09/2026 | art. 49, §3º | Alta — muda a dívida e o caixa |
| Execução das garantias reais e do **aval dos controladores** pelo Beta; a linha essencial volta a ficar exposta no fim da suspensão | art. 49, §3º (proteção só até 08/09/2026, prorrogável até 07/03/2027); responsabilidade de avalistas **NÃO VERIFICADA** na biblioteca | Alta — atinge o patrimônio dos sócios e pode parar a operação |
| União não vinculada; execução fiscal segue e a concessão é negada por falta de certidão | CTN 187; art. 68; art. 6º, §7º-B; art. 57; CTN 191-A | Alta — trava a homologação |
| Caixa exausto antes da venda do galpão: 840.000 duram do **mês 3** (CCB em 12m) ao **mês 12** (melhor caso) | fluxo de caixa e passivo consolidado deste documento | **Crítica** — conduziria à convolação em falência |
| Classe I impugna o prazo de 18 meses | art. 54 | Média-alta — custo extra de 26.666,67/mês |
| Impugnação de credores quirografários ao deságio de 60% | sem teto na biblioteca; aprovação é da classe | Média |
| Plano não demonstra viabilidade (déficit de 5.130.400 sem o Beta; 8.230.400 com o CCB) | análise financeira deste documento | Alta |
| Venda do galpão sem a linha de separação, ou imóvel onerado (hipoteca/penhora não informadas) | art. 49, §3º, in fine; perguntas nº 15 e nº 17 | Alta — pode zerar a fonte de recursos |
| Drenagem do caixa por pagamento fora do plano: a proposta da diretoria de pagar 925.000,00 à Norte ("adiantamento de fornecimento futuro") consome **110,1% do caixa de 840.000** e quebra o runway no mês 0; além de ilegal, é financeiramente inexequível | art. 49; art. 52, IV; art. 64; art. 172 (`sessao1/resposta_diretor.md`, §8) | **Crítica** — antecipa a convolação em falência |

**NÃO VERIFICADO:** quóruns e critérios de aprovação da assembleia e os requisitos de homologação (o INDEX lista
o art. 58, mas o excerto não reproduz seu texto) — não afirmamos nada sobre maiorias nem sobre o conteúdo do
art. 58.

---

## 10. Pendências que permanecem abertas (o cliente não tem mais informações)

Ver `deliverable/QUESTIONS.md`. As que pesam nesta análise: nº 1 (data exata do pedido), nº 3 (galpão:
essencialidade e origem dos R$ 4,5 mi), nº 5 (trabalhistas antes/depois do pedido), nº 11 (semanas 5–13 do
fluxo), **nº 15 (a linha de separação está no galpão?)**, **nº 16 (prestação mensal do CCB do Beta)**,
nº 8 (prejuízo fiscal e base negativa), nº 9 (taxa de desconto do valor presente), nº 14 (pessoas ligadas).

*Elaborado pela controladoria da Atlas Distribuidora S.A. Nenhuma fonte fora de `library/` foi utilizada.*
