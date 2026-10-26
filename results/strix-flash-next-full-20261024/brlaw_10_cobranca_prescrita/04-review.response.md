Revisão sistemática: vou (a) auditar cada citação contra o `library/INDEX.md`, (b) recalcular todos os números, inclusive os de apoio (encargos na data da inscrição), e (c) conferir a consistência entre os arquivos.

Three edits from the previous batch were rejected due to malformed parameters. Re-applying them properly now:

Let me check the current state of §2 and §7 to see what actually got applied:

All targets confirmed. Applying the remaining fixes in parallel:

Nine of ten applied. Let me get the exact STATUS.md text and finish:

One leftover "IPCA/IBGE" in §10 item 1. Fixing, appending the revision log, and re-validating:

PERGUNTAS.md is just a pointer stub — correct as is. Final authority-token audit across all four deliverables against the library:

The "art. 202" flag is a case-sensitivity artifact — the library text has "**Art. 202.**" (capitalized), so it's present. All cited authorities resolve to the library; JSON parses with exact schema keys; memorandum has clean sections 1–10 plus the new revision log.

Audit complete. Here's the full review-and-fix report:

## Revisão pré-entrega — o que foi auditado, encontrado e corrigido

**Auditoria feita:** (1) cada autoridade citada nos 4 entregáveis confrontada texto a texto com a `library/`; (2) toda a aritmética recalculada em Python; (3) consistência interna de datas/valores entre `memorando.md`, `analise.json`, `QUESTIONS.md` e `STATUS.md`.

### Erros encontrados e corrigidos

| # | Onde | Problema | Correção |
|---|---|---|---|
| 1 | Memorando §5 | Encargos "≈ R$ 76 mil" na data da inscrição estavam **errados** | Recalculado pro rata die até 12/08/2026: juros **79.753,33** (10.260 + 7.373,33 + 21.010 + 20.710 + 20.400) + multa 2.400 → crédito exigível atualizado ≈ **R$ 192.153** (sem IPCA). Tese refinada: os R$ 180 mil lançados **não** superam o total atualizado — o problema é a **composição** (R$ 70 mil mortos/pagos), não o valor global |
| 2 | Memorando §10.3 | "reconhecimento posterior a fev/mar de **2026**" — marco temporal errado | Reformulado: nada houve entre os vencimentos (10/02 e 10/03/2021) nem depois |
| 3 | `analise.json` | "encargos… já passavam de R$ 180 mil" — vago | Explicitado: ≈ R$ 192.153 na data da inscrição (juros 79.753 + multa 2.400) |

### Autoridade não suportada — removida ou marcada como não verificada

| # | Onde | Problema | Correção |
|---|---|---|---|
| 4 | §2 | Afirmava "mandado de pagamento" e "embargos com efeito suspensivo" (CPC 701/702) — **fora da library** | Frases removidas; preferência pela monitória agora apoiada só no art. 700; defesas da devedora marcadas como matéria a conferir na petição |
| 5 | §2 | "contrato de 2020 subscrito em papel" — fato não verificado nos autos | Substituído pela nota da própria library (Tema 1.247 "não aplicável aqui") + fala do cliente ("meio informal") |
| 6 | §4 | Citava nominalmente CC arts. 323/324 (imputação) — fora da library | Passou a "regra legal de imputação (externa à library → não verificada, não citada)" |
| 7 | §6 | Protesto "útil para **constituir a mora**" — sem suporte na library | Removido; juros correm do vencimento por cláusula contratual |
| 8 | §8.2 | Citação do art. 189 sem ressalva | Agora sinaliza que o artigo está no INDEX mas **não transcrito** no arquivo da library |
| 9 | §4/§10, QUESTIONS, STATUS | Referências a "IBGE" como fonte | Generalizadas para "fatores oficiais do IPCA em fonte externa ao acervo — não verificável neste workspace" |

### Overstates fáticos atenuados

| # | Onde | Correção |
|---|---|---|
| 10 | §2/§7 | "relatórios mostram os 6 meses entregues" → cliente disse "fez o que deu"; relatórios de fev/mar existem mas conteúdo/datas a conferenciar (a devedora discutiria prestação parcial) |
| 11 | §3 | E-mail de 15/09/2022 agora marca expressamente que é a **única** interrupção admitida (art. 202 caput) |
| 12 | §4 | Convenção pro rata die/mês-30d sinalizada como método nosso, não da library |

### Confirmados corretos (sem mudança)
- Juros a 12/10/2026: **81.990,00** (P1 10.260+7.780; P2 21.620; P3 21.320; P4 21.010); total **194.390,00**; sensibilidade +11.000/+8.439 por 10% IPCA; reconcile 110.000+60.000+10.000=180.000.
- Prescrições (termos 15/09/2027 / 10/02.2026 / 10/03.2026), todos os tokens citados (784 III, 700, 202, 206 §5º I, 189, 389/406, 14.905, Súmulas 385/299/503, REsps 1.438.263/1.792.700, Lei 9.492/97, CDC 43 §5º, Temas 1.247/1.264) presentes na library.
- `analise.json` parseia e bate campo a campo com o schema do CONTRACT; `PERGUNTAS.md` (alias-stub) OK.

Um bloco "Revisão de 12/10/2026 (pré-entrega)" foi acrescentado ao fim do memorando para rastreabilidade. **STATUS segue COMPLETE WITH OPEN ITEMS** — único ponto vivo é a pergunta 7 (data/texto dos relatórios de P5–P6); se vierem relatórios assinados após 10/02–10/03/2021 com reconhecimento da obrigação, a prescrição de P5–P6 é reaberta para reanálise.