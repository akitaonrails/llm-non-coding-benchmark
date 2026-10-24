# Memória de cálculo — DAS maio/2026 — Lumen Soluções Digitais ME

**Versão 2** — incorporando o esclarecimento do cliente (resposta a `QUESTIONS.md`): o pró-labore de
abril (R$ 3.200,00) foi **pago em 30/04/2026** e a glosa da NFS-e 1184 foi **cancelamento de receita**
(NFS-e 1188 + devolução via PIX). Isso **muda o resultado** em relação à versão 1: o Fator R passa de
27,90% para **28,22%** e os serviços migram do Anexo V para o **Anexo III**.

Escopo: apuração do DAS de **maio/2026** a partir das notas, do extrato, do resumo de folha e do
faturamento dos 12 meses anteriores (`documents/`), usando **exclusivamente** a biblioteca fechada
`library/` (índice: `library/INDEX.md`). Todas as citações abaixo apontam para arquivos desse índice.
Nenhuma outra fonte normativa foi usada; o que eu acredito ser a lei mas não consta da biblioteca está
explicitamente marcado como **não verificado**.

---

## 1. Base normativa utilizada (só `library/`)

| Tema | Regra usada | Fonte (citação do INDEX) |
|---|---|---|
| RBT12 para achar a faixa | receita bruta acumulada nos 12 meses anteriores ao período de apuração | `library/lc123_art18_fator_r.md` — LC 123/2006, art. 18, §1º |
| Alíquota efetiva | (RBT12 × Aliq − PD) ÷ RBT12 | `library/lc123_art18_fator_r.md` — art. 18, §1º-A |
| Anexo III × Anexo V para serviços de TI | Fator R = folha (salários + pró-labore + encargo patronal + FGTS) ÷ receita bruta, **ambos dos 12 meses anteriores**; ≥ 28% → Anexo III; < 28% → Anexo V | `library/lc123_art18_fator_r.md` — art. 18, §§5º-J e 5º-M |
| Regime da folha no Fator R | valores **pagos** nos 12 meses anteriores, independentemente do mês de competência | `library/lc123_art18_fator_r.md` — Res. CGSN 140/2018, art. 26, §§1º–2º |
| Segregação de receitas | segregar por atividade e aplicar a cada uma o anexo/alíquota próprios | `library/lc123_art18_fator_r.md` — art. 18, §4º |
| Devoluções/cancelamentos | cancelamento/estorno de serviço **reduz a receita do mês em que ocorrer** | `library/lc123_art18_fator_r.md` — item “Devoluções/cancelamentos” |
| Locação de bens móveis | tributada pelo **Anexo III, deduzida a parcela de ISS** (locação de bens móveis não é serviço de ISS) | `library/locacao_bens_moveis_iss.md` — LC 123/2006, art. 18, §5º-A; Súmula Vinculante 31 (STF); Res. CGSN 140, art. 25, §1º, V |
| Tabelas (alíquotas/parcelas) e repartição do Anexo III, 4ª faixa | ver §4 e §6 | `library/anexos_iii_v_tabelas.md` — LC 123/2006, Anexos III e V (redação LC 155/2016) |

**Não consta da biblioteca** (portanto, não verificável nesta apuração): a tabela de repartição do
Anexo V (agora **desnecessária**, pois ambos os componentes ficaram no Anexo III); regras sobre
compensação/restituição; tratamento de receitas anteriores a mai/2025; qualquer regra sobre DASN ou
retificação de competência alheia.

---

## 2. Classificação nota a nota (maio/2026)

Fonte: `documents/notas_emitidas_maio.md`, `documents/nfe_000512_locacao.xml`, cruzados com
`documents/extrato_maio_2026.csv`.

| Documento | Descrição | Valor | Classificação | Tratamento |
|---|---|---:|---|---|
| NFS-e 1181 | Desenvolvimento de software — sprint 11 | 18.000,00 | serviço de TI (desenvolvimento) | receita de serviços → Anexo III (Fator R ≥ 28%; ver §5) |
| NFS-e 1182 | Sustentação mensal — Cliente Orla | 12.500,00 | serviço de TI (suporte/sustentação) | idem |
| NFS-e 1183 | Consultoria de arquitetura | 9.800,00 | serviço (TIC, em sentido amplo) | idem (ver §3 sobre a extensão de “TI” no §5º-J) |
| NFS-e 1184 | Desenvolvimento — módulo fiscal | 22.000,00 | serviço de TI | idem |
| NFS-e 1185 | Suporte técnico | 6.700,00 | serviço de TI (suporte) | idem |
| NFS-e 1186 | Treinamento equipe | 4.500,00 | serviço de TI/educação | idem (mesma observação da 1183) |
| NFS-e 1187 | Desenvolvimento — integração | 8.500,00 | serviço de TI | idem |
| NFS-e 1188 | **Estorno parcial da NFS-e 1184** — glosa de escopo **confirmada pelo cliente** | (4.000,00) | cancelamento/estorno parcial de serviço | **reduz a receita de serviços de maio/2026** (regra “Devoluções/cancelamentos”, `lc123_art18_fator_r.md`); devolução paga vista no extrato em 29/05/2026 (PIX ENVIADO ESTORNO GLOSA — CLIENTE 1184, −4.000,00). Informe do cliente (paráfrase): o cliente final contestou parte do escopo da 1184, a Lumen emitiu a 1188 estornando R$ 4.000 e devolveu o valor via PIX → **Questão Q3 encerrada.** |
| NF-e 000.512 | **Locação de 20 notebooks** — maio/2026 (natOp “Locação de bens móveis”, CFOP 5949, sem destaque de ISS) | 6.000,00 | **locação de bens móveis** (não é serviço para ISS) | **segregada** dos serviços (art. 18, §4º) e tributada pelo **Anexo III, sem a parcela de ISS** (`locacao_bens_moveis_iss.md`). NÃO vai “junto com os serviços” no Anexo V, como supunha o sócio no e-mail |

Conferência extrato × notas: recebimentos do extrato de maio = 12.500 + 18.000 + 9.800 + 22.000 +
6.700 + 4.500 + 8.500 + 6.000 = **88.000,00** = 82.000,00 (serviços brutos) + 6.000,00 (locação). ✓

Observação sobre o documento da locação: o próprio XML traz “Documento fictício gerado para benchmark;
sem validade fiscal” (`nfe_000512_locacao.xml`, infCpl). Tratei-o como documento interno de apoio; o
valor confere com o TED de 26/05/2026 do extrato. As linhas de PIS/COFINS do XML (CST 01, 0,65%/3,00%)
são incompatíveis com o padrão Simples Nacional, mas a biblioteca não contém regra sobre leiaute NF-e,
então nada affinei a partir delas.

## 3. O estorno e a locação — o que foi feito

- **Estorno (R$ 4.000,00) — RESOLVIDO pelo cliente:** glosa de escopo acordada, tratada como
  cancelamento parcial de receita (NFS-e 1188 + devolução via PIX em 29/05/2026). Reduz a receita bruta
  de **serviços de maio/2026** (mês em que ocorreu): 82.000,00 − 4.000,00 = **78.000,00**. O estorno não
  altera o RBT12 de maio/2026 (janela mai/2025–abr/2026).
- **Locação (R$ 6.000,00):** **segregada** dos serviços (art. 18, §4º) e tributada pelo **Anexo III com a
  parcela de ISS eliminada** (§5º-A + Súmula Vinculante 31 + Res. CGSN 140, art. 25, §1º, V —
  `locacao_bens_moveis_iss.md`). No Anexo III, 4ª faixa, a parcela de ISS da repartição é **32,50%**
  (`anexos_iii_v_tabelas.md`). Se fosse indevidamente incluída nos serviços do Anexo V (como sugeria o
  e-mail do sócio), pagaria 6.000,00 × alíquota efetiva do anexo errado; o tratamento correto paga
  **506,49**, qualquer que seja o anexo dos serviços (a locação é sempre Anexo III sem ISS).
- **Sobre “TI” no §5º-J:** a biblioteca lista “desenvolvimento, licenciamento, suporte **etc.**”
  (`lc123_art18_fator_r.md`). As notas de consultoria de arquitetura (1183) e treinamento (1186) não
  estão expressamente nessa lista; tratei-as como serviços de TI do mesmo negócio (é a premissa do
  próprio Fator R único). Se alguma delas fosse atividade **não-TI**, esta apuração não teria como
  enquadrá-la: a biblioteca não traz Anexo I/II/IV e teria que haver segregação adicional — item aberto
  (STATUS.md; o cliente informou não ter mais informação sobre isso).

## 4. RBT12 e faixa

Janela de 12 meses anteriores a maio/2026 = **mai/2025–abr/2026** (`documents/faturamento_12_meses.csv`):

78.000 + 81.500 + 84.000 + 86.000 + 79.500 + 90.000 + 88.000 + 92.000 + 85.000 + 83.000 + 86.000 + 87.000
= **R$ 1.020.000,00**

Faixa (ambas as tabelas, `anexos_iii_v_tabelas.md`): 720.000 < 1.020.000 ≤ 1.800.000 → **4ª faixa**.

Premissa destacada: o CSV é a receita bruta **total** de cada competência (não há segregação por
atividade nos 12 meses em poder do escritório). O cliente informou não ter a segregação — item aberto
(STATUS.md, item 3). O texto da biblioteca (§1º e §§5º-J/5º-M) fala em “receita bruta” sem segregação
para a faixa e para o Fator R; adotei a leitura literal (RBT12 total).

## 5. Fator R e escolha do anexo (serviços)

O e-mail do sócio (`documents/email_socio.txt`) diz: “Ano passado a gente pagava pelo Anexo V (TI), é
só repetir o cálculo da tabela com a alíquota da faixa” (o contrato resume o pedido como “repetir o
Anexo V com a alíquota da faixa”). A biblioteca não permite “repetir” por inércia: o anexo depende do
Fator R apurado **a cada período** (§§5º-J/§5º-M).

Regra (Res. CGSN 140, art. 26, §§1º–2º, `lc123_art18_fator_r.md`): folha = salários + pró-labore +
contribuições patronais + FGTS, pelo regime de **pagamento** nos 12 meses anteriores (janela de
pagamentos: **mai/2025–abr/2026**), independentemente da competência.

### 5.1 Reconstrução da folha PAGA (pós-esclarecimento do cliente)

Esclarecimento do cliente (resposta à Q1): o pró-labore de abril — **R$ 3.200,00** no total — foi
**“pago em 30 de abril”**; o resumo de folha o mostrava **“em aberto”** porque o PIX só foi lançado no
sistema em maio. O cliente anunciou: “**Te mando o comprovante de 30/04**”. (A divisão por dois sócios
é corroborada pelo extrato de maio/2026, que mostra o pró-labore mensal desdobrado em dois PIX de
R$ 1.600,00 — RENATO e JULIA; a redação exata da mensagem não é transcrita aqui literalmente, apenas as
expressões entre aspas.) Isso substitui a versão do e-mail do sócio (“paguei atrasado, dia 6 de maio”).

Leitura coerente de `documents/resumo_folha_12_meses.csv` com esse esclarecimento:

- A coluna `pro_labore` reflete **pagamentos lançados** em cada mês: 3.200 em 11 competências e R$ 0,00
  na linha 2026-03, cuja observação (“pró-labore de abril: em aberto na data do resumo”) é exatamente o
  pagamento de 30/04 que **não estava lançado** quando o resumo foi tirado.
- O valor de 3.200 lançado na linha 2026-04 corresponde ao pró-labore de **março**, pago atrasado dentro
  de abril (o “paguei atrasado” do e-mail — só a data “6 de maio” é que foi corrigida pelo cliente).
- Consequência: os **12 pró-labores** da janela (mai/2025–abr/2026) foram **pagos dentro da janela** =
  12 × 3.200 = **38.400,00**, dos quais 35.200,00 estão somados no resumo e 3.200,00 (o de 30/04) **não**.

| Componente | Valor | Base / evidência |
|---|---:|---|
| Salários | 193.000,00 | soma da coluna `salarios` do resumo; pagos **no próprio mês** da competência — extrato: “FOLHA MAIO — SALARIOS” pago em 07/05/2026 (16.600,00, competência mai/2026, fora da janela; a janela usa os salários de mai/2025–abr/2026 = 193.000,00) |
| Pró-labore (pago) | 38.400,00 | 12 × 3.200 (11 lançados no resumo + abril pago em 30/04, comprovante pendente) |
| CPP/FGTS patronal | 56.400,00 | pagos com **defasagem de 1 mês** (extrato: “DARF/GPS/FGTS ABR” em 07/05/2026); pagamentos na janela = competências abr/2025–mar/2026; o resumo traz 4.700,00 **constantes** nas 12 linhas documentadas, logo a troca de janela não altera a soma (12 × 4.700). **Premissa:** abr/2025 (mês não documentado) também = 4.700,00 |
| **Folha 12m (pagamento)** | **287.800,00** | 193.000 + 38.400 + 56.400 |

**Fator R = 287.800 ÷ 1.020.000 = 0,2821569 → 28,22% ≥ 28% → Anexo III para os serviços**
(§§5º-J/§5º-M, `lc123_art18_fator_r.md`). Margem sobre o limiar: folha mínima = 28% × 1.020.000 =
285.600,00; estamos **2.200,00 acima**.

### 5.2 Sensibilidade — o resultado depende de UM comprovante

| Cenário | Folha 12m | Fator R | Anexo | DAS total |
|---|---:|---:|---|---:|
| **(Adotado)** pró-labore de abril pago em **30/04/2026** (cliente; comprovante anunciado, ainda ausente de `documents/`) | 287.800 | **28,22%** | **III** | **10.261,08** |
| Pró-labore de abril pago em **06/05/2026** (versão do e-mail do sócio) — fora da janela | 284.600 | 27,90% | V | 15.188,84 |

A diferença entre os dois enquadramentos é de **R$ 4.927,76**. O pagamento de 30/04 (R$ 3.200,00) é,
sozinho, o que leva a folha de 284.600 para 287.800 e cruza o limiar de 28%. **Aguardando o comprovante
de 30/04/2026 que o cliente anunciou** (“Te mando o comprovante” — não veio ainda; verifiquei
`documents/`). Se o comprovante confirmar, o Anexo III está documentado; se mostrar data ≥ 01/05/2026,
vale o Anexo V e o DAS de 15.188,84.

Nota de consistência (a favor da leitura adotada): o resumo de folha e o total de 284.600 **excluem** o
pagamento de 30/04 (é o “em aberto” da observação), de modo que 284.600 é a soma de competência/lançamento,
e NÃO a folha paga; somar o pagamento de 30/04 → 287.800. Ver também §7.4: o DAS de abril pago
(10.480,22) é compatível com Anexo III (receita de abril ≈ 84 mil) e **incompatível** com Anexo V
(exigiria receita ≈ 56 mil) — coerente com o Fator R já ≥ 28% nos meses anteriores.

Robustez do Anexo III quanto ao timing dos **demais** itens da folha (testado): (a) o encargo
patronal (CPP/FGTS) é **insensível** ao deslocamento da janela — 4.700,00 constantes nas 12 linhas
documentadas do resumo dão 12 × 4.700 = 56.400 em qualquer recorte de 12 meses; (b) se os **salários**
seguissem a defasagem de 1 mês do encargo (ao contrário da evidência bancária “FOLHA MAIO” paga em
07/05/2026), a folha paga seria 271.100 + salário da competência abr/2025 (mês fora do resumo), e o
Anexo III se sustentaria enquanto essa competência fosse ≥ 14.500,00 — improvável, dado que as
competências documentadas vão de 15.500,00 a 16.700,00. Em resumo: **nenhum item da folha, exceto a
data de pagamento do pró-labore de abril, é capaz de virar o enquadramento** — o único cenário que
leva ao Anexo V é a linha 2 da tabela acima.

## 6. Cálculo do DAS de maio/2026

Cálculos executados em Python (Decimal); arredondamento a 2 casas apenas no valor final de cada parcela.

### 6.1 Serviços (Anexo III, 4ª faixa — `anexos_iii_v_tabelas.md`)
Nominal 16,00%; parcela a deduzir 35.640,00.

Alíquota efetiva (§1º-A): (1.020.000 × 0,16 − 35.640) ÷ 1.020.000
= (163.200 − 35.640) ÷ 1.020.000 = 127.560 ÷ 1.020.000 = **0,1250588235** (12,5059%)

DAS serviços = 78.000,00 × 0,1250588235 = 9.754,5882 → **R$ 9.754,59**

### 6.2 Locação de bens móveis (Anexo III, 4ª faixa, sem ISS — `locacao_bens_moveis_iss.md`)
Mesma alíquota efetiva de §6.1: 0,1250588235.

DAS cheio da locação = 6.000,00 × 0,1250588235 = 750,3529
Parcela de ISS a eliminar = 32,50% (`anexos_iii_v_tabelas.md`, repartição Anexo III 4ª faixa)
= 750,3529 × 0,325 = 243,86 → eliminada
DAS locação = 750,3529 × (1 − 0,325) = 506,4882 → **R$ 506,49**

### 6.3 Total
DAS maio/2026 = 9.754,59 + 506,49 = **R$ 10.261,08**
(alíquota efetiva combinada sobre 84.000,00 = 12,2156%)

### 6.4 Repartição por tributo — agora verificável

Com **ambos** os componentes no **Anexo III, 4ª faixa**, a repartição usa a única tabela da biblioteca
(`anexos_iii_v_tabelas.md`): IRPJ 4,00% · CSLL 3,50% · COFINS 14,05% · PIS 3,05% · CPP 42,75% · ISS
32,50%. A linha **ISS é zerada na parcela da locação** (§5º-A + SV 31). A tabela do Anexo V, que faltava
na biblioteca, tornou-se desnecessária.

| Tributo | Serviços (base 9.754,5882) | Locação (base cheia 750,3529) | Consolidado |
|---|---:|---:|---:|
| IRPJ | 390,18 | 30,01 | **420,20** |
| CSLL | 341,41 | 26,26 | **367,67** |
| COFINS | 1.370,52 | 105,42 | **1.475,94** |
| PIS | 297,51 | 22,89 | **320,40** |
| CPP | 4.170,09 | 320,78 | **4.490,86** |
| ISS | 3.170,24 | 0,00 (eliminada: 243,86) | **3.170,24** |

(Consolidado = percentagens aplicadas à base combinada, arredondado uma única vez; a soma das parcelas
arredondadas pode diferir em 0,01.)

**Divergência assumida (não balanceada):** as percentagens da tabela somam **99,85%**, não 100%. A soma
da repartição (**10.245,31**) fica **R$ 15,77 abaixo** do DAS total (10.261,08). Não normalizei nem
“forçei” o balanço: ou a tabela da biblioteca está incompleta, ou há um tributo/percentual faltante —
item aberto da biblioteca fechada, deixado à vista.

## 7. Cruzamentos e pontos que não fecham (deixados abertos)

1. **Extrato × notas**: recebimentos de maio batem exatamente com as notas (88.000,00). ✓
2. **Estorno**: confirmado pelo cliente (glosa → NFS-e 1188 → devolução PIX 29/05 vista no extrato). ✓
3. **Pró-labore de abril (R$ 3.200) pago em 30/04**: relato do cliente; **comprovante anunciado e ainda
   ausente de `documents/`**; o e-mail do sócio dizia “6 de maio”. É o item **material** da apuração
   (§5.2). O extrato de maio também não mostra o PIX de 06/05 alegado no e-mail. ✗
4. **DAS de abril (R$ 10.480,22 pago em 20/05/2026)**: não reconciliável de forma fechada (receita de
   abril/2026 = 87.000 no agregado do CSV, mas RBT12 de abril e eventuais segregacoes de abril não
   documentadas). Observação nova: sob **Anexo III** (RBT12 de abril ≈ 1.011.000, se abr/2025 ≈ 78.000),
   a guia de 10.480,22 implicaria receita de abril ≈ **84.000** — compatível com 87.000 (ou com locação
   segregada em abril); sob **Anexo V** implicaria receita ≈ **55.700** — incompatível com o CSV. Ou
   seja: a prática recente do contribuinte aparenta ser **Anexo III**, contradizendo a fala do sócio de
   que “ano passado a gente pagava pelo Anexo V”. Não usei o valor de abril em nenhum cálculo; não há
   regra de retificação na biblioteca (marco como recomendação **não verificada**: conferir as guias de
   2026 com o contador).
5. **Folha de maio paga em 07/05** e **DARF/GPS/FGTS de ABR pagos em 07/05** no extrato: fundamentam o
   regime de pagamento usado em §5.1 (salários no próprio mês; patronal com 1 mês de defasagem). ✓
6. **Constante do encargo patronal**: adotei 4.700,00/mês também para abr/2025 (fora do resumo) para
   fechar 12 × 4.700 na janela de pagamento. Se abr/2025 foi diferente, a folha paga muda na mesma
   proporção e pode aproximar/afastar o Fator R do limiar de 28% (§5.2).

## 8. Diretriz do sócio — resposta documentada

“Repetir o Anexo V com a alíquota da faixa” (resumo do pedido do sócio no contrato; no e-mail: “é só
repetir o cálculo da tabela com a alíquota da faixa”): **não é o que o direito documentado entrega em maio/2026.**
Para os **serviços**, o Fator R apurado em regime de pagamento (28,22% ≥ 28%) leva ao **Anexo III**
(efetiva 12,5059%), não ao Anexo V (18,8235%). Para a **locação**, o pedido está errado: ela vai
segregada ao **Anexo III sem ISS** (506,49), nunca “junto com os serviços” do Anexo V. Se o comprovante
de 30/04 não confirmar o pagamento dentro da janela, aí sim o Anexo V se aplica (DAS 15.188,84) —
ver §5.2.
