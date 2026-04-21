"""
Autore: Federico Podio
Data: 10/04/2026
Titolo: Esercitazione PY 03
"""
# Esercizi sulle liste
# ES 1

# Scrivere un programma python che rimuova gli elementi duplicati da una lista.

lista = [1,2,3,4,4,4,2,5,6,7,8,9]
# print(list(set(lista)))
listafinale = []

def purge(lista):

    for element in lista:
        if element not in listafinale:
            listafinale.append(element)
        elif element in listafinale:
            listafinale = listafinale
        else:
            return listafinale


print(listafinale)