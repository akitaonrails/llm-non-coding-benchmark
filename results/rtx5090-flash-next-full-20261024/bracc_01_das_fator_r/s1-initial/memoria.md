# Memória de cálculo — DAS maio/2026 — Lumen Soluções Digitais ME

Apuração do Simples Nacional (DAS) da competência **maio/2026**. Autoridade exclusiva: a biblioteca
fechada `library/` (índice em `library/INDEX.md`). Tudo que não está nela está rotulado como
**não verificado** — não foi citada nenhuma outra fonte.

---

## 1. RBT12 (receita bruta acumulada dos 12 meses anteriores)

Fonte: `documents/faturamento_12_meses.csv` (competências 2025‑05 a 2026‑04, janelas de
mai/2025–abr/2026 — é a janela exigida por LC 123/2006, art. 18, §1º, in `library/lc123_art18_fator_r.md`).

| Comp. | R$ | Comp. | R$ |
|---|---:|---|---:|
| 2025‑05 | 78.000 | 2025‑11 | 88.000 |
| 2025‑06 | 81.500 | 2025‑12 | 92.000 |
| 2025‑07 | 84.000 | 2026‑01 | 85.000 |
| 2025‑08 | 86.000 | 2026‑02 | 83.000 |
| 2025‑09 | 79.500 | 2026‑03 | 86.000 |
| 2025‑10 | 90.000 | 2026‑04 | 87.000 |

78.000+81.500+84.000+86.000+79.500+90.000+88.000+92.000+85.000+83.000+86.000+87.000 = **R$ 1.020.000,00**

*Suposição:* o `faturamento_12_meses.csv` é a receita bruta **total** (serviços + eventuais locações
dos meses anteriores). Os arquivos não trazem a segregação mensal histórica; nada nos dados sugere
valor diferente. (O arquivo PDF do extrato é igual ao CSV do extrato de maio — conferido.)

## 2. Fator R — as TI vão para o Anexo V ou o Anexo III?

Regra (`library/lc123_art18_fator_r.md`, LC 123/2006, art. 18, §§5º‑J/5º‑M): serviços de TI
(desenvolvimento, licenciamento, suporte etc.) são tributados pelo **Anexo III se** folha/receita
(ambas dos 12 meses anteriores) **≥ 28%**; caso contrário, **Anexo V**.
Res. CGSN 140, art. 26, §§1º‑2º: folha = importes **pagos** nos 12 meses anteriores (salários +
pró‑labore + contribuições patronais + FGTS), **independentemente do mês de competência**.

Folha por competência (`documents/resumo_folha_12_meses.csv`, coluna `total_folha`):

23.400+23.400+23.800+23.800+23.800+24.100+24.100+24.100+24.300+24.300+20.900+24.600 = **R$ 284.600,00**

Ajuste de **pagamento** (atualizado pela resposta do cliente — rodada 2): o **pró‑labore de
abril/2026 (R$ 3.200,00 = 2 × R$ 1.600,00, um por sócio) foi pago em 30/04/2026** — data **dentro**
da janela mai/2025–abr/2026. O resumo contábil o trazia "em aberto" porque o PIX foi lançado no
sistema só em maio. Pelo §2º (conta o que foi **pago** na janela, qualquer que seja a competência),
esse valor **entra** no numerador:

- **Fator R (base pagamentos): 284.600 / 1.020.000 = 0,279020 = 27,90% < 28% → ANEXO V.**

Contexto e ressalvas desta linha:

- O e‑mail original (`documents/email_socio.txt`) dizia o pró‑labore de abril pago **atrasado, em
  06/05/2026**; a resposta do cliente (rodada 2) diz **30/04/2026**. As duas versões são
  contraditórias, mas **não alteram o enquadramento**: com 06/05 o numerador seria 281.400 →
  27,59%; com 30/04 é 284.600 → 27,90%. Ambas < 28% → **Anexo V nos dois casos**, DAS inalterado.
  Adotamos a versão mais recente (30/04).
- O comprovante de 30/04 foi prometido pelo cliente mas **não está no acervo** `documents/`. O
  extrato de maio começa em 01/05, logo nem confirmaria nem refute um pagamento de 30/04.
  Confiamos na declaração do cliente — item aberto.
- Reconciliação estrita da base pagamentos: as contribuições patronais/FGTS da competência
  2026‑04 (R$ 4.700,00) foram pagas em 07/05/2026 (**fora** da janela), mas as da competência
  2025‑04 (pagas em mai/2025, **dentro** da janela) não estão no resumo; assumindo as
  contribuições constantes (4.700,00 em todas as linhas), o impacto líquido é ≈ 0 e mantemos
  284.600,00. Sem extratos dos outros 11 meses, não há como reconstruir melhor — suposição
  rotulada.

⚠ **Sensibilidade — a margem é de só R$ 1.000,00.** O Fator R atinge 28% quando a folha paga
atingir 0,28 × 1.020.000 = **285.600,00**; temos 284.600,00, ou seja, **faltam R$ 1.000,00**.
O resumo mostra pró‑labore **R$ 0,00 na competência 2026‑03**, sem explicação, e o cliente
declarou não ter informação adicional. Se houver pagamento de pró‑labore **não contabilizado**
(de março/2026 ou de qualquer mês da janela) de valor ≥ 1.000,00 — p. ex. os 3.200,00 típicos,
que levariam a 287.800,00 → 28,22% — o enquadramento vira **Anexo III** e o DAS dos serviços
cairia para 78.000 × 12,5059% = 9.754,59 (DAS total 10.261,08, diferença de R$ 4.927,76).
Calculamos **como estão os dados do acervo** (284.600 → Anexo V) e registramos a pendência em
`STATUS.md`; não "forçamos" ajuste algum.

Em qualquer leitura correta dos dados disponíveis o resultado é **Anexo V** (faixa definida pelo
RBT12 total).

## 3. Anexo e faixa

RBT12 = 1.020.000,00 está na **4ª faixa** das tabelas de `library/anexos_iii_v_tabelas.md`:

- **Anexo V** (serviços de TI, fator R < 28%): alíquota nominal **20,50%**, parcela a deduzir **R$ 17.100,00**.
- **Anexo III** (locação de bens móveis, ver §5): alíquota nominal **16,00%**, parcela a deduzir **R$ 35.640,00**.

**Alíquota efetiva** (LC 123/2006, art. 18, §1º‑A — `(RBT12 × Aliq − PD) / RBT12`):

- Anexo V: (1.020.000 × 0,2050 − 17.100) / 1.020.000 = (209.100 − 17.100)/1.020.000 = **192.000/1.020.000 = 18,8235%**
- Anexo III: (1.020.000 × 0,1600 − 35.640) / 1.020.000 = (163.200 − 35.640)/1.020.000 = **127.560/1.020.000 = 12,5059%**

**Aviso ao pedido do sócio** ("repetir o Anexo V com a alíquota da faixa"): o Anexo V até continua
valendo (por coincidência correta, pois o fator R fica abaixo de 28%), **mas a alíquota da faixa
(20,50%) não é a que se aplica** — o art. 18, §1º‑A manda usar a alíquota efetiva (18,8235%). Usar
20,50% sobre os serviços daria 78.000 × 0,2050 = 15.990,00, isto é, **R$ 1.307,65 a mais** do que o
correto (14.682,35) só nessa linha.

## 4. Receita de maio/2026 — classificação nota a nota

Regra de segregação: LC 123/2006, art. 18, §4º (`library/lc123_art18_fator_r.md`) — segregar por
atividade e aplicar a cada uma o anexo/alíquota próprios.

| Documento | Descrição | Valor (R$) | Classificação | Tratamento |
|---|---|---:|---|---|
| NFS‑e 1181 | Desenvolvimento de software — sprint 11 | 18.000,00 | serviço de TI (desenvolvimento) | Anexo V |
| NFS‑e 1182 | Sustentação mensal — Cliente Orla | 12.500,00 | serviço de TI (suporte) | Anexo V |
| NFS‑e 1183 | Consultoria de arquitetura | 9.800,00 | serviço de TI (arquitetura de software) | Anexo V — ver nota A |
| NFS‑e 1184 | Desenvolvimento — módulo fiscal | 22.000,00 | serviço de TI | Anexo V |
| NFS‑e 1185 | Suporte técnico | 6.700,00 | serviço de TI | Anexo V |
| NFS‑e 1186 | Treinamento equipe | 4.500,00 | serviço — ver nota A | Anexo V (presunção) |
| NFS‑e 1187 | Desenvolvimento — integração | 8.500,00 | serviço de TI | Anexo V |
| NFS‑e 1188 | Estorno parcial da 1184 (glosa acordada) | (4.000,00) | devolução/cancelamento | reduz a receita de serviços de **maio** |
| NF‑e 000.512 | Locação de 20 notebooks — maio | 6.000,00 | **locação de bens móveis** | Anexo III sem ISS (§5) |

**Nota A (classificação — rotulada, não verificada na biblioteca):** a biblioteca define as
atividades de TI por exemplos ("desenvolvimento, licenciamento, suporte etc.", §§5º‑J/5º‑M) e **não**
contém a lista completa de atividades/CNAEs. "Consultoria de arquitetura" (de software) e
"Treinamento equipe" foram tratados como serviços da atividade‑fim de TI da empresa e incluídos no
bloco do Anexo V. Se alguma delas não for atividade de TI para fins de fator R, sua tributação
poderia ser distinta — a biblioteca não permite concluir. Pendência registrada em `STATUS.md`.

**Serviços:** bruto = 18.000+12.500+9.800+22.000+6.700+4.500+8.500 = **82.000,00**
**O estorno:** a regra em `library/lc123_art18_fator_r.md` ("cancelamento/estorno de serviço reduz a
receita do mês em que ocorrer") aplica‑o integralmente em maio: líquido = 82.000,00 − 4.000,00 =
**78.000,00**. O extrato confirma o fluxo (crédito de 22.000,00 da 1184 em 15/05 e devolução de
4.000,00 em 29/05: "PIX ENVIADO ESTORNO GLOSA — CLIENTE 1184").

**Conciliação com o extrato de maio** (créditos): 12.500+18.000+9.800+22.000+6.700+4.500+6.000+8.500
= 88.000,00 recebidos − 4.000,00 devolvidos = 84.000,00 = 78.000,00 (serviços) + 6.000,00 (locação). ✔

## 5. Locação de bens móveis — o que foi feito

O sócio achou que a locação "vai junto com os serviços". **Não vai.** Pela biblioteca
(`library/locacao_bens_moveis_iss.md`: LC 123/2006, art. 18, §5º‑A; Súmula Vinculante 31/STF;
Res. CGSN 140, art. 25, §1º, V): locação de bens móveis é tributada pelo **Anexo III, deduzida a
parcela correspondente ao ISS**, porque não é serviço para fins de ISS.

- Alíquota efetiva Anexo III, 4ª faixa: **12,5059%** (§3 acima).
- Supressão da parcela de ISS da repartição da 4ª faixa do Anexo III (32,50%,
  `library/anexos_iii_v_tabelas.md`): 12,5059% × (1 − 0,325) = **8,4415%**.
- **DAS locação = 6.000,00 × 8,4415% = R$ 506,49.**
- ISS sobre a locação: **zero** (Súmula Vinculante 31, via biblioteca).
- *Mecânica rotulada:* a biblioteca diz "deduzida a parcela correspondente ao ISS" mas não detalha
  se a dedução incide sobre a alíquota efetiva ou sobre o valor; aplicamos sobre a parcela
  (percentual) da repartição — leitura que coincide com a sistemática do valor do DAS.
- *Confirmado pelo cliente (rodada 2):* "alugamos 20 notebooks pra Orla por uns meses; emití NF‑e
  porque me disseram que locação não é NFS‑e." A prática da NF‑e é coerente com a biblioteca
  (locação de bens móveis não é serviço de ISS — SV 31). O histórico "por uns meses" reforça a
  suposição do §1 de que o `faturamento_12_meses.csv` já inclui locações dos meses anteriores.

## 6. DAS de maio/2026

| Atividade | Receita (R$) | Base legal | Alíquota aplicada | DAS (R$) |
|---|---:|---|---:|---:|
| Serviços de TI | 78.000,00 | Anexo V, 4ª faixa, §1º‑A | 18,8235% efetiva | 78.000 × 0,188235 = **14.682,35** |
| Locação bens móveis | 6.000,00 | Anexo III, 4ª faixa, sem ISS | 12,5059% × 67,5% = 8,4415% | 6.000 × 0,084415 = **506,49** |
| **Total** | 84.000,00 | | | **R$ 15.188,84** |

(Valores exatos antes de arredondar: serviços 14.682,3529…; locação 506,4882…; total 15.188,84.)

## 7. Repartição por tributo

**Parte serviços (Anexo V) — NÃO VERIFICADA:** os percentuais de repartição do **Anexo V** não
constam da biblioteca (que só traz a repartição da 4ª faixa do Anexo III). Os percentuais abaixo
(IRPJ 14%, CSLL 9%, COFINS 20%, PIS 4%, CPP 37%, ISS 16% — soma 100%) são **suposição não
verificada**, sem fonte citável, aplicada sobre R$ 14.682,35. Recomenda‑se confirmar na guia PGDAS.

**Parte locação (Anexo III) — percentuais da biblioteca** (`anexos_iii_v_tabelas.md`, 4ª faixa):
sobre o valor cheio do Anexo III (6.000 × 12,5059% = 750,35), sem a parcela de ISS:

## 8. Tabela final da repartição (serviços + locação) e a diferença que não fecha

| Tributo | % Anexo V (não verificado) | R$ serviços | % Anexo III (biblioteca) | R$ locação | Total (R$) |
|---|---:|---:|---:|---:|---:|
| IRPJ | 14,00% | 2.055,53 | 4,00% | 30,01 | **2.085,54** |
| CSLL | 9,00% | 1.321,41 | 3,50% | 26,26 | **1.347,67** |
| COFINS | 20,00% | 2.936,47 | 14,05% | 105,42 | **3.041,89** |
| PIS | 4,00% | 587,29 | 3,05% | 22,89 | **610,18** |
| CPP | 37,00% | 5.432,47 | 42,75% | 320,78 | **5.753,25** |
| ISS | 16,00% | 2.349,18 | — (SV 31) | 0,00 | **2.349,18** |
| Soma | | 14.682,35 | 99,85% | 505,36 | **15.187,71** |

⚠ **Não forçamos o fechamento.** A repartição da 4ª faixa do Anexo III na biblioteca soma
**99,85%** (4,00+3,50+14,05+3,05+42,75+32,50), não 100%. Por isso a parte da locação soma
505,36 contra 506,49 apurados — **diferença de R$ 1,13**, que deixamos aberta como item de
conciliação da própria tabela da biblioteca.

## 9. Fontes

- `library/lc123_art18_fator_r.md` — RBT12 (§1º), alíquota efetiva (§1º‑A), fator R (§§5º‑J/5º‑M),
  folha paga (Res. CGSN 140, art. 26), segregação (§4º), estornos.
- `library/anexos_iii_v_tabelas.md` — tabelas dos Anexos III e V e repartição da 4ª faixa do Anexo III.
- `library/locacao_bens_moveis_iss.md` — locação de bens móveis: Anexo III sem ISS (SV 31).
- Documentos do cliente: `notas_emitidas_maio.md`, `extrato_maio_2026.csv`/`.pdf`,
  `faturamento_12_meses.csv`, `resumo_folha_12_meses.csv`, `email_socio.txt`, `nfe_000512_locacao.xml`.
- Respostas do cliente (rodada 2, verbais no processo; comprovante de 30/04 prometido mas **não
  recebido** no acervo): data de pagamento do pró‑labore de abril (30/04/2026), motivo do "em
  aberto" no resumo (PIX lançado em maio), histórico da locação dos notebooks à Orla.
- Nada fora da biblioteca foi citado. Itens não verificados estão rotulados (repartição do Anexo V;
  classificação de consultoria/treinamento; mecânica da dedução do ISS; contribuições de 2025‑04
  no corte da base pagamentos).
