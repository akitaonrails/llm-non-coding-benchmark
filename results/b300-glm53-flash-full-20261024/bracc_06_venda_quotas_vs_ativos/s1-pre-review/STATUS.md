# STATUS — Comparativo Vértice (PF × PJ)

**Status: COMPLETE WITH OPEN ITEMS**

Entregáveis prontos em `deliverable/`:

- `comparativo.json` — schema exigido pelo contrato, preenchido (recomendação `pf`).
- `memorando.md` — memória de cálculo completa, respostas a Hélio (§4.1) e Beatriz (§4.2), análise do "ágio" (§5), riscos (§6) e negociação (§7).

Toda a aritmética foi verificada por script (Python/shell); nenhuma divergência foi forçada a bater. Cada ponto em que a biblioteca é silenciosa está rotulado como não verificado, tanto no memorando quanto abaixo.

## Itens em aberto (não bloqueiam a resposta)

1. **Base do IRRF 2026 (Lei 15.270).** A biblioteca diz "pagos acima de R$ 50.000/mês: IRRF 10%" e não fixa se o 10% incide sobre o excedente ou sobre o valor integral. Leitura adotada (sobre o excedente, por fonte): IRRF R$ 695.600, líquido PJ R$ 6.360.400. Leitura alternativa (integral): R$ 705.600, líquido R$ 6.350.400. Diferença de R$ 10.000 (≤ 0,104% do preço); a recomendação não muda em nenhuma hipótese.
2. **Sustentação do custo de aquisição na DIRPF (R$ 600.000/sócio).** O valor coincide com o histórico social (100 k + 300 k de capitalização de 2018 + 200 k de aporte de 2021), mas a documentação da capitalização de 2018 precisa ser confirmada com o contador. *Nota:* a biblioteca não detalha o alcance (tipos de bem) da Lei 14.973/2024, única hipótese de atualização de custo que cita; a janela dela está encerrada, logo a dúvida é irrelevante para 2026. Se ela não for sustentável, custo mínimo R$ 300.000/sócio → GCAP total R$ 1.260.000, líquido PF R$ 7.740.000 (imposto +90.000; recomendação inalterada).
3. **PIS/COFINS/ISS/ITBI.** Não constam da biblioteca; não calculados e não afirmados como devidos ou não. Se incidirem na venda do estabelecimento (Proposta B), só aumentam o custo da PJ e reforçam a recomendação pela PF.
4. **Correção monetária das 3 parcelas anuais da Proposta A.** Nenhuma cláusula informada; cálculo sobre valores nominais. Se o contrato final trouxer atualização/juros, recalcula-se pela regra do parcelamento (item 6.2 do memorando).
5. **IRPFM (compensação anual).** O IRRF de 10% é antecipação, mas as regras anuais do imposto mínimo (limites, compensação, restituição) não estão na biblioteca — sem modelagem de crédito posterior.
6. **Outras alienações no ano.** Premissa de nenhuma outra alienação de bens da mesma natureza no ano; se existirem, as faixas do GCAP acumulam por contribuinte e os percentuais podem subir.
