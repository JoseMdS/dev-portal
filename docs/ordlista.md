---
status: gällande
ägare: JoseMdS
senast_granskad: 2026-11-23
---

# Ordlista

Gemensamma begrepp. Projektspecifika begrepp står i respektive projekts `docs/ordlista.md`.

| Begrepp | Betydelse |
|---|---|
| **ADR** | Architecture Decision Record. Ett kort dokument per arkitekturbeslut: sammanhang, beslut, konsekvenser. |
| **Acceptanskriterium** | Testbart villkor som avgör om en user story är klar. |
| **Backstage** | Utvecklarportal med katalog över system, komponenter och ägare. Visar TechDocs. |
| **Baslinje** | Funktioner som fanns innan arbetssättet infördes, inlagda som stängda issues (`baslinje`). |
| **C4** | Modell för arkitekturdiagram i nivåer: kontext, container, komponent, kod. |
| **catalog-info.yaml** | Fil i varje repo som beskriver komponenten för Backstage. |
| **DoD / DoR** | Definition of Done / Ready. Se [DoR och DoD](arbetssatt/dor-dod.md). |
| **Epic** | Större mål som samlar flera krav. Etikett `typ:epic`. |
| **HLD** | High Level Design. Översikt över systemets delar och integrationer. |
| **Krav** | Vad systemet ska göra eller uppfylla. Etikett `typ:krav`, ID `<P>-KRAV-NNN`. |
| **LLD** | Low Level Design. Hur koden är byggd: komponenter, flöden, gränssnitt, data. |
| **MkDocs** | Verktyg som bygger en webbplats av Markdown enligt `mkdocs.yml`. |
| **Playerbots** | cmangos-modul med AI-styrda karaktärer (bottar) som RaidManagement styr. |
| **Prefix** | Kort projektkod först i varje ID, t.ex. `RM`, `MUI`, `AV`, `LC`. |
| **SAD** | Solution Architecture Document. Beslutsunderlag för en lösning. |
| **SavedVariables** | WoW-klientens lagring för addon-data per konto eller karaktär. |
| **Spårbarhet** | Länkar epic → krav → story → ADR/LLD → PR → release. |
| **Sub-issue** | GitHub-funktion för att lägga issues under en förälder. Används för epic → krav → story. |
| **TechDocs** | Backstage-tillägg som visar ett repos MkDocs-dokumentation vid komponenten. |
| **techdocs-core** | MkDocs-plugin som ger samma bygge i Backstage och på vanlig webb. |
| **User story** | "Som … vill jag … så att …" med acceptanskriterier. Etikett `typ:story`. |
