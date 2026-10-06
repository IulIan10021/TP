from wsgiref.simple_server import server_version

import requests

BASE_URL = "https://cybercor.org"
ECHO_URL = "https://httpbin.org"
TIMEOUT = 10

# Itemul 9
response = requests.get(BASE_URL, timeout=TIMEOUT)

print("Status code", response.status_code)
print("OK", response.ok)
print("URL", response.url)
print("Encoding", response.encoding)


# Itemul 10
try:
    response = requests.get(ECHO_URL + "/status/404", timeout=TIMEOUT)

    print("Status code", response.status_code)
    response.raise_for_status()

except requests.exceptions.HTTPError as eroare:
    print("Eroare HTTP:", eroare)


# Itemul 11
response=requests.get(BASE_URL,timeout=TIMEOUT)
print("Primele 200 caractere")
print(response.text[:200])

# Itemul 12
response=requests.get(BASE_URL,timeout=TIMEOUT)
content_type=response.headers.get("Content-type")
server=response.headers.get("server")

print("Content-Type:",content_type)

if server:
      print("Server", server)
else:
     print("Denumire server nu este trimisa pe site")

print("\nToate headerurile primite")

for nume,valoare in  response.headers.items():
    print(nume, ":",valoare)

#Itemul 13

response=requests.get(BASE_URL,timeout=TIMEOUT)
print("Lungimea continutului",len(response.content),bytes)

#Itemul 14

response=requests.get(ECHO_URL+"/get",timeout=TIMEOUT)
date_json=response.json()
print("date json")
print(date_json)

print("Tipul date",type(date_json))

#Itemul 15
parametri={
    "nume":"Iulian",
    "grupa":"SI-265"
}
response=requests.get(
    ECHO_URL+"/get",
    params=parametri,
    timeout=TIMEOUT
)
print("URL cu parametri",response.url)
print("Parametri",response.json()["args"])

#Itemul 16

headers={
    "User-Agent":"Student"
}
response=requests.get(
    ECHO_URL+"/headers",
    headers=headers,
    timeout=TIMEOUT
)
print("headers primite de la server")
print(response.json())


#Itemul 17

response=requests.head(BASE_URL,timeout=TIMEOUT)
print("Status head",response.status_code)
print("Content-type",response.headers.get("Content-type"))
print("Lungiea la body",len(response.content))


#Itemul 18
    
response = requests.get(
    ECHO_URL + "/redirect/1",
    timeout=TIMEOUT
)

print("URL final:", response.url)
print("Numar de redirectari:", len(response.history))

#Itemul 19

response = requests.get(BASE_URL, timeout=TIMEOUT)

timp = response.elapsed.total_seconds()

print("Timpul de raspuns:", timp, "secunde")

# Itemul 20

session = requests.Session()

session.get(
    ECHO_URL + "/cookies/set/nume/Iulian",
    timeout=TIMEOUT
)

response = session.get(
    ECHO_URL + "/cookies",
    timeout=TIMEOUT
)

print("Cookie-uri salvate:")
print(response.json())