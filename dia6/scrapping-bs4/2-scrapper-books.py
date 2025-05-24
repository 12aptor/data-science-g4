import requests
from bs4 import BeautifulSoup

URL = 'http://books.toscrape.com/'

response = requests.get(URL)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    for book in books:
        print('-------------')
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        image_url = book.img['src']
        print(f'Title: {title}')
        print(f'Price: {price}')
        print(f'Image URL: {URL + image_url}')
        print('-------------')
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
    exit()