I'll do a full verification pass: re-read every library file and audit each citation and number in the deliverables against them.

The library text is now refreshed. Now I'll audit every high-risk claim in the deliverables against these texts:

Continuing the audit — I need to see the exact wording at each flagged location in parecer, checklist, and contrato.

The minuta confirms every clause reference in the table (3ª, 5ª, 9ª, 10ª all match). Audit complete — 8 fixes to apply:

Applying the 4 remaining fixes (checklist ×2, contrato, STATUS):

All fixes applied. Running final QA sweep — JSON schema, citation audit against INDEX, and arithmetic reconciliation:

Syntax bug in my QA script — fixing and re-running:

Everything reconciles: cliff R$ 50.001 → 10% × 50.001 = R$ 5.000,10 ✓; INSS 11% × 10.000 = 1.100 ✓; S1 35.000÷2 = 17.500 sócio, ×12 = 210.000 < 600.000 ✓; JSON pro-labore Marina 0 / Felipe 10.000 / Luana 8.000 consistent across all documents. Final table integrity check on the edited parecer row:

Revisão de pré-entrega concluída. Re-li os 7 arquivos da biblioteca, todas as citações, referências cruzadas e toda a aritmética dos 7 entregáveis. Encontrei **9 problemas** — todos corrigidos abaixo — e o resto confere sem alterações.

## O que mudou nesta revisão

**`parecer.md` (5 correções)**
1. **Resumo executivo** — dizia que as quotas "preferenciais" "precisam de correção técnica" como se houvesse vedação. A biblioteca (IN DREI 81/2020, aplicação supletiva da LSA) as **admite**; a supressão é escolha de redação. Reescrito.
2. **§2.2 (ITBI)** — faltava o ponteiro de superação que os demais itens do turno 1 têm, e a nota "[aluguel ainda não informado]" estava desatualizada (o aluguel de R$ 8.000/mês foi confirmado no turno 2). Adicionada nota "Atualizado no turno 2 (A.2/A.7)" + flag reescrita.
3. **Item 5, linha da Cláusula 10ª** — removida afirmação sem suporte na biblioteca ("a DREI/registro **pode exigir justificar**" a prioridade de lucro); corrigido erro de digitação ("proporciedade"); corrigida referência cruzada obsoleta ("cláusula 15 do ajustado" → **Cláusula 9ª do ajustado v2**).
4. **A.5, item 9 (Tema 796)** — "nunca 900 mil (ganho de 480 mil + Tema 796)" abreviava mal: pelo texto literal da biblioteca, a imunidade só não alcança o valor que **exceder o capital a ser integralizado**. Agora: ganho de R$ 480 mil (Lei 9.249) + responsabilidade solidária (CC 1.055 §1º) são os motivos; o Tema 796 só alcançaria parcela excedente não integralizada.

**`checklist_registro.md` (2)**
5. **Item 1.3** — "ambos impeditivos/irregulares" era impreciso: 6810-2/02 é **impeditiva** (LC 123 art. 17 XV), mas 8630-5/04 é **permitida** na biblioteca (Anexo III/V, Fator R) — o que falta é o **RT inscrito no CRO**, inexistente no quadro.
6. **Item ❌ integralizar a 900 mil** — mesma abreviação do Tema 796 corrigida (ganho 480 mil + responsabilidade solidária; excedente fora do capital é que paga ITBI).

**`contrato_social_ajustado.md` (1)**
7. **Anexo Variante B** — "excedente fora da imunidade (Tema 796)" soava automático; agora explicita: integralizando os 900 mil **por dentro do capital** não haveria excedente alcançado — mas ganho de capital e superavaliação permanecem como motivo da vedação; se a diferença ficar em reserva, aí sim incide ITBI.

**`STATUS.md` (1)**
8. **Linha 8** — "imune **pelo** Tema 796" → imune pela **CF art. 156 §2º I**; o Tema 796 não morda porque as quotas cobrem todo o valor integralizado (sem excedente).

## O que foi verificado e **não** precisou mudar
- **`numeros.json`** — JSON válido, schema exatamente o do CONTRACT.md (sem chaves extras), valores coerentes com os demais documentos.
- **Todas as citações** `library/…` dos entregáveis estão em `library/INDEX.md`; nada fora da biblioteca circula sem o flag **[NÃO VERIFICADO NA BIBLIOTECA]**; premissas com **[PREMISSA]**.
- **Aritmética conferida e batendo:** 96.000 ÷ 1.296.000 = 7,41%; aluguel 60% = 8.000 ÷ 0,4 × 0,6 = 12.000 [PREMISSA]; turno 1: 570.000 ÷ 0,8 = 712.500 (21,05/58,95/20%) e 1.050.000 ÷ 0,8 = 1.312.500 (Luana 262.500 = 20%); Variante B: 720.000, 20,83%/79,17%; ganho 900k−420k = 480k; cliff 50.001 → 5.000,10; INSS 11% × 10.000 = 1.100; S1 35.000 → 17.500/sócio, 210.000/ano < 600.000.
- **Referências cruzadas:** Cláusulas 3ª/5ª/9ª/10ª da minuta conferem com o diagnóstico; as cláusulas 3ª/6ª/9ª do ajustado v2 batem com o que o parecer e o checklist citam (exceto a "cláusula 15", corrigida acima).
- Nenhuma citação a artigos do CC que a biblioteca não transcreve (1.052/1.053/997/1.010 não aparecem); `simples_possivel: false` permanece deliberado (documenta o plano conforme confirmado; a Estrutura A o restaura, explicado em A.7).

Os 7 entregáveis em `/work/deliverable/` estão prontos para entrega.