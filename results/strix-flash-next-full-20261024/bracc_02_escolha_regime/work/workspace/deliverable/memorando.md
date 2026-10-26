# Memorando — Regime tributário 2026: Simples × Lucro Presumido × Lucro Real

**Cliente:** Vértice Engenharia Consultiva Ltda. (São Paulo/SP, ISS 5%)
**Solicitante:** Hélio Vértice (e-mail `documents/email_socio.txt`)
**Data:** 24/10/2026 — rev. 2 (incorpora as respostas do cliente: mix de receita e base de INSS)
**Pedido:** "estourar o Simples", sair em **dezembro** e ir para o Lucro Real porque "credita tudo". Contar os três regimes.

---

## 0. Resposta em uma página

| Regime (2026, R$ 4,2 mi) | Carga total | % da receita |
|---|---:|---:|
| **Simples Nacional (continuar)** | **R$ 916.500** | 21,8% |
| Lucro Presumido | R$ 1.009.620 | 24,0% |
| Lucro Real | R$ 1.010.790 | 24,1% |

Três conclusões, todas contrárias ao pedido:

1. **O Lucro Real é o regime mais caro dos três** (R$ 94.290 a mais que o Simples; R$ 1.170 a mais que o Presumido). A conta do amigo do contador está errada em dois pontos: (a) **não se credita PIS/COFINS sobre os R$ 1,4 mi de compras** — só sobre os **R$ 900 mil de insumos**; uso e consumo, mobiliário e veículos administrativos **não geram crédito**; (b) fora do Simples a empresa passa a pagar **INSS patronal à parte: 28% × folha de R$ 1,05 mi = R$ 294 mil** (`inss_patronal.md`), que dentro do Simples já está dentro do DAS.
2. **Mudar em dezembro é impossível.** A opção pelo Simples produz efeitos desde 1º de janeiro e é **irretratável por todo o ano-calendário**; a exclusão comunicada depois do último dia útil de janeiro só vale de 1º de janeiro do **ano seguinte** (LC 123/2006, art. 16, §2º e §2º-A). Janela de dezembro não existe em ano nenhum — **nem pelo "pedido no portal em dezembro" sugerido pelo amigo**: mesmo pedido, efeito 1º/01/2027 (§8.1). O plano alternativo de **abrir outra empresa no Real para faturar dezembro** também não se recomenda: migrando só a receita paga-se **mais** (+33.875); a economia só aparece migrando contratos/folha/insumos junto, com risco jurídico que a biblioteca não permite avaliar (§8.2, R8, Q8).
3. **Recomendação: ficar no Simples.** Não há necessidade de sair: a receita projetada (R$ 4,2 mi) está **dentro do limite de R$ 4,8 mi** (art. 3º, II) e o sublimite de R$ 3,6 mi **não exclui** do Simples — ele apenas tira ICMS/ISS do DAS (art. 13-A), o que já está considerado na conta acima.

**Atenção (nova, criada pela resposta do cliente):** a vantagem do Simples caiu de R$ 163 mil para **R$ 93 mil**, e apareceram dois itens capazes de consumi-la — a alocação de folha às obras no **Anexo IV** (empate a partir de **31,7%** da folha alocada) e o tratamento do INSS patronal na base do **Lucro Real** (cenário-limite: Real em R$ 910.830, R$ 5.670 **abaixo** do Simples). Ver §6 e Q6/Q7 em `QUESTIONS.md`. Nenhum deles muda a resposta sobre dezembro (impossível) nem a recomendação para 2026 (travada no Simples por lei). **Rodada 3 (24/10/2026): o cliente informou não ter dados sobre esses itens — os limites acima passam a definitivo e seguem sinalizados, sem pergunta reenviada.**

Se, mesmo assim, o sócio quiser sair, a data operativa é **1º/01/2027**, com comunicação de exclusão até o **último dia útil de janeiro de 2027 = 29/01/2027** (sexta-feira).

---

## 1. Fatos usados (todos de `documents/`, com confirmações do cliente)

| Item | Valor | Fonte |
|---|---:|---|
| Receita bruta 12m (encerrado out/2025) = projeção 2026 | R$ 4.200.000 | `balancete_12m_resumo.md` |
| — obras com emprego de materiais (EPC pequenos) | R$ 630.000 = **15,0% do faturamento** | idem + **confirmado pelo cliente** ("uns 15% do faturamento é obra pequena com material; o resto é consultoria") |
| — serviços de engenharia consultiva | R$ 3.570.000 = 85,0% | idem + confirmado pelo cliente |
| **Folha de pagamento (salários + pró-labore)** | **R$ 1.050.000** | **resposta do cliente (Q1)** + fecha com o balancete |
| Encargos sobre folha (descritos pelo cliente como "INSS patronal + RAT + FGTS etc.") | R$ 250.000 | resposta do cliente (Q1) |
| Linha agregada do balancete: folha + pró-labore + encargos + FGTS | R$ 1.300.000 = 1.050.000 + 250.000 | `balancete_12m_resumo.md` + Q1 → **reconciliada** |
| Compras totais | R$ 1.400.000 (insumos R$ 900.000; uso e consumo/ativos R$ 500.000) | idem + `compras_icms_st.csv` |
| Lucro contábil antes de IRPJ/CSLL (projetado p/ Real) | R$ 756.000 | idem |
| Regime declarado pelo balancete | Simples, Anexo III, "Fator R ≈ 31%" (1.300.000/4.200.000 = 30,95%) | idem — **ver alerta do R2** |
| ISS São Paulo | 5% | idem |

As duas respostas do cliente **fecham exatamente** com o balancete: 630.000 / 4.200.000 = **15,0%** de obras, e 1.050.000 + 250.000 = **R$ 1.300.000**. Por isso **nenhum outro número** foi alterado; o que mudou foi a **base de cálculo do INSS patronal** (§4, §5) e a leitura do Fator R (§7, R2).

Detalhamento das compras (`compras_icms_st.csv`): insumo de obra R$ 420.000 + R$ 280.000 = **R$ 700.000**; insumo de serviço (licenças CAD/BIM) **R$ 200.000** → total insumos **R$ 900.000**; não creditáveis: mobiliário R$ 180.000, 3 veículos R$ 220.000, material de escritório R$ 100.000 → **R$ 500.000**. Os dois grupos fecham exatamente com o balancete (900.000 + 500.000 = 1.400.000).

## 2. Premissas (proeminentes — afetam o resultado)

- **P1 — Base do INSS patronal = R$ 1.050.000 (resolvida).** O cliente informou a divisão da linha de R$ 1,3 mi: **folha (salários + pró-labore) R$ 1.050.000** e **encargos R$ 250.000**. A contribuição previdenciária incide **sobre a folha** (`inss_patronal.md`: "20% de INSS patronal sobre a folha, mais RAT (1–3%) e terceiros (≈5,8%) — total típico ≈ 28% da folha"), logo **não** sobre encargos/FGTS. CPP fora do Simples = **1.050.000 × 28% = R$ 294.000**. Subproduto do cálculo da biblioteca: "≈28%" é valor **típico** — o RAT é ajustado pelo FAP e os terceiros por ≈5,8%; não refinamos (FAP não informado).
- **P1b — Composição dos R$ 250.000 de encargos é contradita pela biblioteca (aberto, Q6).** No Simples Anexo III a CPP **está dentro do DAS** e "a empresa não recolhe INSS patronal à parte" (`inss_patronal.md`). Logo a linha contábil chamada "INSS patronal + RAT + FGTS etc." **não pode** conter a CPP integral devida fora do Simples: 28% × 1.050.000 = **294.000 > 250.000**. Não forçamos a reconciliação; tratamos o efeito como cenário (§6, tabela C).
- **P2 — Receita de obras (R$ 630 mil = 15%) tratada no Anexo III**, como declara o balancete. A biblioteca manda **segregar** obras com emprego de materiais para o **Anexo IV** (LC 123, art. 18, §4º, IV), mas **as alíquotas do Anexo IV não estão na biblioteca** → cenário quantificado só parcialmente em §7 (R1), com limites.
- **P3 — ISS incide sobre R$ 3.570.000** (serviços de consultoria), a 5%. Não aplicamos ISS sobre os R$ 630 mil de obras: a biblioteca não traz regra de incidência/redução de base da construção civil em São Paulo. Se incidir, é **+R$ 31.500 nos três regimes** (não muda o ranking).
- **P4 — Lucro Real = lucro contábil R$ 756.000, sem ajustes** (nenhum dado de adições/exclusões; a biblioteca não trata do Lucro Real) **e com a CPP já absorvida na projeção** — isto é, no cenário-base o INSS patronal de R$ 294.000 é somado como custo adicional do regime **sem** reduzir a base do IRPJ/CSLL. Se a CPP for tratada como despesa dedutível do Lucro Real, o resultado muda (§6, tabela C) — a dedutibilidade **não está na biblioteca**, por isso é cenário e não conta-base.
- **P5 — Receita distribuída uniformemente ao longo do ano.** Confere: no Presumido trimestral, base 298.200/trimestre e IRPJ 68.550/trimestre × 4 = R$ 274.200, idêntico ao cálculo anual; no Real, 189.000/trimestre × 4 = R$ 165.000.
- **P6 — Sublimite já ultrapassado em 2026.** RBT12 de 4,2 mi excede o sublimite de 3,6 mi em **16,67%** (≤20%), logo pelo art. 13-A o ISS/ICMS saem do DAS **a partir do ano seguinte** — i.e., desde 1º/01/2026. Isso é coerente com a 6ª faixa do Anexo III, cuja repartição traz **ISS 0%**.
- **P7 — ICMS não é calculado.** A empresa é de serviços; se algum contrato EPC transferir mercadoria sujeita a ICMS (ou a regra de ICMS-ST do arquivo de compras), a biblioteca não tem a regra → não quantificamos (§7, R4).
- **P8 — Mix de receita confirmado em 15% obras / 85% consultoria** pelo cliente, igual ao balancete. As presunções 8%/12%/32% e o ISS seguem essa divisão; sensibilidade no §6, tabela B.

## 3. Simples Nacional — R$ 916.500

RBT12 = R$ 4.200.000 → 6ª faixa do Anexo III (3.600.000,01 a 4.800.000): nominal **33%**, parcela a deduzir **R$ 648.000** (fonte: `anexo_iii_faixa6.md`).

```
DAS       = 4.200.000 × 33%          = 1.386.000
          − 648.000                  =   738.000      → alíquota efetiva 17,5714%
ISS fora  = 3.570.000 × 5%           =   178.500      (art. 13-A; ISS 0% na 6ª faixa)
INSS      = 0                        (CPP dentro do DAS — LC 123, art. 13, VI)
TOTAL     = 738.000 + 178.500        =   916.500      (21,82% da receita)
```

Repartição do DAS pela tabela da biblioteca (útil para ver o peso da folha): IRPJ 35% = 258.300; CSLL 15% = 110.700; COFINS 16,03% = 118.301,40; PIS 3,47% = 25.608,60; **CPP 30,50% = 225.090**; ISS 0%. Ou seja, hoje a empresa **já paga ≈ R$ 225 mil de CPP dentro do DAS**; fora do Simples pagaria 294.000 → **diferencial de apenas R$ 68.910** de folha (ver §6).

Custo marginal na 6ª faixa é **33%** de cada real adicional de receita, e a alíquota efetiva sobe: 4,5 mi → 18,6%; 4,8 mi → 19,5% (DAS 936.000 + ISS 204.000 = 1.140.000).

## 4. Lucro Presumido — R$ 1.009.620

Presunções (`lei9249_9430_presumido.md`, Lei 9.249 arts. 15 e 20): serviços em geral, inclusive engenharia consultiva, **32%** (IRPJ e CSLL); construção por empreitada com emprego de materiais **8%** (IRPJ) e **12%** (CSLL).

```
Base IRPJ  = 3.570.000 × 32% + 630.000 × 8%  = 1.142.400 + 50.400 = 1.192.800
IRPJ 15%   = 1.192.800 × 15%                                  =   178.920
Adicional  = (1.192.800 − 240.000) × 10% = 952.800 × 10%      =    95.280
IRPJ total =                                                =   274.200
Base CSLL  = 3.570.000 × 32% + 630.000 × 12% = 1.142.400 + 75.600 = 1.218.000
CSLL 9%    = 1.218.000 × 9%                                 =   109.620
PIS/COFINS = 4.200.000 × (0,65% + 3,00%) = 27.300 + 126.000 =   153.300  (cumulativo, sem crédito)
ISS 5%     = 3.570.000 × 5%                                 =   178.500
INSS 28%   = 1.050.000 × 28% (20% + RAT + terceiros)        =   294.000   ← base corrigida (Q1)
TOTAL      = 274.200+109.620+153.300+178.500+294.000        = 1.009.620  (24,04%)
```

## 5. Lucro Real — R$ 1.010.790

```
IRPJ 15%            = 756.000 × 15%                          =   113.400
Adicional 10%       = (756.000 − 240.000) × 10% = 516.000    =    51.600
IRPJ total          =                                        =   165.000
CSLL 9%             = 756.000 × 9%                           =    68.040
PIS/COFINS débito   = 4.200.000 × (1,65% + 7,60%) = 9,25%    =   388.500
Créditos 9,25%      = 900.000 × 9,25% (só insumos)           =   (83.250)
PIS/COFINS líquido  =                                        =   305.250
ISS 5%              = 3.570.000 × 5%                         =   178.500
INSS 28%            = 1.050.000 × 28%                        =   294.000   ← base corrigida (Q1)
TOTAL               = 165.000+68.040+305.250+178.500+294.000 = 1.010.790  (24,07%)
```

**Por que os créditos não salvam o Real:**

- Crédito correto = R$ 83.250. Crédito alegado pelo contador = 1.400.000 × 9,25% = **R$ 129.500** → superestimado em **R$ 46.250**. Uso e consumo administrativo, material de escritório, mobiliário e veículos da área administrativa **não geram crédito** (`pis_cofins_nao_cumulativo.md`, Lei 10.637/02 e Lei 10.833/03, art. 3º).
- Ainda com crédito, PIS/COFINS do Real fica em **R$ 305.250** contra **R$ 153.300** do cumulativo: **+R$ 151.950**.
- A economia do Real sobre o Presumido (IRPJ/CSLL sobre lucro de 756 mil em vez de presunção de 1.192.800) é de **R$ 150.780** — quase exatamente cancelada pelo PIS/COFINS não cumulativo. Resultado: Real e Presumido ficam **empatados (diferença de R$ 1.170)** e ambos **R$ 93–94 mil acima do Simples**.
- O item que o sócio não colocou na conta é o **INSS patronal de R$ 294 mil** (20% + RAT + terceiros sobre a folha de R$ 1,05 mi), que dentro do Simples (Anexo III) está embutido no DAS (`inss_patronal.md`, LC 123, art. 13, VI e §3º).

## 6. Sensibilidades que definem (e podem inverter) o resultado

### A. Base do INSS patronal — **resolvida pela resposta do cliente**

Sem INSS patronal, Presumido/Real custariam 715.620/716.790 — **menos** que o Simples. Igualando contas, o ponto de empate é a base de contribuição:

| Base de INSS patronal | Presumido = 715.620 + 28% × base | Veredito |
|---|---:|---|
| R$ 1.300.000 (linha agregada — **superestimava**) | 1.079.620 | Simples ganhava por 163.120 |
| **R$ 1.050.000 (folha informada — usado)** | **1.009.620** | **Simples ganha por 93.120** |
| **R$ 717.429 (break-even)** | 916.500 | empate |
| abaixo de R$ 717.429 | < 916.500 | Presumido passaria a ganhar |

A folha informada (R$ 1.050.000) está **R$ 332.571 acima** do ponto de empate → folga de 28% × 332.571 = **R$ 93.120**. Esse é hoje o **colchão** da recomendação, e ele é consumido pelos dois itens abaixo.

### B. Mix de receita (confirmado em 15% obras) e alocação de folha ao Anexo IV

Quanto maior a parcela de obra (presunção 8%/12% em vez de 32%), mais barato o Presumido:

| Mix de obras sobre R$ 4,2 mi | Presumido | Folga do Simples |
|---|---:|---:|
| 10% | 1.036.500 | 120.000 |
| **15% (informado = balancete)** | **1.009.620** | **93.120** |
| 20% | 982.740 | 66.240 |
| 30% | 928.980 | 12.480 |
| 32,3% | ≈916.500 | 0 |

Para o Presumido empatar com o Simples só pelo mix, as obras teriam de ser **≈32% do faturamento** — desmentido pelo balancete **e** pela resposta do cliente (15%). **Esse vetor não inverte a recomendação.**

Já a **segregação da receita de obras para o Anexo IV** (P2/R1) pesa pelo lado do Simples: no Anexo IV a CPP **não** está no DAS (`inss_patronal.md`), então a **folha alocada às obras** passa a custar INSS patronal à parte. A biblioteca não diz o critério de alocação nem traz a alíquota do Anexo IV, então isolamos só esse efeito:

| Folha alocada às obras | CPP extra (28% × 1,05 mi × share) | Simples (DAS Anexo III como teto) | Folga vs Presumido |
|---|---:|---:|---:|
| 10% = 105.000 | 29.400 | 945.900 | 63.720 |
| 15% = 157.500 (proporcional à receita) | 44.100 | 960.600 | 49.020 |
| 20% = 210.000 | 58.800 | 975.300 | 34.320 |
| 25% = 262.500 | 73.500 | 990.000 | 19.620 |
| 30% = 315.000 | 88.200 | 1.004.700 | 4.920 |
| **31,7% = 332.600** | 93.120 | **1.009.620** | **0 — empate** |

Ou seja: **se mais de 31,7% da folha for alocada às obras**, o Presumido passa a ser mais barato (assumindo, a favor do Simples, que a alíquota do Anexo IV não é maior que a do Anexo III — se for menor, o break-even sobe). Como as obras são 15% da receita e consomem R$ 700 mil de insumos (quase o faturamento das obras), a hipótese proporcional (15%) parece a mais realista, mas **isso é julgamento nosso, não fato verificado** → Q7.

### C. Tratamento do INSS patronal na base do Lucro Real (P1b/P4) — vetor que **pode inverter**

Fora do Simples a CPP passa de "dentro do DAS" (30,5% × 738.000 = **225.090**) para **294.000** à parte. Se essa CPP adicional for **despesa dedutível** do Lucro Real (mecanismo **não verificado** na biblioteca), o lucro de 756.000 cai e o IRPJ/CSLL acompanham:

| Hipótese sobre os R$ 250 mil de encargos | Lucro p/ Real | IRPJ | CSLL | Real total | vs Simples (916.500) |
|---|---:|---:|---:|---:|---:|
| 756.000 já absorve toda a CPP (**cenário-base, P4**) | 756.000 | 165.000 | 68.040 | **1.010.790** | +94.290 |
| Só R$ 44.000 são incrementais (294.000 − 250.000) | 712.000 | 154.000 | 64.080 | 995.830 | +79.330 |
| **Nenhum centavo de CPP está na projeção** (os 250 mil são FGTS/13º/férias, coerente com o Anexo III) | 462.000 | 91.500 | 41.580 | **910.830** | **−5.670 → Real mais barato** |

Escudo máximo: 34% × 294.000 = **R$ 99.960** — maior que a folga de R$ 93.120. **Este é o único cenário em que a recomendação se inverte**, e ele depende de um fato que o cliente ainda não detalhou (composição da linha de encargos): **Q6**. Combinado com uma alocação de folha às obras ≥15% (linha B), o Real ficaria ≈R$ 50 mil mais barato que o Simples — por isso a recomendação está marcada com reserva e as duas perguntas ficam abertas.

### D. Cenários menores (não invertem sozinhos)

| Cenário | Efeito |
|---|---|
| Crédito das licenças CAD/BIM (R$ 200 mil) negado pela fiscalização (critério da essencialidade, REsp 1.221.170/PR) | Real sobe para 1.029.290 (+18.500) — pior |
| ISS também sobre as obras (R$ 630 mil) | +31.500 nos três regimes (Simples 948.000 / Presumido 1.111.120 / Real 1.112.290) — neutro no ranking |
| Créditos de energia/aluguel/depreciação de equipamentos (não detalhados) | reduziriam o Real; para empatar com o Simples (cenário-base) seria preciso **R$ 1.019.351** de créditos adicionais de insumo (94.290 / 9,25%) — improvável, mas não verificado (Q3) |
| Lucro real acima de 756.000 | cada R$ 100.000 de lucro a mais adds ~R$ 34.000 ao Real; o Real só empataria com o Simples se o lucro fosse **≤ R$ 478.676** (e não ≥) — ver R6 |

## 7. Riscos e itens não quantificáveis

- **R1 — Segregação de Anexo (maior risco).** A receita de **obras com emprego de materiais (R$ 630 mil, 15%)** deve ser segregada para o **Anexo IV** (LC 123, art. 18, §4º, IV). Consequências: (i) alíquota do Anexo IV **não está na biblioteca** → não calculamos; (ii) no Anexo IV a CPP **não** está no DAS → INSS patronal sobre a **folha alocada às obras** (§6-B): **empate com o Presumido a partir de 31,7% da folha alocada**; (iii) o critério de alocação também não está na biblioteca. É o risco que pode consumir o colchão de R$ 93.120 — **Q7**.
- **R2 — Fator R e risco de Anexo V (agravado pela resposta do cliente).** O balancete afirma Fator R ≈ 31%, mas calculado sobre **R$ 1.300.000** (folha + encargos + FGTS). Com a divisão informada, a **folha pura (salários + pró-labore) é R$ 1.050.000 = 25,00%** da receita — **abaixo dos 28%** que a prática usa como fronteira para manter serviços de engenharia no Anexo III; faltariam **R$ 126.000** de folha (28% × 4,2 mi = 1.176.000). A **regra dos 28% do Fator R não está na biblioteca** (por isso mantivemos a classificação declarada de Anexo III), mas a consequência é material: se a consultoria migrar para o **Anexo V**, o DAS sobe (alíquota não está na biblioteca). Limite da tolerância: o DAS poderia subir até **R$ 831.120** (efetiva **19,79%**, vs 17,57% hoje) antes de o Presumido (1.009.620) ficar mais barato — e só até **R$ 787.020** (efetiva 18,74%) se já estiver pagando CPP de Anexo IV sobre 15% da folha. **Manter folha ≥ 28% da receita é a alavanca de defesa.**
- **R3 — Sublimite, teto e cruzamento de receita (corrigido nesta revisão).** Sublimite (R$ 3,6 mi) estourado: ICMS/ISS fora do Simples, sem exclusão (art. 13-A). **Teto de R$ 4,8 mi** (art. 3º, II) dá folga de apenas R$ 600 mil (+14,3%). A alíquota marginal do Simples na 6ª faixa é de **33% + ISS**, contra marginal de ≈17,6% do Presumido → o crescimento de receita **come a vantagem do Simples rapidamente**. Com folha fixa em 1,05 mi (CPP 294.000) e mix constante, o ponto de cruzamento é **≈ R$ 4.674.134** — **abaixo do teto**: a ~R$ 4,8 mi o Simples custaria ≈1.140.000 e o Presumido ≈1.115.280 (Presumido mais barato por 24.720). Variantes: CPP crescendo com a receita (folha mantida em 25% dela) → cruzamento ≈ **R$ 4,94 mi**; com CPP de Anexo IV sobre 15% da folha (+44.100 fixos) → cruzamento ≈ **R$ 4,45 mi**. Portanto **é o crescimento, e não o teto, que encerra a vantagem do Simples** — ela acaba ainda dentro da faixa do Simples. (A versão anterior desta memória indicava ≈5,03 mi; estava calculada com a CPP antiga de 364.000 e foi corrigida. Aproximações: presunções e créditos proporcionais, alíquota da 6ª faixa constante até o teto.)
- **R4 — ICMS / ICMS-ST.** O arquivo de compras mostra ICMS-ST destacado em R$ 700 mil de insumos de obra. A **recuperabilidade de ICMS-ST como crédito de PIS/COFINS não está no texto da biblioteca** fornecido (só alíquotas e hipóteses de crédito) → **não creditamos** e não verificamos. Também não verificamos se os contratos EPC geram ICMS.
- **R5 — Lucro Real é estimado.** R$ 756.000 é lucro **contábil**; a base do Lucro Real exige ajustes (juros, multas, depreciação, receitas/custos diferidos) — nenhuma regra nem dado disponível. Real pode ser pior ou melhor; a biblioteca não permite calcular. Somado a §6-C, o Real é o regime de maior variância desta conta.
- **R6 — Coerência não reconciliada.** Não há demonstração de resultado linha a linha: receita 4,2 mi − folha 1,05 mi − encargos 0,25 mi − compras 1,4 mi = **R$ 1,5 mi**, contra **756 mil** informados → **≈ R$ 744 mil de despesas não detalhadas**. Além disso, a linha de encargos (250.000 = 23,8% da folha) é **menor que a CPP isolada fora do Simples (294.000 = 28%)**, o que é estranho para uma empresa que se declara no Anexo III (onde não há CPP à parte). Não forçamos nenhum dos dois números: usamos 756.000 como informado e deixamos ambas as divergências abertas (Q4 e Q6).
- **R7 — Inconsistência de margem das obras.** Insumos de obra somam **R$ 700.000** contra receita de obras de **R$ 630.000** (`compras_icms_st.csv` × balancete): as obras aparentemente não cobrem nem o material. Pode ser insumo misto (obra + serviço), obra fora do período ou erro de classificação. Não ajustamos; impacta simultaneamente a presunção de 8%, o crédito de PIS/COFINS e a alocação de folha do R1.
- **R8 — Plano "outra empresa no Lucro Real faturando dezembro" (consulta do sócio em 24/10/2026).** A mecânica tributária está calculada em §8.2, mas o **risco jurídico é o ponto central e não tem regra na biblioteca**: desvirtuamento/pluralidade simulada de entidades, transferência de contrato e de pessoal, e a situação de empresa recém-constituída fora do Simples **não estão em nenhum arquivo da biblioteca** → qualquer afirmação sobre a validade da operação seria **não verificada** (Q8). Além disso, a **exclusão por estouro do teto** (possível motivação do plano) também não está na biblioteca (ver §8, último item). Se o objetivo é Lucro Real, existe o caminho legal e gratuito: comunicação até **29/01/2027**.

## 8. "Mudar em dezembro": impossível — e o timing correto

### 8.1 A alegação do amigo ("basta pedir a exclusão no portal em dezembro")

O texto da biblioteca é **expresso e não deixa margem** (`library/lc123_sublimite_opcao.md`, LC 123, art. 16):

- **§2º:** a opção pelo Simples "**produzirá efeitos a partir do primeiro dia do ano-calendário** da opção; a opção é **irretratável para todo o ano-calendário**."
- **§2º-A:** "a exclusão por opção comunicada **até o último dia útil de janeiro** produz efeitos desde **1º de janeiro do mesmo ano**; comunicada **depois, só a partir de 1º de janeiro do ano seguinte**."

Consequência direta: **mesmo se o portal aceitar o pedido em dezembro/2026**, a exclusão produz efeitos **apenas desde 1º/01/2027** (o pedido é posterior ao último dia útil de janeiro de 2026). Não existe nenhuma data de pedido em 2026 que produza saída em dezembro — 2026 inteira permanece no Simples, e todo faturamento de dezembro/2026 é tributado pelo DAS. O "atalho" do amigo, quando muito, antecipa em um mês o **mesmo** efeito (1º/01/2027) que se obtém com a comunicação regular até **29/01/2027** — sem nenhum risco adicional. (Se o portal técnico aceita ou não o pedido fora da janela é fato operacional, não norma; a biblioteca não trata do portal — não verificado, mas irrelevante para o efeito jurídico.)

### 8.2 Plano "abrir outra empresa no Lucro Real e faturar dezembro por ela" (consulta de 24/10/2026)

Duas camadas: **(i) a mecânica tributária** (calculável, com premissas) e **(ii) a validade da operação** (não verificável na biblioteca).

**(i) Mecânica** — dezembro = média 4,2 mi / 12 = **R$ 350.000** de receita (sazonalidade não informada — premissa). Manter mix 15/85 e alíquotas do memorando:

| Cenário | Cálculo | Imposto |
|---|---|---:|
| Vértice mantém dezembro (caso-base) | Simples sobre 4,2 mi | 916.500 |
| Vértice sem dezembro (3,85 mi — ainda 6ª faixa, > 3,6 mi: 33% − 648.000) | DAS 622.500 + ISS 163.625 | **786.125** |
| **Economia na Vértice se dezembro sair** | 916.500 − 786.125 | **130.375** (marginal efetivo ≈ 37,25%) |
| **(a)** Nova empresa recebe **só a receita** de dezembro (contratos, folha e insumos ficam na Vértice → lucro da fatia = 350.000) | IRPJ 15%×350.000 + adicional 10%×(350.000−20.000) = 85.500; CSLL 9%×350.000 = 31.500; PIS/COFINS 9,25%×350.000 = 32.375 (sem crédito); ISS 5%×297.500 = 14.875 | **164.250** → **pior em 33.875** |
| **(b)** Migram **também** contratos, folha (87.500/mês) e insumos (75.000/mês, limite de Q3) → lucro da fatia ≈ 63.000 (margem informada 18%) | IRPJ 9.450 + adicional 4.300 = 13.750; CSLL 5.670; PIS/COFINS 32.375 − 6.938 = 25.438; ISS 14.875; CPP 28%×87.500 = 24.500 | **84.232** → "ganho" de **46.142** |

Leitura fria da aritmética: o plano **só economiza se a estrutura inteira do negócio migrar junto** (cenário b). Se migrar só a receita, **aumenta** o imposto (cenário a). Mas "migrar a estrutura inteira" um mês antes do ano fiscal é exatamente o desenho que atrai questionamento — o que nos leva à camada (ii).

**(ii) Validade — não verificado (biblioteca muda).** Nenhum arquivo da biblioteca trata de: **desvirtuamento / pluralidade simulada de entidades / negócio jurídico com objetivo de fraude**, cessão de contratos e de pessoal, constituição de empresa no fim do ano, nem do **regime tributário de empresa recém-constituída** (a opção pelo Real de quem abre no meio do ano não está na biblioteca). Também **não está na biblioteca** a consequência de estouro do teto (o único motivo pelo qual tirar dezembro da Vértice *preservaria algo*: manter RBT12 ≤ 4,8 mi — e não podemos dizer o que aconteceria se dezembro empurrasse o acumulado acima do teto). **Quaisquer afirmações sobre esses pontos seriam não verificadas e não as fazemos.** O que é verificável: (1) se o objetivo é Lucro Real, o caminho **legal e sem risco** é a comunicação de exclusão até **29/01/2027**, efeitos 1º/01/2027 (§8.1); (2) o benefício máximo mensurável do plano é ≈ **R$ 46 mil** (cenário b, premissas acima) contra um risco jurídico que **não podemos dimensionar com a biblioteca** — desproporcional; (3) a **folha de dezembro da Vértice não desaparece**: se os empregados forem para a nova empresa, a Vértice ainda paga folha nov/26 e o Fator R/Anexo III de 2026 é medido pelo RBT12 (art. 18 da LC 123 no texto disponível não detalha o cálculo do Fator R — não verificado).

Recomendação registrada: **não executar o plano**. Se o sócio insistir, respondê-lo-ei mediante os fatos da Q8.

- Opção pelo Simples **vale do 1º dia do ano-calendário e é irretratável pelo ano inteiro** (art. 16, §2º). A exclusão comunicada **até o último dia útil de janeiro** vale desde 1º/01 daquele ano; **depois disso, só de 1º/01 do ano seguinte** (§2º-A). Portanto, em **nenhum** cenário (dezembro/2025 ou dezembro/2026) existe mudança em dezembro; a janela de 2026 (comunicação até **30/01/2026**, último dia útil de janeiro de 2026) já está fechada — 2026 está travado no Simples.
- Próxima janela: comunicar a exclusão **até 29/01/2027** (sex, último dia útil de janeiro de 2027 — sem contagem de feriados, que a biblioteca não traz) → efeitos **desde 1º/01/2027**.
- No Presumido, a opção se manifesta com o **pagamento da 1ª quota do 1º período de apuração do ano** e é **definitiva por todo o ano** (Lei 9.430/96, art. 26). A data exata de vencimento dessa DARF **não está na biblioteca**.
- Regras de **exclusão de ofício / retroativa** quando a receita ultrapassa o teto no meio do ano **não estão na biblioteca** → não afirmamos nada sobre isso (marcado como não verificado).

## 9. Passo a passo, se o sócio insistir em sair (efeitos 01/01/2027)

1. Antes de decidir, fechar **Q6** (composição dos R$ 250 mil de encargos / a CPP está ou não na projeção de 756 mil) e **Q7** (folha alocada às obras) — são os dois itens que podem inverter a conta (§6-B e §6-C).
2. Até **29/01/2027**: comunicar a **exclusão do Simples** no e-CAC (DASN/Simples Nacional → "exclusão"), escolhendo como efeito **1º/01/2027**. Guardar o recibo.
3. Pagar a **1ª quota do 1º período de apuração de 2027** do IRPJ/CSLL pelo Lucro Presumido — isso **manifesta a opção** (Lei 9.430, art. 26); é **definitiva pelo ano todo**.
4. Em 2027, abrir apurações separadas: **ISS 5% diretamente ao município** (SP) sobre os serviços, **PIS/COFINS não cumulativos** (9,25% débito; crédito só de insumos — 900 mil/ano, com o critério da essencialidade), **folha com INSS patronal 20% + RAT/FAP + terceiros** em GFIP/eSocial, e segregação de receitas 8%/32% (IRPJ) e 12%/32% (CSLL).
5. **Não recomendado**: com os fatos atuais e as respostas já dadas, a migração custaria **+R$ 93.120/ano** (Presumido) ou **+R$ 94.290/ano** (Real). Só reconsiderar se (i) a **folha** cair abaixo de **R$ 717.429** (§6-A — aí o Presumido vence), ou (ii) a resposta de **Q6** confirmar que a CPP de R$ 294 mil é toda incremental e dedutível na base do Real (§6-C), ou (iii) a resposta de **Q7** mostrar alocação de folha às obras acima de **31,7%** (§6-B).

## 10. Fontes usadas (todas em `library/INDEX.md`)

| Arquivo | Citação (INDEX) | Usado para |
|---|---|---|
| `library/lc123_sublimite_opcao.md` | LC 123/2006, arts. 3º, §§1º e 9º; 13-A; 16; 20; 30 | teto 4,8 mi; sublimite 3,6 mi e ISS/ICMS fora; anualidade/irretratabilidade; prazos de opção/exclusão; segregar obras |
| `library/anexo_iii_faixa6.md` | LC 123/2006, Anexo III; Res. CGSN 140, arts. 9º-12 | 6ª faixa: 33% − 648.000; repartição (CPP 30,50%; ISS 0%) |
| `library/lei9249_9430_presumido.md` | Lei 9.249/95, arts. 15 e 20; Lei 9.430/96, arts. 1º-4º, 25 (e art. 26); Lei 9.718/98 | presunções 32/8/12%; 15% + 10% sobre > 240 mil/ano; CSLL 9%; PIS/COFINS cumulativos 0,65+3,00%; opção definitiva |
| `library/pis_cofins_nao_cumulativo.md` | Lei 10.637/2002 art. 3º; Lei 10.833/2003 art. 3º; IN RFB 2.121/2022 arts. 175-176 | alíquotas 1,65/7,6%; créditos de insumo (essencialidade); vedação a uso e consumo, mobiliário, veículos |
| `library/inss_patronal.md` | Lei 8.212/91 art. 22; LC 123 art. 13, VI e §3º | base = folha; 20% + RAT + terceiros ≈ 28% fora do Simples/Anexo IV; CPP embutida no DAS nos Anexos I, II, III, V |
| `library/INDEX.md` | — | lista fechada de citações permitidas |

**Nota de citação:** a regra da opção pelo Presumido (manifestação com o pagamento da 1ª quota do 1º período, definitiva pelo ano) está no texto de `library/lei9249_9430_presumido.md` como "Lei 9.430, art. 26"; a coluna de citação do `INDEX.md` para esse arquivo lista "arts. 1º a 4º, 25". Cito o arquivo do índice, marcando essa diferença de número de artigo.

**Afirmativas não verificadas (não constam da biblioteca — não foram usadas como fundamento):** alíquotas do Anexo IV e do Anexo V; regra dos 28% do Fator R e o numerador do Fator R (folha × (1) ou folha + encargos?); critério de alocação de folha entre anexos; dedutibilidade do INSS patronal na base do Lucro Real; FGTS e suas alíquotas; redução de base de ISS da construção civil em São Paulo; recuperação de ICMS-ST no PIS/COFINS não cumulativo; ajustes do Lucro Real; exclusão de ofício/retroativa por excesso de receita; vencimentos de DARF; feriados que alteram "último dia útil".

## 11. Perguntas ao cliente

Em `deliverable/QUESTIONS.md` (espelho em `PERGUNTAS.md`): **respondidas** — Q1 (divisão folha 1.050.000 / encargos 250.000 → base do INSS corrigida para R$ 294.000) e Q2 na parte do mix (15% obras / 85% consultoria, igual ao balancete). **Sem resposta na rodada 3 (24/10/2026): o cliente informou não ter informações adicionais sobre nenhum item em aberto — as perguntas ficam encerradas (não serão reenviadas) e permanecem como desconhecidos explicitamente sinalizados, com limites calculados** — Q3 (valores de energia, aluguel, equipamentos), Q4 (reconciliação do lucro de 756 mil), Q5 (folha/receita projetadas de 2027). **Novas perguntas, surgidas da resposta do cliente** — Q6 (composição da linha de encargos: há CPP nela? o Lucro Real deduziria os R$ 294 mil?) e Q7 (parcela da folha alocada às obras no Anexo IV), além de Q8 (plano do sócio "outra empresa no Real faturando dezembro" — respondido em §8.2, **não executar**). **Estado final do trabalho:** recomendação (Simples), resposta sobre dezembro (impossível) e prazo (29/01/2027) **inalterados**; todos os desconhecidos ficam sinalizados com limites calculados — Q6: tolerância de apenas **5.670** (único item capaz de inverter o ranking, cenário-limite não adotado); Q7: empate com **31,7%** da folha alocada às obras; Q3: seriam precisos **1.019.351** de créditos extras; Q4: inversão só com lucro **≤ 478.676** (divergência de ~744 mil não reconciliada, número não forçado); Q5: Presumido vence a partir de **≈ 4.674.134** de receita (folha fixa).
