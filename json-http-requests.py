import sys
import json
import requests

# this code is from:
#  https://stackoverflow.com/questions/26000336/execute-curl-command-within-a-python-script

res = requests.get('https://api.magicthegathering.io/v1/types')
print(f'original api response is:\n{res.text}\n')

json_object = json.loads(res.text)

print(f'parsed json for "types" is:\n{json_object["types"]}')
