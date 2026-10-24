# REVISAO.md — o que mudou na revisão (rodada 3)

**Apuração revisada:** DAS maio/2026 da Lumen Soluções Digitais LTDA ME.
**Resultado apurado: NÃO MUDOU — R$ 15.188,84** (serviços 14.682,35 + locação 506,49, Anexo V / Anexo III−ISS).

A revisão consistiu em reler cada afirmação da entrega **contra o arquivo-fonte** (`documents/`, `library/`) e
repetir toda a aritmética em `Decimal` (validador independente, **87 verificações — inclusive a soma das
fontes `faturamento_12_meses.csv`, `resumo_folha_12_meses.csv` e `extrato_maio_2026.csv` — todas PASS**).
Foram **16 correções**, agrupadas abaixo. Nada foi acrescentado sem fonte: o que a biblioteca não cobre
continua marcado **NÃO VERIFICADO NA BIBLIOTECA**, e o que não fecha continua registrado como **divergência**.

> Convenção usada ao citar a versão anterior: quando o texto antigo está transcrito no próprio arquivo corrigido
> (caso do §3.6 e do JSON), ele é citado literalmente; nos demais casos descreve-se o defeito e dá-se o valor
> **corrigido**, porque as versões anteriores não foram preservadas (não há git neste workspace).

---

## A. Conciliação do extrato — alegações que não constam dos documentos (4)

| # | Correção | Motivo (fonte) |
|---|---|---|
| 1 | Retirada a alegação de que o PDF traria um débito **"OUTBACK STEAK R$ 120,00"**. | Nenhuma ocorrência em `documents/extrato_maio_2026.csv` (busca por `OUTBACK` nas 15 linhas: **zero**) nem no texto integral do PDF (`pdftotext -layout`). Afirmativa sem fonte foi **eliminada**, não "corrigida". |
| 2 | Retirada a alegação de que o **saldo final do PDF seria R$ 100,00 menor** que o do CSV. | Os dois arquivos trazem o mesmo cabeçalho: abertura **41.280,55**, créditos **88.000,00**, débitos **43.180,22**, final **86.100,33**. Diferença alguma. |
| 3 | Retirada a alegação de **inconsistência da coluna saldo nas linhas de 28–29/05**. | Conferência linha a linha das 15 linhas: **0 divergências**. Na ponta do extrato: 81.600,33 + 8.500,00 = **90.100,33** (28/05) e 90.100,33 − 4.000,00 = **86.100,33** (29/05) — batem com o cabeçalho. |
| 4 | Passou a registrar (a) que o rodapé do PDF declara **instituição bancária fictícia, criada para benchmark**, e (b) as **diferenças apenas de forma** entre PDF e CSV (emissor/período/conta no PDF; descrição do estorno quebrada em duas linhas; "ALUGUEL ESCRITORIO" no CSV). | `documents/extrato_maio_2026.pdf`. O conteúdo dos dois arquivos é **idêntico**; a qualificação do rodapé é transparência sobre a natureza do documento, e não afeta a conciliação, que usa os valores. |

**Estado corrigido:** extrato **100% conciliado** — créditos 88.000,00 (= soma das notas emitidas), débitos
43.180,22 (= 16.600,00 + 4.700,00 + 4.200,00 + 1.600,00 + 1.600,00 + 10.480,22 + 4.000,00), saldo
41.280,55 + 88.000,00 − 43.180,22 = **86.100,33**. Ver `memoria.md` §8.1 e `apuracao.json` `conciliacao_extrato`.

---

## B. Aritmética — números recomputados e convenção explicitada (5)

| # | Correção | Conta que sustenta |
|---|---|---|
| 5 | Cenário **treinamento (NFS-e 1186) no Anexo III** recomputado: DAS **14.904,54**, efeito **−284,30** (valor anterior divergia da conta exata em centavos). | 73.500,00 × 18,8235% = 13.835,29 **mais** 4.500,00 × 12,5059% = 562,76 **mais** locação 506,49 = 14.904,54; 14.904,54 − 15.188,84 = −284,30. |
| 6 | Confrontos de **abril/2026** recomputados: Anexo V **16.376,47** · Anexo III **10.880,12** · segregado **10.636,25**. | 87.000,00 × 18,8235% · 87.000,00 × 12,5059% · (81.000,00 × 12,5059% = 10.129,78) + (6.000,00 × 8,4415% = 506,49). |
| 7 | §6.3 (**método do sócio**) refeita com as duas parcelas da diferença explicitadas: **+1.307,65** (serviços) e **+723,51** (locação) = **+2.031,16**. | 78.000,00 × 20,50% = 15.990,00 → 15.990,00 − 14.682,35 = 1.307,65; 6.000,00 × 20,50% = 1.230,00 → 1.230,00 − 506,49 = 723,51; soma 2.031,16 = 17.220,00 − 15.188,84. |
| 8 | **Carga efetiva do mês** explicitada: **0,180820** (18,08%). | 15.188,84 ÷ 84.000,00 = 0,1808195…; campo `das.carga_efetiva_mes` no JSON. |
| 9 | **Bloco indicativo de junho/2026 refeito** — a fórmula anterior **não fechava**: "284.600,00 − 23.400,00 + 16.600,00 + 4.700,00 = 285.700,00" (esses quatro termos dão **282.500,00**, faltava o pró-labore de mai/26). A conclusão anterior ("junho/2026 tenderia ao **Anexo III**") **não se sustenta** na leitura-base. | Janela 06/2025–05/2026 (por competência, como o resumo): 284.600,00 − 23.400,00 (2025-05) **+ 24.500,00** (competência 2026-05 estimada: salários 16.600,00 + pró-labore 3.200,00 + INSS/FGTS recorrente 4.700,00) = **285.700,00** → fator R 285.700,00 ÷ 1.026.000,00 = **27,85% < 28%** → **ainda Anexo V** (limiar 287.280,00, margem 1.580,00). Só na variante com a lacuna de **U1** (+3.200,00 → 288.900,00) o fator R vai a **28,16%** e junho/2026 iria ao **Anexo III** (limiar excedido em 1.620,00). Armadilha evitada: o DARF/GPS/FGTS de 4.700,00 pago em 07/05/2026 é da competência **abr/2026**, que já está em 284.600,00. Ver `memoria.md` §3.6 e `apuracao.json` `indicativo_junho_2026`. |

---

## C. Autoridade — separar texto de lei × inferência × indicativo (4)

| # | Correção | Motivo |
|---|---|---|
| 10 | O redutor de ISS da locação (**67,50%**) deixou de ser apresentado como se a lei fixasse o percentual: passou a **inferência documentada**, rotulada **P7**, com o texto da biblioteca citado e a sensibilidade quantificada. | `library/locacao_bens_moveis_iss.md` manda tributar "na forma do **Anexo III, deduzida a parcela correspondente ao ISS**", **sem fixar percentual**; o 32,50% veio da **repartição da 4ª faixa do Anexo III** (`anexos_iii_v_tabelas.md`). Como a tabela soma **99,85%**, a variante ISS 32,65% (redutor 67,35%) dá locação **505,36** e DAS **15.187,71** (−1,13) — registrada em U6, sem forçar fechamento. |
| 11 | O cálculo de **abril/2026** deixou de aparecer como apuração/fato e passou a **cálculo INDICATIVO**. | Falta o RBT12 da janela **abr/2025–mar/2026**, que não está no pacote; as alíquotas efetivas usadas são as desta apuração. O único fato é o pagamento: **10.480,22** = **12,05%** de 87.000,00 (`extrato_maio_2026.csv`, 20/05/2026). |
| 12 | Registrado explicitamente que o **estorno da NFS-e 1188 não altera o fator R** desta apuração. | A janela de folha é **05/2025–04/2026**; maio/2026 **não** integra a janela de maio/2026. O estorno afeta as receitas do mês (82.000,00 → **78.000,00**) e o RBT12 das janelas **futuras** (junho/2026 ≈ 1.026.000,00). Campo novo `estorno_efeito_fator_r` no JSON. |
| 13 | Criada a premissa **P6** (faixa/alíquota efetiva apuradas pelo **RBT12 global** nos dois blocos) e o unknown **U9**. | `library/lc123_art18_fator_r.md` (art. 18, §4º × §1º-A) **não disciplina** se a faixa de cada bloco segregado vem do RBT12 global ou do RBT12 da atividade. Leitura alternativa, **não adotada** e ilustrativa: locação na 1ª faixa do Anexo III → 6.000,00 × 6,00% × 67,50% = **243,00**, DAS **14.925,35** (−263,49). Não adotada porque pressupõe dado inexistente (locação mês a mês) e contraria a literalidade do §1º-A. |

---

## D. Consistência interna e rastreabilidade (3)

| # | Correção | Motivo |
|---|---|---|
| 14 | **Convenção de arredondamento explicitada** (`convensao_arredondamento` no JSON, §6.2 da memória): arredondar **cada bloco ao centavo** e depois somar; o valor a recolher é apurado por anexo. Conferência exata sem arredondamento também mostrada (14.682,35294 / 506,48824 / 15.188,84118). | Sem a convenção declarada, os totais dos cenários divergiam em centavos conforme o caminho de cálculo (é o que explicava as diferenças de centavos corrigidas no item 5). |
| 15 | **Numeração unificada**: os arquivos de perguntas e a memória passaram a usar **U1–U9** e **P1–P7** (as referências soltas no formato "Q5/Q7/Q8/Q9" foram substituídas por U2/U4/U5/U7), e os cinco arquivos ficaram com as mesmas listas, sem duplicar perguntas já respondidas. | Rastreabilidade: cada número nos arquivos de perguntas aponta para o mesmo item na memória e no JSON (`premissas`, `unknowns`, `nao_verificado`, `cenarios`). |
| 16 | O **comprovante de pagamento do pró-labore em 30/04/2026** passou a ser rotulado como **alegação do cliente** (o documento **não** integra `documents/`), e os contadores de rodada do cabeçalho da memória e do `STATUS.md` foram alinhados a esta lista. | Evita apresentar como prova um item que não está no pacote; e mantém `memoria.md`, `STATUS.md`, `QUESTIONS.md`, `PERGUNTAS.md` e `apuracao.json` na mesma versão (rodada 3). |

---

## O que **não** mudou

- **DAS maio/2026 = 15.188,84** (serviços **14.682,35** no Anexo V + locação **506,49** no Anexo III com a parcela de ISS excluída).
- RBT12 **1.020.000,00** (4ª faixa), folha **284.600,00**, fator R **27,90%** (< 28%), limiar de folha **285.600,00**, margem **1.000,00**.
- Anexos aplicáveis, premissas P1–P5, e a recusa do método do sócio (20,50% nominal sobre tudo = 17.220,00).

## O que continua **em aberto** (não resolvido pela revisão)

- **U1 (único risco material):** folha **paga** na janela 05/2025–04/2026 não comprovada por documentos de pagamento; a linha **2026-03** do resumo tem pró-labore **0,00** sem explicação. Se a folha paga for **≥ 285.600,00**, os serviços vão ao **Anexo III** e o DAS cai para **10.261,08** (−4.927,76). A mesma incógnita define junho/2026 (item 9).
- **U2–U9**: composição do RBT12, classificação de "consultoria de arquitetura" e "treinamento" (listas de atividades **ausentes da biblioteca**), anexo efetivamente usado em períodos anteriores, repartição dos **serviços** (tabela do Anexo V **ausente**), tabela de repartição que soma 99,85%, destaque de PIS/COFINS na NF-e 512, CNAE/PGDAS-D e retenções da locação, e a base de faixa por bloco (P6/U9).

Detalhe de cada item em `QUESTIONS.md` / `PERGUNTAS.md`; estado de entrega em `STATUS.md`.
