The client's reply materially changes the result — the April pro-labore was paid **inside** the 12-month window (30/04), which I must recompute for the Fator R (payment regime). Let me first check whether the receipt arrived, then recompute:

All figures verified. The client's clarification flips the Fator R to ≥28% → services move to **Anexo III**. Now rewriting all deliverables:

Now updating the remaining deliverables to the round‑2 state:

Final sanity pass — JSON validity and cross-file numeric consistency:

All deliverables are updated to the round‑2 state and verified consistent. Final result:

## DAS maio/2026 — Lumen Soluções Digitais ME: **R$ 10.261,08** (Anexo III)

The client's clarification **changed the outcome**: the April pró‑labore (R$ 3.200) paid **30/04/2026** falls inside the payment window (mai/2025–abr/2026), so the folha paga becomes:

- Salários 193.000 + pró‑labore 38.400 (12×3.200: 11 no resumo + o de 30/04 não lançado) + CPP/FGTS 56.400 = **287.800**
- **Fator R = 287.800 ÷ 1.020.000 = 28,22% ≥ 28% → serviços no Anexo III** (era Anexo V na v1)

| Componente | Receita | Cálculo | DAS |
|---|---:|---|---:|
| Serviços (Anexo III, 4ª faixa) | 78.000,00 | efetiva (1.020.000×0,16 − 35.640)/1.020.000 = 12,5059% | 9.754,59 |
| Locação notebooks (Anexo III sem ISS) | 6.000,00 | ×12,5059% ×(1−32,5%) | 506,49 |
| **Total** | 84.000,00 | | **10.261,08** |

Repartição agora integralmente verificável na biblioteca (ambos Anexo III): IRPJ 420,20 · CSLL 367,67 · COFINS 1.475,94 · PIS 320,40 · CPP 4.490,86 · ISS 3.170,24 — soma 10.245,31, **15,77 abaixo do DAS** porque a tabela da biblioteca soma 99,85%; deixado à vista, não balanceado.

## ⚠ Dependência crítica — um comprovante

O resultado pende de **um único pagamento de R$ 3.200**:

- Pago em **30/04** (cliente; comprovante anunciado mas **ainda não chegou** a `documents/` — verifiquei) → folha 287.800 → **Anexo III → 10.261,08**
- Pago em **06/05** (versão do e‑mail do sócio) → folha 284.600 → 27,90% → **Anexo V → 15.188,84**

Diferença: **R$ 4.927,76**. Margem sobre o limiar de 28%: só R$ 2.200 de folha. Sensibilidade documentada em `memoria.md` §5.2.

## Arquivos (`workspace/deliverable/`)

- `apuracao.json` — Anexo III, folha 287.800, fator_r 0.282157, notas de dependência do comprovante (JSON validado, aritmética conferida em Decimal)
- `memoria.md` v2 — reconstrução da folha por pagamento, tabela de sensibilidade, estorno resolvido (Q3), repartição verificável, e o achado de que o DAS de abril pago (10.480,22) é **compatível com Anexo III e incompatível com Anexo V** — contra a fala do sócio de "ano passado Anexo V"
- `STATUS.md` — **COMPLETE WITH OPEN ITEMS**: comprovante pendente, premissa CPP abr/2025 = 4.700, falta segregação dos 12 meses, escopo "TI" das notas 1183/1186, gap de 99,85% da tabela
- `QUESTIONS.md` / `PERGUNTAS.md` v2 — Q1/Q3 registradas como respondidas (não re‑perguntadas); desconhecidos restantes sinalizados sem re‑pergunta, pois o cliente informou não ter mais informação