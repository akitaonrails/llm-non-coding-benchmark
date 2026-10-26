Vou fazer a revisão de pré-entrega em passada completa: releitura integral dos quatro artefatos, conferência de toda citação contra a biblioteca, recomputação de toda a aritmética e varreduras de resíduo. Começando pelos textos completos:

Prosseguindo a revisão — leitura integral das partes que faltam:

JSON e §5.7–§10 lidos. Faltam o miolo do parecer (§2–§5.6), as partes restantes de QUESTONS/STATUS e a biblioteca — lendo tudo:

Arquivo principal mapeado. Falta o fim do STATUS, o cabeçalho do parecer e a biblioteca — conferindo agora (pontos críticos: a citação de Lei 9.029/95 e o suporte do dano moral):

Biblioteca parcialmente lida — a **Lei 9.029/95 consta da biblioteca** (linha 3 de `estabilidade_gestante.md`), então a citação em si é suportada. Falta conferir ÍNDICE, CIPA e CLT 482/493, e enumerar as ocorrências da data "22/09/2027":

Biblioteca integralmente conferida. Resultado das verificações de autoridade:

- **Lei 9.029/95 consta da biblioteca** (`estabilidade_gestante.md` linha 3; INDEX linha 8) — a citação é válida; mas o parêntese em §4.2 atribui conteúdo ("veda a discriminação por gravidez") que **não está transcrito** no arquivo da biblioteca. Vou destacar explicitamente.
- **"Deslocar o dano moral para o topo da faixa"** (§10, item 2): a biblioteca fixa apenas a faixa R$ 5–20 mil / 223-G; o deslocamento para o topo é ponderação própria — precisa de rótulo "não verificado".
- **Off-by-one de datas confirmado**: 11 ocorrências de "22/09/2027" / "2027-09-22" contra DPP ≈ 23/04/2027 + 5 meses = **23/09/2027**.
- **Retaliação agravando dano moral** (§6, item 6): assertiva de efeito jurídico sem suporte na biblioteca — rotular.
- Pontos de aritmética (§5.1/§5.2/§5.5/§5.7) parecem coerentes — revalidarei em Python após as correções, com nota de fração de dias (≥15 dias = 1 mês) que hoje não está rotulada.

Corrigindo o parecer.md (5 correções):

Tentativa anterior falhou por "sumam" vs "somam" — aplicando com o texto exato:

A nota de fração foi inserida, mas o rótulo ficou contraditório com a frase anterior ("a biblioteca lista as verbas sem transcrever regras de fração" + "**constante da biblioteca, não verificado**"). Corrigindo para o rótulo correto:

Agora os arquivos JSON, QUESTIONS e STATUS. Primeiro os textos exatos das linhas do JSON:

Todas as editeis aplicados. Agora a revalidação aritmética completa em Python:

O script saiu incompleto — reescrevendo integralmente:

Antes de rodar, confiro quais números realmente aparecem em cada arquivo (para não criar checks falsos):

Boa notícia: sem números órfãos — o JSON contém os totais principais e não contém o cenário §5.5 (como projetado). Ajustando os checks de presença por arquivo e rodando:

A edição removeu o carregamento dos arquivos — reescrevendo a cauda do script por completo:

Há uma linha corrompida no script ("topo进行调查") — confiro antes a contagem real de "topo" no md e então conserto:

O único FAIL é do próprio check, não do parecer: `02/06 − 12/05` em `.days` é 21 por convenção de diferença de endpoints, mas a contagem de salário-dia é inclusiva (12–31/05 = 20 dias + 1–2/06 = 2 dias = 22). Corrijo o check para a convenção certa, com prova de cobertura exata do intervalo:

Revisão concluída. Script de verificação reexecutado após a correção do check de §5.2: **143 PASS / 0 FAIL** nos 4 entregáveis (`parecer.md`, `parecer.json`, `STATUS.md`, `QUESTIONS.md`). O único FAIL intermediário era bug do próprio script (diferença de datas em `.days` é exclusiva de extremo; a contagem de salário-dia é inclusiva: 12–31/05 = 20 + 1–2/06 = 2 = 22 dias) — o check foi reescrito com prova de cobertura exata do período (20 + dias de 01/11/2026–31/05/2028 + 2 = dias de 12/10/2026–02/06/2028) e passou.

## O que foi alterado nesta revisão

**1. Datas da garantia gestante — 11 pontos corrigidos (deslocamento de 1 dia)**
- "~22/09/2027" → "~23/09/2027" em 5 lugares do `parecer.md`, 2 do `parecer.json`, 1 do `QUESTIONS.md` e 2 do `STATUS.md`.
- `parecer.json`: campo `"ate"` → `"2027-09-23 (estimado…)"`.
- Motivo: DPP 23/04/2027 + 5 meses completos = 23/09/2027 (o "22" vinha de contagem inclusiva do dia do parto). Nenhum total mudou.

**2. `parecer.md` §4.2 — citação da Lei 9.029/95 restringida à biblioteca**
- Nova redação: "a biblioteca cita ainda a Lei 9.029/95 como fonte deste fundamento (sem texto de dispositivo transcrito no arquivo)". Releitura confirmou que a lei **está** no INDEX e em `estabilidade_gestante.md` — portanto citável; nada foi removido, apenas o glosa passou a afirmar só o que a biblioteca de fato contém.

**3. `parecer.md` §10 — alegação do "topo da faixa" rotulada**
- A faixa de dano moral R$ 5–20 mil segue fundamentada na biblioteca; a ponderação de que a dispensa punitiva por crítica verdadeira desloca a fixação ao **topo** da faixa agora está rotulada "ponderação deste parecer, não constante da biblioteca — não verificado".

**4. Rótulos de retaliação**
- `parecer.md` §6 item 6 e linha correspondente do `parecer.json`: "retaliação agravaria o risco de dano moral" recebeu "(ponderação não constante da biblioteca — não verificado)".

**5. `parecer.md` §5.2 — decomposição explícita**
- "19 salários mensais" + "22 salários-dia" agora demonstrados: 22 = 20 dias de out/2026 (12 a 31/10) + 2 dias de jun/2028, com nota de checagem Python (148.200,00 + 5.720,00 = 153.920,00 ✓).

**6. `parecer.md` §5.1 — nota de regras de fração**
- Inserida após a tabela: 13º exige fração ≥ 15 dias (out/2026 = 11 dias, não conta → 9/12); férias = 6 meses completos (15/03→15/09/2026) + fração de 26 dias, que ≥ 15 dias conta como mês → 7/12; salário-dia sobre divisor 30. Rotulada "**não constante da biblioteca — não verificado**" + (P) — a versão inicial tinha rótulo contraditório ("constante da biblioteca"), corrigido.

**7. Verificações de resíduo (tudo zero)**
- Sem sobras de total antigo (197.326 / 199.326 / 200.326), sem 22/09/2027 ou 2027-09-22 em qualquer arquivo, sem typo "sumam", cronologia sem linhas duplicadas, JSON válido, cenário §5.5 (R$ 261.930,79) confirmado fora do JSON, §9 lista exatamente as 4 fontes do INDEX.

**Intactos:** total principal R$ 213.326,27; piso R$ 198.326,27; teto R$ 218.326,27; `justa_causa_cabivel: false`; data do parecer 11/10/2026; P1–P6 em aberto sem repetição.