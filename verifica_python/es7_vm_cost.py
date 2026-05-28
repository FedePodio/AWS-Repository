'''
ESERCIZIO 7 — Calcolo costo VM 

Chiedere:
nome studente
numero di ore utilizzo VM
costo orario (float)
Calcolare costo totale.
Se ore > 100 applicare sconto 10%.

Output:
<nome> - costo totale VM: XX.XX euro
'''

nome = input("Inserisci il tuo nome: ")  #Federico Podio

nome2 = input("Inserisci il nome dello studente: ")
ore = int(input("Inserisci per quante ore ha usato la VM: "))
prezzo = float(input("Inserisci quanto vuoi far pagare l'ora: "))
costo = prezzo * ore

if ore >= 100:
    costo = costo - costo * 0.10  #sconto oltre le 100h
else:
    costo = costo

print(f"{nome} - {nome2} - costo totale VM: {costo:.2f} euro")