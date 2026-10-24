

Client confirmed the April pró-labore was paid **30/04/2026** — inside the window. Let me update the calculations:





Agora atualizando a memoria de cálculo — §3 (folha), sensibilidade, pontos abertos:





Now the questions files and STATUS:





Both files are identical. Rewriting them as an answered-question log with remaining unknowns flagged (not re-asked):





Final consistency check:





Apuração atualizada com a resposta do cliente. Resumo:

## O que mudou

**Pró-labore abr/2026 (R$ 3.200,00): incluído na folha.** O cliente confirmou pagamento em **30/04/2026** — dentro da janela mai/25–abr/26. Isso resolve a contradição que eu havia apontado: o e-mail anterior ("paguei dia 6 de maio") estava errado, e o extrato de maio de fato não tem esse débito, corroborando pagamento em abril.

- Folha 12m: 281.400 → **284.600,00** (salários 193.000 + pró-labore 35.200 + encargos 56.400)
- Fator R: **284.600 / 1.020.000 = 27,90% < 28% → Anexo V** (confirmado)
- DAS maio/2026 **não muda**: serviços 78.000 × 18,823529% = 14.682,35 + locação 6.000 × 8,441471% = 506,49 → **R$ 15.188,84**
- O enquadramento é robusto: mesmo que o comprovante prometido (ainda não recebido) mostrar data posterior, a folha volta a 281.400 (27,59%) — continua Anexo V.

## Desconhecidos sinalizados (cliente sem informação adicional — não re-perguntados)

1. **Pró-labore mar/2026 — único risco de mudança de anexo.** O resumo traz 0,00 na linha 2026-03 e o cliente não soube informar. Se existir ~3.200,00 pago dentro da janela: folha 287.800 → Fator R **28,22% ≥ 28% → Anexo III** → DAS total cairia para **10.261,08** (DAS serviços 9.754,59). Verificável no extrato de mar/2026, que não foi fornecido. Deixei quantificado na sensibilidade da memória.
2. Cotas de repartição do Anexo V fora da biblioteca → repartição dos serviços marcada **NÃO VERIFICADO** (total do DAS independe delas).
3. Equivalência de caixa dos encargos (4.700 fixos/mês) permanece inferência; no pior cenário testado (279.900 → 27,44%) o Anexo V se mantém.
4. Base do `faturamento_12_meses.csv` (líquida? inclui locação?) não confirmada — afeta RBT12.
5. DAS abr/2026 (10.480,22) continua sem reconciliação com os documentos; sem efeito em maio.

## Arquivos

- `workspace/deliverable/apuracao.json` — folha 284.600, fator_r 0,279020; repartição confere com o DAS (15.188,84)
- `workspace/deliverable/memoria.md` — §3 reescrito (pró-labore abr incluído), sensibilidade A–D, §5 com os 6 abertos
- `workspace/deliverable/QUESTIONS.md` / `PERGUNTAS.md` — Q2 marcada como respondida; as demais viraram desconhecidos sinalizados (U1–U5), sem repetir perguntas
- `workspace/deliverable/STATUS.md` — **COMPLETE WITH OPEN ITEMS**

Pendência material principal: o comprovante de 30/04 (prometido) e, se quiser encerrar o único risco de anexo, o extrato bancário de março/2026.