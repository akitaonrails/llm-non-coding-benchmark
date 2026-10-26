Resposta do cliente confirma a causa raiz. Vou verificar a redação exata da NT sobre a rejeição antes de atualizar as peças:

A regra de rejeição está no comunicado do CGIBS; a NT traz o leiaute. Atualizando as três peças com a causa raiz confirmada:

Engajamento atualizado com a resposta do cliente. Os números da apuração não mudam — as duas rejeitadas nunca se tornaram documentos autorizados e não estão na pasta, então a apuração continua fechada com os 12 documentos recebidos (débitos 4.320/480; créditos 1.458/162; saldo 3.180; recolhimento 0 sob a dispensa condicionada).

## O que a resposta encerra

- **Causa das 2 rejeições confirmada**: *"Grupo IBSCBS não informado para emitente do regime regular (NT 2025.002)"* — exatamente a vedação do comunicado do CGIBS para regime regular a partir de 03/08 (citada como informação da empresa; a regra em si está em `library/cgibs_comunicado_03_08_2026.md`).
- **Cadeia causal fechada**: o rebaixamento da versão do emissor pelo TI removeu a validação do grupo — é a raiz comum das 2 rejeições **e** das notas 2308/2310/2312, que voltaram a ser emitidas sem o grupo depois de 03/08.

## O que atualizei

- `deliverable/orientacao.md` — §2 registra a mensagem de rejeição e o contorno do TI; §3 ação 1 passa a ser **"desfazer o contorno do TI"** (o emissor deve voltar a preencher IBSCBS; corrigir o sistema não sana as notas já emitidas); §6 reescrito: causa confirmada + desdobramentos não apurados.
- `deliverable/PERGUNTAS.md` — item 1 marcado como encerrado na causa; permanece aberto o destino das 2 notas; **novo item 5**: revalidação do emissor antes das emissões de setembro.
- `deliverable/STATUS.md` — refletindo 5 desconhecidos explícitos.

## Desconhecidos sinalizados explicitamente (empresa não tem informação)

1. **Numeração/valor e destino das 2 NF-e rejeitadas** — ponto sensível descoberto agora: a soma das 12 notas (R$ 480.000,00) confere *exatamente* com a base de PIS/COFINS da apuração normal. Se as 2 rejeitadas correspondem a operações realizadas, **essa receita falta nas duas apurações** (normal e-teste). Recomendação: extrair do log de rejeições do TI / consulta à SEFAZ.
2. NF-e 2312 — houve reemissão com o grupo? (pasta só tem a versão irregular)
3. CT-e/NFS-e nacional de serviços — a obrigatoriedade do CGIBS alcança esses documentos; nada na pasta.
4. NF-e 2313 — a empresa pedirá documento corretivo à Distribuidora Norte para recuperar o crédito? (mecanismo de correção fora da biblioteca, não indicado como regra)
5. Emissor substituído por versão com validação IBSCBS antes de setembro.

Status mantido: **COMPLETE WITH OPEN ITEMS**.