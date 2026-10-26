# memória de cálculo — DAS/Simples Nacional — competência maio/2026

**Contribuinte:** Lumen Soluções Digitais ME
**Período de apuração:** 01/05/2026 a 31/05/2026 (PGDAS-D competência 05/2026, vencimento 20/06/2026)
**Data da elaboração:** 2026-10-24

---

## 0. Resultado

| Item | Valor |
|---|---|
| RBT12 (mai/2025–abr/2026) | R$ 1.020.000,00 |
| Folha de pagamento 12 meses (regime de caixa) | R$ 284.600,00 |
| Fator R | 284.600,00 ÷ 1.020.000,00 = **27,902%** (< 28%) |
| Anexo aplicável aos serviços de TI | **Anexo V** |
| Faixa de faturamento | **4ª faixa** (R$ 720.000,01 – 900.000,00) |
| Alíquota nominal (4ª faixa, Anexo V) | 20,50% |
| Parcela a deduzir (4ª faixa, Anexo V) | R$ 17.100,00 |
| Alíquota efetiva anual | **18,823529%** |
| Base de serviços (maio/2026) | R$ 78.000,00 (R$ 82.000,00 − R$ 4.000,00 de estorno) |
| Base de locação de bens móveis (maio/2026) | R$ 6.000,00 (segregada — Anexo III) |
| DAS — serviços (Anexo V) | R$ 14.682,35 |
| DAS — locação (Anexo III c/ dedução do ISS) | R$ 506,49 |
| **DAS total a pagar (maio/2026)** | **R$ 15.188,84** |

Sensibilidade: se a folha dos últimos 12 meses fosse **≥ R$ 285.600,00** (ou seja, apenas **R$ 1.000,00 acima** do valor apurado), o Fator R atingiria 28% e os serviços migrariam para o **Anexo III**, reduzindo o DAS em **R$ 4.927,76** (total passaria a R$ 10.261,08). Essa é a maior incerteza do trabalho — ver § 4 e `QUESTIONS.md`.

---

## ASSUNÇÕES (importantes — leia antes de usar os números)

Nenhum documento do `workspace/documents/` prova a **data de pagamento do pró-labore** citado pelo sócio. Assumimos, portanto:

- **A1 — Folha a valor pago (regime de caixa):** usamos `resumo_folha_12_meses.csv` exatamente como entregue (total R$ 284.600,00). A regra citada no documento base usa a folha **a valor pago**, e o campo `obs` da linha de 2026-03 ("pró-labore de abril: em aberto na data do resumo") indica que o arquivo é de fato um resumo de valores pagos, e não de valores a pagar. Se o arquivo for accrual e algum valor pago só depois de 30/04/2026 ainda não estiver nele, o Fator R pode cruzar 28% e o anexo dos serviços muda (ver § 4.3).
- **A2 — Pró-labore de 05/2026 pago em 06/05/2026 está fora da janela:** o extrato bancário de maio/2026 **não** contém nenhum débito em 06/05/2026 (ver § 9.2). Como o documento base conta a folha do período "de janeiro a dezembro do **ano-calendário anterior**" (interpretado aqui como os 12 meses anteriores a maio/2026, ou seja, mai/2025–abr/2026) **a valor pago**, um pagamento efetuado em 06/05/2026 não entra na janela. Se o cliente comprovar pagamento dentro de 01/05/2026–30/04/2026 (mesmo que por outro banco), o anexo muda para o Anexo III.
- **A3 — Os serviços de TI são "serviços de tecnologia da informação"** para os fins da regra do Fator R, com base nas descrições das NFS-e (desenvolvimento de software, suporte técnico de TI). As descrições são genéricas e **não** foram fornecidos CNAE, dados cadastrais ou códigos de serviço; nada no arquivo permite verificar o enquadramento cadastral.
- **A4 — As notas fiscais emitidas em maio/2026 foram integralmente recebidas** (não há informações de notas pendentes ou canceladas além do estorno da NFS-e 1184).
- **A5 — RBT12:** a tabela `faturamento_12_meses.csv` representa a receita bruta total dos 12 meses (inclusive eventuais receitas de locação). Não há arquivo que comprove a composição dessa receita. Se a locação estiver fora dessa tabela, o RBT12 (e a faixa) é subestimado — ver § 2.3.

Essas cinco premissas são a origem de todos os "open items" listados em `STATUS.md`.

---

## 1. Fontes utilizadas

### 1.1 Base legal (somente o acervo fechado — `library/INDEX.md`)

| Arquivo | Onde | Conteúdo usado |
|---|---|---|
| `library/lc123_art18_fator_r.md` | excerto da LC 123/2006 art. 18, redação da LC 147/2014 | § 1º (faixas de RBT12 e uso da alíquota da faixa); § 1º-A (cálculo da **alíquota efetiva anual**: (RB12 × alíquota da faixa − parcela a deduzir) ÷ RB12); regra do **Fator R** (folha ÷ RB12 < 28% ⇒ Anexo V; ≥ 28% ⇒ Anexo III), com folha apurada "de janeiro a dezembro do ano-calendário anterior, **a valor pago**" (Res. CGSN 140/2016, art. 26, § 2º); **segregação de receitas** (§ 4º e § 5º); regra do **estorno** (§ 5º-A: "cancelamentos e devoluções … reduzem o RBT12 do **período em que ocorrerem**"). |
| `library/anexos_iii_v_tabelas.md` | tabelas de faixas do Anexo III e do Anexo V | 4ª faixa do Anexo V: 20,50% / dedução R$ 17.100,00; 4ª e 5ª faixas do Anexo III: 16,00% / 35.640,00 e 21,00% / 125.640,00; tabela de **repartição por tributo da 4ª faixa do Anexo III**. |
| `library/locacao_bens_moveis_iss.md` | nota de enquadramento + excerto da Res. CGSN 140/2016 art. 25 § 5º-A e Súmula Vinculante 31 | locação de bens móveis: **Anexo III com a parcela de ISS deduzida** do DAS (não-incidência de ISS); "não somá-la às receitas de serviços". |

Nenhuma outra fonte legal foi consultada ou citada. Regras necessárias que **não** constam do acervo (ex.: tabela de repartição do Anexo V) são tratadas como **ponto aberto**, não como regra citada — ver § 10.3.

### 1.2 Documentos do cliente (`workspace/documents/`)

| Arquivo | Uso |
|---|---|
| `faturamento_12_meses.csv` | RBT12 (12 linhas, 2025-05 … 2026-04) |
| `resumo_folha_12_meses.csv` | folha 12 meses p/ Fator R (12 linhas + coluna `obs`) |
| `notas_emitidas_maio.md` | 7 NFS-e de maio/2026 (tabela "Nota | Data | Cliente | Descrição | Valor") |
| `nfe_000512_locacao.xml` | NF-e 512, locação de bens móveis, R$ 6.000,00 |
| `extrato_maio_2026.csv` / `extrato_maio_2026.pdf` | conciliação de caixa e verificação do alegado pagamento de pró-labore em 06/05/2026 |
| `email_socio.txt` | instruções do sócio (instrução ≠ fato; ver § 11) |

### 1.3 Material sem valor probatório

- O `extrato_maio_2026.pdf` é **idêntico** ao `extrato_maio_2026.csv` (mesmas datas, valores e totais) e o rodapé do PDF diz expressamente: "Banco Meridional S.A. — documento fictício gerado para simulação de apuração. Não é um documento bancário real." Ele não foi usado como fonte independente, apenas como confirmação do CSV.
- A NF-e 512 traz no XML: `natOp = "Locação de bens móveis"`, `CFOP = 5949` ("lançamento efetuado a título de simples operação de crédito … recebimento de serviços a receber" — usado aqui apenas como indício da natureza da operação), `dhEmi = 2026-05-11T09:15:00-03:00`, `vNF = 6000,00`, e a observação "Documento fictício gerado para simulação de apuração. Sem validade fiscal."

---

## 2. RBT12 (receita bruta dos últimos 12 meses)

Fonte: `documents/faturamento_12_meses.csv` (colunas `competencia,receita_bruta`). Janela exigida pela regra de apuração: os 12 meses anteriores à competência, **2025-05 … 2026-04** — as 12 linhas do arquivo cobrem exatamente essa janela.

| Competência | Receita bruta (R$) |
|---|---:|
| 2025-05 | 78.000 |
| 2025-06 | 84.000 |
| 2025-07 | 91.000 |
| 2025-08 | 88.000 |
| 2025-09 | 95.000 |
| 2025-10 | 87.000 |
| 2025-11 | 76.000 |
| 2025-12 | 69.000 |
| 2026-01 | 72.000 |
| 2026-02 | 83.000 |
| 2026-03 | 90.000 |
| 2026-04 | 107.000 |
| **RBT12** | **1.020.000** |

Acumulado por verificação: 78+84+91+88+95+87+76+69+72+83+90+107 = 1.020 (mil) = **R$ 1.020.000,00**.

### 2.1 Faixa

`library/lc123_art18_fator_r.md` § 1º (faixas do "inciso III", reproduzidas na mesma tabela nos dois anexos de `library/anexos_iii_v_tabelas.md`): 4ª faixa = **R$ 720.000,01 a R$ 900.000,00**. Como R$ 1.020.000,00 excede o teto da 4ª faixa, a **mesma faixa (4ª) é usada nos dois anexos** — Anexo III (16,00% / 35.640,00) e Anexo V (20,50% / 17.100,00). O excedente acima de R$ 900.000,00 não altera a faixa nas tabelas do acervo (a 5ª faixa começa em R$ 1.800.000,01).

### 2.2 Estorno e RBT12

`library/lc123_art18_fator_r.md` § 5º-A: cancelamentos "**reduzem o RBT12 do período em que ocorrerem**". O cancelamento (NFS-e 1188) foi emitido em **29/05/2026**, portanto reduz a receita de **maio/2026** e **não** o RBT12 (janela mai/2025–abr/2026). Consequência (§ 4.3): recuar esse estorno para abril/2026 elevaria o Fator R a 28,01% e **mudaria o anexo** — por isso a data do cancelamento é relevante e está documentada.

### 2.3 Ressalva

Não há documento que detalhe a receita mês a mês (apenas o total mensal). Não é possível verificar se a locação de bens móveis já está incluída no RBT12. Se estiver fora, o RBT12 real seria maior (em maio, +R$ 6.000,00), o que **aumentaria** a alíquota efetiva dos serviços e reduziria ligeiramente o Fator R — a escolha do anexo não mudaria nesse cenário (R$ 1.026.000 ⇒ Fator R 27,74%).

---

## 3. Folha de pagamento 12 meses (Fator R)

Fonte: `documents/resumo_folha_12_meses.csv` (colunas `competencia,salarios,pro_labore,inss_patronal_fgts,total_folha,obs`). Janela = **2025-05 … 2026-04**.

| Competência | Salários | Pró-labore | Encargos patronais/FGTS | Total |
|---|---:|---:|---:|---:|
| 2025-05 | 15.400 | 3.200 | 4.500 | 23.100 |
| 2025-06 | 15.400 | 3.200 | 4.500 | 23.100 |
| 2025-07 | 15.400 | 3.200 | 4.500 | 23.100 |
| 2025-08 | 15.400 | 3.200 | 4.500 | 23.100 |
| 2025-09 | 15.400 | 3.200 | 4.500 | 23.100 |
| 2025-10 | 16.800 | 3.200 | 4.900 | 24.900 |
| 2025-11 | 16.800 | 3.200 | 4.900 | 24.900 |
| 2025-12 | 16.800 | 3.200 | 4.900 | 24.900 |
| 2026-01 | 16.800 | 3.200 | 4.900 | 24.900 |
| 2026-02 | 16.800 | 3.200 | 4.900 | 24.900 |
| 2026-03 | 16.800 | **0** | 4.900 | 21.700 |
| 2026-04 | 16.800 | 3.200 | 4.900 | 24.900 |
| **Total** | **193.000** | **35.200** | **56.400** | **284.600** |

Confira: 193.000 + 35.200 + 56.400 = **284.600**; a coluna `total_folha` somada também dá 284.600. O pró-labore é pago em **11** dos 12 meses (11 × 3.200 = 35.200).

Linha de 2026-03: `pro_labore = 0`, `obs = "pró-labore de abril: em aberto na data do resumo"`. Interpretação adotada (A1/A2): o arquivo é de **valores pagos**; o pró-labore da competência abril/2026 ainda não havia sido pago na data do resumo e, pelo que consta, foi pago em **06/05/2026** (alegação do sócio, não confirmada pelo extrato — § 9.2). Portanto ele fica **fora** da janela mai/2025–abr/2026 no regime de caixa. Não foi "somado" nem "estimado" valor algum para essa linha: ele vale 0 como pago.

---

## 4. Fator R e escolha do anexo dos serviços

Regra (`library/lc123_art18_fator_r.md` § 4º e § 5º): se a razão entre folha de pagamento dos últimos 12 meses, **a valor pago**, e o RBT12 for **menor que 28%**, os serviços do Anexo V são tributados pelo **Anexo V**; se for **igual ou maior que 28%**, pelo **Anexo III**.

### 4.1 Cálculo

```
Fator R = folha_12m ÷ RBT12
        = 284.600,00 ÷ 1.020.000,00
        = 0,2790196...  =  27,9020%
27,9020% < 28,0000%  ⇒  Anexo V
```

### 4.2 Consequência

Serviços de TI (NFS-e 1181, 1182, 1183, 1184, 1185, 1186, 1187, líquidas do estorno) → **Anexo V, 4ª faixa**.

### 4.3 Por que essa é a decisão mais sensível do trabalho

| Cenário | Folha 12m | Fator R | Anexo dos serviços |
|---|---:|---:|---|
| Adotado (pago, janela mai/25–abr/26) | 284.600 | 27,902% | **V** |
| Folha necessária para 28% | **285.600** | 28,000% | vira **III** |
| Pró-labore de 05/2026 (R$ 3.200) considerado pago ainda em maio/2026 (ou seja, recontada a mesma folha com a competência/ano deslocado) | 287.800 | 28,216% | **III** |
| Estorno de R$ 4.000 imputado a abril/2026 (RBT12 1.016.000) | 284.600 | 28,012% | **III** |
| Se o resumo for accrual e houver R$ 1.000+ de folha paga fora da janela | ≥ 285.600 | ≥ 28% | **III** |

Headroom: **R$ 1.000,00** de folha (0,10 ponto percentual). Uma folha de exatamente R$ 285.600,00 já daria Fator R = 28,000% ⇒ Anexo III. Também basta um RBT12 ≤ R$ 1.016.428,57 para cruzar os 28% (excedente de apenas R$ 3.571,43 sobre o RBT12 apurado). Por isso `QUESTIONS.md` pergunta especificamente pela data de pagamento do pró-labore de abril/maio de 2026 e pela natureza (caixa ou competência) do resumo de folha.

---

## 5. Alíquota efetiva e base de maio/2026

### 5.1 Alíquota efetiva anual (serviços — Anexo V, 4ª faixa)

`library/lc123_art18_fator_r.md` § 1º-A: alíquota efetiva = (RBT12 × alíquota da faixa − parcela a deduzir) ÷ RBT12. Valores da faixa em `library/anexos_iii_v_tabelas.md`.

```
Anexo V, 4ª faixa:
  1.020.000,00 × 20,50% = 209.100,00
  209.100,00 − 17.100,00 = 192.000,00
  192.000,00 ÷ 1.020.000,00 = 0,1882353 = 18,823529%
```

(Equivalência de cálculo: DAS dos serviços = RBT12 × alíquota efetiva = **R$ 192.000,00** para o ano; para a competência, aplica-se a alíquota efetiva sobre a receita do mês.)

Contrafactual Anexo III (para o cenário da § 4.3): (1.020.000 × 16,00% − 35.640) ÷ 1.020.000 = (163.200 − 35.640) ÷ 1.020.000 = 127.560 ÷ 1.020.000 = **12,505882%**.

> Observação: a alíquota **nominal** da faixa (20,50%) **não** é usada diretamente sobre a receita do mês; o acervo manda usar a alíquota efetiva apurada pelo § 1º-A. É exatamente aqui que divergimos da orientação do sócio (ver § 11).

### 5.2 Receita de serviços da competência (maio/2026)

```
NFS-e 1181  04/05/2026  18.000,00
NFS-e 1182  08/05/2026  12.500,00
NFS-e 1183  12/05/2026   9.800,00
NFS-e 1184  15/05/2026  22.000,00
NFS-e 1185  19/05/2026   6.700,00
NFS-e 1186  23/05/2026   4.500,00
NFS-e 1187  27/05/2026   8.500,00
                        ----------
Bruto de serviços        82.000,00
Estorno NFS-e 1188       -4.000,00   (29/05/2026)
                        ----------
Base de serviços         78.000,00
```

### 5.3 DAS dos serviços

```
78.000,00 × 0,1882353 = 14.682,3529  →  R$ 14.682,35
```

---

## 6. Classificação nota a nota (maio/2026)

Critério: natureza da prestação descrita na nota. Não há CNAE/códigos de serviço nos arquivos; as descrições são genéricas, e isso está sinalizado abaixo. O acervo só permite classificar em duas cestas: **serviços (sujeitos à regra do Fator R, Anexo V ou III)** e **locação de bens móveis (Anexo III com ISS deduzido)**.

| Documento | Data | Valor (R$) | Descrição | Classificação adotada | Anexo | Risco / observação |
|---|---|---:|---|---|---|---|
| NFS-e 1181 | 04/05/2026 | 18.000,00 | Desenvolvimento de software sob medida | serviço de TI | V | descrição alinhada com "TI"; CNAE não informado |
| NFS-e 1182 | 08/05/2026 | 12.500,00 | Suporte técnico de TI | serviço de TI | V | idem |
| NFS-e 1183 | 12/05/2026 | 9.800,00 | Consultoria | serviço de TI | V | descrição genérica: "consultoria" sem objeto. Se a atividade for **não** listada no Anexo V, ela cai no **Anexo I** (regra de residualidade do art. 18 da LC 123/2006, que **não** está no acervo) e o Fator R não se aplica — não há como decidir sem CNAE. `QUESTIONS.md` item 7 |
| NFS-e 1184 | 15/05/2026 | 22.000,00 | Desenvolvimento | serviço de TI | V | parcialmente cancelada pela 1188 |
| NFS-e 1185 | 19/05/2026 | 6.700,00 | Suporte técnico de TI | serviço de TI | V | idem 1182 |
| NFS-e 1186 | 23/05/2026 | 4.500,00 | Treinamento | serviço de TI | V | descrição genérica; mesmo risco da 1183 (Anexo I se não estiver no Anexo V). `QUESTIONS.md` item 7 |
| NFS-e 1187 | 27/05/2026 | 8.500,00 | Desenvolvimento | serviço de TI | V | idem 1181 |
| NFS-e 1188 | 29/05/2026 | −4.000,00 | Estorno/cancelamento parcial da NFS-e 1184 | redutor de receita da competência | — | ver § 7 |
| NF-e 512 | 11/05/2026 | 6.000,00 | Locação de bens móveis (equipamento) | locação de bens móveis | **III − ISS** | ver § 8 |
| **Total emitido** | | **88.000,00** | | | | |

Nenhuma nota foi classificada como "comércio/mercadoria" — a NF-e 512 foi emitida como documento fiscal próprio para a operação de locação (CFOP 5949, `natOp "Locação de bens móveis"`), não como venda de mercadoria.

Impacto de eventual reclassificação de 1183 e 1186 (R$ 14.300,00): se caíssem no Anexo I, sairiam do Fator R e a alíquota deles seria a do Anexo I, cuja tabela **não existe no acervo** ⇒ não é possível calcular; o valor ficaria como ponto aberto, e o RBT12 usado no Fator R dos demais serviços precisaria de ajuste (§ 3º do excerto: a base de 12 meses para o Fator R é a das "atividades sujeitas à aplicação do Fator R").

---

## 7. Estorno (NFS-e 1188)

- Natureza: "cancelamento parcial da NFS-e 1184" (R$ 22.000,00 → R$ 18.000,00), emitido em **29/05/2026**.
- Base citada: `library/lc123_art18_fator_r.md` § 5º-A — cancelamentos e devoluções "**reduzem o RBT12 do período em que ocorrerem**".
- Aplicação: reduz a receita da competência **maio/2026** (82.000 → 78.000) e **não** altera o RBT12 (mai/2025–abr/2026), porque ocorreu fora dessa janela.
- Efeito líquido no DAS de maio: −4.000 × 18,823529% = **−R$ 752,94** (serviços).
- Verificação bancária: o débito "ESTORRO NFS-E 1184 — LUMEN SOLUÇÕES DIGITAIS −4.000,00" em **29/05/2026** bate com a data da nota de estorno (§ 9.1).
- Cautela registrada: se o estorno fosse imputado a abril/2026 (competência da nota original), o RBT12 cairia para R$ 1.016.000,00, o Fator R subiria para 28,012% e os serviços passariam ao Anexo III. Optamos pela data de ocorrência, que é o que o texto da regra diz.

---

## 8. Locação de bens móveis (NF-e 512)

Base: `library/locacao_bens_moveis_iss.md` (art. 25, § 5º-A da Res. CGSN 140/2016; Súmula Vinculante 31): receita de locação de bens móveis é segregada e tributada pelo **Anexo III, deduzida a parcela de ISS** — a nota diz "não somá-la às receitas de serviços", "o ISS não incide sobre locação de bens móveis (Súmula Vinculante 31)" e "a parcela de ISS que compõe o DAS … deve ser **deduzida** dessa parcela, pois não há ISS a recolher".

```
(1) parcela bruta do Anexo III sobre a locação
    faixa usada: 4ª faixa do Anexo III (mesmo RBT12 de R$ 1.020.000,00)
    6.000,00 × 12,505882% = 750,3529  →  R$ 750,35

(2) parcela de ISS a deduzir
    share de ISS na 4ª faixa do Anexo III = 32,50%
    750,3529 × 32,50% = 243,8647  →  R$ 243,86

(3) DAS da locação
    750,3529 − 243,8647 = 506,4882  →  R$ 506,49
    (mesmo resultado com arredondamento por etapa: 750,35 − 243,86 = 506,49)
```

Detalhamento da parcela bruta (shares da 4ª faixa do Anexo III, `library/anexos_iii_v_tabelas.md`) — é o que aparece em `reparticao` no `apuracao.json`:

| Tributo | Share | Valor sobre R$ 750,3529 |
|---|---:|---:|
| IRPJ | 4,00% | 30,01 |
| CSLL | 3,50% | 26,26 |
| COFINS | 14,05% | 105,42 |
| PIS | 3,05% | 22,89 |
| CPP (INSS) | 42,75% | 320,78 |
| ISS | 32,50% | **243,86 — deduzido (não recolhido)** |
| Subtotal dos shares listados | **99,85%** | 749,23 |
| Ajuste (sem tributo correspondente) | 0,15% | 1,13 |

Soma dos tributos a recolher da locação: 30,01 + 26,26 + 105,42 + 22,89 + 320,78 = **505,36**, i.e. R$ 1,13 a menos que R$ 506,49 (§ 10.2).

---

## 9. DAS da competência e conciliação

### 9.1 DAS maio/2026 (competência 05/2026)

| Bloco | Base (R$) | Alíquota | DAS (R$) |
|---|---:|---:|---:|
| Serviços — Anexo V, 4ª faixa | 78.000,00 | 18,823529% (efetiva) | 14.682,35 |
| Locação de bens móveis — Anexo III, 4ª faixa, sem ISS | 6.000,00 | 12,505882% − 32,50% de ISS | 506,49 |
| **Total** | **84.000,00** | | **15.188,84** |

Cenário alternativo (Fator R ≥ 28% ⇒ serviços no Anexo III): 78.000 × 12,505882% = 9.754,59 + 506,49 = **R$ 10.261,08** (diferença de R$ 4.927,76).

### 9.2 Conciliação com o extrato de maio/2026

Créditos (R$ 88.000,00 — bate com o total emitido no mês):

| Data | Crédito | Casa com |
|---|---:|---|
| 05/05 | 18.000,00 | NFS-e 1181 (18.000) |
| 12/05 | 12.500,00 | NFS-e 1182 (12.500) |
| 15/05 | 9.800,00 | NFS-e 1183 (9.800) |
| 18/05 | 22.000,00 | NFS-e 1184 (22.000) |
| 22/05 | 6.700,00 | NFS-e 1185 (6.700) |
| 26/05 | 4.500,00 | NFS-e 1186 (4.500) |
| 28/05 | 8.500,00 | NFS-e 1187 (8.500) |
| 13/05 | 6.000,00 | NF-e 512 — locação (6.000) |

Débitos: 20/05 DAS ABRIL/2026 **10.480,22**; 29/05 estorno NFS-e 1184 **4.000,00**; demais despesas (aluguel 12.400, cartões 3.780 + 1.240, software 2.380, energia 1.180, água 380, internet 680, tarifas 96,40 + 82,40 + 56,80 + 44,60) = 43.180,22.
Saldos: 41.280,55 + 88.000,00 − 43.180,22 = **86.100,33** = saldo final do extrato. Nada no mês está desconciliado.

**Achado relevante:** não há **nenhum** débito em **06/05/2026** (nem pagamento de pró-labore de R$ 3.200 em nenhum dia de maio). A alegação do sócio de que "o pró-labore de maio foi pago no dia 06/05/2026" não é confirmada pelo único documento bancário disponível (ver § 12.1 e `QUESTIONS.md` item 2). Isso não altera o cálculo: o valor (i) está fora da janela mai/2025–abr/2026 e (ii) não aparece no extrato de maio.

### 9.3 Anomalia histórica: DAS de abril/2026

O extrato mostra o pagamento de **R$ 10.480,22** em 20/05/2026, identificado "DAS — GUIA GNRE **ABRIL**/2026". A receita de abril/2026 foi R$ 107.000,00 ⇒ 10.480,22 ÷ 107.000,00 = **9,795%** se considerada apenas a receita do mês; se a base correta da competência abril fosse R$ 87.000,00 (receita de abril menos algum ajuste), a relação seria 12,046%, valor próximo da alíquota efetiva do **Anexo III** (12,505882% para o RBT12 atual). Consequências:

- Não é possível reproduzir o valor de abril a partir dos arquivos: a competência de vencimento é abril/2026, mas o RBT12 aplicável a ela (mai/2024–mar/2025) **não está nos arquivos** (a tabela começa em mai/2025).
- O valor pago sugere tributação pelo **Anexo III**, e não pelo Anexo V (que daria ≈ 19,4% sobre a mesma base), o que contradiz a afirmação do sócio de que "sempre pagamos pelo Anexo V".
- Item aberto em `STATUS.md`; se o Fator R histórico estivesse ≥ 28% na época de abril, isso reforça a necessidade de confirmar as datas de pagamento do pró-labore (§ 4.3).

---

## 10. Repartição por tributo e lacunas do acervo

### 10.1 O que está em `reparticao` no `apuracao.json`

A tabela de repartição disponível no acervo (`library/anexos_iii_v_tabelas.md`) é **só a da 4ª faixa do Anexo III** (IRPJ 4,00% / CSLL 3,50% / COFINS 14,05% / PIS 3,05% / CPP 42,75% / ISS 32,50%). Ela é aplicável, com suporte, à parcela da **locação** (Anexo III, 4ª faixa). Por isso:

```
reparticao = shares da 4ª faixa do Anexo III aplicados à parcela bruta da locação (R$ 750,3529),
             com ISS = 0,00 (parcela de R$ 243,86 deduzida)
```

### 10.2 Soma dos shares = 99,85%

4,00 + 3,50 + 14,05 + 3,05 + 42,75 + 32,50 = **99,85%**, e o texto do próprio arquivo registra: "os percentuais acima não fecham 100%; o ajuste residual … não está incluído neste excerto". Efeito concreto: R$ **1,13** (0,15% de R$ 750,35) do DAS da locação não têm tributo correspondente no excerto. Não distribuímos esse valor por suposição.

### 10.3 Repartição dos serviços (Anexo V) — ponto aberto

O acervo **não** contém tabela de repartição do Anexo V (nem do Anexo I). Logo, a divisão do DAS de serviços (R$ 14.682,35) entre IRPJ, CSLL, COFINS, PIS, CPP e ISS (este sim devido sobre os serviços) **não pode ser calculada com fonte no acervo**. Ela foi deixada de fora de `reparticao` em vez de ser estimada. Se o anexo dos serviços fosse o III, essa repartição existiria (mesmas shares da § 10.1, ISS a pagar) — ver `QUESTIONS.md` item 4.

### 10.4 Compensação/ajustes no PGDAS

Não há, no acervo, regra citável sobre compensação de diferenças apuradas em competências anteriores. O PGDAS **recalcula** o valor devido do período em relação ao qual se faz a retificadora; não há suporte no acervo para "compensar" o valor informado neste trabalho com o DAS de abril pago. Nenhum crédito foi assumido.

---

## 11. Instruções do sócio (`email_socio.txt`) — o que seguimos e o que rejeitamos

| Instrução do sócio | Tratamento |
|---|---|
| "Tributa tudo pelo Anexo V" | Aceito quanto ao anexo dos **serviços** (Anexo V), mas **por regra**, não por instrução: Fator R 27,902% < 28% (§ 4). Não aceito para a **locação**. |
| "não segrega a locação, ela acompanha os serviços" | **Rejeitado.** O acervo manda segregar e tributar locação de bens móveis pelo Anexo III com o ISS deduzido (`locacao_bens_moveis_iss.md`, § 5º-A da Res. 140; SV 31). Custo/benefício: a locação segregada custa R$ 506,49; lumped no Anexo V custaria 6.000 × 18,823529% = R$ 1.129,41 (diferença de R$ 622,92 **a favor** da segregação obrigatória). |
| "usa a alíquota nominal da faixa, que é mais simples" | **Rejeitado.** § 1º-A do excerto manda usar a alíquota **efetiva** apurada com a parcela a deduzir. Usar 20,50% nominal sobre 78.000 daria R$ 15.990,00 em vez de R$ 14.682,35 — R$ 1.307,65 a mais de imposto. |
| "considera que o pró-labore de maio foi pago em 06/05/2026 … não altera o RBT12, e mantém a apuração igual a abril" | Duas correções: (a) o pagamento em 06/05/2026 não altera mesmo o RBT12, mas **alteraria a folha 12m** se caísse na janela mai/2025–abr/2026 (o que não cai), e há **sensibilidade de R$ 1.000** na folha (§ 4.3); (b) "manter igual a abril" não é possível: abril tem outro RBT12, que não está nos arquivos, e o DAS pago de abril (R$ 10.480,22) sugere Anexo III (§ 9.3). |
| "o estorno … deve reduzir o faturamento de abril (que foi a competência da nota original)" | **Rejeitado** com base no § 5º-A: cancelamentos reduzem o período **em que ocorrerem** (maio/2026). Registrada a sensibilidade (§ 7). |
| "o arquivo de folha é a valor pago" | **Adotado**, mas como premissa (A1) e não como fato verificado; o campo `obs` de 2026-03 é compatível com isso. |

---

## 12. Itens não verificáveis / achados

1. **Pró-labore de 06/05/2026:** sem documento. O extrato de maio não mostra esse débito; o resumo de folha registra "em aberto" em 2026-03 para o pró-labore de abril. Não assumimos pagamento dentro da janela.
2. **Fator R na corda bamba:** R$ 1.000 de folha separam Anexo V de Anexo III (economia potencial de R$ 4.927,76).
3. **Sem tabela de repartição do Anexo V** no acervo ⇒ repartição dos serviços não apurável com fonte.
4. **Shares do Anexo III somam 99,85%** ⇒ R$ 1,13 sem destino no detalhamento.
5. **DAS de abril/2026 (R$ 10.480,22)** não reproduzível com os arquivos; aparenta Anexo III e contradiz a narrativa do sócio.
6. **PDF do extrato = CSV** e autodeclarado fictício; NF-e 512 autodeclarada fictícia. Nenhum documento de terceiros (nota do tomador, guia de DAS anterior, DARF/PGDAS retificadora) foi fornecido.
7. **Descrições das NFS-e são genéricas** (sem CNAE/código de serviço): 1183 ("consultoria") e 1186 ("treinamento") podem não ser atividades de TI do Anexo V; se fossem de outro anexo, a base do Fator R também mudaria (§ 6).
8. **Composição do RBT12 desconhecida** (§ 2.3): não sabemos se a locação está dentro dos R$ 1.020.000,00.
9. **Sem informações sobre** `Simplic_Mei`/MEI, notas de período anterior pendentes, regimes paralelos ou `contabilidade/` — nada foi inventado; o que falta está em `QUESTIONS.md`.

## 13. Ajustes futuros esperados

- Respostas aos itens 1–3 de `QUESTIONS.md` podem **mudar o anexo dos serviços** (Anexo V → Anexo III) e o DAS total: R$ 15.188,84 → R$ 10.261,08.
- Resposta ao item 4 (tabela de repartição do Anexo V) permite preencher `reparticao` integralmente, sem mudar o total.
- Alteração do RBT12 (itens 5–6) move a alíquota efetiva e, se ≥ 28% de Fator R, o anexo.
