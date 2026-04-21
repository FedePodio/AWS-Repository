"""Simple dice roller game - python version."""

import random
import time

facce = 6
lanci = 100_000
vittorie = 0

def lancia():
    return random.randint(1, facce)  

start = time.time()
for x in range(lanci):
    dado1 = lancia()
    dado2 = lancia()
    # print(f"Ripetizione nr {x}")
    # print(f"Dado 1 vale {dado1}")
    # print(f"Dado 2 vale {dado2}")
    if dado1 == dado2:
        # print(f"Hai vinto con una coppia di {dado1}")
        vittorie += 1
stop = time.time()
elaborazione = (stop - start)
print(f"L'elaborazione è durata {elaborazione:.2f}s")
percentuale = vittorie / lanci
print(f"Hai vinto {vittorie} volte, con una percentuale di successo del {percentuale*100:.2f}%")
