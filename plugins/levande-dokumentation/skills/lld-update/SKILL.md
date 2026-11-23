---
name: lld-update
description: Uppdaterar docs/lld.md så att den stämmer med koden efter en ändring, branch eller PR, inklusive spårbarhetstabellen krav → kod → test. Använd när koden har ändrats, när användaren ber om att uppdatera LLD, eller innan en PR som ändrar designen öppnas.
---

# lld-update

Håller `docs/lld.md` levande enligt mallen i dev-portal (https://josemds.github.io/dev-portal/mallar/lld/).

## Steg

1. **Ta reda på ändringen.** `git diff --stat origin/<standardgren>...HEAD` och läs de ändrade filerna. Gäller det en PR: `gh pr diff <nr>`.
2. **Läs LLD.** Läs hela `docs/lld.md`. Saknas den, kopiera mallen från dev-portal (`template/project/docs/lld.md`).
3. **Avgör vad som påverkas**, avsnitt för avsnitt:
   - 2 Komponenter och filer: nya, borttagna eller flyttade filer och moduler.
   - 3 Flöden: ändrad ordning, nya steg (uppdatera Mermaid-diagrammet).
   - 4 Gränssnitt: kommandon, endpoints, protokoll, konfiguration.
   - 5 Data: SavedVariables, tabeller, fält, standardvärden.
   - 6 Test: nya eller ändrade tester och hur de körs.
   - 7 Kända begränsningar: lägg till eller ta bort, med länk till issue.
   - 8 Spårbarhet: en rad per krav som ändringen rör (krav-ID, fil/funktion, test).
4. **Skriv kort och sakligt.** Beskriv hur det är, inte historiken. Ändra bara det som påverkas.
5. **Metadata.** Sätt `senast_granskad` till dagens datum och lägg till nya krav-ID i `krav:` och ADR:er i `beslut:`.
6. **Kontrollera.** `mkdocs build --strict` och, om dev-portal finns lokalt, `python <dev-portal>/tools/check_docs.py docs`.
7. **Berätta** vilka avsnitt som ändrades. Påverkas inte designen, säg det och föreslå texten "påverkar inte designen" i PR:en.

## Regler
- Fyll inte i HLD eller SAD här. De är stommar tills användaren ber om dem.
- Hitta inte på krav-ID. Saknas ett krav för ändringen, föreslå skillen `user-story`.
