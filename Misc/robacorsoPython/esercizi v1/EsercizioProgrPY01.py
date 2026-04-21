"""
Autore: Federico Podio
Data: 06/03/20206
Titolo: Esercitazione PY 01
"""

"Selezione"
# Es 1
# Un negoziante per ogni spesa di importo superiore a 100 € effettua uno sconto del 5%, se
# l’importo risulta superiore a 300€ lo sconto è del 10%. Scrivere un programma che richieda
# all'utente l'ammontare della spesa e visualizzi quindi l'importo effettivo da pagare.

# Sezione di input Dati
price = int(input("Seleziona un prezzo: "))  #int perchè str va in conflitto

# Elaborazione
if price > 100:
    final_price = price - price * 5 / 100 #sconto del 5%
elif price > 300:
    final_price = price - price * 10 / 100 #sconto del 10%
else:
    final_price = price

# Sezione di output
print(f"Il prezzo finale é: {final_price}")

