#!/usr/bin/env python3
"""Bygger hela Pages-sajten: dev-portal i site/ och varje projekt i site/projekt/<slug>/.

Projekten ska redan vara utcheckade i projects/<slug>/ (görs av pages.yml).
Ett projekt som saknas eller saknar mkdocs.yml hoppas över med en varning.
"""
import pathlib
import subprocess
import sys

import yaml

root = pathlib.Path(__file__).resolve().parent.parent
subprocess.run([sys.executable, "-m", "mkdocs", "build", "--strict", "-d", "site"], cwd=root, check=True)
for p in yaml.safe_load((root / "projects.yml").read_text())["projects"]:
    src = root / "projects" / p["slug"]
    if not p.get("publish"):
        continue
    if not (src / "mkdocs.yml").exists():
        print(f"::warning::{p['name']}: ingen mkdocs.yml i {p['repo']}@{p['branch']}, hoppar över")
        continue
    out = root / "site" / "projekt" / p["slug"]
    subprocess.run([sys.executable, "-m", "mkdocs", "build", "-f", str(src / "mkdocs.yml"), "-d", str(out)], check=True)
    print(f"byggde {p['name']} -> site/projekt/{p['slug']}/")
