Vou revisar tudo contra a biblioteca e os números: primeiro uma varredura sistemática de citações e valores, depois as correções.

Retomando a revisão: a varredura de citações e a matemática passaram. Agora preciso das localizações exatas das citações sobre encarregado/DPO e dos demais pontos a corrigir.

Localizações confirmadas. Vou ler o STATUS.md para atualizar as descrições e depois aplicar todas as correções.

Correções principais aplicadas. Atualizando as descrições do STATUS.md:

Agora a validação final: JSON, presença das correções e varredura de possíveis citações fora da biblioteca:

Revisão concluída. Varri as cinco entregáveis em busca de (i) citações que não existem na biblioteca fechada, (ii) afirmações mais fortes do que a fonte permite e (iii) números divergentes. A matemática conferiu inteiramente (mensalidade R$ 20.700 → contrato R$ 793.200; multa no mês 12 = 24 × 20.700 = R$ 496.800; teto de 3 mensalidades = R$ 62.100 ≈ R$ 2,82/paciente; R$ 500 mil ≈ 24,15 mensalidades = 2,01× o valor anual; SLA 1% = 7,2 h; crédito R$ 414/ponto; teto 10% = R$ 2.070) e toda autoridade citada foi confirmada nos arquivos de `library/`. **Cinco correções** foram necessárias:

1. **Citação de autoridade sem suporte (DPO)** — `nota_socia.md` (item 6) e `PERGUNTAS.md` (item 5): eu atribuía a obrigação de nomear um encarregado (DPO) a "LGPD, art. 5º, VIII". Esse artigo apenas *define* o encarregado; a norma que *impõe* a nomeação (art. 41) **não existe na biblioteca de referência**. Ambas as passagens agora afirmam explicitamente que a regra que a torna obrigatória não está coberta pela biblioteca — mantendo a recomendação como boa prática e apontando que a designação é criada por obrigação contratual em si (item 5.13 da cláusula de dados). Nenhuma referência solta ao art. 41 foi introduzida.

2. **Overclaim sobre CPC art. 63, §3º** — `clausulas.json` (cláusula 14): "destina-se a contratos de adesão com parte vulnerável" foi suavizado para "tem como caso típico o contrato de adesão com parte vulnerável — o que não é o nosso", porque a biblioteca diz "típica", não exclusiva. A conclusão (foro válido) permanece.

3. **Overclaim de legalidade** — `clausulas.json` (cláusula 6, SLA): "Não há ilegalidade" → "Nenhuma ilegalidade identificável à luz da biblioteca" (afirmação epistemicamente honesta em uma biblioteca fechada).

4. **Plano de ação desatualizado** — `nota_socia.md` (passo 2 do plano de 10 dias): ainda pedia à NEXA "onde os dados já estão hospedados hoje", que o cliente já respondeu (AWS "provavelmente" EUA). Substituído pela exigência real: região exata da AWS + mecanismo do art. 33 documentado, ou plano de migração para o Brasil em ≤90 dias.

5. **Descrições do STATUS.md** — a linha de entregáveis descrevia incorretamente o `PERGUNTAS.md` (agora um registro de "lacunas remanescentes", não um conjunto de perguntas abertas) e omitia o item 8 da nota (objeção do colega sobre o foro) e o item 7 (atualização da resposta do cliente). Atualizado, marcando a rodada de revisão.

O que foi verificado e **não** precisou de mudança: as 15 avaliações (8 alterar / 7 aceitável) são defensáveis sob a biblioteca; a escolha do foro da cláusula 14 permanece "aceitável" — reconfirmei os arts. 2º/3º/51 do CDC, art. 63 do CPC e o precedente REsp 1.707.855/SP todos nos arquivos INDEX; as afirmações de não concorrência da cláusula 13 correspondem aos dois Recursos Especiais listados; as afirmações sobre prontuário (guarda por 20 anos, Resoluções CFM 1.821/2007 e 2.299/2021, Lei 13.787/2018) correspondem a `cfm_prontuario.md`; as regras de incidente de 24h→3 dias úteis correspondem à Res. CD/ANPD 15/2024 citada em `lgpd_excertos.md`; o item 5.13 em si é uma obrigação criada por contrato, não uma afirmação legal, então está correto. O JSON foi revalidado após as edições (15 entradas válidas).

`STATUS.md` permanece **COMPLETE WITH OPEN ITEMS** — os itens em aberto continuam sendo demandas documentais contra a NEXA embutidas na contraproposta, não pendências de análise. Tudo pronto para entrega.