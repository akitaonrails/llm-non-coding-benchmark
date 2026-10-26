

Good practice before delivery. I'll re-verify from the ground up: every citation against the actual library text, every number across files, and the internal cross-references. Starting with the library (the ground truth) and the full v2 `parecer.md`:






Continuing the review. Let me read the full library texts and the current deliverables to verify every citation.






The full library is now verified against the parecer. I've found several real issues — including one significant one about **CC art. 977's literal text** ("entre si **ou com terceiros**") that undercuts the recommended design's claimed compliance. Let me read the remaining deliverables before making the fixes:






Continuing the review round. I have the library ground truth verified; now I need the exact current text of each deliverable to apply the fixes. Let me re-read the files:






Now the remaining three deliverables:







The grep output truncated; I'll re-grep with a narrower set and re-read the two files I need exact strings from (parecer in two passes so nothing truncates):






I have the full parecer. Now I need the exact remaining text of the other files (previous reads truncated):







I have all target strings. Before writing the batch-fix script, one byte-level inspection (curly vs straight quotes and the en dash have broken edits before), plus STATUS.md in full:






Files use ASCII quotes throughout — good. Two final ground-truth checks before applying (exact wording of art. 977 in the library, and INDEX count), plus `numeros.json` to confirm it needs no touch:






I have all ground truth I need: the exact art. 977 text from the library, confirmation that all deliverables use ASCII quotes, and the exact current text of every target line. The fix script has not been run yet — applying it now. Writing the script to disk first (avoids heredoc quoting risks), with an idempotency guard (old count==1 → apply; old==0 & new present → skip as already applied; else hard fail, nothing written):





Now the remaining pair files (parecer part 2, contrato+checklist, QUESTIONS+STATUS):





Before writing pairs_c/d, let me verify the exact old strings in the other four files:





Several lines were cut at my display limit — I need full tails of a few target lines:





All old strings confirmed (including the exact `||` tail and line 52 wording). Writing the last two pair files:






Now run the fix engine:





第3次运行重复应用了3个重复对（`old` 是 `new` 的前缀，而我的跳过条件只检查 `count(old)==0`），所以三个附加片段现在都出现了两次。让我验证重复结构并删除多余的副本：





Confirmed — each snippet is duplicated back-to-back. Removing the second copy in each file:





De-duplication concluída — cada bloco aparece exatamente uma vez agora. Verificando as junções (o texto original após cada inserção intacto) e, em seguida, a verificação completa de strings obsoletas:





All clear. Final integrity check, then the report:





Tudo verificado: as 7 linhas do INDEX estão intactas, `numeros.json` analisa, todos os 37 arquivos de correção aplicados, sem duplicações, sem strings desatualizados (o único `desconhecido U5` restante é um uso legítimo marcado como NÃO VERIFICADO na linha ITCMD do parecer).

## O que mudou nesta rodada de revisão (37 edições em 5 arquivos)

### `deliverable/parecer.md` — 21 mudanças
**Problema central corrigido — art. 977 (U11):** eu havia afirmado que a literatura dá suporte ao desenho Marina+Luana. A literalidade arquivada diz o contrário do que eu tratei como assentado: *"Faculta-se aos cônjuges contratar sociedade, **entre si ou com terceiros**, desde que não tenham casado no regime da comunhão universal…"* — leitura literal barra **qualquer** sociedade com cônjuge em comunhão universal, não só o casal juntos. A interpretação restritiva (a que salva o desenho) é a corrente, mas **não está na biblioteca**. Reescrito em 7 pontos (§1.2 com citação verbatim + R1×R2, resumo executivo, tabela de configurações com condição, §2 fallback, premissas), criado o item **U11** com poder de redesenhar o quadro — verificação técnico-registral na Junta, não fato do cliente.
**Exposição previdenciária (P2):** onde eu escrevi "base R$ 600.000/ano" sem fundamento, agora a conta correta: pró-labore zero → base ≈ **420.000/ano**, INSS patronal 20% × 420.000 = **84.000/ano** de exposição da sociedade; a retenção de 11% é ônus do segurado, não custo da PJ; base de autuação e multas marcadas [NV].
**IRRF (Lei 15.270):** 10% incide sobre o **total pago no mês** quando excede R$ 50.000 — não sobre a parcela excedente; "progressivo **até** R$ 1,2 mi"; renda agora por **CPF** (Marina ≈ 240.000 lucros; Felipe ≈ 60.000 pró-labore), não "por cônjuge 300.000".
**Teto ME/EPP:** valor inventado removido — "não consta da biblioteca [NV — U9]".
**Teste do CTN art. 37 (§4.2/P5):** alarmes agora com aritmética explícita — teste literal só rompe com estética < ~96.000/ano (96.000 ÷ 192.000 = 50,0%); alarme prudencial < ~192.000/ano.
**Fundamento de integralização:** trocado de art. 1.055 (que veda serviços, não exige integralização no ato) para art. 1.052, marcado [literalidade NV — o trecho arquivado não transcreve].
**Erros/texto:** `ouLuana`, `estrututra`, `compatização`, `cobriria`, `tribut-se`, `intervm` corrigidos; U5/U2 re-etiquetados.

### `deliverable/contrato_social_ajustado.md` — 4 mudanças
Bloco de desenho e Cl.1.3(i) agora **condicionam** a entrada de Marina ao lado de Luana à leitura restritiva do 977 + verificação na Junta antes de firmar (U11); Cl.8.4 corrigida a base do IRRF (total pago no mês); cabeçalho U1–U11.

### `deliverable/checklist_registro.md` — 4 mudanças
Item A com **verificação pré-assinatura da leitura da Junta (U11)** + fallback (Luana + terceiro não cônjuge / alteração de regime [NV]); item C com a aritmética dos dois alarmes; Anexo III (B) com citação a `library/lc123_vedacoes.md`; cabeçalho U1–U11.

### `deliverable/QUESTIONS.md` — 5 mudanças
Linha 2 (regime de bens) com a condição U11; **U9 desinventado** ("R$ 4,8 mi" não estava na biblioteca); bullet U11 novo; **nova seção D** — a única pergunta nova da rodada: se a Junta seguir a leitura literal, plano B preferido **(a)** Luana + terceiro não cônjuge ou **(b)** alterar regime de bens.

### `deliverable/STATUS.md` — 3 mudanças
Referências U1–U11 (×3), pendência U11 acrescentada, e **"8 arquivos" → 7 arquivos** (eu havia contado errado o INDEX).

### `deliverable/numeros.json` — 0 mudanças
Verificado contra o round do cliente (aluguel 8.000/mês → 96.000/ano, 8,0% de 1,2 mi; cessão 114.000; IRRF 0) — permanece correto e refletindo o desenho pretendido A.

Nota de processo: três pares de substituição foram aplicados em duplicidade por um bug de idempotência na minha ferramenta de edição (bloco anexado = sufixo do próprio texto de destino); detectei por contagem de ocorrências e removi as cópias — verifiquei que cada trecho inserido (bullet U11 no parecer e no QUESTIONS, bloco "Antes de firmar" no checklist) aparece exatamente uma vez e que o texto circundante original ficou intacto nos três pontos. Os entregáveis estão prontos para entrega: `STATUS.md` = **COMPLETE WITH OPEN ITEMS** (U1–U11, com U11 como a única pendência com poder de redesenhar o quadro).