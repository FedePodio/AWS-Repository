"""
Autore: Federico Podio
Data: 06/03/20206
Titolo: Esercitazione PY 01
"""

"Iterazione"
#Es 1
# Scrivere un programma che chieda quanti alunni ci sono in una classe poi per ogni alunno
# fa inserire M voti, M dato in input, e ne scrive la media.

import math
alunni = input("Quanti alunni ci sono? ")

voti = int(input(f"Inserisci i voti dell'alunno, q per uscire: "))

media = sum(voti) / len(voti)

