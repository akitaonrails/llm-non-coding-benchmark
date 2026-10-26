# Nota à sócia — contrato NexaClin (Clínica Aurora)

**Para:** Dra. Beatriz Lemos **Re:** minuta NexaClin × Clínica Aurora **Prazo:** assinatura desejada em 10 dias

## Resumo em uma frase

Dá para assinar em 10 dias **se** renegociarmos 6 cláusulas antes; a cláusula de foro **não** é "anulável pelo CDC" — a informação que a senhora recebeu não se aplica ao nosso caso.

## 1. Sobre o foro (Florianópolis) — a colega está errada para este contrato

- O Código de Defesa do Consumidor só vale para **relação de consumo**: consumidor é quem usa o serviço como **destinatário final**. Aqui a clínica contrata o software como **insumo da própria atividade** (prontuário e faturamento). Pela teoria finalista do STJ, a clínica **não é consumidora** deste contrato; a exceção (mitigação da finalista) exige vulnerabilidade técnica/jurídica/econômica **comprovada**, o que não se presume numa empresa de R$ 9,2 mi de faturamento assessorada por advogado. **Conclusão: o art. 51 do CDC (que anula cláusulas abusivas, inclusive foro) não se aplica** — `library/cdc_art51_distrator.md`.
- Entre **empresas paritárias**, a cláusula de eleição de foro é **válida** (CPC, art. 63; STJ, REsp 1.707.855/SP), e a nossa atende os requisitos formais — `library/cc_contratos_empresariais.md`.
- **Na prática:** não podemos contar com anulação futura. Ou negociamos o foro agora (domicílio da ré, Curitiba, ou mediação prévia — vale tentar, com expectativa baixa), ou assinamos sabendo que eventual ação corre em Florianópolis. O CDC continua protegendo os **seus pacientes** contra a clínica; isso não afeta o foro deste contrato. *(Desenvolvimento completo da resposta à colega, para circular: `nota_complementar_foro.md`.)*

## 2. O que tem de mudar antes de assinar (em ordem de prioridade)

| # | Cláusula | Problema em linguagem simples | Gravidade |
|---|---|---|---|
| 1 | **5 (Dados)** | Autoriza a NEXA a guardar dados onde quiser (inclusive exterior) e a usar nossos dados de saúde — "anonimizados/agregados" — para criar **produtos dela**. Com ~22 mil pacientes, "agregado" não é anônimo: a lei trata isso como dado pessoal e o operador não pode tratar dados por conta própria (LGPD, arts. 11, 12, 33, 39). | Alta |
| 2 | **7 (Término)** | Devolve nossos dados por **só 30 dias, em CSV**. O prontuário pertence ao paciente e nós somos obrigados a guardá-lo por **20 anos** (CFM 1.821/2007; Lei 13.787/2018). Se perdermos a janela de 30 dias, perdemos o que devemos guardar por 20 anos. | Alta |
| 3 | **12 (Subcontratação)** | A NEXA pode colocar quem quiser para hospedar/processar nossos dados de saúde **sem nos avisar**. Perdemos o controle e a LGPD nos responsabiliza (art. 42). | Alta |
| 4 | **10 (Multa de saída)** | Sair antes do prazo custa **100% das mensalidades que faltam**: no pior caso, 36 × R$ 20.700 = **R$ 745.200**; no 6º mês, 30 × R$ 20.700 = **R$ 621.000 (6,75% do faturamento anual)**. Multa manifestamente excessiva pode ser reduzida pelo juiz (CC, art. 413), mas revisão judicial é excepcional (CC, art. 421-A) — **corrigir no texto, não no processo**. | Alta |
| 5 | **13 (Não concorrência)** | Proíbe a clínica, por **5 anos em todo o Brasil**, de usar software concorrente (multa R$ 500 mil). Para o STJ, não concorrência válida exige limite de tempo/espaço/objeto (±2 anos) e, em licença de software, proibir o **cliente** de usar concorrente é abusivo/sem causa — `library/stj_nao_concorrencia.md`. É provavelmente nula, mas **nulidade se discute em processo**: suprimir agora. | Alta |
| 6 | **8 (Responsabilidade)** | A NEXA responde no máximo por 3 mensalidades (R$ 20.700 ou R$ 62.100, ambíguo) — menos que os R$ 48.000 da implantação. Se houver vazamento de 22 mil prontuários, quem responde perante o paciente é a clínica (art. 42 LGPD), e o "teto" não nos protege perante titulares. Excluir dados/confidencialidade/culpa grave do teto e fixar 12 mensalidades. | Alta |
| 7 | **2 (Reajuste)** | "IGP-M **ou outro índice a critério da NEXA**" = ela escolhe quanto cobrar de aumento. Fixar índice único e substituto oficial (boa-fé — CC, art. 422). | Média |
| 8 | **3 (Renovação)** | Renova sozinha por mais **36 meses** se não denunciarmos com **180 dias** de antecedência; se esquecermos a janela, a multa da Cl. 10 corre sobre o ciclo novo. Pedir renovação de 12 em 12 meses, aviso prévio de 90 dias e **obrigação de a NEXA avisar antes de renovar**. | Média |
| 9 | **Nova cláusula 5-A** | Cláusula completa de proteção de dados (papéis, bases legais, instruções, subcontratação, transferência internacional, incidentes, portabilidade/20 anos, auditoria) — **redação pronta em `clausula_dados.md`**. | Alta |

**Não precisam mudar (são válidas):** Cl. 1, 4, 6 (SLA fraco, mas negociável, não inválido), 9, 11, 14 (foro, ver item 1), 15.

## 3. Dados e operadoras — a notícia boa

A integração com **Unimed e Bradesco para faturamento é lícita**: a LGPD permite o compartilhamento de dados de saúde entre controladores quando se trata das **transações financeiras e administrativas resultantes do uso e da prestação dos serviços**, em benefício dos titulares (art. 11, §4º). O que **não** é lícito é a NEXA usar nossos dados para obter vantagem econômica própria fora disso — exatamente o que a minuta autoriza hoje (Cl. 5). A guarda e o tratamento para prontuário têm base legal própria (art. 11, I, "f" — tutela da saúde por serviços de saúde), sem precisar de consentimento dos pacientes.

## 4. Números do contrato (mostrando a conta)

- Mensalidade com 3 unidades: 3 × R$ 6.900 = **R$ 20.700/mês** → ano: 12 × R$ 20.700 = **R$ 248.400** (2,7% do faturamento anual de R$ 9,2 mi).
- Custo do contrato de 36 meses: R$ 48.000 + 36 × R$ 20.700 = **R$ 793.200** (≈8,6% de um ano de faturamento).
- Multa de saída no pior caso: 36 × R$ 20.700 = **R$ 745.200**; nossa proposta: 30% das vincendas, teto de 6 mensalidades = **R$ 124.200** (1,35% do faturamento anual).
- SLA 99% tolera ~**87,7 h/ano** de sistema fora do ar (0,01 × 8.766 h), com crédito máximo de 10% × R$ 20.700 = **R$ 2.070/mês**. Fraco, mas legal.

## 5. Plano para os 10 dias

1. **D+1/D+2:** enviar contraproposta escrita com as alterações acima + cláusula 5-A pronta (já redigida).
2. **D+3 a D+7:** negociar; vermelho não-negociável: Cl. 5/5-A, 7, 12, 13 e teto de responsabilidade (Cl. 8) — sem isso, não assinar. Flexíveis: foro (14), SLA (6), multa do atraso (11).
3. **D+8 a D+10:** minuta final, conferência de anexos (lista de subcontratados, instruções de tratamento) e assinatura.
4. **Paralelo, pela clínica:** designar formalmente um **encarregado (DPO)** — hoje não temos (a definição legal está na LGPD, art. 5º, VIII; o dever específico de designação não está reproduzido na biblioteca — não verificado aqui) — e revisar a política de privacidade do site. Isso não trava a assinatura, mas reduz nosso próprio risco.

## 6. Premissas e advertências

- Presumi **3 unidades licenciadas** (a R$ 6.900/unidade = R$ 20.700/mês), conforme ficha clínica; se forem 2 unidades, os valores mudam proporcionalmente.
- Tudo acima está ancorado **somente na biblioteca do escritório** (INDEX: LGPD; CC/CPC/Lei de Liberdade Econômica; CDC art. 51; STJ não concorrência; CFM prontuário). Pontos de mercado que a biblioteca não traz — como a prática de excluir violação de dados do teto de responsabilidade ou padrões de exportação técnica — estão marcados como **não verificados**.
- Não há na biblioteca nada sobre regulação ANS/TISS para a integração com operadoras; o enquadramento de faturamento acima se apoia apenas no art. 11, §4º da LGPD. Eventuais exigências da ANS para troca de dados TISS **não foram verificadas** nesta análise.
