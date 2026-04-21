"""
Autore: Federico Podio
Data: 15/04/2026
Titolo: Esercitazione PY 03
"""
# Esercizi sulle tuple
# ES 1

# Scrivere un programma per rimuovere l'n- esimo elemento da una tupla non vuota.

def rimuovich(tupla, n):
    # if n < 0 or n >= len(tupla):    # non necessario non essendoci innput
    #     return "Errore: Indice fuori portata."
    tupla2 = tupla[:n] + tupla[n+1:]
    return tupla2

tupla = (['verduna', 'alessandro', 'storia', 'laurea'])
n = 3

res = rimuovich(tupla, n)

print(f"{res}")