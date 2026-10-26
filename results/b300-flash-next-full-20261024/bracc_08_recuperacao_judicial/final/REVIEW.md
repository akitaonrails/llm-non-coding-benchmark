# Revisão pré-entrega — changelog

**Escopo da revisão (todas as sessões):** (1) releitura integral de `documents/`, `library/` (os 4 arquivos) e dos 10 arquivos de `deliverable/`; (2) validação aritmética por script Python — 31 verificações, todas aprovadas (somas da relação de credores, classes, caixa do demonstrativo mensal, ganho de deságio, D=C nos lançamentos, fechamento pós-plano); (3) varredura de citações: todo "art./lei/CTN/CPC" citado em `deliverable/` confrontado com os textos efetivos da biblioteca; (4) revalidação dos 3 JSONs (schema CONTRACT + somas) após as correções.

**Princípio aplicado:** a biblioteca é a única autoridade citável (CONTRACT, linha 15–16). O que não está nela é marcado **não verificado** e nunca vira fundamento. Nenhuma mudança numérica foi necessária ou feita.

## Correções aplicadas (4 arquivos, 5 edições)

1. **`sessao2/analise_plano.md` (Cláusula 1, risco)** — texto citava "arts. 57-58" como base para não homologação, mas a biblioteca traz o art. 57 (nota: concessão exige certidões) e **não traz o corpo do art. 58** (só o lista no cabeçalho/INDEX). Corrigido para: art. 57 como risco verificado (concessão depende de quitação fiscal); requisitos de assembleia/art. 58 marcados **não verificado** (remissão à Cláusula 6, onde o art. 58 já estava sinalizado).

2. **`sessao2/analise_plano.md` (Cláusula 2, ressalva iii)** — afirmava que a ME/EPP "vota em classe própria" sem suporte documental na biblioteca. A Classe IV vem da relação de credores do cliente (fato), mas a **mecânica de votação por classe não consta da biblioteca** — agora sinalizado.

3. **`sessao1/classificacao_creditos.json` (fundamento do Fornecedor Sul)** — mesma questão: "votará em classe própria na assembleia" virou "votação por classe própria na assembleia: mecânica não consta da biblioteca — não verificado". Classificação (Classe IV) e demais campos inalterados; JSON revalidado.

4. **`sessao1/addendum_sinal_norte.md`** — o texto qualificava cada pagamento como "ato isolado **nulo/fraudulento**". A nulidade civil do ato é conclusão jurídica plausível, mas **não está na biblioteca**; o que está verificado são o **crime de favorecimento (art. 172)**, o **afastamento dos administradores (art. 64)** e a **convolação em falência** (nota final dos excertos). Reescrito como "ato atacável", listando os efeitos verificados e sinalizando a nulidade como não verificada — conclusão (não pagar) inalterada.

5. **`STATUS.md` (contagem)** — linha de status dizia "8 entregáveis"; o contrato exige **7** e `deliverable/` contém 10 arquivos (7 + 2 adendos + notas). Corrigido para "7 exigidos + 3 adicionais = 10".

## Conferido e considerado correto sem alteração

- **Aritmética (31/31 verificações Python aprovadas):** total credores 13.540.000; concursais 7.430.000 (960.000 + 4.200.000 + 1.850.000 + 420.000); caixa 820.000 + 5.770.000 − 5.750.000 = 840.000; ganho 0,60 × 6.470.000 = 3.882.000 = 3.630.000 (id 1) + 252.000 (id 2); novo passivo 40% = 2.588.000 (2.420.000 + 168.000); D=C em todos os lançamentos firmes (6.050.000 / 420.000 / 960.000 / 2.700.000); pós-plano 3.548.000 + 2.700.000 + 3.100.000 = 9.348.000; redução 4.192.000 = 3.882.000 + 310.000; vias A/B/C do passivo federal (22.500 = 2.700.000/120; 810.000 = 30% × 2.700.000; 1.890.000/84 = 22.500; 6.750 = 810.000/120); PF pleno p/ offset total + Via B = 4.692.000.
- **Citações sensíveis confirmadas como sustentáveis:** arts. 42/58 da Lei 8.981/95 e 15/16 da Lei 9.065/95 são citáveis **porque aparecem literalmente no corpo do art. 50-A da biblioteca** (citação por remissão interna); LRF art. 59 (novação) é citável pelo cabeçalho do verbete CPC 48 (`cpc_contabil_rj.md`); a referência a "art. 52" em `passivo_fiscal_solucao.md` aponta para a **decisão judicial do cliente** (que invoca art. 52 e art. 6º §4º), não para corpo normativo inexistente na biblioteca — mantida.
- **Já sinalizados como não verificados (nada a corrigir):** art. 66 (autorização de pagamento), art. 58 (quóruns), art. 60-A (UPI), art. 7º III, CPC 32 (tributos diferidos), alíquotas de IRPJ/CSLL (~34%, ilustrativo), restrições pós-2024 à compensação, critérios internos da Portaria PGFN 2.382/2021 além do teto 70%/120, honorários do AJ.
- **Schema/estrutura:** os 3 JSONs passam nos schemas do CONTRACT; o lançamento id 5 do arquivo de lançamentos é **condicional por construção** (valores `null` — valor contábil do galpão desconhecido), corretamente sinalizado no próprio arquivo, não um erro de D≠C.

## O que permanece aberto (não é erro; são desconhecidos documentais do cliente)

Ver `QUESTIONS.md` — saldo de prejuízo fiscal; data exata do pedido; semanas 5–13 do fluxo; abertura dos R$ 5,75 mi; pessoas ligadas (art. 50-A, único); trabalhistas individualizados/Simples da Sul; valor contábil e regime da UPI; taxa de desconto do plano (mensuração a valor presente pelo CPC 48 — registrado no nominal); % efetivo de transação PGFN e encargos do parcelamento. Nada foi forçado a fechar.
