

Vou fazer a revisão completa antes da entrega: biblioteca (o que pode ser citado), contratos, entregáveis, e a aritmética contra os XMLs.







Wording in the library confirmed. Now let me re-read the full current `orientacao.md` and `STATUS.md` to apply precise edits:






All asserts passed, and the JSON has been regenerated in strict schema. Let me quickly verify the contents:





All checks passed. Now applying the review fixes to `orientacao.md`:






`orientacao.md` fixed. Now `STATUS.md` — let me re-read it in full:





Now a final verification pass — contract schema line, email asks, and a full read of the revised memo:






The schema has been verified against line 8 of `CONTRACT.md` (already asserted in the generator), and the memo is also well written. Final check — `PERGUNTAS.md` and the regenerated JSON samples:






One consistency fix in `PERGUNTAS.md` — lines 18–19 still state the protocol premise as flat fact:





All fixes are in. Final sweep for lingering issues:





Revisão pré-entrega concluída. Todos os achados foram corrigidos e os números foram re-verificados linha a linha (não mudaram). Resumo das mudanças:

## `apuracao_teste.json` + gerador (`tools/gerar_apuracao_teste.py`)
- **Schema exato do CONTRACT.md** — o JSON anterior tinha chaves extras fora do contrato. Reescrito para emitir exatamente `saidas[{numero,data,valor,cbs,ibs,situacao,motivo}]`, `entradas[{numero,valor,credito_cbs,credito_ibs,motivo}]`, `totais` com os 6 campos, `recolhimento_devido`, `condicao_dispensa`. Chaves de acesso, grupo IBSCBS observado e memória de cálculo migraram para dentro de `motivo`/`condicao_dispensa` (identificação da empresa e período num preâmbulo do `condicao_dispensa`, já que a raiz não admite outras chaves).
- **Autoválidas no gerador**: asserções de schema (chaves exatas por linha e na raiz), de aritmética por linha (débito = alíquota × base), da base R$ 480.000,00 (confere PIS/COFINS) e dos totais esperados — todas passam.
- **Citações corrigidas**: removida a menção a PGDAS-D (fora da biblioteca) na nota 2315; 2314/2316/2317 citam apenas o art. 346; 2315 cita o art. 347 na redação exata ("limitado ao valor efetivamente recolhido pelo optante… em 2026, sem destaque, não há crédito") + 346.
- Números inalterados e reconferidos: CBS débito 4.320,00 / crédito 1.458,00 / saldo 2.862,00; IBS 480,00 / 162,00 / 318,00; recolhimento R$ 0,00; irregulares 2308/2309/2310/2312; creditadas 2314/2316/2317.

## `orientacao.md`
- **§3 (objeção "a SEFAZ autorizou")**: reestruturado — primeiro o que a biblioteca diz (emissão proibida desde 03/08; nada convalida a omissão via autorização; a perda da dispensa se liga ao cumprimento, não ao protocolo); a premissa "protocolo cStat 100 valida o leiaute transmitido" agora está **rotulada como premissa de leitura fora da biblioteca**, com nota de que a conclusão não depende dela.
- **§3(c) e §6**: a ressalva de penalidades foi restringida à redação do Comunicado ("pelo **não preenchimento**, caráter educativo"); sinalizado que a biblioteca **não** afirma a mesma ressalva para preenchimento **errado** (inversão da 2309).
- **§4**: removida a extrapolação "cliente Simples não se credita (art. 347)" — agora usa a redação do art. 347 ("não sujeito a destaque/apuração em 2026"), com o dever de destaque do emitente no art. 346.
- **§5**: item Ponto Fixo alinhado ao art. 347 literal (caiu a inferência "não recolhe"); item 2313 ganhando o contexto de emissão pré-03/08 (documento válido, porém sem destaque → crédito zero, art. 346).
- **§7 item 3**: subtotal de R$ 197.000,00 renomeado para "grupo IBSCBS preenchido no documento" (antes dizia "destaque correto", mas inclui a 2309 invertida), com a soma 197.000 + 283.000 = 480.000 explícita.

## `STATUS.md`
- Descrição de `orientacao.md` reescrita: a versão anterior citava seções inexistentes ("prazos 2026–2032", "o que dizer ao sócio", mito como "nota rejeitada = não tributada"). Agora espelha as seções reais (1–7), casadas com as 4 perguntas do e-mail do Paulo.
- Item em aberto 2: trocado "carta de correção/estorno" (procedimento fora da biblioteca) por "procedimento de saneamento não definido na biblioteca — definir após consulta ao Fisco".
- Linha de atualização e descrição do JSON registram a revisão de schema/premissas; a objeção do protocolo passou a citar a premissa rotulada.

## `PERGUNTAS.md`
- Registro da segunda rodada realinhado: a afirmação sobre o protocolo deixar de ser fato e virar premissa rotulada, coerente com o §3 do memorando.

Status permanece **COMPLETE WITH OPEN ITEMS** — os 4 ignorados declarados continuam em aberto e nenhum afeta os números de teste.