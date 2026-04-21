"""
Autore: Federico Podio
Data: 06/03/20206
Titolo: Esercitazione PY 01
"""

"Selezione"
# Es 3
# Scrivere un programma che legga i coefficienti a e b di un'equazione di primo grado ax=b e
# ne scriva la soluzione (attenzione al dominio del coefficiente a)

# Sezione di input Dati
a = float(input("Inserisci il coefficiente a: "))
b = float(input("Inserisci il coefficiente b: "))

# Elaborazione
if a != 0:
    x = b / a
    print(f"equazione determinata x = {x}")
else:
    if b == 0:
        # Sezione di output
        print("equazione indeterminata")
    else:
        # Sezione di output
        print("equazione impossibile")