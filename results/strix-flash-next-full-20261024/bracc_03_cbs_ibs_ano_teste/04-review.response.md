Revisão sistemática. Primeiro, extraio todos os campos-fonte dos XMLs e confiro contra os entregáveis, item a item:

A fonte bate com a orientação na tabela de notas. Agora o JSON contra a fonte, e a biblioteca contra as afirmações dos §§4–5:

O JSON fecha 100% com a fonte. Agora a checagem de autoridade — releio a biblioteca contra cada afirmação jurídica:

Checagem completa. Verificação final de integridade dos quatro arquivos:

Revisão concluída. Verifiquei tudo contra a fonte (XMLs, apuração normal, biblioteca) e encontrei **4 problemas**; todos corrigidos.

## O que foi conferido e reconcilia (sem alterações)

- **`apuracao_teste.json` nota a nota vs. XML**: os 12 valores de saída conferem com `<vNF>` (total 480.000,00); CBS/IBS de cada linha = valor × 0,9%/0,1%; créditos conferem com `<vCBS>`/`<vIBSUF>` destacados nas entradas (2314: 558/62; 2316: 360/40; 2317: 540/60); totais e saldos batem (4.320−1.458=2.862; 480−162=318).
- **Reconciliação cruzada**: soma das saídas (480.000,00) = base da apuração normal (PIS 3.120 = 0,65%; COFINS 14.400 = 3,00%) ✓.
- **Datas/cStat/grupos**: 2301–2305 e 2313 antes de 03/08 sem grupo (válidas, CGIBS); 2308/2310/2312 após 03/08 sem grupo; 2309 com alíquotas invertidas (0,90/0,10 vs. 0,10/0,90 — conferido nos tags); todas cStat 100; CRTs confirmados (2315 CRT 1; demais entradas CRT 3).
- **Autoridades**: todas as citações da orientação têm base literal em `lc214_2025_transicao.md`, `cgibs_comunicado_03_08_2026.md`, `nt_nfe_grupo_ibscbs.md` e `lei_pis_cofins_compensacao.md` (inclusive "limitado ao valor efetivamente recolhido" do art. 347 e o "IN RFB a editar").

## Corrigido nesta revisão

1. **orientacao.md §1 — autoridade excedida**: dizia "IBS **sempre** no campo UF — LC 214, art. 343". A biblioteca não diz "sempre": o art. 343 dá só as alíquotas; a NT dá pIBSMun 0,00 **para 2026**. Reescrito com a atribuição correta a cada fonte.
2. **orientacao.md §3 — autoridade excedida**: recomendava "CST 000, cClassTrib 000001" citando a NT da biblioteca, que **não contém esses valores**. Passaram a ser fundamentados no que as próprias notas corretas da empresa (2306/2307/2311) já usam, com o leiaute/alíquotas citados à NT.
3. **PERGUNTAS.md item 3 — detalhe órfão**: perguntava sobre "operações de transporte/instalação **citadas no e-mail**" — o e-mail atual não menciona isso (sobrou de versão anterior do caso). Reescrito: pergunta se a empresa emitiu CT-e/NFS-e nacional em agosto (nada disso na pasta; a obrigatoriedade do comunicado alcança esses documentos).
4. **orientacao.md §3 — fundamento implícito**: a classificação da destinatária de 2308 como "Simples" agora traz a prova documental (mesmo CNPJ da entrada 2315, CRT 1 — 44555666000177).

Varredura final: nenhuma referência obsoleta restante (art. 124, "Comercial Paulista", detalhes de snapshot antigo), JSON válido, 12 saídas + 5 entradas.

**Status: COMPLETE WITH OPEN ITEMS** — números inalterados (saldo-teste 3.180,00; recolhimento 0 sob dispensa condicionada), 5 desconhecidos explícitos em `PERGUNTAS.md`, todos não bloqueantes. Pronto para entrega.