# Memória de cálculo — DAS maio/2026
**Lumen Soluções Digitais ME** (CNPJ 41.228.907/0001-55, CRT 1 — Simples Nacional)
Período de apuração: **maio/2026**. Fontes: `documents/` (client file as received) + `library/` (only authority cited).

## 1. Receitas de maio/2026 (classificação de cada nota)

| Documento | Classificação | Valor | Tratamento |
|---|---|---:|---|
| NFS-e 1181 (software — sprint 11) | Serviços (TI) | 18.000,00 | receita bruta do mês |
| NFS-e 1182 (sustentação — Orla) | Serviços (TI) | 12.500,00 | receita bruta do mês |
| NFS-e 1183 (consultoria de arquitetura) | Serviços (TI) | 9.800,00 | receita bruta do mês |
| NFS-e 1184 (módulo fiscal) | Serviços (TI) | 22.000,00 | bruto; sofre glosa parcial |
| NFS-e 1185 (suporte técnico) | Serviços (TI) | 6.700,00 | receita bruta do mês |
| NFS-e 1186 (treinamento) | Serviços (TI) | 4.500,00 | receita bruta do mês |
| NFS-e 1187 (integração) | Serviços (TI) | 8.500,00 | receita bruta do mês |
| NFS-e 1188 (estorno parcial de 1184) | Estorno/cancelamento | (4.000,00) | reduz a receita do mês em que ocorre |
| NF-e 000.512 (locação de 20 notebooks) | **Locação de bens móveis** | 6.000,00 | segregada — Anexo III sem ISS (item 4) |

- Serviços (bruto): 18.000 + 12.500 + 9.800 + 22.000 + 6.700 + 4.500 + 8.500 = **82.000,00** (bater com `notas_emitidas_maio.md` ✓).
- **Estorno:** o cancelamento/estorno de serviço reduz a receita do mês em que ocorre → 82.000,00 − 4.000,00 = **78.000,00** (Citação: `lc123_art18_fator_r.md` — "Devoluções/cancelamentos"). O estorno foi pago ao cliente em 29/05 (`extrato_maio_2026.csv`: "PIX ENVIADO ESTORNO GLOSA — CLIENTE 1184, −4.000,00") ✓.
- **Locação:** o sócio sugeriu juntá-la aos serviços, mas a locação de bens móveis **não é serviço para fins de ISS** (Súmula Vinculante 31) e é tributada na forma do **Anexo III, deduzida a parcela do ISS** (Citação: `locacao_bens_moveis_iss.md`). As receitas devem ser segregadas por atividade, aplicando-se a cada uma o anexo e a alíquota correspondentes (Citação: `lc123_art18_fator_r.md` — "Segregação de receitas, art. 18, §4º"). Portanto a locação (R$ 6.000,00) é apurada à parte.
- Conferência com o extrato: os 8 recebimentos (12.500; 18.000; 9.800; 22.000; 6.700; 4.500; 6.000; 8.500) batem com as notas; o "DAS ABR/2026 (−10.480,22)" é a guia de abril, irrelevante para maio.
- A NF-e 000.512 declara-se "documento fictício gerado para benchmark; sem validade fiscal" (seu próprio `infCpl`); usamos apenas a operação (locação, R$ 6.000,00), não os cálculos de imposto embutidos nela.

**Assunção (destacada):** todos os valores das NFS-e de maio são de serviços de TI dentro das atividades que elegem o Anexo III/V pelo Fator R ("desenvolvimento, licenciamento, suporte etc." — Citação: `lc123_art18_fator_r.md`), o que é coerente com o email do sócio ("Ano passado a gente pagava pelo Anexo V (TI)").

## 2. RBT12 (12 meses anteriores a maio/2026: mai/2025–abr/2026)

Somatório de `faturamento_12_meses.csv` (competência mai/2025 a abr/2026):
78.000 + 81.500 + 84.000 + 86.000 + 79.500 + 90.000 + 88.000 + 92.000 + 85.000 + 83.000 + 86.000 + 87.000 = **R$ 1.020.000,00**

Para a alíquota nominal usa-se a receita bruta acumulada nos 12 meses anteriores (Citação: `lc123_art18_fator_r.md` — §1º).
**Assunção (destacada):** o arquivo traz receita bruta total (sem segregação); uso como RBT12 total. O estorno de maio não altera o RBT12 (ocorreu no mês de apuração, não nos 12 anteriores).

## 3. Folha de salários dos 12 meses (Fator R) — critério de **pagamento**

Regra: para o Fator R consideram-se os valores **pagos** no período, independentemente do mês de competência (Citação: `lc123_art18_fator_r.md` — Res. CGSN 140, art. 26, §§1º-2º). Período: pagamentos efetivados entre mai/2025 e 30/abr/2026.

Saldo do resumo por competência (`resumo_folha_12_meses.csv`): 23.400 + 23.400 + 23.800 + 23.800 + 23.800 + 24.100 + 24.100 + 24.100 + 24.300 + 24.300 + 20.900 + 24.600 = **284.600,00** (competência).

Ajustes para o critério de pagamento:
- **Pró-labore de abril (R$ 3.200,00): INCLUÍDO (corrigido após resposta do cliente).** Na primeira versão eu o excluí baseado no email do sócio ("paguei atrasado, dia 6 de maio") e na obs. da linha 2026-03 ("pró-labore de abril: em aberto na data do resumo"). **O cliente esclareceu:** o pagamento foi feito em **30/04/2026** (R$ 1.600 por sócio); a contabilidade o marcou "em aberto" no resumo apenas porque o lançamento do PIX no sistema só ocorreu em maio. 30/04/2026 está **dentro** dos 12 meses anteriores a maio/2026 → o valor (que já consta na linha 2026-04 do resumo) permanece na folha. O comprovante de 30/04 foi prometido pelo cliente, mas **não chegou ao workspace** — a data de pagamento é, portanto, por representação do cliente (item aberto, sem efeito no valor se confirmada).
- **Encargos de abril (DARF/GPS/FGTS ABR, R$ 4.700,00): excluídos.** O extrato de maio mostra o pagamento em **07/05/2026**, fora do período (mai/2025–30/abr/2026). A regra da biblioteca é estritamente de caixa: pago em maio/2026 → fora dos 12 meses anteriores, ainda que na prática seja o recolhimento "no prazo" de abril.
- **Assunção (destacada):** para os demais meses (mai/2025–mar/2026) não há extratos; presumo pago no período o valor da competência (sem atrasos reportados).

**folha_12m = 284.600,00 − 4.700,00 = R$ 279.900,00**

### Fator R
Fator R = folha / RBT12 = 279.900 / 1.020.000 = **0,274412 (27,44%) < 28%** → **Anexo V** (Citação: `lc123_art18_fator_r.md` — §5º-J/§5º-M: Anexo III se ≥ 28%, senão Anexo V).

**Sensibilidade (resultado robusto):** mesmo incluindo os encargos de abril (284.600 → 27,90%), o Fator R fica < 28% → Anexo V em todos os cenários.

## 4. Faixa, alíquotas e DAS

**Serviços (Anexo V):** RBT12 = 1.020.000,00 → **Faixa 4** (720.000,00 < RBT12 ≤ 1.800.000,00); alíquota nominal 20,50%; parcela a deduzir 17.100,00 (Citação: `anexos_iii_v_tabelas.md` — Anexo V).

Alíquota efetiva = (RBT12 × Aliq − PD) / RBT12 = (1.020.000 × 0,2050 − 17.100) / 1.020.000 = (209.100 − 17.100) / 1.020.000 = 192.000 / 1.020.000 = **0,188235 (18,8235%)** (Citação: `lc123_art18_fator_r.md` — §1º-A).

DAS serviços = 78.000,00 × 0,18823529… = **R$ 14.682,35**

**Locação (Anexo III, sem ISS):** mesma RBT12 → Faixa 4 do Anexo III: 16,00% e PD 35.640,00 (Citação: `anexos_iii_v_tabelas.md` — Anexo III).
Alíquota efetiva Anexo III = (1.020.000 × 0,1600 − 35.640) / 1.020.000 = (163.200 − 35.640) / 1.020.000 = 127.560 / 1.020.000 = 0,12505882…
DAS locação bruto = 6.000,00 × 0,12505882… = 750,352941…
Dedução do ISS (parcela de 32,50% da repartição da 4ª faixa do Anexo III — Citação: `anexos_iii_v_tabelas.md`, e `locacao_bens_moveis_iss.md`): 750,352941… × (1 − 0,3250) = 750,352941… × 0,675 = **R$ 506,49**

**DAS total de maio/2026 = 14.682,35 + 506,49 = R$ 15.188,84**

## 5. Repartição (IRPJ/CSLL/COFINS/PIS/CPP/ISS)

A biblioteca traz repartição apenas para o **Anexo III, 4ª faixa**: IRPJ 4,00% · CSLL 3,50% · COFINS 14,05% · PIS 3,05% · CPP 42,75% · ISS 32,50% (Citação: `anexos_iii_v_tabelas.md`).

- **Fatia da locação** (base 750,352941…): IRPJ 30,01 · CSLL 26,26 · COFINS 105,42 · PIS 22,89 · CPP 320,78 · **ISS 0,00** (excluído — locação de bens móveis, SV 31).
- **Fatia dos serviços (R$ 14.682,35): NÃO pode ser alocada** — a repartição do Anexo V **não está na biblioteca**. Não invento parâmetros (regra de trabalho: o que não está na biblioteca é citado como não verificado). Os valores de `reparticao` em `apuracao.json` correspondem **apenas** à fatia da locação.

### Não bate (deixado em aberto)
A repartição da 4ª faixa do Anexo III na biblioteca soma **99,85%**, não 100%. Consequência: a soma das parcelas da locação (505,36) é **R$ 1,13 menor** que o DAS da locação (506,49). Não forcei a equalização; item aberto (a título de referência, fora da biblioteca e não verificado, a tabela de 2016 tem ISS 32,65% na 4ª faixa do Anexo III, o que faria 100% — mas isso **não pode ser citado** aqui).

## 6. Pontos abertos / premissas (resumo)
1. **Pró-labore de abril:** data de pagamento (30/04/2026) **confirmada pelo cliente** nesta rodada; valor incluído na folha_12m (279.900,00). O comprovante de 30/04 foi prometido mas **ainda não chegou ao workspace** — pendência documental, sem efeito no valor do DAS de maio/2026.
2. Repartição do Anexo V ausente da biblioteca e o cliente não possui informação adicional → fatia de serviços (R$ 14.682,35) **não alocada** (desconhecido remanescente, explicitado).
3. Repartição do Anexo III (4ª faixa) soma 99,85% (não 100%) → gap de R$ 1,13 entre a soma das parcelas e o DAS da locação; não equalizado, deixado em aberto.
4. Presumidos pagamentos no período para mai/2025–mar/2026 (sem extratos); faturamento_12_meses.csv tratado como receita bruta total; todas as NFS-e de maio classificadas como serviços de TI.

## Citações (todas em `library/INDEX.md`)
- `lc123_art18_fator_r.md` — LC 123/2006, art. 18, §§1º, 1º-A, 4º, 5º-J, 5º-M; Res. CGSN 140/2018, arts. 25, 26
- `anexos_iii_v_tabelas.md` — LC 123/2006, Anexos III e V (redação LC 155/2016)
- `locacao_bens_moveis_iss.md` — LC 123/2006, art. 18, §5º-A; Súmula Vinculante 31 (STF); Res. CGSN 140, art. 25, §1º, V
