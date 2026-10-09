
import requests
import time

BASE_URL = "https://cybercor.org"
TIMEOUT = 10


# Itemul 21
def fetch(url, timeout=10):
    """Descarca pagina si returneaza raspunsul HTTP."""
    return requests.get(url, timeout=timeout)


response = fetch(BASE_URL)
print("Itemul 21:", response.status_code)

time.sleep(1)


# Itemul 22
def get_status(url: str) -> int:
    """Returneaza codul de stare HTTP."""
    response = fetch(url)
    return response.status_code


paths = ["/", "/robots.txt", "/sitemap.xml"]

for path in paths:
    print("Itemul 22:", path, get_status(BASE_URL + path))
    time.sleep(1)


# Itemul 23
# Functia fetch are timeout implicit de 10 secunde.
response = fetch(BASE_URL)
print("Itemul 23 - timeout implicit:", response.status_code)

time.sleep(1)

response = fetch(BASE_URL, timeout=3)
print("Itemul 23 - timeout 3:", response.status_code)

time.sleep(1)


# Itemul 24
def get_title(html):
    """Extrage titlul din codul HTML."""
    html_lower = html.lower()
    start = html_lower.find("<title>")
    end = html_lower.find("</title>")

    if start == -1 or end == -1:
        return None

    start += len("<title>")
    return html[start:end].strip()


response = fetch(BASE_URL)
print("Itemul 24:", get_title(response.text))


# Itemul 25
# Afisam documentatia functiei get_title.
print("\nItemul 25:")
help(get_title)


# Itemul 26
# get_status are adnotarile url: str si -> int.
# Adnotarile nu verifica automat tipurile la executie.

print("\nItemul 26:")
try:
    print(get_status(123))
except (requests.RequestException, TypeError, ValueError) as eroare:
    print("Eroare:", eroare)


# Itemul 27
def page_exists(url):
    """Returneaza True daca pagina poate fi accesata."""
    try:
        response = fetch(url)
        return response.status_code < 400
    except requests.RequestException:
        return False


print("Itemul 27:", page_exists(
    "https://this-domain-does-not-exist.invalid"
))


# Itemul 28
def check_paths(base, paths):
    """Verifica fiecare cale si returneaza codurile HTTP."""
    rezultate = {}

    for index, path in enumerate(paths):
        if index > 0:
            time.sleep(1)

        url = base.rstrip("/") + "/" + path.lstrip("/")

        try:
            rezultate[path] = get_status(url)
        except requests.RequestException:
            rezultate[path] = None

    return rezultate


time.sleep(1)
print("Itemul 28:", check_paths(BASE_URL, paths))


# Itemul 29
def get_header(url, name, default="lipsește"):
    """Returneaza valoarea unui antet HTTP."""
    response = fetch(url)
    return response.headers.get(name, default)


time.sleep(1)
print("Itemul 29:", get_header(BASE_URL, name="Server"))


# Itemul 30
def security_headers(url):
    """Verifica prezenta a cinci antete de securitate."""
    response = fetch(url)

    antete = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options",
        "X-Content-Type-Options",
        "Referrer-Policy"
    ]

    rezultate = {}

    for antet in antete:
        rezultate[antet] = antet in response.headers

    return rezultate


time.sleep(1)
rezultate = security_headers(BASE_URL)

print("\nItemul 30:")
for antet, prezent in rezultate.items():
    print(antet, ":", prezent)


# Itemul 31
def score_headers(results):
    """Returneaza scorul antetelor de securitate."""
    prezente = sum(results.values())
    total = len(results)
    return f"{prezente}/{total}"


print("Itemul 31:", score_headers(rezultate))


# Itemul 32
def fetch_robots(base):
    """Returneaza textul robots.txt sau None daca lipseste."""
    url = base.rstrip("/") + "/robots.txt"

    try:
        response = fetch(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException:
        return None


def disallowed_paths(robots_text):
    """Returneaza toate valorile Disallow din robots.txt."""
    if robots_text is None:
        return []

    rezultate = []

    for linie in robots_text.splitlines():
        linie = linie.strip()

        if linie.lower().startswith("disallow:"):
            valoare = linie.split(":", 1)[1].strip()
            rezultate.append(valoare)

    return rezultate


time.sleep(1)
robots = fetch_robots(BASE_URL)
print("Itemul 32:", disallowed_paths(robots))


# Itemul 33
def response_times(*urls):
    """Returneaza timpul de raspuns pentru fiecare URL."""
    rezultate = {}

    for index, url in enumerate(urls):
        if index > 0:
            time.sleep(1)

        try:
            response = fetch(url)
            rezultate[url] = response.elapsed.total_seconds()
        except requests.RequestException:
            rezultate[url] = None

    return rezultate


time.sleep(1)
timpi = response_times(
    BASE_URL,
    BASE_URL + "/robots.txt"
)
print("Itemul 33:", timpi)


# Itemul 34
def log(message, **details):
    """Afiseaza mesajul si detaliile primite."""
    rezultat = message

    for cheie, valoare in details.items():
        rezultat += f" | {cheie}={valoare}"

    print(rezultat)


print("Itemul 34:")
log("verificat", url=BASE_URL, status=200)
