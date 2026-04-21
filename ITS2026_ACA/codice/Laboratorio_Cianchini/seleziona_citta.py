import sqlite3

query = "select * FROM regioni;"
db = sqlite3.connect("regioni.db")

cursor = db.cursor()

cursor.execute(query)

result = cursor.fetchall()
for riga in result:
    print(f"Il capoluogo della regione {riga[1]} é: {riga[2]}")

