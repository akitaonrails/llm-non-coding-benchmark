# STATUS — DAS maio/2026 · Lumen Soluções Digitais ME

**COMPLETE WITH OPEN ITEMS** — fase de perguntas **encerrada** (cliente sem informação
adicional na 2ª rodada; nada foi re-perguntado)

Entregáveis em `deliverable/`: `apuracao.json` ✓ · `memoria.md` ✓ (encerramento no §9) ·
`PERGUNTAS.md` ✓ (registro em `QUESTIONS.md`) ✓

Resultado final: **Anexo V, 4ª faixa, alíquota efetiva 18,8235%** (RBT12 = R$ 1.020.000;
folha paga 12m = R$ 284.600; Fator R = **27,90%** < 28%) · Serviços (78.000, estorno de 4.000
deduzido): **R$ 14.682,35** · Locação de bens móveis segregada (6.000, Anexo III sem ISS):
**R$ 506,49** · **DAS total: R$ 15.188,84**. Corrigimos a instrução do sócio em dois pontos,
com base na biblioteca: (i) usa-se a **alíquota efetiva** (§1º-A), não a nominal da faixa;
(ii) a locação é **segregada** e sem ISS, não "vai junto com os serviços". A resposta da 1ª
rodada (pró-labore de abril pago em **30/04/2026**, na janela) elevou a folha para 284.600 e
o Fator R para 27,90%, **sem alterar o enquadramento nem o valor**; a 2ª rodada não trouxe
novos fatos.

## Itens em aberto — explicitamente sinalizados (U1–U6 em QUESTIONS.md)

1. **U1 — Pró-labore de março/2026:** único ponto capaz de mudar o Anexo. O resumo traz
   zero na linha 2026-03 e o cliente não confirmou pagamento além do registrado; premissa
   adotada: não houve. Se existir pagamento ≤ 30/04/2026 não registrado: 287.800 → **28,22%
   → Anexo III**, DAS total 10.261,08. Resultado principal mantém **Anexo V** (todas as
   leituras documentadas: 27,44%–27,90%).
2. **U2 — Comprovante do pró-labore de abril (30/04) prometido e não entregue:** divergência
   com o e-mail do sócio ("6 de maio", débito ausente do extrato) registrada sem forçar
   reconciliação. **Sem efeito no resultado** (ambas as datas → Anexo V).
3. **U3 — Repartição do Anexo V indisponível na biblioteca:** o campo `reparticao` do JSON
   contém **apenas a cota da locação** (R$ 506,49 decomposta), não a dos serviços
   (R$ 14.682,35). Não inventamos números.
4. **U4 — Dedução do ISS na locação:** premissa adotada em definitivo — proporcional à
   alíquota efetiva (8,4415% → 506,49); alternativa sobre a nominal daria total 15.120,70
   (−68,14). Memória §5.3.
5. **U5 — Premissas de caixa da folha** (salários/PL no mês; encargos com 1 mês de
   defasagem; encargos 04/2025 = 4.700 não documentados): não confirmáveis; sensibilidade
   27,44%–27,90% não altera o Anexo.
6. **U6 — Tabela de repartição da biblioteca soma 99,85%** (cotas não-ISS da locação:
   505,36 vs 506,49, diff 1,13): divergência da própria fonte, deixamos aberto.

Nada foi calculado com base fora de `library/INDEX.md`; regras que faltam na biblioteca estão
rotuladas como NÃO VERIFICADAS na memória §7.
