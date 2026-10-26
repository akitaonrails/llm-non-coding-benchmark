# STATUS — Engajamento: apuração-teste CBS/IBS agosto/2026

**Status: COMPLETE WITH OPEN ITEMS**

## Atualização de out/2026 — resposta do cliente incorporada

> *"A rejeição dizia: 'Rejeição: Grupo IBSCBS não informado para emitente do regime regular (NT 2025.002)'. O TI 'contornou' voltando a versão do emissor."*

- **Causa raiz das autorizações irregulares (cStat 100 em 2308/2310/2312) confirmada:** após 2 rejeições corretas da SEFAZ, o TI fez **rollback da versão do emissor** para voltar a emitir — daí as notas saírem autorizadas sem o grupo. Incorporado nos motivos de `apuracao_teste.json` e em `orientacao.md` §4/§8 (reverter rollback; parametrizar por upgrade; NF 2309 = defeito à parte).
- **Números da apuração inalterados** (a resposta explica a causa, não altera valores): base 480.000,00; débito CBS 4.320,00 / IBS 480,00; crédito CBS 1.458,00 / IBS 162,00; saldo CBS 2.862,00 + IBS 318,00 = **3.180,00**; **recolhimento devido hoje 0,00** condicionado à dispensa (ADCT art. 125, §4º); irregulares somam 234.300,00 (CBS 2.108,70 / IBS 234,30).
- **Q3 fechada.** Demais perguntas (Q1-parcial, Q2, Q4, Q5): cliente **sem informação adicional** — não repetidas; ficam como desconhecidos D1–D6 abaixo.
- **Pergunta adicional do Paulo (out/2026):** *"A SEFAZ autorizou; autorizada não é regular?"* — **respondida em `orientacao.md` §4 (bloco dedicado): não.** A regra pós-03/08 proíbe a emissão sem grupo (norma > cStat); a própria NF 2309 prova que documento autorizado pode estar errado (destaque invertido); o comunicado separa "sem penalidade" de "sem risco à dispensa" (ADCT 125 §4º pede cumprimento, não autorização). **Não altera números nem o status do engajamento.**

## Entregáveis

| Arquivo | Estado |
|---|---|
| `apuracao_teste.json` | ✅ Concluído — schema do CONTRACT; JSON válido; somas conferidas em Python; motivos de 2308/2309/2310/2312 atualizados com a causa confirmada |
| `orientacao.md` | ✅ Concluído e atualizado — seção 4 reescrita com causa raiz confirmada (rollback do TI) e direção de reversão urgente; §8 e §9 atualizados; desconhecidos explícitos |
| `QUESTIONS.md` | ✅ Atualizado — resposta registrada; perguntas respondidas não repetidas; desconhecidos D1–D6 tabelados com tratamento |
| `PERGUNTAS.md` | ✅ Cópia idêntica de `QUESTIONS.md` (CONTRACT lista `PERGUNTAS.md` opcional; usuário pediu `QUESTIONS.md`) |

## Open items — desconhecidos explícitos (cliente sem informação adicional)

1. **D1** — Quais documentos foram as 2 notas rejeitadas e se foram reemitidos dentro/fora da série 2301–2312. Premissa adotada (e registrada): população = documentos fornecidos; base 480.000,00 reconcilia com PIS/COFINS. Doc. adicional reabriria a apuração.
2. **D2** — NFS-e/serviços ou outros documentos de agosto além dos 17 fornecidos — mesma premissa da D1.
3. **D3** — Tratamento das 4 notas irregulares (cancelar/reemitir ou outro caminho): decisão interna da empresa; mecanismo não constante na biblioteca **[não verificado]**.
4. **D4** — Se BRISA/SERRA VERDE já usaram os créditos de 2312 e 2309 (impacto: 1.584,00 + 176,00 sem crédito; destaque trocado) — comunicação aos clientes pendente.
5. **D5** — Decisão sobre o crédito perdido de 480,00 na NF 2313 — registrado como custo do mês.
6. **D6** — Versão/data do rollback do emissor e situações subsequentes (setembro/…) — o risco permanece até a reversão; recomendação de NF-e de teste pós-correção já registrada.

## Notas de conformidade

- Somente fontes da `library/INDEX.md` são citadas (`lc214_2025_transicao.md`, `cgibs_comunicado_03_08_2026.md`, `nt_nfe_grupo_ibscbs.md`, `lei_pis_cofins_compensacao.md`); todo o restante rotulado **[não verificado]**.
- A causa raiz do rollback é **informação do cliente** (fato declarado), distinguida da base normativa (NT 2025.002/CGIBS).
- tpAmb=2 e a infAdic "fictitious benchmark" nos XMLs: ruído de teste, não achado de compliance.
- Nada foi forçado a bater: 480.000,00 reconcilia naturalmente com a apuração normal de PIS/COFINS.
