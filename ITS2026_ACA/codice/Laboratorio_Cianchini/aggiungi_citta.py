import sqlite3

while True:
    regione = input('Inserisci il nome della regione (q per uscire): ')
    if regione.lower() == 'q' :
        break
    capoluogo = input('Inserisci il nome della città capoluogo di regione: ')

    query = "insert into regioni(regione_nome, capoluogo) VALUES (?,?)"
    values = (regione, capoluogo)

    db = sqlite3.connect('regioni.db')
    cursor = db.cursor()
    cursor.execute(query, values)

    db.commit()
    print(f"{regione} inserita con successo")

