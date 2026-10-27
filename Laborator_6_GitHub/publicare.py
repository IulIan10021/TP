"""Finalizează publicarea laboratorului 6, păstrând istoriile existente.

Rulare din terminal: python3 Laborator_6_GitHub/publicare.py --publica
Necesită conexiune la GitHub și autentificare prin gh auth login.
"""

import argparse
import base64
from email import policy
from email.message import EmailMessage
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import zipfile


ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / "Laborator_6_GitHub"
OWNER = "IulIan10021"
COURSE = "TP_Colta_Iulian_SI-265"
TEACHER = "cristiangonceari-dotcom"


def run(*args, cwd=ROOT, capture=False, input_text=None):
    result = subprocess.run(
        args, cwd=cwd, text=True, input=input_text,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.PIPE if capture else None,
        timeout=180, check=False,
    )
    if result.returncode:
        detail = (result.stderr or "").strip()
        raise RuntimeError(f"Comanda {args[0]} {args[1]} a eșuat. {detail}")
    return result.stdout.strip() if capture else ""


def api(endpoint, data=None):
    args = ["gh", "api", endpoint]
    if data is not None:
        args += ["--method", "PUT", "--input", "-"]
    output = run(*args, capture=True,
                 input_text=json.dumps(data) if data is not None else None)
    return json.loads(output) if output else None


def verify_exercise(name, count):
    info = api(f"repos/{OWNER}/{name}")
    if info["private"]:
        raise RuntimeError(f"{name} trebuie să fie Public.")
    entries = api(f"repos/{OWNER}/{name}/contents?ref=main")
    files = {entry["name"] for entry in entries}
    required = {"README.md"}
    if name == "exercitiu-git":
        required |= {"salut.py", ".gitignore"}
    if not required <= files:
        raise RuntimeError(f"Lipsesc fișiere în {name}: {required - files}")
    commits = api(f"repos/{OWNER}/{name}/commits?sha=main&per_page=100")
    if len(commits) < count:
        raise RuntimeError(f"Istoric insuficient în {name}.")


def update_reports():
    old = f"https://github.com/{OWNER}/TP"
    new = f"https://github.com/{OWNER}/{COURSE}"
    replacements = {
        "Am clonat depozitul local de exercițiu și am verificat fișierele din copia de lucru.":
            "Am clonat depozitul public exercitiu-git de pe GitHub și am verificat fișierele din copia de lucru.",
        "Am modificat README.md într-o a doua copie locală și am preluat schimbarea prin origin comun.":
            "Am actualizat README.md pe GitHub prin API și am preluat schimbarea în copia locală prin git pull.",
    }
    report = LAB / "L6_TP_Colta_Iulian_SI-265.md"
    text = re.sub(re.escape(old) + r"(?![\w-])", new, report.read_text())
    for before, after in replacements.items():
        text = text.replace(before, after)
    report.write_text(text)
    word = ROOT / "Lab_6_TP_Colta_Iulian_SI-265.docx"
    with zipfile.ZipFile(word) as archive:
        entries = [(info, archive.read(info.filename)) for info in archive.infolist()]
    with zipfile.ZipFile(word, "w") as archive:
        for info, data in entries:
            if info.filename == "word/document.xml":
                data = re.sub(re.escape(old) + r"(?![\w-])", new, data.decode()).encode()
            archive.writestr(info, data)
    return report, word


def publish():
    # Toate verificările de acces preced modificările depozitelor.
    user = api("user")
    if user["login"].lower() != OWNER.lower():
        raise RuntimeError(f"Autentifică-te în contul {OWNER}.")
    repositories = json.loads(run(
        "gh", "repo", "list", OWNER, "--limit", "1000", "--json", "name",
        capture=True,
    ))
    names = {repo["name"] for repo in repositories}
    origin = run("git", "remote", "get-url", "origin", capture=True)
    allowed = {
        f"https://github.com/{OWNER}/{name}.git"
        for name in ("TP", COURSE)
    }
    if origin not in allowed:
        raise RuntimeError("Origin diferă de depozitul disciplinei așteptat.")
    if COURSE in names and "TP" in names:
        raise RuntimeError("Există ambele depozite TP și TP_Colta_Iulian_SI-265; verifică destinația înainte de continuare.")
    if run("git", "diff", "--cached", "--name-only", capture=True):
        raise RuntimeError("Există fișiere pregătite pentru alt commit; salvează-le înainte de publicare.")
    run("gh", "auth", "setup-git", "--hostname", "github.com")

    with tempfile.TemporaryDirectory(prefix="l6-publicare-") as temporary:
        temporary = Path(temporary)
        for name, count in (("exercitiu-git", 4), ("exercitiu-2", 1)):
            clone = temporary / name
            run("git", "clone", str(LAB / "exemple" / (name + ".bundle")), str(clone))
            if name not in names:
                run("gh", "repo", "create", f"{OWNER}/{name}", "--public")
            elif api(f"repos/{OWNER}/{name}")["private"]:
                raise RuntimeError(f"{name} există deja ca depozit privat; verifică înainte de a-l face public.")
            run("git", "remote", "set-url", "origin",
                f"https://github.com/{OWNER}/{name}.git", cwd=clone)
            # Un istoric remote diferit produce refuz; nu se folosește force push.
            remote_head = run("git", "ls-remote", "origin", "refs/heads/main", cwd=clone, capture=True)
            if remote_head:
                run("git", "pull", "--ff-only", "origin", "main", cwd=clone)
            run("git", "push", "-u", "origin", "main", cwd=clone)
            if name == "exercitiu-git":
                endpoint = f"repos/{OWNER}/{name}/contents/README.md"
                readme = api(endpoint + "?ref=main")
                content = base64.b64decode(readme["content"]).decode()
                marker = "Exerciții de versionare pentru laboratorul 6."
                if marker not in content:
                    content = content.rstrip() + "\n" + marker + "\n"
                    api(endpoint, {
                        "message": "Actualizez README pe GitHub pentru exercitiul pull",
                        "sha": readme["sha"], "branch": "main",
                        "content": base64.b64encode(content.encode()).decode(),
                    })
                run("git", "pull", "--ff-only", "origin", "main", cwd=clone)
                run("python3", "salut.py", cwd=clone)
                run("git", "clone", f"https://github.com/{OWNER}/{name}.git",
                    str(temporary / "clonare-github"))
            verify_exercise(name, count)

    if COURSE not in names:
        if "TP" not in names:
            raise RuntimeError("Depozitul disciplinei TP nu a fost găsit.")
        run("gh", "repo", "rename", COURSE, "--repo", f"{OWNER}/TP", "--yes")
    info = api(f"repos/{OWNER}/{COURSE}")
    if not info["private"]:
        run("gh", "repo", "edit", f"{OWNER}/{COURSE}", "--visibility", "private")
    api(f"repos/{OWNER}/{COURSE}/collaborators/{TEACHER}", {"permission": "pull"})
    run("git", "remote", "set-url", "origin", f"https://github.com/{OWNER}/{COURSE}.git")
    report, word = update_reports()
    run("git", "add", "--", str(report), str(word))
    if run("git", "diff", "--cached", "--name-only", capture=True):
        run("git", "commit", "-m", "Actualizez linkurile dupa publicarea laboratorului 6")
    branch = run("git", "branch", "--show-current", capture=True)
    if not branch:
        raise RuntimeError("Selectează ramura de predare înainte de push.")
    run("git", "push", "-u", "origin", branch)
    local = run("git", "rev-parse", "HEAD", capture=True)
    remote = run("git", "ls-remote", "origin", f"refs/heads/{branch}", capture=True).split()[0]
    if local != remote:
        raise RuntimeError("Commitul online diferă de commitul local.")
    if not api(f"repos/{OWNER}/{COURSE}")["private"]:
        raise RuntimeError("Depozitul disciplinei trebuie să fie privat.")
    api(f"repos/{OWNER}/{COURSE}/contents/Laborator_6_GitHub/{report.name}?ref={branch}")
    access = api(f"repos/{OWNER}/{COURSE}/collaborators/{TEACHER}/permission")
    if access["permission"] not in {"read", "triage", "write", "maintain", "admin"}:
        print("Invitația profesorului a fost trimisă; accesul necesită acceptarea ei.")
    message = EmailMessage(policy=policy.SMTP)
    message["To"] = "cristian.gonceari@isa.utm.md"
    message["Subject"] = "L6_TP_Colta_Iulian_SI-265"
    message["X-Unsent"] = "1"
    message.set_content(
        "Bună ziua,\n\nSunt Colta Iulian, grupa SI-265. Vă transmit laboratorul 6.\n"
        f"Depozitul privat: https://github.com/{OWNER}/{COURSE}\n"
        f"Ultimul commit: {local}\n\nVă mulțumesc,\nColta Iulian\n"
    )
    draft = Path(tempfile.gettempdir()) / "L6_TP_Colta_Iulian_SI-265_DRAFT.eml"
    draft.write_bytes(message.as_bytes())
    print(f"Publicarea verificată. Commit: {local}\nE-mail pregătit, netrimis: {draft}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--publica", action="store_true", required=True,
                        help="Publică exercițiile, configurează depozitul privat și trimite commiturile.")
    parser.parse_args()
    try:
        publish()
    except (RuntimeError, OSError, ValueError, subprocess.TimeoutExpired) as error:
        print(f"Publicarea s-a oprit: {error}", file=sys.stderr)
        sys.exit(1)
