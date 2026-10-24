# Memória de cálculo — DAS de maio/2026
**Lumen Soluções Digitais ME** — competência maio/2026
Bibliotecas citadas (ver `library/INDEX.md`):
- [LC18] `lc123_art18_fator_r.md` — LC 123/2006, art. 18, §§1º, 1º-A, 5º-J, 5º-K, 5º-M; Res. CGSN 140/2018, arts. 25, 26
- [TABELAS] `anexos_iii_v_tabelas.md` — LC 123/2006, Anexos III e V (redação LC 155/2016)
- [LOCACAO] `locacao_bens_moveis_iss.md` — LC 123/2006, art. 18, §5º-A; Súmula Vinculante 31; Res. CGSN 140, art. 25, §1º, V

Fontes do cliente: `documents/notas_emitidas_maio.md`, `documents/extrato_maio_2026.csv` (e `.pdf`, conferido — mesmo conteúdo), `documents/faturamento_12_meses.csv`, `documents/resumo_folha_12_meses.csv`, `documents/email_socio.txt`, `documents/nfe_000512_locacao.xml` (conferido — valor/data/operação coerentes com o §6).

## 1. RBT12 — receita bruta dos 12 meses anteriores (LC 123/2006, art. 18, §1º [LC18])
Janela: 05/2025 a 04/2026 (`faturamento_12_meses.csv`):
78.000 + 81.500 + 84.000 + 86.000 + 79.500 + 90.000 + 88.000 + 92.000 + 85.000 + 83.000 + 86.000 + 87.000 = **R$ 1.020.000,00**

## 2. Folha de salários dos 12 meses — critério de pagamento
Res. CGSN 140, art. 26, §§1º-2º [LC18]: considera-se o montante **pago** nos 12 meses anteriores, independentemente do mês de competência.

`resumo_folha_12_meses.csv` (competência, somatório 284.600):
23.400 + 23.400 + 23.800 + 23.800 + 23.800 + 24.100 + 24.100 + 24.100 + 24.300 + 24.300 + 20.900 + 24.600 = 284.600

Ajustes para base de **pagamento** na janela 05/2025–04/2026:
- **(3.200)** pró-labore de competência 04/2026: pago em maio/2026 (e-mail do sócio: "paguei atrasado, dia 6 de maio"; extrato: 05/16 PIX Renato 1.600 + Julia 1.600). Fora da janela → excluído.
- **(4.700)** encargos patronais/FGTS de competência 04/2026: extrato 05/07 "DARF/GPS/FGTS ABR −4.700", pago em maio/2026 → fora da janela → excluído.

folha_12m = 284.600 − 3.200 − 4.700 = **R$ 276.700,00**

> **Suposição:** presumiu-se que as demais linhas do resumo foram pagas no mês da competência (o resumo não traz outra informação e o extrato só cobre maio/2026).
> **Sensibilidade:** se os encargos de abril fossem tratados como pagos em abril, folha_12m = 281.400 e Fator R = 27,59%. Nos dois casos Fator R < 28% → **mesmo Anexo V**; o resultado é insensível a esse ponto.
> **Discrepância não material:** o sócio diz que pagou o pró-labore em 06/05; o extrato mostra os PIX em 16/05. Ambos em maio/2026 → mesma conclusão (exclusão da janela).

## 3. Fator R e escolha do Anexo (art. 18, §§5º-J/5º-M [LC18])
Fator R = folha_12m ÷ RBT12 = 276.700 ÷ 1.020.000 = **27,13%** (< 28%)
→ Serviços de TI tributados pelo **Anexo V**. (Confere com a instrução do sócio de "repetir o Anexo V", mas o anexo foi determinado pelo cálculo, não apenas pela instrução.)

## 4. Faixa e alíquotas (TABELAS)
RBT12 = 1.020.000 → 4ª faixa (RBT12 até 1.800.000) nos dois anexos.
- **Anexo V, 4ª faixa (serviços):** alíquota nominal 20,50%, parcela a deduzir 17.100.
- **Anexo III, 4ª faixa (locação, §5º-A [LOCACAO]):** alíquota nominal 16,00%, parcela a deduzir 35.640.

## 5. Alíquota efetiva (art. 18, §1º-A [LC18]: (RBT12 × Aliq − PD) / RBT12)
- Serviços (Anexo V): (1.020.000 × 0,205 − 17.100) ÷ 1.020.000 = (209.100 − 17.100) ÷ 1.020.000 = 192.000 ÷ 1.020.000 = **18,8235%**
- Locação (Anexo III): (1.020.000 × 0,160 − 35.640) ÷ 1.020.000 = (163.200 − 35.640) ÷ 1.020.000 = 127.560 ÷ 1.020.000 = **12,5059%**

## 6. Receitas de maio/2026 e classificação de cada nota
| Documento | Classificação | Tratamento | Valor |
|---|---|---|---:|
| NFS-e 1181 | serviço (dev. software) | Anexo V | 18.000,00 |
| NFS-e 1182 | serviço (sustentação) | Anexo V | 12.500,00 |
| NFS-e 1183 | serviço (consultoria) | Anexo V | 9.800,00 |
| NFS-e 1184 | serviço (dev. módulo fiscal) | Anexo V | 22.000,00 |
| NFS-e 1185 | serviço (suporte) | Anexo V | 6.700,00 |
| NFS-e 1186 | serviço (treinamento) | Anexo V | 4.500,00 |
| NFS-e 1187 | serviço (dev. integração) | Anexo V | 8.500,00 |
| NFS-e 1188 | estorno parcial de 1184 | **reduz a receita de maio** (estorno/cancelamento [LC18]) | (4.000,00) |
| NF-e 000.512 | locação de bens móveis (notebooks) | **Anexo III, sem ISS** (§5º-A; SV 31 [LOCACAO]) — o sócio achou que "vai junto com os serviços", mas a segregação por atividade (§4º [LC18]) a afasta dos serviços | 6.000,00 |

- Serviços (líquidos) = 82.000 − 4.000 = **78.000,00**
- Locação = **6.000,00** · Total de maio = **84.000,00**

Estorno pago ao cliente (débito) confirmado no extrato (05/29 "PIX ENVIADO ESTORNO GLOSA — CLIENTE 1184, −4.000").

## 7. DAS de maio/2026
Segregação de receitas (§4º [LC18]): cada atividade aplica o anexo e a alíquota correspondentes.
- DAS serviços = 78.000 × 18,8235% = **14.682,35**
- DAS locação = 6.000 × 12,5059% × (1 − 32,50%) = 6.000 × 8,4415% = **506,49**
  (parcela do ISS deduzida [LOCACAO]; **inferência, sem número na biblioteca**: [LOCACAO] manda deduzir "a parcela correspondente ao ISS" sem fixar fração — usei 32,50%, único valor de ISS disponível na biblioteca: a fatia de ISS da repartição da 4ª faixa [TABELAS])
- **DAS total = 14.682,35 + 506,49 = 15.188,84**

> Leitura alternativa rejeitada: se a locação fosse tributada pela alíquota efetiva do Anexo V (sem a segregação do §5º-A), o total seria 15.444,71. A leitura literal da biblioteca ("tributadas na forma do Anexo III, deduzida a parcela correspondente ao ISS") sustenta o valor acima.

## 8. Repartição do DAS (TABELAS — única repartição presente na biblioteca: Anexo III, 4ª faixa)
Base = DAS total 15.188,84:
- IRPJ 4,00% = 607,55 · CSLL 3,50% = 531,61 · COFINS 14,05% = 2.134,03 · PIS 3,05% = 463,26 · CPP 42,75% = 6.493,23
- **ISS = 32,50% apenas sobre o DAS de serviços** (14.682,35 × 32,50% = 4.771,76); a fatia de ISS da locação (506,49 × 32,50% = 164,61) é a parcela deduzida pelo §5º-A [LOCACAO] e não é devida.
- Soma da repartição = **15.001,45**

**Não fecha com o DAS total (15.188,84); diferença = 187,39**, composta de:
1. 164,61 — fatia de ISS que a repartição "carregaria" se incidisse sobre a locação (506,49 × 32,50%); foi corretamente excluída (§5º-A [LOCACAO]) — a própria locação já foi cobrada sem ISS (DAS bruto Anexo III: 6.000 × 12,5059% = 750,35; líquido: 506,49; dedução de 243,86);
2. 22,78 — a tabela de repartição da biblioteca soma 99,85%, não 100% (ISS 32,50%).

**Deixamos aberto, sem forçar ajuste**, conforme as regras de trabalho: a única repartição disponível na biblioteca é a do Anexo III e sua tabela não fecha 100%; a repartição do Anexo V (que seria a adequada ao DAS de serviços) não consta da biblioteca — qualquer preenchimento dela seria não verificado e não foi usado.

## 9. Conferência com o extrato (maio/2026)
Créditos 88.000,00 · Débitos 43.180,22 · Saldo final 86.100,33 — o PDF do extrato confere linha a linha com o CSV (mesmos valores; apenas o formato da data difere).
Reconciliação com o §6: créditos 88.000,00 = 82.000,00 (serviços brutos) + 6.000,00 (locação, TED 05/26 "LOCACAO NOTEBOOKS"); o estorno de 4.000,00 sai como débito (05/29) → **receita líquida de maio = 84.000,00**, conforme §6.
Todos os recebimentos de serviços/notas de maio constam; o DAS de abril (10.480,22, pago em 05/20) e os pagamentos de folha/encargos de maio não entram na apuração de maio (competência; a folha só entra via Fator R, pelos 12 meses anteriores).

NF-e 000.512 (XML conferido): operação "Locação de bens móveis" (notebooks, 20 un., maio/2026), emitida em 26/05/2026, valor 6.000,00, CRT 1 — coerente com a classificação do §6.
