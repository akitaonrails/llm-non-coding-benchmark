I'll re-verify everything against the closed library and re-check the arithmetic before delivery. Let me re-read the full deliverable set and the library files.

The cached extracts are gone. Let me re-extract the source documents to verify the data room and minuta claims directly.

Now let me locate the remaining edit targets precisely.

One edit missed due to text mismatch — retrying with the exact fragment.

All fixes applied. Running final validation sweep: JSON validity, citation whitelist, leftover phrasings, and arithmetic.

Auditoria concluída. Reabri os PDFs originais da data room e da minuta (os textos em cache haviam se perdido), conferi palavra por palavra todas as asserções factuais, cada citação contra o `library/INDEX.md`, e refiz toda a aritmética. Encontrei 4 problemas e apliquei 5 correções:

## O que foi corrigido

1. **`redline.md` §10.2 — autoridade inexistente removida.** A redação proposta terminava com *"Subrogação do Comprador contra seguradores/órgãos quando cabível"*. Seguro não aparece em lugar nenhum — nem na minuta, nem na data room, nem na biblioteca. Frase removida (a sub-rogação do Comprador na defesa do crédito, que é o que os fatos sustentam, já estava na frase anterior).

2. **`resposta_advogado_comprador.md` §3 e §3.1 — inferência apresentada como fato.** *"o Comprador se indeniza pelo que já sabia e precificou"* e *"data room examinada (e precificada) pelo Comprador"* afirmam que o comprador **precificou** os riscos — isso não é verificável em lugar nenhum. Suavizado para o que é sustentado pelos fatos: o que ele *"conhecia do data room que tem em mãos"* / *"data room entregue ao Comprador"*. A argumentação não perde força: a falsidade de 5.7/5.9 decorre do próprio texto da data room. (O termo *"precificável"*, que só diz que o risco *pode* ser precificado, foi mantido — é correto.)

3. **`nota_socios.md` rodada 3, item 4 — fato não confirmado tratado como certo.** *"a cláusula de preferência (30 dias) ainda não foi disparada"* agora está qualificada: *"se houver sócio que não vai vender, o que ainda não confirmamos (QUESTIONS.md)"*, alinhado à premissa aberta da pergunta Q2. A anuência da Horizonte Azul ("nem foi pedida") ficou como fato — essa vem da resposta dos próprios sócios.

4. **`redline.md` cabeçalho — parâmetros numéricos desmarcados.** O cabeçalho prometia marcar sugestões sem lastro na biblioteca, mas propostas como *"liberação 50% no 12º mês / saldo no 24º"*, *"custeio 50/50 do auditor"* e *"régua de 10%"* não estavam marcadas. Acrescentada uma linha única: esses números são **parâmetros de negociação** — a biblioteca dá a direção da proteção, não o número.

## O que foi conferido e está correto

- **Fontes conferidas verbatim** contra os PDFs: Cláusula 19 da Horizonte Azul (rescisão imediata + 20% do saldo), cessão total vedada em Sorocaba §1.2, CND positiva de R$ 310 mil sem parcelamento §3.1, ISS "por fora"/sublimite §3.2, 11 PJ "perfil Solaris" §2.2, 3 reclamatórias R$ 1,4 mi vs provisão R$ 380 mil §2.3, preferência de 30 dias §4.1, R$ 4,2 mi / R$ 390 mi §4.2, e toda a minuta (2.3, 3.2, 5.7, 5.9, 8.4(a)–(d), 9.1, 10.2 e a carta do advogado).
- **Citações:** as 7 referências `library/*.md` usadas batem exatamente com o whitelist do INDEX — nada fora da biblioteca é citado como autoridade.
- **Aritmética:** 1.500.000 ÷ 0,35 = 4.285.714,29 → EBITDA de 5.385.714,29 > faturamento de 4,2 mi; franquia 310 − 150 = 160 mil; gap trabalhista 1,4 mi − 0,38 mi = 1.020.000; escrow 20% > teto 15%; preferência 30/45 = 2/3 do prazo. Tudo confere.
- **`achados.json`:** 19 achados, schema e enum de `efeito` válidos.

STATUS continua **COMPLETE WITH OPEN ITEMS** — as correções não criaram nem eliminaram itens abertos (a premissa da preferência já era a Q2). Os entregáveis estão prontos para entrega.