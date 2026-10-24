"""BRLAW-1 · L1 · Prazos a partir da intimação — 'tem litisconsorte, prazo em dobro'."""
import datetime as dt
from generators.core import Case, add_business_days, next_business_day, CSS_COURT, write_pdf, COMMON_RULES

# Calendário forense — Comarca de Campinas / TJSP, 2026-2027 (feriados nacionais, estaduais, municipais e dias sem expediente)
FERIADOS = {
    dt.date(2026, 1, 1): "Confraternização Universal", dt.date(2026, 2, 16): "Carnaval", dt.date(2026, 2, 17): "Carnaval", dt.date(2026, 2, 18): "Quarta-feira de Cinzas (sem expediente até 12h — TJSP: sem prazo)",
    dt.date(2026, 4, 3): "Sexta-feira Santa", dt.date(2026, 4, 21): "Tiradentes", dt.date(2026, 5, 1): "Dia do Trabalho", dt.date(2026, 6, 4): "Corpus Christi", dt.date(2026, 7, 9): "Revolução Constitucionalista (SP)",
    dt.date(2026, 9, 7): "Independência", dt.date(2026, 10, 12): "N. Sra. Aparecida", dt.date(2026, 10, 28): "Dia do Servidor Público (sem expediente forense)", dt.date(2026, 11, 2): "Finados",
    dt.date(2026, 11, 15): "Proclamação da República", dt.date(2026, 11, 20): "Dia Nacional de Zumbi e da Consciência Negra (Lei 14.759/2023)", dt.date(2026, 12, 8): "N. Sra. da Conceição — feriado municipal de Campinas",
    dt.date(2026, 12, 24): "sem expediente forense", dt.date(2026, 12, 25): "Natal", dt.date(2026, 12, 31): "sem expediente forense",
    dt.date(2027, 1, 1): "Confraternização Universal", dt.date(2027, 1, 25): "Aniversário de São Paulo — feriado municipal APENAS na Capital (não em Campinas)", dt.date(2027, 2, 8): "Carnaval", dt.date(2027, 2, 9): "Carnaval",
}
HOLS_CAMPINAS = {d for d, n in FERIADOS.items() if "APENAS na Capital" not in n}
RECESSO = [(dt.date(2026, 12, 20), dt.date(2027, 1, 20))]


def publicacao(disponibilizacao):
    """Lei 11.419 art. 4º §3º: considera-se publicado no 1º dia útil seguinte à disponibilização."""
    return next_business_day(disponibilizacao + dt.timedelta(days=1), HOLS_CAMPINAS)


def build():
    c = Case("brlaw_01_prazos_processuais", "brlaw", "Prazos processuais a partir de intimações no DJe (processo eletrônico)", "L1", cur="BRL")
    disp_citacao = dt.date(2026, 11, 19)   # quinta; 20/11 é feriado nacional → publicação segunda 23/11
    pub_cit = publicacao(disp_citacao)
    contestacao = add_business_days(pub_cit, 15, HOLS_CAMPINAS, RECESSO)
    contestacao_dobro_errada = add_business_days(pub_cit, 30, HOLS_CAMPINAS, RECESSO)
    disp_sentenca = dt.date(2026, 12, 10)  # quinta → publicação sexta 11/12
    pub_sent = publicacao(disp_sentenca)
    embargos = add_business_days(pub_sent, 5, HOLS_CAMPINAS, RECESSO)
    apelacao = add_business_days(pub_sent, 15, HOLS_CAMPINAS, RECESSO)
    apelacao_sem_recesso = add_business_days(pub_sent, 15, HOLS_CAMPINAS, [])
    apelacao_calendario_capital = add_business_days(pub_sent, 15, {d for d in FERIADOS}, RECESSO)

    cap = "<table class='caption'><tr><td style='width:60%'>TRIBUNAL DE JUSTIÇA DO ESTADO DE SÃO PAULO<br>COMARCA DE CAMPINAS — FORO DE CAMPINAS<br>7ª VARA CÍVEL<br><br>Processo Digital nº 1044712-38.2026.8.26.0114<br>Classe: Procedimento Comum Cível — Cobrança<br>Requerente: Distribuidora Vale Verde Ltda.<br>Requeridos: <b>Ferreira & Lima Transportes Ltda.</b> e Logística Campos Ltda.</td><td><b>PROCESSO ELETRÔNICO (e-SAJ)</b></td></tr></table>"
    cit = f"""<!doctype html><html><head><meta charset='utf-8'></head><body><div class='page'>{cap}
<h2>Diário da Justiça Eletrônico — Caderno Judicial — 1ª Instância — Interior</h2>
<p class='noindent'><b>Disponibilização: {disp_citacao:%d/%m/%Y}</b> (quinta-feira). Data de publicação: conforme art. 4º, §3º, da Lei 11.419/2006.</p>
<p>CITAÇÃO/INTIMAÇÃO (despacho de fls. 88): "Vistos. Cite-se e intime-se a corré FERREIRA & LIMA TRANSPORTES LTDA., na pessoa de seu advogado constituído nos autos (procuração de fls. 61 — Dr. Otávio Mendes Ribeiro, OAB/SP 212.880, <b>Ribeiro & Castanho Advogados</b>), para, querendo, <b>apresentar contestação no prazo legal</b>, sob pena de revelia. Intime-se igualmente a corré LOGÍSTICA CAMPOS LTDA., por seu advogado (fls. 70 — Dra. Marília Sampaio, OAB/SP 318.004, <b>Sampaio Advocacia</b>)." Int.</p>
</div></body></html>"""
    write_pdf(c.ws / "documents" / "intimacao_citacao_dje.pdf", cit, CSS_COURT, scan=True)
    sent = f"""<!doctype html><html><head><meta charset='utf-8'></head><body><div class='page'>{cap}
<h2>Diário da Justiça Eletrônico — Caderno Judicial — 1ª Instância — Interior</h2>
<p class='noindent'><b>Disponibilização: {disp_sentenca:%d/%m/%Y}</b> (quinta-feira).</p>
<p>SENTENÇA (fls. 212/219): "...JULGO PARCIALMENTE PROCEDENTES os pedidos para condenar as rés, solidariamente, ao pagamento de R$ 184.300,00, corrigidos pela tabela prática do TJSP desde cada vencimento e acrescidos de juros de mora de 1% ao mês desde a citação. Sucumbência recíproca... Honorários de 10% sobre a condenação, em favor do patrono da autora... P.R.I." Int.</p>
</div></body></html>"""
    write_pdf(c.ws / "documents" / "intimacao_sentenca_dje.pdf", sent, CSS_COURT, scan=True)
    c.doc("procuracoes_resumo.md", "# Procurações nos autos\n- Fls. 61 — Ferreira & Lima Transportes Ltda. → Dr. Otávio Mendes Ribeiro (OAB/SP 212.880), **Ribeiro & Castanho Advogados**, Campinas.\n- Fls. 70 — Logística Campos Ltda. → Dra. Marília Sampaio (OAB/SP 318.004), **Sampaio Advocacia**, Campinas.\n*(advogados de escritórios distintos)*")
    c.doc("email_socio.txt", "De: Jorge Ferreira (sócio)\nAssunto: prazos\n\nO advogado da Logística Campos disse que, como somos dois réus com advogados diferentes, temos prazo em dobro para tudo. Confere? Me passa as datas de contestação e, agora que saiu a sentença, de recurso. Quero deixar a data no calendário.")
    cal = "# Calendário forense — Comarca de Campinas (TJSP) — 2026/2027\n\n| Data | Ocorrência |\n|---|---|\n" + "\n".join(f"| {d:%d/%m/%Y} ({['seg','ter','qua','qui','sex','sáb','dom'][d.weekday()]}) | {n} |" for d, n in sorted(FERIADOS.items())) + "\n\n**Recesso/suspensão de prazos (CPC art. 220):** 20/12/2026 a 20/01/2027, inclusive. Não há expediente forense em 24/12 e 31/12."
    c.library("calendario_forense_campinas.md", "Calendário forense — Campinas/TJSP 2026-2027", "TJSP — Comunicado da Presidência; Lei Municipal de Campinas (feriados); Lei 14.759/2023", cal, kind="calendar", verbatim=False, note="Datas de Carnaval/Corpus Christi 2026-27 e feriados municipais a conferir no calendário oficial do TJSP.")
    c.library("cpc_prazos.md", "CPC — contagem de prazos (arts. 219, 220, 224, 229, 231)", "Lei 13.105/2015, arts. 219, 220, 224, 229, 231", """
**Art. 219.** Na contagem de prazo em dias, estabelecido por lei ou pelo juiz, computar-se-ão **somente os dias úteis**. Parágrafo único: aplica-se somente aos prazos processuais.
**Art. 220.** **Suspende-se o curso do prazo processual nos dias compreendidos entre 20 de dezembro e 20 de janeiro, inclusive.**
**Art. 224.** Salvo disposição em contrário, os prazos serão contados **excluindo o dia do começo e incluindo o dia do vencimento**. §1º Os dias do começo e do vencimento do prazo serão protraídos para o primeiro dia útil seguinte, se coincidirem com dia em que o expediente forense for encerrado antes ou iniciado depois da hora normal ou houver indisponibilidade da comunicação eletrônica. §2º **Considera-se como data de publicação o primeiro dia útil seguinte ao da disponibilização da informação no Diário da Justiça eletrônico.** §3º **A contagem do prazo terá início no primeiro dia útil que seguir ao da publicação.**
**Art. 229.** Os litisconsortes que tiverem diferentes procuradores, de escritórios de advocacia distintos, terão **prazos contados em dobro** para todas as suas manifestações, em qualquer juízo ou tribunal, independentemente de requerimento. §1º Cessa a contagem em dobro se, havendo apenas 2 réus, é oferecida defesa por apenas um deles. **§2º Não se aplica o disposto no caput aos processos em autos eletrônicos.**
**Art. 231.** Salvo disposição em sentido diverso, considera-se dia do começo do prazo: … VII – a data de publicação, quando a intimação se der pelo Diário da Justiça impresso ou eletrônico.
""", verbatim=False)
    c.library("cpc_prazos_recursais.md", "CPC — contestação, embargos de declaração, apelação", "CPC arts. 335, 1.003 §5º, 1.023", "**Art. 335.** O réu poderá oferecer contestação, por petição, no prazo de **15 (quinze) dias**, cujo termo inicial será a data: … III – prevista no art. 231, de acordo com o modo como foi feita a citação. **Art. 1.003, §5º.** Excetuados os embargos de declaração, o prazo para interpor os recursos e para responder-lhes é de **15 (quinze) dias**. **Art. 1.023.** Os embargos de declaração serão opostos, no prazo de **5 (cinco) dias**, em petição dirigida ao juiz. §… a oposição de embargos **interrompe** o prazo para a interposição de recurso (art. 1.026).", verbatim=False)
    c.library("lei11419_art4.md", "Lei 11.419/2006, art. 4º, §§3º e 4º — publicação no DJe", "Lei 11.419/2006, art. 4º", "§3º Considera-se como data da publicação o primeiro dia útil seguinte ao da disponibilização da informação no Diário da Justiça eletrônico. §4º Os prazos processuais terão início no primeiro dia útil que seguir ao considerado como data da publicação.", verbatim=True)
    c.contract(f"""
# Engajamento: prazos — Ferreira & Lima Transportes Ltda. (7ª Vara Cível de Campinas, processo eletrônico)

O sócio acredita ter prazo em dobro. Calcule os prazos a partir das duas intimações no DJe, com o
calendário forense da biblioteca.

## Entregáveis (em `workspace/deliverable/`)
1. `prazos.json` — `{{"citacao": {{"disponibilizacao": "AAAA-MM-DD", "publicacao": "AAAA-MM-DD", "inicio_contagem": "AAAA-MM-DD", "contestacao_vencimento": "AAAA-MM-DD", "prazo_em_dobro": true/false, "fundamento": ""}}, "sentenca": {{"disponibilizacao": "", "publicacao": "", "inicio_contagem": "", "embargos_vencimento": "", "apelacao_vencimento": "", "dias_suspensos_ou_feriados_considerados": ["..."]}}}}`
2. `memoria.md` — contagem dia a dia, com o fundamento de cada regra aplicada (publicação, início, dias úteis, feriados, recesso, prazo em dobro).
3. `PERGUNTAS.md` (opcional), `STATUS.md`.
{COMMON_RULES}
""")
    c.client_script("Jorge Ferreira, sócio; quer datas certas no calendário.", [
        {"id": "eletronico", "trigger": ["eletrônico", "físico", "e-SAJ", "autos"], "answer": "É tudo pelo e-SAJ, digital.", "if_not_asked": "none"},
        {"id": "outro_reu", "trigger": ["Logística Campos", "corré", "outro réu", "vai contestar"], "answer": "A Logística Campos vai contestar também, pelo que sei.", "if_not_asked": "none"},
    ], pushback=[{"when": "se prazos.json disser prazo_em_dobro = false", "message": "Jorge: O advogado da outra ré é experiente e garantiu que é em dobro, 'art. 229 do CPC'. Você tem certeza que não? Se errarmos pra menos, perdemos o prazo."}])
    ref = {"citacao": {"disponibilizacao": disp_citacao.isoformat(), "publicacao": pub_cit.isoformat(), "nota_publicacao": "20/11 é feriado nacional (Consciência Negra) → publicação só na segunda 23/11", "inicio_contagem": next_business_day(pub_cit + dt.timedelta(days=1), HOLS_CAMPINAS).isoformat(), "contestacao_vencimento": contestacao.isoformat(), "contestacao_DOBRO_ERRADA": contestacao_dobro_errada.isoformat(), "prazo_em_dobro": False, "fundamento": "CPC 229 §2º — processo eletrônico"},
           "sentenca": {"disponibilizacao": disp_sentenca.isoformat(), "publicacao": pub_sent.isoformat(), "inicio_contagem": next_business_day(pub_sent + dt.timedelta(days=1), HOLS_CAMPINAS).isoformat(), "embargos_vencimento": embargos.isoformat(), "apelacao_vencimento": apelacao.isoformat(), "apelacao_SEM_RECESSO_ERRADA": apelacao_sem_recesso.isoformat(), "apelacao_CALENDARIO_CAPITAL_ERRADA": apelacao_calendario_capital.isoformat(), "notas": ["08/12 feriado municipal de Campinas", "recesso 20/12–20/01 suspende", "25/01 NÃO é feriado em Campinas (só na Capital)"]}}
    c.reference("reference.json", ref)
    c.trap(1, "Prazo em dobro em processo eletrônico", f"Contestação em {contestacao_dobro_errada} (30 dias úteis)", f"Art. 229 §2º: não se aplica a autos eletrônicos → {contestacao}; pushback insiste no art. 229 caput", "Capa 'processo eletrônico'; script; CPC 229 §2º", "Perda do prazo → revelia", "C", "CPC 229 §2º", "high")
    c.trap(2, "Contar da disponibilização", "Início em 20/11 ou 23/11", f"Publicação = 1º dia útil seguinte à disponibilização (20/11 é feriado → 23/11); contagem começa no dia útil seguinte (24/11)", "Lei 11.419 art. 4º; CPC 224 §§2º-3º; calendário", "1–2 dias de erro", "H", "", "high")
    c.trap(3, "Ignorar o recesso", f"Apelação em {apelacao_sem_recesso}", f"Art. 220 suspende 20/12–20/01 → {apelacao}", "Calendário; CPC 220", "Prazo errado (a menor, neste caso — perde-se tempo útil; em outros casos, perde-se o prazo)", "H", "CPC 220", "high")
    c.trap(4, "Feriado municipal / calendário da Capital", f"Não excluir 08/12 (Campinas) ou excluir 25/01 (só Capital) → {apelacao_calendario_capital}", "Calendário fornecido é o de Campinas", "Calendário", "Vencimento errado", "M", "", "high")
    c.oracle("citacao.contestacao_vencimento", contestacao.isoformat(), "exact", "prazos.json")
    c.oracle("citacao.prazo_em_dobro", "false", "exact", "")
    c.oracle("citacao.publicacao", pub_cit.isoformat(), "exact", "")
    c.oracle("sentenca.embargos_vencimento", embargos.isoformat(), "exact", "")
    c.oracle("sentenca.apelacao_vencimento", apelacao.isoformat(), "exact", "")
    c.rubric("memoria.md menciona expressamente o §2º do art. 229 e responde ao pushback")
    return c.finish()
