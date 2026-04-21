"""
Autore: Federico Podio
Data: 20/03/2026
Titolo: Esercitazione PY 02
"""

#ES 1

# Creare una funzione che riceva una quantità di tempo in formato ore, minuti e secondi e la restituisca espressa solamente in secondi.
def calc_sec(h, m, s):
    tot = h * 3600 + m * 60 + s
    return tot

# creare un programma principale che chieda in input due quantità di tempo e stampi in output quale quantità di tempo è maggiore.

print("inserisci il primo orario in h:m:s")
h1 = int(input("Inserisci soltanto le ore: "))
m1 = int(input("Inserisci soltanto i minuti: "))
s1 = int(input("Inserisci soltanto i secondi: "))

print("inserisci il secondo orario in h:m:s")
h2 = int(input("Inserisci soltanto le ore: "))
m2 = int(input("Inserisci soltanto i minuti: "))
s2 = int(input("Inserisci soltanto i secondi: "))

tots1 = calc_sec(h1, m1, s1)
tots2 = calc_sec(h2, m2, s2)

if tots1 > tots2:
    print(f"Il primo risultato ({h1}h {m1}m {s1}s) è maggiore.")
elif tots2 > tots1:
    print(f"Il secondo risultato ({h1}h {m1}m {s1}s) è maggiore.")
else:
    print("I due tempi sono uguali")

