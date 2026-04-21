"""Number guessing game 1-100  (federico podio)"""

import random as rnd
numero_estratto = rnd.randint(1,100)
indovinato = False
tentativo = 0

while not indovinato and tentativo < 7:
    numero_utente = int(input("Inserisci un numero da 1 a 100: "))
    if numero_utente > numero_estratto:
        print("Troppo alto, riprova")
    elif numero_utente < numero_estratto:
        print("Troppo basso, riprova")
    else:
        indovinato = True

    # elif tentativo == 7:
    #     print("Hai perso")
    # else:
    #     print(f"Hai indovinato in {tentativo} tentativi")
    
    tentativo = tentativo + 1

if tentativo == 7:
    print("Hai perso")
else:
    print(f"Hai indovinato in {tentativo} tentativi")


# while numero_utente != numero_estratto:
#     if numero_utente > numero_estratto:
#         print("Troppo alto, riprova")
#         tentativo = tentativo + 1
#     elif numero_utente < numero_estratto:
#         print("Troppo basso, riprova")
#     else:
#         print(f"Hai indovinato in {tentativo} tentativi!")
