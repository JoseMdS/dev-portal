#!/bin/sh
# Kopierar projektmallen till ett repo och fyller i namn och prefix.
# användning: tools/new-project.sh <repo-katalog> <PREFIX> "<Projektnamn>" <backstage-system> [gren=main] [typ=library]
set -e
dest="$1"; prefix="$2"; name="$3"; system="$4"; branch="${5:-main}"; type="${6:-library}"
[ -d "$dest" ] && [ -n "$prefix" ] && [ -n "$name" ] && [ -n "$system" ] || {
  echo "användning: $0 <repo-katalog> <PREFIX> \"<Projektnamn>\" <backstage-system> [gren] [typ]"; exit 1; }
tpl="$(cd "$(dirname "$0")/../template/project" && pwd)"
dest="$(cd "$dest" && pwd)"
# Reponamnet tas från origin (rätt versaler), annars från katalognamnet.
repo="$(git -C "$dest" remote get-url origin 2>/dev/null | sed -e 's|.*/||' -e 's|\.git$||')"
[ -n "$repo" ] || repo="$(basename "$dest")"
component="$(echo "$repo" | tr '[:upper:]' '[:lower:]')"
today="$(date +%Y-%m-%d)"
fill() {
  sed -e "s|{{PROJEKT}}|$name|g" -e "s|{{PREFIX}}|$prefix|g" -e "s|{{REPO}}|$repo|g" \
      -e "s|{{SYSTEM}}|$system|g" -e "s|{{KOMPONENT}}|$component|g" -e "s|{{GREN}}|$branch|g" \
      -e "s|{{TYP}}|$type|g" -e "s|{{DATUM}}|$today|g" -e "s|{{TAGGAR}}||g" \
      -e "s|{{BESKRIVNING}}|$name|g" "$1"
}
cd "$tpl"
find . -type f | while read -r f; do
  target="$dest/${f#./}"
  mkdir -p "$(dirname "$target")"
  if [ "${f#./}" = "CLAUDE.md" ] && [ -f "$target" ]; then
    printf '\n' >> "$target"; fill "$f" | sed '1,2d' >> "$target"; echo "la till avsnitt i CLAUDE.md"
  elif [ -e "$target" ]; then
    echo "finns redan, hoppar över: ${f#./}"
  else
    fill "$f" > "$target"; echo "skapade ${f#./}"
  fi
done
echo "Klart. Kör tools/labels.sh JoseMdS/$repo och registrera repot i dev-portal (se docs/nytt-projekt.md)."
