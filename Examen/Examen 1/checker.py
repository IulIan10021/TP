import requests

SITES = [
    "https://example.com",
    "https://httpbin.org/html",
    "https://httpbin.org/json",
    "https://httpbin.org/status/200",
    "https://httpbin.org/redirect/1",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/status/404",
    "https://httpbin.org/status/500",
    "https://httpbin.org/delay/10",
    "http://this-site-does-not-exist.invalid",
    "https://httpbin.org/response-headers?X-Frame-Options=DENY&X-Content-Type-Options=nosniff",
    "https://httpbin.org/response-headers?x-frame-options=DENY",
    "https://httpbin.org/status/200,500",
]

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
]

def build_url(host, path):
    return "https://" + host.rstrip("/") + "/" + path.lstrip("/")

def is_https(url):
    return url.startswith("https://")

def show_response(url):
    try:
        response = requests.get(url, timeout=5)
        print("Status:", response.status_code)
        print("Content-Type:", response.headers.get("Content-Type", "unknown"))
    except requests.RequestException as error:
        print("Eroare:", str(error))

def check_site(url):
    try:
        response = requests.get(url, timeout=5)
        return {
            "status": response.status_code,
            "content_type": response.headers.get("Content-Type", "unknown"),
            "length": len(response.content),
            "server": response.headers.get("Server", "unknown"),
        }
    except requests.RequestException as error:
        return {"status": None, "error": str(error)}

def scan_sites():
    results = []
    for url in SITES:
        result = check_site(url)
        results.append((url, result))
    successful = [(url, result) for url, result in results if result["status"] == 200]
    successful.sort(key=lambda item: item[1]["length"], reverse=True)
    for url, result in successful:
        print(f"{url} -> 200, {result['length']} octeți")
    success_count = len(successful)
    failure_count = len(results) - success_count
    print(f"Reușite: {success_count} | Eșuate: {failure_count}")

def check_headers(url):
    try:
        response = requests.get(url, timeout=5)
        present = []
        missing = []
        for header in SECURITY_HEADERS:
            if header in response.headers:
                present.append(header)
            else:
                missing.append(header)
        score = len(present) * 100 // len(SECURITY_HEADERS)
        return {"present": present, "missing": missing, "score": score}
    except requests.RequestException as error:
        return {"status": None, "error": str(error)}

def retry_check(url, attempts=3):
    status = None
    error = None
    count = 0
    for _ in range(max(0, attempts)):
        count += 1
        try:
            response = requests.get(url, timeout=5)
            status = response.status_code
            if status < 500:
                return {"status": status, "attempts": count}
        except requests.RequestException as request_error:
            error = str(request_error)
    result = {"status": status, "attempts": count}
    if status is None and error is not None:
        result["error"] = error
    return result
