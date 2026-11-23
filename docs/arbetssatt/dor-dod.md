---
status: gällande
ägare: JoseMdS
senast_granskad: 2026-11-23
---

# Definition of Ready och Definition of Done

## Ready (en story kan påbörjas)

- [ ] Storyn har formen "Som … vill jag … så att …"
- [ ] Den har minst ett testbart acceptanskriterium
- [ ] Den är sub-issue till ett krav (`typ:krav`)
- [ ] Öppna vägval är antingen beslutade eller har en ADR med status `föreslagen`

## Done (en story är klar)

- [ ] Acceptanskriterierna är uppfyllda och avbockade
- [ ] Tester finns eller är uppdaterade, och CI är grön
- [ ] `docs/lld.md` stämmer med koden
- [ ] Ny ADR om ett vägval gjordes
- [ ] PR:en har `Closes #nr` och kravets ID
- [ ] README eller användarinstruktion är uppdaterad om beteendet ändrats
