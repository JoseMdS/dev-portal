---
name: sad-hld-draft
description: Gör ett första utkast av docs/hld.md eller docs/sad.md från koden, LLD, ADR:er och kraven när ett projekt har växt. Använd bara när användaren ber om HLD eller SAD, eller frågar om projektet behöver en.
---

# sad-hld-draft

HLD och SAD är stommar i varje repo. Den här skillen fyller i dem när det behövs. Se https://josemds.github.io/dev-portal/arbetssatt/dokumentniva/.

## Avgör först
- **HLD** behövs när systemet har flera delar eller integrationer som behöver en översikt.
- **SAD** behövs när lösningen ska beslutas av någon annan, eller har krav på drift, säkerhet eller kostnad.
Säg vad du rekommenderar innan du skriver.

## Steg för HLD
1. Läs `README`, `docs/lld.md`, `docs/adr/`, `catalog-info.yaml` och öppna krav (`gh issue list --label typ:krav`).
2. Fyll i stommens rubriker:
   - Översikt (C4 nivå 1): Mermaid-diagram med användare, systemet och externa system.
   - Containrar (C4 nivå 2): körbara delar, hur de kommunicerar, var de körs.
   - Integrationer: en rad per integration med ID `INT-01`, `INT-02` …, riktning, protokoll, format.
   - Icke-funktionella krav: prestanda, säkerhet, drift. Hänvisa till krav-ID.
   - Beslut: länka ADR:erna.
3. Hänvisa till LLD för detaljer i stället för att upprepa dem.

## Steg för SAD
1. Samma underlag som HLD, plus det användaren berättar om mål och intressenter.
2. Fyll i: bakgrund och mål, krav i sammandrag (länka issues), lösningsöversikt (hänvisa till HLD), alternativ i beslutstabeller `AB01`, `AB02` … (alternativ, för- och nackdelar, rekommendation), säkerhet och drift, risker och öppna frågor.

## Båda
- Sätt `status: utkast` och dagens datum i metadata, och ta bort "Stomme"-rutan.
- Kontrollera med `mkdocs build --strict`.
- Markera antaganden tydligt med "Antagande:" så att användaren kan rätta dem.
