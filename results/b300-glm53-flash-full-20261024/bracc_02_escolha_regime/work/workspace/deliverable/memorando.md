# Memorando — Regime tributário 2026, Vértice Engenharia Consultiva Ltda.

**Para:** Hélio Vértice (sócio) — **De:** Contabilidade — **Data de referência:** decisão para o ano-calendário 2026 (balancete de 12 meses encerrado em out/2025; projeção 2026 estável em R$ 4,2 mi).

**Resposta em uma frase:** as contas abaixo mostram que **ficar no Simples é o regime mais barato para 2026** (R$ 948.000,00 contra R$ 1.060.690,00 do Real e R$ 1.111.120,00 do Presumido), que a tese do amigo contador "credita tudo" compra menos crédito do que o sócio imagina (R$ 83.250, e não R$ 129.500), e que **mudar de regime com efeitos em dezembro é impossível pela própria regra de opção** — a saída do Simples só produz efeitos a partir de 1º de janeiro, com pedido até o último dia útil de janeiro (30/01/2026).

---

## 1. Premissas e limitações da biblioteca (leituras obrigatórias)

Trabalhamos **exclusivamente** com `library/` (INDEX) e os documentos do cliente. Premissas-chave, todas marcadas:

- **P1 — Base de ano inteiro 2026:** receita R$ 4,2 mi uniforme (350.000/mês), conforme projeção do cliente (`documents/balancete_12m_resumo.md`). Todas as células do `comparativo.json` são **projeções anuais**, não apurações de 2025.
- **P2 — Anexo III para toda a receita:** o balancete afirma "Regime atual: Simples Nacional, Anexo III (Fator R ≈ 31%)" e o Fator R calculado é `1.300.000 / 4.200.000 = 30,95% ≤ 40%`. Usamos a 6ª faixa do Anexo III para **toda** a receita. **Atenção:** o excerto da LC 123 em `library/lc123_sublimite_opcao.md` (art. 18, §4º, IV) diz que receitas de obras com emprego de materiais são **segregadas em Anexo IV** — e **a biblioteca não contém as alíquotas do Anexo IV**. Mantemos a leitura do próprio cliente (Anexo III) e deixamos o item aberto (Seção 9). A segregação está na biblioteca, portanto é verificável; o efeito financeiro caso as obras fossem Anexo IV **não pode ser calculado com esta biblioteca** (as alíquotas do Anexo IV não constam dela).
- **P3 — ISS fora do DAS no ano inteiro de 2026:** sublimite R$ 3,6 mi (`lc123_sublimite_opcao.md`, art. 13-A). Com receita de R$ 4,2 mi, o excesso sobre o sublimite (600.000 = 16,7% do sublimite) é inferior a 20%, e a regra do art. 13-A ("a partir do mês seguinte, se o excesso for superior a 20%, ou do ano seguinte") coloca o **ISS fora do Simples em qualquer dos ramos já para 2026** (o excesso se deu em 2025) — daí "ISS 0%" na repartição da 6ª faixa (`anexo_iii_faixa6.md`) e ISS pago ao município: 5% × 4.200.000 = **210.000**. Premissa adicional: **toda a receita** (obras e consultiva) é serviço sujeito ao ISS paulistano de 5% (único dado do cliente; a biblioteca não traz a lista de serviços da LC 116).
- **P4 — INSS patronal ≈ 28% da folha:** `library/inss_patronal.md` diz 20% + RAT (1–3%) + terceiros ≈ 5,8% = "total típico ≈ 28%". Usamos 28% exatos sobre R$ 1,3 mi = 364.000 (faixa implícita na biblioteca: 26,8%–28,8% conforme RAT/FAP — não informados; pergunta ao cliente).
- **P5 — Lucro Real: apuração anual, sem adicional.** IRPJ 15% e CSLL 9% sobre o lucro real de 756.000 (Lei 9.249/95, arts. 15 e 20, excerto em `library/lei9249_9430_presumido.md`). O adicional (10%) é descrito na biblioteca para apuração **trimestral**/presumido; a biblioteca **não traz texto sobre adicional na apuração anual do Lucro Real** — assumimos apuração anual sem adicional e marcamos como nuance não verificada na biblioteca (Seção 9). Com apuração trimestral e lucro uniforme, o adicional somaria ~51.600/ano e inverteria Real × Presumido (0,1% de margem) — ver Seção 7.
- **P6 — Créditos PIS/COFINS só sobre insumos aplicados na atividade:** critério de essencialidade/relevância e vedação de crédito a uso e consumo/mobiliário/veículos administrativos (`library/pis_cofins_nao_cumulativo.md`, Lei 10.637 art. 3º; Lei 10.833 art. 3º; IN 2.121 arts. 175-176). Aplicado ao CSV do cliente.
- Não foi necessário inventar nenhum fato legal fora da biblioteca; cada número tem fonte entre colchetes.

## 2. Simples Nacional 2026 (Anexo III, 6ª faixa)

Alíquota efetiva: `(4.200.000 × 33% − 648.000) / 4.200.000 = (1.386.000 − 648.000) / 4.200.000 = 738.000 / 4.200.000 = 17,5714%` [library/anexo_iii_faixa6.md].

- DAS (IRPJ+CSLL+COFINS+PIS+CPP, **ISS 0% na repartição**): 17,5714% × 4.200.000 = **738.000,00**. (Mensal: 350.000 × 17,5714% = 61.500,00 × 12 = 738.000,00.)
- Desdobramento pela repartição da faixa (35% IRPJ / 15% CSLL / 16,03% COFINS / 3,47% PIS / 30,5% CPP; soma 100%): IRPJ 258.300,00; CSLL 110.700,00; COFINS 118.301,40; PIS 25.608,60; CPP 225.090,00. **Concilia: 258.300 + 110.700 + 118.301,40 + 25.608,60 + 225.090 = 738.000,00** ✓
- ISS fora, a 5%: **210.000,00** [premissa P3; balancete: ISS SP 5%].
- INSS patronal fora: **0** (a CPP está dentro do DAS — `library/inss_patronal.md`; LC 123 art. 13, VI).
- **Total Simples = 738.000 + 210.000 = 948.000,00** (22,57% da receita).

## 3. Lucro Presumido 2026 (trimestral)

Presunções [library/lei9249_9430_presumido.md]: obras com emprego de materiais 8% IRPJ / 12% CSLL; serviços em geral, inclusive consultiva, 32% / 32%.

- Base IRPJ: `630.000 × 8% + 3.570.000 × 32% = 50.400 + 1.142.400 = 1.192.800`
- IRPJ: `1.192.800 × 15% = 178.920` + adicional `10% × (1.192.800 − 240.000) = 95.280` → **274.200,00** (checagem trimestral, resultado idêntico: (1.192.800/4 − 60.000) × 10% × 4 = 95.280 ✓)
- Base CSLL: `630.000 × 12% + 3.570.000 × 32% = 75.600 + 1.142.400 = 1.218.000` → CSLL `9% × 1.218.000 =` **109.620,00**
- PIS 0,65% + COFINS 3,00% (cumulativos, sem crédito): `3,65% × 4.200.000 =` **153.300,00**
- ISS 5%: **210.000,00**; INSS patronal 28% × 1.300.000 = **364.000,00** [P4]
- **Total Presumido = 274.200 + 109.620 + 153.300 + 210.000 + 364.000 = 1.111.120,00** (26,46% da receita). (No Presumido o lucro contábil real é irrelevante: a base é a receita.)

## 4. Lucro Real 2026 (auditoria dos créditos)

Débito [library/pis_cofins_nao_cumulativo.md]: PIS 1,65% + COFINS 7,6% = 9,25% × 4.200.000 = **388.500,00** (PIS 69.300 + COFINS 319.200).

Créditos, item a item do `documents/compras_icms_st.csv`:

| Fornecedor / compra | Valor | Crédito 9,25% | Justificativa |
|---|---:|---:|---|
| Aço Forte (perfis, obras) — ICMS-ST | 420.000 | 38.850,00 | insumo material aplicado em obra/serviço (essencial) |
| ElétricaSul (cabos/quadros, obras) — ICMS-ST | 280.000 | 25.900,00 | idem |
| TopSoft (licenças CAD/BIM) | 200.000 | 18.500,00 | insumo da prestação (serviço) — uso inerente à atividade |
| Móveis Planejados Já (mobiliário) | 180.000 | **0,00** | uso e consumo/ativo administrativo — vedado |
| Auto Center (3 veículos) | 220.000 | **0,00** | veículos da área administrativa — vedado |
| Papelaria Central | 100.000 | **0,00** | material de escritório — vedado |
| **Total base vedado** | **500.000** | **—** | **64% das compras (900.000) geram crédito; 36% não geram** |

- **Créditos = 900.000 × 9,25% = 83.250,00** — **não** 129.500 (o que o sócio contou: `1.400.000 × 9,25%`).
- ICMS-ST destacado (aço e cabos) **não altera a conta federal**: não é crédito de PIS/COFINS, e a empresa, como prestadora (ISS), não é contribuinte de ICMS nessas compras — o imposto está embutido no custo. (A biblioteca não traz dispositivo sobre o aproveitamento de ICMS-ST por prestadora de serviços; nada no comparativo depende disso.)
- IRPJ 15% × 756.000 = **113.400,00**; CSLL 9% × 756.000 = **68.040,00** [P5]
- ISS **210.000,00**; INSS patronal **364.000,00** [P4]
- PIS/COFINS líquido = 388.500 − 83.250 = **305.250,00**
- **Total Real = 113.400 + 68.040 + 305.250 + 210.000 + 364.000 = 1.060.690,00** (25,25% da receita).

**Teste da tese do sócio ("credita tudo"):** mesmo concedendo crédito sobre **100%** das compras (129.500), o Real somaria `1.060.690 − 46.250 = 1.014.440,00` — **ainda 66.440 a mais que o Simples**. A tese não vira nem com premissa generosa.

## 5. Ponte Simples × Real (por que o Simples ganha)

Componentes "por fora" equivalentes, usando as repartições da biblioteca:

| Componente | Simples (dentro do DAS) | Lucro Real (por fora) | Simples economiza |
|---|---:|---:|---:|
| CPP/INSS patronal | 225.090,00 | 364.000,00 | 138.910,00 |
| PIS/COFINS | 143.910,00 | 305.250,00 | 161.340,00 |
| IRPJ + CSLL | 369.000,00 | 181.440,00 | (187.560,00) |
| ISS fora (5%) | 210.000,00 | 210.000,00 | 0 |
| **Total** | **948.000,00** | **1.060.690,00** | **112.690,00** |

Conciliação exata: −138.910 − 161.340 + 187.560 = **−112.690** ✓. O que mata a migração é a **CPP paga por fora (364.000)** e o **PIS/COFINS líquido (305.250)**, mesmo com créditos; o DAS a 17,57% "empacota" tudo isso a uma taxa menor. O IRPJ/CSLL é o único componente em que o Real é verdadeiramente menor.

## 6. Resposta ao pedido: "mudar em dezembro"

- **A opção pelo Simples é irretratável para todo o ano-calendário** e a exclusão por opção comunicada **até o último dia útil de janeiro** produz efeitos a partir de **1º de janeiro do mesmo ano**; depois disso, só no 1º de janeiro do ano seguinte [library/lc123_sublimite_opcao.md, art. 16, §2º (irretratabilidade) e §2º-A (prazo e efeitos da exclusão por opção)]. Portanto:
  1. **Não existe mudança com efeitos em dezembro** — a exclusão por opção produz efeitos a partir de 1º/01/2026, nunca no decorrer do ano; o DAS de dezembro/2025 segue devido, no Simples. (O DAS de dezembro/2025 não foi recalculado neste memorando: o excerto não detalha o tratamento do ISS mês a mês em 2025, e o comparativo aqui cobre apenas o ano-calendário 2026.)
  2. O que é possível: **pedir a exclusão do Simples já em dezembro/2025 (ou até 30/01/2026) com efeitos a partir de 1º/01/2026** — mas, pelas contas da Seção 5, **não recomendamos** essa saída para 2026.
- **Passo a passo da opção (se o cliente insistir na saída):**
  1. Decidir o ano-alvo (efeitos a partir de 1º/01). A exclusão por opção é comunicação **até o último dia útil de janeiro do ano em que a saída passa a valer**: pedido em dezembro/2025 ou janeiro/2026 → efeitos 1º/01/2026; pedido após 30/01/2026 → efeitos 1º/01/2027 (prazo análogo: 29/01/2027; conferência de dias úteis: 31/01/2026 é sábado → último dia útil de janeiro/2026 é sexta-feira, 30/01/2026; e 29/01/2027 é sexta).
  2. Protocolar o pedido de exclusão por opção no ambiente do Simples (procedimento do portal — **a biblioteca não traz o guia do portal**; a parte procedimental está fora da biblioteca e não é citada como lei).
  3. Mantidos os livros, a empresa passa a reger-se pelo regime geral; para **Presumido** seria preciso manifestação da opção no pagamento da 1ª quota do 1º trimestre [library/lei9249_9430_presumido.md, Lei 9.430 art. 26]; para **Real** não há manifestação de opção (regime geral por livro).
  4. Conferir recolhimentos de transição (DAS de dezembro/2025 + eventual saldo) antes da troca.
- **Nosso conselho:** permanecer no Simples em 2026 e reavaliar se a receita fugir do hiato de 4,2 mi → 4,8 mi (Seção 7). O pedido de exclusão **não precisa ser feito agora**; se for feito, o prazo é 30/01/2026.

## 7. Sensibilidade (por que "reavaliar")

Modelo proporcional (créditos e lucro escalam com receita; INSS fixo; ISS 5%):

| Receita 2026 | Simples (total) | Real (total) | Real − Simples |
|---:|---:|---:|---:|
| 4.200.000 (projeção) | 948.000 (22,57%) | 1.060.690 (25,25%) | **+112.690 (fica Simples)** |
| 4.480.000 | 1.054.400 (23,54%) | 1.107.136 (24,71%) | +52.736 (fica Simples) |
| 4.500.000 | 1.062.000 (23,60%) | 1.110.454 (24,68%) | +48.454 (fica Simples) |
| 4.800.000 (teto EPP) | 1.176.000 (24,50%) | 1.160.217 (24,17%) | **−15.783 (Real seria menor)** |

Acima de ~R$ 4,7–4,8 mi o Real passaria a vencer; acima de R$ 4,8 mi de receita bruta anual a própria permanência no Simples é vedada [library/lc123_sublimite_opcao.md, art. 3º, II]. Se a receita crescer, reabrir a conta. Presumido é sempre o pior dos três nesta faixa (26,46%) — se algum dia sair do Simples, a rota racional é o **Real**, não o Presumido (+50.430 de diferença a favor do Real: IRPJ/CSLL ganham 202.380 e perdem 151.950 no PIS/COFINS líquido).

## 8. Riscos

1. **Anexo IV nas obras** [P2]: se a receita de 630.000 for recolhida como Anexo IV (LC 123 art. 18, §4º, IV conforme excerto), o DAS do Simples muda e o INSS patronal pode sair dessa parcela — alíquotas do Anexo IV **não constam da biblioteca**. Item aberto.
2. **ISS**: base total assumida e alíquota municipal 5% do balancete; benefícios municipais (se existissem) não foram modelados.
3. **RAT/FAP** (faixa 26,8%–28,8%): assumimos 28%; delta de −15.600 a +10.400/ano.
4. **Adicional no Lucro Real** [P5]: apuração anual sem adicional (assunção); na apuração trimestral o adicional (~51.600) deixaria o Real (1.112.290) pior que o Presumido (1.111.120) por 1.170 — o resultado do comparativo não se inverte porque o Simples segue menor em ambos os cenários.
5. **Crédito de licenças CAD/BIM** (TopSoft): creditamos como insumo da prestação (uso essencial/relevante à atividade). Se a fiscalização considerar "incorporado ao ativo/uso geral", o crédito cai em 18.500 — o ranking não se altera (Real = 1.079.190).
6. **Projeção**: os números são do balancete/projeção do cliente; qualquer mudança de mix (Fator R < 28% → Anexo V; crescimento > 4,8 mi) invalida o comparativo.

## 9. O que precisamos do cliente / itens abertos

Estão em `PERGUNTAS.md`, resumidamente: (a) confirmação do ano de efeitos da eventual mudança (2026); (b) rateio da folha e confirmar se obras seguem ou não Anexo IV; (c) RAT/FAP; (d) base integral (100%) da receita sujeita ao ISS de 5%; (e) notas fiscais das licenças TopSoft, para resguardar o crédito.

## 10. Fontes citadas

- `library/lc123_sublimite_opcao.md` — art. 3º, II (limite 4,8 mi); art. 13-A (sublimite 3,6 mi e regra do excesso; ISS por fora); art. 16 §§2º e 2º-A (irretratabilidade e efeitos da exclusão por opção); art. 18 §4º IV (segregação de obras).
- `library/anexo_iii_faixa6.md` — Anexo III 6ª faixa: 33%, dedução 648.000, repartição (ISS 0%), fórmula da alíquota efetiva.
- `library/lei9249_9430_presumido.md` — presunções (8%/32% IRPJ; 12%/32% CSLL), adicional, alíquotas 15%/9%, PIS/COFINS cumulativos 3,65%, opção (Lei 9.430 art. 26).
- `library/pis_cofins_nao_cumulativo.md` — PIS/COFINS 9,25% e créditos (insumo/essencialidade; vedação a uso e consumo, mobiliário, veículos, material de escritório).
- `library/inss_patronal.md` — INSS patronal ≈ 28% e CPP inclusa no DAS dos Anexos III (LC 123 art. 13, VI).
- `documents/balancete_12m_resumo.md`, `documents/compras_icms_st.csv`, `documents/email_socio.txt` — dados do cliente (não são fontes normativas).
