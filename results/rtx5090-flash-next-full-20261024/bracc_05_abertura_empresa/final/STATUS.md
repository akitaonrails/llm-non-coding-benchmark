# STATUS — engajamento Clínica Estética Aurora (turno 2 consolidado)

**STATUS: COMPLETE WITH OPEN ITEMS**

Entregáveis em `deliverable/`: `parecer.md` (Rev. 2 — **ANEXO A** consolida a estrutura final), `numeros.json`, `contrato_social_ajustado.md` (v2 — Estrutura A + anexo Variante B), `checklist_registro.md`, `QUESTIONS.md` (registro de respostas), `PERGUNTAS.md` (espelho), `STATUS.md`. Todas as citações apontam para arquivos indexados em `library/INDEX.md`; o que não está na biblioteca está marcado **[NÃO VERIFICADO NA BIBLIOTECA]**; premissas de modelagem, **[PREMISSA]**. O cliente respondeu o questionário e **não dispõe de mais informação** — as lacunas restantes são **decisões/incógnitas sinalizadas**, não perguntas pendentes.

## Conclusões centrais (Estrutura A — parecer, ANEXO A)
- **Imóvel fora do capital:** casal permanece proprietário; **clínica aluga 60% (~R$ 12.000/mês [PREMISSA])** e **casal aluga 40% ao dentista (R$ 8.000/mês, confirmado)**. Sem transmissão → **ITBI sem fato gerador** (JSON: `devido: false`; campo base documenta a Variante B: 420.000 declaratório, quotas cobrem o valor integralizado → **imune** — CF art. 156 §2º I; Tema 796 sem excedente; locação 7,41% < 50% — CTN art. 37).
- **Simples:** `simples_possivel: false` no JSON documenta o **plano como proposto/confirmado** (sociedade locando os 40% = impeditivo LC 123 art. 17 XV — `library/lc123_vedacoes.md`). **Na Estrutura A o Simples (Anexo III) volta a ser possível** — afirmação no parecer A.7, não no booleano.
- **Marina:** **só cotista** (Lei 8.112 art. 117, X — "fora do expediente" **não** é exceção); **nunca** administradora/gestora de fato. Só entra no quadro se resolvido o **CC art. 977** (mutação do regime — caminho crítico — ou terceiro com capital).
- **Felipe:** administrador [PREMISSA], pró-labore R$ 10.000 [PREMISSA] com retenção de 11% (`library/pro_labore_inss.md`).
- **Luana:** **não cotista** (serviços vedados — CC 1.055 §2º; sem dinheiro) → profissional contratada ~R$ 8.000/mês [PREMISSA]; 20% futuros só por **compra de quotas com dinheiro**.
- **Retiradas:** plano 25+25 mil/mês **excede o lucro apurável em todos os cenários** (S1 35k/mês → máx. 17,5k/sócio; S2 23k; S3 5k). Complemento do caixa familiar vem dos **aluguéis PF (20 mil/mês)**. IRRF dividendos 2026: **R$ 0** (teto de 50 mil/mês por sócio respeitado — cliff da Lei 15.270 documentado).

## Open items (decisões sinalizadas — o cliente não tem mais informação; não re-perguntamos)
1. **Regime de bens (CC 977):** o casal não disse se alterará o regime. [PREMISSA] de que persiste → **sem mutação (ou terceiro com capital), não existe quadro registrável conforme a biblioteca** para a sociedade desejada. Decisão patrimonial do casal (A.4; checklist Fase 0.1).
2. **Outras optantes pelo Simples** no nome dos sócios (LC 123 art. 17): condição de elegabilidade **não declarada** — ressalva no contrato (Cláusula 13ª.3).
3. **Base da projeção de R$ 420 mil** (deduz ou não aluguel/pró-labore): tratada por cenários S1–S3 (A.6); números do JSON não forçados a reconciliar.
4. **Habilitação profissional de Luana** para estética: pendência de alvará/contrato (checklist 0.4) [regra: NÃO VERIFICADO NA BIBLIOTECA].
5. **Preço de mercado do aluguel dos 60%** e **tributação/retenções do aluguel na PF**: reprecificar/recolher com contador [NÃO VERIFICADO NA BIBLIOTECA].
6. **Aceite do ajuste de retiradas** e **escopo da não concorrência** (2 anos/município [PREMISSA]) e **município da sede** ([PREMISSA] São Paulo/SP): conduzidos como premissas nos documentos.

## Itens não resolvíveis com a biblioteca (marcados no parecer)
- Comparação quantitativa Simples × Lucro Presumido (tabela do Anexo III e alíquotas do LP ausentes).
- Alíquotas: ganho de capital PF, ITBI municipal, IRPF sobre salário/folha, tributação do aluguel na PF.
- Procedimento de mutação de regime de bens; pluralidade de cotistas na limitada; capital mínimo; tipo societário que admita contribuição de trabalho; habilitação da biomedicina estética; obrigações acessórias da Lei 15.270; preço de transferência entre sócio-PF e PJ; RE 1.495.108 pendente.
