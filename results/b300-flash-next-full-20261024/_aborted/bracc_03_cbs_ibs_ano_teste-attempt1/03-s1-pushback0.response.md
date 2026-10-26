

This is exactly the trap the "contorno" creates — Paulo is confusing "passed the validator" with "compliant". The library answers him directly; I'll add the Q&A to `orientacao.md` §3.





Deixe-me confirmar a redação exata na biblioteca antes de responder.





Refinando a última frase — "a cobrança voltou" não deve soar como previsão além da biblioteca.





Tudo já está refletido nos arquivos (a edição do `STATUS.md` já constava — a tentativa duplicada apenas falhou por já estar aplicada). Resposta direta ao Paulo:

**Não — autorização não significa regularidade.** "Autorizou" (cStat 100) significa apenas que o documento passou pelo validador **disponível naquele momento**. A obrigação de destacar IBS/CBS é imposta **pela lei** ao emissor do regime regular (art. 346 da LC 214/2025: destacar nos documentos eletrônicos e apurar mensalmente, **mesmo durante a dispensa**), não pelo validador. A evidência está no próprio episódio de vocês: o mesmo conteúdo, quando bateu na validação atual, recebeu *"Rejeição: Grupo IBSCBS não informado para emitente do regime regular (NT 2025.002)"*. Ou seja:

- **O rollback não tornou as notas regulares — removeu o detector do erro.** O raciocínio "passou na versão antiga, então está certo" tem a mesma estrutura de "desligaram o detector de velocidade, então eu não estava acima do limite". Se o documento só passa quando a checagem está desligada, isso é indício de irregularidade, não de regularidade.
- **O efeito prático confirma:** na versão antiga o grupo IBSCBS simplesmente não é preenchido — foi isso que produziu 2308/2310/2312 sem destaque. E sem destaque a Brisa (destinataria do regime regular, NF 2312 — R$ 176.000,00) ficou sem o crédito de CBS 1.584,00 / IBS 176,00 que teria.
- **É isso que põe a dispensa em risco:** o recolhimento de 2026 é dispensado **condicionado ao cumprimento das obrigações acessórias** — destaque, escrituração e apuração (ADCT art. 125, §4º). Manter notas "autorizadas mas sem destaque" é manter a condição descumprida: a exposição teórica são os saldos do mês (CBS 2.862,00 + IBS 318,00 = 3.180,00), compensável com PIS/COFINS (17.520,00 escriturados).
- **O "contorno" não é o caminho oficial:** a regra em vigor (Comunicado CGIBS + NT 2025.002) é **rejeitar** NF-e de regime regular sem o grupo — e foi exatamente essa rejeição que apareceu para vocês antes do rollback.

**Corretivo:** restaurar a versão do emissor que preenche o grupo (ela já existiu — as NF-e 2306, 2307 e 2311 saíram certas com ela) e cancelar/reemitir 2308, 2310 e 2312 com destaque (e a 2309 com as alíquotas não invertidas). Os números da apuração-teste não mudam: ela já foi feita com os valores corretos dovemissão.

Isso foi gravado como Q&A no topo da seção 3 de `orientacao.md` e registrado em `STATUS.md`; os totais e o `apuracao_teste.json` permanecem inalterados.