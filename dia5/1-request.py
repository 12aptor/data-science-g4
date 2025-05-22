import requests

URL = 'https://randomuser.me/api/?results=2'

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    for usuario in data['results']:
        #print(usuario)
        print("="*50)
        print(f'Nombre : {usuario["name"]["first"]} {usuario["name"]["last"]}')
        print(f'Email : {usuario["email"]}')
        print(f'Ubicación : {usuario["location"]["city"]}, {usuario["location"]["country"]}')
        print(f'Fecha de nacimiento : {usuario["dob"]["date"]}')
        print(f'Imagen : {usuario["picture"]["large"]}')
else:
    print(f"Error: {response.status_code}")
    print(response.text)