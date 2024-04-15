import sys
import json
import requests

if len(sys.argv) < 2:
    print(f'usage: {sys.argv[0]} card-name')
    sys.exit(0)	

card_name = sys.argv[1]

res = requests.get('https://api.magicthegathering.io/v1/cards?supertypes=legendary&types=creature')
#print(f'original api response is:\n{res.text}\n')

json_object = json.loads(res.text)

print(f'mana cost for {card_name} is:\n{json_object["cards"][0]["manaCost"]}')
