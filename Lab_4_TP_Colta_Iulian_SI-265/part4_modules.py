
import requests
import time
import re
import hashlib
import json
import socket
import ssl

from datetime import datetime, timezone
from urllib.parse import urlparse, urljoin
from html.parser import HTMLParser

BASE_URL = "https://cybercor.org"
TIMEOUT = 10


# Itemul 35
def parse_url(url):
    """Descompune un URL in componente."""
    rezultat = urlparse(url)

    print("Schema:", rezultat.scheme)
    print("Domeniu:", rezultat.netloc)
    print("Cale:", rezultat.path)
    print("Query:", rezultat.query)
    print("Fragment:", rezultat.fragment)


print("\nItemul 35")
parse_url("https://cybercor.org/path?x=1#top")


# Itemul 36
def complete_urls(base, links):
    """Transforma linkurile relative in URL-uri complete."""
    rezultate = []

    for link in links:
        rezultate.append(urljoin(base, link))

    return rezultate


print("\nItemul 36")

links = ["/about", "contact.html", "../index.html"]

for link in complete_urls(BASE_URL, links):
    print(link)


# Itemul 37
def extract_links(html):
    """Extrage linkurile href fara duplicate."""
    links = re.findall(r'href="([^"]+)"', html)

    return list(dict.fromkeys(links))


print("\nItemul 37")

response = requests.get(BASE_URL, timeout=TIMEOUT)
links = extract_links(response.text)

print("Numar linkuri:", len(links))
for link in links:
    print(link)


# Itemul 38
def split_links(links, domain):
    """Separa linkurile interne de cele externe."""
    interne = []
    externe = []

    base = "https://" + domain

    for link in links:
        url_complet = urljoin(base, link)
        domeniu_link = urlparse(url_complet).netloc

        if domeniu_link == domain:
            interne.append(url_complet)
        else:
            externe.append(url_complet)

    return interne, externe


print("\nItemul 38")

interne, externe = split_links(links, "cybercor.org")

print("Linkuri interne:", len(interne))
print("Linkuri externe:", len(externe))


# Itemul 39
class ImageFinder(HTMLParser):
    """Gaseste sursele imaginilor din codul HTML."""

    def __init__(self):
        super().__init__()
        self.images = []

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            src = dict(attrs).get("src")

            if src is not None:
                self.images.append(src)


print("\nItemul 39")

test_html = """
<html><body>
  <img src="/logo.png" alt="Logo">
  <IMG SRC="poza.jpg">
  <img alt="imagine fara src">
  <img src="https://cdn.example.com/banner.webp" />
  <a href="/despre">Aceasta nu este o imagine</a>
</body></html>
"""

finder = ImageFinder()
finder.feed(test_html)

print("Imagini din test:", finder.images)

assert finder.images == [
    "/logo.png",
    "poza.jpg",
    "https://cdn.example.com/banner.webp"
], "Parserul nu a gasit exact imaginile asteptate"

print("Testul a trecut!")

finder = ImageFinder()
finder.feed(response.text)

print("Imagini gasite pe site:", len(finder.images))

for src in finder.images:
    print(src)

print("Taguri img in HTML:",
      response.text.lower().count("<img"))


# Itemul 40
def page_fingerprint(url):
    """Calculeaza amprenta SHA-256 a continutului paginii."""
    response = requests.get(url, timeout=TIMEOUT)
    response.raise_for_status()

    return hashlib.sha256(response.content).hexdigest()


print("\nItemul 40")

time.sleep(1)
hash1 = page_fingerprint(BASE_URL)

time.sleep(1)
hash2 = page_fingerprint(BASE_URL)

print("Prima amprenta:", hash1)
print("A doua amprenta:", hash2)
print("Sunt identice:", hash1 == hash2)

# Amprentele pot fi diferite daca pagina isi modifica
# continutul intre cele doua cereri.


# Itemul 41
def save_headers(url):
    """Salveaza antetele HTTP in JSON si le citeste inapoi."""
    response = requests.get(url, timeout=TIMEOUT)

    with open("headers.json", "w", encoding="utf-8") as file:
        json.dump(dict(response.headers), file, indent=2)

    with open("headers.json", "r", encoding="utf-8") as file:
        date = json.load(file)

    print("Fisierul headers.json a fost creat.")
    print("Content-Type:", date.get("Content-Type", "lipseste"))


print("\nItemul 41")

time.sleep(1)
save_headers(BASE_URL)


# Itemul 42
def resolve(hostname):
    """Returneaza adresa IPv4 a unui domeniu."""
    return socket.gethostbyname(hostname)


print("\nItemul 42")

try:
    ip = resolve("cybercor.org")
    print("Adresa IP:", ip)
except socket.gaierror as eroare:
    print("Eroare DNS:", eroare)


# Itemul 43
def cert_days_left(hostname):
    """Returneaza zilele ramase pana la expirarea certificatului."""
    context = ssl.create_default_context()

    with socket.create_connection(
        (hostname, 443), timeout=TIMEOUT
    ) as sock:

        with context.wrap_socket(
            sock, server_hostname=hostname
        ) as secure_sock:

            certificat = secure_sock.getpeercert()
            data_expirare = certificat["notAfter"]

    timestamp = ssl.cert_time_to_seconds(data_expirare)
    expirare = datetime.fromtimestamp(timestamp, timezone.utc)
    acum = datetime.now(timezone.utc)

    diferenta = expirare - acum

    return diferenta.days


print("\nItemul 43")

try:
    zile = cert_days_left("cybercor.org")
    print("Zile ramase:", zile)
except (OSError, ssl.SSLError, KeyError, ValueError) as eroare:
    print("Eroare certificat:", eroare)


print("\nPartea 4 a fost executata.")
