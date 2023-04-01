import json

with open('JSON/weapons.json', 'r') as f:
    wpn = json.load(f)


if any('2-hand' in i for i in wpn['Maul']['props']):
    print(wpn['Maul']['props'])