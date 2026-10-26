As entregas da S2 já existem; vou fazer uma sincronização de consistência com a rodada mais recente (a proposta de pagamento por fora de 925.000 agora é um risco concreto de viabilidade) e depois entregar o resumo avaliado.

Sessão 2 está fechada — os três entregáveis existem, foram validados e acabam de ser sincronizados com a última rodada (a proposta de pagar 925.000 por fora entrou como risco nº 10 em `analise_plano.md` §9). Segue a avaliação consolidada:

## 1. A minuta, cláusula a cláusula (`sessao2/analise_plano.md`)

| Cláusula | Veredicto | Ponto central |
|---|---|---|
| **1. Trabalhistas — integral em até 18 meses** | **Condicional → ilegal como redigida** | art. 54: prazo máximo de **1 ano** para créditos trabalhistas vencidos até o pedido; 2 anos só nas condições do §2º (que a minuta não observa). Custo de corrigir: 80.000/mês (12m) vs 53.333,33/mês (18m) |
| **2. Quirografários + ME/EPP — deságio 60%, 120×, carência 24m** | **Legal em princípio** (classe IV: base legal NÃO VERIFICADA na biblioteca) | base 6.470.000 → 2.588.000; parcela 21.566,67/mês |
| **3. Fiduciários (Beta) sujeitos ao plano, deságio 40%** | **Ilegal / ineficaz** | art. 49, §3º: o proprietário fiduciário **não se submete** à RJ. O "ganho" de 1.240.000 é fantasma; os 3.100.000 seguem fora, **vencidos desde 03/2025**, com máquinas (linha de separação = essenciais) protegidas só até 08/09/2026 |
| **4. União no plano, deságio 50%, 180×** | **Ilegal — três fundamentos independentes** | CTN 187 + art. 68 (tributo não se sujeita ao plano); deságio de tributo fora do poder da assembleia; 180 > 120 parcelas do art. 10-A da Lei 10.522. Ganho fantasma de 1.350.000; saída legal é parcelamento/transação (S3) |
| **5. Fonte de recursos: operação + galpão (UPI) 4,5 mi** | **Insuficiente em números; regime da UPI NÃO VERIFICADO** | déficit de **5.130.400** em 120 meses sem o Beta / **8.230.400** servindo o CCB, contra 4.500.000 do galpão; caixa de 840.000 acaba **entre o mês 3 e o mês 12** |

**Armadura central:** do deságio contado na minuta (6.472.000), **só 3.882.000 (60%) existe juridicamente** — fiduciário e União não cabem no plano. E o plano não se paga: o esforço federal mínimo (22.500,00/mês) somado aos 53.333,33 trabalhistas (meses 1–18) e 21.566,67 da renegociação dá ~75.833,33/mês contra geração de +5.000/mês.

## 2. Efeito tributário do deságio (`sessao2/efeito_tributario_desagio.json` + sensibilidade)

| Chave | Valor | Base |
|---|---|---|
| ganho_desagio | **3.882.000** | 60% × 6.470.000 — **não** os 6.472.000 da minuta (2.590.000 são ganhos inexistentes) |
| pis_cofins_sobre_ganho | **0** | art. 50-A, I — receita da renegociação fora da base PIS/COFINS |
| trava_30_aplicavel | **false** | art. 50-A, II — o diretor está errado: a trava de 30% **não** se aplica ao ganho da renegociação. (Se aplicasse, o prejuízo fiscal valeria *menos*, não mais: 923.916 vs 1.319.880.) |
| prejuizo_fiscal / compensacao | **0 = ausência de dado** | pergunta nº 8; se houver prejuízo, abate a base **por inteiro** (sem trava) |
| base_irpj_csll | **3.882,000 nominal = piso** | pelo CPC 48 o ganho contábil é **maior**: PV a 1,0% a.m. → 5.286.124; a 1,5% → **5.632.704** (sensibilidade no arquivo irmão) |
| irpj_csll | **1.319.880 (provisão)** | 3.882.000 × 34%; o parâmetro 34% é **NÃO VERIFICADO** (aliquotes fora da biblioteca) — cenários a 25% (970.500) e 9% (349.380) no arquivo de sensibilidade |

Ressalvas registradas: benefícios do art. 50-A **não alcançam pessoas ligadas** (parágrafo único — pergunta nº 14); ganho eventual do galpão também escapa da trava (art. 6º-B), mas o valor contábil é desconhecido (nº 21).

## 3. O que muda com os fatos novos
- **Beta vencido + garantias + aval**: risco de execução após 08/09/2026 e de o aval atingir os controladores (responsabilidade de avalista NÃO VERIFICADA — remetida à assessoria).
- **Galpão × linha de separação** (nº 15) e ônus (nº 17): travam a validação da fonte de recursos.
- **Risco nº 10 (novo, §9)**: o pagamento de 925.000 à Norte "por fora" consome **110,1% do caixa** — além de ilegal (resposta §8 da S1), quebraria o runway no mês 0.

Status do engajamento segue **COMPLETE WITH OPEN ITEMS** (`deliverable/STATUS.md`), com as lacunas rotuladas P1–P11 e a lista NÃO VERIFICADO preservadas.