'''
ESERCIZIO 6 — Gestione credenziali

Chiedere:
nome studente
password
La password è valida se:
almeno 8 caratteri
contiene almeno una lettera maiuscola
contiene almeno una minuscola
contiene almeno un numero

Stampare:
<nome> - Password valida oppure <nome> - Password non valida
'''

nome = input("Inserisci il tuo nome: ")  #Federico Podio

nome_studente = input("Inserisci il nome dello studente: ")
password = input("Inserisci la password: ")

pass_ok = True
upper = False
lower = False
number = False

#check su lunghezza/maiusc/minusc/num
lunghezza = len(password) >= 8
for carattere in password:
    if carattere.isupper():
        upper = True
    elif carattere.islower():
        lower = True
    elif carattere.isdigit():
        number = True

if lunghezza and upper and lower and number:  #se tutte e 3 sono valide
    print(f"{nome} - {nome_studente} - Password valida")
else:
    print(f"{nome} - {nome_studente} - Password non valida")
