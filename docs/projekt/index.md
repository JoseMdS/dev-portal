---
status: gällande
ägare: JoseMdS
senast_granskad: 2026-11-23
---

# Projekt

| Projekt | Repo | Prefix | Backstage-system | Dokumentation |
|---|---|---|---|---|
| RaidManagement | [RaidManagement](https://github.com/JoseMdS/RaidManagement) (privat) | `RM` | `raidmanagement` | I repot: [docs/](https://github.com/JoseMdS/RaidManagement/tree/main/docs) och i Backstage |
| Mangos UI | [cmangos-cms](https://github.com/JoseMdS/cmangos-cms) (privat) | `MUI` | `mangos-ui` | I repot: [docs/](https://github.com/JoseMdS/cmangos-cms/tree/server-switch/docs) och i Backstage |
| Forever AddOns – AltVault | [altvault](https://github.com/JoseMdS/altvault) | `AV` | `forever-addons` | [AltVault](altvault/) |
| Forever AddOns – LevelCoach | [LevelCoach](https://github.com/JoseMdS/LevelCoach) | `LC` | `forever-addons` | [LevelCoach](levelcoach/) |

!!! info "Privata repon"
    dev-portal är publikt och därmed även GitHub Pages-sajten. Dokumentationen för de privata repona byggs därför inte in här förrän du väljer det i `projects.yml` (`publish: true`) och lägger in en läs-token som secret `PORTAL_READ_TOKEN`. I Backstage syns alla fyra.

Projektlistan styrs av [`projects.yml`](https://github.com/JoseMdS/dev-portal/blob/main/projects.yml) och Backstage-katalogen av [`catalog/`](https://github.com/JoseMdS/dev-portal/tree/main/catalog).
