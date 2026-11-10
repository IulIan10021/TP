# -*- coding: utf-8 -*-
"""
===============================================================================

   LUCRAREA DE LABORATOR NR. 9  -  OBIECTE SI CLASE
   Laborator macOS în Python: inventar de procese și evenimente de securitate

   Universitatea Tehnica a Moldovei
   Facultatea Calculatoare, Informatica si Microelectronica
   Disciplina: Tehnici de programare        Anul I, grupele SI-265 / SI-266

===============================================================================

   CUM PORNESTI

   1. Deschide Terminal pe Mac (Applications > Utilities > Terminal).
      Folosește comanda cd pentru a intra în folderul acestui fișier.
      Nu porni prin dublu-clic sau din butonul Run al editorului: programul
      are nevoie de Terminal pentru a putea citi de la tastatură.

   2. Porneste programul:

          python3 L9_TP_Colta_Iulian_SI-265.py

   3. Iti apare un meniu. Incepe cu optiunea  c , "Cum se lucreaza".

   -----------------------------------------------------------------------

   CE AI DE FACUT

   Datele sunt o captură demonstrativă macOS. Modelezi procesele și evenimentele
   ca obiecte: clase cu câmpuri și metode. Apoi le interoghezi pentru a
   identifica activitatea suspectă.

   Partea A - procesul și evenimentul ca obiecte   4 sarcini
   Partea B - clasa Inventar și raportul          4 sarcini

   Fiecare sarcină valorează un punct. Nota = punctajul obținut.

   Clasele sunt deja scrise (câmpurile lor). Tu completezi metodele și
   funcțiile marcate TODO. Salvezi fișierul și apeși Enter în terminal.

   -----------------------------------------------------------------------

   CAPTURILE

   La prima pornire, programul creează folderul start/ cu două fișiere:
   procese.json și evenimente.json. Nu ai nimic de descărcat.

   Pe un Mac, lista proceselor poate fi obținută cu ps, iar evenimentele cu
   log show. Fișierele acestui laborator sunt capturi demonstrative, ca să
   poți lucra pe date stabile fără acces la alte sisteme.

===============================================================================
"""
import io
import json
import os
import sys
from dataclasses import dataclass, asdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VERSIUNE = "L9-v1"
DOSAR = os.path.dirname(os.path.abspath(sys.argv[0])) or os.getcwd()
START = os.path.join(DOSAR, "start")

# Căi neobișnuite pentru procese: cache-ul utilizatorului și LaunchAgents.
CAI_SUSPECTE = ("/Library/LaunchAgents/", "/Users/ana/Library/Caches/")
# Coduri atribuite capturii pentru exercițiu; nu sunt ID-uri native macOS.
SUSPECTE_ID = {1001, 1002, 1003}


# PARTEA A — procesul și evenimentul ca obiecte

@dataclass
class Proces:
    """Un proces macOS din captura demonstrativă."""
    pid: int
    nume: str
    user: str
    cale: str

    def e_suspect(self):
        """Sarcina 1. True dacă procesul rulează dintr-o cale suspectă.

        Întoarce True dacă una dintre căile din CAI_SUSPECTE apare în self.cale,
        altfel False. Cache-ul și LaunchAgents pot necesita verificare.

        Proces(1, "helper", "ana", "/Users/ana/Library/Caches/helper")
            .e_suspect()  ->  True
        """
        # TODO: verifică dacă una dintre căile suspecte apare în self.cale
        raise NotImplementedError


@dataclass
class Eveniment:
    """Un eveniment normalizat din captura demonstrativă macOS."""
    id: int
    nivel: str
    sursa: str
    cont: str
    mesaj: str

    def e_suspect(self):
        """Sarcina 2. True daca evenimentul merita atentie.

        Întoarce True dacă self.id este în SUSPECTE_ID SAU self.nivel este
        "critical". Altfel False.

        Eveniment(1001, "warning", "authd", "ana", "...").e_suspect() -> True
        Eveniment(9000, "critical", "kernel", "SYSTEM", "...").e_suspect() -> True
        """
        # TODO: verifică ID-ul sau nivelul critic
        raise NotImplementedError


def procese_din_json(cale):
    """Sarcina 3. Incarca o lista de obiecte Proces dintr-un fisier JSON.

    Citeste fisierul si intoarce o lista de Proces. Proces(**d) despacheteaza
    un dictionar din JSON direct in campurile obiectului, pe nume.

    procese_din_json("start/procese.json")  ->  lista cu 7 obiecte Proces
    """
    with open(cale, encoding="utf-8") as f:
        # TODO: intoarce [Proces(**d) for d in json.load(f)]
        raise NotImplementedError


def evenimente_din_json(cale):
    """Sarcina 4. Incarca o lista de obiecte Eveniment dintr-un fisier JSON.

    La fel ca procese_din_json, dar pentru Eveniment.

    evenimente_din_json("start/evenimente.json")  ->  lista cu 8 obiecte
    """
    with open(cale, encoding="utf-8") as f:
        # TODO: intoarce [Eveniment(**d) for d in json.load(f)]
        raise NotImplementedError


# PARTEA B — clasa Inventar și raportul

@dataclass
class Inventar:
    """Tine lista de procese si stie sa o interogheze."""
    procese: list

    @classmethod
    def din_json(cls, cale):
        """Sarcina 5. Constructor alternativ: umple inventarul din JSON.

        E o metoda de clasa (@classmethod): primeste clasa in cls si intoarce
        un Inventar nou, cu lista de procese incarcata din fisier.

        Inventar.din_json("start/procese.json")  ->  un Inventar cu 7 procese
        """
        with open(cale, encoding="utf-8") as f:
            # TODO: return cls([Proces(**d) for d in json.load(f)])
            raise NotImplementedError

    def __len__(self):
        return len(self.procese)

    def suspecte(self):
        """Sarcina 6. Lista proceselor care se declara suspecte.

        Intoarce lista obiectelor Proces din self.procese pentru care
        p.e_suspect() este True, in ordinea din inventar.
        """
        # TODO: lista proceselor cu p.e_suspect()
        raise NotImplementedError

    def pe_user(self):
        """Sarcina 7. Gruparea numelor de proces pe utilizator.

        Intoarce un dictionar user -> lista de nume de proces ale acelui
        utilizator, in ordinea din inventar. Foloseste setdefault.

        {"SYSTEM": ["launchd", "kernel_task"], "ana": ["Finder", ...]}
        """
        # TODO: dict user -> lista de nume (foloseste setdefault)
        raise NotImplementedError


def raport(dosar):
    """Sarcina 8. Raportul complet, ca dictionar gata de pus in JSON.

    Primeste folderul capturilor. Incarca procesele si evenimentele, apoi
    intoarce un dictionar cu patru chei:

        {"procese": numarul de procese,
         "suspecte": [asdict(p) pentru fiecare proces suspect],
         "evenimente": numarul de evenimente,
         "alarma": [asdict(e) pentru fiecare eveniment suspect]}

    asdict(obiect) transforma un obiect @dataclass inapoi in dictionar.
    Nu tipari nimic aici; doar intoarce.
    """
    # TODO: foloseste Inventar.din_json si evenimente_din_json, apoi asdict
    raise NotImplementedError


#  @@ AICI SE TERMINA ZONA TA @@

# Marcajul e lipit din doua bucati dinadins: altfel randul acesta ar contine
# el insusi textul cautat, iar taierea ar cadea in mijlocul lui.
MARCAJ_ZONA = "@@ AICI SE TERMINA " + "ZONA TA @@"

# Captură demonstrativă macOS: două procese rulează din căi neobișnuite,
# iar cinci evenimente normalizate merită verificate.
PROCESE = [
    {"pid": 101,  "nume": "launchd",  "user": "SYSTEM", "cale": "/sbin/launchd"},
    {"pid": 740,  "nume": "kernel_task", "user": "SYSTEM", "cale": "/System/Library/Kernels/kernel"},
    {"pid": 2100, "nume": "Finder", "user": "ana", "cale": "/System/Library/CoreServices/Finder.app/Contents/MacOS/Finder"},
    {"pid": 2560, "nume": "Safari", "user": "ana", "cale": "/Applications/Safari.app/Contents/MacOS/Safari"},
    {"pid": 3120, "nume": "update", "user": "ana", "cale": "/Users/ana/Library/Caches/update"},
    {"pid": 3450, "nume": "Terminal", "user": "ana", "cale": "/System/Applications/Utilities/Terminal.app/Contents/MacOS/Terminal"},
    {"pid": 3890, "nume": "helper", "user": "ana", "cale": "/Library/LaunchAgents/helper"},
]
EVENIMENTE = [
    {"id": 1001, "nivel": "warning", "sursa": "authd", "cont": "ana", "mesaj": "Mai multe autentificări eșuate"},
    {"id": 1001, "nivel": "warning", "sursa": "authd", "cont": "ana", "mesaj": "O nouă autentificare eșuată"},
    {"id": 1003, "nivel": "warning", "sursa": "launchd", "cont": "ana", "mesaj": "A fost încărcat un agent nou"},
    {"id": 9000, "nivel": "critical", "sursa": "kernel", "cont": "SYSTEM", "mesaj": "Repornire neașteptată a sistemului"},
    {"id": 1002, "nivel": "critical", "sursa": "auditd", "cont": "ana", "mesaj": "Configurația de audit a fost modificată"},
    {"id": 2001, "nivel": "information", "sursa": "authd", "cont": "ana", "mesaj": "Autentificare reușită"},
    {"id": 2002, "nivel": "information", "sursa": "loginwindow", "cont": "ana", "mesaj": "Sesiunea utilizatorului a fost închisă"},
    {"id": 2003, "nivel": "information", "sursa": "launchd", "cont": "SYSTEM", "mesaj": "Serviciul de sistem a pornit"},
]


def pregateste_capturile():
    """Scrie folderul start/ cu cele doua fisiere JSON la prima pornire."""
    nou = False
    if not os.path.isdir(START):
        os.makedirs(START)
        nou = True
    for nume, date in (("procese.json", PROCESE), ("evenimente.json", EVENIMENTE)):
        cale = os.path.join(START, nume)
        if not os.path.exists(cale):
            json.dump(date, io.open(cale, "w", encoding="utf-8"),
                      indent=2, ensure_ascii=False)
            nou = True
    return nou


_N_PROC = 7
_SUSP_PID = [3120, 3890]
_PE_USER = {
    "SYSTEM": ["launchd", "kernel_task"],
    "ana": ["Finder", "Safari", "update", "Terminal", "helper"],
}
_N_EV = 8
_N_ALARM = 5


def reincarca_codul():
    """Reciteste de pe disc zona in care scrii tu si actualizeaza clasele.
    Intoarce (reusit, mesaj_de_eroare)."""
    try:
        cale = os.path.abspath(sys.argv[0])
        sursa = io.open(cale, encoding="utf-8").read()
    except Exception as e:
        return False, "Nu pot reciti fișierul: " + str(e)
    taietura = sursa.find(MARCAJ_ZONA)
    if taietura == -1:
        return False, "Nu găsesc marcajul de separare din fișier."
    zona = sursa[:taietura]
    spatiu = {}
    try:
        exec(compile(zona, cale, "exec"), spatiu)
    except IndentationError as e:
        return False, ("Indentare greșită la rândul " + str(e.lineno) + "."
                       + chr(10) + "Codul dintr-o metodă se scrie cu 4 spații "
                       "mai la dreapta decât def.")
    except SyntaxError as e:
        return False, ("Eroare de sintaxă la rândul " + str(e.lineno) +
                       ":" + chr(10) + str(e.msg) + chr(10) +
                       "Verifică ghilimelele, parantezele și două puncte.")
    except Exception as e:
        return False, ("Codul tău a produs o eroare la încărcare:" +
                       chr(10) + type(e).__name__ + ": " + str(e))
    g = globals()
    for n, v in spatiu.items():
        if not n.startswith("__"):
            g[n] = v
    return True, ""


def _scurt(v, maxim=56):
    t = repr(v)
    return t if len(t) <= maxim else t[:maxim - 3] + "..."


def _p(pid, nume, user, cale):
    return globals()["Proces"](pid, nume, user, cale)


def _e(idp, nivel, sursa, cont, mesaj):
    return globals()["Eveniment"](idp, nivel, sursa, cont, mesaj)


def v_proces_suspect():
    cache = _p(1, "helper", "ana", "/Users/ana/Library/Caches/helper")
    agent = _p(2, "helper", "ana", "/Library/LaunchAgents/helper")
    curat = _p(3, "launchd", "SYSTEM", "/sbin/launchd")
    if cache.e_suspect() is not True:
        return False, "Un proces din Library/Caches ar trebui să fie suspect (True)."
    if agent.e_suspect() is not True:
        return False, "Un proces din LaunchAgents ar trebui să fie suspect (True)."
    if curat.e_suspect() is not False:
        return False, "Procesul de sistem din /sbin nu ar trebui să fie suspect."
    return True, "Corect."


def v_eveniment_suspect():
    for idp, niv, ok in [(1001, "warning", True), (1002, "critical", True),
                         (1003, "warning", True), (9000, "critical", True),
                         (2001, "information", False), (2002, "information", False)]:
        got = _e(idp, niv, "S", "c", "m").e_suspect()
        if got is not ok:
            return False, ("Pentru id=%d nivel=%s se aștepta %s, s-a primit %s."
                           % (idp, niv, ok, got))
    return True, "Corect."


def v_procese_json():
    lst = globals()["procese_din_json"](os.path.join(START, "procese.json"))
    if not isinstance(lst, list) or len(lst) != _N_PROC:
        return False, "Se aștepta o listă cu %d procese." % _N_PROC
    if not all(isinstance(x, globals()["Proces"]) for x in lst):
        return False, "Lista trebuie să conțină obiecte Proces, nu dicționare."
    if sum(1 for p in lst if p.e_suspect()) != 2:
        return False, "Se așteptau 2 procese suspecte."
    return True, "Corect."


def v_evenimente_json():
    lst = globals()["evenimente_din_json"](os.path.join(START, "evenimente.json"))
    if not isinstance(lst, list) or len(lst) != _N_EV:
        return False, "Se aștepta o listă cu %d evenimente." % _N_EV
    if not all(isinstance(x, globals()["Eveniment"]) for x in lst):
        return False, "Lista trebuie să conțină obiecte Eveniment."
    if sum(1 for e in lst if e.e_suspect()) != _N_ALARM:
        return False, "Se așteptau %d evenimente de alertă." % _N_ALARM
    return True, "Corect."


def v_inventar():
    inv = globals()["Inventar"].din_json(os.path.join(START, "procese.json"))
    if not isinstance(inv, globals()["Inventar"]):
        return False, "din_json trebuie să returneze un obiect Inventar."
    if len(inv) != _N_PROC:
        return False, "len(inventar) ar trebui să fie %d." % _N_PROC
    return True, "Corect."


def v_suspecte():
    inv = globals()["Inventar"].din_json(os.path.join(START, "procese.json"))
    s = inv.suspecte()
    if not isinstance(s, list) or len(s) != 2:
        return False, "suspecte() ar trebui să returneze 2 procese."
    if sorted(p.pid for p in s) != _SUSP_PID:
        return False, "PID-urile proceselor suspecte așteptate sunt %s." % _SUSP_PID
    return True, "Corect."


def v_pe_user():
    inv = globals()["Inventar"].din_json(os.path.join(START, "procese.json"))
    d = inv.pe_user()
    if d != _PE_USER:
        return False, ("pe_user() nu returnează gruparea așteptată." + chr(10) +
                       "   asteptam: " + _scurt(_PE_USER, 90) + chr(10) +
                       "   am primit: " + _scurt(d, 90))
    return True, "Corect."


def v_raport():
    r = globals()["raport"](START)
    if not isinstance(r, dict):
        return False, "raport trebuie să returneze un dicționar."
    for cheie in ("procese", "suspecte", "evenimente", "alarma"):
        if cheie not in r:
            return False, "Lipsește cheia '%s' din raport." % cheie
    if r["procese"] != _N_PROC or r["evenimente"] != _N_EV:
        return False, "Numărul de procese/evenimente nu este corect."
    if len(r["suspecte"]) != 2 or len(r["alarma"]) != _N_ALARM:
        return False, "Numărul de procese suspecte/alerte nu este corect."
    if not all(isinstance(x, dict) for x in r["suspecte"]):
        return False, "Elementele suspecte din raport trebuie să fie dicționare (asdict)."
    if {x.get("pid") for x in r["suspecte"]} != set(_SUSP_PID):
        return False, "Procesele suspecte din raport nu sunt cele așteptate."
    return True, "Corect."


def verifica_sarcina(s):
    """Intoarce (reusit, mesaj)."""
    fn = globals().get(s["cheie_functie"])
    if fn is None and s.get("clasa"):
        fn = globals().get(s["clasa"])
    if fn is None:
        return False, "Nu găsesc " + (s.get("clasa") or s["cheie_functie"]) + " în fișier."
    try:
        return s["verificator"]()
    except NotImplementedError:
        return False, "Sarcina nu este încă rezolvată."
    except Exception as e:
        return False, ("Codul tău a produs o eroare:" + chr(10) + "         "
                       + type(e).__name__ + ": " + str(e))


def stare_completa(reincarca=True):
    if reincarca:
        ok, mesaj = reincarca_codul()
        if not ok:
            return None, mesaj
    out = []
    for s in SARCINI:
        reusit, mesaj = verifica_sarcina(s)
        out.append((s, reusit, mesaj))
    return out, ""


def punctaj(stare):
    return sum(1 for _, reusit, _ in stare if reusit)


SARCINI = [
    {"nr": 1, "parte": "A", "cheie_functie": "e_suspect_proces", "clasa": "Proces",
     "titlu": "Metoda e_suspect pe Proces",
     "indiciu": "any(c in self.cale for c in CAI_SUSPECTE).",
     "verificator": v_proces_suspect},
    {"nr": 2, "parte": "A", "cheie_functie": "e_suspect_eveniment", "clasa": "Eveniment",
     "titlu": "Metoda e_suspect pe Eveniment",
     "indiciu": "self.id in SUSPECTE_ID or self.nivel == 'critical'.",
     "verificator": v_eveniment_suspect},
    {"nr": 3, "parte": "A", "cheie_functie": "procese_din_json",
     "titlu": "Incarca procesele din JSON",
     "indiciu": "[Proces(**d) for d in json.load(f)] - ** despacheteaza dictionarul.",
     "verificator": v_procese_json},
    {"nr": 4, "parte": "A", "cheie_functie": "evenimente_din_json",
     "titlu": "Incarca evenimentele din JSON",
     "indiciu": "La fel ca la procese, dar cu Eveniment(**d).",
     "verificator": v_evenimente_json},

    {"nr": 5, "parte": "B", "cheie_functie": "din_json", "clasa": "Inventar",
     "titlu": "Inventar.din_json (constructor de clasa)",
     "indiciu": "return cls([Proces(**d) for d in json.load(f)]).",
     "verificator": v_inventar},
    {"nr": 6, "parte": "B", "cheie_functie": "suspecte", "clasa": "Inventar",
     "titlu": "Inventar.suspecte()",
     "indiciu": "[p for p in self.procese if p.e_suspect()].",
     "verificator": v_suspecte},
    {"nr": 7, "parte": "B", "cheie_functie": "pe_user", "clasa": "Inventar",
     "titlu": "Inventar.pe_user()",
     "indiciu": "d.setdefault(p.user, []).append(p.nume).",
     "verificator": v_pe_user},
    {"nr": 8, "parte": "B", "cheie_functie": "raport",
     "titlu": "Raportul JSON, din obiecte",
     "indiciu": "asdict(p) transforma un obiect inapoi in dictionar.",
     "verificator": v_raport},
]


LAT = 74


def linie(ch="-"):
    print(ch * LAT)


def titlu(text, ch="="):
    print()
    linie(ch)
    print("  " + text)
    linie(ch)


def bara(cate, din, latime=34):
    plin = int(round(latime * cate / float(din))) if din else 0
    return "[" + "#" * plin + "." * (latime - plin) + "]"


def harta(stare):
    """Analiza capturii macOS, care se completează pe măsură ce rezolvi.
    Fiecare rand e un pas al apararii, aprins cu date adevarate cand rezolvi
    sarcina care il produce."""
    gata = set(s["nr"] for s, reusit, _ in stare if reusit)

    def are(*nrs):
        return all(n in gata for n in nrs)

    def rand(eticheta, deblocat, text, cheie):
        tinta = text if deblocat else "in ceata ... (rezolva %s)" % cheie
        marcaj = " +" if deblocat else "  "
        print("  %s %-12s %s" % (marcaj, eticheta, tinta[:52]))

    titlu("MAȘINA macOS  -  inventar și jurnal", "-")
    print()
    rand("proces:", are(1), "știu când un proces rulează dintr-o cale suspectă",
         "sarcina 1")
    rand("eveniment:", are(2), "știu când un eveniment din jurnal declanșează o alertă",
         "sarcina 2")
    rand("procese:", are(3), "%d procese încărcate ca obiecte" % _N_PROC,
         "sarcina 3")
    rand("evenimente:", are(4), "%d evenimente încărcate ca obiecte" % _N_EV,
         "sarcina 4")
    print()
    rand("inventar:", are(5), "inventarul conține %d procese" % _N_PROC,
         "sarcina 5")
    rand("SUSPECTE:", are(6), "2 procese din folderul utilizatorului",
         "sarcina 6")
    rand("pe utilizator:", are(7), "procesele pornite de fiecare cont", "sarcina 7")
    rand("RAPORT:", are(8), "2 procese + %d evenimente de alarma" % _N_ALARM,
         "sarcina 8")
    print()
    if are(*range(1, 9)):
        print("  >>> Inventarul este gata. Procesele din căile neobișnuite au fost identificate. <<<")
    else:
        print("  Rezolvă sarcinile pentru a analiza activitatea de pe mașină.")


def arata_progres(stare):
    titlu("LABORATORUL 9  -  OBIECTE ȘI CLASE", "=")
    p = punctaj(stare)
    print()
    print("  " + bara(p, len(SARCINI)) + "   %d din %d sarcini" % (p, len(SARCINI)))
    harta(stare)
    print()
    parte = None
    for s, reusit, mesaj in stare:
        if s["parte"] != parte:
            parte = s["parte"]
            print("  PARTEA %s" % parte)
        semn = "[x]" if reusit else "[ ]"
        print("   %s %2d. %-34s %s" % (semn, s["nr"], s["titlu"],
                                       "" if reusit else mesaj.split(chr(10))[0][:26]))
    print()
    print("  Nota ta în acest moment: %d" % max(1, min(10, p)))


def arata_sarcina(s, reusit, mesaj):
    titlu("SARCINA %d  (partea %s)  -  %s" % (s["nr"], s["parte"], s["titlu"]))
    print()
    # documentatia e in metoda/functia careia ii apartine sarcina
    doc = ""
    tinta = globals().get(s["cheie_functie"])
    if tinta is not None and getattr(tinta, "__doc__", None):
        doc = tinta.__doc__
    elif s.get("clasa"):
        cls = globals().get(s["clasa"])
        m = getattr(cls, s["cheie_functie"], None) if cls else None
        doc = (m.__doc__ or "") if m else ""
    for r in doc.strip().split(chr(10)):
        print("   " + r.strip())
    print()
    if reusit:
        print("   REZOLVATĂ.")
    else:
        print("   Încă nu funcționează:")
        for r in mesaj.split(chr(10)):
            print("      " + r)
        print()
        print("   Indiciu: " + s["indiciu"])


def _tine_fereastra_deschisa():
    if os.name == "nt" and sys.stdout.isatty():
        try:
            os.system("pause")
        except Exception:
            pass


def iesire_fara_terminal():
    print()
    print("   " + "!" * 66)
    print("   Programul s-a închis deoarece nu a fost pornit din Terminal")
    print("   și nu poate citi de la tastatură (de obicei, la dublu-clic sau")
    print("   când îl pornești din butonul editorului).")
    print()
    print("   Pornește-l astfel pe Mac:")
    print("     1. Deschide aplicația Terminal.")
    print("     2. Scrie cd, lasă un spațiu, trage folderul fișierului în")
    print("        fereastră și apasă Enter.")
    print("     3. Rulează comanda:")
    print()
    print("          python3 " + os.path.basename(sys.argv[0]))
    print("   " + "!" * 66)
    _tine_fereastra_deschisa()
    raise SystemExit


def asteapta():
    try:
        input()
    except EOFError:
        iesire_fara_terminal()
    except KeyboardInterrupt:
        raise SystemExit


def instructiuni():
    titlu("CUM SE LUCREAZĂ")
    print("""
   1. Lasă acest program pornit în Terminal.

   2. Deschide fisierul  L9_TP_Colta_Iulian_SI-265.py  intr-un editor.

   3. Clasele Proces, Eveniment și Inventar sunt deja scrise. Tu completezi
      METODELE lor (e_suspect, din_json, suspecte, pe_user) si functiile
      (procese_din_json, evenimente_din_json, raport). Fiecare are un marcaj TODO
      și se termină cu raise NotImplementedError.

   4. SALVEAZĂ fișierul.

   5. Revino aici și apasă Enter. Programul recitește fișierul și îți spune
      imediat dacă funcția este corectă.

   Capturile sunt în folderul start/, creat la prima pornire: procese.json și
   evenimente.json. Le poți deschide și citi oricând.
""")


MAIN_INVENTAR = (chr(10) + chr(10) +
    "def main():" + chr(10) +
    "    import argparse" + chr(10) +
    "    p = argparse.ArgumentParser(description='Analizează procesele și evenimentele din capturi JSON.')" + chr(10) +
    "    p.add_argument('capturi', help='folderul cu procese.json și evenimente.json')" + chr(10) +
    "    p.add_argument('--json', action='store_true', help='afișează raportul în format JSON')" + chr(10) +
    "    a = p.parse_args()" + chr(10) +
    "    inv = Inventar.din_json(a.capturi + '/procese.json')" + chr(10) +
    "    ev = evenimente_din_json(a.capturi + '/evenimente.json')" + chr(10) +
    "    alarma = [e for e in ev if e.e_suspect()]" + chr(10) +
    "    if a.json:" + chr(10) +
    "        print(json.dumps(raport(a.capturi), indent=2, ensure_ascii=False))" + chr(10) +
    "        return" + chr(10) +
    "    sus = inv.suspecte()" + chr(10) +
    "    print('Procese: %d | suspecte: %d' % (len(inv), len(sus)))" + chr(10) +
    "    for p in sus:" + chr(10) +
    "        print('  [%d] %s  (%s)  %s' % (p.pid, p.nume, p.user, p.cale))" + chr(10) +
    "    print('Evenimente: %d | alerte: %d' % (len(ev), len(alarma)))" + chr(10) +
    "    for e in alarma:" + chr(10) +
    "        print('  %d [%s] %s: %s' % (e.id, e.nivel, e.cont, e.mesaj))" + chr(10) +
    chr(10) + chr(10) + "if __name__ == '__main__':" + chr(10) + "    main()" + chr(10))

CODA_TEST = (
    "# -*- coding: utf-8 -*-" + chr(10) +
    '"""Verifică procesele dintr-o cale suspectă și dintr-o cale de sistem."""' +
    chr(10) + "from arsenal.macos.inventar import Proces" + chr(10) + chr(10) + chr(10) +
    "def test_proces_din_cache_e_suspect():" + chr(10) +
    "    p = Proces(1, 'helper', 'ana', '/Users/ana/Library/Caches/helper')" + chr(10) +
    "    assert p.e_suspect() is True" + chr(10) + chr(10) + chr(10) +
    "def test_proces_de_sistem_nu_e_suspect():" + chr(10) +
    "    p = Proces(2, 'launchd', 'SYSTEM', '/sbin/launchd')" + chr(10) +
    "    assert p.e_suspect() is False" + chr(10))


def pregateste_predarea(stare):
    nerezolvate = [s["nr"] for s, reusit, _ in stare if not reusit]
    sursa = io.open(os.path.abspath(sys.argv[0]), encoding="utf-8").read()
    zona = sursa[:sursa.find(MARCAJ_ZONA)]
    # pastram tot din zona studentului de la prima clasa in jos (fara intro)
    corp = zona[zona.find("@dataclass"):].rstrip()

    LUCRARE = os.path.join(DOSAR, "Laborator_9")
    dest = os.path.join(LUCRARE, "arsenal", "macos")
    os.makedirs(dest, exist_ok=True)
    io.open(os.path.join(LUCRARE, "arsenal", "__init__.py"), "w",
            encoding="utf-8").write("")
    io.open(os.path.join(dest, "__init__.py"), "w", encoding="utf-8").write("")
    io.open(os.path.join(LUCRARE, ".gitignore"), "w", encoding="utf-8").write(
        "__pycache__/" + chr(10) + "*.pyc" + chr(10) + "venv/" + chr(10) +
        ".venv/" + chr(10))

    antet = ("# -*- coding: utf-8 -*-" + chr(10) +
             '"""Laboratorul 9 - inventar macOS de procese și evenimente."""' +
             chr(10) + "import json" + chr(10) +
             "from dataclasses import dataclass, asdict" + chr(10) + chr(10) +
             "CAI_SUSPECTE = (" + repr("/Library/LaunchAgents/") + ", " +
             repr("/Users/ana/Library/Caches/") + ")" +
             chr(10) + "SUSPECTE_ID = {1001, 1002, 1003}" + chr(10) + chr(10) + chr(10))
    io.open(os.path.join(dest, "inventar.py"), "w", encoding="utf-8").write(
        antet + corp + MAIN_INVENTAR)
    io.open(os.path.join(dest, "test_inventar.py"), "w", encoding="utf-8").write(CODA_TEST)

    sdest = os.path.join(dest, "start")
    os.makedirs(sdest, exist_ok=True)
    json.dump(PROCESE, io.open(os.path.join(sdest, "procese.json"), "w",
              encoding="utf-8"), indent=2, ensure_ascii=False)
    json.dump(EVENIMENTE, io.open(os.path.join(sdest, "evenimente.json"), "w",
              encoding="utf-8"), indent=2, ensure_ascii=False)

    titlu("PACHETUL DE PREDARE ESTE PREGĂTIT")
    print()
    print("   Am creat următoarele fișiere:")
    print()
    print("      Laborator_9/arsenal/macos/inventar.py       clasele și raportul")
    print("      Laborator_9/arsenal/macos/test_inventar.py  verificări")
    print("      Laborator_9/arsenal/macos/start/            datele JSON")
    print()
    if nerezolvate:
        linie("!")
        print("  ATENȚIE. Mai ai de rezolvat sarcinile: " +
              ", ".join(str(x) for x in nerezolvate))
        print("  Până le termini, comanda de mai jos se va opri la")
        print("  prima metodă neimplementată.")
        linie("!")
        print()
    print("   Verifică-l astfel:")
    print()
    print("      cd Laborator_9")
    print("      python3 -m arsenal.macos.inventar arsenal/macos/start")
    print()
    print("   Apoi încarcă fișierele în depozitul tău:")
    print()
    print("      git add Laborator_9")
    print('      git commit -m "Laboratorul 9: obiecte și clase"')
    print("      git push")


def deschide_sarcina(stare, numar):
    s, reusit, mesaj = stare[numar - 1]
    arata_sarcina(s, reusit, mesaj)
    print()
    print("   Apasă Enter după ce salvezi fișierul, pentru a verifica din nou.")
    asteapta()


def main():
    if pregateste_capturile():
        print()
        print("   Am creat folderul start/ cu fișierele JSON.")

    while True:
        stare, eroare = stare_completa()
        if stare is None:
            titlu("CODUL TĂU NU POATE FI CITIT", "!")
            print()
            for r in eroare.split(chr(10)):
                print("   " + r)
            print()
            print("   Corectează codul și apasă Enter.")
            asteapta()
            continue

        arata_progres(stare)
        print()
        print("   Introdu numărul unei sarcini (1-%d) pentru detalii." % len(SARCINI))
        print()
        print("   Enter  verifică din nou toate sarcinile")
        print("   p      pregătește pachetul de predare")
        print("   c      instrucțiuni de lucru")
        print("   i      ieșire")
        print()
        print("   Alege o opțiune: ", end="")
        try:
            op = input().strip().lower()
        except EOFError:
            iesire_fara_terminal()
        except KeyboardInterrupt:
            break

        if op.isdigit():
            numar = int(op)
            if 1 <= numar <= len(SARCINI):
                deschide_sarcina(stare, numar)
            else:
                print()
                print("   Sarcinile sunt numerotate de la 1 la %d." % len(SARCINI))
                print("   Apasă Enter.")
                asteapta()
        elif op == "p":
            pregateste_predarea(stare)
            print()
            print("   Apasă Enter.")
            asteapta()
        elif op == "c":
            instructiuni()
            print("   Apasă Enter.")
            asteapta()
        elif op == "i":
            break


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except KeyboardInterrupt:
        print()
        print("   Program întrerupt. Codul tău rămâne salvat în fișier.")
    except Exception as _e:
        print()
        print("   A apărut o eroare neașteptată în program:")
        print("   " + type(_e).__name__ + ": " + str(_e))
        _tine_fereastra_deschisa()
