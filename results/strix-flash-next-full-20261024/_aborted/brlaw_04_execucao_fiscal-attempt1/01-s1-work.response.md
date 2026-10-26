The PDF extracts fine via pdftotext. I have the full picture now — let me run the decadence arithmetic in Python before drafting.

Sessão 1 concluída. Entregas em `deliverable/sessao1/` (`analise.json` + `peca.md`), além de `deliverable/QUESTIONS.md` e `deliverable/STATUS.md` (COMPLETE WITH OPEN ITEMS).

## Análise da decadência (regras da biblioteca: CTN 150 §4º / 173 I, Súmula 555 e Tema 163/STJ)

O PAF mostra que a regra muda trimestre a trimestre (pagamento parcial → 150 §4º; nenhum pagamento/DCTF zerada → 173 I). Lançamento (auto de infração) em **03/02/2026**:

| Período | Situação no vencimento | Regra | Termo do quinquênio | Decadente? | Valor |
|---|---|---|---|---|---:|
| 3T/2020 | sem pagamento, DCTF zerada | 173 I (marco 01/01/2021) | 31/12/2025 | **SIM** | 268.000 |
| 4T/2020 | pagamento parcial R$ 61 mil (29/01/2021) | 150 §4º (FG 31/12/2020) | 31/12/2025 | **SIM** | 241.000 |
| 1T/2021 | pagamento parcial R$ 84 mil (30/04/2021) | 150 §4º | 31/03/2026 | não | 302.000 |
| 2T/2021 | sem pagamento, DCTF zerada | 173 I (marco 01/01/2022) | 31/12/2026 | não | 289.000 |

- **Decaído: R$ 509.000,00; remanescente: R$ 591.000,00** (conferência da CDA feita em Python: parcelas somam 1.100.000).
- Ponto forte: para 3T/2020 e 4T/2020 a decadência vale **sob qualquer regra ou marco alternativo** (testei 150 §4º pelo vencimento → 29/01/2026, ainda antes do lançamento) — logo, é matéria de direito puro, sem dilação probatória.
- A ressalva de fraude do 150 §4º não socorre a Fazenda: ela aplicou multa de 75% (Lei 9.430, art. 44, I) e não a dobrada de 150% (§1º, sonegação/fraude).

## Vício formal da CDA
Campo **"fundamento da multa" em branco** — violação do art. 2º, §5º, III da LEF (não se sabe se a multa é do art. 44 I ou §1º). Sanável por emenda (§8º/Súmula 392), o que já antecipo na peça: a emenda não reanima crédito decaído nem permite mudar o sujeito passivo.

## Veículo escolhido: **exceção de pré-executividade**
Matéria cognoscível de ofício com prova pré-constituída (Súmula 393), **independe de garantia do juízo** (a exigência do art. 16 §1º é só dos embargos) e corta de imediato R$ 509 mil. Embargos ficam reservados para as questões probatórias (ex.: falta de baixa dos DARFs pagos), com prazo correndo da garantia.

**Alertas para as próximas sessões** (já registrados na peça e nas perguntas): a certidão negativa do oficial (28/09/2026) antecipa o redirecionamento, mas a mudança de endereço foi comunicada à JUCESP (12/03/2026) e à RFB (20/03/2026) **antes da diligência** — o que afasta a presunção da Súmula 435. Perguntas ao cliente sobre DARFs, citação, sócios e bens estão em `QUESTIONS.md`.