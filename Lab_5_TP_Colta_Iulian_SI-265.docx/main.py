"""Porneste toate etapele laboratorului 5: python main.py."""

import importlib.util
import subprocess
import sys
from pathlib import Path


RADACINA = Path(__file__).resolve().parent


def main():
    python = sys.executable
    if importlib.util.find_spec("PIL") is None:
        python_local = RADACINA / ".venv" / "bin" / "python"
        if not python_local.is_file():
            print(
                "Lipseste biblioteca Pillow. Instaleaz-o cu: "
                f'"{sys.executable}" -m pip install Pillow',
                file=sys.stderr,
            )
            return 1
        python = str(python_local)

    print("Pornire laborator 5: decodare, hashuri, analiza si steganografie...", flush=True)
    proces = subprocess.run(
        [python, str(RADACINA / "ruleaza_demo.py")], cwd=RADACINA
    )
    raport = RADACINA / "output_demo.txt"
    if raport.is_file():
        print(raport.read_text(encoding="utf-8"), flush=True)
    if proces.returncode:
        print("Executia a esuat. Consulta mesajele de mai sus.", file=sys.stderr)
        return proces.returncode

    print(f"Laborator finalizat. Raport complet: {raport}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
