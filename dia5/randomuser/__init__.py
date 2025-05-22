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