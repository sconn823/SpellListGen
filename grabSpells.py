import requests
import json

url = "http://www.dnd5eapi.co/api/spells"

response = requests.get(url)

print(response.json())

with open("spells.json", "w") as output:
    json.dump(response.json(), output)
