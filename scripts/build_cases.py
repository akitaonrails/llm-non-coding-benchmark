#!/usr/bin/env python3
"""Build every case pack under tasks/ from fixtures/cases/*.py. Idempotent. Never runs a model."""
import argparse
import importlib
import pkgutil
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "fixtures"))

import cases  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", help="module names, e.g. usacc_01")
    args = ap.parse_args()
    mods = sorted(m.name for m in pkgutil.iter_modules(cases.__path__))
    if args.only:
        mods = [m for m in mods if m in args.only]
    built = []
    for name in mods:
        t = time.time()
        mod = importlib.import_module(f"cases.{name}")
        d = mod.build()
        n_docs = len(list((d / "workspace" / "documents").glob("*")))
        n_lib = len(list((d / "workspace" / "library").glob("*.md"))) - 1
        print(f"{name:12s} -> {d.relative_to(ROOT)}  docs={n_docs:2d} lib={n_lib:2d}  {time.time()-t:4.1f}s")
        built.append(name)
    print(f"built {len(built)} cases")


if __name__ == "__main__":
    main()
