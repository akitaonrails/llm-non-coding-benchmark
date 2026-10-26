# PERGUNTAS AO CLIENTE — apuração DAS maio/2026

Responda cada item abaixo (Q1–Q8) na próxima rodada. Os itens **Q1–Q3 podem mudar o resultado**:
com a folha como enviada, o Fator R ficou a **R$ 1.000** do limiar de 28%. Antes de pagar o DAS,
respondam principalmente Q1–Q3.

Contexto numérico comum: RBT12 = 1.020.000; folha do resumo = 284.600; Fator R = 27,9020%;
limiar de 28% em reais = 0,28 × 1.020.000 = **285.600**.

---

## Q1 — Datas de PAGAMENTO da folha na janela mai/2025–abr/2026

O `resumo_folha_12_meses.csv` vem **por competência**. A biblioteca (Res. CGSN 140/2018, art. 26, §2º,
em `library/lc123_art18_fator_r.md`) conta no Fator R o que foi **pago** dentro dos 12 meses, não o que
foi empenhado no mês.

**Pergunta:** para cada competência da janela, em que data efetiva foram pagos (a) salários,
(b) pró-labore, (c) INSS patronal + FGTS? Houve algum pagamento de competência mai/2026 **dentro**
da janela (p. ex. adiantamento em abril/2026) ou algum pagamento de competência antiga atrasado
para depois de abr/2026?

**Impacto:** se a folha **paga** na janela for ≥ 285.600 (faltam 1.000), o anexo passa de V para III e
o DAS cai de 15.188,84 para **10.261,08** (−4.927,76). Se for < 284.600, continua Anexo V e o DAS não muda.

## Q2 — Pró-labore de mar/2026 (linha zerada) e de abr/2026

No resumo, a competência 2026-03 tem pró-labore **0,00** com a observação "pró-labore de abril: em
aberto na data do resumo". O e-mail do sócio diz que o pró-labore de abril foi pago em **06/05/2026**
— data que está **fora** da janela mai/2025–abr/2026; o extrato de maio, porém, **não** mostra
pagamento em 06/05: só dois pagamentos de 1.600,00 em 16/05/2026 rotulados "PRO-LABORE MAI".

**Perguntas:** (a) o pró-labore de **março/2026** foi pago? Em que data e valor? (b) o pró-labore de
**abril/2026** foi pago em que data exatamente (06/05 ou 16/05)? (c) os dois pagamentos de 1.600,00 de
16/05 são o pró-labore de **abril** ou de **maio**, dos dois sócios?

**Impacto:** se algum desses pagamentos caiu **dentro** da janela (até 30/04/2026), a folha sobe e pode
cruzar o limiar de 285.600 (vide Q1). Se todos caíram em maio/2026, entram na janela de junho/2026 em diante.

## Q3 — Comprovantes para conferir a base de pagamento

**Pedido:** enviem a folha de pagamentos da janela e os comprovantes de INSS patronal (GPS/DARF) e
FGTS (guias/recolhimento) — ou o extrato bancário dos 12 meses, se existir. O extrato de mai/2026
(`extrato_maio_2026.csv`) só cobre um mês e mostra encargos constantes de 4.700/mês; isso **não**
substitui a confirmação dos pagamentos de mai/2025 a abr/2026.

**Impacto:** é o que permite substituir a premissa "competência = pagamento" usada em `apuracao.json`.

## Q4 — Tabela de repartição do Anexo V, 4ª faixa

`library/anexos_iii_v_tabelas.md` traz a repartição **apenas** da 4ª faixa do **Anexo III**
(IRPJ 4,00 · CSLL 3,50 · COFINS 14,05 · PIS 3,05 · CPP 42,75 · ISS 32,50) e **não** traz a do
**Anexo V** — que é o anexo dos serviços em maio/2026. Por isso os campos `reparticao` de
IRPJ/CSLL/COFINS/PIS/CPP estão `null` em `apuracao.json` (não apurado, não zero).

**Pedidos:** (a) a tabela de repartição do Anexo V, 4ª faixa, para eu preencher o campo `reparticao`;
(b) confirmando, a linha do Anexo III, 4ª faixa está mesmo incompleta? Os percentuais somam
**99,85%**, e aplicados à base da locação fecham em 749,23 contra 750,35 (diferença de 1,13), e o
subtotal sem ISS fica 505,36 contra 506,49 apurados. Não corrigi para fechar.

## Q5 — Dois pontos que não fecham com a biblioteca

**(a) Descrição fiscal das NFS-e 1183 e 1186.** "Consultoria de arquitetura" (9.800,00) e
"Treinamento equipe" (4.500,00) foram tratados como serviços de TI do art. 18, §5º-J, cuja lista na
biblioteca é aberta ("desenvolvimento, licenciamento, suporte etc."). **Pergunta:** qual o CNAE e a
descrição fiscal dessas notas? Em maio/2026 isso **não altera o valor** (com Fator R < 28% tudo sai
pelo Anexo V de qualquer forma), mas passa a importar se o Fator R virar ≥ 28% (Q1–Q3).

**(b) Mecânica da dedução do ISS na locação de bens móveis.** A biblioteca manda tributar "no Anexo III,
deduzida a parcela correspondente ao ISS", mas não diz como. Adotei a dedução proporcional à alíquota
efetiva: 12,505882% × (1 − 0,325) = **8,4415%** → DAS 506,49. A leitura alternativa (deduzir 32,50% da
alíquota nominal: 12,505882% − 5,20%) daria **7,3059%** → 438,35. **Pergunta:** qual mecânica o PGDAS-D
adota / qual valor a empresa usaria? **Impacto: R$ 68,14** no DAS de maio.

## Q6 — Natureza do `faturamento_12_meses.csv`

Usei o arquivo como a receita bruta mensal dos 12 meses anteriores, assumindo que (a) estornos e
cancelamentos de cada mês **já estão líquidos** nos valores e (b) receitas de locação dos meses
anteriores **já estão incluídas**. **Pergunta:** essas duas premissas estão corretas? Se a locação
histórica não estiver no arquivo, o RBT12 (e a faixa/alíquota) muda.

**Impacto potencial:** RBT12 é a base da faixa e da alíquota efetiva das duas atividades.

## Q7 — NF-e 512 com destaque de PIS/COFINS

A `nfe_000512_locacao.xml` destaca PIS 0,65% e COFINS 3,00% com CST 01 (regra geral) e o próprio XML traz
a anotação "documento fictício... sem validade fiscal". No Simples essas contribuições viriam dentro do
DAS; a biblioteca não trata de NF-e/CST, então **não alterei a apuração** — apenas registro.
**Pergunta:** essa NF-e foi realmente escriturada assim? Há outra via/CF-e de locação emitida?

## Q8 — Base do DAS de abril/2026 (informativo, fora desta apuração)

O extrato mostra DAS ABR/2026 = 10.480,22 pago em 20/05/2026. Com receita de abril de 86.000,00, isso
implica alíquota de ~12,19%, compatível com **Anexo III** (10.474,86 pelo cálculo para RBT12 933.000),
e **não** com Anexo V (16.053,79). Isso contradiz a lembrança do sócio de que "pagávamos pelo Anexo V".
**Pergunta:** podemos conferir o PGDAS-D/mey de abril/2026? Não refiz abril (faltam documentos); é só
para validar a premissa de histórico.

---

**Não perguntei/assumi e está declarado na memória:** janela do RBT12 = mai/2025–abr/2026; estorno da
NFS-e 1188 reduzindo maio/2026; vencimento do DAS (fora da biblioteca).
