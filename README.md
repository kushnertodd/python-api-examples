# Python API Examples

These examples also [here](https://www.dropbox.com/scl/fo/xc065ron8h8pptusbtbg8/h?rlkey=yu89g3bzhujg1hxfumrlmjpg6&dl=0).

I have something that's interesting and educational! Have you used JSON? Magic has an API that gives Magic information when you send JSON requests that's described at this site:
https://docs.magicthegathering.io/
You should be able to type this at DOS and get the card types:
```
C:>curl "https://api.magicthegathering.io/v1/types"
{"types":["Artifact","Battle","Conspiracy","Creature","Dragon","Elemental","Enchantment","Goblin","Hero","instant","Instant","Jaguar","Knights","Land","Phenomenon","Plane","Planeswalker","Scheme","Sorcery","Stickers","Summon","Tribal","Universewalker","Vanguard","Wolf"]}
```
Take a look and see what you think.

- How do I parse  that file into human-readable form using python? I'm glad you asked. Make sure you have python installed from https://www.python.org and run json-format.bat in dos.

json-format.py

import sys
import json

if len(sys.argv) < 2:
    print(f'usage: {sys.argv[0]} filename')
    sys.exit(0)	

json-format.bat

curl "https://api.magicthegathering.io/v1/types">types.txt
type types.txt
python json-format.py
python json-format.py types.txt

- Now you're going to say How do I parse that into data in a usable python form? I'm glad you asked that too. The json is actually loaded into a dictionary that has "types" as the key and the list of types as the value . json-parse.bat strips the "types" off the json and just prints the list of types. Let me know what you think.

json-parse.py

import sys
import json

if len(sys.argv) < 2:
    print(f'usage: {sys.argv[0]} filename')
    sys.exit(0)	

json-parse.bat

curl "https://api.magicthegathering.io/v1/types">types.txt
type types.txt
python json-parse.py types.txt

- Now you're going to say Sure, that's fine if I want to get  a fixed set of data from a json request, but suppose I want to specify the thing to get the json for and print out a specific set of data for that thing? json-http-requests-name.bat will get the mana cost for a card you specify.

json-http-requests-name.py

import sys
import json
import requests

if len(sys.argv) < 2:
    print(f'usage: {sys.argv[0]} card-name')

json-http-requests-name.bat

json-http-requests.bat

python json-http-requests-name.py "'Cho-Manno, Revolutionary'"

- You want to know what kind of data you can get for a specific card? You can capture all the request json with this command:
C:>curl "https://api.magicthegathering.io/v1/cards?supertypes=legendary&types=creature">card.txt
and copy and paste that text into this web page:
https://jsonformatter.org/
and it will show the information for "Cho-Manna, Revolutionary" as the first entry:

{
  "cards": [
    {
      "name": "Cho-Manno, Revolutionary",
      "manaCost": "{2}{W}{W}",
      "cmc": 4,
      "colors": [
        "W"
      ],
      "colorIdentity": [
        "W"
      ],
...

- You can then print out what data you want by changing  json-http-requests-name.py to print the data you want:
print(f'supertype for {card_name} is:\n{json_object["cards"][0]["supertypes"]}') 

- You can get data for a list of fields with json-http-requests-name-list.bat.

json-http-requests-name-list.py

import sys
import json
import requests

if len(sys.argv) < 2:
    print(f'usage: {sys.argv[0]} card-name')

import sys
import json
import requests

if len(sys.argv) < 2:
    print(f'usage: {sys.argv[0]} card-name')

json-http-requests-name-list.bat

python json-http-requests-name-list.py "'Cho-Manno, Revolutionary'

- you can also put the address in chrome to see the data https://api.magicthegathering.io/v1/types

https://api.magicthegathering.io/v1/types


json-http-requests.py


import sys
import json
import requests

# this code is from:
#  https://stackoverflow.com/questions/26000336/execute-curl-command-within-a-python-script

res = requests.get('https://api.magicthegathering.io/v1/types')
print(f'original api response is:\n{res.text}\n')

json_object = json.loads(res.text)

print(f'parsed json for "types" is:\n{json_object["types"]}')

json-http-requests.bat

python json-http-requests.py

