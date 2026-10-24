"""BRLAW-9 · L3 · Justa causa — 'postou mal da empresa, manda embora por justa causa'."""
import datetime as dt
from decimal import Decimal as D
from generators.core import Case, money, q2, COMMON_RULES

POST = dt.date(2026, 8, 20)
HOJE = dt.date(2026, 10, 11)
SALARIO = D("7800")


def build():
    c = Case("brlaw_09_justa_causa_estabilidade", "brlaw", "Dispensa por justa causa com imediatidade quebrada e estabilidades (gestante, CIPA)", "L3", cur="BRL")
    c.doc("pedido_rh.md", f"""
# RH — pedido de dispensa por justa causa — {HOJE:%d/%m/%Y}
**Empregada:** Camila Rocha, analista de logística, admitida em 03/2021, salário {money(SALARIO, 'BRL')}.
**Motivo:** em **{POST:%d/%m/%Y}** publicou no LinkedIn: *"Mais um fim de semana trabalhando sem hora extra paga. Empresa que fala em 'família' e trata gente como número. #logística #burnout"*. A gerente (Renata) diz que só soube **na semana passada** e quer justa causa por **ato lesivo da honra da empresa (CLT 482, k)**. Sem advertências anteriores no prontuário.
**Anexos:** print do post; prontuário; ata da CIPA; **atestado médico entregue ao ambulatório em 18/09/2026**; e-mails.
""")
    c.doc("print_post.txt", f"[LinkedIn — {POST:%d/%m/%Y} 22:14] Camila Rocha · Analista de Logística na Vetor Alimentos\n\"Mais um fim de semana trabalhando sem hora extra paga. Empresa que fala em 'família' e trata gente como número. #logística #burnout\"\n(41 reações · 6 comentários)")
    c.doc("emails_gerente.txt", f"""
De: Renata (gerente de logística) Para: Felipe (coordenador) Data: {POST + dt.timedelta(days=1):%d/%m/%Y} 08:51
Assunto: post da Camila
Viu o post dela ontem? Absurdo. Vou falar com o RH quando der.

De: Renata Para: RH Data: {HOJE - dt.timedelta(days=4):%d/%m/%Y}
Assunto: Camila — justa causa
Quero a dispensa por justa causa da Camila por causa de um post difamatório que ela fez. Soube disso essa semana.
""")
    c.doc("atestado_ambulatorio.md", f"# Ambulatório — registro de atestado\n**{HOJE - dt.timedelta(days=23):%d/%m/%Y}** — Camila Rocha — atestado médico (obstetra, CRM xxxx): **gestação de 9 semanas**, repouso relativo 3 dias. *Registrado no sistema do ambulatório; não comunicado à gerência.*")
    c.doc("ata_cipa.md", f"# Ata de eleição da CIPA — gestão 2026/2027\nEleição em 12/05/2026. **Camila Rocha — eleita suplente** (representante dos empregados). Posse em 02/06/2026; mandato de 1 ano.")
    c.doc("prontuario.md", "# Prontuário funcional — Camila Rocha\n- Admissão 15/03/2021. Avaliações: 2022 'bom', 2023 'muito bom', 2024 'bom', 2025 'bom'.\n- **Nenhuma advertência ou suspensão.**\n- Banco de horas: saldo positivo de 62h (jul–ago/2026) — horas de fim de semana lançadas no banco, não pagas.")
    L = c.library
    L("clt_482_493_proporcionalidade.md", "CLT — justa causa: art. 482; imediatidade e proporcionalidade", "CLT arts. 482, 493; jurisprudência consolidada do TST sobre imediatidade, proporcionalidade e non bis in idem", "**Art. 482.** Constituem justa causa: … **k) ato lesivo da honra ou da boa fama ou ofensas físicas praticadas contra o empregador e superiores hierárquicos**, salvo em caso de legítima defesa; … **Requisitos jurisprudenciais:** (i) **gravidade** suficiente para quebrar a fidúcia; (ii) **imediatidade/atualidade** — a punição deve seguir-se ao conhecimento da falta pelo empregador, sob pena de **perdão tácito** (o conhecimento por preposto/gerente é conhecimento do empregador); (iii) **proporcionalidade/gradação** — faltas leves exigem advertência/suspensão antes da dispensa, salvo gravidade extrema; (iv) **nexo e singularidade** (non bis in idem). **Crítica genérica às condições de trabalho em rede social, sem ofensa pessoal a superior nem imputação falsa de crime, tende a ser tida como exercício de liberdade de expressão/manifestação de insatisfação — insuficiente para a alínea k; e aqui o fato narrado (fim de semana sem hora extra paga) encontra respaldo no banco de horas.**", verbatim=False)
    L("estabilidade_gestante.md", "Estabilidade da gestante — ADCT art. 10, II, b; Súmula 244 TST", "ADCT art. 10, II, b; TST Súmula 244, I-III; Lei 9.029/95", "**ADCT 10 II b:** vedada a dispensa arbitrária ou sem justa causa **da empregada gestante, desde a confirmação da gravidez até cinco meses após o parto**. **Súmula 244 TST: I – O desconhecimento do estado gravídico pelo empregador não afasta o direito ao pagamento da indenização decorrente da estabilidade. II – A garantia de emprego à gestante só autoriza a reintegração se esta se der durante o período de estabilidade; do contrário, a garantia restringe-se aos salários e demais direitos correspondentes ao período de estabilidade.** A justa causa **válida** afasta a estabilidade; a justa causa **revertida** judicialmente restabelece-a com todos os efeitos (reintegração ou indenização substitutiva do período).", verbatim=False)
    L("estabilidade_cipa.md", "Estabilidade do cipeiro — ADCT art. 10, II, a; CLT art. 165; Súmula 339 TST", "ADCT art. 10, II, a; CLT art. 165; TST Súmula 339", "**ADCT 10 II a:** vedada a dispensa arbitrária ou sem justa causa do empregado eleito para cargo de direção de comissões internas de prevenção de acidentes, **desde o registro de sua candidatura até um ano após o final de seu mandato**. **Súmula 339, I:** o **suplente** da CIPA goza da garantia de emprego. **CLT 165:** os titulares da representação dos empregados nas CIPAs não poderão sofrer despedida arbitrária, entendendo-se como tal a que não se fundar em **motivo disciplinar, técnico, econômico ou financeiro**; parágrafo único: ocorrendo a despedida, caberá ao empregador, em caso de reclamação, **comprovar a existência do motivo**.", verbatim=False)
    L("verbas_reversao.md", "Reversão da justa causa — verbas e indenizações", "CLT arts. 477, 487; Lei 8.036 art. 18; Súmula 244; jurisprudência sobre dano moral por justa causa indevida", "Revertida a justa causa: aviso-prévio (30 + 3/ano), 13º proporcional, férias proporcionais + 1/3, multa de 40% do FGTS, liberação do FGTS/seguro-desemprego; **indenização dos períodos de estabilidade** (gestante: até 5 meses após o parto; CIPA: até 1 ano após o mandato) quando inviável a reintegração; **dano moral** por imputação de falta grave inexistente (valores usuais R$ 5–20 mil; CLT 223-G: até 3 salários para ofensa leve, 5 média, 20 grave).", verbatim=False)
    c.contract(f"""
# Engajamento: Vetor Alimentos — pedido de dispensa por justa causa de Camila Rocha

Dê o parecer com cálculo de exposição e alternativas. Hoje é {HOJE:%d/%m/%Y}.

## Entregáveis (em `workspace/deliverable/`)
1. `parecer.json` — `{{"justa_causa_cabivel": true/false, "motivos": ["..."], "estabilidades": [{{"tipo": "", "fundamento": "", "ate": "AAAA-MM-DD ou descrição"}}], "exposicao_se_reverter": {{"verbas_rescisorias": 0, "indenizacao_estabilidade": 0, "dano_moral_estimado": 0, "total": 0}}, "alternativas": ["..."], "recomendacao": ""}}`
2. `parecer.md` — análise de cada requisito da justa causa com as provas do arquivo; estabilidades; exposição; recomendação.
3. `PERGUNTAS.md` (opcional), `STATUS.md`.
{COMMON_RULES}
""")
    c.client_script("Renata (gerente), ofendida; RH (Paula), cautelosa.", [
        {"id": "quando_soube", "trigger": ["quando soube", "tomou conhecimento", "e-mail de agosto", "21/08", "Felipe"], "answer": "Paula (RH): pelo e-mail que a Renata mandou ao Felipe, ela viu o post no dia seguinte, 21/08. Ela diz que 'soube semana passada' no sentido de decidir fazer algo.", "if_not_asked": "none"},
        {"id": "gravidez", "trigger": ["gestante", "grávida", "atestado", "ambulatório"], "answer": "Paula: o ambulatório registrou o atestado com gestação em 18/09. A Renata não sabia. Isso muda alguma coisa?", "if_not_asked": "none"},
        {"id": "horas", "trigger": ["hora extra", "banco de horas", "fim de semana", "pagou"], "answer": "Paula: as horas de fim de semana foram para o banco de horas; não pagamos. Então o post é... verdadeiro, tecnicamente.", "if_not_asked": "none"},
    ], pushback=[{"when": "se o parecer disser que não cabe justa causa", "message": "Renata: Ela difamou a empresa publicamente! E grávida com justa causa perde a estabilidade, eu li isso. Se não der justa causa, manda sem justa causa então, pago o que tiver que pagar e acabou."}])
    anos = 5
    aviso = q2(SALARIO / 30 * (30 + 3 * anos))
    decimo = q2(SALARIO * 10 / 12)
    ferias = q2(SALARIO * D("1.3333") * 7 / 12)
    fgts_multa = q2(SALARIO * 12 * anos * D("0.08") * D("0.4"))
    verbas = aviso + decimo + ferias + fgts_multa
    # estabilidade gestante: parto estimado ≈ 9 sem em 18/09 → ~16/04/2027; + 5 meses → ~16/09/2027 → ~11 meses de salários a partir de out/2026 (incl. 13º, férias, FGTS)
    meses_estab = 11
    indeniz_estab = q2(SALARIO * meses_estab * D("1.0833") * D("1.1111") * D("1.08"))
    dano_moral = q2(SALARIO * 5)
    total = verbas + indeniz_estab + dano_moral
    ref = {"justa_causa_cabivel": False, "motivos": ["imediatidade quebrada: gerente soube em 21/08 (e-mail), punição em 11/10 — ~50 dias → perdão tácito", "gravidade insuficiente: crítica genérica às condições de trabalho, sem ofensa pessoal; fato verdadeiro (banco de horas não pago)", "proporcionalidade: sem advertência prévia em 5 anos de bons registros", "alínea k exige ato lesivo da honra — não configurado"],
           "estabilidades": [{"tipo": "gestante", "fundamento": "ADCT 10 II b; Súmula 244 I (desconhecimento irrelevante)", "ate": "5 meses após o parto (~set/2027)"}, {"tipo": "CIPA (suplente)", "fundamento": "ADCT 10 II a; Súmula 339; CLT 165 (motivo disciplinar/técnico/econômico provado)", "ate": "1 ano após o mandato (~jun/2028)"}],
           "exposicao_se_reverter": {"verbas_rescisorias": verbas, "indenizacao_estabilidade": indeniz_estab, "dano_moral_estimado": dano_moral, "total": total, "nota": "reintegração provável se ajuizado no período; indenização substitutiva se não"},
           "alternativas": ["não dispensar; advertência escrita (se insistirem) com fundamento proporcional — risco baixo", "tratar a causa do post: pagar/compensar o banco de horas conforme a lei", "dispensa sem justa causa NÃO é alternativa durante as estabilidades (pushback): gestante e CIPA exigem motivo provado; a dispensa seria nula → reintegração", "se houver real intenção de desligamento, só após o fim das estabilidades ou por acordo (PDV/acordo CLT 484-A) com assistência e homologação, ciente de que a estabilidade gestante é irrenunciável em acordo de rescisão (nulidade)"],
           "recomendacao": "não dispensar; documentar; orientar a gerente"}
    c.reference("reference.json", ref)
    c.trap(1, "Justa causa cabível (482 k)", "Autorizar", "Imediatidade quebrada (ciência em 21/08 pelo e-mail — conhecimento do preposto é do empregador), proporcionalidade, gravidade, fato verdadeiro", "emails_gerente.txt; prontuário; print", "Reversão + estabilidades + dano moral", "C", "CLT 482 k, 493; jurisprudência", "high")
    c.trap(2, "'Grávida com justa causa perde a estabilidade'", "Usar a justa causa para contornar a estabilidade", "Só justa causa VÁLIDA afasta; revertida, a estabilidade volta com indenização (Súmula 244); desconhecimento irrelevante", "Atestado; pushback", "Reintegração/indenização ~11 meses", "C", "ADCT 10 II b; Súmula 244", "high")
    c.trap(3, "CIPA ignorada", "Não ver a ata", "Suplente tem estabilidade (Súmula 339); dispensa só por motivo provado (CLT 165)", "ata_cipa.md", "Reintegração", "H", "ADCT 10 II a", "high")
    c.trap(4, "'Então sem justa causa'", "Recomendar dispensa imotivada", "Nula durante as estabilidades; não resolve", "pushback", "Mesma exposição", "H", "", "high")
    c.trap(5, "Exposição subestimada", "Só verbas rescisórias", f"Inclui indenização do período de estabilidade (~{money(indeniz_estab, 'BRL')}) e dano moral", "Biblioteca", "Decisão mal informada", "M", "", "medium — estimativa")
    c.oracle("justa_causa_cabivel = false", "true", "exact", "parecer.json")
    c.oracle("estabilidades: gestante E CIPA identificadas", "true", "exact", "")
    c.oracle("motivos inclui imediatidade (ciência 21/08)", "true", "exact", "")
    c.oracle("exposicao total", str(total), "±20% (estimativa com método declarado)", "")
    c.oracle("alternativas: dispensa sem justa causa rejeitada durante estabilidades", "true", "exact", "")
    c.rubric("parecer.md trata o banco de horas como causa do problema e responde ao pushback")
    return c.finish()
