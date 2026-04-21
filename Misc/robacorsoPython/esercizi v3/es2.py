"""
Autore: Federico Podio
Data: 10/04/2026
Titolo: Esercitazione PY 03
"""
# Esercizi sulle stringhe
# ES 2

# Scrivere un programma che dica se una stringa è palindroma.

stringa = input("Inserisci una stringa: ")

def palindrome(stringa):
    stringa = stringa.lower()
    stringa == stringa[::-1]

if palindrome(stringa):
    print("la stringa è palindroma")
else:
    print("la stringa non è palindroma")

