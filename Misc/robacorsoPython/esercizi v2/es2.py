"""
Autore: Federico Podio
Data: 20/03/2026
Titolo: Esercitazione PY 02
"""

#ES 2

# Creare una funzione che abbia come parametri formali un numero arbitrario di valori numerici.
# Si vuole che restituisca la somma dei soli numeri pari e il prodotto dei soli numeri dispari
def elabora_numeri(numeri: int):
    somma_pari = 0
    prodotto_dispari = 1
    ha_dispari = False

    for n in numeri:
        if n % 2 == 0:
            somma_pari += n
        else:
            prodotto_dispari= n
            ha_dispari = True

    if not ha_dispari: prodotto_dispari = 0
    return somma_pari, prodotto_dispari

# Successivamente creare un programma che richiami tale funzione e che stampi in output i risultati 
s_p, p_d = elabora_numeri(2, 3, 4, 5, 6)
print(f"Somma dei numeri pari: {s_p}")
print(f"Prodotto dei numeri dispari: {p_d}")

