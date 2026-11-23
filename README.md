# dev-portal

Central plats för levande dokumentation i Josés projekt. Här finns:

| Del | Var | Vad |
|---|---|---|
| Dokumentationssajt | `mkdocs.yml`, `docs/` | Arbetssätt, mallar, ordlista och projektöversikt. Publiceras på GitHub Pages tillsammans med projektens egna `docs/`. |
| Backstage-katalog | `catalog/` | Domän, system, komponenter och ägare. Varje projektrepo har sin egen `catalog-info.yaml` som katalogen pekar på. |
| Backstage-konfiguration | `backstage/` | Konfiguration för en Backstage-app som läser katalogen och visar TechDocs. |
| Claude-skills | `plugins/levande-dokumentation/` | Claude Code-plugin med `lld-update`, `adr-new`, `user-story`, `sad-hld-draft` och `pr-trace`. |
| Projektmall | `template/project/` | Allt ett nytt repo behöver. Kopieras in med `tools/new-project.sh`. |
| Gemensam CI | `.github/workflows/docs-check.yml` | Återanvändbart workflow som projektrepona anropar på varje PR. |

## Snabbstart

```sh
python3 -m venv .venv && . .venv/bin/activate
pip install -r tools/requirements-docs.txt
mkdocs serve            # http://127.0.0.1:8000
```

Ett projekts dokumentation förhandsgranskas på samma sätt i projektets repo (`mkdocs serve`).

## Nytt projekt

Se [docs/nytt-projekt.md](docs/nytt-projekt.md). Kort version:

```sh
tools/new-project.sh ../mitt-repo MITT "Mitt projekt" mitt-system
```

## Projekt

| Projekt | Repo | Backstage-system |
|---|---|---|
| RaidManagement | [JoseMdS/RaidManagement](https://github.com/JoseMdS/RaidManagement) | `raidmanagement` |
| Mangos UI | [JoseMdS/cmangos-cms](https://github.com/JoseMdS/cmangos-cms) | `mangos-ui` |
| Forever AddOns | [JoseMdS/altvault](https://github.com/JoseMdS/altvault), [JoseMdS/LevelCoach](https://github.com/JoseMdS/LevelCoach) | `forever-addons` |
