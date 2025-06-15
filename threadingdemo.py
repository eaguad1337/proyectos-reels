import time
import requests
import threading

sitios = [
    "https://www.google.com",
    "https://www.facebook.com",
    "https://www.twitter.com",
    "https://www.instagram.com",
    "https://www.youtube.com",
]

def check_sitio(sitio):
    response = requests.get(sitio)
    if response.status_code == 200:
        print(f"{sitio} is up")
    else:
        print(f"{sitio} is down")

t1 = time.perf_counter()
for sitio in sitios:
    threading.Thread(check_sitio, args=(sitio,)).start()

while threading.active_count() > 1:
    time.sleep(0.5)

t2 = time.perf_counter()
print(f"Tiempo: {(t2 - t1):.2f} segundos")