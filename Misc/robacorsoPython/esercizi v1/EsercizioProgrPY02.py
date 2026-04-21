"""
Autore: Federico Podio
Data: 06/03/20206
Titolo: Esercitazione PY 01
"""

"Selezione"
# Es 2
# Su una linea ferroviaria, rispetto alla tariffa piena, gli utenti pensionati usufruiscono di uno
# sconto del 10%, gli studenti del 15% e i disoccupati del 25%. Codificando i pensionati con
# un 1, gli studenti con un 2 e i disoccupati con un 3, scrivere un programma che, richiesto il
# costo di un biglietto e l'eventuale condizione particolare dell'utente, visualizzi l'importo da
# pagare.

# Sezione di input Dati
print(""" Salve, il prezzo del biglietto regionale è di 5 euro.
Seleziona con il numero appropriato se sei:
1: Pensionato
2: Studente
3: Disoccupato
4: Altro             
""")
user = int(input("Inserire il numero appropriato: "))

# Inizializzazioni variabili
price = 5
final_price = 0

# Elaborazione
while user < 4:
    if user == 1:
        user2 = "Sconto pensionati"
        final_price = price - price * 10 / 100
    elif user == 2:
        user2 = "Sconto studenti"
        final_price = price - price * 15 / 100
    elif user == 3:
        user2 = "Sconto disoccupati"
        final_price = price - price * 25 / 100
    else:
        user = 4
        user2 = "Biglietto intero"
        final_price = price
    # Sezione di output
    print(f"Hai selezionato {user2}, il costo del biglietto è: {final_price:.2f} €")
    break
