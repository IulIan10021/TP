# Laboratorul 6 — GitHub, pas cu pas

## DATELE STUDENTULUI

Student: Colta Iulian
Grupa: SI-265
Username GitHub: IulIan10021
Tema: GitHub, pas cu pas

## LINKURILE DE PREDARE

Depozitul disciplinei: https://github.com/IulIan10021/TP
Primul depozit de exercițiu: https://github.com/IulIan10021/exercitiu-git
Al doilea depozit de exercițiu: https://github.com/IulIan10021/exercitiu-2
Acestea sunt adresele destinate predării; existența și vizibilitatea online nu au fost confirmate.

## A1. CONTUL GITHUB

Am utilizat username-ul existent IulIan10021. Verificarea curentă cu gh auth status indică autentificare invalidă. Pentru continuarea online trebuie refăcută autentificarea.
Comandă: gh auth login -h github.com

## A2. CONFIGURAREA GIT

Am verificat Git și identitatea disponibilă. Exercițiile folosesc identitatea locală Colta Iulian și adresa noreply a contului. Configurarea identității stabilește autorul commit-urilor; autentificarea GitHub se face separat.
Comenzi:
git --version
git config user.name "Colta Iulian"
git config user.email "134854600+IulIan10021@users.noreply.github.com"
git config init.defaultBranch main
git config pull.rebase false
git config --local --list

## A3. PRIMUL DEPOZIT

Am pregătit un depozit de exercițiu cu README.md. Pentru cerința online se creează pe GitHub depozitul Public exercitiu-git. În demonstrația locală s-a folosit un origin bare local; acesta nu confirmă crearea unui depozit public.

## A4. CLONAREA

Am clonat depozitul local și am verificat fișierele. Pentru un depozit public, comenzile corespunzătoare sunt:
git clone https://github.com/IulIan10021/exercitiu-git.git
cd exercitiu-git
ls
Clonarea copiază fișierele și istoricul Git.

## A5. STATUS, ADD ȘI COMMIT

Am creat și rulat salut.py, apoi am salvat fișierul prin add și commit.
Codul programului:
print("Salut, GitHub!")
Comenzi:
python3 salut.py
git status
git add salut.py
git commit -m "Adaug salut.py"
Rezultat Python: Salut, GitHub!
Status arată modificările; add le pregătește; commit salvează versiunea locală.

## A6. PUSH

Am exersat trimiterea commit-urilor către origin local. Pentru GitHub se folosește git push după autentificare și configurarea adresei origin. Publicarea online nu este confirmată.
Comandă: git push

## A7. PULL

Am adus o modificare a README.md dintr-o a doua copie locală prin origin comun. Aceasta demonstrează sincronizarea locală. Pasul cerut în browser presupune editarea README.md pe GitHub, adăugarea rândului „Aici exersez git.” și preluarea modificării.
Comenzi:
git pull
cat README.md

## A8. FIȘIERUL .GITIGNORE

Am creat mediul virtual și regulile de ignorare. Fișierul .gitignore conține:
.venv/
__pycache__/
Comenzi:
python3 -m venv .venv
git status --short
git check-ignore .venv/
git add .gitignore
git commit -m "Ignor mediul virtual"
git push
Mediul virtual și cache-ul Python nu se includ în istoric.

## A9. LOG, DIFF ȘI RESTORE

Am verificat istoricul cu patru commit-uri. Am adăugat temporar print("al doilea"), am verificat diferența și am revenit la versiunea salvată.
Comenzi:
git log --oneline
git diff
git restore salut.py
git status
Restore elimină modificările nesalvate ale fișierului indicat.

## A10. AL DOILEA DEPOZIT

Am inițializat local exercitiu-2, am adăugat README.md cu titlul „Al doilea depozit” și am creat primul commit. Am exersat push -u către origin local. Pentru publicare se creează un depozit GitHub Public gol, fără README generat online.
Comenzi pentru un proiect nou:
mkdir exercitiu-2
cd exercitiu-2
git init -b main
# Creează README.md în editor înainte de comanda următoare.
git add README.md
git commit -m "Primul commit"
git remote add origin https://github.com/IulIan10021/exercitiu-2.git
git push -u origin main
Opțiunea -u configurează urmărirea ramurii remote.

## A11. VERIFICAREA FINALĂ

De verificat în browser după publicare:
1. exercitiu-git este Public și conține README.md, salut.py și .gitignore.
2. Istoricul exercitiu-git are minimum patru commit-uri clare.
3. exercitiu-2 este Public și conține README.md.
4. Depozitul disciplinei este Private și profesorul cristiangonceari-dotcom are acces.
5. Raportul Markdown este prezent în folderul Laborator_6_GitHub.
6. Ultimul commit al predării este vizibil pe GitHub.
Verificările online rămân de realizat.

## A12. ERORI ȘI REZOLVĂRI

fatal: not a git repository — intră în folderul corect.
Author identity unknown — configurează user.name și user.email.
nothing to commit — nu există modificări noi de salvat.
untracked files — folosește git add pentru fișierele necesare.
fetch first — preia schimbările prin git pull și rezolvă eventualele conflicte înainte de push.
403 / Permission denied — verifică autentificarea și drepturile de acces.
Could not resolve host — verifică accesul la rețea și DNS.
LF will be replaced by CRLF — avertisment despre terminatorii de linie.

## STRUCTURA ȘI DENUMIREA PREDĂRII

Fișa cere depozitul privat TP_Nume_Prenume_Grupa; pentru student: TP_Colta_Iulian_SI-265. Depozitul existent identificat este TP; denumirea lui trebuie verificată față de cerința profesorului.
În depozitul privat se pune:
Laborator_6_GitHub/L6_TP_Colta_Iulian_SI-265.md
Documentul Word însoțește raportul, iar fișierul Markdown este livrabilul cerut explicit.
Nu se publică token-uri, parole sau chei API.

## PUBLICAREA ISTORIILOR EXISTENTE

Pentru copiile locale deja realizate nu se repetă inițializarea și commit-urile. După autentificare se creează pe GitHub două depozite publice goale, apoi se execută:
cd /Users/mac/Desktop/L6_exercitii_locale/exercitiu-git
git remote set-url origin https://github.com/IulIan10021/exercitiu-git.git
git push -u origin main
cd /Users/mac/Desktop/L6_exercitii_locale/exercitiu-2
git remote set-url origin https://github.com/IulIan10021/exercitiu-2.git
git push -u origin main
Aceste comenzi sunt instrucțiuni pentru finalizare; nu reprezintă confirmarea publicării.

## E-MAILUL CERUT DUPĂ PREDARE

Destinatar: cristian.gonceari@isa.utm.md
Subiect: L6_TP_Colta_Iulian_SI-265
Text propus:
Bună ziua,
Sunt Colta Iulian, grupa SI-265. Vă transmit laboratorul 6.
Depozitul privat: [linkul verificat al depozitului disciplinei]
Ultimul commit: [codul obținut prin git rev-parse HEAD după push]
Vă mulțumesc.
E-mailul este doar pregătit; nu a fost trimis.

## CONCLUZII ȘI STAREA REALIZĂRII

Am exersat local configurarea Git, clonarea, salvarea versiunilor, transferul între copii, ignorarea fișierelor, citirea istoricului și anularea modificărilor. Primul depozit are patru commit-uri, iar al doilea are un commit. Pentru îndeplinirea integrală mai sunt necesare autentificarea GitHub, publicarea depozitelor, verificarea accesului profesorului, push-ul predării și e-mailul final. Nota nu poate fi confirmată înaintea acestor verificări.

## SURSE

Fișa L6_Laborator_GitHub_pas_cu_pas.docx și documentul Word existent. Imaginile din partea inițială sunt redări ale transcrierilor de terminal, nu capturi ale depozitelor publicate pe GitHub.

## DESCHIDEREA RAPORTULUI ÎN TERMINAL

Fișierul Markdown este un document, nu un program executabil. Pentru citire:

```sh
cd /Users/mac/Desktop/TP
cat Laborator_6_GitHub/L6_TP_Colta_Iulian_SI-265.md
```

Rularea directă a căii fișierului poate produce `zsh: permission denied`. Nu este necesară schimbarea permisiunilor de execuție.
