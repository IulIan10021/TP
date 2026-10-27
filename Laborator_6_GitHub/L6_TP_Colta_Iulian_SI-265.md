# Laboratorul 6 — GitHub, pas cu pas

## Datele studentului

- Student: Colta Iulian
- Grupa: SI-265
- Username GitHub: IulIan10021
- Disciplina: Tehnici de programare

## Scopul lucrării

Exersarea configurării Git, a gestionării versiunilor și a sincronizării unui proiect prin comenzile clone, status, add, commit, push, pull, log, diff și restore.

## Linkurile depozitelor

- Depozitul disciplinei: https://github.com/IulIan10021/TP
- Primul depozit de exercițiu: https://github.com/IulIan10021/exercitiu-git
- Al doilea depozit de exercițiu: https://github.com/IulIan10021/exercitiu-2

## A1. Contul GitHub

Am utilizat contul GitHub cu username-ul IulIan10021. Username-ul identifică proprietarul depozitelor și apare în adresele acestora.

## A2. Configurarea Git

Am verificat instalarea Git și am configurat numele autorului, adresa de e-mail, denumirea implicită a ramurii și comportamentul comenzii pull.

```sh
git --version
git config --global user.name "Colta Iulian"
git config --global user.email "134854600+IulIan10021@users.noreply.github.com"
git config --global init.defaultBranch main
git config --global pull.rebase false
git config --global --list
```

## A3. Primul depozit

Am pregătit depozitul de exercițiu exercitiu-git cu fișierul README.md. Un depozit păstrează fișierele proiectului împreună cu istoricul modificărilor.

## A4. Clonarea

Am clonat depozitul local de exercițiu și am verificat fișierele din copia de lucru. Comanda git clone copiază fișierele și istoricul unui depozit existent.

## A5. Status, add și commit

Am creat fișierul salut.py, l-am executat și l-am salvat în istoric folosind git add și git commit.

```python
print("Salut, GitHub!")
```

```sh
python3 salut.py
git status
git add salut.py
git commit -m "Adaug salut.py"
```

Programul afișează `Salut, GitHub!`. Status arată starea fișierelor, add pregătește conținutul, iar commit salvează versiunea în istoricul local.

## A6. Push

Am exersat trimiterea commit-urilor către depozitul origin local prin git push. Comanda transmite commit-urile ramurii către depozitul configurat ca destinație.

```sh
git push
```

## A7. Pull

Am modificat README.md într-o a doua copie locală și am preluat schimbarea prin origin comun. Am verificat prezența rândului „Aici exersez git.”.

```sh
git pull
cat README.md
```

## A8. Fișierul .gitignore

Am creat mediul virtual Python și am adăugat reguli de ignorare pentru mediul virtual și fișierele cache.

```gitignore
.venv/
__pycache__/
```

```sh
python3 -m venv .venv
git check-ignore .venv/
git add .gitignore
git commit -m "Ignor mediul virtual"
```

## A9. Log, diff și restore

Am citit istoricul celor patru commit-uri, am adăugat temporar o instrucțiune în salut.py, am analizat diferența și am revenit la versiunea salvată.

```sh
git log --oneline
git diff
git restore salut.py
git status
```

Log afișează istoricul, diff arată modificările, iar restore readuce fișierul la versiunea salvată.

## A10. Al doilea depozit

Am inițializat local exercitiu-2, am creat README.md cu titlul „Al doilea depozit” și am salvat primul commit. Am exersat git push -u către un origin local; opțiunea -u configurează urmărirea ramurii remote.

```sh
git init -b main
git add README.md
git commit -m "Primul commit"
git push -u origin main
```

## Concluzii

Am exersat configurarea Git, salvarea versiunilor, transferul commit-urilor între copii locale, ignorarea fișierelor generate și citirea istoricului. Am observat diferența dintre pregătirea fișierelor prin add, salvarea lor prin commit și sincronizarea depozitelor prin push și pull.

## Bibliografie

Fișa de laborator L6_Laborator_GitHub_pas_cu_pas.docx.
