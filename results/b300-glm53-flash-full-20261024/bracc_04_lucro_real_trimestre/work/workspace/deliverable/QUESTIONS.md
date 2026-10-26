# QUESTIONS.md — Atlas Distribuidora S.A. (rodada 3)

Perguntas já respondidas **não são repetidas**: natureza dos brindes e justificativa do crédito da NF 8812
(rodada 1); detalhamento dos brindes — entregue na NF 4410 (R$ 48.000,00, fev/2026) e documentos de
fev/2026 (rodada 2). Efeitos em `deliverable/mes_01/pendencias.md` §5 e `deliverable/mes_02/pendencias.md`.

## Pedido de documentos (necessário para desbloquear a sessão 3)
1. Enviar os documentos do fechamento de **março/2026**, no padrão dos meses anteriores: balancete de
   mar/2026, razão de mar/2026 e documentos específicos do mês (notas, contratos, recibos ou
   detalhamentos que existam). Sem esse pacote, a apuração IRPJ/CSLL do 1º trimestre e o e-LALUR
   (`deliverable/mes_03/lalur.json` + `memoria.md`) não podem ser produzidos — sessão 3 **BLOCKED**.
2. Confirmar se o balancete de mar/2026 virá no mesmo formato **cumulativo** observado em fev/2026
   (jan+fev+mar) — importa para reconstruir a DRE do trimestre e conferir o saldo de 1.1.04.

## Pergunta de processo (surgiu na conferência do balancete de fev)
3. **Postagem do ajuste contábil nos livros:** o balancete de fev/2026 prova que o lançamento
   A-2026-01-01 (estorno do crédito NF 8812: Dr 3.1.02 / Cr 1.1.04 11.100,00) **não foi postado** —
   1.1.04 ainda traz os 155.067,00 + 11.100,00 + 157.509,00 = 323.676,00. Repetimos a mesma partida em
   `deliverable/mes_02/ajustes.json` (A-2026-02-01). Confirmar que o cliente **postará o ajuste nos
   próprios livros (uma única vez)** — após a postagem, o saldo esperado de 1.1.04 é 312.576,00
   (+ movimentos de março, se houver).

## Incógnitas já registradas na rodada 2 e sem resposta do cliente (não re-pedidas; permanecem abertas)
- **Data de transmissão da EFD-Contribuições original de 01/2026** — sem ela e sem índices de acréscimos
  na biblioteca, os acréscimos do complemento de R$ 11.100,00 seguem **incalculáveis**
  (`library/pis_cofins_uso_consumo.md` exige apenas que sejam devidos; nada forçado a fechar).
- **Parcelamento do prejuízo fiscal de R$ 900.000,00 (parcelas pós-1995?)** — suposição assumida e
  destacada: todas as parcelas apuradas a partir de 1º/01/1995 → trava de 30% (Lei 9.065/95, art. 15/16;
  STF Tema 117 — `library/lei9065_art15_trava.md`). Se houver parcelas anteriores a 1995, elas não se
  submetem à trava.
- **Quitação do complemento PIS/COFINS (11.100,00 + acréscimos)** — responsável e data não confirmados;
  tratamos como obrigação da Atlas a quitar.
