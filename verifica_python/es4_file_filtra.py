'''
ESERCIZIO 4 — File filter avanzato (ordine caratteri) 

Uguale all’esercizio file precedente, ma:
file input: input.txt
file output deve chiamarsi: output_<nome>.txt
Esempio: output_Mauro.txt
Scrivere solo le righe che contengono i caratteri della stringa s in ordine.
'''

nome = input("Inserisci il tuo nome: ")  #Federico Podio


with open("input.txt", 'r') as file: #path in verifica_python
    for linea in file:
        linea = linea.strip()
indice = 0
for carattere in linea:
    if carattere == 's'[indice]:
        indice += 1
        if indice == len('s'):
            break
        if indice == len('s'):
            print(linea)
       
        


#output richiesto in file esterno
output_Podio = open("output_Podio.txt", "w")
print(f"{nome} - ", file=output_Podio)
output_Podio.close()