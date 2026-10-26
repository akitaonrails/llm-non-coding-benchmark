# Memorando — Regime tributário 2026: Simples Nacional × Lucro Presumido × Lucro Real
**Cliente:** Vértice Engenharia Consultiva Ltda. · **Data:** 24/10/2026 (base documental: balancete 12m encerrado out/2025)
**Pergunta do sócio:** sair do Simples **em dezembro** e migrar para o Lucro Real porque "credita tudo".

## Resposta executiva (TL;DR)
1. **A mudança em dezembro é impossível.** A permanência no Simples é irretratável por todo o ano-calendário e a exclusão por opção comunicada depois do último dia útil de janeiro só vale a partir de 1º/01 do ano seguinte ([lc123_sublimite_opcao.md], LC 123/2006, art. 16, §2º e §2º-A). O efeito mais cedo possível seria **01/01/2026**, e para isso a comunicação teria de ser feita **até 30/01/2026** (último dia útil de janeiro de 2026 — 31/01/2026 cai em sábado).
2. **A conta não favorece o Lucro Real — nem Presumido.** Estimativa 2026 (receita R$ 4,2 mi): **Simples R$ 916.500** · **Presumido R$ 1.079.620** · **Real R$ 1.080.790**. Lucro Real custaria **~R$ 164 mil a mais** que ficar no Simples.
3. **"Credita tudo" é falso.** Pelas fontes da biblioteca, material de uso e consumo, mobiliário e veículos administrativos **não geram crédito** ([pis_cofins_nao_cumulativo.md]): dos R$ 1,4 mi de compras, só R$ 900 mil (insumos) creditam → crédito de **R$ 83.250** contra débito de **R$ 388.500**. E fora do Simples nasce uma despesa nova: **CPP patronal ≈ R$ 364 mil** ([inss_patronal.md]) — dentro do Simples ela já está dentro do DAS.
4. **O que de fato muda em 2026 (gostemos ou não):** a receita de R$ 4,2 mi **ultrapassa o sublimite de R$ 3,6 mi**, e o excesso (R$ 600 mil = 16,7%, ≤ 20%) faz **ICMS e ISS saírem do DAS a partir do ano seguinte**, i.e., 2026 ([lc123_sublimite_opcao.md], art. 13-A). A empresa **continua no Simples** para os demais tributos (receita ≤ R$ 4,8 mi, art. 3º, II).

---

## 1. Base factual (documents/)
| Item | Valor | Fonte |
|---|---:|---|
| Receita bruta 12m (= projeção 2026, "estável") | 4.200.000 | balancete_12m_resumo.md |
| — obras c/ emprego de materiais (EPC) | 630.000 | balancete |
| — serviços de engenharia consultiva | 3.570.000 | balancete |
| Folha + pró-labore + encargos + FGTS | 1.300.000 | balancete |
| Compras totais | 1.400.000 | balancete; confere com compras_icms_st.csv (420+280+200+180+220+100) |
| — insumos/materiais (obras e serviços) | 900.000 | balancete; CSV: aço 420k + cabos 280k + licenças CAD/BIM 200k ("insumo") |
| — uso e consumo admin., mobiliário, veículos | 500.000 | balancete; CSV: mobiliário 180k + veículos 220k + papelaria 100k (todos "não" destacam ST; veículos = "ativo (admin)") |
| Lucro contábil antes de IRPJ/CSLL (proj. Real) | 756.000 | balancete |
| Fator R | 1.300.000 ÷ 4.200.000 = **30,95%** (≥ 28% → Anexo III) | cálculo próprio sobre balancete |
| ISS SP | 5% | balancete |
| ICMS-ST destacado nas compras | 700.000 (aço 420k + cabos 280k) | compras_icms_st.csv |

### 1.1 Resposta do cliente (2ª rodada do engajamento)
> "Uns 15% do faturamento é obra pequena com material; o resto é consultoria."

- **Confere exatamente com o balancete**: 15% × 4.200.000 = **630.000** (obras) e 85% = **3.570.000** (consultoria) — os números usados em todos os cenários. **Nenhum recálculo foi necessário**; `comparativo.json` permanece válido.
- O cliente informou **não ter mais informação** sobre as demais perguntas. A caracterização fiscal das obras (ISS × ICMS), a base da CPP, a segregação Anexo IV e os ajustes do Real passam a **desconhecidos definitivos**, sinalizados no §7 e no STATUS — não são mais "perguntas em aberto", são limitações documentais do engajamento.

## 2. Cenário A — Simples Nacional (recomendado)
- Empresa segue EPP: 4,2 mi ≤ 4,8 mi (LC 123, art. 3º, II — `lc123_sublimite_opcao.md`). **Não há exclusão do Simples.**
- **DAS — Anexo III, 6ª faixa** (`anexo_iii_faixa6.md`): alíquota efetiva = (RBT12 × 33% − 648.000) ÷ RBT12
  = (4.200.000 × 0,33 − 648.000) ÷ 4.200.000 = 738.000 ÷ 4.200.000 = **17,5714%** → **DAS = R$ 738.000**.
  A repartição dessa faixa traz **ISS 0%** (ISS sai do DAS acima do sublimite) e **CPP 30,5%** (logo, INSS patronal **não** é cobrado à parte — `inss_patronal.md`: nos Anexos I, II, III e V a CPP está no DAS, art. 13, VI).
- **ISS fora do DAS** (art. 13-A + nota da 6ª faixa): premissa P3 — 5% × 3.570.000 (serviços consultivos) = **R$ 178.500**.
- **CPP à parte: R$ 0.**
- **Total A = 738.000 + 178.500 = R$ 916.500** (carga efetiva 21,8% da receita).

## 3. Cenário B — Lucro Presumido
Presunções e alíquotas de `lei9249_9430_presumido.md` (Lei 9.249, arts. 15 e 20):
- Base IRPJ: obras c/ materiais 8% × 630.000 = 50.400; serviços 32% × 3.570.000 = 1.142.400 → **1.192.800**.
  IRPJ = 15% × 1.192.800 = 178.920 + adicional 10% × (1.192.800 − 240.000) = 95.280 → **274.200** (limite R$ 240.000/ano).
- Base CSLL: 12% × 630.000 = 75.600 + 32% × 3.570.000 = 1.142.400 → 1.218.000 × 9% = **109.620**.
- PIS/COFINS cumulativos: (0,65% + 3,00%) × 4.200.000 = **153.300** (sem créditos).
- ISS: 5% × 3.570.000 = **178.500**.
- CPP fora do Simples ≈ 28% × folha (premissa P1): 0,28 × 1.300.000 = **364.000**.
- **Total B = 274.200 + 109.620 + 153.300 + 178.500 + 364.000 = R$ 1.079.620** (+ R$ 163.120 vs Simples).

## 4. Cenário C — Lucro Real ("credita tudo")
- IRPJ: 15% × 756.000 = 113.400 + adicional 10% × (756.000 − 240.000) = 51.600 → **165.000**.
- CSLL: 9% × 756.000 = **68.040** (premissa P4: lucro contábil = base, sem ajustes no library).
- PIS/COFINS não cumulativos (1,65% + 7,6% = 9,25%, `pis_cofins_nao_cumulativo.md`):
  - Débito: 9,25% × 4.200.000 = **388.500**.
  - Crédito: só **insumos** (critério essencialidade/relevância, REsp 1.221.170/PR): 9,25% × 900.000 = **83.250**.
  - **Sem crédito** (expressamente na fonte): uso e consumo administrativo, material de escritório, **mobiliário e veículos da área administrativa** (180k + 220k + 100k = 500k) e mão de obra pessoa física. Não há máquinas/equipamentos de produção listados, logo crédito por depreciação = 0.
  - Líquido: 388.500 − 83.250 = **305.250** (vs 153.300 no cumulativo — a "economia de crédito" é negativa aqui).
- ISS: **178.500**. CPP: **364.000** (P1).
- **Total C = 165.000 + 68.040 + 305.250 + 178.500 + 364.000 = R$ 1.080.790** (+ R$ 164.290 vs Simples).
- Detalhe que derruba o argumento do amigo contador: o adicional de IRPJ existe nos dois regimes; e o ICMS-ST destacado (700k) geraria no máximo crédito de **PIS/COFINS sobre a parcela de insumo** já considerada — a biblioteca não traz regra de crédito/ressarcimento de ST (ver item 7).

## 5. Comparativo
| | Simples | Presumido | Real |
|---|---:|---:|---:|
| IRPJ | dentro do DAS | 274.200 | 165.000 |
| CSLL | dentro do DAS | 109.620 | 68.040 |
| PIS/COFINS | dentro do DAS | 153.300 | 305.250 (388.500 − 83.250) |
| ISS | 178.500 (fora do DAS) | 178.500 | 178.500 |
| CPP/INSS patronal | dentro do DAS (0) | 364.000 | 364.000 |
| DAS | 738.000 | — | — |
| **Total** | **916.500** | **1.079.620** | **1.080.790** |

**Sensibilidade (o resultado é robusto):**
- **CPP menor:** os R$ 1,3 mi incluem encargos e FGTS, que não são base de CPP. Mesmo depurando para ~R$ 904 mil de remuneração "pura" (CPP ≈ 253 mil), Presumido ≈ 968,7 mil e Real ≈ 969,9 mil ainda perdem. O *break-even* é CPP ≤ ~R$ 200 mil (base ≤ ~R$ 715 mil) — improvável sem confirmação, mas é o único furo que mudaria o ranking. (PERGUNTAS.md Q1.)
- **Obras também tributadas por ISS 5%** (em vez de ICMS): Simples 948.000; Presumido 1.111.120; Real 1.112.290 — Simples continua vencedor.
- Se as obras (EPC c/ materiais) caírem no **ICMS**, todos os regimes pagariam ICMS fora do Simples sobre os 630 mil (alíquota não está na biblioteca — não calculável); como o efeito é idêntico nos três cenários, não altera o ranking.

## 6. Cronograma / passo a passo
**Recomendação: permanecer no Simples Nacional em 2026.** Nada comunicar (a permanência é automática); mas **cumprir a saída de ICMS/ISS do DAS desde 01/01/2026** (art. 13-A): inscrição/recolhimento normal de ISS SP (5% sobre os serviços) e ICMS estadual sobre as receitas cobertas, com obrigações acessórias próprias.
**Se, ainda assim, o sócio quiser sair do Simples** (o que custa +~R$ 160 mil/ano):
1. Comunicar a exclusão por opção **até 30/01/2026** (último dia útil de janeiro; 31/01 é sábado) → efeitos desde 01/01/2026 (art. 16, §2º-A). Comunicação posterior = só 01/01/2027; em dezembro de 2025, nada produz efeito no exercício em curso (opção irretratável, §2º).
2. Presumido: a opção se formaliza com o **pagamento da 1ª quota do 1º período de apuração** e é **definitiva pelo ano todo** (Lei 9.430/96, art. 26 — `lei9249_9430_presumido.md`). Real: apuração de ofício se não houver opção pelo Presumido; mechanicamente os dois se amarram ao início do ano-calendário (a regra específica do Real para 2026 **não está na biblioteca** — não verificado).
3. Antes de decidir: responder Q1–Q4 de PERGUNTAS.md (base de CPP, natureza fiscal das obras, segregar Anexo IV, depreciações/energia/locação p/ créditos).

## 7. Premissas (P) e riscos/pendências (R) — pós-resposta do cliente
- **P1 — CPP 28% × R$ 1,3 mi (desconhecido definitivo):** o balancete agrega folha + pró-labore + encargos + FGTS; a base real da CPP é só a remuneração (Lei 8.212, art. 22 — `inss_patronal.md`). Usei o valor agregado (superestima a saída do Simples). Break-even no §5 (CPP ≤ ~R$ 200 mil). **Perguntado (Q1); o cliente não dispõe da informação** → mantém-se a premissa conservadora e o break-even como salvaguarda do ranking.
- **P2 — RBT12 2026 = 4,2 mi** e repartição 630k/3.570k ("projeção estável"; repartição **confirmada pelo cliente**: 15% obras / 85% consultoria = exatamente os valores usados). Como a alíquota efetiva do Simples usa RBT12, o DAS de dez/2025 sobe gradualmente com o acumulado — mas isso não abre opção de sair no meio do ano.
- **P3 — ISS fora do DAS sobre os 3.570k de consultivos (5%) (caracterização das obras = desconhecido definitivo):** as obras 630k ("obra pequena com material", dizeres do cliente) foram tratadas como lato sensu ICMS (EPC c/ materiais; compras com ST destacado); o ICMS sobre elas não é calculável (sem alíquota na biblioteca). O cliente **não informou** se o município ou o estado as tributa → os dois cenários alternativos estão quantificados no §5 (ISS sobre tudo: Simples 948 mil, ainda vencedor; ICMS: acréscimo idêntico nos três regimes, neutro no ranking).
- **P4 — Lucro Real: lucro contábil informado (756k) = base de IRPJ/CSLL (desconhecido definitivo)**, sem adições/exclusões nem créditos extras de PIS/COFINS (energia, locação, depreciação de máquinas de prestação); não há demonstrativo no library e o cliente não tem mais informação. Isso só refina o cenário C, que já perde por R$ 164 mil.
- **R1 — Pendência de conformidade relevante (desconhecido definitivo):** a receita de obras c/ emprego de materiais deveria ser **segregada no Anexo IV** (LC 123, art. 18, §4º, IV — `lc123_sublimite_opcao.md`), cujo DAS **não embute a CPP** (`inss_patronal.md`: "fora do Simples **ou no Anexo IV**" paga-se patronal à parte). Perguntado se a empresa segrega hoje (Q3): **sem resposta** — e o **quadro de alíquotas do Anexo IV não consta do library**, então o cenário alternativo não é calculável daqui. Deixo **em aberto, não conciliado**: se tudo sempre somou no Anexo III, pode haver subrecolhimento de CPP/tributos pretéritos (exposição não quantificada). Recomendo ao sócio uma revisão de conformidade Anexo III × IV dos últimos 5 anos como ação separada.
- **R2 — Crédito de ICMS-ST na base de PIS/COFINS** e exclusão de ICMS da base de contribuição: fora do library → não calculado, tratado como **não verificado**.
- **R3 — Reversão de créditos** ao migrar de regime / saída de itens do ativo: não verificado (não está no library).
- **R4 — Calendário exato da exclusão no e-CAC/DASNIT** e efeitos práticos do art. 13-A "mês seguinte" se 2026 estourar o sublimite em >20% (receita > 4,32 mi): regras detalhadas não constam do library; usei apenas os excertos citados.
- Não inventei nada fora de `library/INDEX.md`; afirmações sem lastro ali estão rotuladas "não verificado" acima.

## 8. Fontes citadas (todas em library/INDEX.md)
`lc123_sublimite_opcao.md` · `anexo_iii_faixa6.md` · `lei9249_9430_presumido.md` · `pis_cofins_nao_cumulativo.md` · `inss_patronal.md`

---

## Anexo A — Rodada 3: "o amigo disse que basta pedir no portal" e "abrir outra empresa"

### A.1 Pedido de exclusão no portal em dezembro — o amigo confunde protocolar com ter efeito
A library é explícita (LC 123/2006, art. 16, §2º e §2º-A — `lc123_sublimite_opcao.md`): a exclusão por opção comunicada **até o último dia útil de janeiro** produz efeitos desde **1º de janeiro do mesmo ano**; comunicada depois, **só a partir de 1º de janeiro do ano seguinte**. A opção pelo Simples é **irretratável por todo o ano-calendário**. Não existe, nas fontes deste engajamento, nenhum mecanismo — portal ou papel — que produza efeito **em dezembro**: o melhor cenário jurídico é 01/01 do ano seguinte.
- Se o "dezembro" em questão é dez/2025 (data do e-mail/balancete): pedido em dez/2025 → efeitos 01/01/2026, comunicação até 30/01/2026.
- Se a pergunta vale para dez/2026 (data de hoje): efeitos 01/01/2027, comunicação até **29/01/2027** (31/01/2027 é domingo). **Sinalizado: as datas-base do contrato (12m out/2025) e a data de hoje não fecham — confirmar a que dezembro o sócio se refere (Q6).**
- E a premissa oculta dele — "a alíquota alta de dezembro" — também não se sustenta: a alíquota **efetiva** do Simples na 6ª faixa é **17,57%** (33% nominal menos parcela a deduzir de R$ 648 mil — `anexo_iii_faixa6.md`). Sair do Simples **aumenta** a carga sobre a receita de dezembro para ~25,7% (Presumido: 1.079.620/4.200.000; Real idem na prática), não reduz.

### A.2 "Abro outra empresa no Lucro Real e faturam dezembro por ela" — perde na conta E no risco
**Na conta (mesmo sem considerar risco nenhum), é prejuízo.** Dezembro típico ≈ 4.200.000 ÷ 12 = **R$ 350 mil** de receita, folha do mês ≈ R$ 108 mil. Baseline: ficar no Simples custa DAS 17,57% × 350 mil = **61,5 mil** (ISS comparável dos dois lados, fora da diferença):

| Configuração | Tributos de dezembro na "empresa nova" | Δ vs. ficar no Simples |
|---|---|---:|
| Folha migra p/ a nova; lucro proporcional | PIS/COFINS 9,25%×350k = 32,4 mil + CPP 28%×108k = 30,3 mil + IRPJ/CSLL sobre lucro proporcional ~19,4 mil | **+20,6 mil** |
| Lucro "zerado" na nova (créditos ≈ 0, sem insumos próprios em dez.) | 32,4 + 30,3 = 62,7 mil | **+1,2 mil** — e a "economia" evapora com custos de abrir/manter a PJ |
| Folha fica na Vértice → receita de 350 mil sem custo na nova = lucro fantasma | PIS/COFINS 32,4 mil + IRPJ 15% + adicional 10% e CSLL 9% ≈ 117 mil (+ CPP que não desaparece na antiga) | **≈ +118 mil** |

A "empresa nova" no Real nasce sem insumos próprios → créditos PIS/COFINS ≈ 0 (`pis_cofins_nao_cumulativo.md` exige insumo da atividade-fim), e a CPP de 28% sobre a folha passa a correr à parte (`inss_patronal.md`) — exatamente a despesa que mantém o Real caro o ano inteiro (memorando §4). Não há dezembro que compense.

**No risco (rotulado como NÃO VERIFICADO):** a **library não contém** normas antifraude/antielisão (nada equivalente a dispositivo antiabusivo, regra de simulação ou desconsideração está no INDEX). Portanto **não posso citar** a base legal que tornaria a operação indevida; digo expressamente: **minha avaliação profissional, sem fonte verificada neste engajamento (não verificado)**, é que faturar via PJ recém-aberta, sem estrutura própria, receita que é da Vértice (clientes, contratos e profissionais dela) é operação classificável como simulação/desvio de receita, com risco tributário e trabalhista — e ainda criaria segmentação artificial de receita/Fator R no futuro. **Não recomendo e não estruturo essa operação.** O caminho lícito existe e está no memorando: exclusão comunicada até o último dia útil de janeiro, com efeitos em 1º de janeiro — que, aliás, a própria conta desaconselha (Simples 916,5 mil < Presumido 1.079,6 mil < Real 1.080,8 mil).

### A.3 O que o sócio ganha ao não fazer nada
Ficar no Simples: carga ~21,8% (916,5/4.200.000), alíquota efetiva de 17,57% sobre o DAS (a dedução da 6ª faixa derruba os 33% nominais que ele teme), e a única providência obrigatória: recolher **ISS/ICMS fora do DAS desde 01/01** (art. 13-A — excesso de sublimite de 16,7% ≤ 20% → efeitos do ano seguinte).

**Q6 (pergunta da rodada 3, encerrada na rodada 4 como desconhecido definitivo):** o "dezembro" do pedido era dez/2025 (janela de exclusão para efeitos em 01/01/2026, até 30/01/2026) ou dez/2026 (efeitos 01/01/2027, até 29/01/2027)? Os documentos (12m encerrado out/2025) e a data de hoje (24/10/2026) não coincidem, e o cliente informou **não ter mais informação** — a pergunta não foi respondida. Como as duas leituras mantêm **todas** as conclusões (dezembro impossível; Simples vencedor em todos os cenários; ISS/ICMS fora do DAS), `comparativo.json` registra **2026-01-30** — a janela do exercício de 2026, enquadramento definido no contrato — e a variante **29/01/2027** fica documentada acima para o caso de o sócio estar falando de dez/2026.
