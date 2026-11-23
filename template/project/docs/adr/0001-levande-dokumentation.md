---
status: beslutad
ägare: JoseMdS
datum: {{DATUM}}
krav: []
---

# ADR-0001: Levande dokumentation i repot

## Sammanhang
Krav och idéer har hittills funnits i commit-meddelanden, README-filer och samtal med Claude. Det gör det svårt att se varför koden ser ut som den gör, och vad som är kvar att göra.

## Beslut
- Krav, epics och user stories är GitHub Issues med etiketter och sub-issues.
- Design och beslut är Markdown i `docs/` (LLD och ADR fylls i, HLD och SAD är stommar tills de behövs).
- `mkdocs.yml` med `techdocs-core` gör att samma dokument visas på dev-portal (GitHub Pages) och i Backstage.
- Varje PR kontrolleras av det gemensamma workflowet i dev-portal.

## Konsekvenser
- LLD uppdateras i samma PR som koden.
- Lite extra arbete per PR, som Claude-skillarna `lld-update` och `pr-trace` tar det mesta av.

## Alternativ som valdes bort
- Azure DevOps Boards och Wiki: finns inte i det här sammanhanget.
- GitHub Wiki: ligger utanför PR-flödet och kan inte granskas på samma sätt.
