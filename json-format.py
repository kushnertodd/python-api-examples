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

