from locale import format_string
from urllib import request, response
import requests
import config

BASE_URL = "https://cat-fact/facts/random"



response = requests.get(BASE_URL)

if response.status_code == 200:
    data = response.json()
    info = data["text"]

    print(data)
    print(data)

    print(data)
else:
    print("An error occurred.")