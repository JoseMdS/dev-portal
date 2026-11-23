---
status: gällande
ägare: JoseMdS
senast_granskad: 2026-11-23
---

# Arbetssätt

GitHub är basen för allt:

| Behov | Verktyg |
|---|---|
| Krav, epics, user stories, buggar | GitHub Issues med issue-mallar och etiketter, kopplade som sub-issues |
| Planering | GitHub Projects (valfritt), med vyer per etikett |
| Kod och dokument | Git-repo per projekt, `docs/` + `mkdocs.yml` |
| Granskning | Pull request med PR-mall |
| Kontroll | GitHub Actions: bygge, tester, `mkdocs build --strict`, metadata och spårbarhet |
| Publicering | GitHub Pages (dev-portal) och Backstage TechDocs |
| AI-stöd | Claude Code med skills från [dev-portal-pluginet](../skills.md) |

## Kort om flödet

1. En idé blir ett **krav** (issue med etiketten `typ:krav`) under en **epic**.
2. Kravet bryts ner i **user stories** med acceptanskriterier.
3. Ett beslut som påverkar designen blir en **ADR** i `docs/adr/`.
4. Koden och **LLD** uppdateras i samma PR. PR:en länkar till storyn med `Closes #nr`.
5. CI kontrollerar att dokumenten bygger och att PR:en är spårbar.
6. Efter merge publiceras dokumentationen och releasen får ändringslogg från PR:erna.

Läs mer under [Spårbarhet](sparbarhet.md) och [Från idé till release](flode.md).
