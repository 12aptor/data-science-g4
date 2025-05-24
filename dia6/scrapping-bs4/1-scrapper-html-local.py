import requests
from bs4 import BeautifulSoup

URL = "http://127.0.0.1:5500/html/index.html"

response = requests.get(URL)
if response.status_code == 200:
    print("se cargo la pagina")
    soup = BeautifulSoup(response.content, "html.parser")
    #print(soup.prettify())
    articulo = soup.find("article")
    print(articulo)
    print(articulo.get_text())
    #enlaces
    enlaces = soup.find_all("a")
    print("Enlaces encontrados:")
    for enlace in enlaces:
        print(enlace.get_text())
        print(enlace["href"])
    imagen = soup.find("img")['src']
    print("Imagen encontrada:")
    print(imagen)
else:
    print("Error al cargar la pagina")
    print(response.status_code)