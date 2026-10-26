Vou fazer uma auditoria completa antes da entrega: reler toda a biblioteca (autoridade), os documentos-fonte, o contrato e o parecer, e recomputar cada número. Começando pelas fontes:

Agora os documentos-fonte e o contrato:

Fontes conferidas (biblioteca, documentos, contrato). Agora releio na íntegra os quatro entregáveis para cruzar cada número e cada citação:

Continuing the audit. I need the exact text of the parecer in small chunks to apply precise edits (the full-file read got truncated):

Tenho o parecer completo. Preciso dos trechos finais de QUESTIONS.md e STATUS.md antes de editar:

Tenho tudo. Aplico agora os ajustes da auditoria (paralelos, alvos distintos):

Ajustes aplicados. Agora executo a validação completa (JSON/schema, aritmética, figuras-chave e strings proibidas/obrigatórias):

Pequena correção no script (geração dos escapes `\uXXXX` para casar com o texto bruto do JSON):

O schema do CONTRACT é aninhado (o meu script assumiu JSON plano). Ajusto o verificador para percorrer folhas recursivamente:

O comentário do arquivo tem acento que não reproduzi. Sobrescrevo o arquivo inteiro com a versão recursiva:

Executando a validação completa (script reescrito, versão recursiva):

Somente 1 falha — e é um artefato do meu verificador (a regex de chaves `[a-zA-Z_]+` não aceita dígitos, logo não casa `irrf_distribuicao_2026`). Vou confirmar no CONTRACT:

Confirmado: a falha é artefato do script — o schema na linha 8 do CONTRACT traz `"irrf_distribuicao_2026"`, mas a regex de chaves (`[a-zA-Z_]+`) não aceita dígitos, e o schema está em bloco inline (`` ` ``), não em bloco ```json```. Corrijo o verificador:

Sem falhas. Confirmo o início da saída (checagem de schema, que era a que falhava):

Validação 100% limpa: schema (14 caminhos = 14 do CONTRACT), folhas inteiras, ~45 asserções aritméticas Decimal, presença de figuras, correções aplicadas e strings proibidas ausentes. Confiro o registro duradouro em STATUS.md para reproduzir fielmente a lista ao usuário:

Auditoria concluída e tudo validado. Resumo do que revistei e do que mudei:

## Como auditei
- **Autoridade:** cada citação do parecer conferida palavra por palavra contra os 6 arquivos de `library/` (governados por `INDEX.md`); tudo que não está na biblioteca agora está rotulado "não verificável".
- **Números:** todos refeitos com aritmética decimal em script de validação — schema do JSON conferido recursivamente contra o schema fixo do `CONTRACT.md` (14/14 caminhos idênticos), folhas numéricas todas inteiras e ~45 asserções aritméticas passando.
- **Rastreio de texto despachado:** checagens de presença (correções aplicadas) e ausência (frases removidas) — 0 falhas.

## O que mudei (registro duradouro em `STATUS.md`, item "Auditoria pré-entrega")
1. **Legítima citada pelos arts. 1.845–1.846** (parecer) — o art. 1.789 aparece só na linha de citação da biblioteca, sem texto reproduzido. Eliminada citação sem suporte.
2. **Removida a afirmação "base legal do ITBI = valor venal municipal"** (parecer item 1, Premissa C, `numeros.json`, QUESTIONS item 1, STATUS item 3) — a biblioteca não traz a base. A estimativa pelo valor de mercado **permanece como premissa** rotulada "não verificável", com a nota de que a estimativa cai na mesma proporção se a base real for menor.
3. **Removido o gloss "(fato gerador consumado)"** no item 3 do parecer — não é texto da biblioteca.
4. **Registrada a opção de ITCMD integral no ato** (a biblioteca a menciona junto ao 2/3–1/3); total invariante de R$ 328.600, muda só o timing.
5. **Cláusulas restritivas em doação relabeladas como inferência** (arts. 1.848 + 544, por inferência dos dispositivos reproduzidos) — sem regra textual na biblioteca; "definição literal" ajustada.
6. **Nota do RE 1.495.108 (Tema 1.348) acrescentada** ao item 1 do parecer — consta da biblioteca e estava ausente.
7. **QUESTIONS item 6 reescrito** — o texto antigo afirmava que mais despesas *aumentariam* a vantagem da PJ sem condição. Correto: depende do tipo — despesas dedutíveis no carnê-leão **diminuem** a vantagem; fora da lista, **aumentam**.
8. **"Demais regras da colação (arts. 2.002–2.012)" e "base legal do ITBI-SP"** incluídas na lista de não verificáveis do parecer.

## O que NÃO mudei
**Nenhum cálculo alterado.** A recomputação confirmou todas as figuras: ITBI 492.900 = 3% × 16.430.000 (141.600 + 351.300); PF 257.756,40; PJ 124.031,64; PJ+IRRF 145.358,08; economia 112.398,32; payback 4,39 anos (leitura alternativa: 205.358,08 / 20,16% / payback 9,41); ITCMD 328.600 (219.066,67 + 109.533,33); total do plano 741.200; doação 8.215.000 ≤ teto 9.265.000 (folga 1.050.000); piso de Marcos 3.088.333,33; R/P 7.720.833,33 cada; receita anual 1.018.800 = 84.900 × 12. Também descartei um erro meu de contagem mental (1.038.800) — o arquivo sempre esteve certo.

Os quatro entregáveis (`parecer.md`, `numeros.json`, `QUESTIONS.md`, `STATUS.md`) estão prontos para envio.