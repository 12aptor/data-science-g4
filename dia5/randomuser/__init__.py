import requests
import mysql.connector

class RandomUser:
    def __init__(self):
        self.api_url = "https://randomuser.me/api/"
        
    def get_users(self, num_users=1):
        response = requests.get(f"{self.api_url}?results={num_users}")
        if response.status_code == 200:
            return response.json()['results']
        else:
            raise Exception("Failed to fetch data from API")
        
    def load_users_to_db(self, users):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='db_g4'
            )
            cursor = connection.cursor()
            
            # Create table if it doesn't exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255),
                    email VARCHAR(255),
                    city VARCHAR(255),
                    country VARCHAR(255),
                    dob DATE
                )
            """)
            connection.commit()
            
            for user in users:
                name = user['name']['first'] + " " + user['name']['last']
                email = user['email']
                city = user['location']['city']
                country = user['location']['country']
                dob = user['dob']['date'].split("T")[0]  # Get only the date part
                
                cursor.execute("""
                    INSERT INTO users (name, email, city, country, dob)
                    VALUES (%s, %s, %s, %s, %s)
                """, (name, email, city, country, dob))
            
            connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()