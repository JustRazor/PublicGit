import json
adatbazis = []
with open("database.json", mode="r", encoding="utf8") as fajl:
    adatbazis = json.load(fajl)
print(adatbazis)