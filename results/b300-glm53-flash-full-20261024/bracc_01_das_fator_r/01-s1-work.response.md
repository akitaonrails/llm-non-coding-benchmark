Calculations verified. Now writing the deliverables.

Fixing two typos in memoria.md.

Now the STATUS.md:

Engagement complete. Deliverables are in `workspace/deliverable/`:

## Result — DAS maio/2026: **R$ 15.188,84**

| Rubrica | Base | Anexo/Faixa | Alíq. efetiva | DAS |
|---|---:|---|---:|---:|
| Serviços | 78.000,00 | V / 4 | 18,8235% | 14.682,35 |
| Locação bens móveis | 6.000,00 | III / 4, deduzido ISS 32,50% | 12,5059% × 0,675 | 506,49 |

## Key findings (vs. the sócio's instructions)
- **Anexo V confirmed, but by computation, not repetition:** RBT12 = R$ 1.020.000 (mai/25–abr/26); folha paga 12m = R$ 281.400 after excluding the **April pró-labore paid late on 06/05** (Res. CGSN 140, art. 26 §2º — paid-month rule). Fator R = **27,59% < 28%** → Anexo V, 4ª faixa (equation 28% × RBT12 = R$ 285.600 was never reached under any reading: 25,49%–27,90%).
- **Rate correction:** the sócio wanted the bracket's nominal rate (20,50%); LC 123/2006 art. 18 §1º-A requires the effective-rate formula → **18,8235%** (averted overcharge of R$ 1.307,65 on services).
- **Estorno:** the R$ 4.000 partial cancel of NFS-e 1184 reduces May services to 78.000 (documented in nota 1188 and the 29/05 PIX); it does not touch RBT12 since May is outside the 12-month window.
- **Locação of notebooks does NOT "go with services":** per the library (SV 31 / art. 18 §5º-A) it's Anexo III **deduzido do ISS (32,50%)**, kept as a separate revenue and tax line.

## Open items (STATUS.md = COMPLETE WITH OPEN ITEMS)
1. **Anexo V repartição is not in the library** — `reparticao` in `apuracao.json` left zeroed and flagged unverified (does not affect the DAS total); the Anexo III split used only to deduct ISS from the locação.
2. **No 06/05 bank debit matches the claimed pró-labore payment** — substitute question raised in `QUESTIONS.md`; irrelevant to May's DAS but relevant to June's Fator R.
3. Assumptions A1–A4 stated prominently in `memoria.md` (composition of the 12-month revenue history, prior-month folha payment timing impossible to remap without older extracts, PDF extract unreadable → CSV mirror used, fully cross-checked against the notas).