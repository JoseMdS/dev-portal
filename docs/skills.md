---
status: gällande
ägare: JoseMdS
senast_granskad: 2026-11-23
---

# Claude-skills

Skillarna ligger centralt i dev-portal som Claude Code-pluginet **levande-dokumentation** (`plugins/levande-dokumentation/`). Ett repo slår på det med `.claude/settings.json`:

```json
--8<-- "template/project/.claude/settings.json"
```

Claude Code frågar första gången om du litar på marknadsplatsen `dev-portal`. Kommer ingen fråga, installera från terminalen (en gång per dator):

```sh
claude plugin marketplace add JoseMdS/dev-portal
claude plugin install levande-dokumentation@dev-portal
claude plugin list        # ska visa levande-dokumentation@dev-portal som enabled
```

Därefter finns skillarna i alla repon som har filen. Uppdateringar i dev-portal når alla repon (`/plugin marketplace update dev-portal`).

| Skill | Gör | Typisk fras |
|---|---|---|
| `user-story` | Gör om en idé till krav och user stories med acceptanskriterier, nästa lediga ID och sub-issue-koppling | "lägg in det här som en story" |
| `lld-update` | Uppdaterar `docs/lld.md` utifrån en ändring eller PR, inklusive spårbarhetstabellen | "uppdatera LLD" |
| `adr-new` | Skapar nästa numrerade ADR, länkad till krav och story, och uppdaterar ADR-index | "skriv en ADR för valet av …" |
| `sad-hld-draft` | Första utkast av SAD eller HLD från repot, LLD och kraven | "projektet har växt, gör en HLD" |
| `pr-trace` | Kontrollerar att en PR länkar story, krav, LLD och ADR, och fyller i det som saknas | "kolla spårbarheten i PR:en" |

Samma kontroll som `pr-trace` gör finns också i CI, som varning på varje PR.
