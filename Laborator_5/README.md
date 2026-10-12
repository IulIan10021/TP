# Laboratorul 5 — Colta Iulian, SI-265

Python 3.10 sau mai nou. Comentariile Itemul 1–15 corespund exercitiilor.
Comenzile se ruleaza din folderul Laborator_5 pe macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 probe/pregateste_demo.py
python3 -m unittest discover -s teste -v
python3 arsenal/forensics/decode.py probe/mesaj.txt --fisier
python3 arsenal/forensics/decode.py probe/xor.bin --fisier --mod xor --iesire rezultate/xor.json
python3 arsenal/forensics/decode.py probe/hashuri.txt --fisier --mod hash --iesire rezultate/hashuri.json
python3 forensics.py probe/foto.jpg
python3 forensics.py probe/ascuns.png --arhiva gasit.zip --extrage-in extras
python3 stego.py ascunde probe/foto.jpg 'FLAG{ascuns_in_pixeli}' stego.png
python3 stego.py dezvaluie stego.png
```

probe/pregateste_demo.py este un generator creat pentru demonstratie.
Nu este scriptul probe/pregateste.py al profesorului. Pentru rezultatele
oficiale, obtine scriptul original si ruleaza aceleasi unelte pe probele lui.
GPS-ul demonstrativ este sintetic, nu provine dintr-o fotografie reala.

Un sir poate semana simultan cu text si base64. Detectarea este euristica.
XOR produce mai multi candidati: scorul nu garanteaza cheia corecta.
Lungimea hash-ului sugereaza algoritmul; aici sunt acceptate cele trei
algoritmi nesarati din fisa: MD5, SHA1 si SHA256.
Decoderul continua cat timp recunoaste un strat, cel mult 8 transformari.
Exemplul NTM1OTU3NTk= din fisa nu ajunge la un mesaj natural: trece prin
53595759, apoi SYWY, apoi octetii 498598.

raport.md si output_demo.txt descriu exclusiv probele demonstrative.
Actualizeaza raportul cu rezultatele probelor originale inainte de predare.

Copie folderul Laborator_5 in depozitul TP_Colta_Iulian_SI-265.
Din radacina depozitului, dupa verificare:

```bash
git add Laborator_5
git commit -m "Lab 5: decoder universal + forensics si stego"
git push
git rev-parse --short HEAD
```

Email: cristian.gonceari@isa.utm.md
Subiect: L5_TP_Colta_Iulian_SI-265
Mesaj: linkul depozitului si codul ultimului commit.

Pentru rularea demonstratiei complete si salvarea output-ului:
```bash
python3 ruleaza_demo.py
```
Aceasta comanda regenereaza probele DEMONSTRATIVE. Nu o rula peste probele
originale; pastreaza copiile originale intr-un folder separat.
