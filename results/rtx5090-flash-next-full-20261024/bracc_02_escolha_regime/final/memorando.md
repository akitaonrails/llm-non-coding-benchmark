# Memorando — Regime tributário 2026 — Vértice Engenharia Consultiva Ltda.

**Para:** Hélio Vértice (sócio)
**Data:** 24/10/2026
**Assunto:** Conta dos três regimes para 2026 (RBT12 projetado R$ 4.200.000) e resposta ao pedido de "sair do Simples em dezembro e ir para o Lucro Real".

---

## 1. Resposta executiva ao pedido

1. **A mudança em dezembro é impossível.** A opção/exclusão do Simples Nacional produz efeitos a partir de 1º de janeiro do ano-calendário e é **irretratável por todo o ano** (LC 123/2006, art. 16, §2º — `library/lc123_sublimite_opcao.md`). Comunicada a exclusão depois do último dia útil de janeiro, ela só vale **a partir de 1º de janeiro do ano seguinte** (§2º-A). Ou seja: comunicado em dez/2026, o novo regime começaria em **01/01/2027** — dezembro/2026 continuaria no Simples de qualquer forma. Não existe "sair em dezembro para não pagar a alíquota de dezembro".
2. **O Lucro Real não paga menos neste caso.** A premissa do contador ("credita tudo que compra": 9,25% sobre R$ 1,4 mi) está errada: **R$ 500 mil das compras são uso e consumo administrativo, mobiliário e veículos administrativos, que NÃO geram crédito** (Lei 10.637/02, art. 3º; Lei 10.833/03, art. 3º; IN RFB 2.121/2022, arts. 175-176 — `library/pis_cofins_nao_cumulativo.md`). Créditos reais: R$ 900 mil × 9,25% = **R$ 83.250** (não R$ 129.500). PIS/COFINS não cumulativo fica em **R$ 305.250**, contra **R$ 153.300** do cumulativo no Presumido. No Real a carga total projetada é a **maior** das três: **R$ 1.080.790** (25,73% efetivos) vs. **R$ 908.460** no Simples (21,63%).
3. **Vocês não estouraram o limite do Simples.** O limite (RBT12) é **R$ 4,8 mi** (LC 123, art. 3º, II). Com R$ 4,2 mi vocês estão **dentro** do limite, mas **acima do sublimite de R$ 3,6 mi** de ICMS/ISS (art. 13-A). Consequência correta: o **ISS passa a ser recolhido fora do DAS**, pelas regras normais — foi isso que gerou a sensação de "alíquota alta". O remédio não é trocar de regime.
4. **Recomendação: permanecer no Simples Nacional (Anexo III + Anexo IV segregado).** Economia projetada de ~**R$ 166 mil/ano** vs. Presumido e ~**R$ 172 mil/ano** vs. Real. Atenção ao gatilho: se a RBT12 **ultrapassar R$ 4,8 mi**, haverá exclusão obrigatória (regras de retroatividade por excesso — art. 26 da LC 123 — **não constam da biblioteca**; ver §6, item U5).

---

## 2. Dados usados (arquivo do cliente)

De `documents/balancete_12m_resumo.md` (12 meses encerrados em out/2025; projeção 2026 estável) e `documents/compras_icms_st.csv`:

| Item | Valor (R$) |
|---|---:|
| Receita bruta 12m (RBT12) | 4.200.000 |
| — obras com emprego de materiais (EPC) | 630.000 |
| — serviços de engenharia consultiva | 3.570.000 |
| Folha + pró-labore + encargos + FGTS | 1.300.000 |
| Compras totais | 1.400.000 |
| — insumos/materiais de obras e serviços (aço 420k + cabos 280k + licenças CAD/BIM 200k) | 900.000 |
| — uso e consumo admin., mobiliário, veículos (180k + 220k + 100k) | 500.000 |
| Lucro contábil antes de IRPJ/CSLL (projetado p/ Real) | 756.000 |
| Regime atual | Simples, Anexo III (Fator R ≈ 31%) |
| ISS São Paulo | 5% |

Fator R = 1.300.000 / 4.200.000 = **30,95%** — registrado apenas como checagem de consistência: **a regra que vincula Fator R ≥ 28% ao Anexo III não consta da biblioteca** (item U2) e não é usada como fundamento. O enquadramento em **Anexo III** segue a informação explícita do balancete ("Regime atual: Simples, Anexo III").

Segregação de receitas: obras com emprego de materiais → **Anexo IV**; engenharia consultiva → **Anexo III** (LC 123, art. 18, §4º, IV — `library/lc123_sublimite_opcao.md`).

---

## 3. Cálculo — Simples Nacional (recomendado)

**RBT12 = 4.200.000** → dentro do limite (4,8 mi) e na **6ª faixa do Anexo III** (3.600.000,01 a 4.800.000): nominal 33%, dedução R$ 648.000 (LC 123, Anexo III; Res. CGSN 140, arts. 9º-12 — `library/anexo_iii_faixa6.md`).

Alíquota efetiva (fórmula do arquivo):
(4.200.000 × 33% − 648.000) / 4.200.000 = (1.386.000 − 648.000) / 4.200.000 = **17,5714%**

- **DAS — Anexo III (serviços 3.570.000):** 738.000 × (3.570.000 / 4.200.000) = **627.300,00**. Mecânica adotada: a alíquota efetiva apurada sobre a RBT12 total (fórmula transcrita em `anexo_iii_faixa6.md`) aplicada à receita segregada de cada anexo (LC 123, art. 18, §4º, IV). ⚠️ O excerto **não transcreve** os arts. 9º-12 da Res. CGSN 140 que ele cita — esse passo (efetiva da RBT12 aplicada por anexo na segregação) é **inferência** (item U7).
- **DAS — Anexo IV (obras 630.000):** ⚠️ **A tabela do Anexo IV NÃO consta da biblioteca.** Estimativa rotulada como **NÃO VERIFICADA**, aplicando a mesma fórmula da estrutura de faixas com valores nominais de memória ([10,2%; ded. 108.000]): efetiva ≈ (4.200.000 × 10,2% − 108.000)/4.200.000 = 7,629% → ≈ **48.060,00**. **Sensibilidade:** para qualquer alíquota efetiva de Anexo IV entre 0% e 15%, o Simples continua sendo o regime mais barato (o DAS-IV ficaria entre 0 e 94.500). Ver perguntas P1.
- **ISS fora do DAS:** RBT12 (4,2 mi) > sublimite (3,6 mi); excesso = 4,2/3,6 − 1 = 16,7% ≤ 20% → ICMS/ISS fora **a partir do ano seguinte** (art. 13-A). Estando o RBT12 de 12m já em 4,2 mi em out/2025, o ISS de 2026 é fora do DAS. Na 6ª faixa do Anexo III a repartição do DAS tem **ISS 0%** (`anexo_iii_faixa6.md`). ISS SP 5% sobre serviços: 3.570.000 × 5% = **178.500,00**. (Ver premissa A3 sobre as obras.)
- **CPP (INSS patronal) fora do DAS — parcela Anexo IV:** no Simples a CPP está dentro do DAS apenas nos Anexos I, II, III e V; **no Anexo IV a empresa recolhe ~28% sobre a folha** (20% + RAT 1-3% + terceiros ≈5,8%) (LC 123, art. 13, VI e §3º; Lei 8.212/91, art. 22 — `library/inss_patronal.md`). Premissa A2 (rateio proporcional à receita): folha das obras = 1.300.000 × 15% = 195.000 → CPP ≈ 28% × 195.000 = **54.600,00**.
- **DAS Anexo III não tem CPP adicional** — já incluída (art. 13, VI).

**Total Simples ≈ 627.300 + 48.060 + 178.500 + 54.600 = R$ 908.460** (efetivo 21,63%).

---

## 4. Cálculo — Lucro Presumido

Fontes: Lei 9.249/95, arts. 15 e 20; Lei 9.430/96, arts. 1º-4º; Lei 9.718/98 (`library/lei9249_9430_presumido.md`).

**IRPJ (presunção segregada por atividade — premissa A1):**
- Serviços (eng. consultiva): 32% × 3.570.000 = 1.142.400
- Obras com materiais (empreitada): 8% × 630.000 = 50.400
- Base: 1.192.800 → IRPJ 15% = **178.920**
- Adicional 10% sobre o que exceder R$ 60.000/trimestre (apuração trimestral). Com segregação: serviços 285.600/tri − 60.000 = 225.600 × 10% × 4 = **90.240**; obras 12.600/tri < 60.000 → 0. **IRPJ total = 269.160**. (Sem segregação: adicional 95.280 → IRPJ 274.200; carga Presumido sobe para 1.079.620.)

**CSLL (9%):** presunção 32% serviços = 1.142.400; 12% obras = 75.600; base 1.218.000 × 9% = **109.620**

**PIS/COFINS cumulativos (sem crédito):** (0,65% + 3,00%) × 4.200.000 = **153.300**

**ISS:** 5% × 3.570.000 = **178.500** (ver A3)

**CPP:** fora do Simples → ≈28% × 1.300.000 = **364.000** (ver premissa A2/R3)

**Total Presumido = 269.160 + 109.620 + 153.300 + 178.500 + 364.000 = R$ 1.074.580** (efetivo 25,59%)

---

## 5. Cálculo — Lucro Real

**IRPJ sobre lucro real** (lucro contábil antes de IRPJ/CSLL informado = 756.000; premissa A4):
- 15% × 756.000 = 113.400
- Adicional 10% × (756.000 − 240.000/ano) = 10% × 516.000 = 51.600
- **IRPJ = 165.000**

**CSLL:** 9% × 756.000 = **68.040**

**PIS/COFINS não cumulativo** (PIS 1,65% + COFINS 7,6%; `library/pis_cofins_nao_cumulativo.md`):
- Débitos: 9,25% × 4.200.000 = **388.500**
- Créditos — **apenas insumos** (critério da essencialidade/relevância, REsp 1.221.170/PR): aço 420k + cabos 280k + licenças CAD/BIM 200k = 900.000 × 9,25% = **83.250** (ver risco R2)
- **NÃO geram crédito** (usados explicitamente no arquivo): mobiliário 180k, veículos administrativos 220k, material de escritório 100k = 500.000 → crédito zero. O sócio creditou 129.500; o correto é 83.250.
- **PIS/COFINS líquido = 305.250** (vs. 153.300 no Presumido → o Real paga **+151.950** só nesse tributo)

**ISS:** 5% × 3.570.000 = **178.500** (ver A3)

**CPP:** ≈28% × 1.300.000 = **364.000**

**Total Real = 165.000 + 68.040 + 305.250 + 178.500 + 364.000 = R$ 1.080.790** (efetivo 25,73%)

### Comparativo (2026, R$)

| Regime | Total | Efetivo | Δ vs. Simples |
|---|---:|---:|---:|
| **Simples (recomendado)** | **908.460*** | 21,63% | — |
| Lucro Presumido | 1.074.580 | 25,59% | +166.120 |
| Lucro Real | 1.080.790 | 25,73% | +172.330 |

\* inclui estimativa NÃO VERIFICADA do DAS-IV (48.060) — ver §7.

Por que o Real perde: (i) PIS/COFINS não cumulativo ~2× o cumulativo porque a empresa é de serviços com poucos insumos creditáveis; (ii) CPP de ~28% da folha inteira (no Simples, a parcela Anexo III embute a CPP no DAS); (iii) o lucro real 756.000 gera IRPJ/CSLL quase tão altos quanto a presunção.

### 5-bis. Conferência do balancete — "lucro antes de IRPJ/CSLL = 756.000" (item em aberto, não reconciliado)

A linha de lucro do balancete **não fecha integralmente** com as linhas de custo. Registrado, sem forçar ajuste:

- Base: 4.200.000 − 1.400.000 (compras) − 1.300.000 (folha/encargos/FGTS) = **1.500.000** antes de tributos e de custos não listados.
- Para o lucro informado de 756.000 se sustentar, os **tributos embutidos + demais custos não listados** têm de somar exatamente **744.000** (1.500.000 − 756.000).
- **Leituras descartadas por aritmética:**
  - Se 756.000 embutisse a carga **Simples** atual (675.360 + 178.500 + 54.600 = 908.460): demais custos = 1.500.000 − 756.000 − 908.460 = **−164.460** (negativo) → impossível.
  - Se 756.000 embutisse PIS/COFINS do Real (305.250) + ISS (178.500) + **CPP destacada** (364.000, i.e., a CPP somada À PARTE da linha de 1,3 mi de folha): demais custos = 1.500.000 − 756.000 − 847.750 = **−103.750** → impossível.
- **Leitura adotada (A4, sentindo literal de "antes de IRPJ/CSLL"):** 756.000 já desconta PIS/COFINS (305.250) e ISS (178.500), e a **CPP do Real está dentro da linha de folha/encargos** (projeção já a traz nos 1,3 mi) → demais custos não listados = **260.250**. Plausível (o balancete é um resumo gerencial, não uma DRE itemizada), e é a única leitura compatível com o rótulo e com custos não negativos.
- **Sensibilidade do total Real ao LCRI** (PIS/COFINS 305.250 + ISS 178.500 + CPP 364.000 = 847.750 fixos; IRPJ/CSLL sobre o LCRI, 15% + adicional 10% acima de 240.000/ano + 9%):

| LCRI | IRPJ+CSLL | Total Real |
|---:|---:|---:|
| 756.000 (adotado) | 233.040 | **1.080.790** |
| 583.610 | 174.427 | 1.022.177 |
| 392.000 | 109.280 | 957.030 |
| **249.147 (break-even)** | 60.710 | **908.460 = Simples** |

- **Break-even: LCRI = 249.147** (5,93% da receita) contra 756.000 informados (18,0%) — margem de 3×.
- **Resposta à P8 (cliente, rodada 4):** "margem antes de imposto uns 18%" → 18,0% × 4.200.000 = **756.000 exatos**, conferindo com a linha do balancete. A grandeza do lucro está **confirmada** (LCRI 756.000 mantido; nenhum número do comparativo muda). A expressão "antes de imposto" é gerencial e tecnicamente imprecisa; mantemos o rótulo literal do balancete ("antes de IRPJ/CSLL", projetado para o Real). Nota contra a leitura EBIT integral: sob ela, a empresa hoje teria **prejuízo de −152.460** no Simples (1.500.000 − 744.000 demais custos − 908.460 carga Simples), o que contradiz a própria existência de uma "margem" e o balancete — reforça a leitura adotada (A4), sem eliminá-la formalmente (inferência, não norma). **A DRE itemizada não foi fornecida (cliente não tem mais informação)**; o item permanece aberto, agora com a magnitude ancorada nos dois documentos.
- **Único cenário que inverteria o ranking:** se a linha "lucro antes de IRPJ/CSLL" fosse, na verdade, *antes de todos os tributos* (tipo EBIT, com demais custos de 744.000), o LCRI no Real seria negativo (−91.750) → IRPJ/CSLL ≈ 0 → Real = **847.750**, ~60,7 mil **mais barato** que o Simples. Isso contradiz o rótulo do balancete ("antes de IRPJ/CSLL" = somente IRPJ/CSLL já que PIS/COFINS/ISS/CPP despesas acima dessa linha), mas não pode ser integralmente descartado sem a **DRE projetada itemizada** — **item em aberto** (P8 em `QUESTIONS.md`).
- Conclusão: sob qualquer leitura compatível com o rótulo do balancete, o Real perde para o Simples (na adotada, +172.330; nos pontos de sensibilidade, ainda acima do break-even). O ranking só inverte se o rótulo estiver errado.

---

## 6. Premissas e itens NÃO VERIFICADOS (rotulados)

**Premissas (dados/hipóteses de cálculo):**
- **A1.** Segregação das bases de presunção (32%/8% IRPJ; 32%/12% CSLL) e do adicional por trimestre, por atividade segregada contabilmente. Sem segregação, Presumido = 1.079.620.
- **A2.** Rateio proporcional à receita (15% da folha) para a folha das obras, para a CPP do Anexo IV; RAT+FAP não informados → usado o total típico de 28% do arquivo `inss_patronal.md`.
- **A3.** ISS de 5% aplicado somente sobre a receita de engenharia consultiva (3,57 mi). Não aplicamos ISS nem ICMS sobre as obras (630 mil) nem tratamos o ICMS-ST destacado nas compras de aço/cabos — **as regras de incidência de ISS sobre obras (base reduzida?) e de ICMS sobre construção civil não constam da biblioteca**. Se o município exigir ISS sobre as obras, some até 5% × (base) em Simples/Presumido/Real igualmente (não altera o ranking).
- **A4.** Lucro real (LCRI) = 756.000, sem ajustes de adições/exclusões (ocultação de custos e receitas não tributáveis). A base "antes de IRPJ/CSLL" já embute PIS/COFINS/ISS e a **CPP do Real dentro da linha de folha/encargos** (CPP destacada à parte não é conciliável com o balancete — ver §5-bis, onde a conferência aritmética e a sensibilidade estão detalhadas).
- **A5.** RBT12 2026 = 4.200.000 (projeção "estável" do balancete); sublimite já extrapolado em 2025 (RBT12 de 12m em out/2025 = 4,2 mi), com excesso ≤ 20% → ISS fora do DAS desde o início de 2026 (art. 13-A).

**Itens NÃO VERIFICADOS (não constam da biblioteca — não citados como fundamento):**
- **U1.** Tabela de alíquotas do **Anexo IV** (usamos [10,2%/108.000] apenas como estimativa sinalizada).
- **U2.** Regra de escolha Anexo III × V pelo Fator R (o balancete do cliente já informa Anexo III; a regra em si não está na biblioteca).
- **U3.** Prazo de vencimento do DAS e datas de vencimento de DARF/PER/DCOMP.
- **U4.** Regras de ISS/ICMS sobre obras e de crédito sobre ICMS-ST (ver A3).
- **U5.** Consequências de exclusão de ofício/excesso acima do limite (art. 26 da LC 123 — **não incluído nos excertos**): se em 2026 a RBT12 passar de 4,8 mi, os efeitos (inclusive retroativos, se o excesso > 20%) precisam ser verificados em fonte oficial antes de qualquer decisão.
- **U6.** LC 123, arts. 3º, §§ 1º e 9º, 20 e 30 constam da **citação** do arquivo `lc123_sublimite_opcao.md`, mas o texto desses dispositivos **não foi transcrito** no excerto — nada no acervo trata de sucessão/dissimulação/sucessão simulada, tema do plano da "empresa nova" (§8-ter (b)).
- **U7.** Res. CGSN 140, arts. 9º-12 constam da citação de `anexo_iii_faixa6.md`, mas **não foram transcritos** — a mecânica de aplicar a alíquota efetiva apurada sobre a RBT12 à receita segregada de cada anexo (§3) é **inferência**; o excerto confirma apenas a fórmula da efetiva e a repartição interna do DAS.
- **U8.** **Nenhum excerto específico de Lucro Real** na biblioteca — aplicamos ao lucro real as alíquotas gerais do arquivo `lei9249_9430_presumido.md` (IRPJ 15% + adicional 10% acima de 240.000/ano; CSLL 9%); adições/exclusões de LCRI não computadas (A4) e a linha de lucro do balancete não reconcilia integralmente (§5-bis).

---

## 7. Riscos

- **R1 (rank robusto, com ressalva):** a conclusão "Simples < Presumido < Real" se mantém para qualquer DAS-IV plausível (até ~214 mil, efetiva ~34%, o Simples segue abaixo do Presumido) e sem segregação do adicional. No Real, o **break-even contra o Simples é LCRI = 249.147** (5,93% da receita) contra 756.000 informados — margem de 3× (§5-bis). **Ressalva:** se a linha de lucro do balancete for, na prática, *antes de todos os tributos* (rótulo impreciso), o Real cairia para 847.750 e o ranking **inverteria**. A P8 foi respondida só quanto à grandeza (cliente: margem ~18% = 756.000 confirmados); a leitura EBIT integral não foi formalmente excluída, mas implicaria **prejuízo de −152.460 no Simples hoje**, incompatível com o balancete — improvável (§5-bis). Item aberto encerrado como limitado: sem DRE itemizada disponível no cliente.
- **R2 (crédito CAD/BIM):** tratamos as licenças (200k) como insumo essencial ao serviço de engenharia (critério do REsp 1.221.170/PR, citado na biblioteca). Se a RFB negar (uso e consumo), créditos caem para 64.750 e o Real sobe para ~1.099.290 — aumenta a vantagem do Simples.
- **R3 (CPP):** 28% é o "total típico" do arquivo; RAT/FAP reais podem mover ±2 p.p. (~±26 mil) em Presumido/Real e ±4 mil no Simples.
- **R4 (estouro do limite):** se a RBT12 2026 passar de 4,8 mi, a permanência no Simples fica vetada e a exclusão pode ter efeitos retroativos (ver U5). Monitorar mensalmente; a 4,2 mi há folga de 14%.
- **R5 (dezembro):** qualquer "exclusão" comunicada agora só vale de 01/01/2027; comunicar achando que dezembro sai do DAS gera pagamento indevido/auto-exclusão mal formalizada.

---

## 8. Passo a passo para a opção (apenas se o sócio insistir em sair)

1. **Decidir Presumido × Real até jan/2027.** Pelo cálculo, se sair do Simples, o melhor seria **Presumido** (1.074.580 vs. 1.080.790) — mas ambos são piores que ficar no Simples.
2. **Não fazer nada em dezembro:** a exclusão comunicada em dez/2026 produz efeitos a partir de **01/01/2027** (art. 16, §2º-A — `lc123_sublimite_opcao.md`). Dezembro/2026 continua DAS + ISS fora normalmente.
3. **Formalizar a exclusão do Simples** — prazo-limite para efeitos desde **01/01/2027**: comunicar até o **último dia útil de janeiro de 2027 = 29/01/2027** (sex; 31/01/2027 é domingo). Comunicada depois disso, os efeitos só viriam em 01/01/2028.
4. **Presumido:** a opção manifesta-se com o **pagamento da 1ª quota do 1º período de apuração de 2027** (apuração trimestral) e é **definitiva por todo o ano** (Lei 9.430/96, art. 26 — `lei9249_9430_presumido.md`). Data exata de vencimento: U3 (não verificada).
5. **Real:** não há "opção" — é o regime padrão para quem sai do Simples; exige escrituração contábil completa e controle de LCRI, além de registros PIS/COFINS não cumulativo (débito sobre a receita, crédito apenas de insumos/energia/aluguéis/depreciação de máquinas usadas na prestação — `pis_cofins_nao_cumulativo.md`).
6. Em qualquer saída do Simples: implantar recolhimento de **CPP ~28% sobre a folha inteira** (Lei 8.212/91, art. 22) e apuração trimestral de IRPJ/CSLL.

---

## 8-bis. Adendo — resposta do cliente (rodada 2)

O cliente informou que **~15% do faturamento é obra pequena com material e o restante consultoria**, e que **não possui informação adicional** para as demais perguntas (P1-P4, P6-P7).

- A resposta **confirma a premissa A2 de rateio** (proporcional à receita): 15% × 630.000/4.200.000 coincide com o balancete. O rateio da *folha* continua hipótese de trabalho, agora corroborada pelo cliente.
- As incógnitas remanescentes tornam-se definitivas para esta entrega e ficam rotuladas:
  - **U1/A-anexo-IV:** alíquota efetiva do Anexo IV não obtida → DAS-IV ≈ 48.060 é estimativa NÃO VERIFICADA (sensibilidade no §3: qualquer efetiva 0-15% preserva a recomendação).
  - **A5/P2:** mês exato de extravasamento do sublimite não informado; mantida a inferência do balancete (RBT12 = 4,2 mi já em out/2025; excesso 16,7% ≤ 20% → ISS fora do DAS desde jan/2026).
  - **R4/P3:** risco de estouro dos 4,8 mi em 2026 não quantificável pelo cliente; manter monitoramento mensal.
  - **R3/P4:** RAT/FAP não informados; CPP a 28% típico (±2 p.p. ≈ ±26 mil em Presumido/Real).
  - **R2/P6:** natureza das licenças CAD/BIM não esclarecida; crédito mantido com risco sinalizado.
  - **A3/U4/P7:** ISS de obras em SP não verificável na biblioteca; não aplicado sobre os 630 mil (afetaria os três regimes igualmente).
- Nenhum número do comparativo muda.

## 8-ter. Rodada 3 — perguntas do sócio (exclusão no portal em dezembro; nova empresa no Real faturando dezembro)

### (a) "Basta pedir a exclusão no portal em dezembro" — correto quanto ao rito, errado quanto ao efeito

O pedido de exclusão pode ser feito a qualquer momento (é o rito), mas o **efeito** está travado em lei (LC 123/2006, art. 16, §2º e §2º-A — `library/lc123_sublimite_opcao.md`):

- a permanência no Simples é **irretratável por todo o ano-calendário** (§2º);
- exclusão comunicada **depois do último dia útil de janeiro** produz efeitos **somente a partir de 1º de janeiro do ano seguinte** (§2º-A).

Logo, pedir no portal em **dez/2026 = sair em 01/01/2027**. O DAS de dezembro/2026 é devido de qualquer forma. Não há no acervo regra que permita saída no meio do exercício. (Pode existir regra de exclusão por excesso acima do limite — art. 26 da LC 123 — mas **não consta da biblioteca** (U5), e de todo modo não se aplicaria: vocês não estouraram os 4,8 mi. Não afirmamos que ela seria "a única" saída retroativa do sistema — simplesmente nada mais consta do acervo que permitisse saída no meio do exercício.) E não vale a pena nem se pudesse: no mês de dezembro o Simples custa **R$ 75.705** contra **R$ 90.066** no Real (cálculo abaixo).

### (b) "Abrir outra empresa no Lucro Real e faturar dezembro por ela"

**1. Pelo próprio cálculo, é pior.** dezembro ≈ 1/12 do RBT12 = R$ 350.000 (85% consultoria / 15% obras):

| | Simples (Vértice) | Real (qualquer empresa) |
|---|---:|---:|
| IRPJ/CSLL | dentro do DAS | 13.750 + 5.670 (lucro proporcional) |
| PIS/COFINS | dentro do DAS | 32.375 débito − 6.938 crédito = **25.438** |
| ISS | 14.875 (fora do DAS) | 14.875 |
| DAS-III (297.500 × 17,5714%) | 52.275 | — |
| DAS-IV estimado (52.500 × 7,63%)* | 4.005 | — |
| CPP folha obras (16.250 × 28%) | 4.550 | 30.333 (CPP ~28% da folha inteira) |
| **Total dezembro** | **75.705 (21,6%)** | **90.066 (25,7%)** |

\* estimativa NÃO VERIFICADA (U1). Empresa **nova** no Real ainda tem crédito PIS/COFINS próximo de zero no primeiro mês (sem compras/depreciação próprias) — piora para até ~R$ 97.000 (**+R$ 21 mil** vs. Simples). E o ISS não some: mesmo sem dezembro, a RBT12 da Vértice fica em 3,85 mi — **ainda acima do sublimite de 3,6 mi** (art. 13-A) — e a nova empresa também paga ISS.

**2. Quanto à legalidade: não posso recomendar, e o acervo não dá suporte a isso.** Faturar por empresa nova, dos mesmos sócios, a mesma atividade/contratos/empregados da empresa no Simples, só para trocar de regime dentro do exercício, é o retrato de uma **dissimulação** — o tipo de operação que a administração tributária desconsidera e que pode caracterizar fraude. **Nenhuma fonte da biblioteca trata de sucessão/dissimulação** (a citação do arquivo LC 123 refere os arts. 3º, §9º e 20, mas o texto desses dispositivos **não foi transcrito no excerto** — item novo de não verificação, **U6**), portanto não posso fundamentar juridicamente nem "precificar" o risco; profissionalmente, porém, a resposta é **não fazer**. Se a empresa nova existisse para **atividade nova e real**, com estrutura própria e fundamento negocial, seria outra conversa — mas "faturar o dezembro da Vértice por ela" não é isso. Consequências típicas (não verificáveis no acervo): desenquadramento retroativo, solidariedade entre as empresas e responsabilização dos sócios.

**Conclusão da rodada 3:** confirmar a recomendação — nada é feito em dezembro; o único ato possível é comunicar a exclusão até **29/01/2027** se (contra a conta) o sócio quiser sair a partir de 01/01/2027. A ideia da empresa nova **não economiza imposto (custa +R$ 14 a +21 mil só em dezembro) e cria risco jurídico** que o acervo não permite dimensionar.

## 9. Fontes (todas em `library/INDEX.md`)

- `lc123_sublimite_opcao.md` — LC 123/2006, arts. 3º, §§1º/9º; 13-A; 16 (§§2º e 2º-A); 20; 30; art. 18, §4º, IV
- `anexo_iii_faixa6.md` — LC 123/2006, Anexo III; Res. CGSN 140, arts. 9º-12
- `lei9249_9430_presumido.md` — Lei 9.249/95, arts. 15 e 20; Lei 9.430/96, arts. 1º-4º, 25, 26; Lei 9.718/98
- `pis_cofins_nao_cumulativo.md` — Lei 10.637/02, art. 3º; Lei 10.833/03, art. 3º; IN RFB 2.121/2022, arts. 175-176; REsp 1.221.170/PR (STJ)
- `inss_patronal.md` — Lei 8.212/91, art. 22; LC 123, art. 13, VI e §3º

Divergências registradas entre a linha "Citation" do `INDEX.md` e o corpo dos arquivos (sem efeito prático além dos rótulos U): o corpo de `lc123_sublimite_opcao.md` **transcreve art. 3º, II e art. 18, §4º, IV** (não listados na linha de citação do INDEX) e **não transcreve** os arts. 3º, §§1º/9º, 20 e 30 (U6); o corpo de `lei9249_9430_presumido.md` **transcreve a opção do art. 26 da Lei 9.430** (usada no §8, passo 4), embora a linha do INDEX liste apenas arts. 1º-4º e 25.

Nenhuma outra fonte foi usada. Itens U1-U8 acima não têm respaldo na biblioteca e estão rotulados como não verificados.
