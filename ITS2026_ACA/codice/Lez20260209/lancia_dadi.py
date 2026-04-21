""" Lancia dadi"""
import random
import time

# for i in range(10):
#     print(random.random())


NUM_LANCI = 10000
vittorie = 0

start = time.time()
for i in range(NUM_LANCI):
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    if dado1 == dado2:
        print(f"Hai vinto con una coppia di {dado1}")
        vittorie += 1
    # print(f"il valore del dado 2 è: {dado2}")
    # print("---------------------------------")
stop = time.time()

print(f"Hai lanciato {NUM_LANCI} volte")
print(f"Hai vinto {vittorie} volte")
print(f"La percentuale di vittoria è {vittorie / float(NUM_LANCI) * 100:.2f}% volte")
print(f"l'elaborazione è durata {stop - start:.2f} secondi")
