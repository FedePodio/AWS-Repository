import mysql.connector
from dataclasses import dataclass

@dataclass
class Prodotto:
    nome: str
    prezzo: float
    giacenza: int


magazzino = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'magazzino'
)

cursore = magazzino.cursor()

query = "select nome, prezzo_unitario, quantita_stock from prodotti"
cursore.execute(query)

prodotti = cursore.fetchall()

tendina = [Prodotto(n, p, q) for n, p, q in prodotti]

with open("Esercizio_magazzino.txt", "w") as f:
    f.write(query)
    f.write("\n")

    # for row in tendina:
    #     print(f"{row[0]:30} {row[1]:10} {row[2]:5}\n")

    for p in tendina:
        f.write(f"{p.nome:30} {p.prezzo:10} {p.giacenza:5}\n")

