# Memória de cálculo — DAS maio/2026 · Lumen Soluções Digitais ME

Competência: **maio/2026** · Simples Nacional · Fontes clientes: `documents/notas_emitidas_maio.md`, `documents/nfe_000512_locacao.xml`, `documents/faturamento_12_meses.csv`, `documents/resumo_folha_12_meses.csv`, `documents/extrato_maio_2026.csv`, `documents/email_socio.txt`.

**Fontes da biblioteca (as únicas citáveis, conforme `library/INDEX.md`):**

| # | Arquivo | Citação |
|---|---|---|
| L1 | `library/lc123_art18_fator_r.md` | LC 123/2006, art. 18, §§1º, 1º-A, 5º-J, 5º-K, 5º-M, 4º; Resolução CGSN 140/2018, arts. 25, 26 |
| L2 | `library/anexos_iii_v_tabelas.md` | LC 123/2006, Anexos III e V (redação LC 155/2016) |
| L3 | `library/locacao_bens_moveis_iss.md` | LC 123/2006, art. 18, §5º-A; Súmula Vinculante 31 (STF); Res. CGSN 140, art. 25, §1º, V |

---

## 1. Classificação das notas de maio/2026

| Doc. | Descrição | Valor | Classificação | Tratamento |
|---|---|---:|---|---|
| NFS-e 1181 | Desenvolvimento de software — sprint 11 | 18.000,00 | Serviço de TI | Anexo V (Fator R) |
| NFS-e 1182 | Sustentação mensal — Cliente Orla | 12.500,00 | Serviço de TI (suporte) | Anexo V |
| NFS-e 1183 | Consultoria de arquitetura | 9.800,00 | Serviço de TI | Anexo V |
| NFS-e 1184 | Desenvolvimento — módulo fiscal | 22.000,00 | Serviço de TI | Anexo V — valor bruto (glosa estornada por 1188) |
| NFS-e 1185 | Suporte técnico | 6.700,00 | Serviço de TI | Anexo V |
| NFS-e 1186 | Treinamento equipe | 4.500,00 | Serviço de TI | Anexo V (ver premissa P3) |
| NFS-e 1187 | Desenvolvimento — integração | 8.500,00 | Serviço de TI | Anexo V |
| NFS-e 1188 | Estorno parcial de 1184 (glosa de escopo) | (4.000,00) | Cancelamento/estorno | Reduz a receita de serviço de maio |
| NF-e 000.512 | Locação de 20 notebooks | 6.000,00 | **Locação de bens móveis** | **Não é serviço (SV 31)** → Anexo III, deduzida a parcela do ISS |

Bruto de serviços conferido: 18.000+12.500+9.800+22.000+6.700+4.500+8.500 = **82.000,00** = total informado na planilha de notas. O sócio sugeriu "a locação vai junto com os serviços": **não vai** — a biblioteca (L1, segregação do art. 18, §4º; L3, SV 31) exige segregação e anexo próprio.

## 2. Estorno NFS-e 1188 (glosa de escopo, R$ 4.000,00)

L1 (fecho do arquivo): não integram a receita as vendas canceladas, e *"o cancelamento/estorno de serviço reduz a receita do mês em que ocorrer"*. O estorno ocorreu e foi pago em 29/05/2026 (extrato: `PIX ENVIADO ESTORNO GLOSA — CLIENTE 1184 −4.000,00`).

- Receita de serviços de maio: 82.000,00 − 4.000,00 = **R$ 78.000,00**.
- Conferência com o extrato: recibos de 02–28/05 = 12.500+18.000+9.800+22.000+6.700+4.500+6.000+8.500 = 88.000; − 4.000 (estorno) = 84.000 líquidos recebidos = 78.000 serviços + 6.000 locação. **Fecha.**

## 3. Locação de bens móveis (NF-e 512, R$ 6.000,00)

Emissão 26/05/2026 (CFOP 5949, natOp "Locação de bens móveis"). Por L3 (art. 18, §5º-A + SV 31 + Res. CGSN 140, art. 25, §1º, V): tributada pelo **Anexo III, deduzida a parcela correspondente ao ISS** — ISS 32,50% da 4ª faixa do Anexo III (L2) **não é recolhido no DAS** dessa parcela. A competência é de maio pela emissão da nota (a data do recebimento, 26/05, é indiferente para receita; valores pagos no mês batem com o extrato).

## 4. RBT12 (12 meses anteriores a maio/2026)

`faturamento_12_meses.csv`, competências 2025-05 a 2026-04:

78.000 + 81.500 + 84.000 + 86.000 + 79.500 + 90.000 + 88.000 + 92.000 + 85.000 + 83.000 + 86.000 + 87.000 = **R$ 1.020.000,00** (L1, art. 18, §1º). A planilha está rotulada apenas como "receita_bruta"; assumi que é a receita bruta **total** da empresa, incluindo eventual locação dos meses anteriores (premissa P1).

## 5. Folha de 12 meses e Fator R

`resumo_folha_12_meses.csv` (competência, total_folha incluindo salários + pró-labore + INSS patronal/FGTS — base correta por L1, art. 26):

23.400 + 23.400 + 23.800 + 23.800 + 23.800 + 24.100 + 24.100 + 24.100 + 24.300 + 24.300 + 20.900 + 24.600 = **284.600,00**.

**Correção pelo regime de caixa:** para o Fator R a folha é o montante **pago** nos 12 meses anteriores, independentemente da competência (L1, Res. CGSN 140, art. 26, §§1º–2º). O sócio informou (email) que o **pró-labore de abril foi pago em 06/05/2026** — pagamento **fora** da janela (pagamentos de 01/05/2025 a 30/04/2026). A observação do próprio resumo ("pró-labore de abril: em aberto na data do resumo", lançada na linha 2026-03) confirma que não estava pago. Portanto:

- Folha 12 meses (base de pagamento) = 284.600,00 − 3.200,00 = **R$ 281.400,00**.
- Esse R$ 3.200,00 entra na apuração do Fator R de **junho/2026**.
- Efeitos simétricos checados no extrato: "DARF/GPS/FGTS ABR" R$ 4.700 (encargos de abril pagos em 07/05) e "FOLHA MAIO" R$ 16.600 (salários de maio) são pagamentos de maio/2026, fora da janela de maio/2026; como os encargos mensais são constantes (4.700), a defasagem de um mês nos encargos é neutra ao longo dos 12 meses, admitindo encargos de competência 2025-04 também de 4.700 (premissa P2 — indiferente na prática).

**Fator R = 281.400 ÷ 1.020.000 = 0,275882 (27,5882%).**

*Sensibilidade:* sem a correção, 284.600 ÷ 1.020.000 = 27,9020%. **Em ambos os casos < 28% → Anexo V** (o ponto de corte seria folha ≥ R$ 285.600 = 28% × 1.020.000). O anexo, portanto, não depende da correção — mas o Fator R informado sim.

## 6. Anexo e faixa

- Fator R < 28% ⇒ serviços de TI pelo **Anexo V** (L1, art. 18, §§5º-J/5º-M). O pedido do sócio ("repita o Anexo V") coincide com o resultado, mas aqui ele decorre do teste do Fator R, não da mera repetição de 2025.
- Locação de bens móveis ⇒ **Anexo III, deduzido ISS** (L3), mesmo teste de RBT12.
- RBT12 1.020.000 ⇒ **4ª faixa** nas duas tabelas (L2): Anexo V — alíquota 20,50%, PD 17.100,00; Anexo III — alíquota 16,00%, PD 35.640,00.

## 7. Alíquotas efetivas (L1, art. 18, §1º-A: (RBT12 × Alíq − PD) ÷ RBT12)

- **Anexo V:** (1.020.000 × 0,2050 − 17.100) ÷ 1.020.000 = (209.100 − 17.100) ÷ 1.020.000 = 192.000 ÷ 1.020.000 = **18,823529%**.
- **Anexo III:** (1.020.000 × 0,16 − 35.640) ÷ 1.020.000 = (163.200 − 35.640) ÷ 1.020.000 = 127.560 ÷ 1.020.000 = **12,505882%**.

## 8. DAS de maio

| Atividade | Base (maio) | Anexo/Faixa | Alíquota efetiva | Cálculo | ISS parcela deduzida | DAS |
|---|---:|---|---:|---|---:|---:|
| Serviços de TI | 78.000,00 | V, 4ª faixa | 18,823529% | 78.000 × 0,18823529 | — | **14.682,35** |
| Locação bens móveis | 6.000,00 | III, 4ª faixa | 12,505882% | 6.000 × 0,12505882 | −243,86 (= 750,35 × 32,50%) | **506,49** |

- Serviços: 78.000 × 192.000 ÷ 1.020.000 = 14.682,352941 → **14.682,35**.
- Locação: bruto Anexo III = 6.000 × 127.560 ÷ 1.020.000 = 750,352941; parcela ISS = 750,352941 × 32,50% = 243,864706 (**não recolhida**, L3); líquido = 750,352941 − 243,864706 = 506,488235 → **506,49**.
- **Total DAS = 14.682,35 + 506,49 = R$ 15.188,84** (sem arredondamento intercalar: 15.188,841176; arredondamento por truncamento-convencional ao centavo em cada parcela).

## 9. Repartição do DAS por tributo (item aberto)

- Único dado da biblioteca: repartição da **4ª faixa do Anexo III** (L2): IRPJ 4,00 · CSLL 3,50 · COFINS 14,05 · PIS 3,05 · CPP 42,75 · ISS 32,50 (%).
- Aplicada ao bruto da locação (750,35): IRPJ 30,01 · CSLL 26,26 · COFINS 105,42 · PIS 22,89 · CPP 320,78 · ISS 243,86 deduzido (não recolhido).
- **A biblioteca não contém a repartição do Anexo V** → a decomposição por tributo da parcela de serviços (14.682,35) **não pode ser calculada sem inventar números**; deixada em aberto (`ISS: null` no JSON; demais valores = parcela da locação, como declarado no campo `reparticao_observacao`).
- Inconsistência interna da biblioteca: as percentagens do Anexo III somam **99,85%**, não 100% — a soma das parcelas locação-recuperáveis (505,36) difere do líquido recolhido (506,49) em **R$ 1,13** (0,15% × 750,35). Não forcei o equilíbrio; anotado como divergência.

## 10. Premissas e limitações explícitas

- **P1** — `faturamento_12_meses.csv` = receita bruta **total** (serviços + eventual locação) dos 12 meses; não existe separação por atividade no arquivo.
- **P2** — encargos mensais constantes (4.700) também em 2025-04, o que torna neutra a defasagem de pagamento dos encargos dentro da janela.
- **P3** — NFS-e 1186 (Treinamento) tratada como serviço de TI pela enumeração exemplificativa de L1 ("desenvolvimento, licenciamento, suporte **etc.**", "entre outras"); a biblioteca não traz a lista casuística completa do §5º-B/§5º-K. Independente da classificação, a nota estaria no mesmo bloco Anexo V — sem efeito no DAS.
- **Não consta na biblioteca** (não afetado, mas registrado como não verificável): data de vencimento do DAS, lista completa das atividades do §5º-K, repartição do Anexo V, mecanismos de antecipação/sublimite. Nada disso foi citado como fato.
- Datas e valores de receitas/haveres conferidos contra `extrato_maio_2026.csv` — conciliam (seção 2).

## 11. Resumo

| Item | Valor |
|---|---:|
| RBT12 | 1.020.000,00 |
| Folha 12m (pagamentos até 30/04/2026) | 281.400,00 |
| Fator R | 27,5882% (< 28%) |
| Anexo / Faixa | **V / 4ª** |
| Alíquota nominal × PD | 20,50% × 17.100,00 |
| Alíquota efetiva serviços | 18,823529% |
| Receitas maio: serviços / locação | 78.000,00 / 6.000,00 |
| DAS serviços / locação / **total** | 14.682,35 / 506,49 / **15.188,84** |
