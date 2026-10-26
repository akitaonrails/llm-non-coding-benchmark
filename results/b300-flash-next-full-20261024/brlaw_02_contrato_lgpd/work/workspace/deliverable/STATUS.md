# STATUS

**COMPLETE**

Entregáveis exigidos pelo `CONTRACT.md`, todos em `workspace/deliverable/`:

| Arquivo | Conteúdo |
|---|---|
| `clausulas.json` | 16 avaliações no formato exigido: 8 "alterar" (Cl. 2 e 3 — média; Cl. 5, 7, 8, 10, 12 e 13 — alta), 7 "aceitavel" (Cl. 1, 4, 6, 9, 11, 14 e 15) e 1 "inserir" (nova Cl. 5-A). Toda fundamentação cita apenas arquivos de `library/INDEX.md`. |
| `clausula_dados.md` | Cláusula 5-A completa, pronta para inserir: papéis (controlador/operador), base legal do dado sensível de saúde, instruções do controlador, vedações de uso próprio, subcontratação, transferência internacional, incidentes, direitos dos titulares, auditoria, término/portabilidade e guarda de 20 anos, com tabela de fundamentação por item. |
| `nota_socia.md` | Resposta em linguagem simples, incluindo o ponto perguntado pela sócia: o foro de Florianópolis **não** é anulável pelo CDC neste contrato B2B (fundamentação e o que dá/não dá para fazer). |
| `nota_complementar_foro.md` | Nota extra, a pedido da sócia: por que a tese "foro abusivo pelo CDC, o juiz anula" não se aplica a este contrato e qual a conduta prática recomendada. |
| `STATUS.md` | este arquivo. |

## Decisões centrais (registradas para conferência)

- **Fórum (Cl. 14) — "aceitavel"**, contrariando a premissa da sócia: a clínica contrata software como insumo, não é consumidora (teoria finalista; mitigação exige vulnerabilidade demonstrada — `library/cdc_art51_distrator.md`); entre empresas paritárias vale a eleição de foro (CPC, art. 63; REsp 1.707.855/SP — `library/cc_contratos_empresariais.md`).
- As 7 cláusulas classificadas "aceitavel" estão válidas; onde há apenas oportunidade negocial (SLA da Cl. 6, encargos da Cl. 11 etc.), isso consta do campo `redacao_proposta` como "sugestão apenas negocial", sem classificar a cláusula como abusiva.
- Integração TISS com operadoras para faturamento: lícita (LGPD, art. 11, §4º); já o uso pela NEXA de dados "agregados" para produtos próprios não é (arts. 12 e 39 — `library/lgpd_excertos.md`).

## Premissas e limites (transparência)

- **Premissa:** 3 unidades licenciadas (ficha da cliente) × R$ 6.900 = R$ 20.700/mês; a minuta diz "por unidade" mas não quantifica. Aritmética completa demonstrada na nota (ex.: 36 × 20.700 + 48.000 = 793.200; 30 × 20.700 = 621.000 = 6,75% de 9,2 mi).
- **Não verificado (fora da biblioteca, como exige a regra de trabalho):** exigências da ANS sobre troca de dados TISS; dever específico de designação de DPO (a definição legal está na LGPD, art. 5º, VIII, mas o dever de designação não está reproduzido na biblioteca); práticas de mercado de referência (exclusão de violação de dados do teto, formatos de exportação). Nada disso foi citado como direito; tudo está rotulado como não verificado nos próprios entregáveis.
- `PERGUNTAS.md`/`QUESTIONS.md` não foi criado: **não há pergunta bloqueante** — as peças necessárias (ficha, e-mail, minuta) respondem ao essencial, e a única premissa remanescente está declarada em destaque acima e na nota à sócia.

## Revisão pré-entrega (auditoria interna)

- **Autoridades:** cada citação foi conferida contra o arquivo correspondente de `library/` (todos os 5 lidos na íntegra). Erro encontrado e corrigido em 5 pontos (3 arquivos + `clausulas.json`): a base "tutela da saúde" consta no **art. 11, II, "f"** da LGPD (hipótese sem consentimento), não "art. 11, I, 'f'" — art. 11, I é *consentimento* (essa citação, em 5-A.3(c), está correta e foi mantida). demais citações confirmadas (CC 421/421-A/422/413/473 p.u./478, CPC 63 §§1º/3º, REsp 1.707.855/SP, CDC 2/3/51, REsp 1.203.109/MG e 680.815/PR, CFM 1.821/2007, 2.299/2021, Lei 13.787/2018, LGPD 5º/11/12/33/37-39/42/46-48; Res. CD/ANPD 15/2024 e art. 12 rotuladas como "citada/conforme o arquivo").
- **Fatos da minuta:** todas as descrições de cláusulas reconferidas contra o PDF (preço, vigência/180 dias, SLA 99% com créditos de 2%/ponto até 10%, CSV/30 dias, teto "3 mensalidades", multa 100% das vincendas, NC 5 anos/Brasil/R$ 500 mil, foro de Florianópolis).
- **Aritmética:** 16/16 verificações recalculadas e corretas (20.700; 248.400 = 2,7%; 793.200 ≈ 8,6%; 621.000 = 6,75%; 745.200; 124.200 = 1,35%; 500.000 = 5,4%; 87,66 h/ano; crédito 2.070; ambiguidade 20.700 × 62.100).
- **Consistência:** contagens 8/7/1 confirmadas por script; `JSON` válido com as 5 chaves exigidas; "6 cláusulas" no resumo da nota corrigido para as 8 da tabela (6 críticas + 2 médias); typo e duas frases ambiguas corrigidas (nota complementar do foro; 5-A.11, agora remetendo ao item (ii) da Cl. 10 revisada).
