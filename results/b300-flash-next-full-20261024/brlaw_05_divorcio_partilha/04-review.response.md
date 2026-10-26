

Vou fazer uma revisão completa: conferir cada citação contra os arquivos da biblioteca real, verificar toda a aritmética e validar consistência cruzada entre os entregáveis.






Applying the remaining fixes to `proposta_acordo.md` (§6 rewrite, §9 items 4 and 7, §1 FGTS 8% flag):








Now fixing `partilha.json`, `STATUS.md` and `QUESTIONS.md` — first getting exact current strings:





All edits applied. Now running the full validation suite — JSON parse, all sums, torna split, and grep for stale strings:





The script filter missed the uppercase "DIVIDAS" row — the JSON itself is consistent. Re-running with the correct filter:





Reconferência completa — tudo valida. A seguir, o que a revisão encontrou e corrigiu.

## Revisão pré-entrega — alterações aplicadas

### Erros substantivos (dinheiro) corrigidos

1. **Torna/FGTS em duplicidade — `proposta_acordo.md` §3/§5, `partilha.json`, `STATUS.md`.** O quadro §3 já incluía o FGTS (140.000) nos bens de Marcelo e fixava torna de 155.000, mas o §5 apresentava os 70.000 da meação dela no FGTS como **pagamento à parte** — na redação anterior ele pagaria 155.000 + 70.000 e ela receberia 1.275.000 (70.000 a mais que a meação). Corrigido: torna de **155.000 = 85.000 à vista/parcelado + 70.000 exigíveis no saque do FGTS** (mesmo total, diferimento de fluxo, não acréscimo), com conferência explícita 1.050.000 + 85.000 + 70.000 = 1.205.000 ✓.

2. **Desconstrução da sobre-exigência mal rotulada — §4.** Os componentes "60.000 (dedução integral do financiamento)" e "90.000 (FGTS embutido)" estavam errados: confrontados com `documents/`, 60.000 é o **carro que ela retém omitido da proposta** (líquido) e 90.000 é o **PGBL que ela retém omitido**. Total inalterado (450 + 400 + 750 + 60 + 90 = 1.750.000; excesso 545.000), mas agora os rótulos batem com o texto da proposta dela.

3. **"Realiza a meação dela de 180.000" — `partilha.json` (DIVIDAS)** era impreciso: ela assume 360.000 (2× a meação dela de 180.000). Reescrito: os bens onerados saem **líquidos** do quadro (apto 900.000, carro 60.000) e os 180.000 pagos por Marcelo estão embutidos no cálculo líquido da torna, sem reembolso autônomo.

### Autoridade não suportada — corrigida contra a biblioteca

4. **"STJ IN 84/2001" → IN RFB 84/2001 (art. 3º, §3º e art. 20)** — a IN é da Receita Federal, não do STJ; e o conteúdo também estava errado: a regra é da **atribuição na própria partilha acima do valor declarado = ganho de capital sobre a diferença** (não só "alienação posterior"). §6 reescrito com a base correta.
5. **"Alíquotas de ITCMD/ITBI não constam da biblioteca" era falso** — `tributos_partilha.md` traz **ITCMD 4% (SP)** para excesso de meação gratuito e **ITBI 3% (SP, imóveis)** para oneroso (Lei 10.705/2000). §6, §9.7, STATUS item 6 e QUESTIONS item 4 agora citam essas alíquotas; permanecem marcados **não verificados** apenas o que realmente não está na biblioteca: alíquotas de IR, isenções municipais de ITBI e o regime da apuração de haveres.
6. **Alíquota de 8% do FGTS não está na biblioteca** — onde usada (2.400 = 8% × 30.000), agora marcada explicitamente como **conferência aritmética, não citação** (proposta §1, `partilha.json`, STATUS).

### Verificações que passaram sem alteração
- Todas as citações (REsp 1.399.199, 1.595.775, EREsp 1.623.858, 1.698.774, 1.332.808, AgInt no AREsp, Súmula 358, CC 1.658–1.662/1.664, 1.584 §2º, 1.694/1.695/1.699) conferidas nos 6 arquivos da biblioteca — todas presentes.
- Aritmética refeita por script: JSONs validam; somas por bem = TOTAL (2.410.000 / 1.205.000 / 3.850.000); torna split = 155.000; alternativa 1.055.000; excesso 545.000; fechamento global 3.490.000; alimentos 15/20/30% = 6.550,00 / 8.733,33 / 13.100,00.
- `alimentos.json` e `guarda` (§8) — sem mudanças necessárias.

Nenhuma fonte fora de `library/` é citada; os 6 itens abertos permanecem em `QUESTIONS.md` e o `STATUS.md` está marcado **COMPLETE WITH OPEN ITEMS (v2.1 — com revisão pré-entrega)**. Pronto para entrega.