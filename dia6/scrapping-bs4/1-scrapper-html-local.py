import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:5500/html/index.html"

response = requests.get(URL)
if response.status_code == 200:
    print("se cargo la pagina")
    soup = BeautifulSoup(response.content, "html.parser")
    print(soup.prettify())
else:
    print("Error al cargar la pagina")
    print(response.status_code)