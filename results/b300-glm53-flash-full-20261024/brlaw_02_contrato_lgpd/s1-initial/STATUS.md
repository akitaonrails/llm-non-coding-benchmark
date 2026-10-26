# STATUS.md

**STATUS: COMPLETE WITH OPEN ITEMS**

## Entregáveis

| Arquivo | Situação |
|---|---|
| `deliverable/clausulas.json` | ✔ completo — 15 cláusulas avaliadas (9 "alterar", 6 "aceitavel"); fundamentos atualizados com as respostas da cliente (cl. 2 índice IGP-M como base; cl. 5/12 AWS "provavelmente" EUA → art. 33; cl. 7 transição ≥ 180 dias; cl. 10 efeito de captura; cl. 14 foro genérico "domicílio da CONTRATANTE") |
| `deliverable/clausula_dados.md` | ✔ completo — cláusula substitutiva íntegra; §5º reescrito (declaração escrita de região/serviços + prova de salvaguardas art. 33 + vedação de réplica em região não autorizada + Brasil exclusivo como alternativa) e §9º atualizado (b: 180 dias de leitura; novo e: ensaio anual de portabilidade) |
| `deliverable/nota_socia.md` | ✔ completo — linguagem simples; nova seção 8 com o impacto das respostas (AWS/EUA e migração de meses), §3 item 4 recalibrado, §6 com pendência da confirmação AWS e designação de encarregado |
| `deliverable/QUESTIONS.md` | ✔ fechado — registro das respostas recebidas + pendências explícitas com premissas de trabalho; **não há novas perguntas à cliente** |
| `deliverable/STATUS.md` | este arquivo |

## Resumo das conclusões

- Foro (cláusula 14): **válido** — CDC/teoria finalista (STJ) afastam o art. 51; CPC art. 63 + CC art. 421-A; troca de foro é pedido comercial opcional (redação genérica "domicílio da CONTRATANTE").
- Alterar (gravidade alta): cláusulas 5 (dados — substituição integral), 7 (exportação 30 dias vs guarda de 20 anos), 8 (teto R$ 62.100 incl. violação de dados), 10 (multa 100% das vincendas = R$ 745.200), 12 (subcontratação sem aviso), 13 (não concorrência 5 anos/R$ 500.000 — suprimir).
- Alterar (gravidade média): cláusulas 2 (índice a critério da NEXA), 3 (renovação 36m/aviso 180d), 6 (SLA 99% = 7,2 h/mês; crédito teto R$ 2.070).
- Aceitável: cláusulas 1, 4, 9, 11, 14, 15.
- **Respostas da cliente incorporadas:** (i) hospedagem indicada como AWS "provavelmente" nos EUA — tratada como **transferência internacional (art. 33)** até a confirmação escrita da Nexa; (ii) migração dos ~22 mil prontuários como projeto de meses — saída no meio caótica → transição de saída mínima de **180 dias** + ensaio anual de exportação + alerta de captura (multas 10+13 = R$ 1.245.200 = 1,57× o custo da primeira vigência).

## Itens abertos

1. **Confirmação por escrito da Nexa** sobre hospedagem (região/país — que a cliente ouviu ser AWS "provavelmente" nos EUA, **não confirmado**) e serviços envolvidos, com prova do mecanismo de salvaguardas do art. 33 **antes do início do fluxo**. Qual mecanismo vigente se aplica à transferência para os EUA **não consta do excerto da biblioteca** (`library/lgpd_excertos.md`) — verificação externa; a prova fica a cargo da Nexa. A redação da cláusula de dados §5º já impõe isso.
2. **Decisão comercial em aberto (opcional):** exigir hospedagem e acesso exclusivamente no Brasil, se disponível sem custo adicional — a redação do §5º funciona nos dois cenários.
3. **Informações não fornecidas pela cliente, com premissa de trabalho adotada:** cidade-sede (redação genérica de foro "domicílio da CONTRATANTE"); índice de reajuste (IGP-M da minuta mantido como base, vedada escolha unilateral); janela de manutenção (default 1×/mês, ≤ 4 h, horário de menor uso); encarregado de dados (nome/contato a inserir **antes da assinatura** — Aurora não designou ninguém). Registro completo em `deliverable/QUESTIONS.md`.
4. **Verificação externa à biblioteca:** art. 41 (obrigatoriedade do encarregado) e art. 18 (direitos dos titulares) da LGPD **não verificados** — `library/lgpd_excertos.md` não os traz; confirmar antes da assinatura.

## Aritmética exposta (fonte: cálculo Python nesta sessão)

Mensalidade total 3×6.900 = R$ 20.700/mês; anual = R$ 248.400; 36m = R$ 745.200; implantação+36m = R$ 793.200; multa cláusula 10/implantação = 15,525×; multa/faturamento anual = 8,1%; teto cláusula 8 = R$ 62.100; crédito SLA teto = R$ 2.070/mês = R$ 24.840/ano; downtime 99% = 7,2 h/mês ≈ 87,6 h/ano; multa cláusula 13/custo anual do contrato = 2,01×; multa cláusula 13/faturamento anual = 5,43%; soma das multas 10+13 = R$ 1.245.200 = 1,57× o custo total da primeira vigência (R$ 793.200).

> Contrato de 36 meses com renovações pela minuta multaria também no ciclo renovado — o cálculo foi feito para a primeira vigência, cenário de pior caso razoável; reajustes pelo IGP-M não foram projetados (falta índice histórico na biblioteca; nada forçado a equilibrar).
