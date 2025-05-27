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

@flow(name="ETL Random User")
def etl_random_user():
    users = extract()
    print(users)
    
if __name__ == "__main__":
    etl_random_user()
    print(f"ETL Random User completed at {datetime.now()}")