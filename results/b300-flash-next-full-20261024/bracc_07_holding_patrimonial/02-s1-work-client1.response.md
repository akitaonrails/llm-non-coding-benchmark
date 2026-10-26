

Resposta da cliente recebida — vou cruzá-la com os fatos do CSV e recalcular o que muda. Primeiro, reler os documentos-base e os arquivos afetados.







Todos os documentos revistos. Agora o recálculo com a comissão de 8% e os novos fatos — reescrevo o script de cálculo (o antigo se perdeu com o `/tmp` limpo) para manter tudo reproduzível.





Tabela por imóvel com erro de escala — corrijo a fórmula (a economia anual por imóvel é proporcional à fatia do aluguel):





Números confirmados. Agora vou reler o parecer integral para fazer as edições precisas.





Agora as edições. Primeiro, ver o `numeros.json` e `QUESTIONS.md` completos (as leituras anteriores foram truncadas):





`parecer.md` atualizado. Agora os 3 valores do `numeros.json` e, em paralelo, a revalidação virá depois:







`QUESTIONS.md` reescrito. Agora `PERGUNTAS.md` e `STATUS.md` com os números da rodada 2:






Anti-artifact grep is clean (the remaining "280.170" is an intentional historical mention in item 8 of QUESTIONS, and "vagos" only appears as a flagged client utterance). The last two typos remain:






Tudo consistente e validado. Entregáveis finais em `workspace/deliverable/` (`parecer.md`, `numeros.json`, `QUESTIONS.md`, `PERGUNTAS.md`, `STATUS.md`).

## Resumo para Dona Helena — rodada 2 (respostas de 24/10/2026 incorporadas)

### As cinco afirmações da palestra, verificadas com números

1. **"Integraliza imóveis na holding sem ITBI" — FALSA.** A locação é preponderante (100% da receita), e a exceção do CTN art. 37 §§1º–2º incide para empresa nova nos 3 primeiros anos. Planeje **pagar R$ 432.900** (3% × 14.430.000), não litigar (Tema 1.348 pendente). O Tema 796 dá teto de **126.600** se a base for o capital — os 306.300 de diferença ficam em discussão, não no planejamento.
2. **"Pagaria só 11,33%" — verdadeiro como modelo, FALSA aqui.** Com a **comissão de 8%** que ela confirmou (R$ 81.504/ano): federal no Presumido **124.031,64 inalterado** (a presunção de 32% incide sobre a receita, sem deduzir despesa), mas o distribuível cai para **813.264,36 (67.772,03/mês)**; concentrando na usufrutuária, IRRF de **21.326,44** → carga real **145.358,08 = 14,27%**. Banda honesta: **12,17%–14,27%**.
3. **"ITCMD de 4% sobre o valor contábil" — alíquota certa, base errada.** Base é o valor patrimonial atualizado (mercado): **384.800 agora + 192.400 no fim do usufruto = 577.200**.
4. **"Tira Marcos da sucessão" — FALSA.** Herdeiro necessário não se exclui por testamento. O desejo dela ("mínimo possível") **é realizável**: 0 quotas para Marcos, quinhão (3.088.333,33) pago com **ativos fora da PJ**. Os ~6 anos de afastamento **não estão na library** como justa causa de deserdação — só advogada pode qualificar.
5. **Cláusulas de proteção — DEPENDE** (justa causa, CC 1.848, em testamento); "protege dos credores" **não tem fonte na library** — não afirme isso.

### O que as respostas dela mudaram (recalculado)

- **PF hoje:** comissão é dedutível na PF → teto caiu de 280.170 para **257.756,40/ano**.
- **Payback do ITBI:** ~**3,2 anos** (cenutto) / ~**3,9 anos** (cenário real com IRRF); por imóvel 2,7–4,8 anos.
- **Fluxo pessoal:** plano entrega ~65.995/mês líquidos vs até ~56.628 hoje — melhora, mas ela paga aluguel em Higienópolis e o valor não foi informado.
- Confirmado: Casa CDJ e Terreno Cotia **ficam na PF**; netos existem; a estrutura fecha com folga de **1.011.666,67** na parte disponível.

### O que continua em aberto (ela declarou não ter mais informação)

- **Só documentos resolvem:** partilha do inventário (se houver meação, os números sucessórios caem ~à metade), carnês de IPTU (municípios/alíquotas), espelhos de IRPF 2024–2025.
- **3 perguntas novas (Q19–Q21):** quanto ela paga de aluguel em Higienópolis; os encargos mensais de locadora nos 9 locados; e o alerta mais importante — ela falou em "IPTU dos **vagos**", mas **não existe nenhum imóvel vago no CSV**: se houver imóvel fora da lista, todo o patrimônio do parecer muda.
- **Advogada:** se 6 anos de rompimento configuram justa causa; **contador:** IRRF na estrutura final com usufruto e a divisão de distribuição entre PFs.