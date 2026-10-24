# Memória de cálculo — DAS maio/2026 · Lumen Soluções Digitais ME

**Base legal utilizada:** somente a biblioteca fechada (`library/INDEX.md`): `lc123_art18_fator_r.md`
(LC 123/2006, art. 18, §§1º, 1º-A, 4º, 5º-A, 5º-J, 5º-K, 5º-M; Res. CGSN 140/2018, arts. 25 e 26),
`anexos_iii_v_tabelas.md` (Anexos III e V, redação LC 155/2016) e `locacao_bens_moveis_iss.md`
(locação de bens móveis — sem ISS; Súmula Vinculante 31). Nada fora da biblioteca foi citado; o que
não está nela está explicitamente marcado como **NÃO VERIFICADO**.

**Período de apuração:** maio/2026. Janela dos 12 meses anteriores (RBT12 e Fator R): **mai/2025 – abr/2026**.

---

## 1. Receita do mês (maio/2026) — classificação de cada nota

| Documento | Descrição | Valor (R$) | Classificação | Fonte |
|---|---|---:|---|---|
| NFS-e 1181 | Desenvolvimento de software — sprint 11 | 18.000,00 | serviço (TI) | `notas_emitidas_maio.md`; crédito TED 05/05 no extrato |
| NFS-e 1182 | Sustentação mensal — Cliente Orla | 12.500,00 | serviço (TI) | `notas_emitidas_maio.md`; PIX 02/05 |
| NFS-e 1183 | Consultoria de arquitetura | 9.800,00 | serviço (TI) | `notas_emitidas_maio.md`; PIX 09/05 |
| NFS-e 1184 | Desenvolvimento — módulo fiscal | 22.000,00 | serviço (TI) | `notas_emitidas_maio.md`; TED 15/05 |
| NFS-e 1185 | Suporte técnico | 6.700,00 | serviço (TI) | `notas_emitidas_maio.md`; PIX 19/05 |
| NFS-e 1186 | Treinamento equipe | 4.500,00 | serviço (TI) | `notas_emitidas_maio.md`; PIX 22/05 |
| NFS-e 1187 | Desenvolvimento — integração | 8.500,00 | serviço (TI) | `notas_emitidas_maio.md`; PIX 28/05 |
| NFS-e 1188 | Estorno parcial da 1184 (glosa de escopo) | (4.000,00) | **dedução da receita do mês do cancelamento** | `notas_emitidas_maio.md`; PIX enviado 29/05 |
| NF-e 000.512 | Locação de 20 notebooks — maio | 6.000,00 | **locação de bens móveis** (CFOP 5949, natOp "Locação de bens móveis") | `nfe_000512_locacao.xml`; TED 26/05 |

**Aritmética:** 18.000 + 12.500 + 9.800 + 22.000 + 6.700 + 4.500 + 8.500 = **82.000,00** serviços brutos.

### O estorno
A biblioteca (art. 18: "devoluções/cancelamentos") determina que o cancelamento/estorno de serviço
**reduz a receita do mês em que ocorrer**. A NFS-e 1188 (glosa acordada de R$ 4.000,00 sobre a 1184)
foi emitida e paga em maio/2026 (PIX de −4.000,00 em 29/05 no extrato). Portanto reduz a receita de
**maio/2026** → serviços do mês = 82.000,00 − 4.000,00 = **78.000,00**. A janela do RBT12 para
maio/2026 (mai/25–abr/26) não é afetada.

### A locação
A NF-e 000.512 é locação de bens móveis. Pela biblioteca (`locacao_bens_moveis_iss.md`: art. 18,
§5º-A; SV-31; Res. CGSN 140, art. 25, §1º, V), essa receita é tributada pelo **Anexo III, deduzida a
parcela correspondente ao ISS**, e deve ser **segregada** das demais receitas (art. 18, §4º). Ela
NÃO se mistura com os serviços do Anexo V, ao contrário do palpite do sócio no e-mail ("acho que vai
junto com os serviços"). Receita do mês: **6.000,00**.

### Conciliação com o extrato (mai/2026)
Créditos: 12.500 + 18.000 + 9.800 + 22.000 + 6.700 + 4.500 + 6.000 + 8.500 = 88.000,00 = notas (82.000)
+ locação (6.000) ✓. Débitos: 16.600 (folha mai) + 4.700 (DARF/GPS/FGTS **abr**) + 4.200 (aluguel) +
3.200 (pró-labore **mai**) + 10.480,22 (DAS **abr**) + 4.000 (estorno) = 43.180,22 ✓. Saldo final
86.100,33 = 41.280,55 + 88.000,00 − 43.180,22 ✓ (`extrato_maio_2026.csv`/`.pdf`).

---

## 2. RBT12 (para a alíquota nominal)

Soma de `faturamento_12_meses.csv` (mai/2025–abr/2026):
78.000 + 81.500 + 84.000 + 86.000 + 79.500 + 90.000 + 88.000 + 92.000 + 85.000 + 83.000 + 86.000 + 87.000 =
**R$ 1.020.000,00** → **4ª faixa** (até 1.800.000,00) em ambos os anexos.

Obs.: assumi que essa planilha já reflete cancelamentos/estornos ocorridos em cada mês (não há
detalhamento mensal). Ver `PERGUNTAS.md` #5.

## 3. Fator R — folha dos 12 meses anteriores

A biblioteca (Res. CGSN 140, art. 26, §§1º-2º) define folha como o montante **pago** nos 12 meses
anteriores (salários + pró-labore + contribuições patronais + FGTS), **independentemente da competência**.

`resumo_folha_12_meses.csv` (mesma janela): salários 193.000 + pró-labore 35.200 + encargos 56.400 =
**R$ 284.600,00**.

**Pró-labore abr/2026 (R$ 3.200,00, linha 2026-04):** o sócio esclareceu (resposta à pergunta 2) que
foi **pago em 30/04/2026** — dentro da janela mai/25–abr/26 — e que o resumo saiu com a obs. "em
aberto" porque o PIX foi lançado no sistema só em maio. O e-mail anterior ("paguei atrasado, dia 6
de maio") estava equivocado: o extrato de maio não tem débito de 3.200,00 em 06/05, compatível com
pagamento ocorrido em abril. **Incluído** na folha pelo critério de caixa do §2º. Comprovante de
30/04 prometido pelo cliente — **ainda não recebido**; se ele mostrar data posterior, a folha volta a
281.400,00 (27,59%) — **o enquadramento não muda** (Anexo V nas duas hipóteses).

**Folha adotada = R$ 284.600,00. Fator R = 284.600 / 1.020.000 = 0,279020 = 27,90% < 28% →
ANEXO V** (art. 18, §§5º-J/5º-M).

Encargos: o extrato mostra o pagamento dos encargos de abr/2026 (DARF/GPS/FGTS **abr**, 4.700,00)
apenas em **07/05/2026**. Mantive os 56.400,00 porque, se os encargos são pagos no mês seguinte à
competência em todos os meses, os valores pagos na janela (competências abr/25–mar/26) equivalem aos
acumulados no resumo (4.700 fixos/mês: −4.700 de abr/26 +4.700 de abr/25). Isso é uma **inferência**,
não um fato comprovado; o cliente não tinha informação adicional (pergunta 3 sem resposta).

### Sensibilidade (por que o Anexo V é robusto)

| Cenário | Folha (R$) | Fator R | Anexo |
|---|---:|---:|---|
| **A. Adotado: pró-labore abr pago 30/04 (dentro da janela); mar/26 = 0 no resumo** | **284.600** | **27,90%** | **V** |
| B. Se o comprovante de 30/04 mostrar pagamento posterior (ex.: 06/05) | 281.400 | 27,59% | V |
| C. Caixa estrito dos encargos sem a inferência de equivalência (exclui encargos abr/26, pagos 07/05) | 279.900 | 27,44% | V |
| D. **Risco residual:** se houver pró-labore de mar/2026 (~3.200,00) pago dentro da janela, além do de abr | 287.800 | 28,22% | III |

Só o cenário **D** levaria ao Anexo III. Ele depende de um único fato desconhecido: a linha 2026-03
do resumo traz pró-labore 0,00 (com obs. aparentemente deslocada sobre abril), e o cliente **não soube
informar** se houve pró-labore de março pago na janela. O Anexo V (pedido do sócio: "repetir o Anexo
V") coincide com o resultado dos documentos disponíveis; o cenário D está sinalizado em `STATUS.md`.

## 4. Alíquotas e DAS

**Serviços (Anexo V, 4ª faixa):** alíquota nominal 20,50%, parcela a deduzir 17.100,00
(`anexos_iii_v_tabelas.md`).
- Alíquota efetiva (§1º-A): (1.020.000 × 0,2050 − 17.100,00) / 1.020.000 = (209.100 − 17.100) / 1.020.000 =
  192.000 / 1.020.000 = **18,823529%**
- DAS serviços = 78.000,00 × 18,823529% = **R$ 14.682,35**

**Locação de bens móveis (Anexo III, 4ª faixa, sem ISS):** nominal 16,00%, PD 35.640,00.
- Efetiva cheia = (1.020.000 × 0,16 − 35.640) / 1.020.000 = 127.560 / 1.020.000 = 12,505882%
- Deduzida a parcela de ISS (cota do ISS na 4ª faixa do Anexo III = **32,50%**, tabela da biblioteca):
  12,505882% × (1 − 0,3250) = **8,441471%**
- DAS locação = 6.000,00 × 8,441471% = **R$ 506,49**

**DAS total maio/2026 = 14.682,35 + 506,49 = R$ 15.188,84**

### Repartição dos R$ 15.188,84

| Tributo | Serviços (R$) | Locação (R$) | Total (R$) |
|---|---:|---:|---:|
| IRPJ | 763,48 | 30,01 | 793,49 |
| CSLL | 668,05 | 26,26 | 694,31 |
| COFINS | 2.679,53 | 105,42 | 2.784,95 |
| PIS | 582,89 | 22,89 | 605,78 |
| CPP | 8.161,92 | 321,91 | 8.483,83 |
| ISS | 1.826,48 | 0,00 | 1.826,48 |
| **Total** | **14.682,35** | **506,49** | **15.188,84** |

- **Locação:** cotas da 4ª faixa do Anexo III (IRPJ 4,00 · CSLL 3,50 · COFINS 14,05 · PIS 3,05 ·
  CPP 42,75) aplicadas sobre o DAS cheio de 12,505882%, com **ISS = 0** (SV-31) — verificado na biblioteca.
- **Serviços:** as cotas de repartição do **Anexo V não constam da biblioteca**. Usei, **NÃO
  VERIFICADO** (sem fonte citável, apenas para preencher o quadro), IRPJ 5,20 · CSLL 4,55 ·
  COFINS 18,25 · PIS 3,97 · CPP 55,59 · ISS 12,44. Solicitei as cotas oficiais ao cliente
  (`PERGUNTAS.md` #4); se divergentes, a repartição será corrigida — o total do DAS não muda.
- Ajustes de arredondamento de centavos foram lançados em CPP.
- Nota: o ISS de 1.826,48 é a cota interna do DAS-Simples dos serviços; a locação não gera ISS (SV-31).

## 5. Pontos que NÃO fecham (abertos, não forcei equilíbrio)

1. **Pró-labore mar/2026 (único fato que pode mudar o enquadramento):** a linha 2026-03 do resumo traz
   pró-labore 0,00, com a obs. "pró-labore de abril: em aberto na data do resumo" (nota aparentemente
   fora de posição). O cliente **não soube informar** se houve pró-labore de março e se foi pago na
   janela. Se existir um valor (~3.200,00) pago em mai/25–abr/26, a folha iria a 287.800,00 → Fator R
   28,22% ≥ 28% → **Anexo III** para os serviços: efetiva cheia 12,505882%, DAS serviços
   78.000 × 12,505882% = **9.754,59** e DAS total **10.261,08** (contra 15.188,84). Diferença relevante
   — verificar no extrato bancário de mar/2026 (fora dos documentos fornecidos).
2. **Comprovante do pró-labore abr/2026 (30/04) ainda não recebido.** Prometido pelo cliente. Em
   qualquer data plausível (30/04 ou posterior) o enquadramento é Anexo V; apenas a folha oscila
   284.600 ↔ 281.400.
3. **DAS abr/2026 pago (10.480,22 em 20/05) não reconcilia** com os documentos: para abr, RBT12 =
   933.000 (4ª faixa). Anexo V cheio: 87.000 × 18,6672% = 16.240,47; Anexo III cheio: 10.596,66.
   Nenhum cenário limpo dá 10.480,22 (Anexo III com segregação de uma locação de ~6k daria ~10.359).
   Deixo aberto — pode indicar premissas diferentes usadas pelo contador em abril.
4. **Cotas de repartição do Anexo V** não constam da biblioteca; os percentuais usados na repartição
   dos serviços são **NÃO VERIFICADO** (item 4 de `PERGUNTAS.md`, sem resposta do cliente). O total do
   DAS não depende deles.
5. **Base do `faturamento_12_meses.csv`** (líquida de estornos? inclui a locação?) — pergunta 5 sem
   resposta; afeta RBT12 e, por consequência, faixa/alíquotas.
6. **Timing de pagamento dos encargos** (pergunta 3 sem resposta): a equivalência de caixa assumida em
   §3 permanece inferência.

## 6. Instrução do sócio vs. direito

"Repetir o Anexo V com a alíquota da faixa": confirmado pelo cálculo — Fator R < 28% em todos os
cenários suportados pelos documentos (o único cenário que inverteria para o Anexo III, D, depende de
um fato inexistente nos documentos e desconhecido do cliente). Mas **não** se repete um anexo único
"com a alíquota da faixa" sobre tudo: a
alíquota é a **efetiva** (§1º-A), os serviços (Anexo V) e a locação (Anexo III sem ISS) são
**segregados** (§4º), e o estorno reduz a receita do mês em que ocorreu.
