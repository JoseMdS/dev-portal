---
name: user-story
description: Gör om en idé eller ett önskemål till krav och user stories som GitHub Issues med acceptanskriterier, nästa lediga ID och sub-issue-koppling. Använd när användaren beskriver en ny funktion, idé, ändring eller bugg som ska in i backloggen.
---

# user-story

Gör om en idé till spårbara issues enligt dev-portal (https://josemds.github.io/dev-portal/arbetssatt/).

## Steg

1. **Läs sammanhanget.** Hitta repots prefix i `CLAUDE.md` (t.ex. `RM`). Läs `docs/lld.md` så att storyn använder rätt begrepp.
2. **Hitta föräldern.** Lista öppna epics och krav:
   `gh issue list --label typ:epic --state all --limit 100` och `gh issue list --label typ:krav --state all --limit 200`.
   Passar idén under ett befintligt krav, lägg bara till stories. Annars skapa ett nytt krav under rätt epic (eller föreslå en ny epic).
3. **Nästa lediga ID.** Ta det högsta numret i titlarna (`[<P>-KRAV-NNN]`, `[<P>-US-NNN]`) och lägg till ett.
4. **Skriv issues** på svenska, i formen från issue-mallarna:
   - Krav: titel `[<P>-KRAV-NNN] <vad systemet ska göra>`, brödtext med `**<P>-KRAV-NNN** · Epic: #nr`, kravet, källa och en spårbarhetssektion.
   - Story: titel `[<P>-US-NNN] Som <roll> vill jag <förmåga>`, brödtext med `Som … vill jag … så att …`, 2–5 **testbara** acceptanskriterier som `- [ ]` och Definition of Done.
   - Etiketter `typ:krav` respektive `typ:story`.
5. **Visa först.** Visa titlar och acceptanskriterier för användaren och vänta på ok innan du skapar något.
6. **Skapa och koppla.** `gh issue create`, sedan sub-issue-koppling:
   `gh api -X POST repos/{owner}/{repo}/issues/<förälder-nr>/sub_issues -F sub_issue_id=<barnets id>` (id, inte nummer: `gh api repos/{owner}/{repo}/issues/<nr> --jq .id`).
7. **Svara** med länkar till de nya issues.

## Regler
- Ett acceptanskriterium ska gå att pröva (i test, i spelet eller i webbläsaren). Skriv inte "fungerar bra".
- Behåll användarens egna ord i storyn där det går.
- Skapa aldrig dubbletter: sök på nyckelord först (`gh issue list --search`).
