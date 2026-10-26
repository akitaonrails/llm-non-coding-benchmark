# PERGUNTAS E IGNORADOS DECLARADOS — apuração-teste CBS/IBS agosto/2026

> Atualizado em 25/10/2026, após resposta do cliente. As perguntas feitas em 24/10/2026
> foram respondidas (ou o cliente declarou não ter a informação). Nada será re-perguntado;
> os pontos sem resposta ficam aqui como **ignorados declarados**, com seu efeito.
> Nenhum deles altera os números de teste do `apuracao_teste.json`.

## Resposta recebida do gerente fiscal (registro)

- **P2 respondida:** a rejeição da SEFAZ dizia *"Rejeição: Grupo IBSCBS não informado para
  emitente do regime regular (NT 2025.002)"* — exatamente o bloqueio previsto no Comunicado
  CGIBS de 03/08/2026. O TI da Horizonte **"contornou" voltando a versão do emissor**, o que
  explica as NF-e 2308, 2310 e 2312 emitidas sem o grupo IBSCBS após 03/08 (a 2309 é defeito
  distinto: alíquotas invertidas no cadastro). Causa-raiz confirmada; orientação de reversão
  do rollback e regularização dada em `orientacao.md`, seções 3 e 4.
- **Segunda rodada (25/10/2026) — objeção respondida:** Paulo perguntou se, "como a SEFAZ
  autorizou essas notas depois que o TI voltou a versão do emissor", elas estariam regulares.
  Respondido em `orientacao.md`, seção 3: o protocolo valida o **leiaute transmitido**, não o
  cumprimento da obrigação acessória (destacar o grupo IBSCBS); o rollback apenas ocultou o
  defeito da validação, e nada na biblioteca convalida a omissão pela autorização. As notas
  2308/2310/2312 permanecem tratadas como irregulares na apuração-teste.

## Ignorados declarados (cliente não dispõe da informação)

Cada item é um **desconhecido explícito** — não verificado na biblioteca de referência e
sem fonte no cliente. Se qualquer um se resolver de forma contrária à premissa adotada,
refaça a apuração.

1. **Integralidade dos arquivos.** Os 17 XMLs são ambiente de homologação (tpAmb=2, com
   anotação "Documento fictício" no infCpl). Assunção adotada: representam as operações
   reais de agosto. Se houver notas de agosto fora desta pasta (ou estas não corresponderem
   a operações reais), os totais mudam.
2. **Circulação das notas irregulares.** Não se sabe quais NUMs foram efetivamente
   rejeitados antes do rollback do TI nem se as 2308/2310/2312 **circularam** com os
   clientes. A apuração-teste as considera válidas e irregulares quanto ao destaque
   (débito pelos valores corretos); se alguma não circulou, ela deve ser baixada e os
   totais reduzidos.
3. **Regime dos fornecedores.** Distribuidora Norte e Logística Atlas não estão na
   carteira de clientes. Assunção: regime regular (CRT 3 das notas que emitiram), o que
   garante o crédito de 2314 e 2317 (R$ 1.080,00 CBS + R$ 120,00 IBS). Se alguma for
   Simples/MEI, o crédito correspondente deve ser estornado (arts. 346/347 da LC 214/2025).
4. **Procedimento de correção das notas irregulares em 2026 e extensão da perda da
   dispensa.** A biblioteca não trata de como sanar NF-e de agosto emitidas sem o grupo
   IBSCBS nem se a perda da dispensa do art. 125, §4º do ADCT atingiria só as operações
   irregulares ou o mês inteiro. **Exposição máxima estimada: R$ 3.180,00**
   (CBS 2.862,00 + IBS 318,00). A consulta formal ao Fisco permanece em aberto — e a
   causa-raiz confirmada (rollback deliberado do emissor pelo TI, em vez de adequação à
   NT 2025.002) torna essa consulta ainda mais urgente.
