# STATUS — COMPLETE WITH OPEN ITEMS

Atualizado em 24/10/2026 (rev. 3 — **rodada final**: além das respostas da rev. 2 (folha/encargos e mix),
o cliente informou **não ter informações adicionais** sobre todas as perguntas em aberto; elas ficam
**encerradas como desconhecidos explicitamente sinalizados, com limites calculados**, e **não serão
repetidas** — conforme a instrução do cliente).

Entregáveis presentes em `workspace/deliverable/`:

- `comparativo.json` — ok (todos os campos do esquema preenchidos; somas conferem com o memorando)
- `memorando.md` — ok (memória de cálculo com aritmética, fontes da biblioteca, premissas, sensibilidades, riscos, passo a passo)
- `PERGUNTAS.md` / `QUESTIONS.md` — ok (mesmo teor; perguntas já respondidas **não** são repetidas, ficam registradas com o efeito que tiveram; rodada 3: todas as não respondidas encerradas como desconhecidos sinalizados, também não reenviadas)
- `STATUS.md` — este arquivo

Conclusão entregue: **recomendacao = simples** (Simples R$ 916.500 < Presumido R$ 1.009.620 < Real R$ 1.010.790);
**mudanca_em_dezembro = impossivel**; **prazo_opcao = 2027-01-29** (último dia útil de janeiro de 2027, para efeitos em 1º/01/2027).

O que a resposta do cliente alterou: a base do INSS patronal passou a ser a **folha de R$ 1.050.000**
(CPP = 294.000, antes 364.000). A vantagem do Simples caiu de 163.120 para **93.120**; o mix de obras foi
confirmado em 15% e o vetor de sensibilidade do mix foi encerrado. A recomendação **não mudou**.

## Itens abertos

1. **Q6 — composição da linha de R$ 250.000 de encargos / dedutibilidade da CPP na base do Lucro Real
   (hoje é o único item capaz de inverter o ranking).** No Anexo III a CPP está dentro do DAS
   (`inss_patronal.md`) e 28% × folha (294.000) **excede** os 250.000 lançados, então a linha não pode
   conter a CPP integral. Cenário-limite (CPP inteira incremental e dedutível): Real = **910.830**, ou seja,
   **R$ 5.670 abaixo** do Simples. Escudo máximo = 34% × 294.000 = 99.960 > folga de 93.120.
   **Encerrada na rodada 3 — o cliente não tem o dado:** a inversão fica registrada como **cenário-limite,
   não adotado**; recomendação mantém **simples**, com a menor tolerância (5.670) explicitamente sinalizada.
2. **Q7 — parcela da folha alocada às obras (Anexo IV).** No Anexo IV a CPP sai do DAS. Ponto de empate com
   o Presumido: **31,7% da folha alocada às obras** (332.600). Alocação proporcional de 15% → Simples sobe a
   960.600 e ainda ganha por 49.020. A **alíquota do Anexo IV não está na biblioteca** → cálculo parcial, por limite.
   **Encerrada na rodada 3 (cliente não tem o dado):** caso-base mantém Anexo III integral.
3. **R2 — Fator R reavaliado pela resposta do cliente.** Folha pura = 1.050.000 = **25,00%** da receita
   (o balancete usava 1.300.000 → 30,95%). Se a fronteira de 28% se aplicar à folha pura, a consultoria
   migraria para o **Anexo V**. Tolerância calculada: o DAS poderia ir até **831.120** (efetiva 19,79%) antes
   de o Presumido vencer. Regra dos 28% e alíquotas do Anexo V **não estão na biblioteca** → classificação
   do balancete (Anexo III) mantida, com o risco sinalizado. **Reforçado na rodada 3:** sem novos dados do
   cliente, segue como exposição permanente; defesa prática: manter folha ≥ 28% da receita em 2027.
4. **Q3 — créditos de PIS/COFINS não detalhados** (energia, aluguéis, depreciação de equipamentos): não
   creditados por falta de valores; reduziriam o Real. Para empatar com o Simples seriam necessários
   **R$ 1.019.351** de créditos adicionais de insumo.
5. **Q4 — Lucro Real estimado em R$ 756.000** (lucro contábil, sem ajustes). A divergência entre a margem
   implícita (4,2 − 1,05 − 0,25 − 1,4 = **1,5 mi**) e o lucro informado (756 mil) **não reconcilia**
   (**≈744 mil** de despesas não detalhadas) e foi deixada aberta — número não ajustado. O Real só empataria
   com o Simples se o lucro fosse **≤ 478.676**.
6. **Q5 — plano de 2027** (receita e folha). Sem isso, usamos 4,2 mi e folha de 1.050.000. Cruzamento de
   receita (folha fixa): o Presumido passa a ser mais barato a partir de **≈ R$ 4.674.134** — **abaixo** do
   teto de 4,8 mi; a vantagem do Simples termina antes do enquadramento acabar (memorando R3, corrigido).
7. **Q2 (parte restante) — natureza das obras**: empreitada com material fornecido pela Vértice ou material
   do dono da obra (define Anexo IV × Anexo III e ICMS). Mix (15%) já confirmado.
8. **R7 — inconsistência de margem das obras**: insumos de obra de **700.000** contra receita de obras de
   **630.000**. Não ajustado; afeta presunção de 8%, crédito de PIS/COFINS e a alocação de folha do item 2.
9. **ISS sobre as obras** (R$ 630 mil) não aplicado por falta de regra na biblioteca; se incidir,
   **+R$ 31.500 nos três regimes** (não muda o ranking).
10. **Plano "outra empresa no Real faturando dezembro" (R8/Q8 — memorando §8.2).** Recomendado **não
    executar**: migrando só a receita, o imposto **sobe** 33.875; o ganho de ≈46.142 só existe migrando
    contratos/folha/insumos junto — e a validade jurídica desse desenho (desvirtuamento/pluralidade
    simulada, cessão de contratos, empresa recém-constituída, estouro do teto) **não está na biblioteca**
    → risco não dimensionável com as regras disponíveis. Caminho legal para o Real: exclusão até
    29/01/2027. **Rodada 3: o sócio não forneceu os fatos pedidos (Q8) — encerrada como desconhecido; a
    recomendação não executar permanece**, e o item reabre apenas se o plano avançar com fatos concretos
    (sazonalidade de dezembro; se 2026 estoura 4,8 mi; o que efetivamente migraria).
11. **Itens marcados como não verificados porque não estão na biblioteca** (não usados como fundamento):
    alíquotas do Anexo IV e do Anexo V; regra dos 28% do Fator R e o numerador do Fator R; critério de
    alocação de folha entre anexos; **dedutibilidade do INSS patronal na base do Lucro Real**; FGTS e
    alíquotas; redução de base de ISS da construção civil em SP; recuperação de ICMS-ST no PIS/COFINS;
    ICMS sobre contratos EPC; ajustes do Lucro Real; exclusão de ofício/retroativa por excesso de receita;
    **desvirtuamento/pluralidade simulada de entidades, cessão de contratos e de pessoal, regime de
    empresa recém-constituída**; vencimento da DARF que manifesta a opção pelo Presumido; feriados que
    alteram o "último dia útil".

Nenhum cálculo foi forçado para fechar; tudo que não fecha está listado acima.
