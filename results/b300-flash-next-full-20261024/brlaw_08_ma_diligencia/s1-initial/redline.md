# Redline — minuta do comprador (Grupo Meridiano) · lado vendedor (Vértice)

**Premissas e limites (ler antes):**
- O **preço** de fechamento não consta do arquivo e o cliente não tem essa informação — **desconhecido permanente**; limites expressos em % de preço não são conversíveis em R$ (ver `PERGUNTAS.md`, itens não respondidos).
- **Assunção declarada:** Hélio e Beatriz vendem a totalidade das quotas (e-mail conjunto "Hélio e Beatriz Vértice"); nesse caso a preferência do contrato social se resolve com a assinatura de ambos. Se houver sócio que permanece, a renúncia expressa é condição (redline 3.2(d)).
- O "caso Solaris" é citado no data room mas **não consta da `library/`** — seu conteúdo é **não verificado**; usamos apenas o que o data room afirma (perfis idênticos de subordinação).
- Prazos prescricionais específicos (trabalhista/fiscal), encargos de recálculo trabalhista/tributário e regras de parcelamento **não constam da library**; onde usados, a fórmula "prescrição aplicável + 6 meses" é a que a library oferece como defensável (`library/sandbagging_franquia_mercado.md`) e o parcelamento é sugestão prática **não verificada**.
- Fatos acrescentados pelo cliente nesta rodada: (i) anuência Horizonte Azul **ainda não pedida**; (ii) PJs 9h-18h, exclusivos, com gestor; (iii) débito IRPJ 2023 (~R$ 310 mil) não pago/não parcelado por discordância.
- Toda citação aponta para arquivo indexado em `library/INDEX.md`.

---

## Cláusula 2.3 — Earn-out · **ALTERAR**

**Texto atual (problema):** EBITDA "apurado pelo Comprador segundo suas práticas contábeis, podendo incluir rateio de despesas corporativas do grupo". Aritmética: pagamento = 35% × (EBITDA − R$ 1.100.000), teto R$ 1.500.000. Para pagar o teto é preciso excedente de R$ 1.500.000 ÷ 0,35 = R$ 4.285.714,29, i.e., **EBITDA de R$ 5.385.714,29 — acima do faturamento total da empresa em 2025 (R$ 4,2 mi)**: teto inatingível. Exemplos: EBITDA R$ 1,5 mi → earn-out R$ 140.000; EBITDA R$ 2,0 mi → R$ 315.000. E como o comprador apura e inclui rateios, pode comprimir o número para zerar.

**Redação proposta:**
> 2.3. O Comprador pagará aos Vendedores 35% do valor em que o EBITDA dos 12 meses seguintes ao fechamento exceder R$ 1.100.000,00, limitado a R$ 1.500.000,00. "EBITDA" significa o lucro antes de juros, impostos, depreciação e amortização da Sociedade, apurado conforme **os princípios e práticas contábeis históricos da Sociedade e os CPCs, aplicados de forma consistente**, sendo **vedado incluir**: (i) rateios de despesas, cobranças internas ou management fees do grupo do Comprador; (ii) custos de integração, reestruturação ou da própria transação; (iii) despesas decorrentes de conduta do Comprador fora do curso normal. O Comprador obriga-se a conduzir a Sociedade no curso normal e a **não praticar atos com o efeito de reduzir o EBITDA ou frustrar o earn-out**; fornecerá aos Vendedores o cálculo mensal e a documentação de suporte; controvérsias sobre o cálculo serão resolvidas por **perito contador independente** indicado de comum acordo, com decisão vinculante; em caso de alienação do controle da Sociedade pelo Comprador ou suas afiliadas durante o período, o earn-out será **acelerado** no valor máximo.

**Motivo:** EBITDA "apurado pelo Comprador segundo suas práticas" com "rateio de despesas corporativas" permite zerar o earn-out; as proteções propostas (princípios históricos/CPC, exclusão de rateios e custos de integração, curso normal, acesso a informações, perito independente, aceleração em revenda) são as da prática de M&A (`library/earnout_pratica.md`). Se o comprador mantiver a métrica como está, a cláusula é ilusória e o valor esperado deve migrar para o preço do fechamento.

---

## Cláusula 3.2 e Anexo 3.2 — Condições precedentes · **ALTERAR**

**Texto atual (problema):** anuências listadas em Anexo 3.2 que diz "não aplicável" — mas o data room §1.1 mostra anuência essencial; e exige "Aprovação do CADE" de ato **não notificável**.

**Redação proposta:**
> 3.2. Condições precedentes ao fechamento: (a) **anuência prévia e expressa da Construtora Horizonte Azul S.A.**, nos termos da Cláusula 19 do contrato de prestação de serviços 2024–2028 (anexo 3.2, item 1); (b) **comunicação prévia ao Município de Sorocaba** (Contrato Administrativo nº 044/2025), comprovada a manutenção das condições de habilitação e da regularidade fiscal (anexo 3.2, item 2; Lei 14.133/2021, art. 92, XVI, e art. 137, VI, a contrario — `library/lei14133_alteracao_societaria.md`); (c) **substituição do responsável técnico perante o CREA e a Administração** (anexo 3.2, item 3); (d) **renúncia ou exaurimento do direito de preferência** dos sócios (contrato social, 30 dias); (e) quitação ou regularização do débito federal de R$ 310.000,00 (IRPJ 2023), com emissão de certidão negativa ou positiva com efeitos de negativa.
> Onde a minuta exige "Aprovação do CADE, nos termos da Lei 12.529/2011", **suprimir** e substituir por: "As Partes declaram que este ato de concentração **não é sujeito a notificação obrigatória**, por não atingidos cumulativamente os limiares do art. 88 da Lei nº 12.529/2011 (Grupo Meridiano: R$ 390 mi < R$ 750 mi; Vértice: R$ 4,2 mi < R$ 75 mi)."

**Motivo:** (i) Sem a anuência da Horizonte Azul (31% da receita, ~R$ 1.302.000/ano), a mudança de controle autoriza rescisão imediata com multa de 20% do saldo contratual — condição que protege o próprio negócio comprado; "não aplicável" é inexato. **Plano de abordagem (fatos do cliente):** a venda ainda não foi comunicada à contratante e o jurídico dela é rígido — Hélio deve tratar o assunto pessoalmente com o diretor (relação de confiança) sob NDA, entregando minuta de anuência já redigida, com negociação travada para que o consentimento não reabra preço/prazo; pedir tarde ou vazar a notícia dá ao jurídico deles alavanca sobre o contrato inteiro. (ii) No contrato público não se pede anuência, mas comunicação prévia + habilitação + regularidade fiscal mantidas (Lei 14.133, via library). (iii) CADE: a notificação é obrigatória apenas se **cumulativamente** um grupo ≥ R$ 750 mi e outro ≥ R$ 75 mi — aqui nenhum dos dois (`library/cade_limiares.md` — Lei 12.529/2011, art. 88; Portaria Interministerial 994/2012). Manter a condição cria passagem impossível de satisfazer e mata o plano de 45 dias; risco residual de o CADE requerer análise em até 1 ano (art. 88, §7º, mesma fonte) é gerenciável.

---

## Cláusula 5.7 — Declaração trabalhista · **ALTERAR**

**Texto atual (problema):** "inexistindo risco de reconhecimento de vínculo empregatício" é falsa frente ao data room §2.2–2.3 (11 engenheiros PJs exclusivos, com horário e subordinação; 3 ações com R$ 1,4 mi de causas, provisionadas em R$ 380 mil — gap de R$ 1.020.000).

**Redação proposta:**
> 5.7. Todos os prestadores de serviços da Sociedade estão regularmente contratados, **exceto**: (i) 11 engenheiros contratados como pessoas jurídicas, cujos contratos descrevem continuidade, horário e subordinação, conforme **relação do Anexo [X-1]**; (ii) 3 reclamações trabalhistas em curso (valor de causa total R$ 1.400.000,00; provisão contábil R$ 380.000,00), conforme **Anexo [X-2]**. As matérias dos incisos (i) e (ii) serão reguladas exclusivamente pela indenização específica da Cláusula 8.5, com tetos próprios.

**Motivo:** Na cessão de quotas a empregadora permanece a mesma; o passivo — inclusive o risco de pejotização dos 11 engenheiros — fica na sociedade vendida e é objeto de preço/indenização (`library/clt_10_448_sucessao_trabalhista.md` — CLT arts. 10, 448, 448-A). O pacote "declaração limpa + sandbagging + limite preço + 5 anos" transferiria esse risco conhecido integralmente aos vendedores; a proteção da prática é o anexo de exceções + indenização específica dimensionada (`library/sandbagging_franquia_mercado.md`). A resposta do cliente **agrava** o quadro: os PJs trabalham **9h-18h nas dependências, com exclusividade e gestor** — subordinação e habitualidade completas; "sempre foi assim" é confissão de habitualidade, não defesa. Classificação do risco: **alta probabilidade de reconhecimento de vínculo** (não mero "possível"). Teto da indenização: **fórmula em aberto** — exige a folha/remuneração dos PJs, que o cliente não forneceu (desconhecido permanente); encargos de recálculo não constam da library (não verificado, não calculado).

---

## Cláusula 5.9 — Declaração tributária · **ALTERAR**

**Texto atual (problema):** "situação fiscal regular, com certidões negativas vigentes" é falsa: a CND federal é **positiva** (R$ 310 mil de IRPJ 2023 em cobrança, sem parcelamento — data room §3.1); há ISS "por fora" do Simples com sublimite ultrapassado (§3.2 — qualificação jurídica não verificada na library).

**Redação proposta:**
> 5.9. A Sociedade encontra-se em situação fiscal regular, **exceto**: (i) CND federal positiva, referente a débito de IRPJ 2023 de R$ 310.000,00 em cobrança, sem parcelamento, conforme Anexo [X-3], matéria regulada pela indenização específica da Cláusula 8.5, com teto igual ao débito principal mais encargos legais; (ii) matéria de ISS decorrente do sublimite do Simples Nacional ultrapassado em 2025, conforme Anexo [X-3]. CRF/FGTS e estaduais/municipais regulares.

**Motivo:** Declaração "limpa" sobre fato revelado no data room + sandbagging + limite do preço = risco integral ao vendedor (`library/sandbagging_franquia_mercado.md`). Na cessão de quotas **não há sucessão tributária**: o débito continua sendo da sociedade vendida e por isso deve ser precificado/indenizado, não declarado inexistente; a CND positiva impede certidões e afeta contratos públicos (`library/ctn_133_sucessao.md` — CTN arts. 132-133; `library/lei14133_alteracao_societaria.md` — Lei 14.133, art. 92, XVI). Fato novo do cliente: os sócios **discordam** do débito e por isso não pagaram nem parcelaram — a discordância não suspende a cobrança nem a CND positiva (disciplina de suspensão/garantia não está na library — **não verificado**); os encargos de atualização não são calculáveis sem indexadores na library (**desconhecido permanente** até haver cálculo oficial). Alternativa preferível: quitar/regularizar no fechamento com retenção no preço — o direito de discutir o débito não se confunde com a regularidade exigida pelo contrato público e pela declaração 5.9.

---

## Cláusula 8.4 — Limites

### 8.4(a) Franquia · **ALTERAR**
> "Franquia **dedutível** de R$ 150.000,00: indenizáveis apenas as perdas que excederem esse valor; reclamações individuais abaixo de R$ 25.000,00 não dão causa a indenização."

**Motivo:** a franquia "não dedutível (tipping)" faz o vendedor pagar desde o primeiro real após o gatilho — é proteção de comprador; a posição de vendedor na prática brasileira é franquia **dedutível** (`library/sandbagging_franquia_mercado.md`). O recorte por reclamação (de minimis) é pedido adicional de negociação (prática; sem correspondência específica na library).

### 8.4(b) Limite global · **ALTERAR (manter o teto geral, derrubar o 'Preço Total')**
> "Limite global das indenizações: 15% do Preço de Fechamento. Para as matérias das cláusulas 5.7 e 5.9 (e da indenização específica da Cláusula 8.5) aplicam-se **tetos próprios dimensionados**: (i) débito IRPJ — principal + encargos; (ii) engenheiros PJ — R$ [teto a calcular com a folha informada]; (iii) ações listadas — perda efetiva até R$ [teto]."

**Motivo:** o teto geral de 10–20% do preço é a prática — 15% se mantém; porém exceções com limite = "Preço Total", somadas a declarações limpas sobre matéria revelada e sandbagging, significam devolver até 100% do preço por riscos já conhecidos (`library/sandbagging_franquia_mercado.md`).

### 8.4(c) Sandbagging · **MANTER CONDICIONADO (ou suprimir)**
> Aceitável: "O conhecimento do Comprador não afasta nem reduz o direito à indenização, **ressalvadas as matérias excepcionadas nos Anexos [X-1] a [X-3] e reguladas pela Cláusula 8.5**."
> Alternativa: suprimir a cláusula (conhecimento prévio afasta a indenização).

**Motivo:** pro-sandbagging combinado com declaração 'limpa' sobre matéria revelada no data room e limite do preço transfere ao vendedor risco conhecido e precificável, integral e por 5 anos (`library/sandbagging_franquia_mercado.md`). Só há sentido em aceitar sandbagging se as declarações forem qualificadas pelo anexo de exceções e os riscos conhecidos migrarem para indenizações específicas com tetos próprios.

### 8.4(d) Prazos · **ALTERAR**
> "2 anos (reduzível a acordo) para as declarações em geral; para as matérias fiscal e trabalhista, **a prescrição aplicável acrescida de 6 meses**, contado para cada matéria listada nos Anexos [X-1] a [X-3] da ocorrência do fato gerador/decisão transitada."

**Motivo:** na prática, para fiscal/trabalhista "prescrição + 6 meses é defensável"; 5 anos fixos sem conexão com a prescrição de cada matéria prolongam o risco e o escrow (`library/sandbagging_franquia_mercado.md`). Os prazos prescricionais em si não constam da library — por isso a fórmula, e não o número de anos.

---

## Cláusula 9.1 — Não concorrência · **ALTERAR**

**Texto atual (problema):** 10 anos, território nacional.

**Redação proposta:**
> 9.1. Os Vendedores obrigam-se, por **5 anos** contados do fechamento, a não explorar, diretamente ou como sócios, atividade **concorrente à da Sociedade** (engenharia consultiva nas especialidades hoje por ela prestadas), **nas localidades onde a Sociedade mantenha contratos ativos ou tenha prestado serviços nos últimos 24 meses** anteriores ao fechamento.

**Motivo:** o CC art. 1.147 fixa 5 anos ao alienante de estabelecimento, aplicado por analogia à cessão de controle; "prazos muito superiores a 5 anos e território nacional sem relação com a atuação regional tendem a ser reduzidos (razoabilidade; STJ)" (`library/cc_1147_nao_concorrencia.md`). Vértice é regional (contratos em Sorocaba; R$ 4,2 mi de faturamento) — 10 anos/Brasil é abusivo e judicialmente vulnerável.

---

## Cláusula 10.2 — Conta-garantia (escrow) · **ALTERAR**

**Texto atual (problema):** 20% do preço retidos por 5 anos.

**Redação proposta:**
> 10.2. (i) **Escrow específico** de R$ 310.000,00 + encargos para o débito de IRPJ 2023 — **dispensado** se quitado/regularizado com retenção no preço no fechamento; (ii) escrow específico **dimensionado** para as matérias trabalhistas dos Anexos [X-1]/[X-2], com tetos da Cláusula 8.5; (iii) para as demais declarações, retenção máxima de 10% do preço, liberada em 2 anos, sem prorrogação, salvo reclamação pendente formalizada. Liberações automáticas vinculadas às sobrevidas da Cláusula 8.4(d) e ao trânsito em julgado das ações listadas.

**Motivo:** escrow deve ser **dedicado** e dimensionado por risco (débito de IRPJ; PJs), não um bloqueio uniforme de 20% × 5 anos que imobiliza o caixa dos sócios muito além do necessário (`library/sandbagging_franquia_mercado.md`).
