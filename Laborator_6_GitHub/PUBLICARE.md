# Finalizarea publicării

Raportul de predare este `L6_TP_Colta_Iulian_SI-265.md`. Acest fișier explică publicarea și nu face parte din textul raportului.

După restabilirea accesului la GitHub:

```sh
cd /Users/mac/Desktop/TP
gh auth login --hostname github.com --git-protocol https --web
python3 Laborator_6_GitHub/publicare.py --publica
```

Programul verifică autentificarea în contul `IulIan10021`, apoi:

1. Recuperează istoriile originale din fișierele bundle și publică `exercitiu-git` și `exercitiu-2` ca depozite publice.
2. Verifică fișierele și numărul minim de commituri. Actualizează README pe GitHub prin API, preia schimbarea cu pull și verifică clonarea de pe GitHub.
3. Redenumește depozitul disciplinei `TP` în `TP_Colta_Iulian_SI-265`, îl configurează privat și acordă profesorului `cristiangonceari-dotcom` acces de citire. Dacă profesorul nu a acceptat invitația, accesul rămâne în așteptare.
4. Actualizează linkul în raportul Markdown și în documentul Word principal, salvează modificările și trimite ramura curentă. Verifică identificatorul commitului publicat și prezența raportului online.
5. Generează `/tmp/L6_TP_Colta_Iulian_SI-265_DRAFT.eml`, cu destinatarul, subiectul, linkul și identificatorul real al ultimului commit. E-mailul trebuie trimis din aplicația de poștă după verificarea accesului profesorului.

Istoriile nu sunt rescrise. Dacă un depozit conține un istoric incompatibil, operația se oprește pentru verificare. Modificările online deja reușite se păstrează dacă un pas ulterior eșuează.

La susținere trebuie explicate comenzile și commiturile realizate. Fișa originală cere și declararea surselor sau a ajutorului primit.
