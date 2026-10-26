Vou revisar tudo sistematicamente: cada citação contra a biblioteca, cada número por aritmética, e a consistência entre arquivos.

Agora vou conferir os fatos contra os documentos, as citações contra a biblioteca e o contrato:

A verificação por Python confirma os achados. Vou ler o JSON completo para a varredura final antes de aplicar as correções:

O JSON está internamente consistente. Vou conferir a numeração das perguntas (Q2/Q3/Q7 citadas no §4) antes de editar:

Agora o JSON e o STATUS:

Validação final — JSON e varredura de consistência entre arquivos:

Revisão de qualidade concluída. Validação final: JSON íntegro (schema ok, soma = total = R$ 317.999,87), nenhum resíduo dos erros, e todas as ocorrências de "P5" agora apontam só para a premissa correta (ambulatório).

## O que foi conferido e confirmado (sem alteração)

**Aritmética (re-verificada em Python):**
- Lapso disciplinar: 20/08→11/10 = **52 dias**; 21/08→11/10 = **51**; 18/09→11/10 = **23 dias** (dispensa pós-ambulatório) — todos corretos.
- DUM ≈ 17/07/2026 (18/09 − 63d ✓) e **DN 23/04/2027 = DUM + 280 exatos** (checado; a data estava certa) → estabilidade até ~23/09/2027 ✓.
- Períodos indenizáveis: 347 dias (gestante) e 599 dias (CIPA) → R$ 90.220,00 e R$ 155.740,00 ✓.
- Verbas: 11.700,00 + 7.150,00 + 16.466,67 + 16.723,20 = **52.039,87**; piso 40.090,27; cenários A/B/C = 227.779,87 / 317.999,87 / 359.599,87; soma do JSON bate com o total ✓.
- 223-G: 23.400/39.000/156.000 = 3/5/20 × 7.800 ✓.

**Autoridade:** todas as citações foram conferidas literalmente contra os 4 arquivos da biblioteca (régua da alínea "k", requisitos (i)–(iv), "justa causa válida afasta / revertida restabelece", Súmulas 244-I/II e 339-I, ADCT 10 II "a"/"b", CLT 165 + parágrafo único, verbas e faixa 5–20 mil + 223-G). Todo ponto fora da biblioteca continua marcado **[NÃO VERIFICADO NA BIBLIOTECA]** e sem ser sustentado.

**Fatos:** datas e conteúdos conferidos item a item contra os 6 documentos (admissão 15/03/2021, salário, post 20/08 22:14, e-mails 21/08 "viu ontem" e 07/10 "soube essa semana", atestado de 9 semanas em 18/09, ata CIPA, prontuário sem advertências, 62h).

## O que foi corrigido

1. **Rótulo de premissa trocado** (`parecer.md` §3.2 e `parecer.json` CIPA): a falta da data de registro da candidatura estava rotulada "P5" (que é a premissa do ambulatório) → corrigido para **P3**.
2. **Faixa divergente** (§5): "passivo estimado entre **R$ 142 mil** e R$ 360 mil" não reconciliava com o piso demonstrado no §4.4 → corrigido para **R$ 130 mil–R$ 360 mil**, com remissão explícita à faixa R$ 130.310,27–359.599,87.
3. **Contagem de dias** (§2.3): "07/10 (47 dias depois)" ambíguo — 48 dias após a ciência de 20/08 (47 apenas a partir do e-mail de 21/08) → explicitado: "48 dias após a ciência de 20/08; 47 após o e-mail de 21/08".
4. **Duração do contrato exagerada** (§2.4 e JSON motivo 3): "5 anos e 7 meses" não é afirmativa do prontuário (que sequer registra duração) e da margem; o cálculo exato é **5 anos, 6 meses e 26 dias** (15/03/2021→11/10/2026) → substituído com as datas. (O aviso de 45 dias usa 5 anos completos e não muda.)
5. **Referências cruzadas órfãs** (§4.1): "pergunta Q2" e "(Q3)" não existem mais na tabela atual do `QUESTIONS.md` → substituídas pelos nomes dos itens ("Espelho de férias", "Extrato analítico do FGTS"). "Q7" foi mantido (bata com o item respondido sobre as horas).
6. **Refê** (§2.3): "ciência anticipada" → "antecipada".
7. **Trecho escuro** (§7.2): "gratuidade do fundamento fático" → "veracidade do fato narrado no post (62h lançadas no banco e não pagas)".
8. **Expressão inadequada** (§8.2): "para a CIPA vale o mesmo espelho" → "o mesmo raciocínio".
9. **Cabeçalhos** de `parecer.md` e `STATUS.md`: atualizados para Revisão 4, registrando a revisão de qualidade e que **nenhum valor mudou**.

## O que permanece sinalizado (deliberadamente, não são erros)

- Premissas **P1–P7** (dispensa não aplicada; avos/projeção; datas CIPA; DUM ±2 semanas; ambulatório; férias 1 vencido + 7/12; sem reintegração no cenário indenizatório).
- Valores não fecháveis: férias entre R$ 6.066,67–58.066,67; FGTS como piso sem correção; 62h ilustrativas (R$ 2.418–3.627) **excluídas dos totais**; alternativa não cumulativa das estabilidades (155.740,00) registrada à parte.
- Conceitos fora da biblioteca continuam rotulados e não sustentados (tolerância de imediatidade, reflexos, 477 §8º, banco de horas, art. 4º da Lei 9.029, 484-A, critério de inviabilidade da reintegração).

Conclusão e todos os números permanecem: **justa causa incabível**; exposição central **R$ 317.999,87** (faixa R$ 130.310,27–359.599,87). Os quatro entregáveis estão prontos para entrega.