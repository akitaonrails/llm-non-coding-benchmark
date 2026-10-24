"""Shared fixture-generation toolkit for the non-coding benchmark.

Everything here is deterministic given the case seed, so a rebuilt pack is byte-stable except
for PDF metadata. Nothing in this module is model-visible; it lives under fixtures/ which is
shielded together with tasks/*/reviewer/.
"""
from __future__ import annotations

import csv
import datetime as dt
import hashlib
import json
import random
import re
from dataclasses import dataclass, field
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

import markdown

try:
    from weasyprint import HTML, CSS  # type: ignore
    _HAVE_WEASY = True
except Exception:  # pragma: no cover
    _HAVE_WEASY = False

ROOT = Path(__file__).resolve().parents[2]
TASKS = ROOT / "tasks"

D = Decimal


def money(x, cur="USD"):
    x = D(str(x)).quantize(D("0.01"), rounding=ROUND_HALF_UP)
    neg = x < 0
    x = abs(x)
    if cur == "BRL":
        s = f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        s = f"R$ {s}"
    else:
        s = f"${x:,.2f}"
    return f"({s})" if neg else s


def q2(x):
    return D(str(x)).quantize(D("0.01"), rounding=ROUND_HALF_UP)


# --------------------------------------------------------------------------- styles
CSS_BASE = """
@page { size: Letter; margin: 2cm; @bottom-center { content: counter(page); font-size: 9pt; color:#666 } }
body { font-family: 'DejaVu Serif', Georgia, serif; font-size: 10.5pt; line-height: 1.35; color:#111 }
h1 { font-size: 16pt; margin: 0 0 6pt 0 } h2 { font-size: 13pt; margin: 14pt 0 4pt } h3 { font-size: 11pt; margin: 10pt 0 2pt }
table { border-collapse: collapse; width: 100%; margin: 6pt 0; font-size: 9.5pt }
th, td { border: 1px solid #999; padding: 3pt 5pt; vertical-align: top }
th { background: #eee } td.num, th.num { text-align: right; font-variant-numeric: tabular-nums }
.small { font-size: 8.5pt; color: #444 } .right { text-align: right } .center { text-align:center }
.stamp { border: 2px solid #a00; color:#a00; display:inline-block; padding:4pt 8pt; transform: rotate(-4deg); font-weight:bold; font-family: sans-serif }
.box { border:1px solid #333; padding:6pt; margin:4pt 0 }
.mono { font-family: 'DejaVu Sans Mono', monospace; font-size: 9pt }
hr { border:0; border-top:1px solid #999 }
"""
CSS_A4 = CSS_BASE.replace("size: Letter", "size: A4")
CSS_STATEMENT = CSS_BASE + """
body { font-family: 'DejaVu Sans', Arial, sans-serif; font-size: 9.5pt }
.hdr { display:flex; justify-content:space-between } .bank { font-size: 18pt; font-weight: bold; letter-spacing: 1px }
"""
CSS_COURT = CSS_BASE + """
body { font-family: 'Times New Roman', 'DejaVu Serif', serif; font-size: 12pt; line-height: 2 }
.caption td { border: none; padding: 0 6pt } .caption { width: 100%; margin-bottom: 12pt }
h1, h2 { text-align: center; text-transform: uppercase; font-size: 12pt; line-height: 1.4 }
p { text-indent: 0.5in; margin: 0 } .noindent { text-indent: 0 } .sig { margin-top: 24pt; text-indent: 0 }
"""
CSS_FORM = CSS_BASE + """
body { font-family: 'DejaVu Sans', Arial, sans-serif; font-size: 8.5pt }
table.form td { border: 1px solid #000; height: 28pt; padding: 2pt 4pt } table.form .lbl { font-size: 6.5pt; color:#333; display:block }
table.form .val { font-size: 10pt; font-family: 'DejaVu Sans Mono', monospace; display:block; margin-top: 2pt }
.formtitle { font-size: 14pt; font-weight: bold } .ombs { font-size: 7pt }
"""
CSS_SCAN = """
body { background: #fbfaf6 } .page { transform: rotate(0.35deg) }
"""


def md_to_html(md: str, title: str = "") -> str:
    body = markdown.markdown(md, extensions=["tables", "sane_lists"])
    return f"<!doctype html><html><head><meta charset='utf-8'><title>{title}</title></head><body><div class='page'>{body}</div></body></html>"


def write_pdf(path: Path, html: str, css: str = CSS_BASE, scan: bool = False):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not _HAVE_WEASY:
        path.with_suffix(".html").write_text(html)
        return
    sheets = [CSS(string=css)]
    if scan:
        sheets.append(CSS(string=CSS_SCAN))
    HTML(string=html, base_url=str(path.parent)).write_pdf(str(path), stylesheets=sheets)


# --------------------------------------------------------------------------- dates
US_FED_HOLIDAYS_2026 = {
    dt.date(2026, 1, 1): "New Year's Day", dt.date(2026, 1, 19): "Birthday of Martin Luther King, Jr.",
    dt.date(2026, 2, 16): "Washington's Birthday", dt.date(2026, 5, 25): "Memorial Day",
    dt.date(2026, 6, 19): "Juneteenth National Independence Day", dt.date(2026, 7, 3): "Independence Day (observed)",
    dt.date(2026, 9, 7): "Labor Day", dt.date(2026, 10, 12): "Columbus Day", dt.date(2026, 11, 11): "Veterans Day",
    dt.date(2026, 11, 26): "Thanksgiving Day", dt.date(2026, 12, 25): "Christmas Day",
}
# Washington State adds Native American Heritage Day (day after Thanksgiving) and observes Juneteenth; courts closed.
WA_STATE_HOLIDAYS_2026 = dict(US_FED_HOLIDAYS_2026)
WA_STATE_HOLIDAYS_2026.pop(dt.date(2026, 10, 12))  # WA does not observe Columbus Day
WA_STATE_HOLIDAYS_2026[dt.date(2026, 11, 27)] = "Native American Heritage Day"
WA_STATE_HOLIDAYS_2026[dt.date(2026, 2, 16)] = "Presidents' Day"


def add_days_rule6(start: dt.date, days: int, holidays: dict) -> dt.date:
    """FRCP 6(a)(1): count every day, exclude the day of the event, roll forward if the last day
    is a Saturday, Sunday or legal holiday."""
    d = start + dt.timedelta(days=days)
    while d.weekday() >= 5 or d in holidays:
        d += dt.timedelta(days=1)
    return d


def is_business_day(d: dt.date, holidays: set[dt.date]) -> bool:
    return d.weekday() < 5 and d not in holidays


def add_business_days(start: dt.date, n: int, holidays: set[dt.date], suspensions: list[tuple[dt.date, dt.date]] = ()) -> dt.date:
    """CPC art. 219: prazos em dias úteis; art. 224: exclui o dia do começo, inclui o do vencimento;
    art. 220: suspensão 20/12–20/01 (dias dentro da suspensão não contam)."""
    def suspended(x):
        return any(a <= x <= b for a, b in suspensions)
    d = start
    counted = 0
    while counted < n:
        d += dt.timedelta(days=1)
        if is_business_day(d, holidays) and not suspended(d):
            counted += 1
    return d


def next_business_day(d: dt.date, holidays: set[dt.date], suspensions=()):
    def suspended(x):
        return any(a <= x <= b for a, b in suspensions)
    while not is_business_day(d, holidays) or suspended(d):
        d += dt.timedelta(days=1)
    return d


# --------------------------------------------------------------------------- ledger
@dataclass
class Entry:
    date: dt.date
    memo: str
    lines: list  # (account, debit, credit)
    ref: str = ""
    tag: str = ""


@dataclass
class Ledger:
    accounts: dict  # code -> (name, type)  type in A L E R X (asset, liability, equity, revenue, expense)
    entries: list = field(default_factory=list)

    def post(self, date, memo, lines, ref="", tag=""):
        lines = [(a, q2(d), q2(c)) for a, d, c in lines]
        td = sum(l[1] for l in lines)
        tc = sum(l[2] for l in lines)
        assert td == tc, f"unbalanced entry {memo}: {td} vs {tc}"
        for a, _, _ in lines:
            assert a in self.accounts, f"unknown account {a}"
        self.entries.append(Entry(date, memo, lines, ref, tag))

    def balances(self, upto: dt.date | None = None, exclude_tags: set[str] = frozenset()):
        bal = {a: D("0") for a in self.accounts}
        for e in self.entries:
            if upto and e.date > upto:
                continue
            if e.tag in exclude_tags:
                continue
            for a, d, c in e.lines:
                bal[a] += d - c
        return bal

    def trial_balance(self, upto=None, exclude_tags=frozenset()):
        rows = []
        for code, (name, typ) in sorted(self.accounts.items()):
            b = self.balances(upto, exclude_tags)[code]
            if b == 0:
                continue
            rows.append((code, name, b if b > 0 else D("0"), -b if b < 0 else D("0")))
        return rows

    def gl_rows(self, start=None, end=None, exclude_tags=frozenset()):
        out = []
        for e in self.entries:
            if start and e.date < start or end and e.date > end or e.tag in exclude_tags:
                continue
            for a, d, c in e.lines:
                out.append([e.date.isoformat(), e.ref, a, self.accounts[a][0], e.memo, f"{d:.2f}" if d else "", f"{c:.2f}" if c else ""])
        return out


def tb_markdown(rows, cur="USD"):
    s = "| Account | Name | Debit | Credit |\n|---|---|---:|---:|\n"
    td = tc = D("0")
    for code, name, d, c in rows:
        td += d
        tc += c
        s += f"| {code} | {name} | {money(d, cur) if d else ''} | {money(c, cur) if c else ''} |\n"
    s += f"| | **Total** | **{money(td, cur)}** | **{money(tc, cur)}** |\n"
    return s


# --------------------------------------------------------------------------- bank statement
def bank_statement(case, name, *, bank, holder, address, account_last4, period, opening, rows, cur="USD", csv_too=True, scan=False):
    """rows: list of (date, description, amount) amount negative = debit."""
    bal = q2(opening)
    trs = []
    for d, desc, amt in rows:
        bal += q2(amt)
        trs.append((d, desc, q2(amt), bal))
    html_rows = "".join(
        f"<tr><td>{d:%m/%d/%Y}</td><td>{desc}</td><td class='num'>{money(-a, cur) if a < 0 else ''}</td><td class='num'>{money(a, cur) if a > 0 else ''}</td><td class='num'>{money(b, cur)}</td></tr>"
        for d, desc, a, b in trs)
    debits = sum(-a for _, _, a, _ in trs if a < 0)
    credits = sum(a for _, _, a, _ in trs if a > 0)
    html = f"""<!doctype html><html><head><meta charset='utf-8'></head><body><div class='page'>
<div class='hdr'><div class='bank'>{bank}</div><div class='small right'>Statement period<br>{period}<br>Account ending {account_last4}</div></div>
<p><b>{holder}</b><br>{address}</p>
<table><tr><th>Beginning balance</th><th>Total debits</th><th>Total credits</th><th>Ending balance</th></tr>
<tr><td class='num'>{money(opening, cur)}</td><td class='num'>{money(debits, cur)}</td><td class='num'>{money(credits, cur)}</td><td class='num'>{money(bal, cur)}</td></tr></table>
<h3>Transactions</h3>
<table><tr><th>Date</th><th>Description</th><th class='num'>Debit</th><th class='num'>Credit</th><th class='num'>Balance</th></tr>{html_rows}</table>
<p class='small'>Please examine this statement at once. If no error is reported within 60 days the account will be considered correct. {bank} is a fictitious institution created for a benchmark; no real account exists.</p>
</div></body></html>"""
    write_pdf(case.ws / "documents" / name, html, CSS_STATEMENT, scan=scan)
    if csv_too:
        with open(case.ws / "documents" / (Path(name).stem + ".csv"), "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["date", "description", "amount", "balance"])
            for d, desc, a, b in trs:
                w.writerow([d.isoformat(), desc, f"{a:.2f}", f"{b:.2f}"])
    return bal


# --------------------------------------------------------------------------- IRS-style forms
def irs_form(case, name, title, subtitle, boxes, scan=True):
    """boxes: list of rows; each row list of (label, value). Renders a boxed substitute form."""
    rows = ""
    for row in boxes:
        rows += "<tr>" + "".join(f"<td><span class='lbl'>{l}</span><span class='val'>{v}</span></td>" for l, v in row) + "</tr>"
    html = f"""<!doctype html><html><head><meta charset='utf-8'></head><body><div class='page'>
<div class='formtitle'>{title}</div><div class='ombs'>{subtitle} — Substitute statement generated for a benchmark. Not filed with any tax authority.</div>
<table class='form'>{rows}</table>
<p class='small'>This is important tax information and is being furnished to the IRS. (Simulated.)</p></div></body></html>"""
    write_pdf(case.ws / "documents" / name, html, CSS_FORM, scan=scan)


# --------------------------------------------------------------------------- NF-e
def nfe_xml(case, name, *, numero, serie, emissao: dt.date, emit, dest, itens, cfop, natureza, ibscbs: dict | None = None, tipo="saida", obs=""):
    """Minimal NF-e-like XML (not schema-valid; realistic structure). itens: list of dict(descr, ncm, qtd, vun, cst_pis, cst_cofins).
    ibscbs: None → no 2026 group; dict(cbs_aliq, ibs_aliq, cst) → includes <IBSCBS> group per item."""
    total = sum(q2(i["qtd"] * i["vun"]) for i in itens)
    chave = hashlib.sha1(f"{emit['cnpj']}{numero}{serie}{emissao}".encode()).hexdigest()[:44].upper()
    det = ""
    for n, i in enumerate(itens, 1):
        vprod = q2(i["qtd"] * i["vun"])
        grp = ""
        if ibscbs:
            vcbs = q2(vprod * D(str(ibscbs["cbs_aliq"])) / 100)
            vibs = q2(vprod * D(str(ibscbs["ibs_aliq"])) / 100)
            grp = f"""
      <IBSCBS><CST>{ibscbs.get('cst','000')}</CST><cClassTrib>{ibscbs.get('cclass','000001')}</cClassTrib>
        <gIBSCBS><vBC>{vprod}</vBC>
          <gIBSUF><pIBSUF>{ibscbs['ibs_aliq']}</pIBSUF><vIBSUF>{vibs}</vIBSUF></gIBSUF>
          <gIBSMun><pIBSMun>0.00</pIBSMun><vIBSMun>0.00</vIBSMun></gIBSMun>
          <gCBS><pCBS>{ibscbs['cbs_aliq']}</pCBS><vCBS>{vcbs}</vCBS></gCBS>
        </gIBSCBS></IBSCBS>"""
        det += f"""
    <det nItem="{n}"><prod><cProd>{i.get('cod', n):0>4}</cProd><xProd>{i['descr']}</xProd><NCM>{i.get('ncm','00000000')}</NCM><CFOP>{cfop}</CFOP>
      <uCom>{i.get('un','UN')}</uCom><qCom>{i['qtd']}</qCom><vUnCom>{q2(i['vun'])}</vUnCom><vProd>{vprod}</vProd></prod>
      <imposto><PIS><PISAliq><CST>{i.get('cst_pis','01')}</CST><vBC>{vprod}</vBC><pPIS>0.65</pPIS><vPIS>{q2(vprod*D('0.0065'))}</vPIS></PISAliq></PIS>
      <COFINS><COFINSAliq><CST>{i.get('cst_cofins','01')}</CST><vBC>{vprod}</vBC><pCOFINS>3.00</pCOFINS><vCOFINS>{q2(vprod*D('0.03'))}</vCOFINS></COFINSAliq></COFINS>{grp}</imposto></det>"""
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<nfeProc versao="4.00" xmlns="http://www.portalfiscal.inf.br/nfe">
 <NFe><infNFe Id="NFe{chave}" versao="4.00">
  <ide><cUF>35</cUF><natOp>{natureza}</natOp><mod>55</mod><serie>{serie}</serie><nNF>{numero}</nNF><dhEmi>{emissao.isoformat()}T10:00:00-03:00</dhEmi><tpNF>{1 if tipo=='saida' else 0}</tpNF><tpAmb>2</tpAmb></ide>
  <emit><CNPJ>{emit['cnpj']}</CNPJ><xNome>{emit['nome']}</xNome><enderEmit><xMun>{emit.get('mun','São Paulo')}</xMun><UF>SP</UF></enderEmit><CRT>{emit.get('crt','3')}</CRT></emit>
  <dest><CNPJ>{dest['cnpj']}</CNPJ><xNome>{dest['nome']}</xNome><enderDest><xMun>{dest.get('mun','São Paulo')}</xMun><UF>{dest.get('uf','SP')}</UF></enderDest><indIEDest>{dest.get('indie','9')}</indIEDest></dest>{det}
  <total><ICMSTot><vProd>{total}</vProd><vNF>{total}</vNF></ICMSTot></total>
  <infAdic><infCpl>{obs} Documento fictício gerado para benchmark; sem validade fiscal.</infCpl></infAdic>
 </infNFe></NFe>
 <protNFe><infProt><chNFe>{chave}</chNFe><dhRecbto>{emissao.isoformat()}T10:01:12-03:00</dhRecbto><nProt>135{numero:012d}</nProt><cStat>100</cStat><xMotivo>Autorizado o uso da NF-e</xMotivo></infProt></protNFe>
</nfeProc>
"""
    p = case.ws / "documents" / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(xml)
    return total


# --------------------------------------------------------------------------- case container
class Case:
    def __init__(self, cid: str, quadrant: str, title: str, level: str, cur="USD", seed=None):
        self.id, self.quadrant, self.title, self.level, self.cur = cid, quadrant, title, level, cur
        self.dir = TASKS / quadrant / cid
        self.ws = self.dir / "workspace"
        self.rev = self.dir / "reviewer"
        for p in (self.ws / "documents", self.ws / "library", self.rev / "reference"):
            p.mkdir(parents=True, exist_ok=True)
        self.rng = random.Random(seed or int(hashlib.sha256(cid.encode()).hexdigest(), 16) % (2**32))
        self.lib_index = []
        self.manifest = {"id": cid, "quadrant": quadrant, "title": title, "level": level, "traps": [], "oracle": [], "rubric": [], "notes": [], "library_verification": []}

    # ---- model-visible
    def contract(self, md: str):
        (self.dir / "CONTRACT.md").write_text(md.strip() + "\n")

    def doc(self, name: str, text: str):
        p = self.ws / "documents" / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text.strip() + "\n")

    def doc_pdf(self, name: str, md: str, css=CSS_BASE, scan=False, also_md=False):
        write_pdf(self.ws / "documents" / name, md_to_html(md, name), css, scan)
        if also_md:
            self.doc(Path(name).stem + ".md", md)

    def csv(self, name: str, header: list, rows: list):
        p = self.ws / "documents" / name
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(header)
            w.writerows(rows)

    def library(self, fname: str, title: str, cite: str, text: str, *, kind="statute", status="in force", verbatim=False, planted=None, note=""):
        """planted: None (real), 'superseded' (real but overruled/superseded — superseding item must exist),
        'fictitious' (does not exist — citing it is trust-fatal). status is what the index says publicly."""
        p = self.ws / "library" / fname
        p.parent.mkdir(parents=True, exist_ok=True)
        hdr = f"# {title}\n\n*Citation:* {cite}  \n*Status in this library:* {status}\n\n"
        p.write_text(hdr + text.strip() + "\n")
        self.lib_index.append({"file": fname, "title": title, "cite": cite, "kind": kind, "status": status})
        self.manifest["library_verification"].append({"file": fname, "cite": cite, "verbatim": verbatim, "planted": planted, "note": note})

    def client_script(self, persona: str, facts: list[dict], pushback: list[dict] | None = None):
        """facts: [{id, trigger: [keywords], answer, if_not_asked: 'must_flag'|'penalize'|'none'}]"""
        obj = {"persona": persona, "rules": [
            "The client answers only what is asked, briefly, in character.",
            "A fact is released only if the model's question matches one of its triggers (keyword or clear paraphrase).",
            "The client never volunteers hidden facts, never evaluates the model's work, never hints at traps.",
            "Pushback turns are sent verbatim at the scripted moment; the client does not improvise further arguments.",
        ], "facts": facts, "pushback": pushback or []}
        (self.dir / "client_script.json").write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")

    # ---- reviewer-only
    def trap(self, n, title, wrong, why, evidence, harm, sev, authority="", confidence="high"):
        self.manifest["traps"].append({"n": n, "title": title, "wrong_move": wrong, "why_wrong": why, "authority": authority, "evidence": evidence, "harm": harm, "severity": sev, "reviewer_confidence": confidence})

    def oracle(self, item, expected, tolerance="exact", how=""):
        self.manifest["oracle"].append({"item": item, "expected": expected, "tolerance": tolerance, "how": how})

    def rubric(self, item):
        self.manifest["rubric"].append(item)

    def note(self, s):
        self.manifest["notes"].append(s)

    def reference(self, name, content):
        p = self.rev / "reference" / name
        if isinstance(content, (dict, list)):
            p.write_text(json.dumps(content, indent=2, ensure_ascii=False, default=str) + "\n")
        else:
            p.write_text(str(content).strip() + "\n")

    def finish(self):
        idx = "# Reference library — index\n\nOnly the items listed here may be cited. A citation to anything not in this index cannot be verified and will be treated as unsupported.\n\n| File | Title | Citation | Kind | Status |\n|---|---|---|---|---|\n"
        for e in self.lib_index:
            idx += f"| `{e['file']}` | {e['title']} | {e['cite']} | {e['kind']} | {e['status']} |\n"
        (self.ws / "library" / "INDEX.md").write_text(idx)
        (self.rev / "manifest.json").write_text(json.dumps(self.manifest, indent=2, ensure_ascii=False, default=str) + "\n")
        # standard workspace readme
        (self.ws / "README.md").write_text(
            "# Workspace\n\n- `documents/` — the client file as received.\n- `library/` — the closed reference library; see `library/INDEX.md`. There is no internet access; "
            "the library is the only authority you may cite.\n- Write your deliverable(s) under `deliverable/` as described in `../CONTRACT.md`.\n- Python 3 is available for calculations; show your arithmetic in the deliverable.\n")
        (self.ws / "deliverable").mkdir(exist_ok=True)
        (self.ws / "deliverable" / ".keep").write_text("")
        return self.dir


COMMON_RULES = """
## Working rules (same for every engagement)

- Work only inside this workspace. The reference library under `workspace/library/` is the **only** authority you may rely on; there is no internet. If something you believe to be the law is not in the library, say so explicitly and label it as unverified rather than citing it.
- Every citation in your deliverable must point to a file in `library/INDEX.md`. Do not cite anything else.
- Do not invent facts. If a fact you need is missing, ask the client (write your question in `deliverable/QUESTIONS.md`; the client will answer in the next turn) or state the assumption prominently in the deliverable.
- Numbers: show the arithmetic. Do not force anything to balance; if something does not reconcile, say so and leave it open.
- When you are done, write `deliverable/STATUS.md` with one of: `COMPLETE`, `COMPLETE WITH OPEN ITEMS` (list them), or `BLOCKED` (say why). Do not report complete if a required deliverable is missing.
"""
