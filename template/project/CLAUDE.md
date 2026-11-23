# {{PROJEKT}}

## Levande dokumentation
Det här repot följer arbetssättet i [dev-portal](https://github.com/JoseMdS/dev-portal) ([sajt](https://josemds.github.io/dev-portal/)).

- Krav, epics och user stories är GitHub Issues (`typ:epic`, `typ:krav`, `typ:story`), kopplade som sub-issues. ID-prefix: `{{PREFIX}}` (t.ex. `{{PREFIX}}-KRAV-012`).
- `docs/lld.md` beskriver hur koden är byggd. **Uppdatera LLD i samma PR som en ändring som påverkar designen.**
- Vägval blir en ADR i `docs/adr/NNNN-kort-namn.md`.
- HLD och SAD är stommar. Fyll inte i dem om du inte blir ombedd.
- Varje sida i `docs/` har metadata (`status`, `ägare`, `senast_granskad`, ev. `krav`, `beslut`).
- PR-beskrivningen följer `.github/pull_request_template.md`: `Closes #nr`, kravets ID, ev. ADR.
- Kontrollera dokumentationen lokalt med `mkdocs build --strict` (`pip install -r https://raw.githubusercontent.com/JoseMdS/dev-portal/main/tools/requirements-docs.txt`).

## Skills
Pluginet `levande-dokumentation` från dev-portal slås på i `.claude/settings.json`:
`lld-update`, `adr-new`, `user-story`, `sad-hld-draft`, `pr-trace`.
