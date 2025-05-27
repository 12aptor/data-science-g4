from prefect import flow, task
import requests
from datetime import datetime

#creamos una tarea
@task
def extract():
    url = "https://randomuser.me/api/?results=1"
    response = requests.get(url)
    data = response.json()
    return data['results']

@task
def transform(users):
    # Aquí podrías realizar transformaciones adicionales si es necesario
    transformed_users = []
    for user in users:
       nombre = f"{user['name']['first']} {user['name']['last']}"
       sexo = user['gender']
       pais = user['location']['country']
       fecha_nac = user['dob']['date']
       fecha_nac = datetime.fromisoformat(fecha_nac.rstrip("Z")).date()
       transformed_users.append((nombre, sexo, pais, fecha_nac))
       
    return transformed_users

@flow(name="ETL Random User")
def etl_random_user():
    users = extract()
    transformed_users = transform(users)
    print("Transformed Users:",transformed_users)
    
if __name__ == "__main__":
    etl_random_user()
    print(f"ETL Random User completed at {datetime.now()}")