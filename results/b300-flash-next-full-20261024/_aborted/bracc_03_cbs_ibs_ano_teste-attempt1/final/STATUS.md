# STATUS — apuração-teste CBS/IBS agosto/2026 — Horizonte Comércio e Serviços Ltda.

**COMPLETE WITH OPEN ITEMS** (respostas do cliente em 24/10 absorvidas; números inalterados)

## Entregues (em `workspace/deliverable/`)

- `apuracao_teste.json` — schema do contrato; 12 saídas + 5 entradas conferidas documento a documento
  contra `documents/saidas/` e `documents/entradas/`; totais: débitos CBS 4.320,00 / IBS 480,00;
  créditos CBS 1.458,00 / IBS 162,00; saldos 2.862,00 / 318,00; `recolhimento_devido = 0,00` sob a
  condição do ADCT art. 125, §4º (descrita em `condicao_dispensa`).
- `orientacao.md` — resposta ao e-mail do gerente fiscal; já incorpora as respostas do cliente:
  a rejeição ("Grupo IBSCBS não informado para emitente do regime regular — NT 2025.002") confirma a
  regra de rejeição do Comunicado CGIBS; o "contorno" do TI (retorno de versão do emissor) explica a
  retomada das emissões sem grupo **após** as rejeições (2312, 27/08), mas não as de 2308/2310 (10 e
  18/08), anteriores às rejeições — o emissor já alternava acertos e falhas. Em qualquer caso, a
  conduta é desfazer o rollback e cancelar/reemitir as irregulares. Inclui a resposta ao follow-up ("SEFAZ autorizou, então está
  regular?") — não: autorização não convalida a ausência de destaque exigida do regime regular
  (art. 346), e a dispensa segue condicionada às acessórias (ADCT art. 125, §4º). Regime Simples do
  Ponto Fixo confirmado; 2315 segue sem crédito.
- `QUESTIONS.md` / `PERGUNTAS.md` — desconhecidos sinalizados (conteúdo equivalente).

## Itens em aberto (desconhecidos sinalizados — o cliente não dispõe de mais informação)

1. **Números/chaves das duas tentativas rejeitadas**: inexistentes em `documents/`. Sem efeito nos
   totais — rejeição não gera documento fiscal; as 12 saídas autorizadas fecham com a base
   escriturada da apuração normal (480.000,00 de base, à qual correspondem PIS 3.120,00 e COFINS
   14.400,00). **Contingência:**
   documento *autorizado* não enviado ⇒ apuração a refazer.
2. **Premissa — regime regular da LOGISTICA ATLAS S.A.** (NF-e 2316): base `CRT=3` no XML + destaque
   de CBS/IBS. Se cair, crédito de 360,00/40,00 sai (saldos 3.222,00 / 358,00).
3. **Premissa — completude** das 12 saídas + 5 entradas como tudo de agosto/2026: sustentada pela
   conciliação com o livro, não confirmada documentalmente.

## Notas de método

- Fontes citadas: apenas arquivos de `library/` (`INDEX.md`): LC 214/2025 (arts. 343, 346, 347) e
  ADCT art. 125; Comunicado CGIBS jul/2026; NT NF-e 2025.002; regra de compensação PIS/COFINS.
- Valores de `CST`/`cClassTrib` por operação e procedimentos de cancelamento/reemissão de NF-e são
  orientação operacional — **não verificados na biblioteca** e sinalizados como tais na orientação.
- Aritmética conferida item a item; saída total (480.000,00) amarra com a base de PIS/COFINS da
  apuração normal (vPIS 3.120,00 e vCOFINS 14.400,00 destacados nas próprias notas) — sem
  divergência de base. As duas rejeições relatadas pelo cliente não alteram esse fechamento.
