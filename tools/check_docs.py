#!/usr/bin/env python3
"""Kontrollerar metadata i docs/: status, ägare, datum och ID-format.

Användning: python3 check_docs.py [docs-katalog]
Avslutar med kod 1 om något fel hittas. Varningar stoppar inte bygget.
"""
import pathlib
import re
import sys

import yaml

DOC_STATUS = {"utkast", "granskad", "gällande", "ersatt"}
ADR_STATUS = {"föreslagen", "beslutad", "ersatt", "avvisad"}
KRAV_RE = re.compile(r"^[A-Z]{2,5}-KRAV-\d{3}$")
ADR_RE = re.compile(r"^ADR-\d{4}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ADR_FILE_RE = re.compile(r"^\d{4}-[a-z0-9-]+\.md$")


def front_matter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end < 0:
        return None
    return yaml.safe_load(text[4:end]) or {}


def main(root):
    root = pathlib.Path(root)
    errors, warnings = [], []
    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root)
        meta = front_matter(path.read_text(encoding="utf-8"))
        if meta is None:
            errors.append(f"{rel}: saknar metadata (--- status/ägare/senast_granskad ---)")
            continue
        is_adr = rel.parts[0] == "adr" and rel.name != "index.md"
        if is_adr and not ADR_FILE_RE.match(rel.name):
            errors.append(f"{rel}: ADR-filer heter NNNN-kort-namn.md")
        allowed = ADR_STATUS if is_adr else DOC_STATUS
        if meta.get("status") not in allowed:
            errors.append(f"{rel}: status '{meta.get('status')}' ska vara en av {sorted(allowed)}")
        if not meta.get("ägare"):
            errors.append(f"{rel}: ägare saknas")
        date_key = "datum" if is_adr else "senast_granskad"
        date = str(meta.get(date_key, ""))
        if not DATE_RE.match(date):
            errors.append(f"{rel}: {date_key} ska vara ÅÅÅÅ-MM-DD")
        for k in meta.get("krav") or []:
            if not KRAV_RE.match(str(k)):
                errors.append(f"{rel}: kravet '{k}' följer inte <P>-KRAV-NNN")
        for b in (meta.get("beslut") or []) + (meta.get("ersätter") or []):
            if not ADR_RE.match(str(b)):
                errors.append(f"{rel}: beslutet '{b}' följer inte ADR-NNNN")
        if str(rel) == "lld.md" and not meta.get("krav"):
            warnings.append(f"{rel}: LLD hänvisar inte till några krav (krav: [...])")
    for w in warnings:
        print(f"::warning::{w}")
    for e in errors:
        print(f"::error::{e}")
    print(f"check_docs: {len(errors)} fel, {len(warnings)} varningar")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "docs"))
