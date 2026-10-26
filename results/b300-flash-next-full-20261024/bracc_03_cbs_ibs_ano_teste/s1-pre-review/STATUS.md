# STATUS — Apuração de teste CBS/IBS — agosto/2026

**Horizonte Comércio e Serviços Ltda. (CNPJ 27.119.804/0001-30 — emit de todas as NF-e emitidas)**
Situação: **COMPLETE WITH OPEN ITEMS** (concluído com itens em aberto)
Atualizado: 25/10/2026 (resposta do cliente incorporada)

## Entregas
- `apuracao_teste.json` — apuração-teste estruturada: 12 saídas (base R$ 480.000,00 —
  confere com a base PIS/COFINS de agosto) + 5 entradas. CBS: débito 4.320,00 / crédito
  1.458,00 / saldo devedor 2.862,00. IBS: débito 480,00 / crédito 162,00 / saldo 318,00.
  Recolhimento do período de teste = **R$ 0,00** (dispensa do art. 125, §4º do ADCT,
  condicional às obrigações acessórias — não cumpridas nas 4 notas irregulares).
- `orientacao.md` — memorando ao gerente fiscal: situação de agosto, correção do mito
  "nota rejeitada = não tributada", notas sem/invertidas, compras (inclusive a nota da
  Distribuidora Norte que "voltou a entrar"), Simples Nacional, prazos 2026–2032,
  premissas, riscos e o que dizer ao sócio.
- `PERGUNTAS.md` — resposta do cliente registrada (rejeição = "Grupo IBSCBS não informado
  para emitente do regime regular (NT 2025.002)"; TI reverteu a versão do emissor como
  "contorno"), objeção de segunda rodada respondida ("SEFAZ autorizou → está regular?" —
  não: protocolo valida o leiaute transmitido, não o cumprimento da obrigação acessória)
  + 4 ignorados declarados (cliente não dispõe da informação).

## Itens em aberto (não bloqueiam os números de teste)
1. Integralidade dos arquivos entregues (todos tpAmb=2, "documento fictício" — premissa de
   que representam as operações reais de agosto).
2. Se as NF-e 2308/2310/2312 circularam com os clientes (avaliar carta de correção/estorno
   após consulta ao Fisco).
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
