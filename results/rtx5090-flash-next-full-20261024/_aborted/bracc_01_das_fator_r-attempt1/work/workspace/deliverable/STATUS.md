# STATUS — DAS maio/2026, Lumen Soluções Digitais ME

## COMPLETE WITH OPEN ITEMS

Apuração concluída e entregue (`apuracao.json`, `memoria.md`), com todas as citações restritas aos
3 arquivos de `library/INDEX.md`. Nada foi forçado para fechar; os pontos que não reconciliam estão
listados abaixo e detalhados em `QUESTIONS.md` (Q1–Q8).

### Resultado apurado (com a base como recebida)

| Item | Valor |
|---|---:|
| RBT12 (mai/2025–abr/2026) | 1.020.000,00 |
| Folha 12 meses (por competência, premissa) | 284.600,00 |
| Fator R | 27,9020% (< 28% → **Anexo V**) |
| Anexo / faixa | V / 4ª (nominal 20,50%, PD 17.100,00) |
| Alíquota efetiva serviços | 18,823529% |
| Serviços de maio (82.000 − 4.000 estorno) | 78.000,00 → DAS **14.682,35** |
| Locação bens móveis (segregada, Anexo III sem ISS) | 6.000,00 → DAS **506,49** (8,4415%) |
| **DAS maio/2026** | **15.188,84** |

Contraste com o pedido literal do sócio (20,50% nominal sobre 84.000, sem segregar locação):
17.220,00, ou **2.031,16 a mais**.

### Itens abertos

1. **Folha em regime de caixa (Q1–Q3)** — o resumo é por competência; a biblioteca (Res. CGSN 140,
   art. 26, §2º) conta o que foi **pago** na janela. Faltam **1.000** de folha para o limiar de 28%
   (285.600). Se confirmado folha paga ≥ 285.600: anexo vira **III** e o DAS cai para **10.261,08**
   (−4.927,76). É o único item que pode mudar o anexo; não recomendo pagar o DAS antes da resposta.
2. **Pró-labore mar/2026 (linha zerada) e abr/2026 (Q2)** — e-mail diz pago em 06/05/2026 (fora da
   janela); extrato não mostra pagamento em 06/05, só 2× 1.600,00 em 16/05 rotulados "MAI".
3. **Mecânica da dedução do ISS na locação (Q5b)** — adotado `efetiva × (1 − 0,325)` = 8,4415% → 506,49;
   leitura alternativa `efetiva − 32,50%×nominal` = 7,3059% → 438,35. Diferença de **68,14**, aberta.
4. **Repartição (Q4)** — a biblioteca não traz a tabela do Anexo V, 4ª faixa: `reparticao` de
   IRPJ/CSLL/COFINS/PIS/CPP fica `null` (não apurado, ≠ zero apurado); ISS = 0 porque a única receita
   com componente de ISS seria a de serviços, que sai pelo Anexo V sem tabela disponível. A linha do
   Anexo III, 4ª faixa, soma **99,85%** (descasamento de 1,13 na locação: 505,36 vs 506,49) — deixado
   aberto, não corrigido.
5. **CNAE/descrição fiscal de "consultoria de arquitetura" e "treinamento equipe" (Q5a)** — premissa de
   que entram na lista de TI do §5º-J; irrelevante em maio/2026 (Fator R < 28%), passa a importar se
   o anexo virar III.
6. **Natureza do `faturamento_12_meses.csv` (Q6)** — assumido líquido de estornos e incluindo locação
   histórica; se não incluir, RBT12/faixa mudam.
7. **NF-e 512 (Q7)** — destaca PIS/COFINS com CST 01 e o XML se declara "sem validade fiscal"; nada
   alterado na apuração.
8. **DAS de abril/2026 (Q8)** — 10.480,22 pago (recibo no extrato) é compatível com Anexo III
   (12,18% ≈ 12,1801%), não com Anexo V; contradiz o histórico citado pelo sócio. Fora do escopo de
   maio; não refiz abril (documentos ausentes).

### Próxima rodada

Respondidas Q1–Q3, refazemos o teste do Fator R (limiar: folha paga ≥ 285.600) e atualizamos
`apuracao.json`/`memoria.md`; respondida Q4, preenchemos `reparticao`.
