import requests

OUTPUT_PATH = "Desktop/data.json"

data = {}

counter = 1
while True:
    print(counter)
    req = requests.get("https://pokeapi.co/api/v2/pokemon-species/" + str(counter))
    if req.status_code == 404:
        break
    else:
        counter += 1
        jason = req.json()

        data[jason["name"]] = jason["flavor_text_entries"]


import json 
      

with open(OUTPUT_PATH, "w") as outfile:
    json.dump(data, outfile)