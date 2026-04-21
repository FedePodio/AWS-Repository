"""
Autore: Federico Podio
Data: 10/04/2026
Titolo: Esercitazione PY 03
"""
# Esercizi sulle stringhe
# ES 1

# Scrivere un programma per rimuovere l'n- esimo carattere da una stringa non vuota.
def rimuovich(stringa, n):
    if n < 0 or n >= len(stringa):
        return "Errore: Indice fuori portata."
    stringa2 = stringa[:n] + stringa[n+1:]
    return stringa2

# Progettare una funzione che accetti la stringa, la posizione del carattere e restituisca la
# stringa modificata.
stringa = input("Inserisci la frase desiderata: ")
n = int(input("Inserisci la posizione da rimuovere: "))

res = rimuovich(stringa, n)

print(f"{res}")

