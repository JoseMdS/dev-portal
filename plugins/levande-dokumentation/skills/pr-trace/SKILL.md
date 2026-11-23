---
name: pr-trace
description: Kontrollerar och kompletterar spårbarheten i en pull request (story via Closes #nr, krav-ID, LLD, ADR, test) och fyller i PR-mallen. Använd innan en PR öppnas, när användaren ber om att kolla en PR, eller när CI-varningen Spårbarhet visas.
---

# pr-trace

Samma kontroll som `tools/pr_trace.py` i dev-portal gör i CI, men som rättar i stället för att bara varna.

## Steg

1. **Hitta PR:en.** `gh pr view <nr> --json number,title,body,files,headRefName` eller den aktuella branchens PR.
2. **Kontrollera:**
   - [ ] `Closes #nr` för minst en story (eller bugg). Finns ingen, sök efter rätt story (`gh issue list --label typ:story --search <nyckelord>`) eller föreslå skillen `user-story`.
   - [ ] Kravets ID (`<P>-KRAV-NNN`) står i beskrivningen. Hämta det från storyns brödtext (`Krav: #nr`).
   - [ ] Ändras kod: `docs/lld.md` är ändrad, eller beskrivningen säger "påverkar inte designen". Om LLD borde ha ändrats, kör skillen `lld-update`.
   - [ ] Görs ett vägval: en ny ADR finns (skillen `adr-new`).
   - [ ] Testsektionen säger hur det är testat.
3. **Fyll i PR-mallen** (`.github/pull_request_template.md`) med det som saknas och uppdatera beskrivningen med `gh pr edit <nr> --body-file -`. Visa ändringen för användaren först.
4. **Rapportera** kort: vad som var på plats, vad du lade till, och vad användaren själv behöver avgöra.

## Regler
- Ändra aldrig en annans PR utan att användaren bett om det.
- Hitta inte på issue-nummer eller krav-ID.
