# Proposta de acordo — Marcelo Andrade × Fernanda Andrade

Casados em 2014, **comunhão parcial** (sem pacto antenupcial), dois filhos (9 e 6 anos).
Fonte de dados: `documents/resumo_patrimonio.md`, `documents/email_cliente.txt`, `documents/formal_partilha_atibaia.md`. Autoridade citável: `library/INDEX.md`. Cálculos em Python (aritmética exibida abaixo).

## 1. Quadro de partilha (conforme `partilha.json`)

| Bem | Natureza | Valor total (R$) | Partilhável (R$) | Meação de Fernanda (R$) |
|---|---|---:|---:|---:|
| Apartamento (Perdizes), comprado 2017 | comum | 1.200.000 | 1.200.000 | 600.000 |
| Casa Atibaia — herança do pai (2019, matr. 11/2019) | particular | 800.000 | 0 | 0 |
| FGTS de Marcelo — depositado todo no casamento | comum | 140.000 | 140.000 | 70.000 |
| Quotas Andrade Engenharia (constituída 2011) | misto | 1.500.000 | 1.100.000 | 550.000 |
| PGBL Fernanda (aportes 2016–2025) | comum | 90.000 | 90.000 | 45.000 |
| Carro SUV (uso da família) | comum | 120.000 | 120.000 | 60.000 |
| **DIVIDAS** (apto 300.000 + carro 60.000) | comum (CC 1.664) | 360.000 | **−360.000** | **−180.000** |
| **TOTAL** | | 3.850.000 | **2.290.000** | **1.145.000** |

Arithmetic (executada em Python):
- 1.200.000 + 140.000 + 1.100.000 + 90.000 + 120.000 = **2.650.000** (bruto partilhável)
- 2.650.000 − 360.000 = **2.290.000** (líquido partilhável)
- Meação de cada cônjuge: 2.290.000 ÷ 2 = **1.145.000**
- Fração comunicável das quotas: 1.500.000 − 400.000 (valor de 2014) = 1.100.000 → meação 1.100.000 ÷ 2 = **550.000**

Fora da meação (particulares): casa de Atibaia (R$ 800.000, CC 1.659 I) e a parcela das quotas existente em 2014 (R$ 400.000).

## 2. Atribuição proposta e equalização

| Item | Fica com | Valor atribuído (R$) |
|---|---|---:|
| Apartamento (líquido, assume financiamento 300.000) | Marcelo | 900.000 |
| FGTS (integral; saque diferido) | Marcelo | 140.000 |
| Quotas (integral; paga haveres à Fernanda) | Marcelo | 1.100.000 (da fração comunicável) |
| Casa Atibaia (particular) | Marcelo | *fora da conta* |
| Carro (assume financiamento 60.000) | Fernanda | 60.000 |
| PGBL (integral) | Fernanda | 90.000 |

Ledger (Python): in-kind de Marcelo = (1.200.000−300.000) + 140.000 + 1.100.000 = **2.140.000**; in-kind de Fernanda = (120.000−60.000) + 90.000 = **150.000**. Equalização = 2.140.000 − 1.145.000 = **995.000**.

**Marcelo paga a Fernanda R$ 1.055.000,00 decomposto em:**
1. **R$ 550.000** — apuração de haveres da fração comunicável das quotas (STJ REsp 1.595.775/AP; sem ingresso na sociedade, na forma do CC 1.027 conforme a biblioteca);
2. **R$ 445.000** — equalização por excesso de bens comuns recebidos em espécie (2.140.000 − 1.100.000 − 595.000 = 445.000, onde 595.000 = meação de Marcelo sobre os demais bens, 1.190.000 ÷ 2);
3. **R$ 60.000** — compensação pela reforma da casa de Atibaia (2021) paga com verba comum confirmada pelo cliente (~120.000). NÃO é meação de bem comum: a biblioteca não disciplina reposição de verba comum investida em bem particular — proposta como abono composicional, de natureza **unverified** (documentar na escritura como contraprestação, não doação).

Conferência: Fernanda termina com 150.000 + 1.055.000 = **1.205.000** = meação 1.145.000 + compensação 60.000. O pagamento 1 e 2 fecham exatamente na meação (995.000); o item 3 é adicional.

## 3. Alimentos e guarda (conforme `alimentos.json`)

- **Guarda:** compartilhada — é a REGRA quando ambos os genitores são aptos e não houver acordo (CC art. 1.584, §2º, Lei 13.058/2014; art. 1.583 — `guarda_compartilhada.md`), que é exatamente o caso (cliente quer acordo; nada no acervo indica inaptidão). A compartilhada **não** significa divisão igual de tempo e **não** afasta alimentos (`guarda_compartilhada.md`).
- **Alimentos** (binômio e proporcionalidade, CC arts. 1.694 §1º, 1.695, 1.699 — `alimentos_base_calculo.md`): base = **líquidos** (a prática judicial varia de 15% a 30% de rendimentos líquidos). Atualizada com a resposta do cliente: 24.000 (CLT líquido) + 15.000 (pró-labore habitual da própria empresa — *premissa: tomados como líquidos; o cliente não qualificou*). Sugiro **25%**: R$ 9.750/mês (25% × 39.000) + 13º R$ 6.000 (25% × 24.000) + férias R$ 8.000 (25% × 32.000) = **R$ 131.000/ano** (12 × 9.750 + 6.000 + 8.000). Fernanda aufere R$ 9.000 líquidos/mês, o que sustenta a proporcionalidade.
- Pegada prática: 9.750/mês (total dos dois filhos), complementos de 13º e férias no respectivo mês; o pró-labore também compõe a base todo mês. 13º/retiradas especiais do pró-labore: não informados — se existirem, incidirá o mesmo percentual.
- Detalhe tático da resposta: com a base corrigida (39.000 líquidos), 25% ≈ o que a peça oposta alcança de 30% sobre líquidos puros — argumento de fechamento para a Fernanda.

## 4. Tributos (IN RFB 84/2001 arts. 3º §3º e 20; Lei 10.705/2000/SP art. 2º §5º — `tributos_partilha.md`)

- **Excesso de meação:** com o ledger acima cada cônjuge termina com exatamente 1.145.000 (50%) **em bens comuns** → **não há excesso** na atribuição partilhável; logo **não incide ITBI (3% SP) nem ITCMD (4% SP)** sobre essa estrutura.
- **Compensação da reforma (60.000):** pagamento adicional sobre a meação. Para não caracterizar doação (ITCMD 4%), a escritura deve documentá-la como **contraprestação/ressarcimento pela verba comum empregada em bem particular** — a biblioteca exige que a partilha "seja desenhada para equalizar e documentar a contraprestação" (`tributos_partilha.md`). O próprio subjacente jurídico dessa compensação é unverified; o risco tributário descrito segue a única regra disponível na biblioteca (ITCMD se gratuito, ITBI se oneroso).
- **Ganho de capital:** os bens podem ser atribuídos pelo **valor da declaração de bens** sem ganho de capital; se atribuídos por valor superior, a diferença é ganho de capital (IN RFB 84/2001). Os valores usados aqui vêm do laudo/resumo; **não tenho as declarações anuais (AVL) dos cônjuges** (cliente informou não ter essa informação) — ANTES da lavratura: obter as declarações e lavrar pelos valores declarados; se o laudo (ex.: quotas 1.500.000) superar a declaração, haverá ganho de capital sobre a diferença.

## 5. O que RECUSAR da proposta da advogada de Fernanda, e por quê

| Cláusula oposta | Posição | Fundamento (só da biblioteca) |
|---|---|---|
| "Metade da casa de Atibaia" | **RECUSAR** (ponto não negociável) | Herança recebida em 2019 pelo Marcelo — bem particular e sub-rogados (CC 1.659, I); formal de partilha anexo. Também é despido de propósito tributário: sairia como excesso de meação → ITCMD 4% (gratuito) ou ITBI 3% (oneroso, imóvel) sobre a parte de Fernanda (`tributos_partilha.md`). |
| "Metade das quotas" | **RECUSAR na forma apresentada** | As quotas são particulares até o valor de 2014 (400.000); só a valorização/lucros do período comum comunicam (CC 1.659, I e 1.660, V; STJ REsp 1.595.775/AP) = **1.100.000 → meação 550.000 via haveres, sem ingresso na sociedade (CC 1.027)**. Não é "metade da empresa", é apuração de haveres da fração. Concedo os 550.000 na equalização. |
| "FGTS fica com o Marcelo porque é dele" | **CORRIGIR — conceder meação de 70.000** | STJ REsp 1.399.199/RS (2ª Seção, 2017): depósitos na constância integram o comum e partilham, ainda que o saque fique diferido; CC 1.659, VI, não afasta. É erro juridicamente A FAVOR do cliente; mantê-lo convidaria a discutir toda a partilha em juízo. Concedo e compenso. |
| "Pensão de 30% do BRUTO, incluindo FGTS, verbas rescisórias e PLR" | **RECUSAR a base e mantenho o teto alto no percentual** | Base correta = LÍQUIDOS (15–30% da prática); FGTS (depósitos/saque, inclusive os 2.400/mês) e verbas rescisórias indenizatórias saem da base (AgInt no AREsp; STJ, `alimentos_base_calculo.md`); PLR só quando habitual (controvérsia contra). Contra-proposta atualizada com os rendimentos confirmados pelo cliente (39.000 líquidos/mês): **25% dos líquidos** + 13º + férias = R$ 131.000/ano — praticamente o mesmo valor que a peça oposta alcançaria sobre líquidos puros a 30%, o que esvazia a briga. |
| "Guarda unilateral materna, visitas quinzenais" | **RECUSAR** | Compartilhada é a regra legal na falta de acordo (CC 1.584, §2º); redigir plano de convivência, não "visitas". Não afasta alimentos. |
| "Carro fica com a Fernanda" | **ACEITAR, com a dívida** | Cliente confirmou: carro da família, no nome dela, financiamento também no nome dela. Ela retém o SUV e assume o financiamento de 60.000 (dívida comum por uso familiar, CC 1.664). No ledger isso equivale a atribuir a ela 120.000 brutos e onerá-la de 60.000. |
| Reforma da casa de Atibaia (120.000 com verba comum, 2021) | **ACEITAR, limitada** | A casa permanece particular (CC 1.659, I), mas é inegociável tecnicamente que saiu dinheiro comum: proponho compensação de 60.000 (metade de 120.000) na equalização. Fundamento específico **não consta na biblioteca** — unverified; uso como abono composicional, não como direito. |

## 6. Premissas registradas (não inventadas como fatos)

1. **Pró-labore:** confirmado pelo cliente em R$ 15.000/mês, habitual, "fora o salário de 24 mil de um emprego CLT". PREMISSA: tomado como **líquido** — o cliente não qualificou líquido/bruto; se bruto, a base de alimentos desce e o valor baixa (aberto em STATUS).
2. **Quotas:** cliente confirma 400.000 ao casar, 1.500.000 hoje, **sem distribuição de lucros (tudo reinvestido)** — reforça a comunicabilidade da valorização (STJ REsp 1.595.775/AP; CC 1.660, V). Data da separação de fato permanece desconhecida: usa-se o valor do laudo como ponta final.
3. **Carro:** cliente confirma uso pela família e financiamento no nome dela; data da compra continua desconhecida → presunção CC 1.662 mantém a natureza comum.
4. **Casa de Atibaia:** cliente confirma reforma de 2021 com ~120.000 de verba comum → compensação proposta de 60.000 (natureza unverified). Aluguéis/frutos do imóvel: sem resposta → presumo nenhum (frutos seriam comuns, CC 1.660, V, caso houvesse).
5. **Residência de referência dos filhos:** assumida com a Fernanda, decorrente da proposta de guarda unilateral dela.
6. **Valores de declaração (AVL):** cliente não informou; a partilha pressupõe atribuição pelos valores declarados (IN RFB 84/2001) — obter antes da escritura.
7. **FGTS/PGBL/PLR:** sem novas informações → mantêm-se os valores do resumo (140.000; 90.000) e a PLR fora da base por desconhecimento do hábito.

## 7. Recomendação ao cliente

Fechar com Fernanda em: (i) casa de Atibaia só para Marcelo, com a compensação de 60.000 pela reforma (barato perto de perder metade do imóvel); (ii) quotas: haveres de 550.000, sem participação societária; (iii) FGTS partilhado (70.000) para eliminar o erro da peça oposta; (iv) alimentos 25% dos líquidos de 39.000 = 9.750 + 13º e férias (≈ 131.000/ano) — com a base correta, a proposta dela de 30% "do bruto" praticamente converge, o que encerra a briga; (v) guarda compartilhada com plano de convivência; (vi) atribuição: cada cônjuge termina em 1.145.000 (mais os 60.000), sem ITBI/ITCMD, pendente conferência com as declarações anuais (ganho de capital). Marcelo pagará no total **R$ 1.055.000** (550.000 haveres + 445.000 equalização + 60.000 reforma).

