Gatilho da Sessão 5 recebido. Antes de produzir `deliverable/sessao5/`, preciso conferir: o texto exato do item 6 no contrato, os desconhecidos nº 5 e nº 6 no `QUESTIONS.md`, a biblioteca disponível (ÍNDICE + arquivo de SELIC/garantia) — e se algum documento novo ingressou no workspace para resolver os insumos que estavam faltando:

O workspace ingressou exatamente com o insumo que faltava: `documents/sessao5/proposta_garantia.md` — e a biblioteca ganhou os dois arquivos que sustentam a Sessão 5 (`selic_e_garantia.md`, `transacao_pgfn.md`, ambos no INDEX). Lendo tudo em paralelo junto com os desconhecidos nº 5 e nº 6 no QUESTIONS:

Insumos chegaram: a intimação do juízo para garantir (LEF art. 9º) **ou** aderir a transação/parcelamento, com cotações reais (seguro 1,2%/a.a. + 30%; fiança 2,5%/a.a. + 30%; penhora de faturamento 5%), SELIC 3,9% (10/07→30/11/2026) e edital PGFN (65% multa/juros, 120 meses) — resolvendo na prática os desconhecidos nº 5 e nº 6 (cotações obtidas; faturamento/balanco continuam sem número, o que rotularei). Antes de compor o `garantia.json`, espelho o estilo do JSON da Sessão 3 (único JSON entregue até aqui):

Antes de escrever o `garantia.json`, preciso de quatro confirmações de raiz — os valores exatos da decomposição da Sessão 1 (principal/multa/juros por período), o STATUS atual (para reescrita integral com preservação do histórico), o texto do LEF art. 9º na biblioteca (a base citável das modalidades de garantia) e o índice completo da biblioteca mais os desconhecidos nº 5/º6 no QUESTIONS. Também vou resolver uma ambiguidade de caminho (deliverable em `/work` vs `/work/workspace`):

`deliverable` é symlink de `workspace/deliverable` — mesmo destino; a pasta `sessao5` ainda não existe. O LEF art. 9º está verbatim na biblioteca ("fiança bancária ou seguro garantia" + penhora — a base citável das modalidades) e o art. 16 confirma o dado-chave da recomendação: **embargos em 30 dias contados da garantia**. Falta o essencial: o schema exato do item 6 no contrato (truncado na leitura anterior), o índice completo da biblioteca e a redação exata dos desconhecidos nº 5/º6:

Tudo confirmado. O schema exato do item 6: `garantia.json` com `valor_remanescente_atualizado`, `seguro_garantia{valor_garantido,custo_anual}`, `fianca{valor_garantido,custo_anual}`, `transacao{base,desconto_estimado,observacao}` e `recomendacao` — e o precedente da casa (Sessões 1 e 3) acrescenta um array `notas`. Os componentes do remanescente (principal/multa/juros) vêm do bloco de aritmética da Sessão 1 no STATUS, com a nota do `analise.json` confirmando multa = 75% do principal em cada período. Escrevendo o `garantia.json`:

O write anterior foi interrompido por limite de tokens — vou reemitir em passos menores: primeiro os campos do schema (com `observacao`, `recomendacao` e `notas` ainda vazia), depois preencho as notas por edições. Em paralelo, leio o STATUS em duas fatias (fonte verbatim para a reescrita integral):

**Passo 1 — campos do schema:**

`garantia.json` criado com os campos do schema. Agora preencho as notas e reescrevo o STATUS (as edições no STATUS são em regiões disjuntas; as notas no JSON precisam ser sequenciais por causa das âncoras):

**Edição das notas 1-3 + reescrita do STATUS em pontos precisos**