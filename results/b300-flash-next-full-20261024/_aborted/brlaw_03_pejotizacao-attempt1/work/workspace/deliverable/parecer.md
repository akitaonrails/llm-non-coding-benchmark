# Parecer — Solaris Tecnologia Ltda × Rafael Moreira (R.M. Desenvolvimento de Sistemas Ltda)

**Data:** v2.1, 24/10/2026 (após respostas do cliente; revisão pré-entrega) · **Estado da biblioteca:** congelada em out/2026 (sem acesso externo). Todas as citações **jurídicas** constam de `library/INDEX.md`; itens fora da biblioteca estão marcados como **não verificados**. Exceção declarada: o referencial contábil **CPC 25**, exigido pelo próprio schema do contrato (`classificacao_cpc25`), **não integra a biblioteca** — a redação de seus critérios não foi verificada e ele é usado apenas como classificação imposta pelo contrato (nota no §7). Premissas materialmente relevantes estão em destaque no §6 e §9.

---

## 1. Resumo executivo

| Pergunta da diretoria | Resposta |
|---|---|
| "Tema 725 ⇒ risco zero"? | **Não.** O Tema 725 declara **licitude da terceirização entre pessoas jurídicas**; ele **não afasta o reconhecimento de vínculo quando presentes os requisitos do art. 3º da CLT com fraude (art. 9º)** (`stf_tema_725_adc48_adpf324.md`). Aqui não se discute terceirização lícita: discute-se se um **trabalhador pessoa física, subordinado, é escondido atrás de uma PJ de sócio único** — exatamente o **Tema 1.389**, mérito ainda pendente. |
| Probabilidade de vínculo | **Alta — 85–90%** (elevada após as confissões da gestão na rodada 2, §3). |
| Exposição (período não prescrito, base R$ 18 mil, dispensa) | **≈ R$ 744.956** (com HE provadas de jan–jun/25). Grade de cenários: **R$ 449 mil – R$ 1,04 milhão** (§6.3). |
| Provisão (CPC 25) | **Provável — R$ 744.956**, com nota de intervalo 449–1.041 mil. |
| Acordo | **Recomendado, faixa R$ 450–600 mil** — o piso da grade defensiva (R$ 449.405) coincide com o piso da faixa; alvo ≤ R$ 550 mil. |
| Efeito do Tema 1.389 | Processual: **sobrestamento**; econômico: exposição **permanece**, corrigida por IPCA + (SELIC−IPCA) (Lei 14.905/2024, citada em `stf_tema_1389_pejotizacao.md`). |

## 2. Os requisitos do art. 3º da CLT × provas do arquivo

Art. 3º CLT: empregado é quem presta serviço **pessoal, não eventual, oneroso e subordinado** (`clt_requisitos_vinculo.md`).

| Requisito | Provas (documents/) |
|---|---|
| **Pessoalidade** | Cláusula 4ª do contrato: "a CONTRATADA disponibilizará **seu sócio**" — a obrigação pessoal é de Rafael; R.M. Desenvolvimento é **SLT de sócio único** (cabeçalho do contrato). A PJ não tem outro meio de prestar o serviço. |
| **Não eventualidade (habitualidade)** | Prestação contínua de **01/10/2019 a 30/09/2026** (cláusula 1ª + "prazo indeterminado", cláusula 7ª); **84 notas fiscais consecutivas**, sem solução de continuidade (`notas_fiscais_resumo.csv`: 3+12×6+9 = 84 NFs). Nada de "demanda pontual": atividade permanente de engenharia de software da Solaris. |
| **Onerosidade** | Cláusula 2ª: "R$ 18.000,00 mensais contra nota fiscal, **independentemente de entregas**" — retribuição mensal fixa, sem risco do negócio, traço econômico de salário. 84 × 18.000 = **R$ 1.512.000** pagos (NFs fecham com o contrato: 54.000 + 1.296.000 + 162.000 = 1.512.000). |
| **Subordinação** | (i) Contrato cláusula 5ª: "reportar-se-á ao **Gerente de Engenharia**" — hierarquia escrita; (ii) cláusula 4ª: horário **9h–18h**, seg–sex, **nas dependências da contratante** (ou "em home office **autorizado pelo gestor**" — a autorização também é ato de poder); (iii) Slack 12/03/2024: cobrança de horário ("vi que você logou 9h20... o combinado é 9h. Marca no planilha de ponto"); (iv) Slack 02/06/2025: ordem de prorrogação ("fique até 20h hoje e amanhã, release"); (v) Slack 19/08/2025 + e-mail RH 20/08/2025: ausência sujeita a autorização da gestora e do RH ("descontar do saldo de 20 dias"); (vi) Slack 05/01/2026: **avaliação de desempenho com o mesmo formulário dos CLTs**. Poder diretivo, poder de controle e poder disciplinar-organizacional — manual do empregador. |
| **Extracontratual relevante** | Cláusula 3ª: **exclusividade** absoluta; cláusula 6ª: **"férias" de 20 dias "a combinar"**. A empresa tratava Rafael como CLT nos deveres e no controle, pagando-o como PJ na proteção — "desvirtuamento" do **art. 9º** (`clt_requisitos_vinculo.md`). |

**Art. 442-B não salva:** afasta a qualidade de empregado do autônomo "com ou sem exclusividade, de forma contínua ou não" — mas **desde que ausente a subordinação** (interpretação registrada na própria biblioteca); aqui a subordinação está confessada no contrato, comprovada no Slack e agora **admitida pela própria gestora** (§3). **Art. 818:** a prestação está admitida (contrato + NFs) → ônus da autonomia é da Solaris. **Súmula 212/TST:** discussão sobre modo/data de extinção atrai ônus para a empresa (`tst_sumulas_ojs.md`).

**Súmulas canceladas — não utilizadas:** Súmula 256/TST (cancelada pela Res. 121/2003) e OJ SDI-1 191 (cancelada/convertida). Súmula 363/TST inaplicável (contratante privada). Súmula 331/TST/tema 725 cuidam de **terceirização** com responsabilidade subsidiária — hipótese distinta da **pejotização direta**, em que se postula vínculo direto com a tomadora.

## 3. Rodada 2 — o que as respostas do cliente acrescentam

Respostas recebidas (registradas em chat pelo próprio cliente):

1. **Gerente Carla:** *"Não. Ele era dedicado a nós, 7 anos. A PJ dele só tinha a gente."*
2. **Gerente Carla:** *"Eu. Aprovava férias, cobrava horário, dava feedback. Igual aos CLTs."*
3. **Diretor:** *"Os 18 mil eram 'cheios' justamente porque ele era PJ. Um CLT equivalente ganharia uns 12 mil."*

Leitura jurídica:

- **(1) e (2) são admissões contra a própria empresa, na boca de quem exercia a gestão.** Poder de dirigir (cobrar horário), de controlar (aprovar férias, avaliar "igual aos CLTs") e dependência econômica total (**a PJ só tinha a Solaris como cliente**) — a tese de "autônomo/empresário" do art. 442-B perde o único chão que tinha: sem carteira própria, sem estrutura, sem risco, a PJ é envelope vazio (art. 9º). **Probabilidade de vínculo revista de 80–90% para 85–90%.**
- **(3) é a confissão do mecanismo.** "18 mil cheios **porque** ele era PJ" significa: pagava-se ao trabalhador ~6 mil/mês a mais para que ele **suportasse sozinho os tributos e encargos que seriam do empregador** — prêmio de pejotização, que tem natureza **remuneratória** (paga "por causa do trabalho"), não ressarcimento de custo demonstrado. Consequências:
  - **Para a exposição (INSS), a fala é neutra a favor do fisco:** os encargos que Rafael "arcava" como PJ **não quitavam a contribuição patronal da Solaris**, exigível pela RFB (`verbas_e_calculo.md`, Lei 8.212/91 art. 22) — os R$ 352.170 do cálculo permanecem.
  - **Tese de redução da base (12k):** a biblioteca admite a presunção "base = valor pago à PJ, **salvo prova de que embutia tributos/custos** — argumento de defesa". Aqui **não há prova documental de custos** (PJ sem empregados, sem outros clientes, "cheia"), e tributos do trabalhador não reduzem salário por regra — logo **mantenho 18k como premissa principal** e trato 12k como **cenário defensivo** (§6.3). Se o juízo/área técnica moderar com coeficiente, o meio-termo natural é a régua de 15k (cenário-médio R$ 620.797).
  - **Isonomia (OJ 383 SDI-1): risco encerrado** — ele ganhava ~50% acima do "CLT equivalente" declarado (18k × 12k): sem espaço prático para pedido de diferenças salariais (open item da v1 resolvido).
- **Risco probatório:** os fatos por trás das falas estão nos sistemas da empresa (Slack/e-mail do §2), e a admissão da gestora veio do próprio cliente (chat, acima). Em juízo, "igual aos CLTs" vindo da gestora vale mais que dez contratos. **Recomendação de governança:** instruir gestores a não reproduzir esse discurso; a negociação do acordo deve sair do campo da negação ("risco zero") para a de preço.

## 4. Por que o Tema 725 não resolve

A tese do Tema 725 (RE 958.252, 2018; ADPF 324; ADC 48, 2020 — `stf_tema_725_adc48_adpf324.md`) afirma a **licitude da terceirização** "independentemente do objeto social", mantida a responsabilidade subsidiária. O arquivo registra que a tese **"não afasta o reconhecimento de vínculo quando presentes, no caso concreto, os requisitos do art. 3º da CLT com fraude (art. 9º)"**:

1. O Tema 725 liberou **contratar outra empresa**; não autorizou **empregar pessoa física disfçada de empresa** — questão submetida como **Tema 1.389** (ARE 1.532.603), com repercussão geral reconhecida em abril/2025 exatamente porque a controvérsia segue viva.
2. ADC 48 (transportador autônomo, Lei 11.442) não guarda pertinência com desenvolvedor dedicado em regime de exclusividade.
3. Se o Tema 725 bastasse, não haveria **suspensão nacional** determinada pelo STF — "ele é PJ, assinou contrato, emitiu nota por 7 anos" (e-mail da diretoria) **não é escudo**: vale o art. 9º sobre os fatos, e os fatos, aqui, estão nos sistemas da própria Solaris (e na boca das suas lideranças, §3).

## 5. Prescrição (CF art. 7º, XXIX; CLT art. 11; Súmula 308/TST — `cf_art7_xxix_prescricao.md`)

- **Bienal:** extinção em **30/09/2026** (última NF: set/2026; notificação de 30/09/2026). Prazo até 30/09/2028 → ação de **16/11/2026** tempestiva. *(Data exata do fim é desconhecida — ver §9; se o aviso de 30 dias do contrato foi projetado até ~30/10/2026, +≈ R$ 11,9 mil de verbas.)*
- **Quinquenal do ajuizamento (Súmula 308):** corte em **16/11/2021**. **Prescritos:** out/2019–nov/2021 = **26 meses** de calendário (25,5 efetivos, incl. quinzena 01–15/11/2021; a quinzena 16–30/11/2021 vai ao período exigível). **Exigíveis:** 16/11/2021–30/09/2026 = **58 meses cheios + meia quinzena = 58,5 meses** de cálculo.
- **FGTS:** mesma prescrição quinquenal (Súmula 308; STF ARE 709.212/Tema 608, na fonte da biblioteca).
- **Aviso-prévio:** proporcional ao **tempo total** (Lei 12.506/2011 — "ainda que parte das verbas esteja prescrita"), **3 dias por ano completo**, teto 90. De 01/10/2019 a 30/09/2026 falta 1 dia para 7 anos completos; com a projeção do aviso de 30 dias (U2), o término alcança 01/10/2026 → **7 anos completos → 30 + 3×7 = 51 dias**. Contado rigidamente como 6 anos completos (48 dias), o aviso seria R$ 28.800 — diferença de **−R$ 1.800** no total (adotada a leitura conservadora: 51 dias).
- A prescrição é o único ponto em que o tempo joga a favor da Solaris — e só reduz o passivo **até** o ajuizamento; depois dele, a correção passa a correr contra a empresa.

## 6. Cálculo da exposição (aritmética)

### 6.1 Premissa principal: base = valor pago à PJ (R$ 18.000/mês), 58,5 meses exigíveis, extinção como dispensa
Presunção usual da Justiça do Trabalho (`verbas_e_calculo.md`); a rodada 2 **não trouxe prova de custos embutidos** — trouxe explicação de prêmio (§3). Período: 16/11/2021–30/09/2026.

| Verba | Aritmética | Valor (R$) |
|---|---|---:|
| Remuneração-base do período *(já paga à PJ — base de cálculo, **não soma** ao total)* | 18.000 × 58,5 | 1.053.000 |
| 13º salários | 18.000 ÷ 12 × 58,5 = 1.500 × 58,5 | 87.750 |
| Férias + 1/3 — acervo de 58,5 meses (as "férias" gozadas como PJ não eram remuneradas; **simples**, sem dobra — instrução da biblioteca) | 1.500 × 58,5 × 4/3 | 117.000 |
| FGTS 8% (s/ salários + 13º + férias c/ 1/3 — fórmula da biblioteca) | 8% × 1.257.750 | 100.620 |
| Multa FGTS 40% (Lei 8.036/90 art. 18) | 40% × 100.620 | 40.248 |
| Aviso-prévio 51 dias (Lei 12.506 — fundamentação no §5) | 18.000 ÷ 30 × 51 | 30.600 |
| INSS patronal ≈ 28% (Lei 8.212/91 art. 22) s/ verbas remuneratórias (base+13º+férias c/ 1/3; aviso indenizado excluído — premissa; **teto não aplicado** — ver §6.4) | 28% × 1.257.750 | 352.170 |
| Horas extras **com prova** (jan–jun/25: 18+22+15+26+20+34 = 135 h; adicional 50%; divisor 220 — premissa) | 135 × (18.000/220 = 81,8182) × 1,5 | 16.568 |
| **TOTAL principal** | 87.750+117.000+100.620+40.248+30.600+352.170+16.568 | **744.956** |

### 6.2 Ajustes de premissa já sinalizados
- **Renúncia** (se o encerramento for caracterizado pedido de demissão): caem multa 40% (40.248) e aviso (30.600) → total **674.108**. *(Modalidade não foi informada — §9.)*
- **FGTS sobre aviso indenizado:** fórmula da biblioteca restringe a base (salários+13º+férias) — seguido à risca; se incidente, +≈ 2.448 + 40% ≈ **+3.427** (em aberto).

### 6.3 Grade de sensibilidade (a discussão 18k × 12k é o campo de batalha do cálculo)

| Cenário | Base | Total (R$) |
|---|---|---:|
| 18k × renúncia | 18.000 | 674.108 |
| **18k × dispensa — PRINCIPAL** | 18.000 | **744.956** |
| 18k × dispensa + HE de todo o período no ritmo provado (52,5 m × 22,5 h) | 18.000 | 889.928 |
| 12k ("CLT equivalente" do diretor) × renúncia — **piso defensivo** | 12.000 | 449.405 |
| 12k × dispensa | 12.000 | 496.637 |
| 15k (coeficiente médio) × dispensa | 15.000 | 620.797 |
| **Teto realista**: 18k × dispensa + HE integral + multa 477 (1 salário) + honorários máx. 15% | 18.000 | ≈ 1.041.000 |

(12k: 13º 58.500 = 1.000×58,5; férias 78.000; FGTS 8%×838.500 = 67.080; 40% 26.832; aviso 12.000/30×51 = 20.400; INSS 28%×838.500 = 234.780; HE 135×(12.000/220)×1,5 = 11.045 → 496.637.)

### 6.4 Não reconciliado / a apurar (sem forçar números)
- **HE dos demais 52,5 meses exigíveis** — só existe planilha jan–jun/2025. Sem controles e com >20 empregados, a **presunção da Súmula 338/TST** vale a jornada narrada (9h–20h em picos, Slack 02/06/2025); o ritmo médio de 22,5 h/mês levaria a +≈ R$ 144.972 (teto + multas/honorários ≈ R$ 1,04 mi). Número de empregados: **desconhecido** (§9).
- **Reflexos** de HE sobre 13º/férias/FGTS: pendentes do apuramento das HE.
- **Teto de contribuição previdenciária por empregado:** **não aplicado** — a fórmula da biblioteca ("28% × remuneração reconhecida") não o prevê e as séries de teto não estão na biblioteca. Se aplicado, o efeito é **reduzir** os R$ 352.170 de INSS patronal (magnitude não verificável aqui); o valor adotado é, portanto, conservador para a exposição.
- **Adicional noturno/DSR sobre HE:** institutos **não verificados na biblioteca** — não calculados; prováveis na liquidação.
- **Multas dos arts. 467/477 §8º** (50% s/ incontroversas; 1 salário = 18.000): "discutíveis na reversão de pejotização" (`multa_477_e_honorarios.md`) — contingência.
- **Honorários 5–15%** (art. 791-A): +R$ 37.248 a +R$ 111.743 sobre o total principal (s/ cenário 12k: 24.832–74.496).
- **Correção desde os fatos** (IPCA + SELIC−IPCA, Lei 14.905/2024 na fonte da biblioteca): fórmula conhecida, séries indisponíveis — não acumulada mês a mês.
- **Isonomia (OJ 383):** **resolvido** — 18k > 12k declarado pelo diretor; sem espaço prático de diferenças salariais.

## 7. Provisão (CPC 25)

- **Classificação: PROVÁVEL** — vínculo com probabilidade 85–90%; as provas estão na empresa e as lideranças admitem a gestão "igual aos CLTs"; a tese defensiva (Tema 725) não responde à hipótese.
- **Valor: R$ 744.956** (melhor estimativa sob a presunção da biblioteca). **Nota explicativa obrigatória** com a grade 449–1.041 mil (§6.3) e revisão trimestral enquanto o Tema 1.389 pender. Manter "risco zero / nada a provisionar" contradiz o próprio arquivo (contrato com subordinação escrita + admissões da gestão) e é indefensável em auditoria.
- *Nota de referencial:* **CPC 25 não integra `library/INDEX.md`** — a classificação é prestada porque o schema do próprio contrato a exige (`classificacao_cpc25`). Os critérios usados (*obrigação presente decorrente de evento passado; saída provável de recursos*) têm redação **não verificada** nesta biblioteca e valem apenas como o referencial contábil imposto pelo contrato, não como "citação" jurídica.

## 8. Estratégia (processual e negocial)

1. **Não esperar o Tema 1.389 como mérito.** O sobrestamento (ARE 1.532.603, 14/04/2025) dá tempo, mas custa correção IPCA + (SELIC−IPCA) e a tese futura pode sair **pior** (v.g., ônus da prova da autonomia agravado — art. 818 já opera contra a empresa).
2. **Preservar e auditar a prova antes de qualquer notificação judicial:** Slack/RH/ponto/logs (Súmulas 212 e 338 operam contra quem as retém); levantar nº de empregados (Súmula 338) e controles de jornada de todo o período — a planilha parcial de 2025 é **admissão de controle de jornada**. Instruir gestores (rodada 2 mostrou o preço de falar "igual aos CLTs").
3. **Defesas técnicas reais (não o Tema 725):** (i) prescrição quinquenal — já embutida, único ganho certo; (ii) HE só das 135 h provadas + contestar divisor/jornada; (iii) tese de redução da base para 12k — **argumento** de defesa (§3), sem prova documental de custos, mas ancora o piso do acordo; (iv) se houver renúncia comprovável, excluir aviso + 40%; (v) art. 442-B — frágil, mas deduzível.
4. **Acordo: SIM.** A grade (§6.3) define a mecânica: **piso defensivo 449.405 · médio 620.797 · principal 744.956 · teto ~1,04 mi**. Faixa recomendada **R$ 450–600 mil** — exatamente entre o piso da defesa e o cenário-médio; alvo ≤ 550 mil, teto 600. Fechar **antes do protocolo (16/11/2026)** e, se possível, **recontratar** Rafael: 7 anos de dedicação, custo atual 18k/mês com risco embutido de ~R$ 745 mil a R$ 1,04 mi; um CLT a 12–15k + encargos sai comparável e elimina o passivo. A alternativa "risco zero" é pagar o mesmo ativo humano com 100% de risco.
5. **Remediar o portfólio:** mapear outros PJs com as mesmas cláusulas (exclusividade + horário + reporte). O nº de casos não foi informado (§9) — cada "Rafael" multiplica o problema, e o Tema 1.389 alcançará a todos.

## 9. Desconhecidos explícitos (cliente não tem mais informação)

O cliente respondeu às perguntas da v1 (rodada 2, §3) e **declarou não dispor de informação adicional** para as demais. Os itens abaixo seguem como **premissas sinalizadas**, não como fatos:

| # | Desconhecido | Premissa adotada no cálculo | Impacto se mudar |
|---|---|---|---|
| U1 | **Modalidade da extinção** (dispensa × renúncia × distrato) | **Dispensa** (conservativa; Súmula 212 — ônus da prova do término é da empresa) | renúncia: −70.848 (total → 674.108) |
| U2 | **Data exata do fim** (30/09 × projeção do aviso de 30 dias) | 30/09/2026 (última NF) | +1 mês: ≈ +11.928 |
| U3 | **Nº de empregados da Solaris** (Súmula 338) | Sem presunção (HE só com prova) | com presunção: HE +≈ 144.972, teto ≈ 1,04 mi |
| U4 | **Controles de ponto** além de jan–jun/2025 | Inexistentes | reduz ou amplia o item U3 |
| U5 | **Benefícios pagos a Rafael** (VR/plano/PLR) | Nenhum | compensável no acordo/liquidação |
| U6 | **Outros PJs no mesmo modelo** | Desconhecido | escala do risco (não afeta este cálculo) |
| U7 | Série de **correção monetária** mensal | Não acumulada | passivo cresce com IPCA+ desde cada vencimento |

## 10. Resposta à objeção da diretoria (rodada 3): "o STF decidiu que é lícita; o processo vai ficar parado; por que provisionar?"

Três erros na premissa, cada um com consequência contábil própria:

1. **"O STF decidiu" — não decidiu (ao estado da biblioteca, out/2026).** O que existe é (i) repercussão geral **reconhecida** no Tema 1.389 (ARE 1.532.603, 14/04/2025) e (ii) **suspensão nacional** dos processos. A suspensão é a *prova de que o mérito não foi julgado*: quem já decidiu não precisa suspender o país esperando a própria decisão. A leitura "está em todo jornal" confunde o Tema 1.389 com o **Tema 725/ADPF 324/ADC 48**, que declararam lícita a **terceirização entre empresas** — e cuja própria ficha na biblioteca registra que a tese "**não afasta o reconhecimento de vínculo quando presentes, no caso concreto, os requisitos do art. 3º da CLT com fraude (art. 9º)**". Pejotização de sócio único com subordinação escrita não é o que está decidido; é exatamente o que está pendente.
2. **"Processo parado = sem risco" — a suspensão para o relógio do processo, não do passivo.** A obrigação (CPC 25 — nota de referencial no §7) nasce do **evento passado** — 7 anos de relação com subordinação confessada — não do protocolo da ação. Durante o sobrestamento, a correção continua correndo (IPCA + SELIC−IPCA, Lei 14.905/2024, na fonte da biblioteca) sobre ~R$ 745 mil, e a prova envelhece. E há uma frente que a suspensão trabalhista **não alcança**: a contribuição previdenciária patronal (**R$ 352.170**) é dívida da empresa **exigível pela RFB** (`verbas_e_calculo.md`, Lei 8.212/91 art. 22), cobrada na esfera fiscal/administrativa — que não é o objeto da suspensão do ARE 1.532.603; não espera o Tema 1.389.
3. **"Licitude" futura não resolve este caso concreto.** Ainda que a tese mais favorável ao empregador no Tema 1.389 (v.g., validade formal do contrato-PJ) seja aprovada, restará de pé a perquirição de **fraude no caso concreto** — e este é o pior fact pattern imaginável para a empresa: exclusividade escrita, horário fixo nas dependências, férias autorizadas pela gestora, avaliação "igual aos CLTs", PJ sem outro cliente, e as falas da diretoria nos autos. Se o tema vier **contra** a empresa, a definição vale para todas as ações suspensas de uma vez, já corrigidas.

**Em termos contábeis:** a classificação CPC 25 pergunta por *obrigação presente + saída provável de recursos*, não por *perspectiva de caixa imediato*. Com probabilidade de vínculo de 85–90%, "não provisionar porque está suspenso" é converter um passivo provável em contingência de divulgação e, depois, em despesa maior (principal + correção + honorários de sucumbência) no ano em que o tema sair — com auditoria sem explicação para a mudança. A provisão de **R$ 744.956** com nota de intervalo (§7) é a posição defensável hoje.

**O que a suspensão realmente dá:** tempo — e o melhor uso do tempo é o acordo na faixa **R$ 450–600 mil** (§8.4), pagando perto do piso da grade antes que o mérito do Tema 1.389 e a correção reponham o preço para cima.

Nenhuma fonte **jurídica** fora de `library/INDEX.md` foi citada (exceção declarada: o referencial contábil **CPC 25**, exigido pelo schema do contrato — ver nota no §7); **Súmula 256/TST e OJ SDI-1 191 (canceladas) não foram utilizadas**; institutos fora da biblioteca (divisor 220, DSR, adicional noturno, teto INSS) estão rotulados como premissa/não verificado.
