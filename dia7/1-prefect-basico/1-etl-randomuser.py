from prefect import flow, task
import requests
from datetime import datetime
import mysql.connector

#creamos una tarea
@task
def extract():
    url = "https://randomuser.me/api/?results=10"
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

@task
def load(users):
   conn = mysql.connector.connect(
       host="localhost",
       user="root",
       password="root",
       database="db_g4"
   )
   cursor = conn.cursor()
   cursor.execute("""
               CREATE TABLE IF NOT EXISTS random_users (
               id INT AUTO_INCREMENT PRIMARY KEY,
               nombre VARCHAR(255),
               sexo VARCHAR(10),
               pais VARCHAR(100),
               fecha_nac DATE)
               """)
   conn.commit()
   insert_query = "INSERT INTO random_users (nombre, sexo, pais, fecha_nac) VALUES (%s, %s, %s, %s)"
   cursor.executemany(insert_query, users)
   conn.commit()
   print(f" {cursor.rowcount} registros insertados en la tabla random_users")
   cursor.close()
   conn.close()

@flow(name="ETL Random User")
def etl_random_user():
    users = extract()
    transformed_users = transform(users)
    load(transformed_users)
    
if __name__ == "__main__":
    etl_random_user()
    print(f"ETL Random User completed at {datetime.now()}")