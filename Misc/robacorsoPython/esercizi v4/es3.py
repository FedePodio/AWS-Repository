"""
Autore: Federico Podio
Data: 15/04/2026
Titolo: Esercitazione PY 03
"""
# Esercizi sulle tuple
# ES 3

# Scrivere un programma per sostituire l'ultimo valore delle liste in una tupla con un valore
# richiesto in input.

tuplo = ([10, 20, 40], [40, 50, 60], [70, 80, 90])
valore = 621

def replacer(tuplo):
    tuplo_rimpiazzato = tuplo((n[:-1] + [valore]) for n in tuplo) # usa for 
    return tuplo_rimpiazzato

print(replacer(tuplo))