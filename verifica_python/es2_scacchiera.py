'''
ESERCIZIO 2 — Scacchiera NxN

Input:
nome studente
intero n
carattere c
Output: scacchiera alternata con _.
In testa deve comparire una riga tipo:
Scacchiera generata da: <nome>
'''
nome = input("Inserisci il tuo nome: ")  #Federico Podio

n = int(input("Inserisci di che dimensioni deve essere la scacchiera: "))
c = input("Inserisci il carattere da usare: ") 

for i in range(n):
    fila = ""
    for x in range(n):
        if (i + x) % 2 == 0:
            fila += c
        else:
            fila += "_"
    print(fila)

print(f"Scacchiera generata da: {nome}")