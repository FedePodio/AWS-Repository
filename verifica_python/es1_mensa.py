'''
ESERCIZIO 1 — Mensa con sconti

Come già definito nella verifica precedente (versione base uguale per tutti):
primi: 5€
secondi: 4€
dal secondo primo in poi: sconto 20%
acqua gratis
bibita non acqua: +0.50€
Il programma deve stampare:
[nome] - Totale pranzo: XX.XX euro
'''

nome = input("Inserisci il tuo nome: ")  #Federico Podio

primo = 5
secondo = 4
acqua = 0
bibita = 0.50

print('''
Il menu offre le seguenti opzioni (menu fisso):
    - primo (5 euro)
    - secondo (4 euro)
    - acqua (free of charge)
    - bibita (0.50 euro)
    ''')

# il costo dei primi o secondi è sempre uguale quindi gli chiedo quanti ne vuole direttamente
# invece che fare una lista di piatti
n_primi = int(input("Inserisci quanti primi vuoi: "))
n_secondi = int(input("Inserisci quanti secondi vuoi: "))
n_acqua = int(input("Inserisci quante bottiglie d'acqua vuoi: "))
n_bibite = int(input("Inserisci quanti bibite vuoi: "))

costo_primi = n_primi * 5.00
if n_primi >= 2:
    costo_primi = 5 + (n_primi - 1) * (5 * 0.80)
else:
    costo_primi = 5.00

costo_secondi = n_secondi * 4.00
costo_bibite = n_bibite * 0.50
totale = costo_primi + costo_secondi + costo_bibite



print(f"{nome}, Totale pranzo: {totale:.2f} euro")



# ho provato con una f ma non mi stava riuscendo, la lascio qui sotto comunque

# def costo_totale():
#     n_ordini = 0
#     totale = input('''
#                    Inserisci cosa ordinare tra:
#                    - primo
#                    - secondo
#                    - acqua
#                    - bibita
#                    (q per uscire)
#                    ''')
#     for ordine in n_ordini:
#         if ordine == primo:
#             n_ordini = n_ordini +1
#             if n_ordini >= 2:
#                 sconto = 0.80
#         else:
#                 n_ordini = n_ordini

#     return totale
