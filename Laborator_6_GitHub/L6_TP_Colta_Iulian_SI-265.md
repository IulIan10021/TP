# Laboratorul 6. GitHub, pas cu pas

**Student:** Colta Iulian  
**Grupa:** SI-265  
**GitHub:** IulIan10021

## Starea realizării

Publicarea pe GitHub nu a putut fi efectuată: terminalul a returnat „Could not resolve host: github.com”. Exercițiile de transfer au fost executate cu depozite bare locale, fără a pretinde că sunt depozite publice. Vizibilitatea depozitului disciplinei și accesul profesorului nu au putut fi verificate.

## Linkuri

- Disciplina: https://github.com/IulIan10021/TP (vizibilitate neverificată).
- https://github.com/IulIan10021/exercitiu-git (publicare neconfirmată).
- https://github.com/IulIan10021/exercitiu-2 (publicare neconfirmată).

## Pașii efectuați

### A1. Contul GitHub

Am utilizat numele contului existent IulIan10021; autentificarea online nu a putut fi confirmată.

### A2. Configurarea Git

Am verificat versiunea Git și am configurat local identitatea Colta Iulian cu adresa GitHub noreply existentă.

### A3. Primul depozit

Am pregătit un depozit bare local cu README.md; crearea depozitului public pe GitHub rămâne de efectuat.

### A4. Clonarea

Am clonat depozitul local în exercitiu-git și am verificat conținutul.

### A5. Primul commit

Am creat salut.py, am rulat programul și am folosit status, add și commit.

### A6. Push

Am trimis commit-ul către origin local; trimiterea pe GitHub este blocată de conexiune.

### A7. Pull

Am modificat README.md dintr-o a doua copie locală și am adus schimbarea cu git pull.

### A8. .gitignore

Am creat mediul virtual și am salvat regulile .venv/ și __pycache__/; git check-ignore confirmă ignorarea.

### A9. Log și diff

Am verificat patru commit-uri, am adăugat temporar un rând în salut.py și l-am eliminat cu git restore.

### A10. Al doilea depozit

Am inițializat local exercitiu-2, am creat README.md și am folosit push -u către un al doilea origin local.

### Figura 1. Configurare si clonare locala

Această imagine prezintă verificarea instalării Git și clonarea primului depozit de exercițiu. Comanda git --version afișează versiunea disponibilă pe calculator. Prin git clone se creează o copie de lucru a depozitului, împreună cu istoricul său. În acest exercițiu, sursa clonării este un depozit bare local, adică un folder care păstrează istoricul Git și poate primi commit-uri de la alte copii de lucru.

După clonare, identitatea autorului este configurată prin user.name și user.email. Numele Colta Iulian și adresa noreply asociată contului existent sunt folosite pentru identificarea autorului commit-urilor. Aceste setări sunt aplicate local, în depozitul de exercițiu. Configurarea identității nu reprezintă autentificare pe GitHub: ea stabilește doar datele înscrise în istoricul Git.

![Rezultate reale, redate din transcriere](capturi/01.png)

### Figura 2. Add, commit si push spre origin local

Această imagine ilustrează crearea fișierului salut.py și salvarea lui în istoricul proiectului. Programul conține instrucțiunea print("Salut, GitHub!") și, la executare, afișează mesajul în terminal. Acest rezultat confirmă că fișierul Python este funcțional înainte de a fi inclus într-un commit.

Comanda git status --short arată inițial fișierul ca ne urmărit, prin marcajul ??, deoarece Git nu îl include automat în istoric. După git add salut.py, fișierul este pregătit pentru următorul commit și apare cu marcajul A. Comanda git commit salvează versiunea cu mesajul „Adaug salut.py”. În final, git push transmite commit-ul către origin, care în această demonstrație este un depozit local, nu un depozit public GitHub.

![Rezultate reale, redate din transcriere](capturi/02.png)

### Figura 3. Pull: schimbare facuta din a doua copie locala

Această imagine prezintă aducerea unei modificări din depozitul origin în copia de lucru exercitiu-git. Fișierul README.md a fost modificat și salvat prin commit într-o a doua copie locală, apoi schimbarea a fost trimisă către depozitul bare comun. Astfel, cele două copii au putut fi folosite pentru a exersa sincronizarea fără acces la GitHub.

Comanda git pull preia schimbările disponibile în origin și le integrează în ramura curentă. În transcriere apare și sincronizarea celei de-a doua copii prin git pull --rebase, înaintea trimiterii modificării. După actualizare, comanda cat README.md afișează conținutul fișierului și permite verificarea rândului „Aici exersez git.”. Exercițiul arată de ce este util să aducem schimbările existente înainte de a continua lucrul sau de a trimite commit-uri noi.

![Rezultate reale, redate din transcriere](capturi/03.png)

### Figura 4. Ignorarea mediului virtual

Această imagine ilustrează crearea mediului virtual Python și folosirea fișierului .gitignore. Mediul .venv conține interpretorul și fișierele necesare unui mediu de lucru separat. Aceste fișiere pot ocupa mult spațiu și pot fi recreate pe alt calculator, de aceea nu este necesară salvarea lor în istoricul proiectului.

În .gitignore sunt introduse regulile .venv/ și __pycache__/. Prima regulă exclude mediul virtual, iar a doua exclude directoarele cu fișiere cache generate de Python. Comanda git check-ignore .venv/ verifică faptul că regula este recunoscută. Fișierul .gitignore este apoi adăugat, salvat cu mesajul „Ignor mediul virtual” și trimis către origin local. Astfel, regulile de ignorare fac parte din proiect și pot fi folosite și în alte copii ale acestuia.

![Rezultate reale, redate din transcriere](capturi/04.png)

### Figura 5. Istoric, diff si restore

Această imagine prezintă citirea istoricului și verificarea unei modificări temporare. Comanda git log --oneline afișează commit-urile într-o formă scurtă: fiecare rând conține un identificator și mesajul care descrie schimbarea. Istoricul primului depozit cuprinde patru commit-uri, corespunzătoare inițializării, adăugării programului, actualizării README.md și regulilor de ignorare.

În fișierul salut.py este adăugată temporar instrucțiunea print("al doilea"). Comanda git diff compară conținutul modificat cu versiunea salvată și marchează rândul nou prin semnul +. Deoarece modificarea nu trebuie păstrată, git restore salut.py readuce fișierul la versiunea din ultimul commit. Mesajul „nothing to commit, working tree clean” confirmă că nu au rămas modificări nesalvate în copia de lucru.

![Rezultate reale, redate din transcriere](capturi/05.png)

### Figura 6. Al doilea depozit: init si push -u local

Această imagine prezintă crearea celui de-al doilea depozit pornind de la un folder local. Comanda git init -b main inițializează istoricul Git și stabilește numele ramurii principale. În folder este creat fișierul README.md cu titlul „Al doilea depozit”, apoi acesta este pregătit cu git add și salvat prin commit-ul „Primul commit”.

Comanda git remote add origin stabilește destinația către care vor fi trimise commit-urile. În exercițiul realizat, această destinație este un al doilea depozit bare local. Prin git push -u origin main se trimite ramura main și se configurează urmărirea ramurii corespunzătoare din origin. După această asociere, următoarele trimiteri pot fi făcute cu git push. Publicarea depozitului exercitiu-2 pe GitHub rămâne de efectuat după restabilirea conexiunii.

![Rezultate reale, redate din transcriere](capturi/06.png)

### Figura 7. Publicarea pe GitHub: blocata de conexiune

Această imagine prezintă încercarea reală de publicare a lucrării în depozitul disciplinei. Comanda git push a fost executată pentru proiectul TP, a cărui adresă origin este https://github.com/IulIan10021/TP.git. Terminalul a returnat mesajul „Could not resolve host: github.com”, ceea ce arată că numele serverului GitHub nu a putut fi transformat într-o adresă de rețea accesibilă în acel moment.

Din cauza acestei erori, comanda nu a putut confirma trimiterea commit-urilor pe GitHub. Fișierele și istoricul sunt păstrate local, iar imaginile anterioare documentează exercițiile efectuate cu depozite locale. Pentru finalizarea predării sunt necesare restabilirea accesului la GitHub, publicarea celor două depozite de exercițiu și repetarea comenzii git push în depozitul disciplinei. Raportul distinge astfel operațiile realizate de cele care nu au putut fi finalizate online.

![Rezultate reale, redate din transcriere](capturi/07.png)

## Surse și ajutor

Fișa laboratorului și modelul Word indicat. Ajutor Codex la executarea comenzilor, organizarea raportului și redarea transcrierilor. Imaginile sunt redări ale rezultatelor reale, nu capturi din GitHub. Istoricul original este păstrat în exemple/*.bundle; copiile de lucru sunt în /Users/mac/Desktop/L6_exercitii_locale.
