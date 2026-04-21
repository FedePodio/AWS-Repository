"""Regioni italiane"""

regioni = {
    "Piemonte" : ["Torino", "Cuneo", "Astri", "Alessandria"],
    "Liguria" : ["Genova", "Savona", "Imperia", "La Spezia"]
}

# print(help(regioni))

chiavi = regioni.keys()
valori = regioni.values()

# for chiave in chiavi:
#     print(chiave)
#     print(regioni.get(chiave))

# for chiave, valore in regioni.items():
#     print(f"La regione {chiave} ha i seguenti comuni capoluoghi di provincia {valore}")

for regione, comuni in regioni.items():
    print(f"La regione {regione} ha i seguenti comuni capoluoghi di provincia {comuni}")