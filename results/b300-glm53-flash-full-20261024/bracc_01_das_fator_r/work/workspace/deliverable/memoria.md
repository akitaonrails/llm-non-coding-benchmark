# Memória de cálculo — DAS maio/2026 · Lumen Soluções Digitais ME

Apuração feita exclusivamente com os arquivos de `documents/` e a biblioteca `library/`
(`INDEX.md`). Moeda em R$. Fontes citadas por arquivo da biblioteca:

- **[FATOR-R]** `library/lc123_art18_fator_r.md` — LC 123/2006, art. 18, §§1º, 1º-A, 5º-J, 5º-M; Res. CGSN 140/2018, arts. 25, 26.
- **[TABELAS]** `library/anexos_iii_v_tabelas.md` — Anexos III e V da LC 123/2006 (redação LC 155/2016).
- **[LOCACAO]** `library/locacao_bens_moveis_iss.md` — LC 123/2006, art. 18, §5º-A; Súmula Vinculante 31; Res. CGSN 140, art. 25, §1º, V.

---

## 1. RBT12 — receita bruta dos 12 meses anteriores (mai/2025–abr/2026)

**[FATOR-R]** §1º: RBT12 = receita bruta acumulada nos 12 meses anteriores ao do período de apuração.
A janela é mai/2025–abr/2026 — exatamente o intervalo de `faturamento_12_meses.csv` (mai/2026, do
período de apuração, fica de fora).

| Mês | Receita (R$) | | Mês | Receita (R$) | | Mês | Receita (R$) | | Mês | Receita (R$) |
|---|---:|---|---|---:|---|---|---:|---|---|---:|
| 2025-05 | 78.000,00 | | 2025-09 | 79.500,00 | | 2026-01 | 85.000,00 | | 2026-04 | 87.000,00 |
| 2025-06 | 81.500,00 | | 2025-10 | 90.000,00 | | 2026-02 | 83.000,00 | | | |
| 2025-07 | 84.000,00 | | 2025-11 | 88.000,00 | | 2026-03 | 86.000,00 | | | |
| 2025-08 | 86.000,00 | | 2025-12 | 92.000,00 | | | | | | |

Soma = 78.000+81.500+84.000+86.000+79.500+90.000+88.000+92.000+85.000+83.000+86.000+87.000

**RBT12 = R$ 1.020.000,00** ⇒ 4ª faixa (acima de 720.000,00 e até 1.800.000,00) nos dois anexos.
*(Composição do CSV não confirmada pelo cliente — premissa A1 em §9; o CSV não detalha se as
locações anteriores à NF-e 512 estão somadas em "receita_bruta".)*

## 2. Folha 12 meses e Fator R

**[FATOR-R]** Res. CGSN 140, art. 26: folha = montante **pago** nos 12 meses anteriores (salários,
pró-labore **incluídos encargos e FGTS**); §2º: valem os valores **pagos no período,
independentemente do mês de competência**.

Resumo `resumo_folha_12_meses.csv` (por competência; total = salários + pró-labore + inss/fgts):

23.400 ×2 + 23.800 ×3 + 24.100 ×3 + 24.300 ×2 + 20.900 + 24.600
= 46.800 + 71.400 + 72.300 + 48.600 + 20.900 + 24.600 = **R$ 284.600,00**.

**Correção pelo critério do pagamento — resolvida com o cliente.** O e-mail inicial falava em
pró-labore de abril "**pago atrasado, dia 6 de maio**"; na resposta aos questionamentos, o cliente
esclareceu (e enviou o comprovante de 30/04 — não consta no acervo de `documents/`): o pró-labore
de abril (2 × 1.600 = **3.200**) **foi pago em 30/04/2026**; o "em aberto" do resumo existia porque
**o PIX só foi lançado no contábil em maio**. Pago em 30/04 ⇒ **dentro da janela**
mai/2025–abr/2026 (Res. CGSN 140, art. 26, §2º: valem os valores **pagos**, independentemente do
mês da competência/lançamento) ⇒ o valor permanece na base:

Folha 12m (paga) = **R$ 284.600,00** (resumo integral, sem exclusões)

**Fator R** = folha 12m ÷ RBT12 = 284.600 ÷ 1.020.000 = 0,279019… ≈ **27,90%**

Robustez — todas as leituras chegam ao mesmo veredito (ponto de corte: 28% × 1.020.000 = **R$ 285.600,00**):
- Base final do cliente (pró-labore pago em 30/04): 284.600 → **27,90%** < 28%;
- Se a primeira versão do sócio ("pago em 06/05") prevalecesse: 281.400 → **27,59%** < 28%;
- Piso (abril inteiro pago em maio — salários 16.700 e encargos 4.700, ver extrato de 07/05): 260.000 → **25,49%** < 28%.
*(Remapear mês a mês pagamentos/encargos de 2025-05 a 2026-04 exigiria extratos anteriores — o
cliente informou não ter mais nada a acrescentar; permanece como incerto, porém sem efeito no
veredito nem no valor do DAS.)*

## 3. Anexo: **V** — faixa 4

**[FATOR-R]** §5º-J/§5º-M: serviços de TI (desenvolvimento, licenciamento, suporte, treinamento,
consultoria) tributados pelo **Anexo III somente se Fator R ≥ 28%; caso contrário, Anexo V**.
Fator R = 27,90% < 28% ⇒ **Anexo V**. ✔ O anexo pretendido pelo sócio ("Anexo V") se confirma —
mas com cálculo próprio, não pela memória de anos anteriores.

**[TABELAS]** Anexo V, faixa 4: alíquota nominal **20,50%**, parcela a deduzir **PD = 17.100,00**.

**[FATOR-R]** §1º-A — alíquota **efetiva** = (RBT12 × Aliq − PD) ÷ RBT12:

Efetiva V = (1.020.000 × 20,50% − 17.100) ÷ 1.020.000 = (209.100 − 17.100) ÷ 1.020.000
= 192.000 ÷ 1.020.000 = 0,188235… = **18,8235%**

⚠ O sócio pediu "repetir o cálculo da tabela com a alíquota da faixa" (20,50%). Aplicar a alíquota
nominal direto sobre a receita violaria o §1º-A: seria 78.000 × 20,50% = R$ 15.990,00, ou seja
R$ 1.307,65 a mais que o devido. Corrigido para a efetiva.

## 4. Classificação das notas de maio/2026

| Documento | Descrição | Classificação | Tratamento |
|---|---|---|---:|
| NFS-e 1181 | Desenvolvimento — sprint 11 | Serviço (TI) | Anexo V |
| NFS-e 1182 | Sustentação mensal — Orla | Serviço (TI) | Anexo V |
| NFS-e 1183 | Consultoria de arquitetura | Serviço (TI) | Anexo V |
| NFS-e 1184 | Desenvolvimento — módulo fiscal | Serviço (TI) | Anexo V |
| NFS-e 1185 | Suporte técnico | Serviço (TI) | Anexo V |
| NFS-e 1186 | Treinamento equipe | Serviço (TI) | Anexo V |
| NFS-e 1187 | Desenvolvimento — integração | Serviço (TI) | Anexo V |
| NFS-e 1188 | Estorno parcial da 1184 (glosa) | **Cancelamento/estorno** | **reduz a receita de maio** |
| NF-e 000.512 | Locação 20 notebooks | **Locação de bens móveis** | **Anexo III, deduzido ISS** — não "vai junto" com os serviços |

Receitas brutas: serviços 18.000+12.500+9.800+22.000+6.700+4.500+8.500 = **82.000,00**; locação **6.000,00**.

**Estorno (desenvolvimento — módulo fiscal, NFS-e 1188, R$ 4.000,00).** **[FATOR-R]** "o
cancelamento/estorno de serviço reduz a receita do mês em que ocorrer". Ocorreu em maio/2026
(nota 1188 substitui/cancela parcialmente a 1184; extrato: PIX ENVIADO ESTORNO GLOSA −4.000,00 em
29/05): Receita líquida de serviços de maio = 82.000 − 4.000 = **R$ 78.000,00**.
Conferência com o extrato bancário: 12.500+18.000+9.800+22.000+6.700+4.500+8.500 = 82.000 recebido;
− 4.000 de estorno ⇒ 78.000. ✔ O estorno **não** altera o RBT12: refere-se à nota 1184
(competência maio/2026), que não integra a janela mai/2025–abr/2026. (Também está trancado pelo
extrato: a TED de 22.000 em 15/05 caiu bruta; a glosa saiu em 29/05.)

**Locação (NF-e 000.512 — locação de 20 notebooks à Orla, R$ 6.000,00).** **[LOCACAO]** locação de
bens móveis **não é serviço** para ISS (Súmula Vinculante 31) e é tributada **no Anexo III,
deduzida a parcela do ISS** — portanto **não se soma aos serviços no Anexo V**, como pedia o
sócio. Receita segregada em livro próprio. O cliente confirmou que emitiu NF-e "porque locação
não é NFS-e" — coerente com **[LOCACAO]**/art. 18, §5º-A ✔. Só a NF-e de maio consta no acervo;
segundo o cliente, a locação à Orla ocorre "por uns meses" (premissas A1/A2 em §9). O sócio alega
"vai junto com os serviços" — **rejeitado pela biblioteca**; apurado separadamente.

## 5. DAS dos serviços (Anexo V, faixa 4)

DAS serviços = 78.000,00 × 18,8235…% = 78.000 × 192.000/1.020.000 = **R$ 14.682,35**
(exato: 14.682,3529…)

## 6. DAS da locação (Anexo III, faixa 4, deduzido ISS)

**[TABELAS]** Anexo III, faixa 4: alíquota nominal 16,00%, PD 35.640,00.
**[FATOR-R]** §1º-A: Efetiva III = (1.020.000 × 16,00% − 35.640) ÷ 1.020.000
= (163.200 − 35.640) ÷ 1.020.000 = 127.560 ÷ 1.020.000 = 0,125058… = **12,5059%**

**[TABELAS]** repartição do Anexo III, 4ª faixa: **ISS = 32,50%** ⇒ dedução do ISS sobre a base de
locação (a parcela do ISS não é devida na locação de bens móveis — **[LOCACAO]/SV 31**):
DAS locação = 6.000 × 12,5059% × (1 − 32,50%) = 750,3529… × 0,675 = **R$ 506,49** (exato: 506,4882…)

## 7. Total do DAS de maio/2026

| Rubrica | Base (R$) | Anexo/faixa | Alíq. efetiva | DAS (R$) |
|---|---:|---|---:|---:|
| Serviços | 78.000,00 | V / 4 | 18,8235% | 14.682,35 |
| Locação de bens móveis | 6.000,00 | III / 4 (−ISS 32,50%) | 12,5059% × 0,675 | 506,49 |
| **Total** | 84.000,00 | — | — | **15.188,84** |

Total exato = 14.682,3529… + 506,4882… = 15.188,8412… ⇒ **R$ 15.188,84** (centavos por arredondamento bancário de cada rubrica).

## 8. Repartição do DAS — **item aberto**

A biblioteca traz a **repartição do Anexo III, 4ª faixa** (usada no §6 apenas para deduzir o ISS da
locação). **A repartição percentual do Anexo V (CPP, IRPJ, CSLL, PIS/Pasep, COFINS) não consta em
nenhum arquivo da biblioteca** e não posso citá-la de outra fonte: o campo `reparticao` de
`apuracao.json` ficou em 0/zerado **sem validação**. Isso **não altera o valor do DAS** (o total
independe da repartição interna; não forcei conciliação). Se a firma enviar os percentuais
oficiais do Anexo V (ex.: folha do PGDAS-D), repartem-se R$ 14.682,35 de serviços conforme tabela
em vigor.

## 9. Premissas e incertos registrados

- **A1 (premissa, incerto).** `faturamento_12_meses.csv` ("receita_bruta") inclui **todas** as
  receitas do período, inclusive eventuais locações anteriores. O cliente esclareceu que a
  locação dos notebooks **à Orla vem ocorrendo "por uns meses"**, mas só apresentou a NF-e de
  maio (000.512) e não confirmou a composição do CSV. **Continua um incerto** — sensibilidade
  quantificada no item 1 de "Itens abertos" de `STATUS.md`. *(A pergunta foi respondida apenas em
  parte; o cliente disse não ter mais nada a acrescentar.)*
- **A2.** Em mai/2026 é documentada apenas uma locação (NF-e 000.512, R$ 6.000,00); a locação "por
  uns meses" **anterior** não tem notas no acervo. A escolha do documento (NF-e, não NFS-e)
  coincide com o que o cliente ouviu e com **[LOCACAO]**/**SV 31** ✔.
- **A3 (resolvida em parte).** O pró-labore de abril foi pago em 30/04/2026 (dentro da janela),
  comprovante informado pelo cliente mas **não anexado ao acervo de `documents/`**. Para o resto
  (2025-05 a 2026-03) não recebemos extratos anteriores: remapear mês a mês os pagamentos
  (ex.: extrato mostra "DARF/GPS/FGTS ABR" −4.700 só em 07/05/2026) permanece impossível; o piso
  de 25,49% (abril inteiro recolhido em maio) não muda o veredito (§2).
- **A4.** Extrato `.pdf` estava ilegível (formato); usei o `.csv` espelho; os valores cruzaram com
  as notas.

## 10. Conferência com o extrato de maio/2026

- Recebimentos dos serviços 82.000 (TED/PIX 02–22/05), locação 6.000 (TED 26/05), estorno −4.000 (29/05) → líquido de caixa 84.000. ✔ Com nota (§4).
- DAS ABR/2026 pago em 20/05: −10.480,22 — desembolso anterior ao período apurado; **fora** do DAS de maio.
- Folha de maio (salários 16.600, pró-labores 2 × 1.600 em 16/05) e encargos "ABR" 4.700 (07/05): competências pagas **em maio/2026** ⇒ não entram no Fator R de maio/2026 (entram no de junho); independem do DAS de maio.
- Sem débito em 06/05 no extrato e o e-mail dizia "pago dia 6 de maio": **resolvido pelo cliente** — o pagamento do pró-labore de abril ocorreu em **30/04/2026** (comprovante); o que aconteceu em maio foi apenas o **lançamento** do PIX no contábil. Para o Fator R de maio/2026 o valor permanece na base (24.600 de abril são de folha paga dentro da janela).
