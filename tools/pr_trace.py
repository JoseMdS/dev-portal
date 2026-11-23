#!/usr/bin/env python3
"""Spårbarhetskontroll av en PR-beskrivning. Läser PR_BODY, PR_FILES och PREFIX från miljön.

Ger varningar (inte fel), så att arbetet inte stoppas men luckorna syns på PR:en.
"""
import os
import re

body = os.environ.get("PR_BODY", "")
files = [f for f in os.environ.get("PR_FILES", "").split("\n") if f]
issues = re.findall(r"(?i)\b(?:closes|fixes|resolves|stänger)\s+#\d+", body)
krav = re.findall(r"\b[A-Z]{2,5}-KRAV-\d{3}\b", body)
code = [f for f in files if not f.startswith(("docs/", ".github/")) and not f.endswith((".md", "mkdocs.yml"))]
docs = [f for f in files if f.startswith("docs/")]

notes = []
if not issues:
    notes.append("PR:en stänger ingen issue. Lägg till 'Closes #nr' för storyn.")
if not krav:
    notes.append("PR:en nämner inget krav-ID (<P>-KRAV-NNN).")
if code and "docs/lld.md" not in files and "påverkar inte designen" not in body.lower():
    notes.append("Koden ändras men inte docs/lld.md. Uppdatera LLD eller skriv 'påverkar inte designen' i PR:en.")
for n in notes:
    print(f"::warning title=Spårbarhet::{n}")
print(f"pr-trace: {len(issues)} länkade issues, {len(krav)} krav-ID, {len(code)} kodfiler, {len(docs)} docs-filer")
