#!/bin/sh
# Skapar etiketterna för arbetssättet i ett repo: tools/labels.sh JoseMdS/<repo>
set -e
repo="$1"; [ -n "$repo" ] || { echo "användning: $0 ägare/repo"; exit 1; }
mk() { gh api -X POST "repos/$repo/labels" -f name="$1" -f color="$2" -f description="$3" >/dev/null 2>&1 && echo "skapade $1" || echo "finns redan: $1"; }
mk "typ:epic"  5319e7 "Epic: ett större mål som samlar krav"
mk "typ:krav"  0e8a16 "Krav (KRAV-xxx) som spåras till LLD, ADR och PR"
mk "typ:story" 1d76db "User story med acceptanskriterier"
mk "typ:bugg"  d73a4a "Fel i levererad funktion"
mk "typ:adr"   fbca04 "Arkitekturbeslut som behöver tas"
mk "baslinje"  c5def5 "Redan levererat, inlagt i efterhand för spårbarhet"
