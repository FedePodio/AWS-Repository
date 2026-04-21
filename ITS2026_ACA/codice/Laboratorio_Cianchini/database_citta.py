""" Database città """

# import json

import sqlite3

regioni = {
    "Piemonte" : ["Torino", "Alessandria", "Asti"],
    "Lombardia" : ["Milano", "Como", "Pavese"],
    "Liguria" : ["Loano", "Genova", "Savona"],
    "Toscana" : ["Livorno", "Firenze", "Pisa"],
    "Veneto" : ["Venezia", "Verona", "Treviso"],
    "Sicilia" : ["Palermo", "Siracusa", "Trapani"],
}

# regionipy = json.dumps(regioni)
# regionijson = json.loads(regionipy)
# print(regionijson)
# print(regionipy)

db = sqlite3.connect("regioni.db")

cursor = db.cursor()

cursor.execute('DROP TABLE IF EXISTS regioni;')

query = """
    CREATE TABLE IF NOT EXISTS regioni(
        regione_id INTEGER PRIMARY KEY AUTOINCREMENT,
        regione_nome TEXT NOT NULL,
        capoluogo TEXT NOT NULL
    );
"""
cursor.execute(query)

for regione in regioni:
    query = f"insert into regioni (regione_nome, capoluogo) VALUES ('{regione}', '{regioni.get(regione)[0]}');"
    cursor.execute(query)


db.commit()



