---
status: gällande
ägare: JoseMdS
senast_granskad: 2026-11-23
---

# Nytt projekt

## 1. Kopiera in mallen

```sh
git clone https://github.com/JoseMdS/dev-portal
dev-portal/tools/new-project.sh <sökväg-till-repot> <PREFIX> "<Projektnamn>" <backstage-system> [gren] [typ]
# exempel
dev-portal/tools/new-project.sh ../min-addon MA "Min addon" forever-addons main library
```

Skriptet kopierar `template/project/` (docs/, mkdocs.yml, catalog-info.yaml, issue- och PR-mallar, CI, `.claude/settings.json`, CLAUDE.md) och fyller i namn och prefix. Befintliga filer skrivs inte över; finns redan en CLAUDE.md läggs avsnittet till sist.

## 2. Skapa etiketterna

```sh
dev-portal/tools/labels.sh JoseMdS/<repo>
```

## 3. Registrera i dev-portal

I en PR till dev-portal:

- lägg till repot i `projects.yml` (och `publish: true` om docs ska synas på Pages),
- lägg till en rad i `catalog/all.yaml` och vid behov ett nytt system i `catalog/systems.yaml`,
- lägg till prefixet i [ID-schema](arbetssatt/id-schema.md) och en rad i [Projekt](projekt/index.md).

## 4. Klart

Öppna repot i Claude Code. Det frågar om pluginet (annars: `claude plugin install levande-dokumentation@dev-portal` efter `claude plugin marketplace add JoseMdS/dev-portal`), och sedan fungerar `user-story`, `lld-update`, `adr-new`, `sad-hld-draft` och `pr-trace`. Börja med att be Claude fylla i LLD utifrån koden.
