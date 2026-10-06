import requests
import urllib.request
import time
import requests as rq
BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

# ITEMUL 3



response3 = rq.get(BASE_URL, timeout=TIMEOUT)
print("Status cu alias:", response3.status_code)

# Aliasul face codul mai scurt.
# Un alias neclar poate face codul mai greu de inteles.



# ITEMUL 4


response4 = urllib.request.urlopen(BASE_URL)

print("Status urllib:", response4.status)

continut = response4.read().decode("utf-8")

print("Primele 200 de caractere:")
print(continut[:200])



# ITEMUL 5


print("Continutul modulului requests:")
print(dir(requests))

# get - functie
# Session - clasa
# exceptions - modul



# ITEMUL 6


help(requests.get)

response6 = requests.get(BASE_URL, timeout=TIMEOUT)
print("Status item 6:", response6.status_code)



# ITEMUL 7

import time

start = time.perf_counter()

response7 = requests.get(BASE_URL, timeout=TIMEOUT)

stop = time.perf_counter()

print("Timp masurat:", stop - start, "secunde")
print("Response elapsed:", response7.elapsed.total_seconds(), "secunde")



# ITEMUL 8


try:
    import bs4
    print("bs4 este instalat")

except ImportError:
    print("bs4 nu este instalat")
    print("Pentru instalare: pip install beautifulsoup4")