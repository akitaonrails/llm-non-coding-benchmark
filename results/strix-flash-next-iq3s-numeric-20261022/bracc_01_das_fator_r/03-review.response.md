Now a verification pass. First, let me re-check every number and citation in the deliverables against the sources.

Agora as correções nos arquivos de unknowns e de status:

Todos os 54 testes passaram, mas o script expôs um erro de aritmética no bloco indicativo de junho/2026. Vou conferir as fontes antes de corrigir:

O validador apontou um erro de soma no bloco indicativo de junho/2026 (que existia em `memoria.md` e no JSON). Corrigindo nas duas fontes:

Revisão concluída. **O DAS apurado não mudou: R$ 15.188,84.** Mas a revisão encontrou **16 problemas reais** na entrega anterior — todos corrigidos e listados em `workspace/deliverable/REVISAO.md`.

## O que foi mudado (16 itens)

**A. Conciliação do extrato — alegações que não constam dos documentos (4)**
1. Removida a afirmação de que o PDF traria um débito "OUTBACK STEAK R$ 120,00" — **não existe** nem no CSV nem no texto integral do PDF.
2. Removida a afirmação de que o saldo final do PDF seria R$ 100,00 menor — os dois arquivos trazem o mesmo cabeçalho (abertura 41.280,55 / créditos 88.000,00 / débitos 43.180,22 / final 86.100,33).
3. Removida a suposta "inconsistência de saldo em 28–29/05" — conferência linha a linha das 15 linhas: **0 divergências** (81.600,33 + 8.500,00 = 90.100,33; − 4.000,00 = 86.100,33).
4. Passou a registrar que o rodapé do PDF declara **instituição bancária fictícia (material de benchmark)** e as diferenças apenas de forma entre PDF e CSV.

**B. Aritmética recomputada (5)**
5. Cenário "treinamento no Anexo III": recomputado para **14.904,54** (Δ −284,30) — 13.835,29 + 562,76 + 506,49.
6. Confrontos de abril/2026 recalculados: **16.376,47** (V) · **10.880,12** (III) · **10.636,25** (segregado).
7. §6.3 (método do sócio) refeita com as parcelas explicitadas: **+1.307,65** + **723,51** = **+2.031,16**.
8. Carga efetiva do mês explicitada: **0,180820** (15.188,84 ÷ 84.000,00).
9. **O achado mais grave: a conta indicativa de junho/2026 não fechava.** A versão anterior escrevia "284.600 − 23.400 + 16.600 + 4.700 = 285.700" — esses quatro termos dão **282.500** — e concluía que junho iria ao **Anexo III**. Refeita por competência: entrada de mai/26 = 16.600 + 3.200 + 4.700 = 24.500 → folha **285.700** → fator R **27,85% < 28%** → **junho/2026 ainda no Anexo V** (limiar 287.280, margem 1.580). O Anexo III só aparece na variante com a lacuna de U1 (288.900 → 28,16%).

**C. Autoridade: separar lei × inferência × indicativo (4)**
10. O redutor de ISS da locação (**67,50%**) deixou de soar como texto de lei: é **inferência documentada (P7)**, porque `library/locacao_bens_moveis_iss.md` manda deduzir "a parcela correspondente ao ISS" **sem fixar percentual**; sensibilidade registrada (ISS 32,65% → DAS 15.187,71, Δ −1,13).
11. O cálculo de abril/2026 foi rebaixado de fato para **INDICATIVO** (falta o RBT12 de abr/2025–mar/2026).
12. Registrado que o **estorno da NFS-e 1188 não altera o fator R** (mai/2026 está fora da janela 05/2025–04/2026).
13. Criada a premissa **P6** (faixa pelo **RBT12 global**, leitura literal do §1º-A) e o unknown **U9**, com a alternativa quantificada e **não adotada** (locação 243,00 → DAS 14.925,35, Δ −263,49).

**D. Consistência e rastreabilidade (3)**
14. **Convenção de arredondamento explicitada** (cada bloco ao centavo e depois somado) + conferência exata sem arredondar.
15. Numeração **unificada U1–U9 e P1–P7** nos cinco arquivos (as referências soltas "Q5/Q7/Q8/Q9" foram substituídas).
16. O comprovante do pró-labore de 30/04/2026 passou a ser rotulado como **alegação do cliente** (não está em `documents/`).

## Validação
Toda a aritmética foi refeita por um validador independente em `Decimal`: **87 verificações, todas PASS**, incluindo as somas batendo direto com `faturamento_12_meses.csv`, `resumo_folha_12_meses.csv` e `extrato_maio_2026.csv` (resíduo zero).

## O que continua em aberto — e é o único risco material
**U1:** a folha **paga** na janela 05/2025–04/2026 não está comprovada por documentos de pagamento, e a linha **2026-03** do resumo traz pró-labore **0,00** sem explicação. A folha atual é 284.600,00 e o limiar é **285.600,00** — **faltam R$ 1.000,00**. Se a folha paga for ≥ 285.600,00, os serviços migram para o **Anexo III** e o DAS cai para **10.261,08** (−4.927,76). A mesma incógnita decide junho/2026 (item 9). U2–U9 seguem sinalizados, sem repetição de perguntas já respondidas.

Arquivos em `workspace/deliverable/`: `apuracao.json`, `memoria.md`, **`REVISAO.md`** (novo), `QUESTIONS.md`, `PERGUNTAS.md`, `STATUS.md` — status **COMPLETE WITH OPEN ITEMS**. Sem git no workspace, as mudanças estão apenas nos arquivos (não commitadas).