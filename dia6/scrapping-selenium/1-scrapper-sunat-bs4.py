import requests
from bs4 import BeautifulSoup

URL = 'https://www.sunat.gob.pe/'

response = requests.get(URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    precio_venta = soup.find('strong',id='sell-rate')
    print(f'precio venta dolares : {precio_venta.get_text()}')