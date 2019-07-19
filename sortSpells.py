import json
import requests

with open("spellsComplete.json", 'r') as inputFile:
    fullList = json.load(inputFile)

categorizedList = {
    "Wizard": [],
    "Bard": [],
    "Cleric": [],
    "Paladin": [],
    "Sorcerer": [],
    "Warlock": [],
    "Ranger": [],
    "Druid": []
}
for obj in fullList:
    classes = obj['classes']
    for dude in classes:
        try:
            categorizedList[dude["name"]].append(obj)
        except KeyError as e:
            print(e)

with open("classSortedSpells.json", "w") as output:
    json.dump(categorizedList, output)
