Iniciando a revisão pré-entrega. Primeiro, reconferir cada fundamento citável do pacote contra a biblioteca e os arquivos de origem:

Caminho com um erro de digitação — reemitindo com os caminhos corretos em `/work/workspace`, além do restante do excerto da e leitura de confirmação dos itens das perguntas 6/7:

Estrutura e biblioteca confirmadas: arts. 64/172, par condicio e convolação **estão** no excerto da lei11101 (linha 13). Agora verificando o MIX de citabilidade do INDEX, referência cruzada §3.2 e lendo de volta os entregáveis principais da Sessão 3 + resposta_diretor:

All § cross-references check out (§1, §3, §6, §6.4, §3.2 all exist). Two library files remain to verify their contents against claims, plus the minuta for the "não fixa valor por parcela" claim:

Todas as verificações de biblioteca e cross-refs fecharam. Agora preciso das strings exatas das linhas a editar (STATUS.md linha 26, QUESTIONS.md linha 41, passivo_fiscal linha 20, JSON linhas 84/97, resposta_diretor linha 61) e de dois checks finais de biblioteca (CTN 191-A; arts. 6º/57/58/68 no excerto):

Todas as strings exatas confirmadas, e os dois checks finais de biblioteca fecham (CTN 191-A = trava de concessão/como certidão positiva-efeito negativa; lei11101 linha 7 = art. 6º §7º-B + art. 57). A minuta confirmada: **não fixa valor por parcela** (classe III/IV) — vou apenas refinar a atribuição no JSON linha 45 (a §6 cobre índice/taxa; o fato "sem valor por parcela" vem da própria minuta). Aplicando agora as 9 correções:

9/9 correções aplicadas. Agora o recompute formal em Python — todas as asserções sobre os números-chave do engajamento + revalidação do parse dos dois JSONs (inclusive verificação do balanço do lançamento 1 dentro do próprio JSON editado):

`valor: null` no bloco condicional da UPI quebrou o somatório (`None`). Corrigindo o somboramento:

29 asserções + 3 checks estruturais: tudo passa. Último passo — registrar a revisão no `STATUS.md` (antes de "Itens em aberto"), mantendo o status geral:

Checagem final das edições (presença do novo, ausência do antigo):

O grep revelou **um site adicional não triado** do mesmo problema de rotulagem: `sessao2/efeito_tributario_desagio.json` linha 44 também afirma como fato que "o art. 50-A, II trata apenas do LIMITE da trava de compensação" — mesmo erro semântico corrigido no S3. Lendo o arquivo para corrigir com contexto:

Confirmado — a linha 44 carrega a mesma imprecisão ("trata apenas do LIMITE da trava de compensação" como fato; o objeto do limite não vem da biblioteca). Corrigindo no S2 com a mesma redação do S3 e alinhando a nota da revisão no STATUS; depois revalido o parse:

Última pendência: o JSON do S2 foi editado **depois** do último run de Python — revalido o parse e confirmo que nenhum resíduo das frases antigas sobrou (bem como os rótulos de interpretação que devem permanecer):

Os "resíduos" apontados estão no `STATUS.md` — mas a seção de revisão que acabei de adicionar **cita as frases antigas entre aspas** ao descrever cada correção ("já **deletada**" → ...). Verifico se todos os hits são essas citações do changelog (uso legítimo), e não afirmações vivas:

Tudo fechou: os três únicos "hits" do padrão são as **citações entre aspas no próprio changelog do STATUS.md** (linhas 29–31: "X" → "Y"), uso legítimo — não há nenhuma ocorrência viva das frases antigas em nenhum entregável. Os relabels, o flag `trava_30`, a fórmula de compensação rotulada e o parse pós-edit estão todos verificados. Encerrando o turno.

---

## Revisão final concluída — resumo das mudanças

**Entregáveis corrigidos (11 correções em 6 arquivos):**

1. **`STATUS.md`** — itens em aberto com numeração trocada corrigida: **6 = pessoas ligadas · 7 = encargos/juros/taxas** (conforme QUESTIONS.md itens 6/7).
2. **`QUESTIONS.md`** — item 13: "pre-declarada" → "**pré-declarada**"; item 14: frase embaralhada reescrita ("lançamentos datados no placeholder **D_HOM** — os valores **independem da data**").
3. **`sessao3/passivo_fiscal_solucao.md`** — (i) "cláusula já **deletada**" → "**deleção recomendada** (veredicto #4 da Sessão 2) e pendente de ajuste da minuta" — a recomendação **nunca foi executada**; (ii) célula da Rota C: "≤ 2.700.000 − 70% = 810.000" → "**2.700.000 × 30% = 810.000 no teto do desconto**".
4. **`sessao3/lancamentos_novacao.json`** — (i) ruído "; conclusão ao final" removido de `fontes_citadas`; (ii) art. 50-A, II relabelado: apenas **afasta a sujeição do ganho ao limite percentual (trava de 30%)** — não isenta; **objeto do limite NÃO VERIFICADO**; (iii) nota da parcela média reatribuída com precisão (nem a minuta fixa valor por parcela — fato da própria minuta; nem constam índice/taxa — `analise_plano.md` §6, item 1).
5. **`sessao2/efeito_tributario_desagio.json`** — mesmo relabel do art. 50-A, II na `irpj_csll.base.nota` (afirmava como fato que a trava é "de compensação"); a fórmula condicional de compensação local **já era interpretação rotulada** — mantida.
6. **`sessao1/resposta_diretor.md`** — "≈" → "=" (1.890.000 ÷ 84 **=** R$ 22.500/mês, valor exato).

**Decisão de autoridade (sem mudança, documentada no STATUS):** as citações dos arts. 64/172, par condicio e convolação reproduzem literalmente o texto do arquivo whitelisted `lei11101_excertos.md` (linha 13), e todas as passagens do deliverable atribuem a esse arquivo. A coluna de citação do INDEX enumera as matérias principais do excerto — não retira autoridade do conteúdo citável do próprio arquivo. Nenhuma autoatribuição a normas fora da biblioteca.

**Validação executada:**
- **Python — 29 asserções ✓**: total de créditos 13.540.000 (concursais 7.430.000 = trab 960.000 + quiro/ME-EPP 6.470.000; Beta 3.100.000; União 2.700.000; pós-pedido 310.000); plano pagável 3.548.000 (960.000 + 40% × 6.470.000); ganho 3.882.000 (2.520.000 + 1.110.000 + 252.000); parcelas (12×80.000; 2.588.000/120 = 21.566,67); rotas A/B/C (120×22.500; 810.000 + 84×22.500; teto 810.000); matriz de folgas **952.000 / 142.000 / −938.000 / −1.748.000**; caixas 890.000/840.000.
- **Balanço do lançamento 1 lido de dentro do JSON**: Dr = Cr = 7.430.000 ✓.
- **Parse dos dois JSONs revalidado após cada edição** ✓; cross-refs § (§1/§3/§6/§6.4 de `analise_plano.md`; §3.2 e §4 de `demonstrativo_mensal_aj.md`) todos válidos.
- **Varredura final de resíduos**: 0 ocorrências vivas em todo o `deliverable/` (os únicos hits são as citações do changelog).

**Status final:** `deliverable/STATUS.md` — **COMPLETE WITH OPEN ITEMS** (mantido), com a nova seção "## Revisão pré-entrega (2026-10-25)" registrando as correções, a decisão de autoridade e a validação. As pendências carregadas (itens sem resposta do cliente) permanecem documentadas e nunca serão re-perguntadas.