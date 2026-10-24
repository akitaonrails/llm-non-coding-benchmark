# Unknowns restantes — DAS maio/2026

**Rodada 2.** O cliente respondeu (22/10/2026) e informou **não ter mais informação** para as
demais perguntas. Este arquivo **não reapresenta perguntas já respondidas**: registra, de forma
explícita, o que **continua não verificado** e o documento que fecharia cada ponto.

**Respondidas e aplicadas (não repetidas aqui):**
- pró-labore de abril/2026 → **pago em 30/04/2026** (dentro da janela mai/25–abr/26); o "em aberto"
  do resumo veio do lançamento tardio do PIX. Cenário de folha 281.400,00 **eliminado**.
- NFS-e 1188 → **glosa de escopo com devolução via PIX**, sem nota substitutiva (confirmada pelo
  débito de 29/05/2026 no extrato). Receita de serviços **78.000,00**; cenário +752,94 **eliminado**.

**Resultado mantido: DAS maio/2026 = R$ 15.188,84.**

---

## U1 — Folha **paga** na janela mai/25–abr/26 (único item que pode mudar o resultado)

O resumo é por **competência**; a regra usa o valor **pago** nos 12 meses anteriores
(`library/lc123_art18_fator_r.md`, Res. CGSN 140, art. 26, §2º). Com o esclarecimento do pró-labore
de abril, as duas leituras convergem para **284.600,00** → fator R **27,90%** → **Anexo V**.
**Mas a linha 2026-03 do resumo traz `pro_labore = 0`**, e a observação do cliente se refere a
**abril** — a lacuna de **março/2026 segue sem explicação**.

- Efeito se houver prestação de março/2026 (3.200,00) paga na janela: folha **287.800,00** →
  fator R **28,22%** → serviços ao **Anexo III** → DAS **10.261,08** (**−4.927,76**).
- **Limiar objetivo: folha paga ≥ 285.600,00** (margem atual de apenas **R$ 1.000,00**).
- Também permanecem não verificados 13º, férias/terço e FGTS de competências anteriores pagos na
  janela (o resumo não os traz e o cliente não tem a relação de pagamentos).
- **Fecha com:** extratos de mar/2026 e abr/2026, ou folha de pagamento/DIRF do período, ou o
  comprovante de 30/04/2026 (que **não chegou** a `documents/` — hoje é alegação).

## U2 — Composição do RBT12 (1.020.000,00)

Não confirmado se o `faturamento_12_meses.csv` é **bruto**, se está **líquido de cancelamentos** de
competências anteriores e se **inclui** a receita de locação; nem se houve outra receita (venda de
licenças, comércio, trabalho avulso) nos 12 meses. *Efeito: muda faixa e alíquota efetiva
(ex.: RBT12 ≤ 720.000,00 → 3ª faixa, nominal 19,50% / PD 9.900,00 no Anexo V).*
- **Fecha com:** o extrato do PGDAS-D (receita bruta acumulada mês a mês por atividade).

## U3 — Classificação de "consultoria de arquitetura" (1183) e "treinamento equipe" (1186)

Assumidas como **mesmo bloco de serviços de TI** (premissa P2). As **listas de atividades dos
anexos não estão na biblioteca** → classificação **NÃO VERIFICÁVEL NA BIBLIOTECA**.
*Efeito quantificado: se o treinamento (4.500,00) fosse do Anexo III, o DAS cairia **284,29**.*
- **Fecha com:** CNAEs do cadastro/PGDAS-D e o código de serviço usado nas NFS-e; as listas de
  anexos precisam entrar na biblioteca do trabalho para que a conclusão seja verificável.

## U4 — Anexo efetivamente usado em períodos anteriores (anomalia do DAS de abril/2026)

DAS **abr/2026 = 10.480,22** pago em 20/05/2026 = **12,05%** da receita de abril (87.000,00):
**incompatível com o Anexo V** (16.376,45) e **compatível com o Anexo III** (10.880,13; com locação
segregada 10.636,27). Isso sugere **folha ≥ 28% nas janelas antigas** — o que torna a folha
informada de 284.600,00 suspeita de subestimação (ver U1) — ou apurações anteriores em anexo
equivocado, caso em que há **retificação** a avaliar.
- Não refeita aqui: faltam as receitas de **abr/2025–mar/2026** para o RBT12 daquela apuração.
- **Fecha com:** declaracoes/PGDAS-D de jan–abr/2026 e a folha das janelas correspondentes.

## U5 — Repartição por tributo dos **serviços** (Anexo V)

A biblioteca só contém a repartição do **Anexo III, 4ª faixa** → aplicada **só à locação**.
A repartição dos 14.682,35 de serviços está **NÃO APURADA** (percentuais inventados seriam fato não
suportado).
- **Fecha com:** a tabela de repartição do **Anexo V** vigente anexada à biblioteca do trabalho.

## U6 — Tabela de repartição da biblioteca não soma 100%

Anexo III, 4ª faixa: 4,00 + 3,50 + 14,05 + 3,05 + 42,75 + 32,50 = **99,85%**. Na locação, a soma dos
componentes (**505,36**) não fecha com o DAS da locação (**506,49**) — diferença de **1,13**
(= 0,15% de 750,35). **Não foi criado ajuste** para forçar o fechamento.
- **Fecha com:** a tabela oficial integral (a versão da biblioteca está truncada ou com erro).

## U7 — NF-e 512 destaca PIS 39,00 e COFINS 180,00

Destaque em regime não cumulativo, incompatível com optante do Simples (PIS/COFINS vêm no DAS).
A vedação aplicável **não está na biblioteca** → **NÃO VERIFICADO NA BIBLIOTECA**; sem efeito sobre
o valor do DAS.
- **Fecha com:** a NFS-e/NF-e emitida ao cliente e a norma pertinente na biblioteca.

## U8 — Situação cadastral da locação de bens móveis

Não verificado se a locação consta do **CNAE/objeto** e foi informada no **PGDAS-D** como atividade
própria (condição prática para a segregação do Anexo III sem ISS) e se há **retenção de ISS na fonte**
em alguma NFS-e (a lista de serviços do município está ausente: `documents/_faltando_servicos_municipio.md`).
- **Fecha com:** ficha cadastral/PGDAS-D e a lista de serviços do município.

---

### Como isso afeta a entrega
Nenhum dos unknowns acima altera o valor **apurado e entregue** (15.188,84), que está ancorado nos
documentos do pacote. **U1 é o único com efeito material conhecido** (−4.927,76). Se o cliente
fornecer qualquer documento listado em "Fecha com", refazemos a apuração e republicamos
`apuracao.json`/`memoria.md`.
