# Memória de cálculo — DAS de maio/2026 — Lumen Soluções Digitais ME (CRT 1, Simples Nacional)

Apuração do período de apuração **maio/2026**. Todos os valores em reais.
Autoria: apuração sobre os documentos recebidos (`workspace/documents/`) usando **exclusivamente** a
biblioteca fechada (`workspace/library/`, ver `library/INDEX.md`). Nada além do que está aqui foi
usado; o que não tem suporte na biblioteca está marcado como **não verificado** ou como **premissa**.

**Resultado (resumo):** Fator R = 27,9020% (< 28%) → **Anexo V**, 4ª faixa, alíquota efetiva
**18,823529%** sobre os serviços; locação de bens móveis segregada e tributada pelo **Anexo III sem a
parcela de ISS** (8,441500%). **DAS total de maio/2026 = R$ 15.188,84** (serviços 14.682,35 + locação
506,49). A classificação em Anexo V é de fronteira: faltam **R$ 1.000** de folha paga na janela para o
resultado mudar para Anexo III (−R$ 4.927,76 de DAS). Ver §5 e `QUESTIONS.md`.

---

## 1. Fontes

### 1.1 Biblioteca (única autoridade citável — `library/INDEX.md`)

| Arquivo | Citação (conforme o índice) | Uso nesta apuração |
|---|---|---|
| `library/lc123_art18_fator_r.md` | LC 123/2006, art. 18, §§1º, 1º-A, 5º-J, 5º-K, 5º-M; Resolução CGSN 140/2018, arts. 25, 26 | conceito de RBT12 (§1º); fórmula da alíquota efetiva (§1º-A); Fator R 28% (§5º-J/5º-M); folha = valores **pagos** nos 12 meses anteriores, independentemente da competência (Res. CGSN 140, art. 26, §§1º-2º); segregação de receitas por atividade (§4º); estorno/cancelamento reduz a receita do mês em que ocorrer |
| `library/anexos_iii_v_tabelas.md` | LC 123/2006, Anexos III e V (redação LC 155/2016) | faixas, alíquotas nominais e parcelas a deduzir dos Anexos III e V; percentual de ISS (32,50%) da repartição da 4ª faixa do Anexo III |
| `library/locacao_bens_moveis_iss.md` | LC 123/2006, art. 18, §5º-A; Súmula Vinculante 31 (STF); Res. CGSN 140, art. 25, §1º, V | locação de bens móveis: Anexo III **deduzida a parcela correspondente ao ISS** |

Observação de integridade da biblioteca: o arquivo `lc123_art18_fator_r.md` traz no corpo dispositivos
(§4º — segregação; devoluções/cancelamentos) que não aparecem na linha de citação do próprio arquivo
(que enumera §§1º, 1º-A, 5º-J, 5º-K, 5º-M). Citei o arquivo, não um parágrafo adicional que a
biblioteca não documenta.

### 1.2 Documentos do cliente (base de fato, não de direito)

`documents/faturamento_12_meses.csv` · `documents/resumo_folha_12_meses.csv` ·
`documents/notas_emitidas_maio.md` · `documents/nfe_000512_locacao.xml` ·
`documents/extrato_maio_2026.csv` (conferido contra `documents/extrato_maio_2026.pdf`) ·
`documents/email_socio.txt`.

---

## 2. Passo 1 — RBT12 (receita bruta dos 12 meses anteriores)

Janela definida por LC 123/2006, art. 18, §1º (`library/lc123_art18_fator_r.md`): receita bruta
acumulada nos **12 meses anteriores** ao período de apuração → **mai/2025 a abr/2026**, exatamente o
intervalo do arquivo `faturamento_12_meses.csv` (12 linhas, sem lacunas).

| Competência | Receita |
|---|---:|
| 2025-05 | 78.000 |
| 2025-06 | 81.500 |
| 2025-07 | 84.000 |
| 2025-08 | 86.000 |
| 2025-09 | 79.500 |
| 2025-10 | 90.000 |
| 2025-11 | 88.000 |
| 2025-12 | 92.000 |
| 2026-01 | 85.000 |
| 2026-02 | 83.000 |
| 2026-03 | 86.000 |
| 2026-04 | 87.000 |
| **RBT12** | **1.020.000** |

Aritmética: 78.000+81.500+84.000+86.000+79.500+90.000+88.000+92.000+85.000+83.000+86.000+87.000 = **1.020.000**.

- A receita de **maio/2026 não entra** no RBT12 de maio/2026 (só afeta as apurações de junho/2026 em diante).
- O RBT12 é único e vale para as duas atividades (é a receita bruta total, não por atividade); a
  separação por atividade ocorre na escolha do anexo/alíquota (§4º), não na base de 12 meses.
- **Premissa não verificável:** o arquivo traz "receita_bruta" por competência, sem informar se os
  cancelamentos/estornos de cada mês já foram líquidos nem se as receitas de locação dos meses
  anteriores já estão incluídas. Assumido que sim (é o dado de faturamento da empresa). Ver `QUESTIONS.md` Q6.

## 3. Passo 2 — Folha de salários dos 12 meses (folha_12m)

Base: `resumo_folha_12_meses.csv` (mesma janela mai/2025–abr/2026), coluna por coluna:

| Competência | Salários | Pró-labore | INSS patronal + FGTS | Total |
|---|---:|---:|---:|---:|
| 2025-05 | 15.500 | 3.200 | 4.700 | 23.400 |
| 2025-06 | 15.500 | 3.200 | 4.700 | 23.400 |
| 2025-07 | 15.900 | 3.200 | 4.700 | 23.800 |
| 2025-08 | 15.900 | 3.200 | 4.700 | 23.800 |
| 2025-09 | 15.900 | 3.200 | 4.700 | 23.800 |
| 2025-10 | 16.200 | 3.200 | 4.700 | 24.100 |
| 2025-11 | 16.200 | 3.200 | 4.700 | 24.100 |
| 2025-12 | 16.200 | 3.200 | 4.700 | 24.100 |
| 2026-01 | 16.400 | 3.200 | 4.700 | 24.300 |
| 2026-02 | 16.400 | 3.200 | 4.700 | 24.300 |
| 2026-03 | 16.200 | **0** | 4.700 | 20.900 |
| 2026-04 | 16.700 | 3.200 | 4.700 | 24.600 |
| **Total** | **193.000** | **35.200** | **56.400** | **284.600** |

Confere com a coluna `total_folha` do arquivo (a soma das linhas é 284.600).

Componentes aceitos pela biblioteca: salários, retiradas de pró-labore, contribuições patronais e FGTS
(Res. CGSN 140/2018, art. 26, §1º, em `library/lc123_art18_fator_r.md`) — os três campos do resumo
cobrem exatamente esses componentes.

**Ressalva relevante (é o ponto sensível da apuração):** a mesma fonte manda considerar o montante
**pago** nos 12 meses anteriores, "independentemente do mês de competência" (art. 26, §2º). O resumo
vem por **competência**, e (a) a linha 2026-03 traz pró-labore **zero** com a observação
"pró-labore de abril: em aberto na data do resumo"; (b) o sócio diz no e-mail que o pró-labore de
abril foi pago **em 06/05/2026** — pagamento fora da janela mai/2025–abr/2026. Portanto:

- Se o pró-labore de abril (R$ 3.200) foi pago em 06/05/2026, ele **não** compõe a folha de maio/2026
  (entra na janela de junho/2026, que é jun/2025–mai/2026) → folha = **281.400**.
- Se houve pró-labore de alguma competência efetivamente pago dentro da janela que o resumo não
  registrou (p. ex. o de março) → folha poderia chegar a **287.800**.
- Não há no arquivo a informação de datas de pagamento; os dois casos estão quantificados no §5.

Uso, como valor principal, **folha_12m = 284.600**, que é o próprio total do resumo do cliente (e é o
teto da janela: nenhum cenário com pagamento em maio/2026 aumenta esse número).

## 4. Passo 3 — Fator R e escolha do anexo

Fórmula e limiar: razão folha/receita bruta dos 12 meses anteriores ≥ **28%** → Anexo III; caso
contrário → Anexo V (LC 123/2006, art. 18, §5º-J/§5º-M, `library/lc123_art18_fator_r.md`).

```
fator_r = 284.600 / 1.020.000 = 0,2790196078 = 27,9020%  <  28%  →  ANEXO V
limiar em reais: 0,28 × 1.020.000 = 285.600   →  faltam 1.000 de folha paga na janela
```

Consequências para o pedido do sócio ("é só repetir o Anexo V com a alíquota da faixa"):

1. O anexo **não é herdado**: a biblioteca condiciona Anexo III × Anexo V ao teste do Fator R sobre os
   12 meses anteriores a cada período de apuração. O resultado até dá Anexo V, mas pelo teste — e por
   uma margem de R$ 1.000, não por hábito.
2. O que se aplica **não é a alíquota da faixa (20,50%)**, e sim a **alíquota efetiva** apurada pela
   fórmula do §1º-A (18,823529%). Ver §6.
3. A locação de notebooks **não vai junto com os serviços**: a receita é segregada por atividade (§4º)
   e tem anexo/alíquota próprios (§5º-A). Ver §7.

## 5. Passo 4 — Sensibilidade (por que a folha precisa ser conferida antes de pagar)

| Cenário para a folha paga na janela mai/2025–abr/2026 | folha_12m | Fator R | Anexo | Alíq. efetiva | DAS serviços (78.000) | DAS locação (6.000) | DAS total |
|---|---:|---:|---|---:|---:|---:|---:|
| Resumo como enviado (usado nesta apuração) | 284.600 | 27,9020% | **V** | 18,823529% | 14.682,35 | 506,49 | **15.188,84** |
| Menos o pró-labore de abril pago em 06/05 (fora da janela) | 281.400 | 27,5882% | V | 18,823529% | 14.682,35 | 506,49 | 15.188,84 |
| Mais um pró-labore de 3.200 pago dentro da janela | 287.800 | 28,2157% | III | 12,505882% | 9.754,59 | 506,49 | 10.261,08 |

A alíquota efetiva não muda entre os cenários de 284.600 e 281.400 porque a fórmula do §1º-A depende do
RBT12, não da folha; o que muda é o **anexo**. Traduzindo: **R$ 1.000** de folha paga dentro da janela
valem **R$ 4.927,76** de DAS. Daí as perguntas Q1–Q3 do `QUESTIONS.md`.

## 6. Passo 5 — Faixa e alíquota dos serviços (Anexo V)

`library/anexos_iii_v_tabelas.md`, Anexo V: RBT12 1.020.000 cai na **4ª faixa**
(acima de 720.000 e até 1.800.000) → alíquota nominal **20,50%**, parcela a deduzir **17.100,00**.

Alíquota efetiva (LC 123/2006, art. 18, §1º-A: `(RBT12 × Aliq − PD) / RBT12`):

```
1.020.000 × 0,2050 = 209.100,00
209.100,00 − 17.100,00 = 192.000,00
192.000,00 / 1.020.000 = 0,1882352941 = 18,823529%
```

DAS dos serviços (base líquida do mês, §7):

```
78.000,00 × 0,1882352941 = 14.682,3529…  →  R$ 14.682,35
```

## 7. Passo 6 — Receita de maio/2026: classificação de cada documento

Base: `notas_emitidas_maio.md`, cruzada com `extrato_maio_2026.csv`/`.pdf` e `nfe_000512_locacao.xml`.

| Documento | Descrição | Valor | Classificação na apuração | Enquadramento |
|---|---|---:|---|---|
| NFS-e 1181 | Desenvolvimento de software — sprint 11 | 18.000,00 | serviço de TI (desenvolvimento) | Anexo V, 4ª faixa (§5º-J; "desenvolvimento" está expresso na biblioteca) |
| NFS-e 1182 | Sustentação mensal — Cliente Orla | 12.500,00 | serviço de TI (suporte/sustentação) | Anexo V, 4ª faixa ("suporte" expresso na biblioteca) |
| NFS-e 1183 | Consultoria de arquitetura | 9.800,00 | serviço — tratado como serviço de TI (premissa) | ver nota (a) |
| NFS-e 1184 | Desenvolvimento — módulo fiscal | 22.000,00 | serviço de TI; reduzido pelo estorno da NFS-e 1188 | Anexo V, 4ª faixa |
| NFS-e 1185 | Suporte técnico | 6.700,00 | serviço de TI | Anexo V, 4ª faixa |
| NFS-e 1186 | Treinamento equipe | 4.500,00 | serviço — tratado como serviço de TI (premissa) | ver nota (a) |
| NFS-e 1187 | Desenvolvimento — integração | 8.500,00 | serviço de TI | Anexo V, 4ª faixa |
| **NFS-e 1188** | **Estorno parcial (glosa) da 1184** | **(4.000,00)** | **cancelamento/estorno de serviço: reduz a receita do mês em que ocorre (mai/2026)** | mesma atividade da nota estornada (Anexo V) |
| **NF-e 000.512** | **Locação de 20 notebooks — maio** | **6.000,00** | **locação de bens móveis: receita segregada, sem ISS** | Anexo III, 4ª faixa, menos parcela de ISS (§5º-A + Súmula Vinculante 31) |

Notas:

- **(a) Premissa sobre 1183 e 1186.** O trecho da biblioteca enumera "desenvolvimento, licenciamento,
  suporte etc." como atividades de TI sujeitas ao Fator R, sem fechar a lista. Assumi que consultoria
  de arquitetura e treinamento de equipe entram nessa lista. Isso **não altera maio/2026**: como o Fator
  R ficou abaixo de 28%, ambas as atividades sairiam em Anexo V de qualquer forma. A premissa só passa a
  importar se o Fator R virar ≥ 28% (aí a alíquota aplicável a esses R$ 14.300 poderia não ser a do
  Anexo III). Pedidos de confirmação de CNAE/descrição fiscal em `QUESTIONS.md` Q5.
- **Estorno (o que foi feito).** O R$ 4.000 glosado saiu **da receita de maio/2026** (a biblioteca trata
  cancelamento/estorno como redutor do mês em que ocorre) e não do mês de emissão da 1184. Efeito:
  serviços brutos 82.000 → **78.000 líquidos**. O banco confirma o desembolso em 29/05/2026
  ("PIX ENVIADO ESTORNO GLOSA — CLIENTE 1184", −4.000,00). O estorno **não** altera o RBT12 de
  maio/2026 (janela encerrada em abr/2026), mas reduz a receita de mai/2026 que entrará no RBT12 das
  apurações seguintes. Consequência prática: 1184 passa a gerar receita líquida de 18.000,00.
- **Locação (o que foi feito).** Os 6.000,00 da NF-e 512 **não** foram somados aos serviços. Foram
  segregados (art. 18, §4º) e tributados à parte, sem ISS (art. 18, §5º-A; Súmula Vinculante 31),
  conforme §8. O e-mail do sócio ("acho que vai junto com os serviços") não corresponde à biblioteca.
- **Conferência com o extrato (mai/2026).** Créditos: 12.500 + 18.000 + 9.800 + 22.000 + 6.700 + 4.500 +
  6.000 + 8.500 = **88.000,00** = 82.000 (notas de serviço) + 6.000 (locação) ✔ (bate com o
  "Total credits R$ 88.000,00" do PDF). Débitos: 16.600 + 4.700 + 4.200 + 1.600 + 1.600 + 10.480,22 +
  4.000 = **43.180,22** ✔ (bate com o PDF). Receita líquida fiscal de maio = 88.000 − 4.000 =
  **84.000,00** (= 78.000 serviços + 6.000 locação).
- O aluguel de escritório (−4.200,00) **não** reduz a receita bruta: despesa, não devolução/cancelamento
  de receita. Nenhum dos itens do extrato foi tratado como receita.
- **Não verificado / fora da biblioteca:** a NF-e 512 traz PIS 0,65% e COFINS 3,00% com CST 01, como se a
  empresa estuvera na regra geral (e o próprio XML diz "documento fictício... sem validade fiscal");
  no Simples Nacional essas contribuições vêm dentro do DAS. A biblioteca não trata de NF-e/CST, então
  apenas registro a inconsistência e pergunto ao cliente (`QUESTIONS.md` Q7). Não altera a apuração.

## 8. Passo 7 — Alíquota e DAS da locação de bens móveis

Regra (`library/locacao_bens_moveis_iss.md`): locação de bens móveis é tributada "na forma do **Anexo
III, deduzida a parcela correspondente ao ISS**", porque não é serviço para fins de ISS
(Súmula Vinculante 31; art. 18, §5º-A).

```
Anexo III, 4ª faixa (RBT12 1.020.000): nominal 16,00%, PD 35.640,00   [anexos_iii_v_tabelas.md]
alíquota efetiva do Anexo III = (1.020.000 × 0,16 − 35.640) / 1.020.000
                              = (163.200 − 35.640) / 1.020.000
                              = 127.560 / 1.020.000 = 0,1250588235 = 12,505882%
ISS da 4ª faixa do Anexo III (repartição) = 32,50%
alíquota aplicável = 12,505882% × (1 − 0,325) = 0,0844147059 = 8,441500%   ← critério adotado
DAS locação = 6.000,00 × 0,0844147059 = 506,4882… → R$ 506,49
```

**Leitura alternativa (aberta, não resolvida):** a biblioteca não explicita se a parcela de ISS é
deduzida proporcionalmente à alíquota efetiva (critério adotado acima) ou sobre a alíquota nominal:

```
12,505882% − (32,50% × 16,00%) = 12,505882% − 5,200000% = 7,305882%  →  6.000 × 7,305882% = R$ 438,35
```

Diferença entre as duas leituras: **R$ 68,14** no DAS de maio. Adotei a primeira porque a expressão
"deduzida a parcela **correspondente ao ISS**" aponta para a fatia do próprio valor devido, e registro a
dúvida em `QUESTIONS.md` Q5 para o cliente confirmar a mecânica usada no PGDAS-D.

## 9. Passo 8 — DAS de maio/2026

| Atividade | Base (mai/2026) | Anexo | Faixa | Alíq. efetiva | DAS |
|---|---:|---|---|---:|---:|
| Serviços de TI (7 NFS-e, líquido do estorno) | 78.000,00 | V | 4 | 18,823529% | **14.682,35** |
| Locação de bens móveis (NF-e 512) | 6.000,00 | III (sem ISS) | 4 | 8,441500% | **506,49** |
| **Total DAS maio/2026** | **84.000,00** | — | — | alíq. global 18,0820% | **15.188,84** |

```
14.682,35 + 506,49 = 15.188,84
alíquota global = 15.188,84 / 84.000 = 18,0819% (informativo)
```

Custo de seguir literalmente o pedido do sócio (Anexo V, alíquota nominal de 20,50% sobre tudo, sem
segregar a locação):

```
84.000,00 × 0,2050 = 17.220,00   →   17.220,00 − 15.188,84 = R$ 2.031,16 a mais
   (1.307,65 por usar 20,50% em vez da alíquota efetiva; 723,51 por tributar a locação no Anexo V)
```

## 10. Repartição dos tributos (campo `reparticao` do `apuracao.json`)

**Não apurável para os serviços com a autoridade disponível.** A biblioteca traz a repartição apenas da
**4ª faixa do Anexo III** (IRPJ 4,00% · CSLL 3,50% · COFINS 14,05% · PIS 3,05% · CPP 42,75% ·
ISS 32,50%) e **não traz a tabela de repartição do Anexo V**. Como os R$ 14.682,35 de serviços saem pelo
Anexo V, não há como decompor IRPJ/CSLL/COFINS/PIS/CPP sem inventar percentuais — por isso os campos
ficam `null` em `apuracao.json` (null = não apurado, **não** zero apurado) e o item foi levado a
`QUESTIONS.md` Q4.

O que é possível documentar com a biblioteca é o componente da **locação** (Anexo III, 4ª faixa), sobre
a alíquota cheia de 12,505882% (base teórica 6.000 × 12,505882% = 750,35):

| Tributo | % (Anexo III, 4ª faixa) | Valor sobre 750,35 |
|---|---:|---:|
| IRPJ | 4,00% | 30,01 |
| CSLL | 3,50% | 26,26 |
| COFINS | 14,05% | 105,42 |
| PIS | 3,05% | 22,89 |
| CPP | 42,75% | 320,78 |
| ISS | 32,50% | 243,86 → **excluído** (locação de bens móveis não comporta ISS) |
| Subtotal sem ISS | 67,35% | **505,36** (DAS praticado: 506,49) |

**Descasamento assumido, não corrigido:** os percentuais do Anexo III, 4ª faixa, somam **99,85%**, não
100%. Aplicados à base, somam 749,23 contra 750,35 (diferença de **1,13**), e o subtotal "sem ISS" fica
505,36 contra os 506,49 efetivamente apurados (diferença de **1,13**). Não forcei nada para fechar: ou a
linha de repartição da biblioteca está incompleta, ou a base de aplicação dos percentuais é outra. Ver
`QUESTIONS.md` Q5/Q4.

## 11. Observação sobre o histórico (não usada na apuração)

O extrato mostra o pagamento de **DAS ABR/2026 = 10.480,22** em 20/05/2026. Com receita de abril de
86.000,00 (arquivo de faturamento), isso implica alíquota efetiva de 10.480,22 / 86.000 = **12,186%**.
Para abril, o RBT12 seria abr/2025–mar/2026 = 1.020.000 − 87.000 = **933.000**, o que daria:

```
Anexo III, 4ª faixa:  (933.000 × 0,16 − 35.640) / 933.000 = 12,1801%  →  86.000 × 12,1801% ≈ 10.474,86
Anexo V,   4ª faixa:  (933.000 × 0,205 − 17.100) / 933.000 = 18,6672% →  86.000 × 18,6672% ≈ 16.053,79
```

O valor pago é compatível com **Anexo III** em abril (diferença de 5,36, explicable por composição de
receita/mix que não temos), e não com Anexo V. Ou seja: a memória do sócio ("ano passado a gente pagava
pelo Anexo V") não se confirma para abril/2026 — mais um motivo para não herdar anexo. **Não verificado:**
não temos as notas, o PGDAS-D nem o RBT12 efetivo de abril; fica como pergunta (Q8).

## 12. O que NÃO foi feito / limites desta apuração

- Não se apurou repartição do Anexo V (tabela ausente na biblioteca) — item aberto.
- Não se refez a apuração de abril/2026 nem de exercícios anteriores (documentos ausentes).
- Nenhum ajuste, dedução ou compensação fora da biblioteca foi aplicado (p. ex. eventual dedução do
  INSS patronal pago do CPP: a biblioteca não trata disso, então não foi considerado). Nada no arquivo
  indica sublimites estaduais/municipais, ICMS, ou regime diverso — a biblioteca não traz essas regras
  e elas **não foram verificadas**.
- Data de vencimento do DAS: não está na biblioteca; apenas observo que o extrato mostra o DAS de abril
  pago em 20/05/2026.
- Valores de alíquota foram mantidos em precisão cheia no cálculo e arredondados a 2 casas apenas no
  valor final do DAS (arredondamento comercial, half-up).

## 13. Itens abertos (detalhados em `QUESTIONS.md`)

(A numeração abaixo é a desta lista; entre parênteses, o número da pergunta em `QUESTIONS.md`.)

1. Datas de **pagamento** da folha (salários, pró-labore, INSS patronal, FGTS) na janela mai/2025–abr/2026 —
   mudam o Anexo (V → III) se a folha paga for ≥ 285.600 (faltam 1.000). Impacto: −4.927,76 de DAS. (Q1–Q3)
2. Situação do pró-labore de mar/2026 (linha zerada no resumo) e do de abr/2026 (e-mail diz pago em
   06/05; extrato não mostra pagamento nessa data; o de 16/05 está rotulado "MAI"). (Q2)
3. Mecânica da dedução do ISS na locação de bens móveis (8,4415% adotado × 7,3059% alternativo) e a
   soma de 99,85% da repartição do Anexo III, 4ª faixa. Impacto: R$ 68,14. (Q5b e Q4)
4. Tabela de repartição do Anexo V, 4ª faixa (ausente na biblioteca) para preencher o campo `reparticao`. (Q4)
5. CNAE/descrição fiscal de "consultoria de arquitetura" e "treinamento equipe" (premissa do item (a)). (Q5a)
6. Natureza do `faturamento_12_meses.csv` (receita líquida de estornos? inclui locação histórica?). (Q6)
7. NF-e 512 com destaque de PIS/COFINS e anotação "sem validade fiscal". (Q7)
8. Base do DAS de abril (10.480,22) aparentando Anexo III, contra o histórico de Anexo V citado pelo sócio. (Q8)
