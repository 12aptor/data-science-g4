import requests
from bs4 import BeautifulSoup

URL = 'https://www.sunat.gob.pe/'

response = requests.get(URL)

print(f'Status Code: {response.status_code}')