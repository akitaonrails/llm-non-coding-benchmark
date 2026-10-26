Boa — revisão final antes da entrega. Vou reler todos os entregáveis e o texto exato do quarto arquivo da biblioteca, e reamarrar cada número nos razão/balancete.

O pendente de janeiro confirma a 4.2.02 de janeiro = R$ 85.000,00 — isso corrobora o erro de tabela que encontrei na memória. Vou ler os arquivos-alvo para correção e a memória completa.

Todos os arquivos alvo identificados. Vou ler o arquivo da biblioteca para IRPJ/CSLL e o memorando, e executar novamente a verificação contábil mensal da razão para verificar cada linha da tabela.

O memorando e a biblioteca revelam mais do que as correções planejas — vou fazer uma varredura por palavras cruzadas em todo o entregável quanto a citações não autorizadas e números inconsistentes, e reconfirmar a reconciliação da razão em Python.

O ambiente de código é JavaScript — vou executar em Python através do shell:

Citações da biblioteca verificadas como literais. Vou ler os arquivos JSON restantes e o QUESTIONS.md para concluir a auditoria:

Falta verificar a cauda dos dois arquivos JSON de mes_01 (interrompidos na leitura anterior):

Auditoria completa. Vou ler as seções exatas a corrigir em `memoria.md`, `pendencias.md` e `memorando` para aplicar as edições:

Correções 1–5 e 8 aplicadas. Agora o memorando (correções 6–7):

Todas as 9 correções aplicadas. Re-validação final — JSONs, aritmética da tabela e varredura de resíduos:

Revisão pré-entrega concluída. Reconciliação completa re-rodada em Python (os três razão equilibrados; razão acumulado == balancete de março conta a conta, zero divergências; todo o LALUR re-verificado), as 4 citações conferidas palavra a palavra contra `library/`, e os 11 entregáveis lidos inteiro. **9 correções aplicadas** — nenhum número fiscal mudou:

**Erros de conciliação (1)**
1. `mes_03/memoria.md` §1 — tabela do lucro líquido: linha de **Janeiro** trazia despesas comerciais **163.000** (valor de fevereiro). O razão de janeiro (4.2.02) é **85.000**; corrigido, a linha passa a fechar em 128.483 e a coluna Q1 fica 85+163+85 = 333.000, igual ao balancete de março. Revalidado por Python: Jan 128.483 / Fev 193.083 / Mar 282.583, Q1 604.149.

**Autoridade não suportada pelo acervo fechado (4)**
2. `memoria.md` §7: citação do adicional alterada de "Lei 9.430/96, **art. 2º**" para a citação exata do arquivo da biblioteca ("arts. 1º-2º") — a biblioteca não atribui o adicional a um artigo específico.
3. `memorando_diretor_trava.md` §1: removidos "recurso repetitivo" e "pacificado" (caracterizações que a biblioteca não faz — ela apenas registra "O STF (RE 591.340, Tema 117) declarou a trava constitucional"); título e corpo realinhados a esse texto.
4. `memorando_diretor_trava.md` §3/§4: removidas as afirmações "e não prescreve" e "transportar ... **indefinidamente**" — a biblioteca não fixa termo de expiração; agora diz "para os trimestres subsequentes (o acervo não fixa termo final)".
5. `mes_03/pendencias.md` item 5: "saldo não prescreve" → "a biblioteca não fixa termo de prescrição/validade do saldo (nada afirmado além disso)".

**Typos e clareza (4)**
6. `mes_03/pendencias.md` item 4: "42.975.**387" (ponto) → "42.975**,387" (vírgula — conflitava com a notação de milhar).
7. `mes_03/pis_cofins.json`: "conere" → "confere".
8. `mes_03/lalur.json`: "diferenga" → "diferenca".
9. `mes_03/pendencias.md` item 5: "Pedido diretório" → "Pedido do diretor"; e nota de rodapé ** da tabela do `memoria.md` reescrita: o estorno é lançado **uma única vez** (AJ-2026-03-001 — os AJs de jan/fev nunca foram espelhados) e a tabela alocou seu efeito na linha de janeiro (mês de origem), por isso Fev/Mar mostram "—".

**Checado e sem alteração:** todos os 7 JSON validados (`json.load` OK); `mes_01/`, `mes_02/`, `STATUS.md` e `QUESTIONS.md` auditados limpos; as citações de brindes/doação (Lei 9.249/95 art. 13 VI/VII + §2º II), trava (Lei 9.065/95 arts. 15–16 + RE 591.340) e uso-e-consumo (Lei 10.637/2.002, 10.833/2.003, IN 2.121, REsp 1.221.170) conferem literalmente com a biblioteca. Valores finais intactos: IRPJ 71.625,65 + adicional 41.750,43 + CSLL 42.975,39 = **156.351,47**; Parte B **695.355,30** em cada saldo.