# STATUS.md — Regime tributário 2026, Vértice Engenharia Consultiva Ltda.

**Status: COMPLETE WITH OPEN ITEMS**

Todos os entregáveis obrigatórios e o opcional estão completos em `workspace/deliverable/`:

| Arquivo | Conteúdo | Situação |
|---|---|---|
| `comparativo.json` | Os 3 regimes, 2026, JSON conforme o `schema` do CONTRACT ✓ | pronto |
| `memorando.md` | Memória de cálculo: premissas (P1–P6), contas dos 3 regimes (§2–4), ponte Simples × Real (§5), resposta ao "mudar em dezembro" + passo a passo (§6), sensibilidade (§7), riscos (§8), itens abertos (§9), fontes (§10) | pronto (revisado) |
| `PERGUNTAS.md` | 5 perguntas ao cliente (P1–P5), opcionais, com impacto de cada resposta | pronto |
| `STATUS.md` | Este arquivo | pronto |

## Resultado principal

**Recomendação: permanecer no Simples Nacional em 2026** — total R$ 948.000,00 (DAS 738.000 + ISS fora 210.000; INSS patronal 0, pois a CPP está no DAS) contra Lucro Real R$ 1.060.690,00 (economia de R$ 112.690,00) e Lucro Presumido R$ 1.111.120,00. Todas as somas conciliam nos detalhes (memorando §2–5); nada foi ajeitado para fechar.

**Resposta ao pedido do sócio:** mudança de regime **com efeitos em dezembro é impossível** — a opção pelo Simples é irretratável no ano e a exclusão por opção só produz efeitos a partir de 1º/01, com pedido até o último dia útil de janeiro (**30/01/2026**) [library/lc123_sublimite_opcao.md, art. 16, §2º e §2º-A]. O crédito do Real é R$ 83.250, e não os R$ 129.500 imaginados pelo sócio (só 900.000 de 1.400.000 de compras geram crédito); mesmo concedendo crédito sobre **100%** das compras, o Real fica R$ 66.440 a pior que o Simples.

## Itens abertos (não impedem a entrega; listados por obrigação)

**Para o cliente (ver `PERGUNTAS.md`, P1–P5):**
1. **P1** — Confirmar o ano de efeitos da eventual saída (leitura adotada: 2026, prazo 30/01/2026; se for 2027, prazo 29/01/2027 e comparativo refeito).
2. **P2** — Se as obras (R$ 630.000) devem ficar no Anexo III (leitura do próprio cliente) ou em Anexo IV, e a folha rateável às obras.
3. **P3** — RAT/FAP vigente (assumimos 28%; faixa 26,8%–28,8% → diferencial de −15.600 a +10.400/ano).
4. **P4** — Confirmar base integral (100%) da receita tributável pelo ISS-SP de 5% e ausência de retenção/benefícios municipais.
5. **P5** — Notas fiscais/contratos das licenças TopSoft, para resguardar o crédito de R$ 18.500.

**Gaps da biblioteca (não são inventáveis; marcados como premissas no memorando):**
1. **Alíquotas do Anexo IV** não constam de `library/` — o efeito de segregar as obras não pôde ser quantificado (premissa P2; memorando §8, risco 1).
2. **Adicional de IRPJ na apuração anual do Lucro Real** não está nos excertos — assumimos apuração anual sem adicional (P5). Na variante trimestral, o adicional (~51.600) deixaria o Real pior que o Presumido por 1.170 e **não altera o ranking** (Simples continua o mais barato).
3. **DAS de dezembro/2025** não recalculado: o excerto do art. 13-A não detalha o tratamento do ISS mês a mês de 2025 (dentro/acima do sublimite); o comparativo cobre apenas o ano-calendário 2026.
4. **Procedimento do portal** para protocolar exclusão: fora da biblioteca, apenas descrito genericamente no passo a passo (§6).
5. **Vigência temporal dos dados:** a decisão foi modelada para o ano-calendário 2026 sobre a projeção do cliente; a data de "hoje" do ambiente (out/2026) não coincide com a janela de decisão implícita nos documentos (balancete encerrado em out/2025). A leitura dos prazos permanece como indicada no memorando: os prazos citados valem se a decisão for tomada para efeitos em 2026; na hipótese de a decisão real ocorrer mais tarde, o prazo de janeiro aplicável à exclusão com efeitos no ano seguinte é o último dia útil de janeiro daquele ano (ex.: **29/01/2027** para efeitos em 2027).

## Robustez

O ranking **Simples 1º / Real 2º / Presumido 3º** se mantém em todas as variações testadas: no melhor caso do Real (crédito integral de 129.500 → 1.014.440), sem o crédito TopSoft (1.079.190), com adicional trimestral no Real (+51.600), com RAT/FAP na ponta da faixa, e para receitas de 2026 entre R$ 4,2 mi e até ~R$ 4,7–4,8 mi (a partir daí o Real venceria; acima de R$ 4,8 mi a permanência no Simples é vedada — memorando §7).
