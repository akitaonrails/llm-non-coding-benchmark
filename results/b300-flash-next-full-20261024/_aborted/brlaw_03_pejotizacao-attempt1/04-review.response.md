

I'll do a systematic verification pass: (1) re-check every cited authority against the library, (2) re-verify all arithmetic from source data, (3) check cross-file consistency and schema compliance.






Both remaining library files verified. Now I'll re-read all deliverables in full and re-verify source data in parallel:






Now the remaining deliverables and source data:







Deliverables re-read. Now re-verify the arithmetic against the raw source data:





All source documents match the citations. Now the last unverified library file, the contract PDF, and a full arithmetic re-check:







All arithmetic reconciles exactly (744.956, 496.637, 620.797, 674.108, 449.405, 889.928, 1.041.417, −70.848, +11.928, +3.427, NFs 84/1.512.000, HE 135h). The contract PDF and Tema 725 library file confirm the clause citations and the verbatim thesis text. The verification pass surfaced **six genuine issues**:

1. **CPC 25 is not in the library** — but it's mandated by the contract's own schema (`classificacao_cpc25`); the "no source outside the library was cited" claims are imprecise. Must be labeled.
2. **§10 claimed INSS has "prazos decadenciais próprios"** — not supported by the library (library only supports: company debt, exigible by RFB).
3. **Aviso 51 days uses "7 anos completos"**, but 01/10/2019–30/09/2026 is 1 day short of 7 full years; library formula says "3 por ano completo". Needs disclosure (strict 48 days = −R$ 1.800; 51 only via projeção/U2).
4. **§10 quotation dropped "no caso concreto"** from the library's verbatim thesis text; §4's director paraphrase was inside quote marks; clause 4 quote omitted the home office variant (which actually strengthens the argument).
5. **INSS teto not applied** (library formula applied flat 28%) — real direction of adjustment (reduces INSS) not disclosed prominently.
6. **Férias labeled "proporcionais"** when the arithmetic is full accrual (the "férias" he took as PJ were unpaid) — minor precision fix; §3's "essas falas existem (Slack...)" overstated which statements are archived where.

Applying fixes to `parecer.md`:











Now the JSON quote fix and a fresh read of STATUS.md for precise edits:






Let me read the actual §6.4–§7 text:





Applying all remaining `parecer.md` edits:







Now the §10 fixes and footer:







One residual quote-precision fix in §4 (director's email says "assinou contrato, emitiu nota", not "e emitiu NF"):





Now the STATUS.md updates:








JSON validates, soma == 744.956, all schema keys present. Final consistency sweep on the new insertions:





Revisão concluída. Reauditadas as **sete** fontes da biblioteca, os cinco documentos-fonte, todo o parecer, o JSON e o STATUS, e recalculei todos os valores de forma independente a partir dos CSVs/contratos. Os totais estão todos corretos (`744.956 = 87.750+117.000+100.620+40.248+30.600+352.170+16.568`; 12k→496.637; 15k→620.797; renúncia→674.108/449.405; HE 135 h; NFs 84 → 1.512.000; deltas U1 −70.848, U2 +11.928, FGTS sobre aviso +3.427; honorários 37.248–111.743 / 24.832–74.496 — todos conferem). Encontrei **6 problemas reais**; correções:

**O que mudou (`parecer.md` → v2.1):**

1. **Autoridade não suportada removida — §10.2:** a alegação de que o INSS possui "prazos decadenciais próprios" não consta da biblioteca. Reescrito estritamente ao que a biblioteca suporta: "dívida da empresa exigível pela RFB … cobrada na esfera fiscal/administrativa — que não é o objeto da suspensão do ARE 1.532.603".
2. **Exceção CPC 25 declarada —** CPC 25 **não** integra a biblioteca (o schema do contrato o exige via `classificacao_cpc25`). As antigas alegações de rodapé/cabeçalho de que "Nenhuma fonte fora de `library/INDEX.md` foi citada" eram imprecisas. Adicionada uma *nota de referencial* no §7 (critérios marcados como "redação não verificada"), qualificadas como citações "**jurídicas**" no cabeçalho e no rodapé, e uma referência cruzada em §10.2.
3. **Aviso-prévio 51 dias fundamentado e divergência divulgada — §5:** 01/10/2019–30/09/2026 fica a 1 dia de 7 anos completos, e a fórmula da biblioteca exige anos *completos*. §5 agora demonstra a base conservadora (projeção do aviso/U2 → 7 anos completos → 51 dias) **e** divulga a contagem estrita de 48 dias = R$ 28.800 (**−R$ 1.800**); linha da tabela em §6.1 passa a fazer referência cruzada ao §5. Total mantido em 51 dias.
4. **Teto do INSS divulgado — §6.1/§6.4:** a aplicação de 28% sobre 1.257.750 não aplica o limite individual (a fórmula da biblioteca não o prevê e as séries de valores do limite não estão na biblioteca). Novo destaque no §6.4 informando a **direção** do ajuste (reduziria os 352.170) e que o valor adotado é conservador; a linha do INSS na tabela agora aponta para essa nota.
5. **Fidelidade de citações:** §10 restitui "**no caso concreto**" à tese do Tema 725 *ipsis litteris*; §4 parafraseia corretamente o e-mail do diretor ("ele é PJ, assinou contrato, emitiu nota por 7 anos") em vez de aspas inexatas; a citação da cláusula 4ª é completada com "ou em home office **autorizado pelo gestor**" (o que, de fato, *reforça* a subordinação); o item "O noticiário confunde" foi reancorado na própria alegação do diretor ("está em todo jornal") em vez de afirmar fatos sobre a imprensa.
6. **Precisão de rótulos/fontes:** férias agora rotuladas como **cadente de 58.5 meses** ("as 'férias' gozadas como PJ não eram remuneradas") — mesma quantia de 117.000, rótulo correto; o item probatório em §3 distingue fatos **nos sistemas da empresa** (Slack/e-mails de §2) da admissão da gestora recebida **via chat do cliente**.

**`parecer.json`:** citação da cláusula 4ª completada com home office. Nenhuma alteração numérica — JSON validado (parse ok, `soma == total == 744956`, todas as chaves do schema presentes, incluindo `classificacao_cpc25`).

**`STATUS.md`:** atualizado para v2.1 com um parágrafo "revisão pré-entrega" listando as correções, item de limite do INSS adicionado aos open items e rodapé com a exceção CPC 25. **`QUESTIONS.md`/`PERGUNTAS.md`:** verificadas — todas as citações/números conferem, sem necessidade de alterações.

Nenhuma conclusão ou total alterado: probabilidade **alta (85–90%)**, exposição **R$ 744.956**, grade **449,4 mil–1,04 milhão**, provisão **provável**, acordo **450–600 mil**. Todos os pontos de referência pendentes foram resolvidos (as referências ao §7 e §6.4 agora resolvem).