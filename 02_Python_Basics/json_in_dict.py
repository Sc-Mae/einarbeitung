import json


with open('Hero.json', 'r') as file:
    data = json.load(file)

print(data)
