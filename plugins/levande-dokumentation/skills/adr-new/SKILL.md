---
name: adr-new
description: Skapar nästa numrerade arkitekturbeslut (ADR) i docs/adr/, länkat till krav och story, och uppdaterar ADR-index och LLD. Använd när ett vägval görs eller diskuteras, till exempel val av bibliotek, lagring, protokoll eller struktur.
---

# adr-new

Skapar ett ADR enligt mallen i dev-portal (https://josemds.github.io/dev-portal/mallar/adr/).

## Steg

1. **Nästa nummer.** `ls docs/adr/` och ta det högsta `NNNN` plus ett. Filnamn: `docs/adr/NNNN-kort-namn-med-bindestreck.md` (gemener, a–z, siffror).
2. **Samla underlag.** Fråga efter eller hitta: problemet, alternativen, vad som avgör, och vilket krav (`<P>-KRAV-NNN`) och vilken story det gäller.
3. **Skriv ADR:en** på svenska med metadata:
   ```yaml
   ---
   status: föreslagen        # beslutad när användaren har sagt ja
   ägare: <GitHub-login>
   datum: ÅÅÅÅ-MM-DD
   krav: [<P>-KRAV-NNN]
   ersätter: []
   ---
   ```
   Rubriker: `# ADR-NNNN: <beslut i en mening>`, Sammanhang, Beslut, Konsekvenser, Alternativ som valdes bort.
4. **Ersätter den ett äldre beslut**, sätt det äldres `status: ersatt` och fyll i `ersätter: [ADR-XXXX]` i det nya.
5. **Uppdatera** tabellen i `docs/adr/index.md`, `nav` i `mkdocs.yml`, och `beslut:` i `docs/lld.md` om beslutet påverkar designen.
6. **Kontrollera** med `mkdocs build --strict`.
7. **Status.** Lämna `föreslagen` tills användaren har bekräftat beslutet. Sätt då `beslutad`.

## Regler
- Ett beslut per ADR. Kort: en skärmsida räcker nästan alltid.
- Skriv alternativen ärligt, med varför de valdes bort.
