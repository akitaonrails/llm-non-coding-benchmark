Good discipline. Let me do a systematic pass: re-read the full parecer, verify every authority against the library, and recompute all arithmetic from scratch.

Agora vou conferir item a item os números e as datas citadas, começando pelas provas documentais (prints, notas fiscais, escala e o contrato extraído).

Verificação completa. Surpresa boa: a regra do aviso-prévio por **tempo total de serviço mesmo com prescrição** está de fato na biblioteca (`cf_art7_xxix_prescricao.md`) — a linha 51 está certa. Mas a recálculagem confirmou os erros: o cenário renúncia correto é **657.540 / ≈819.080** (os arquivos trazem 657.165/818.705, defasados), a diferença é **70.848** (não ~70.850), honorários a 15% ≈ **133.500** (não 133.400), e a data da mensagem de ponto é **12/03/2024** (a tabela §1 diz 02/03/2024). Também: referências cruzadas erradas "(§4)" para o Tema 1.389 (é §3), o bullet de prescrição do §8.2 inverte a lógica (atrasar o ajuizamento reduz a base — como o próprio §4 diz), e a Súmula 363 consta no rodapé mas a biblioteca a marca como "não aplicável" e o corpo nunca a usa.

Aplicando as correções:

Agora preciso do texto exato dos trechos restantes (§5 notas, §6, §8, rodapé) para aplicar as correções numéricas e de redação:

Corrigindo um deslize que introduzi ("excludes" em vez de "exclui") e aplicando as três edições restantes:

parecer.md concluído. Agora os outros três arquivos — lendo na íntegra para achar os números defasados:

Verificação final — JSON revalidado e varredura por números defasados ou resquícios de inglês:

Revisão de qualidade concluída. Todos os quatro arquivos em `deliverable/` foram verificados contra a biblioteca, os documentos e recálculo aritmético completo (Python). Erros encontrados e corrigidos:

## Erros numéricos (corrigidos em todos os arquivos onde apareciam)

1. **Cenário renúncia**: estava 657.165 / ≈818.705; o correto é **657.540 / ≈819.080** (889.928 − aviso 30.600 − multa 40.248 = 819.080; sem HE: 728.388 − 70.848 = 657.540). Corrigido em `parecer.md` (§5 e §7), `parecer.json`, `QUESTIONS.md`, `STATUS.md`.
2. **Diferença aviso + multa 40%**: estava "≈70.850"; correto **70.848** (30.600 + 40.248). Corrigido em `QUESTIONS.md` e `STATUS.md`.
3. **Honorários (teto de 15% do art. 791-A)**: estava 133.400; correto **≈133.500** (15% × 889.928 = 133.489). Corrigido em `parecer.md` §5 e `parecer.json`.

## Erro de data

4. **Print da cobrança de ponto**: estava datado 02/03/2024; o print (`prints_mensagens.txt`) é de **12/03/2024**. Corrigido em `parecer.md` (2 ocorrências) e `parecer.json`.

## Erro de lógica jurídica (§8.2 — prescrição)

5. O texto dizia que, se o ajuizamento atrasasse, "a base cresce" — isso **contradiz** a regra do §4 (o corte quinquenal se fixa no ajuizamento: atrasar o ajuizamento **reduz** a base do autor, o corte avança). Reescrito: corte 16/11/2021 já fixado, 25,5 meses prescritos não voltam; quem perde com atraso é o autor; o que cresce durante o sobrestamento é só a **correção monetária**. Frase correspondente no `STATUS.md` ajustada.

## Referências cruzadas e suporte de autoridade

6. Duas remissões ao Tema 1.389 apontavam para **§4** quando a seção é a **§3** — corrigidas; cabeçalho do parecer ajustado para "ver §2 e §8".
7. **Rodapé de súmulas**: a Súmula 363 do TST aparecia na lista de bases, mas a biblioteca a lista como **não aplicável** (contratação irregular pela administração pública). Anotada como "listada na biblioteca como não aplicável — não foi usada" em vez de removida silenciosamente.
8. Verifiquei a regra do aviso-prévio considerar o **tempo total de serviço ainda que verbas prescritas**: ao contrário da suspeita inicial, ela **está suportada na biblioteca** (`cf_art7_xxix_prescricao.md`) — a citação estava correta, nada alterado.
9. Confirmado: nada cita Súmula 256/OJ 191 como vigentes; continuam marcadas como premissas **não verificadas na biblioteca** apenas CPC 25, divisor 220h, adicional de 50% e regra de ≥15 dias para férias/13º.

## Redação

10. **§6.2 (acordo)**: "teto deixa ~20% de margem" estava confuso — reescrito: 800 mil fica ~10% abaixo do cenário-base (≈890 mil) e ~20–30% abaixo do risco total com acessórios/correção (1,0–1,2 mi); "piso" redefinido com precisão: 537 mil = núcleo devido ao autor, **excluídos** salários (já pagos em NF) e INSS (débito da RFB).
11. **Parênteses da linha de férias** simplificado (rótulos de períodos ambíguos removidos; aritmética explícita 4×24.000 + 21.000 = 117.000).
12. **Intrusões de inglês** corrigidas: "notwithstanding a recusa" → "apesar da recusa"; "cenário favorable" → reescrito em português.

## Verificação final

- `parecer.json` revalidado (`python3 -m json.tool` → OK).
- Grep em todo `deliverable/`: nenhum valor antigo (818.705 / 657.165 / 133.400 / 70.850 / 02/03/2024) nem palavra em inglês restante; os valores corretos aparecem nos 7 pontos esperados; remissões §2/§3/§4/§5/§6.2/§6.3 consistentes.

**Status permanece: COMPLETE WITH OPEN ITEMS** — os itens abertos são os desconhecidos sinalizados em `QUESTIONS.md` (ex.: documentação da defesa "R$ 12k", desfecho do Tema 1.389), não pendências de revisão.