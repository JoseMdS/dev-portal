---
status: gällande
ägare: JoseMdS
senast_granskad: 2026-11-23
---

# Hur mycket ska dokumenteras?

Strukturen finns i varje repo, men bara det som behövs fylls i.

| Dokument | När det fylls i | I dagens projekt |
|---|---|---|
| **LLD** | Alltid. Beskriver hur koden är byggd så att den kan ändras säkert. | Ifylld |
| **ADR** | När ett vägval görs som någon senare kan undra över. | En eller ett par per repo |
| **HLD** | När systemet har flera delar eller integrationer som behöver en översikt (C4 nivå 2). | Stomme |
| **SAD** | När lösningen ska beslutas av någon annan än du, eller får krav på drift, säkerhet eller kostnad. | Stomme |
| **Krav** | Som issues. `docs/krav.md` länkar bara till dem. | Issues |
| **Ordlista** | Begrepp som är specifika för projektet. Gemensamma begrepp står i den [centrala ordlistan](../ordlista.md). | Kort |

Tumregel: om en ändring i koden gör att LLD blir fel, uppdatera LLD i samma PR. Allt annat är frivilligt tills projektet växer. Skillen `sad-hld-draft` gör ett första utkast den dag det behövs.
