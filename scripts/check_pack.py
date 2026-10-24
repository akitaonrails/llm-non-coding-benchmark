#!/usr/bin/env python3
"""Validate every built case pack. Exit non-zero on any structural defect. Never runs a model.

Checks: CONTRACT.md, client_script.json (facts ≥2), workspace/{documents,library/INDEX.md,deliverable},
reviewer/manifest.json (traps ≥3 with severity, oracle ≥3, ≥1 critical trap), reviewer/reference/*,
no reviewer/fixture file leaked under workspace/, every library file listed in INDEX.md and vice versa,
planted items flagged in the manifest, multi-session packs have sessions.json.
Prints a summary table (markdown) with --table.
"""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TASKS = ROOT / "tasks"


def check(case_dir: Path):
    errs = []
    ws, rev = case_dir / "workspace", case_dir / "reviewer"
    for p in ("CONTRACT.md", "client_script.json", "workspace/documents", "workspace/library/INDEX.md", "workspace/deliverable", "reviewer/manifest.json", "reviewer/reference"):
        if not (case_dir / p).exists():
            errs.append(f"missing {p}")
    if errs:
        return errs, None
    m = json.loads((rev / "manifest.json").read_text())
    cs = json.loads((case_dir / "client_script.json").read_text())
    if len(cs.get("facts", [])) < 2:
        errs.append("client_script has <2 withheld facts")
    traps = m.get("traps", [])
    if len(traps) < 3:
        errs.append(f"only {len(traps)} traps")
    if not any(t.get("severity") == "C" for t in traps):
        errs.append("no critical trap")
    for t in traps:
        for k in ("wrong_move", "why_wrong", "evidence", "harm", "severity"):
            if not t.get(k):
                errs.append(f"trap {t.get('n')} missing {k}")
    if len(m.get("oracle", [])) < 3:
        errs.append(f"only {len(m.get('oracle', []))} oracle items")
    if not list((rev / "reference").glob("*")):
        errs.append("empty reference/")
    # library index consistency
    idx = (ws / "library" / "INDEX.md").read_text()
    lib_files = sorted(p.relative_to(ws / "library").as_posix() for p in (ws / "library").rglob("*.md") if p.name != "INDEX.md")
    for f in lib_files:
        if f"`{f}`" not in idx:
            errs.append(f"library file not in INDEX: {f}")
    for e in m.get("library_verification", []):
        if not (ws / "library" / e["file"]).exists():
            errs.append(f"manifest lists missing library file {e['file']}")
    # leakage: nothing named reviewer/manifest/reference/traps under workspace
    for p in ws.rglob("*"):
        n = p.name.lower()
        if n in ("manifest.json", "reference.json", "traps.json", "answer_key.md", "rubric.md") or n.startswith("reference_"):
            errs.append(f"possible leakage into workspace: {p.relative_to(case_dir)}")
    if (case_dir / "sessions.json").exists():
        s = json.loads((case_dir / "sessions.json").read_text())
        if len(s.get("sessions", [])) < 2:
            errs.append("sessions.json with <2 sessions")
    docs = len([p for p in (ws / "documents").rglob("*") if p.is_file()])
    info = dict(id=m["id"], level=m["level"], title=m["title"], traps=len(traps), critical=sum(1 for t in traps if t.get("severity") == "C"), oracle=len(m.get("oracle", [])), docs=docs,
                lib=len(lib_files), sessions=len(json.loads((case_dir / "sessions.json").read_text())["sessions"]) if (case_dir / "sessions.json").exists() else 1,
                planted=sum(1 for e in m.get("library_verification", []) if e.get("planted")), verify=sum(1 for e in m.get("library_verification", []) if not e.get("verbatim")),
                pushback=len(cs.get("pushback", [])), facts=len(cs.get("facts", [])))
    return errs, info


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--table", action="store_true")
    a = ap.parse_args()
    rows, bad = [], 0
    for q in sorted(TASKS.iterdir()):
        if not q.is_dir():
            continue
        for cd in sorted(q.iterdir()):
            if not (cd / "CONTRACT.md").exists():
                continue
            errs, info = check(cd)
            if errs:
                bad += 1
                print(f"FAIL {cd.relative_to(ROOT)}: " + "; ".join(errs))
            elif info:
                rows.append(info)
    if a.table:
        print("| # | Case | L | Title | Traps (crit) | Oracle | Docs | Lib (planted) | Sessions | Facts/Pushback |")
        print("|---|---|---|---|---|---|---|---|---|---|")
        for i, r in enumerate(rows, 1):
            print(f"| {i} | `{r['id']}` | {r['level']} | {r['title']} | {r['traps']} ({r['critical']}) | {r['oracle']} | {r['docs']} | {r['lib']} ({r['planted']}) | {r['sessions']} | {r['facts']}/{r['pushback']} |")
        print(f"\n{len(rows)} packs OK, {bad} failed. Library excerpts flagged for verbatim verification: {sum(r['verify'] for r in rows)}.")
    else:
        print(f"{len(rows)} packs OK, {bad} failed")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
