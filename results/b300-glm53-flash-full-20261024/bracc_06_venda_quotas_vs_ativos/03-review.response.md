I'll do a full verification pass: sources → library → deliverables → arithmetic, then fix and report.

Sources check out. Now the library files cited, to verify every legal claim in the memo:

Library claims confirmed. Now re-reading the full memo and STATUS post-edits, and sweeping for citation・typo problems:

Full read done. During the reconciliation pass I spotted one **real arithmetic error** in §3.4 (the 12-month spread scenario): it says "12 pagamentos mensais de R$ 588.000 **por sócio**" — but 588.000/month is the **combined** amount (7.056.000 ÷ 12 = 588.000 total; R$ 294.000/sócio). 588.000 × 2 × 12 would be 14,1 mi — impossible. The IRRF figure 585.600 is correct; the wording is wrong. Let me verify everything by script and sweep for leftovers before fixing:

All numbers reconcile exactly (JSON match: True), and the breakeven chain confirmed: with cents-rounded intermediates the verification lands on **líquido 7.829.999,99** (not the displayed 7.830.000,00 — a R$ 0,01 rounding artifact worth fixing). Let me re-read the exact §3.4/§4/§7 text to anchor the fixes:

Text confirmed. Applying the four fixes now (§3.4 wording + IRRF-runtime caveat, §4 line ending, §7 breakeven rounding disclosure, STATUS reorder + PERGUNTAS note):

One more typo I introduced ("pagamento Mensal" with a capital M) — fixing, then running the final sweep:

Revisão completa concluída — fontes → biblioteca → entregáveis → aritmética, tudo re-verificado por script. Aqui está o que a revisão **encontrou e corrigiu**:

## O que mudou

1. **§3.4 — erro real de aritmética/texto (o achado principal).** O cenário de 12 pagamentos mensais dizia "12 pagamentos mensais de R$ 588.000 **por sócio**" — mas 588.000/mês é o valor **combinado** (7.056.000 ÷ 12); por sócio seria R$ 294.000/mês (588.000 × 2 × 12 = 14,1 mi seria impossível). Corrigido para: "R$ 588.000 **no total (R$ 294.000 por sócio)**". Os valores de IRRF (585.600) e economia (110.000) já estavam certos — o erro era só na descrição.
2. **§3.4 — cláusula de honestidade adicionada:** na leitura alternativa do IRRF (10% sobre o integral), a economia de R$ 110.000 **desaparece** — todo pagamento mensal (294.000/sócio) superaria os R$ 50 mil, e o imposto seria 705.600 em qualquer calendário.
3. **§4 — frase embaralhada corrigida:** "o PJ perde R$ 1.979.600 mesmo com o preço mais caro" não fazia sentido (a comparação é com preço **igualado** em 9,6 mi). Agora: "a rota PJ fica R$ 1.979.600 atrás."
4. **§7 — verificação do ponto de empate agora transparente:** mostra o P exato (12.074.074,074074...) e a cadeia não arredondada (tributo 3.385.185,185; d 8.688.888,889; IRRF 858.888,889; líquido 7.830.000,000 ✔), e **disclose** de que arredondando etapa a etapa a centavos dá 7.829.999,99 — diferença de R$ 0,01 apenas de arredondamento (antes aparecia "7.830.000,00 ✔" sem nota).
5. **STATUS item 2 reordenado:** a *Nota* sobre o alcance da Lei 14.973/2024 foi movida para o fim, para que a frase do custo mínimo de fallback siga direto da frase da documentação.
6. **STATUS — nota explícita de que `PERGUNTAS.md` não foi criado de propósito** (era opcional no contrato; nada bloqueou a elaboração e as ambiguidades já estão como itens em aberto).
7. *Já na sessão:* corrigido typo "somenight" → "somente" no parágrafo da "lei de atualização" §4.2.

## O que passou sem alteração (verificado limpo)

- **Fatos:** todos os números do §1 batem com os 3 documentos de origem (preços, cronograma 40/20/20/20, capital, citação do Hélio, frase do "ágio").
- **Autoridade:** todo parágrafo legal traça para os 6 arquivos do `INDEX.md`; *nenhuma* citação fora da biblioteca; pontos silenciosos (base integral/parcela excedente do IRRF, IRPFM, capitalização↔custo GCAP, escopo da Lei 14.973) seguem rotulados como **não verificados**.
- **JSON:** bate exatamente com o recalculado por script (`JSON matches computed values: True`), schema do contrato completo.

## Placa de reconciliação final

| Cálculo | Valor | ✓ |
|---|---|---|
| PF: ganho 3.900.000/s → GCAP 585.000/s × 2 = **1.170.000** | líquido **7.830.000** (13,0%) | ✔ |
| DARFs 468.000 + 234.000×3 = 1.170.000 | cronograma JSON | ✔ |
| PF a 9,6 mi: 8.340.000 | brecha vs PJ: **1.979.600** | ✔ |
| Custo 300 k/s: GCAP 1.260.000 | líquido 7.740.000 (+90.000) | ✔ |
| PJ: ganho 7.500.000 → IRPJ 1.125.000+744.000 = **1.869.000**; CSLL **675.000** | tributo **2.544.000** | ✔ |
| Distribuição 7.056.000 → IRRF **695.600** (excedente) / 705.600 (integral) | líquido **6.360.400** / 6.350.400 (33,7%) | ✔ |
| Spread 12 meses: IRRF 585.600 | economia 110.000 (→0 na leitura integral) | ✔ |
| Empate: P ≈ **12.074.074,07** | líquido 7.830.000,000 exato | ✔ |
| Retificação ilícita (Beatriz): 15% × 1,4 mi × 2 | **420.000** | ✔ |

Deliverables prontos para entrega em `workspace/deliverable/`.