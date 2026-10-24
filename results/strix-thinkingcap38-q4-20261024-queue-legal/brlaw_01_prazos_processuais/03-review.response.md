Let me do a careful self-audit — re-reading every deliverable and re-checking each calculation and citation.



Let me run an independent re-verification of every date (with a fresh, separate re-implementation) and cross-check the day-of-week labels:



The audit found real errors. Let me verify my findings precisely before fixing:



I've confirmed that the two "dobro" hypothetical dates were miscalculated in my earlier check—I missed that Carnival 2027 (08–09/02) is excluded—which is significant because one of them actually fell on Carnival. Now I'll verify the correct dates and do a final check on all the day-of-week labels.



All **firm** dates are confirmed correct by an independent re-implementation. But the audit caught real errors in the "dobro" hypothetical dates: I had omitted **Carnaval 2027 (08–09/02)** from those two counts. Let me check the client-facing note, then fix everything.



The client-facing note is clean (it contains only firm dates). Now fixing the defects I found in `memoria.md`:

1. **Line 16 — garbled sentence**: I wrote that the "embargos" (5 days) expires *before* the court recess ends — but actually the 4th day is 18/12, and the recess pushes the deadline to 21/01/2027, which is *after* the recess.
2. **Line 16 — unsupported citation**: "CPC art. 1.023, §ÚNICO" — the library's excerpt states the interruption via **art. 1.026**, and the "§ único" provision does not appear in the library.
3. **Line 23**: garbled day-of-week label ("sexta→…") → Monday.
4. **§5 "Arrepião: nenhum" (none)** — this claim has been falsified by this audit (two calculation errors); I'll rewrite it honestly.
5. **§6 table + STATUS.md**: my "dobro" hypothetical dates were wrong — I forgot Carnival 2027 (08–09/02). Correctly: **contestation is 10/02/2027** (not 08/02), **appeal is 01/03/2027** (not 25/02). Embargos 28/01/2027 is correct.



I made an arithmetic mistake in the table header ("60 d.u." should be "30 d.u."). Fixing:



Final sweep for any leftover erroneous text across all deliverables:



Revisão concluída. O que a auditoria encontrou e o que corrigi:

## Erros encontrados

**Erros substantivos (números):**
1. **Datas hipotéticas "de dobro" erradas** (`memoria.md` §6 e `STATUS.md` item 3): nas contagens de 30 dias úteis, eu havia **esquecido de excluir o Carnaval 2027 (08–09/02)**. Correto:
   - Contestação "de dobro": ~~08/02/2027~~ → **10/02/2027 (qua)**
   - Apelação "de dobro": ~~25/02/2027~~ → **01/03/2027 (seg)**
   - Embargos "de dobro": 28/01/2027 ✓ (confirmado, não mudou)
   - O detalhe relevante: a data errada de 08/02/2027 **era** domingo — Carnaval feriado da biblioteca.
2. **Alegação "Arrepião: nenhum" em `memoria.md` §5** — falsa, já que a revisão acabou de encontrar erros reais. Resscrevi a seção para descrever honestamente a verificação em duas passadas e o que foi corrigido.

**Erros de texto/citação:**
3. **`memoria.md` linha 16 (aviso §1)** — frase com erro de raciocínio: dizia que os embargos "terminam **antes** do recesso acabar", quando na verdade o 4º dia é 18/12, o recesso paralisa a contagem, e o vencimento (21/01/2027) é **após** o recesso. Corrigido.
4. **Citação não suportada pela biblioteca**: "CPC art. 1.023, **§ÚNICO**" — o § único não aparece no excerto da biblioteca; a interrupção consta ali **via art. 1.026** ("a oposição de embargos interrompe o prazo — art. 1.026"). Substituí a citação por "CPC art. 1.026, conforme transcrito junto ao art. 1.023 em `cpc_prazos_recursais.md`".
5. **Rótulo de dia da semana corrompido**: "23/11/2026 (sexta→…)" → **23/11/2026 (seg)**.

## Verificado e íntegro (sem mudança)
- **Todas as datas firmes** re-confirmadas por implementação independente em Python (publicação, início, 15 d.u. contestação, 5 d.u. embargos, 15 d.u. apelação) — `prazos.json` batia 7/7 com o recalculo.
- **`prazos.json`** íntegro: válido, `prazo_em_dobro: false` com fundamento; os 4 itens de `dias_suspensos_ou_feriados_considerados` conferem com o calendário.
- **`resposta_prazo_em_dobro.md`** (nota ao sócio) verificada linha a linha: contém apenas datas firmes e a citação correta do art. 229 caput/§2º — sem correções necessárias.
- Todas as demais citações apontam para arquivos em `library/INDEX.md`; nenhum fato novo foi inventado; nenhuma data de dia da semana restante falhou na auditoria automatizada.

Status mantido: **COMPLETE WITH OPEN ITEMS** (as duas ressalvas legítimas — comunicado sobre 25/01/2027 e apelação pós-embargos — permanecem, pois dependem de atos/atos comunicados futuros, não de erro de cálculo).