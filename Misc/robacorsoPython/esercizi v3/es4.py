"""
Autore: Federico Podio
Data: 10/04/2026
Titolo: Esercitazione PY 03
"""
# Esercizi sulle liste
# ES 2

# Scrivere un programma che date due liste stampi "OK" se hanno almeno un membro comune altrimenti stampi "KO".

lista1 = [1,2,3,4]
lista2 = [0,1]

def clone(l1, l2):
    sl1 = set(l1)
    sl2 = set(l2)
    if sl1 & sl2:   # "&" operatore di paragone tra 2 liste a quanto pare
        print("OK")
    else:
        print("KO")

clone(lista1, lista2)