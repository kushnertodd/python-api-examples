# Python API Examples

Here is something that's interesting and educational! Have you used JSON? Magic has an API that gives Magic information when you send JSON requests that's described at this site:
```
https://docs.magicthegathering.io/
```
These are examples of using Python to read JSON from web APIs and process it.
To run them:
-  first download and install [git](https://git-scm.com/downloads) for Windows.
- then download [python](https://www.python.org) for Windows and install it

Then download the example files from DOS using:
```
C:>git clone https://github.com/kushnertodd/python-api-examples
```
You should be able to type this in DOS and get the card types:
```
C:>curl "https://api.magicthegathering.io/v1/types"
{"types":["Artifact","Battle","Conspiracy","Creature","Dragon","Elemental","Enchantment","Goblin","Hero","instant","Instant","Jaguar","Knights","Land","Phenomenon","Plane","Planeswalker","Scheme","Sorcery","Stickers","Summon","Tribal","Universewalker","Vanguard","Wolf"]}
```
- How do I parse that file into human-readable form using python? I'm glad you asked. Run `json-format.bat` in dos.

json-format.py

```
import sys
import json

if len(sys.argv) < 2:
    print(f'usage: {sys.argv[0]} filename')
    sys.exit(0)	

print(f'formatted json in {sys.argv[1]}:')

with open(sys.argv[1], 'r') as json_file:
    json_object = json.load(json_file)

print(json_object)

print(json.dumps(json_object))

print(json.dumps(json_object, indent=1))
```

json-format.bat

```
curl "https://api.magicthegathering.io/v1/types">types.txt
type types.txt
python json-format.py
python json-format.py types.txt
```
- Now you're going to say How do I parse that into data in a usable python form? I'm glad you asked that too. The json is actually loaded into a dictionary that has "types" as the key and the list of types as the value. `json-parse.bat` strips the "types" off the json and just prints the list of types. 

json-parse.py

```
import sys
import json

if len(sys.argv) < 2:
    print(f'usage: {sys.argv[0]} filename')
    sys.exit(0)	

with open(sys.argv[1], 'r') as json_file:
    json_object = json.load(json_file)

print(json_object["types"])
```

json-parse.bat

```
curl "https://api.magicthegathering.io/v1/types">types.txt
type types.txt
python json-parse.py types.txt
```
- Now you're going to say Sure, that's fine if I want to get  a fixed set of data from a json request, but suppose I want to specify the thing to get the json for and print out a specific set of data for that thing? `json-http-requests-name.bat` will get the mana cost for a card you specify.

json-http-requests-name.py
```
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
```

json-http-requests-name.bat

```
python json-http-requests-name.py "'Cho-Manno, Revolutionary'"
```
- You want to know what kind of data you can get for a specific card? You can capture all the request json with this command:
```
C:>curl "https://api.magicthegathering.io/v1/cards?supertypes=legendary&types=creature">card.txt
```
and copy and paste that text into this web page:
```
https://jsonformatter.org/
```
and it will show the information for "Cho-Manna, Revolutionary" as the first entry:
```
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
```
- You can then print out what data you want by changing `json-http-requests-name.py` to print the data you want:
```
print(f'supertype for {card_name} is:\n{json_object["cards"][0]["supertypes"]}') 
```
- You can get data for a list of fields with `json-http-requests-name-list.bat`.


json-http-requests-name-list.py

```
import sys
import json
import requests

if len(sys.argv) < 2:
    print(f'usage: {sys.argv[0]} card-name')
    sys.exit(0)	

card_name = sys.argv[1]

res = requests.get('https://api.magicthegathering.io/v1/cards?supertypes=legendary&types=creature')

json_object = json.loads(res.text)

data_list = ["manaCost", "colors", "type", "text"]
print(f'data for {card_name} is:')
for data in data_list:
    print(f'    {data}:\t{json_object["cards"][0][data]}')
```

json-http-requests-name-list.bat

```
python json-http-requests-name-list.py "'Cho-Manno, Revolutionary'
```
- you can also put the address in chrome to see the data `https://api.magicthegathering.io/v1/types`
```
https://api.magicthegathering.io/v1/types
```
- You can parse the results of running the `curl` command from python using `json-http-requests.bat`.

json-http-requests.py

```
import sys
import json
import requests

# this code is from:
#  https://stackoverflow.com/questions/26000336/execute-curl-command-within-a-python-script

res = requests.get('https://api.magicthegathering.io/v1/types')
print(f'original api response is:\n{res.text}\n')

json_object = json.loads(res.text)

print(f'parsed json for "types" is:\n{json_object["types"]}')
```

json-http-requests.bat

```
python json-http-requests.py
```
