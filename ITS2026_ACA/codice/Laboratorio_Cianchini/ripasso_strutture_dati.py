""" Strutture di Dati Python """

citta = ["Torino", "Milano", "Roma", "Loano"]  # lista, elemento modificabile

citta2 = ("Torino", "Milano", "Roma", "Loano") # tuple, elemento immutabile

citta3 = {"Torino", "Milano", "Roma", "Loano"} # contenitore set (no duplicati)

# citta.append("Genova") # aggiungi elemento alla lista
citta.append("Genova") # aggiungi elemento al set

# dictionary, crea una lista contenente serie di liste/tuple/set
regioni = {
    "Piemonte" : ["Torino", "Alessandria", "Asti"],
    "Lombardia" : ["Milano", "Como", "Pavese"],
    "Liguria" : ["Loano", "Genova", "Savona"],
    "Toscana" : ["Livorno", "Firenze", "Pisa"],
    "Veneto" : ["Venezia", "Verona", "Treviso"],
    "Sicilia" : ["Palermo", "Siracusa", "Trapani"],
}

# print(regioni)
# print(type(regioni)) # classe della lista
# print(dir(regioni)) # elementi della lista (dunder methods)
# print(help(regioni)) 

# for city in citta:
#     print(city)

# for regione, comuni in regioni.items(): # either keys/values/items
#     print(f"La regione {regione} ha i seguenti comuni: {comuni}")

# for regione in regioni.keys():
#     print(f"La regione {regione} ha i seguenti comuni: {regioni.get(regione)}")
#     print(f"La regione {regione} ha i seguenti comuni: {regioni[regione]}")

for regione in regioni.keys():
    print(f"La regione {regione} ha i seguenti comuni:")
    for comune in regioni.get(regione):
        print(comune)
