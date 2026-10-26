# STATUS — Apuração de teste CBS/IBS — agosto/2026

**Horizonte Comércio e Serviços Ltda. (CNPJ 27.119.804/0001-30 — emit de todas as NF-e emitidas)**
Situação: **COMPLETE WITH OPEN ITEMS** (concluído com itens em aberto)
Atualizado: 25/10/2026 (resposta do cliente incorporada + revisão pré-entrega: JSON no schema
exato do CONTRACT.md, afirmações sem base na biblioteca rotuladas como premissas, subtotais conferidos)

## Entregas
- `apuracao_teste.json` — apuração-teste estruturada no schema exato do CONTRACT.md (chaves de
  acesso e memória de cálculo dentro de `motivo`/`condicao_dispensa`): 12 saídas (base
  R$ 480.000,00 — confere com a base PIS/COFINS de agosto) + 5 entradas. CBS: débito 4.320,00 /
  crédito 1.458,00 / saldo devedor 2.862,00. IBS: débito 480,00 / crédito 162,00 / saldo 318,00.
  Recolhimento do período de teste = **R$ 0,00** (dispensa do art. 125, §4º do ADCT,
  condicional às obrigações acessórias — não cumpridas nas 4 notas irregulares).
- `orientacao.md` — memorando ao gerente fiscal respondendo ao e-mail dele: mito "em 2026 é só
  informativo, não precisa fazer nada" (1); o que é devido — R$ 0,00 sob dispensa condicional —
  e a exposição de R$ 3.180,00 (2); as 4 notas irregulares, a causa-raiz confirmada (rollback do
  emissor pelo TI) e a resposta à objeção "a SEFAZ autorizou, então está regular?" (3); cliente
  do Simples/MEI também recebe destaque (4); entradas creditáveis — por que Ponto Fixo (2315) e a
  nota 2313 não geram crédito (5); o que muda desde 03/08/2026 (6); premissas assumidas e
  resumo (7).
- `PERGUNTAS.md` — resposta do cliente registrada (rejeição = "Grupo IBSCBS não informado
  para emitente do regime regular (NT 2025.002)"; TI reverteu a versão do emissor como
  "contorno"), objeção de segunda rodada respondida ("SEFAZ autorizou → está regular?" —
  não: nada na biblioteca convalida a omissão pela autorização; a leitura de que o protocolo
  valida só o leiaute transmitido está rotulada como premissa fora da biblioteca —
  `orientacao.md` §3) + 4 ignorados declarados (cliente não dispõe da informação).

## Itens em aberto (não bloqueiam os números de teste)
1. Integralidade dos arquivos entregues (todos tpAmb=2, "documento fictício" — premissa de
   que representam as operações reais de agosto).
2. Se as NF-e 2308/2310/2312 circularam com os clientes (procedimento de saneamento não
   definido na biblioteca — ver item 4; definir após consulta ao Fisco).
3. Regime das fornecedoras Distribuidora Norte e Logística Atlas (inferido como CRT 3).
4. Procedimento de regularização das 4 NF-e irregulares em 2026 e extensão da perda da
   dispensa (só operações irregulares ou mês todo — exposição máxima R$ 3.180,00).
   Não tratado na biblioteca; consulta formal ao Fisco segue pendente — agora com
   urgência maior, pois a causa-raiz é rollback deliberado do emissor pelo TI (ação
   corretiva imediata orientada em `orientacao.md`, seção 3).

## Fontes
Somente os arquivos de `library/` (LC 214/2025 — transição; Comunicado CGIBS 03/08/2026;
NT 2025.002 do IBSCBS na DFe; lei de compensação PIS/COFINS — confere base de agosto) e os
documentos entregues pelo cliente em `documents/`. Sem acesso à internet.
