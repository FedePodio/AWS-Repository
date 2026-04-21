from dataclasses import dataclass

@dataclass
class Libro:
    titolo: str
    pagine: int

libri = [
    Libro('A nord di ushiaia', 500),
    Libro('E oggi è ancora bello', 300),
    Libro('Bisogna saper perdere', 240),
]

def ordinatore_titolo(libro):
    return libro.titolo
# oppure
def ordinatore_pagine(libro):
    return libro.pagine

# lambda libro:libro.pagine
# libri.sort(key=lambda libro:libro.pagine)


libri.sort(key=ordinatore_titolo)
print(libri)

voti = [25,28,24,27,29,30,18,25]
parole = ['pisolo', 'eolo', 'brontolo', 'mammolo', 'gongolo', 'cucciolo', 'dotto']

# dati 5 numeri interi, implementare la strategia per ritornarli ordinati in senso crescente

# 25,28,24,27,29 -> 24,25,27,28,29

voti.sort()
print(voti)
