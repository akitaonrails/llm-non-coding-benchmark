Good instruction. Let me do a systematic audit: re-run the full bookkeeping with the library calendar, verify every number in each deliverable against it, check authority coverage, and then re-read the files end-to-end.

Audit confirms every number. Now let me read the full files to apply the identified fixes.

All three files read. Before quoting DJe headers as evidence in §1 of the memoria, let me confirm the exact strings from the PDFs:

Confirmed. Now applying the fixes — first the memoria.md edits:

Now the §6 addendum — heading, risk wording (grounded in art. 224, caput), and the completed dobro column:

Now the §7 ressalvas — grammar fix and the act.')

I need to correct the Cinzas-date error and fix the grammar in §7:

- §7 item 3: "fica absorvido" → "são absorvidos"
- §7 item 4 and STATUS item aberto 2: replace the wrong "18/02/2027 Quarta-feira de Cinzas" claim with the correct statement that Ash Wednesday 2027 falls on 10/02/2027, is not listed in the library calendar, and 18/02/2027 is an ordinary business day

Now STATUS.md — the stray "!", the same doctrine wording aligned to art. 224, and the item-aberto Cinzas fix:

Now rewrite `prazos.json` with the exact contract schema (two top-level keys only) and corrected citation attribution:

Final validation pass — JSON schema check, leftover-error grep, and authority whitelist check:

One check failed — likely INDEX.md lists filenames without the `library/` prefix. Let me verify:

INDEX.md lists bare filenames while deliverables cite `library/<file>` paths — the citation is valid; my check just needs basename matching:

All authority checks pass. Final read-through of both edited deliverables to confirm coherence:

One typo remains in STATUS.md line 19 ("deslizaría" — Spanish accent; Portuguese conditional is "deslizaria"):

Review complete. Every number was re-audited against the library calendar with the exact same computation, JSON re-validated, and both deliverables re-read end-to-end. **Conclusions unchanged** — `prazo_em_dobro = false`; dates **16/12/2026** (contestação), **21/01/2027** (embargos), **04/02/2027** (apelação) all reconfirmed. Here is what I found and fixed:

**Correções de fato**
1. **`memoria.md` §7.4 / `STATUS.md` item aberto 2 — erro de data real**: eu escrevia "Quarta-feira de Cinzas de 18/02/2027". Errado: 18/02/2027 é quinta-feira, dia útil ordinário; a Cinzas de 2027 cai em **10/02/2027**, e o calendário da biblioteca só cataloga expediente parcial de Cinzas para 2026 (18/02/2026). Ambos os arquivos corrigidos, e o ponto foi resolvido de vez: pela biblioteca, 10/02/2027 é dia útil, e uma eventual regra análoga em 2027 (não verificável na biblioteca) afetaria só a coluna rejeitada.
2. **`memoria.md` §6 — lacuna de cálculo**: a ilustração dobra da apelação dizia "não calculada". Calculei: **01/03/2027** (30 dias úteis), com a ressalva de que deslizaria para 02/03/2027 se a regra de Cinzas de 2026 fosse repetida em 2027. A tabela da adenda agora fecha completa: 10/02/2027 (contestação-dobro), 28/01/2027 (ED-dobro), 01/03/2027 (apelação-dobro).

**Correções de autoridade**
3. **`memoria.md` §6 + `STATUS.md`**: removi as asserções doutrinárias sem amparo na biblioteca ("prazo não se perde por antecipação", "protocolo antes do vencimento nunca é intempestivo", "quem expectar..."). A assimetria de risco agora se apoia apenas em lógica aritmética ancorada no **art. 224, caput** [library/cpc_prazos.md] — a janela fecha no vencimento, logo a régua curta adotada está contida na régua longa. Também na adenda removi ("Connecticut", "affirmativa") e renomeei o título ("2ª passagem") da seção 6.
4. **`prazos.json` — citação mal alocada**: o `fundamento` creditava art. 231, VII a [library/cpc_prazos_recursais.md]; o dispositivo está em [library/cpc_prazos.md]. Reatribuído, e art. 219/224 ganharam a referência explícita ao arquivo correto. Ajuste estrutural: removi as chaves de nível superior `processo`/`cliente` para o JSON espelhar **exatamente** o esquema do contrato (`citacao` + `sentenca` apenas) — o contexto segue na memória.
5. **`memoria.md` §1 — evidência fortalecida**: "autos eletrônicos" agora cita o texto literal dos DJe: "**PROCESSO ELETRÔNICO (e-SAJ)**" e "Processo Digital nº 1044712-38.2026.8.26.0114" (reconfirmado nos PDFs antes de citar). "Diferença de 2 meses" → **56 dias corridos** (preciso).

**Itens menores**
6. `memoria.md` §3: "incluindo o dia 15" → "incluindo o 15º dia"; §4: ordem do fim de semana corrigida ("12/12 sáb; 13/12 dom"); §7.3: "fica/são absorvidos". `STATUS.md`: exclamação perdida em "14/12/2026!" e o hispanismo "deslizaría" → "deslizaria".

**Verificação final executada**: reauditoria em Python com o calendário integral da biblioteca (todas as 6 séries — simples e dobradas — reproduzidas identicamente), JSON valida e parseia com as chaves exatas do esquema, e os 4 arquivos citados (`cpc_prazos`, `cpc_prazos_recursais`, `lei11419_art4`, `calendario_forense_campinas`) conferem com [library/INDEX.md](file:///work/workspace/library/INDEX.md). Grep confirma que nenhum erro antigo sobrou.

Status segue **COMPLETE WITH OPEN ITEMS** — o único item aberto permanece o mesmo: se qualquer parte opuser embargos de declaração tempestivos, o prazo de apelação se interrompe e `apelacao_vencimento` terá de ser recalculado. Pode entregar.