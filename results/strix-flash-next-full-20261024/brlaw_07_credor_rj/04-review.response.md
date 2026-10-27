Vou auditar tudo: primeiro a biblioteca (o que é citável), depois os documentos e, por fim, as cinco peças — conferindo cada citação, número e data.

Biblioteca mapeada. Agora os documentos do caso e as cinco peças:

O `str_replace` não casou (bytes invisíveis prováveis). Vou inspecionar o raw dessa região e fazer a substituição via Python em bloco único, preservando CRLF:

O arquivo real diverge do que o `read` mostrava — há conteúdo sobre a retirada já no início. Dump real do bytes, linha a linha:

Conteúdo real confirmado — idêntico ao mapeado. Aplicando os 6 ajustes no `resposta_cliente.md` em lote com asserções:

Agora a peça ao AJ: tirar o aparte interno da peça e mover para nota do drafter, e **estrategia.json** inteiro via Python:

Texto real da peça obtido. Aplicando as correções exatas (peça + JSON):

Erro de digitação no script (fechava com `]` em vez de `)`). Corrigindo e rerodando:

A peça ficou limpa (1 menção, só na nota). O JSON tem chaves diferentes das supostas — mapeando a estrutura real:

Agora os dois arquivos de rastreio — despejo o conteúdo real deles antes de editar:

Conteúdos reais confirmados. Ajustes finais em PERGUNTAS.md e STATUS.md (flag do marco do stay, conformidade precisa e registro da auditoria):

Sanidade final nos cinco entregáveis antes de reportar:

A substituição da contagem dupla do prazo não chegou a ser aplicada no JSON (a tentativa anterior falhou em uma chave inexistente). Inspecionando o texto real do prazo:

Auditoria pré‑entrega concluída e aplicada. Varredura final confirma: `estrategia.json` válido (8 ações, schema intacto), nenhuma sonda residual nos entregáveis (as duas ocorrências em `STATUS.md` são apenas as citações do próprio changelog), e todas as datas/contas conferem.

## O que foi revisado
Re‑li integralmente `library/INDEX.md` + os 5 arquivos indexados, os 4 documentos do caso e os 5 entregáveis, e refiz por conta própria (Python) os dias da semana e toda a aritmética: 10/04 sex, 11/04 sáb, 13/04 seg, 24/04 sex, 25/04 sáb, 27/04 seg; 900k + 1,2M = 2,1M; −1,6M = 500k; 1.200.000 × 0,70 = 840k; × 0,40 = 480k; 900k × 0,60 = 540k. **Tudo reconcilia.**

## Correções aplicadas

**`resposta_cliente.md`**
1. "fiança fiduciária" → "garantia fiduciária" (a fiança é a pessoal do sócio; a do crédito é fiduciária).
2. Parágrafo que ainda pedia dados [◆] ao cliente substituído — CNPJ, endereço, certidão EPP, ficha dos bens e planilha serão obtidos **por nós** (autos TJSP, Junta Comercial, registro da garantia), coerente com o registro de que o cliente não tem mais informações.
3. **"3,3 anos mais cedo" removido** — a minuta não fixa juros e a conta 120×III vs. 36×IV não produz esse número. Substituído pelos dados verificáveis da minuta: carência 24→6 meses, 120→36 parcelas.
4. §6: o marco inicial do *stay* passou a ser rotulado como **inferência não verificada** na biblioteca (o art. 6º §7º‑A fixa só a duração — 180 dias prorrogáveis).
5. Banner de urgência agora aponta para os itens **2 e 6** (ambos tratam da retirada vedada); corrigido o typo "bons tratamento".

**`habilitacao_divergencia.md`**
6. O aparte "não verificado na biblioteca" saiu do **corpo da peça** (iria ao AJ Reorganiza) e virou nota do redator [◆]; o corpo ficou com a asserção fática da EPP e os campos [◆] já com a fonte de obtenção (certidão da Junta Comercial).

**`estrategia.json`**
7. Prazo com as **duas contagens convergentes** registradas: (a) dia 1 = 13/04 → dia 15 = 27/04; (b) dia 1 = 11/04 → 25/04 (sábado) + extensão do CPC art. 224 §1º (nota do arquivo indexado) → 27/04; protocolo defensivo até sex 24/04.
8. Economia da classe IV com as **multiplicações explícitas** (840k vs. 480k; 900k vs. 540k), não só resultados.
9. Voto: exceção trabalhista do art. 10 §1º explicitada e direito de voto da habilitada a tempo (*a contrario sensu*); marco do *stay* marcado como NÃO VERIFICADO em 2 pontos.

**`PERGUNTAS.md` / `STATUS.md`**
10. U2 flagada (marco presumido do *stay*) + nova assunção nº 5; STATUS com descrição precisa da resposta ao cliente, conformidade exata das fontes (Tema 1.051 no INDEX; REsp 1.333.349/Tema 885 e CPC 224 §1º no texto dos arquivos indexados) e a seção "Auditoria pré‑entrega (20/04/2026)" com este registro.

## O que continua em aberto (por opção, não por descuido)
- **Divergência dos R$ 1,6 mi**: permanece declarada **não reconciliável** com a nossa base (diferença R$ 500 mil em aberto; não forcamos o número).
- **U2** (data do deferimento do processamento) e **U1/U3–U7**: a extrair dos autos TJSP / Junta Comercial / registro da garantia — nada disso bloqueia o protocolo até 24/04.
- Itens mantidos como "não verificado": limites da LC 123/EPP, regime tributário × classe IV, marco do *stay*, regresso do fiador sujeito à RJ, defesas cambiais.

`deliverable/STATUS.md` mantém **COMPLETE WITH OPEN ITEMS** — os 5 entregáveis existem e nada foi declarado completo com peça faltante.