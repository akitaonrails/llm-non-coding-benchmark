All source files read. Now let me verify the document-by-document data and arithmetic with Python before building the deliverables.

All source files and the closed library are read, and the per-document arithmetic is verified. Now I'll build the deliverables.

Final validation pass — citations against the library index, JSON self-consistency, and file placement:

文件 `deliverable/apuracao_teste.json` 包含不是我写入的内容，且 schema 不同 — 别名目录并非同一个目录，并且某处存在一份预先放置的草稿。我需要精确地检查两者的状态。

Tudo mudou desde a última leitura — a estrutura do XML, os valores de apuração e até o e-mail. Este é um instantâneo atualizado do cenário. Vou ler tudo novamente a partir do zero.

Restam dois acertos de precisão nas citações. Aplicando:

Agora consolido o arquivo de perguntas sob o nome do contrato (`PERGUNTAS.md`):

Validação final do JSON e varredura de consistência:

Engajamento concluído. Todos os entregáveis estão validados contra o snapshot atual dos documentos e a biblioteca fechada.

## Entregáveis (`deliverable/`)

| Arquivo | Conteúdo |
|---|---|
| `apuracao_teste.json` | Schema do contrato exato; 12 saídas + 5 entradas; totais conferem nota a nota |
| `orientacao.md` | Resposta ao gerente, refutando "nada a fazer em 2026" |
| `PERGUNTAS.md` | 4 itens abertos (não bloqueantes) + `QUESTIONS.md` como ponteiro |
| `STATUS.md` | **COMPLETE WITH OPEN ITEMS** |

## Números da apuração-teste (agosto/2026)

- **Débitos:** base R$ 480.000,00 (reconcilia exatamente com a base de PIS/COFINS da apuração normal) → CBS 0,9% = **4.320,00**; IBS 0,1% = **480,00**
- **Créditos:** só 2314/2316/2317 (regulares com destaque) = **1.458,00 CBS / 162,00 IBS**. Sem crédito em 2313 (sem destaque, LC 214 art. 346) e 2315 (fornecedor do Simples, art. 347)
- **Saldo-teste:** 2.862,00 CBS + 318,00 IBS = **R$ 3.180,00**
- **Recolhimento devido: R$ 0,00** — dispensa do ADCT art. 125, §4º, **condicionada** às obrigações acessórias

## Resposta ao gerente

Ele está **meio certo**: nada a *pagar* em 2026, mas há o que *fazer* — e o descumprimento **custa a dispensa**. Há **4 notas irregulares** (2308, 2310, 2312 emitidas após 03/08 sem o grupo IBSCBS; 2309 com alíquotas invertidas pIBSUF/pCBS). Perda da dispensa → R$ 3.180,00 devidos, ainda que compensáveis com PIS/COFINS (17.520,00 disponíveis). As premissas dele sobre "não destacar para Simples/MEI" e "crédito de fornecedor do Simples" estão ambas erradas — §§4–5 da orientação explicam com base nos arts. 346/347 da LC 214.

## Ajustes finais desta rodada

- Removida a referência ao "ADCT art. 124" da orientação (a biblioteca só traz o art. 125)
- `PERGUNTAS.md` criado como arquivo canônico (nome exigido pelo contrato); QUESTIONS.md virou ponteiro
- Pente-fino nas perguntas: a antiga "Q2" (CST/cClassTrib) foi retirada — confirmei nos XMLs que 2306/2307/2309/2311 trazem CST 000 / cClassTrib 000001; a destinatária da 2312 corrigida para Brisa Materiais; a menção a CT-e/NFS-e conferida no comunicado do CGIBS

Itens abertos: as 2 notas rejeitadas do e-mail (ausentes da pasta, todas as 12 estão cStat 100), reemissão da 2312, CT-e/NFS-e de serviços fora da pasta, e recuperação do crédito da 2313 — o mecanismo de correção de NF-e autorizada não existe na biblioteca e por isso não foi indicado como regra.