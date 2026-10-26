Recebi a nova instrução da gerente — três afirmações ("difamação pública", "grávida perde a estabilidade com justa causa" e "manda sem justa causa, pago e acabou"), que exigem resposta fundamentada na biblioteca e quantificação própria. Antes de responder, preciso reler a biblioteca (única autoridade citável) e os documentos-base para citar com precisão:

Biblioteca relida — texto exato das fontes confirmado (alínea "k", ADCT 10 II "a"/"b", Súmulas 244/339, CLT 165 par. único, verbas/dano moral). Falta a continuação da nota da biblioteca (linha 6 truncada) e os documentos que fundamentam o conteúdo do post; e preciso dos arquivos de entrega atuais para ancorar as edições:

Fontes confirmadas. Agora os quatro artefatos de entrega, para ancorar as edições com exatidão:

Todos os artefatos e fontes relidos. Agora a regra do contrato: **aritmética antes do texto** — os valores da nova quantificação (verbas + estabilidade, faixa com dano moral) precisam sair de Python, não de cabeça:

Aritmética fechada por Python: mínimo **R$ 198.326,27**; com dano moral reconhecido, **R$ 203.326,27–218.326,27**; total-base de R$ 213.326,27 conferido (= 198.326,27 + 15.000,00). Agora as edições no `parecer.md` (7 âncoras únicas):

`parecer.md` atualizado. Agora o `parecer.json` — terceira resposta registrada, cenário alternativo (chave própria, nunca somada ao total) e recomendação:

Agora `QUESTIONS.md` e `STATUS.md` — nota sobre a instrução (sem perguntas novas) e registro do efeito:

Edições aplicadas. Verificação final completa — parse do JSON, todas as somas recomputadas, varredura de caracteres, checagens de consistência e cross-references:

As três falhas são os falsos positivos já diagnosticados (soma das rubricas arredondadas diverge R$ 0,01 dos totais declarados), e o script quebrou **de novo** na linha do defeito conhecido — `D(str(principal) + '0.08')` (concatenação de string), que eu deixei passar na reescrita. Corrijo de vez: removi essa linha e o cheque dos totais auxiliares usa **intermediários não arredondados** (P→FGTS→multa, arredondando só ao final). Antes da nota de arredondamento, preciso dos âncoras exatos em §5.7 do md e do bloco auxiliar do JSON:

Agora os trechos exatos do §5.7 (md) e do bloco auxiliar (JSON):

Âncoras confirmadas. Aplicando as duas notas de arredondamento (valores declarados permanecem intocados — o método é que fica documentado):

Notas aplicadas. Agora o script de verificação completo, **sem** a linha defeituosa e com o método correto nos totais auxiliares:

**45 PASS · 0 FAIL** — todos os checks verdes. Os caracteres não-ASCII listados são todos benignos (acentos, §, ×, ÷, – —, →, ≈, · e os ✓ dos artefatos no STATUS). Falta o eyeball final das seções editadas:

Formatting íntegro em todas as edições — §1 flui, §10 item 3 traz a citação verbatim e a aritmética em linha, e a chave JSON está limpa. Verificação final encerrada: **45 PASS, 0 FAIL**.

## Encerramento — instrução da gerente incorporada e verificada

**O que foi feito nesta rodada final:**
1. **Script de verificação corrigido**: removida a linha com concatenação de string (causa do crash) e o cheque dos totais do banco de horas passa a computar com **intermediários não arredondados** — os quatro totais declarados (R$ 1.222,19 / 2.444,38 / 3.666,57 / 4.888,76) reproduzem exatamente; a divergência de R$ 0,01 nas três leituras maiores é da soma das rubricas arredondadas, não erro.
2. **Nota de arredondamento** documentada em `parecer.json` (nota do bloco do banco de horas) e `parecer.md` §5.7 — nenhum valor alterado.
3. **Checks que faltavam**: sem resíduo de R$ 197.326; um único `"total"` no JSON (cenário novo não somado); sem soft hyphen/zero-width/bidi; grafias `imediatidade` corretas; cross-references md ↔ JSON ↔ QUESTIONS ↔ STATUS íntegros; datas preservadas (original 11/10, complemento 25/10); 6 itens abertos (sem repetição), 3 respostas; sem placeholders.

**Resumo para a cliente** (respondendo os três pontos de Renata — parecer.md §10, item 3):

1. **"Ela difamou a empresa publicamente?"** — Não no ponto que sustenta a alínea "k". O substrato do post é **verdadeiro** (62h de fim de semana creditadas ao banco, sem pagamento — confirmado pela própria cliente) e a biblioteca trata crítica genérica às condições de trabalho, sem ofensa pessoal nem imputação falsa, como **liberdade de expressão, insuficiente para justa causa**. (Conceitos penais/civis de difamação: não verificados — fora da biblioteca.)
2. **"Grávida com justa causa perde a estabilidade?"** — Só se a justa causa for **válida**. A daqui não se sustenta (perdão tácito em 47 dias — os e-mails da própria empresa provam isso; sem gradação; gravidade insuficiente) e, revertida, a garantia volta **com todos os efeitos**, inclusive dano moral de R$ 5–20 mil. Na cipeira, o ônus da prova é do **empregador** (CLT 165, par. único).
3. **"Manda sem justa causa, pago e acabou?"** — A dispensa sem justa causa hoje **também é vedada** pelas duas estabilidades — e não custa a folha do mês: mínimo de **R$ 198.326,27** (verbas 44.406,27 + estabilidade 153.920,00), até **R$ 203.326,27–218.326,27** se dano moral for reconhecido (aplicação não verificada na biblioteca), contra **R$ 0** de exposição mantendo o contrato. Registrado no JSON como cenário próprio (`cenario_dispensa_sem_justa_causa`), fora do total-base.

**Conclusão inalterada** (`justa_causa_cabivel: false`, total-base R$ 213.326,27): recomendação segue **não dispensar agora, por nenhuma via** — regularizar o banco de horas e administrar o repouso médico. Os 6 itens abertos (P1–P6) continuam pendentes de resposta da cliente e não bloqueiam a conclusão.