import requests
import config
import json
import time

BASE_URL = "https://cat-fact/facts/random"

#https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1
#https://cat-fact.herokuapp.com/#/facts/random?animal_type=cat&amount=1
#/facts/random?animal_type=cat&amount=2
#response = requests.get(BASE_URL)

#if response.status_code == 200:
# data = response.json()
#  info = data['text']

# print(data)
    
#else:
# print("An error occurred.")

print("test")
data = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1')
print(data.json())