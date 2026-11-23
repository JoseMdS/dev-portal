# dev-portal

Central plats för levande dokumentation: MkDocs-sajten (`docs/`), Backstage-katalogen (`catalog/`), Claude-pluginet `levande-dokumentation` (`plugins/`), projektmallen (`template/project/`) och den gemensamma CI:n (`.github/workflows/docs-check.yml`). Skriv på svenska.

- Ändringar i `template/project/` påverkar nya projekt. Befintliga projektrepon uppdateras med egna PR:er.
- Ändringar i `docs-check.yml` eller `tools/` påverkar alla projektrepons CI direkt (de anropar `@main`). Testa med `mkdocs build --strict` och `python tools/check_docs.py docs` innan merge.
- Ändras en skill i `plugins/levande-dokumentation/skills/`, höj `version` i `plugin.json` och `marketplace.json`.
- Nytt projekt: `tools/new-project.sh`, sedan `projects.yml`, `catalog/all.yaml` och `docs/arbetssatt/id-schema.md`.
- dev-portal är publikt. Lägg inget hemligt här, och publicera inte privata repons docs utan att ägaren valt det i `projects.yml`.
- ID-prefix för dev-portal själv: `DP`.
