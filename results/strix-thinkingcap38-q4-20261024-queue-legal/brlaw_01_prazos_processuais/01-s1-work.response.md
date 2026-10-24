I have the contract, documents, and library. Let me verify the dates with a Python calculation, showing the arithmetic day by day.



The math checks out. Now let me verify the key date determinations before writing the deliverables:



All dates are verified. Let me write the deliverables.



Let me clean up two small slips in `memoria.md`:



Now the status file:



Engajamento concluído. Resposta ao sócio e datas calculadas:

## Prazo em dobro — **NÃO se aplica**
Apesar de haver dois réus com procuradores de escritórios distintos, o **CPC art. 229, §2º** exclui expressamente o prazo em dobro dos **processos em autos eletrônicos** — e este é e-SAJ. Contagem é simples.

## Datas

| Prazo | Início (primeiro dia útil após a publicação) | **Vencimento** |
|---|---|---|
| **Contestação** (15 d.u., art. 335) | publ. 23/11 → início 24/11/2026 | **16/12/2026 (qua)** |
| **Embargos de declaração** (5 d.u., art. 1.023) | publ. 11/12 → início 14/12/2026 | **21/01/2027 (qui)** |
| **Apelação** (15 d.u., art. 1.003 §5º) | idem | **04/02/2027 (qui)** |

**Descontos aplicados** (verificados dia a dia em Python):
- Citação: 20/11 (Consciência Negra), 08/12 (feriado municipal de Campinas) e fins de semana fora da contagem.
- Sentença: **recesso 20/12/2026–20/01/2027** (art. 220) + fins de semana; Natal e Réveillon caem dentro do recesso. **25/01/2027** tratado como dia útil (Aniversário de SP é feriado só da Capital, não de Campinas).
- Publicação/início conforme Lei 11.419/2006 art. 4º §§3º–4º e CPC art. 224 §§2º–3º.

## Entregáveis
- `deliverable/prazos.json` ✓
- `deliverable/memoria.md` ✓ (contagem dia a dia + fundamentos)
- `deliverable/STATUS.md` ✓ — **COMPLETE WITH OPEN ITEMS**

**Pendências** (marcadas na memória e no status):
1. Se o cliente opuser **embargos de declaração** (limite 21/01/2027), a apelação **interrompe-se** e a data de 04/02/2027 deixa de valer — o recomeço depende do despacho de rejeição (ato futuro do juízo).
2. Recomendo conferir o comunicado do TJSP sobre **25/01/2027** antes de carimbar o calendário; se valesse também para Campinas, a apelação desliza para **05/02/2027**.