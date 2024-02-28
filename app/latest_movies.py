from dotenv import load_dotenv
from configs import latest_url
from pprint import pprint
import requests
import os

load_dotenv()

def get_latest_movies_data():
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.getenv('ACCESS_TOKEN')}"
    }
    response = requests.get(latest_url, headers=headers)
    data = response.json()
    return data

if __name__ == "__main__":
    pprint(get_latest_movies_data())