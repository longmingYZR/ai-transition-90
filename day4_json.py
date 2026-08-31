import json

with open("dictionary.json", "r", encoding="utf-8") as file:
    dictionary = json.load(file)

print(dictionary)