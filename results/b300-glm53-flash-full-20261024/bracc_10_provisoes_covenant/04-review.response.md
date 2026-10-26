Boa — revisão prévia à entrega. Vou reabrir tudo: contrato, biblioteca (as 4 normas), documentos do cliente e os 5 entregáveis, conferindo autoridade, itens citados e aritmética.

Biblioteca relida — já flaguei um ponto: a reversão da provisão na `cpc25.md` está no **item 59** (não no 36, como escrevi na seção 7 da carta). Agora os documentos do cliente:

Documentos batem com os números. Agora os 5 entregáveis na íntegra:

Nota e JSON conferidos — achei dois deslizes reais: (a) na carta, atribuição da regra de reversão ao item 36, quando a biblioteca a coloca no **item 59**; (b) na nota, resto de inglês ("papers"). Vou reler carta e PERGUNTAS atuais e o STATUS pós-edição:

Revisão completa terminada. Achei **um erro de substância sério** que passou: escrevemos "sem waiver, **os R$ 31,2 milhões** vão para o circulante" — mas o excerto da escritura só prevê vencimento antecipado das **debêntures**; não há cláusula de cross-default para os demais empréstimos, e o quadro de vencimentos dos R$ 24,7 mi não foi informado. Além disso: item errado da CPC 25 (reversão é **item 59**, não 36), resto de inglês ("papers"), fundamentação errada no argumento "capitalizar o AFAC", parêntese faltando etc. Corrigindo tudo:

Nota corrigida (5 edições aplicadas). Agora as edições da carta — primeiro leio o texto atual para pegar as strings exatas, junto com STATUS e PERGUNTAS completos:

Strings exatas na mão. Aplicando agora as 9 edições da carta (item 59, parêntese §4, §5 reescrita, citação CPC 24/26, capitalização, waiver "representando 75%", acentos e "** Não**"):

Carta corrigida. Agora STATUS, PERGUNTAS e um remate na premissa 6 da nota:

Todas as edições aplicadas. Agora a bateria final de validação — JSON, citações, mojibake e sobras:

Validação limpa: JSON ok, nenhuma citação fora do índice, sem mojibake/cirílico, e as únicas sobras de "item 36"/"≥ 75" estão no log de revisão do STATUS (citação histórica proposital). Última conferência visual das regiões editadas e do diretório:

Pouco antes de fechar, um último acerto de gramática que escapou: "o caixa e aplicações segue R$ 4,1 milhões" (carta §7 e STATUS) — falta a preposição. Confirmo se há outras ocorrências:

O `literal:true` tratou o pipe como texto — refaço como regex:

Confirmado — 2 casos. Acerto ambos:

Caminho errado no segundo (faltou o `/work`). Corrigindo:

Confirmo que não restaram instâncias:

Revisão pré-entrega concluída, incluindo este último acerto de gramática. Resumo do que foi feito:

## Defeitos substantivos encontrados e corrigidos

1. **Regra de reversão da provisão (erro de citação)** — a carta §7 atribuía a regra de reversão ao "item 36" da CPC 25; a regra está no **item 59** (o item 36 integra apenas a seleta do excerto). Corrigido na carta; nota e §1 já usavam o item 59 com a citação do conjunto completa.
2. **Alcance do vencimento antecipado (excesso não suportado)** — nota, carta, STATUS e PERGUNTAS afirmavam "os R$ 31,2 milhões vão para o circulante" no descumprimento. O excerto da escritura prevê aceleração sobre as **debêntures da 1ª emissão**; a CCB vai ao circulante pelo vencimento em 8 meses; **não há cross-default** para os demais R$ 24,7 mi — cujo quadro de vencimentos não foi informado. Consequência reescrita nos quatro arquivos.
3. **Fundamentação da capitalização do AFAC** — o texto anterior ("o caixa do aporte já está dentro dos R$ 4,1 mi") implicava saída de caixa sem base no dossiê. Reescrito: capitalizar **não cria caixa novo** — na leitura restrita da fórmula DL e índice ficam iguais; na leitura em que o mútuo conta como dívida, a capitalização só retira o mútuo do numerador (29,1 → 27,1 mi) e o índice segue 2,77 — **descumprido nas duas leituras** (carta §7 e STATUS).
4. **Redação do waiver** — alinhada ao texto da escritura: "aprovado por debenturistas **representando 75%**" (não "≥ 75%") — sem inferir quórum que o excerto não define.
5. **Premissa 6 adicionada à nota** — a linha de R$ 31,2 mi é agregada (só a CCB está destacada); o valor das debêntures aceleradas não está individualizado; partilha interna do circulante parcialmente indeterminada → novo **item aberto** (STATUS item 3 e PERGUNTAS item 5 estendidos).

## Cosméticos/language

"papers" → português limpo; "Nesta materia" → "Nesta matéria"; "vencidades" → "vencimentos"; "client" → "o cliente"; "** Não**" → "**Não**" (3×); parêntese "(a fórmula soma…)" restaurado em §4; linha da diretoria no bloco de código reescrita; citações "(CPC 24/CPC 26 …)" → "(CPC 24; CPC 26 itens 74-75)" (2×); cauda da premissa 6 da nota relibada; "o caixa e aplicações segue R$" → "o saldo de caixa e aplicações segue **em** R$ 4,1 milhões" (carta) e "caixa segue em R$ 4,1 mi" (STATUS).

## Validação final — tudo limpo

- **JSON** parseia; bloco covenant exatamente conforme o contrato: EBITDA 9.800.000; DL 27.100.000 (nas duas variantes: diretoria e correta); índice da diretoria 2,46 vs. **correto 2,77**; limite 2,75; `cumprido: false`.
- **Citações**: todas as referências `library/` apontam para os 4 arquivos indexados (+ INDEX); nada fora da biblioteca citado como autoridade.
- **Encoding**: sem mojibake ou caracteres cirílicos.
- **Sobras**: "item 36" e "≥ 75%" aparecem apenas no log de revisão do STATUS, como citação histórica do que foi corrigido.
- **Diretório**: exatamente os 5 entregáveis (+ `.keep`).

`STATUS.md` permanece **COMPLETE WITH OPEN ITEMS** — 7 itens abertos (interpretação da escritura sobre mútuos de acionista na DL; quadro dos R$ 24,7 mi e valor individualizado das debêntures; data/instrumento do aporte AFAC; composição da condenação por rubrica; régua de EBITDA auditada; decisão de início do waiver; viabilidade do aporte novo até 31/12), além do log de revisão. Não restam pendências do meu lado: o pacote em `/work/workspace/deliverable/` está pronto para entrega.