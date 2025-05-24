import requests
from bs4 import BeautifulSoup

URL = 'https://neoauto.com/venta-de-autos-seminuevos'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(URL,headers=headers)
if response.status_code == 200:
    print('Conexión exitosa')
    soup = BeautifulSoup(response.content, 'html.parser')
    div_autos = soup.find_all('article', class_='c-results c-results-used--premium')
    for auto_soup in div_autos:
        # Título del auto
        titulo = auto_soup.find('h2', class_='c-results__header-title').get_text(strip=True)
        # Precio
        precio = auto_soup.find('div', class_='c-results-mount__price').get_text(strip=True)
        # Kilometraje
        kilometraje_tag = auto_soup.find('span', class_='c-results-used__subtitle-description')
        kilometraje = kilometraje_tag.find_next_sibling(text=True).strip() if kilometraje_tag else None
        # Ubicación
        ubicacion_tag = auto_soup.find('span', class_='c-results-details__description-text--highlighted')
        ubicacion = ubicacion_tag.get_text(strip=True) if ubicacion_tag else None
        # Combustible y transmisión
        desc_texts = auto_soup.find_all('p', class_='c-results-details__description-text')
        combustible = desc_texts[0].find('span', class_='c-results-used__detail-fuel').get_text(strip=True) if desc_texts else None
        transmision = desc_texts[0].get_text(strip=True).split('|')[-1].strip() if desc_texts else None
        # Imprime la información extraída
        print('Título:', titulo)
        print('Precio:', precio)
        print('Kilometraje:', kilometraje)
        print('Ubicación:', ubicacion)
        print('Combustible:', combustible)
        print('Transmisión:', transmision)
        print('---'*20)

else:
    print('Error en la conexión')
    print(response.status_code)
    print(response.reason)