import requests
from bs4 import BeautifulSoup
import mysql.connector
import re

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='db_g4'
)

cursor = conn.cursor()
# Crear la tabla si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS autos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255),
    precio DOUBLE,
    kilometraje VARCHAR(50),
    ubicacion VARCHAR(255),
    combustible VARCHAR(50),
    transmision VARCHAR(50),
    enlace LONGTEXT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
''')
conn.commit()

URL = 'https://neoauto.com/venta-de-autos-seminuevos'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
total_paginas = 1

response_pages = requests.get(URL, headers=headers)
if response_pages.status_code == 200:
    pages_soup = BeautifulSoup(response_pages.content, 'html.parser')
    # Encuentra el número total de páginas
    last_page_link = pages_soup.find('a', class_='c-pagination-content__last-page')
    match = re.search(r'page=(\d+)', last_page_link['href']) if last_page_link else None
    total_paginas = int(match.group(1)) if match else 1
    print(f'Número total de páginas: {total_paginas}')

for pagina in range(1, total_paginas +1):
    URL = f'{URL}?page={pagina}'
    print(f'Conectando a la página {pagina}...')
    # Realiza la solicitud HTTP
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
            enlace = auto_soup.find('a', class_='c-results__link')['href'] if auto_soup.find('a', class_='c-results__link') else None
            enlace = URL + enlace
            # Imprime la información extraída
            precio = precio.replace(' ', '')
            precio = float(precio.replace('US$', '').replace(',', '').strip())
            # print('Título:', titulo)
            # print('Precio:', precio)
            # print('enlace:', enlace)
            # print('---'*20)
            
            cursor.execute('''
            INSERT INTO autos (titulo, precio, kilometraje, ubicacion, combustible, transmision,enlace)
            values (%s, %s, %s, %s, %s, %s,%s)
            ''', (titulo, precio, kilometraje, ubicacion, combustible, transmision,enlace))
            
            conn.commit()
        print('Datos insertados correctamente')

else:
    print('Error en la conexión')
    print(response.status_code)
    print(response.reason)