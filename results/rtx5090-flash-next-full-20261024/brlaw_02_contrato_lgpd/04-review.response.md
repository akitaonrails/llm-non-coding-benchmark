Vou revisar tudo sistematicamente: (1) cada citação contra os arquivos da biblioteca, (2) toda a aritmética re-executada, (3) consistência interna entre os entregáveis.

Todos os alicerces da biblioteca correspondem. Agora o resto do JSON e uma nova execução da aritmética:

Continuing the review: the recomputation confirms the one discrepancy I found — the Cl. 2 reajuste figure. Let me locate its exact wording and fix it:

All four fixes applied. Final validation sweep — JSON integrity, every cited statute against the library allow-list, and a re-scan for stale figures across all five files:

Spot-checking the Cl. 13 JSON figures and confirming the REsp 1.707.855 actually appears in the library file (line 6 was truncated):

All checks pass. The pre-delivery review is complete — here is the full report of what was found and fixed.

## Revisão pré-entrega — relatório

### Erros encontrados e corrigidos (4)

1. **`clausulas.json`, Cl. 2 (reajuste) — conta rotulada errada.** O texto dizia "1% ~ R$ 7.452,00 no ano 2", que é 1% do contrato inteiro (745.200) rotulado como se fosse o impacto no ano 2 — não é o que um reajuste de 1pp acima do esperado faz no ano 2. **Corrigido** para a conta real, com aritmética: 1pp acima do esperado pesa R$ 207/mês sobre parcelas futuras → **~R$ 2.484** por ciclo de 12 meses reajustado (12 × 207), **~R$ 4.968** se o excesso incidir sobre as 24 parcelas restantes após o 1º reajuste, e **~R$ 7.477** no contrato inteiro se os dois reajustes anuais (meses 13 e 25) vierem 1pp acima (efeito composto). O número antigo "7.452" foi inteiramente removido.

2. **`nota_socia.md` §4 — base do percentual do teto ambígua.** "8,3% do valor do contrato" conflitava com a linha anterior da tabela que chama "R$ 793.200" de contrato em 36 meses (aí daria 7,8%). **Corrigido** com base explícita: "8,3% das mensalidades de 36 meses (62.100 ÷ 745.200 = 8,33%; 20.700 ÷ 745.200 = 2,78%)" — agora bate com o fundamento da Cl. 8 no JSON.

3. **`clausula_dados.md` §2º — remisso impreciso.** "escapar da base legal do §1º/§3º" apontava para parágrafos que tratam de limitações e vedações, não de base legal (que está no §2º). **Corrigido** para "das bases legais e limitações dos §§1º a 3º".

4. **`clausula_dados.md` §13º — referência cruzada desatualizada.** A nota do DPO apontava para `PERGUNTAS.md`, onde essa questão não está mais (era fato da ficha, não pergunta em aberto). **Corrigido** para apontar a `nota_socia.md` §5, onde a designação do encarregado está tratada (com o due diligence de transparência sobre arts. 41/52 não estarem na biblioteca).

### O que foi verificado e **não** exigia correção

- **Autoridade — 100% biblioteca fechada.** Re-li os 5 arquivos de `library/` e bati cada citação dos 5 entregáveis: CC 421-A/413/422, CPC 63 §§1º/3º, CDC 2/3/51, REsp 1.203.109/MG + 680.815/PR + 1.707.855/SP (confirmado no arquivo CC), Res. CFM 1.821/2007 + 2.299/2021 + Lei 13.787, LGPD arts. 5º/11/12/33/37–39/42/46–48 + Res. CD/ANPD 15/2024. Varredura automática: **nenhum artigo citado fora da allow-list**. Os únicos "art. 41/52" que aparecem estão dentro do disclaimer deliberado "não citado" — corretos assim.
- **Aritmética — re-rodada em Python, tudo confere.** Mensal 3 × 6.900 = 20.700; 36m = 745.200; total 793.200 (8,62% de 9,2 mi); renovação leva a 1.538.400; multa mês 12 = 496.800 (paga o contrato inteiro: 296.400 + 48.000 + 496.800 = 793.200 ✓; 1,68× o já pago); mês 30 = 124.200; mês 1 = 724.500; cap 62.100 = 8,33% de 745.200 e R$ 2,82/paciente; multa 500.000 = 24,2 mensalidades = 8,1× o cap; SLA 99% = 87,6h/ano; crédito máx. R$ 2.070 atingido a 94%; 30/7.300 = 0,41%.
- **Consistência entre arquivos.** Cifras-chave batem entre JSON e nota; o "24 mensalidades" da nota vs. "24,2" do JSON é só arredondamento da mesma conta (500.000 ÷ 20.700 = 24,15); itens §10º (i)–(vii) sem repetição; Cl. 14 foro segue **aceitavel** com a refutação à tese de anulação pelo CDC na nota §2.
- **JSON íntegro:** parseia, 16 entradas, avaliar inalterado — **7 alterar / 8 aceitavel / 1 inserir**.

### Status

`workspace/deliverable/` está pronto para entrega: **COMPLETE WITH OPEN ITEMS** — os open items continuam sendo apenas os fatos sinalizados que não travam nada (uso de dados pela NEXA em P&D, cidades das unidades, pré-autorização na integração, certificações da NEXA), todos listados em `STATUS.md`/`PERGUNTAS.md` como diligência, não como perguntas sem resposta da cliente.