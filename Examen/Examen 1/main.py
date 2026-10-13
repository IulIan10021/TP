from urllib.parse import urlsplit
from checker import (
    SITES,
    build_url,
    is_https,
    show_response,
    check_site,
    scan_sites,
    check_headers,
    retry_check,
)

def main():
    host = urlsplit(SITES[0]).netloc
    path = urlsplit(SITES[1]).path

    print("\n Partea 1: Funcții ajutătoare ")
    print("build_url, cale fără /:", build_url(host, path.lstrip("/")))
    print("build_url, cale cu /:", build_url(host, path))
    print("is_https, HTTPS:", is_https(SITES[0]))
    print("is_https, HTTP:", is_https(SITES[9]))

    print("\nPartea 2: Trimiterea cererii ")
    print("Site obișnuit:", SITES[0])
    show_response(SITES[0])
    print("\nSite inexistent:", SITES[9])
    show_response(SITES[9])

    print("\n Partea 3: Verificarea fiecărei adrese ")
    for url in SITES:
        print("check_site:", url, "->", check_site(url))

    print("\n Partea 4: Scanarea site-urilor ")
    scan_sites()

    print("\n Partea 5: Anteturi de securitate ")
    for index in (0, 10, 11, 9):
        url = SITES[index]
        print("check_headers:", url, "->", check_headers(url))

    print("\nPartea 6: Încercări repetate ")
    print("Status 200:", retry_check(SITES[3]))
    print("Status 404, oprire după prima cerere:", retry_check(SITES[6]))
    print("Status 500, maximum 3 încercări:", retry_check(SITES[7]))
    print("Status 500, maximum 2 încercări:", retry_check(SITES[7], attempts=2))
    print("Site inexistent:", retry_check(SITES[9]))
    print("Status aleatoriu 200 sau 500:", retry_check(SITES[12]))

if __name__ == "__main__":
    main()
