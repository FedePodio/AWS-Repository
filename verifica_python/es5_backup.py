'''
ESERCIZIO 5 — Backup simulator 

Scrivere un programma che simula un tool di backup.
Input:
nome studente
lista di file (nomi file come stringhe, uno per riga)
la lista termina quando l utente inserisce "STOP"
Regole:
se un file termina con .tmp o .log non va salvato (ignorato)
gli altri vanno aggiunti al backup
Output finale:
Backup Report - <nome>
File inclusi: X
File esclusi: Y
Elenco inclusi:
- ...
- ...
'''

nome = input("Inserisci il tuo nome: ")  #Federico Podio


file_inclusi = []
file_esclusi_count = 0

print("Inserisci i nomi dei file (uno per riga). STOP per uscire:")
while True:
    file_inserito = input().strip()
        
    if file_inserito.upper() == "STOP":  #termina lista
        break
    if not file_inserito:
        continue
            
    if file_inserito.endswith('.tmp') or file_inserito.endswith('.log'): #ignora tmp/log
        file_esclusi_count += 1
    else:
        file_inclusi.append(file_inserito) #aggiunti al backup

  
print(f"{nome} - File inclusi: {len(file_inclusi)}")
print(f"{nome} - File esclusi: {file_esclusi_count}")
for file in file_inclusi:
    print(f"{nome} - Elenco inclusi: {file}")



