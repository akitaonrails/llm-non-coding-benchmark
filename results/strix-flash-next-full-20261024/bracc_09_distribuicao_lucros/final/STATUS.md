# STATUS

**COMPLETE WITH OPEN ITEMS**

## Entregáveis escritos (todos os exigidos pelo CONTRACT.md)
- `parecer.md` — conclusão: **não pode distribuir nada isento em jan/2026** (lucro distribuível = R$ 0: prejuízo de 2025 + prejuízos acumulados + vedação autônoma do art. 32 pela confirmação de débito sem garantia); distribuição de 800 mil geraria IRRF de R$ 80.000 (Lei 15.270) e multas de R$ 400.000 para PJ e R$ 400.000 para beneficiários (art. 32 §1º, dentro do teto de 740 mil), além de responsabilidade solidária (CC 1.009); mútuo **não recomendado** (retirada disfarçada). **§6 (novo): rejeição fundamentada do pedido do Sócio A de registrar os 800 mil como "antecipação de lucros futuros"** — o rótulo não altera nenhum dos quatro filtros (art. 32; IN 1.700 art. 238 §§3º/§4º; Lei 15.270; CC 1.009), e a ECD — longe de "formalidade" — é o que fixa o teto isento em R$ 0.
- `numeros.json` — schema completo; números **inalterados** pela nova demanda (notas `_atualizacao_rodada_cliente` e `_atualizacao_rodada_3`).
- `QUESTIONS.md` / `PERGUNTAS.md` — rodada 1 encerrada (respostas incorporadas); **rodada 2 aberta com Q7–Q9** (histórico de distribuições nas ECDs anteriores; projeção de lucro 2026; conciliação do balanço recebido). Desconhecidos sinalizados: U1–U9.

## Rodada 1 — encerrada
Cliente respondeu: (i) sem ata até 31/12/2025 → transição da Lei 15.270 definitivamente afastada; (ii) débito de 1.480 mil com impugnação de 2024 na DRJ, sem depósito/garantia/parcelamento → "débito não garantido" confirmado; (iii) não dispõe de mais informações para o restante. Nenhuma pergunta foi repetida.

## Rodada 2 — aberta (nova demanda do Sócio A)
- **Q7** — lucros distribuídos escriturados × resultado apurado em cada exercício anterior (ECDs 2022–2024): dimensiona exposição pretérita da prática da contadora anterior.
- **Q8** — projeção de lucro 2026 (informativa; a vedação do art. 32 permanece até garantir o débito).
- **Q9** — divergência no balanço recebido: Passivo + PL somam 10.610.000 contra total declarado de 9.850.000 (diferença de 760.000; Ativo fecha). Achado da revisão pré-entrega; pedimos revalidação do arquivo/balancete.

## Itens abertos (sinalizados explicitamente; não alteram a conclusão)
- **U1** — Valores efetivos de IRPJ/CSLL/PIS/COFINS/ISS e composição dos tributos a recolher (610 mil): limite presumido teórico (1.351.680) permanece ilustrativo e é teto do teto.
- **U2** — Presunção proeminente de que os sócios são PF residentes no Brasil (base da regra dos R$ 50 mil/mês).
- **U3** — Antiguidade dos prejuízos acumulados e plano societário (redução/integralização de capital) para o caminho de volta.
- **U4** — Disposição (não manifestada) para garantir/parcelar o auto de infração antes de distribuições futuras.
- **U5** — Alíquotas IRPJ 25%/CSLL 9% usadas no limite teórico não constam da biblioteca (rotuladas).
- **U6** — Ambiguidade do texto da Lei 15.270: IRRF sobre o total (adotado: R$ 80.000) vs. sobre o excedente (R$ 70.000).
- **U7** — "Antecipação de lucros futuros" não é disciplinada pela biblioteca; requisitos/limites do instituto não verificáveis neste acervo.
- **U8** — Histórico de distribuições anteriores (alegação "a contadora fazia todo ano") e composição anual dos prejuízos: não verificável sem as ECDs; decadência/prescrição fora da biblioteca (Q7).
- **U9** — Divergência documental no balanço recebido (Passivo + PL = 10.610.000 vs. total declarado 9.850.000; diferença de 760.000 não reconciliável com o arquivo enviado). Grandezas usadas na análise estão expressas no documento; conclusão inalterada (Q9).
- Inteiro teor do acórdão CARF 1402-00.xxx e da SC COSIT 30/2016 não está na biblioteca — citados apenas por referência ao arquivo da Lei 4.357.

## Revisão pré-entrega (rodada 4 — auditoria interna)
Verificação de cada citação contra o texto integral dos 5 arquivos da biblioteca e de toda a aritmética (recomputada em Python). Correções aplicadas em `parecer.md` (§5.4: regra de transição da Lei 15.270 restringida a lucros apurados até 2025 — generalização a lucros futuros removida por não ter suporte na biblioteca; §2.3: responsabilidade do contador separada da do administrador do CC 1.009; §4: tributação de juros recebidos rotulada como fora da biblioteca; §5.2/§3: vocabulário alinhado a "garantia integral do débito"; §6.1: citação do inciso I verbatim; §5.5: asserção de rigor suavizada; U6 reescrito) e rotulagem de novo achado factual (**Q9/U9**: balanço recebido não fecha internamente — diferença de 760.000). **Nenhum número do `numeros.json` mudou** (apenas nota `_observacao_documento` adicionada).

Nenhuma conclusão depende desses itens: **distribuição recomendada = R$ 0; mútuo = não recomendado; "antecipação de lucros futuros" = rejeitada para janeiro/2026.**
