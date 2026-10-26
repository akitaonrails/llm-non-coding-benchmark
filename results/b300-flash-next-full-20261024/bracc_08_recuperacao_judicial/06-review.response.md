

A entrega da Sessão 3 já está completa em disco (e o prompt repetido não pede retrabalho) — mas há uma pendência explícita sua: **revisão pré-entrega**. Em vez de reapresentar o mesmo material, vou fazer agora essa revisão sistemática: recontar toda a aritmética, conferir cada citação contra os excertos da biblioteca e amarrar as pontas entre arquivos.

Começando pela leitura integral de todas as fontes e de todos os entregáveis:










Minuta confirmada: **deságio de 60%** (classe III/IV) — credor recebe 40%. Isso muda a checagem dos lançamentos. Lendo biblioteca e entregáveis:








Sessões 1–2 revisadas; dois pontos de autoridade a ajustar (art. 58 sem excerto usado como fundamento; mecânica de votação por classe sem sinalização). Lendo o restante:








Retomando a revisão: o sweep de citações falhou na chamada anterior (parâmetro errado). Refazendo com a ferramenta correta:






Varredura cortada no meio. Pegando o restante e conferindo os textos da biblioteca que sustentam as citações sensíveis (art. 50-A e周围):






Correções aplicadas. Revalidando os três JSONs e reexecutando as verificações de soma:





Before writing the review log, one consistency check in STATUS.md line 4 ("8 entregáveis" vs. a list of 10 items):





Revisão concluída. Revisão completa de pré-entrega executada: re-lei todos os `documents/`, todos os 4 arquivos de `library/` e todos os 10 arquivos `deliverable/`; executei 31 verificações aritméticas em Python; realizei uma varredura completa de citações (cada "art./lei/CTN/CPC" confrontado com os textos efetivos da biblioteca); e re-validei os 3 JSONs (schema + D=C + totais) após cada edição.

## O que a revisão alterou (5 edições em 4 arquivos, todas de suporte de autoridade — nenhum número alterado)

1. **`sessao2/analise_plano.md` (Cláusula 1)** — Citava "arts. 57-58" como base para não homologação. A biblioteca contém uma nota sobre o art. 57, mas **não o texto do art. 58**. Agora: art. 57 como risco confirmado (concessão depende de quitação fiscal); requisitos de assembleia/art. 58 marcados como *not verified* ("não verificado").
2. **`sessao2/analise_plano.md` (Cláusula 2, ressalva iii)** — "ME/EPP vota em classe própria" não tem suporte na biblioteca. A Classe IV permanece como vem da lista de credores do cliente, mas a mecânica de votação por classe está agora sinalizada como não verificada.
3. **`sessao1/classificacao_creditos.json` (fundamento do Sul)** — Mesmo ponto: "votará em classe própria na assembleia" alterado para "votação por classe própria na assembleia: mecânica não consta da biblioteca — não verificado". O JSON foi re-validado.
4. **`sessao1/addendum_sinal_norte.md`** — "ato isolado **nulo/fraudulento**" afirmava um efeito de nulidade civil que não está na biblioteca. Reescrito como "ato atacável", listando o que *é* confirmado (crime de favorecimento de credores do art. 172, afastamento do art. 64, conversão em falência) e sinalizando a nulidade civil como não verificada. A recomendação de recusa permanece inalterada.
5. **`STATUS.md`** — A linha de status dizia "8 entregáveis"; o contrato exige **7** e a pasta `deliverable/` contém 10 arquivos (7 contratados + 2 adendos + notas). Corrigido, com um registro de revisão adicionado.

## Verificado como limpo (nenhuma mudança necessária)

- **Aritmética:** 31/13540.000→13.540.000, 7.430.000 concursal, 820.000+5.770.000−5.750.000=840.000 de caixa, ganho 0,60×6.470.000=3.882.000, novo passivo 2.588.000, todos D=C, passivo pós-plano 9.348.000, Vias A/B/C fecham — tudo confere. (Uma falha anterior em *script* era um nome de chave errado no meu validador, não um defeito de arquivo — o validador corrigido passa.)
- **Citações difíceis, sustentadas:** Leis 8.981/95 e 9.065/95 são citáveis como *citações dentro do texto do art. 50-A da biblioteca*; o art. 59 (novação) vem do cabeçalho da entrada CPC 48; o "art. 52" no `passivo_fiscal_solucao.md` refere-se à própria decisão judicial do cliente — todos mantidos.
- **Já sinalizados:** art. 66, quóruns do art. 58, art. 60-A (UPI), art. 7º III, CPC 32, alíquotas de IRPJ/CSLL, alterações de compensação pós-2024, detalhes da transação PGFN — todos rotulados corretamente.
- O lançamento 5 de id está correto *por construção* — condicional com valores `null` porque o valor contábil do galpão é desconhecido, sinalizado no arquivo, não um erro D≠C.

O log completo de alterações está em **`deliverable/REVIEW.md`**; o `deliverable/STATUS.md` recebe uma nota de revisão sob **COMPLETE WITH OPEN ITEMS** (open items = desconhecimentos documentais permanentes listados em `QUESTIONS.md`, não pontos de ação). Prontos para entrega.