from prefect import task
import mysql.connector

@task
def load_jobs(jobs):
    print("CARGA DE OFERTAS DE LINKEDIN")
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="db_g4"
    )
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ofertas_laborales (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255),
            location VARCHAR(255),
            link TEXT,
            date DATE
        )
    """)

    for job in jobs:
        cursor.execute("""
            INSERT INTO ofertas_laborales (title, location, link, date)
            VALUES (%s, %s, %s, %s)
        """, (job["title"], job["location"], job["link"], job["date"]))

    conn.commit()
    cursor.close()
    conn.close()