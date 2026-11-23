---
status: gällande
ägare: JoseMdS
senast_granskad: 2026-11-23
---

# ID-schema och etiketter

## Prefix per projekt

| Projekt | Repo | Prefix |
|---|---|---|
| RaidManagement | RaidManagement | `RM` |
| Mangos UI | cmangos-cms | `MUI` |
| Forever AddOns | altvault | `AV` |
| Forever AddOns | LevelCoach | `LC` |

Nya projekt väljer ett kort prefix i versaler och lägger till det här.

## ID:n

| Typ | Format | Exempel | Var |
|---|---|---|---|
| Epic | `<P>-EPIC-NN` | `RM-EPIC-02` | Issue-titel |
| Krav | `<P>-KRAV-NNN` | `MUI-KRAV-017` | Issue-titel, dokumentens `krav:` |
| User story | `<P>-US-NNN` | `LC-US-003` | Issue-titel |
| Beslut | `ADR-NNNN` | `ADR-0002` | Filnamn `docs/adr/0002-kort-namn.md` |

Numren räknas per repo. Nästa lediga nummer hittas med sökning på titeln, eller med skillen `user-story` som gör det åt dig.

## Etiketter

| Etikett | Betydelse |
|---|---|
| `typ:epic` | Större mål, samlar krav |
| `typ:krav` | Krav som spåras till dokument och PR |
| `typ:story` | User story med acceptanskriterier |
| `typ:bugg` | Fel i levererad funktion |
| `typ:adr` | Ett beslut som behöver tas |
| `baslinje` | Redan levererat, inlagt i efterhand |

## Metadata i dokument

Varje sida i `docs/` börjar med:

```yaml
---
status: utkast | granskad | gällande | ersatt
ägare: <GitHub-login>
senast_granskad: ÅÅÅÅ-MM-DD
krav: [RM-KRAV-008]          # valfritt
beslut: [ADR-0002]           # valfritt
---
```

ADR:er har `status: föreslagen | beslutad | ersatt | avvisad`. `tools/check_docs.py` kontrollerar detta i CI.
