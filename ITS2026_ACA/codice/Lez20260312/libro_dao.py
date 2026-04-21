import mysql.connector   # originale fatto nel 3 marzo
from libro import Libro

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'biblioteca'
)

cursor = db.cursor()

cursor.execute("SELECT * FROM libri;")

libri = cursor.fetchall()

tabella_libri = []

for libro in libri:
    libroId = libro[0]
    autore = libro[1]
    titolo = libro[2]
    editore = libro[3]
    classificazione = libro[4]
    collocazione = libro[8]

    libro = Libro(libroId, collocazione, titolo, autore, editore, classificazione)
    tabella_libri.append(libro)
    
    print(libro)