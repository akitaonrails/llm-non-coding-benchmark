Farei a revisão em camadas: (1) regras do contrato e lista de citas permitidas; (2) leitura integral de cada entregável; (3) verificação das fontes citadas (library, data room, minuta); (4) reconciliação de números entre arquivos. Começo pelo inventário e pelas fontes normativas:

A pasta `/tmp/opencode/` está vazia — os extratos do data room e da minuta precisarão ser regerados dos PDFs originais para verificação. Primeiro, a lista de autoridade permitida e os arquivos da library, para conferir cada citação dos entregáveis:

Agora, os entregáveis e o e-mail dos sócios (fonte primária das respostas do cliente):

Agora QUESTIONS/PERGUNTAS e a verificação dos documentos-fonte (PDFs):

Continuando a revisão: preciso dos textos completos dos entregáveis (as leituras anteriores vieram truncadas no registro) e das duas fontes em PDF. Extraio os PDFs para `/tmp/opencode/` e relê os arquivos na íntegra:

`achados.json` lido por inteiro — 14 achados, JSON bem formado. O comando de extração falhou por caminho errado; refaço e sigo com as leituras completas restantes:

Arquivos-fonte extraídos. Agora leio as duas fontes e os entregáveis que faltam na íntegra, para conferir cada fato e citação:

Fontes conferidas: cada cláusula e seção citada nos entregáveis bate com os dois PDFs (%%1.1/1.2/1.3, 2.1–2.3, 3.1–3.3, 4.1/4.2; minuta 2.3, 3.2, 5.7/5.9, 8.1/8.4(a)–(d), 9.1, 10.2) ✅. Agora os três entregáveis restantes na íntegra:

Todos os entregáveis foram relidos na íntegra e confrontados com as duas fontes. A verificação de fatos, citações e aritmética fecha sem divergências (os números 1.302.000, 504.000, 1.020.000, 4.285.714/5.385.714, limiares CADE e o exemplo de franquia conferem). Sobram cinco problemas de texto/coerência a corrigir:

1. **Garble na resposta ao comprador (buy-facing)** — "(...e das 3.2/CADE **já com o qual exposto**);" frase quebrada.
2. **Ponteiro vencido na nota dos sócios** — intro manda "ver a seção final" para CADE, mas a explicação do CADE está na tabela do meio e na seção "Podemos só assinar?".
3. **Citação imprecisa do 5.7 na nota** — texto entre aspas não corresponde ao da minuta ("não existe risco de vínculo de emprego" vs. minuta "inexistindo risco de reconhecimento de vínculo empregatício").
4. **Dupla contagem potencial no 8.4(b) do redline** — itens (i) e (iii) fixam o mesmo teto de R$ 310.000 como se fossem matérias independentes (somando 620 mil se lidos separadamente); o referencial correto é teto único para a matéria fiscal e seus desdobramentos.
5. **PERGUNTAS.md desatualizado** — título "8 temas **pendentes** e referência à seção "Respostas …no fim do arquivo", quando 7 já foi respondida, 2 foi parcialmente respondida, e a seção de respostas em QUESTIONS.md chama-se "Respostas recebidas".

Antes de editar, leio o restante do CONTRACT.md, que estava truncado:

Contrato confirmado. Aplicando as correções:

Mais um ponteiro desatualizado no PERGUNTAS.md (a seção de respostas do QUESTIONS.md chama-se "Respostas recebidas" e já existe, não fica "no fim do arquivo" como lugar a preencher):

Correções aplicadas. Passo final de validação — JSON, palavras-garble/vestígios, e vazamento de fatos internos no arquivo voltado ao comprador:

Verificação final do estado das linhas editadas:

Revisão concluída. Todos os pontos verificados fecham; encontrei e corrigi seis problemas de texto/coerência (nenhum erro de fundo, de citação ou de conta).

## O que foi conferido

- **Fontes, linha a linha:** reextraí os dois PDFs (`pdftotext -layout`) e conferi verbatim cada seção do data room citada (§1.1–1.3, 2.1–2.3, 3.1–3.3, 4.1/4.2) e cada cláusula da minuta (2.3, 3.2, 5.7, 5.9, 8.1, 8.4(a)–(d), 9.1, 10.2 e a carta do comprador). Nenhuma citação divergente.
- **Aritmética, recalculada:** 31% × 4.200.000 = 1.302.000; 12% × 4.200.000 = 504.000; 1.400.000 − 380.000 = 1.020.000; 1.500.000 ÷ 0,35 = 4.285.714 (+1.100.000 → 5.385.714 de referência); CADE: 390 mi < 750 mi e 4,2 mi < 75 mi; exemplo de franquia (tipping R$ 200.000 vs. dedutível R$ 50.000) — tudo reconcilia.
- **Autoridade:** todas as invocações apontam para arquivos reais de `library/INDEX.md` e o atribuído a cada arquivo corresponde ao seu conteúdo; o que não tem base segue rotulado "não verificado".
- **Vazamento:** `resposta_advogado_comprador.md` não contém nenhum fato interno (diretor amigo, jurídico "duro", venda não comunicada) — grep dedicado: zero ocorrências.
- **Schema:** `achados.json` válido (14 achados; efeitos restritos a anuencia/preco/indenizacao/prazo/nenhum).

## O que mudou (6 correções)

| # | Arquivo | Correção |
|---|---|---|
| 1 | `resposta_advogado_comprador.md` (L16) | Frase travada "Guardando as datas — anuência pleiteada…" → "Com o pedido de anuência protocolado imediatamente após a assinatura, nada disso ameaça o fechamento em 45 dias." |
| 2 | `resposta_advogado_comprador.md` (L77) | Garble "revisão do Anexo 3.2 e das 3.2/CADE já com o qual exposto" → "revisão do Anexo 3.2 e da condição de CADE, conforme o exposto acima" (carta voltada ao comprador não pode ter frase quebrada) |
| 3 | `nota_socios.md` (intro) | Ponteiro vencido "veja a seção final" → posição correta do CADE: linha na tabela + seção "Podemos só assinar?" |
| 4 | `nota_socios.md` (ponto 1) | Citação do 5.7 operava parafraseada como se fosse texto da minuta → agora reproduz a redação real: "inexiste risco de reconhecimento de vínculo empregatício" |
| 5 | `redline.md` (8.4(b)) | Itens (i) e (iii) fixavam o mesmo teto de R$ 310.000 como capas independentes (leitura possível: R$ 620.000 somados) → unificado: **um** teto conjunto de R$ 310.000 + encargos para a matéria fiscal federal **e** seus desdobramentos no contrato público (retenções/sanções da CND positiva); (ii) CAP_PJ segue separado. Nenhum número novo — só eliminação da dupla contagem aparente |
| 6 | `PERGUNTAS.md` | "Resumo dos 8 temas **pendentes**" → "Resumo dos 8 temas" + blocoquote de status (pergunta 7 respondida, 2 parcialmente, demais sem informação adicional); ponteiro corrigido para a seção "Respostas recebidas" (já iniciada) do `QUESTIONS.md` |

Validação pós-edição: JSON revalidado; grep para todos os fragmentos corrigidos/garbles → zero resíduos; as seis regiões editadas conferidas no texto final.

## Situação final

`STATUS.md` permanece **`COMPLETE WITH OPEN ITEMS`** — posição de fundo completa em todos os entregáveis; seguem em aberto apenas os dados que o cliente não tem: **P**, **S_HA**, **CAP_PJ** (salários/tenura dos 11 PJs), EBITDA histórico 2023–2025, composição das quotas, território além de Sorocaba e confirmação de outras cláusulas de mudança de controle (o data room §1.3 é fonte única). Os símbolos ficam com as fórmulas expostas, e nada foi forçado a fechar.