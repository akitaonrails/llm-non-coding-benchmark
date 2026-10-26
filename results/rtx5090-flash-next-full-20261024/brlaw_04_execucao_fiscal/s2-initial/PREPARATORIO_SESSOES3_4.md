# PREPARATÓRIO — SESSÕES 3–4 (REDIRECIONAMENTO)
**Não é entregável.** Análise de preparação baseada exclusivamente em documentos **já juntados** (contrato social e alterações; certidão do Oficial de Justiça) e na biblioteca. Será convertida nos entregáveis `sessao3a4/analise_redirecionamento.json`, `defesa_redirecionamento.md` e `carta_aos_socios.md` quando o contrato scriptar o pedido de redirecionamento à ex-sócia (o pedido ainda **não está nos autos** — nada será redigido contra petição inexistente).

## Linha do tempo documentada (cálculos conferidos)
| Data | Fato | Fonte |
|---|---|---|
| 2012 | Constituição: Ana Paula Vieira (60%, **administradora**) + Carlos Vieira (40%) | contrato social |
| 3T/2020–2T/2021 | Fatos geradores (IRPJ/CSLL) | CDA |
| **15/06/2023** | **Ana Paula retira-se** (cede 60% a Bruno Tavares); **Bruno = administrador único** | 3ª alteração |
| 22/06/2023 | Retirada registrada na **JUCESP** | 3ª alteração |
| 03/02/2026 | Auto de infração (2a 7m 17d **depois** do registro da retirada — 957 dias) | CDA/PAF |
| 12/03/2026 | Mudança de sede registrada na **JUCESP** (Rua das Pedras, 100 → Av. Industrial, 2.500, Cotia) | 4ª alteração |
| 20/03/2026 | CNPJ atualizado na **RFB** | 4ª alteração |
| 28/09/2026 | Certidão **negativa** do oficial: empresa não localizada na sede antiga; ocupante diz que ali é "outro estabelecimento desde o começo do ano" | certidão OJ |

## Enquadramento pela biblioteca (`redirecionamento_sumulas_temas.md`)
1. **Súmula 435 — presunção de dissolução irregular exige dois elementos**: deixar de funcionar no domicílio fiscal **+ "sem comunicação aos órgãos competentes"**. Aqui a comunicação houve — JUCESP 12/03/2026 e RFB 20/03/2026, **192–200 dias antes** da diligência (28/09/2026). A própria biblioteca registra: *"a presunção da Súmula 435 é afastada pela comunicação da mudança de endereço aos órgãos competentes (Junta Comercial/RFB) anterior à diligência"*. → **Presunção afastada; dissolução irregular NÃO configurada.**
2. **Tema 962 (REsp 1.377.019)** — mesmo que configurada a dissolução, o redirecionamento **não pode ser autorizado contra quem, embora exercesse poderes de gerência ao tempo do fato gerador, dela regularmente se retirou e não deu causa à sua posterior dissolução irregular**. Correção do idioma: a tese é: Ana Paula exercia gerência nos FGs (2020–2021), mas **retirou-se regularmente em 15/06/2023 (JUCESP 22/06/2023)**, ~2,5 anos antes da AIF e ~3 anos antes da saída da sede (início de 2026), sem dar causa a ela. → **Redirecionamento à ex-sócia é vedado pelo Tema 962 em qualquer cenário.**
3. **Tema 981 (REsp 1.645.333)** — responde pelo redirecionamento quem tinha poderes de administração **na data em que configurada/presumida a dissolução irregular**. Se (arguendo tantum) a dissolução se configurasse em 2026, o único gestor seria **Bruno Tavares** — nunca Ana Paula.
4. **Súmula 430** — inadimplemento da sociedade não gera, por si só, responsabilidade do sócio-gerente; e **CTN 135, III** exige ato com excesso de poderes/infração à lei — não alegado nos autos (U2: nenhuma fraude descrita no AIF; multa é 44 I, 75%).

## Fato desfavorável a antecipar (honestidade analítica)
A certidão OJ diz que o local já era "outro estabelecimento desde o começo do ano" — a **saída fática** (jan/2026) precedeu a comunicação (mar/2026) em ~70 dias. A Fazenda pode argumentar atraso. Resposta pela biblioteca: o texto da Súmula 435 condiciona a presunção à **ausência de comunicação aos órgãos competentes**, e a nota library é expressa: a comunicação **anterior à diligência** afasta a presunção — o que ocorreu (192–200 dias antes). A comunicação existiu e precede a diligência; a presunção legal não se forma.

## Rascunho do gabarito JSON futuro (a confirmar com o pedido real)
- `socio_pedido`: aguardar petição (contrato scripta: ex-sócia Ana Paula).
- `requisitos_435`: não preenchidos — comunicação JUCESP/RFB anterior à diligência.
- `tema_962`: favorece a ex-sócia (retirada regular registrada, sem causa da dissolução).
- `tema_981`: gestor à época da alegada dissolução (2026) era Bruno, não Ana Paula.
- `dissolucao_irregular_configurada`: **não**.
- `socio_que_responderia_se_configurada`: Bruno Tavares (Tema 981), jamais a ex-sócia (Tema 962).
- `conclusao`: improcedência do pedido contra a ex-sócia.

## Pendências que afetam S3–4
- **U6**: CDA substitutiva ausente dos autos — se alterar o sujeito passivo, Súmula 392/STJ barra.
- Petição da Fazenda ainda não scriptada; teses dela (ex.: alegação de fraude/abuso da personalidade) serão enfrentadas quando existirem.
