# Laboratorul 5 — Informații invizibile

Student: Colta Iulian  
Grupa: SI-265

## Proveniența probelor
Acest raport prezintă probe DEMONSTRATIVE generate cu pregateste_demo.py,
nu probele originale ale profesorului. Coordonatele GPS sunt sintetice.
La predare, înlocuiesc rezultatele cu cele obținute pe probele originale.

## Lucrarea A
Mesajul a fost desfăcut în ordinea Base64 → hex → URL.
Rezultatul demonstrativ este FLAG{straturi_demo}.
Am încercat toate cele 256 de chei XOR de un octet. Cheia 42 produce:
The secret message is FLAG{xor_demo}.
Rezultatele euristice sunt în rezultate/xor.json.
Dicționarul demonstrativ conține student265. Această parolă corespunde
celor trei hash-uri demonstrative MD5, SHA1 și SHA256.
Fișa mesajului este în arsenal/forensics/fisa.json.
Hash-urile au fost comparate cu hash-urile cuvintelor, nu decriptate.

## Lucrarea B
Semnăturile indică JPEG pentru foto.jpg și PNG pentru ascuns.png.
EXIF: producător Camera demonstrativa, autor Colta Iulian.
GPS sintetic: latitudine 47.0, longitudine 28.833333333333332.
Arhiva ZIP de după IEND a fost salvată în gasit.zip.
Fișierul extras secret.txt conține FLAG{arhiva_demo}.
Mesajul FLAG{ascuns_in_pixeli} a fost scris în ultimii biți ai canalelor
RGB, cu octet nul la final, apoi recuperat din stego.png.
PNG păstrează biții mesajului fără recomprimare cu pierderi.

## Verificare
7 teste automate trecute și toate comenzile din ruleaza_demo.py executate.
Output-ul real al rulării demonstrative este păstrat în output_demo.txt.

## Rezultate oficiale de completat
- Mesajul original și straturile:
- Cheia XOR și textul original:
- Hash-ul, algoritmul și parola găsită:
- EXIF și coordonatele GPS originale:
- Conținutul arhivei originale:
- Mesajul LSB:
- Linkul depozitului și commit-ul:
