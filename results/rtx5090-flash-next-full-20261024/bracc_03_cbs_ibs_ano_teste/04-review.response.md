Good discipline before delivery. I'll re-verify everything bottom-up: (1) every citation against the actual library text, (2) every per-document number against the XMLs, (3) internal consistency across the four deliverables.

Library text confirmed. Now I'll re-derive every document-level fact straight from the XMLs:

Corrigindo o erro de sintaxe no script de extração:

All document facts confirmed against the XMLs so far. Let me verify supplier names (xNome) and re-run the full arithmetic, then read the JSON and orientacao in full for the authority review:

JSON is clean and validated. Now the markdown softenings — let me get the exact current text of the pending sections:

Batch 2 (rollback inference, homologação inference in QUESTIONS, STATUS item 2):

Batch 3 (FAQ point 3, reissue inference, STATUS header):

Final batch (rejection attribution in "O que muda", STATUS round-3 review note):

All edits applied. Final verification sweep — residual overclaims, duplicates, English remnants, and JSON integrity:

Revisão final concluída e verificada. O que foi corrigido nesta rodada de revisão, e nada mais mudou:

## Correções aplicadas

**1. JSON (defeito real — texto duplicado)**
- Os `motivo` das NF-e **2308, 2310 e 2312** e o campo `condicao_dispensa` continham blocos inteiros **repetidos duas vezes** (efeito colateral da reaplicação do patch da rodada 2). Reescritos com cópia única via script de substituição completa, com asserções automáticas de deduplicação.
- Referência cruzada corrigida: `"(ver QUESTOES)"` → `"(ver QUESTIONS.md)"` (o arquivo chama-se QUESTIONS.md).

**2. Autoridade sem suporte → rotulada como inferência**
- *"Em homologação a validação do grupo IBSCBS não é bloqueante"* aparecia como fato em `orientacao.md` (nota de conciliação e FAQ item 3) e em `QUESTIONS.md`. A biblioteca **não descreve** o ambiente de homologação — agora redigido como inferência compatível com os arquivos, com a ressalva explícita de que o cStat 100 dos arquivos **não prova** autorização em produção.
- *"Rebaixar o emissor gera XML sem o grupo IBSCBS"* aparecia como fato em 3 lugares (`orientacao.md`, `QUESTIONS.md`, JSON). Agora rotulado como **inferência** (a explicação compatível com a própria mensagem de rejeição), inclusive no `condicao_dispensa` do JSON e no open item 2 do STATUS.

**3. Atribuição da mensagem de rejeição corrigida**
- O texto literal *"Rejeição: Grupo IBSCBS não informado…"* vem do **relato do cliente**; o comunicado do CGIBS só promete "rejeição específica (cStat 999/…)". Todas as ocorrências de "é exatamente a rejeição anunciada/prevista" (orientacao, QUESTIONS, STATUS, motivos do JSON) passaram a **"compatível com a rejeição anunciada no comunicado"**, com a origem do texto literal explicitada.
- Em "O que muda a partir de 03/08": a **rejeição** agora é atribuída ao **comunicado do CGIBS**, e o leiaute/alíquotas à **NT 2025.002** (antes os dois apareciam citados juntos para a rejeição).

**4. STATUS.md**
- Cabeçalho atualizado (rodada 3 = revisão interna pré-entrega) e parágrafo novo registrando exatamente estas correções, para auditoria.

## O que foi re-conferido e **não** mudou
- **Aritmética, documento a documento e nos totais**: saídas R$ 480.000,00 → débitos CBS 4.320,00 / IBS 480,00; créditos 1.458,00 / 162,00 (só 2314/2316/2317); saldos 2.862,00 / 318,00; recolhimento R$ 0,00 — tudo recalculado por asserções no script e batendo com os XMLs e com a base PIS/COFINS da apuração normal.
- **Classificações** (2301–2305, 2306, 2307, 2311 regulares; 2308–2310, 2312 irregulares), créditos zero (2313 sem destaque; 2315 Simples, art. 347) e a condição de dispensa: inalterados — cada citação foi conferida contra os textos integrais da biblioteca (ADCT art. 125 §§1º/4º, LC 214 arts. 343/346/347, NT 2025.002, comunicado CGIBS).
- **Esquema do JSON** confere com o `CONTRACT.md` (chaves exatas de `saidas`, `entradas`, `totais`, `recolhimento_devido`, `condicao_dispensa`).
- Varredura final: sem duplicações residuais, sem resquícios de inglês, sem alegações factuais remanescentes sem suporte na biblioteca.

**Status do engajamento: COMPLETE WITH OPEN ITEMS** — os 6 desconhecidos sinalizados permanecem abertos (quais notas exatas foram rejeitadas, destino das reemissões do emissor rebaixado, instrumento de regularização, escopo da perda da dispensa, completude da carteira, origem do erro de alíquotas da 2309), todos registrados em `STATUS.md` e `QUESTIONS.md` sem repetir perguntas já encerradas. Entrega pronta em `workspace/deliverable/`.