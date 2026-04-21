"""
Autore: Federico Podio
Data: 20/03/2026
Titolo: Esercitazione PY 02
"""

#ES 1

##
## Funzioni:
##
# def fun(param1: int, param2: float) -> int:
# ‘’’
# Funzione: fun
# Template per costruire le funzioni
# Parametri formali:
# int Param1 -> descrizione Param1
# float Param2 -> descrizione Param2
# Valore di ritorno:
# int -> descrizione valore di ritorno
# ‘’’
# retValue = 5 # Valore di ritorno della funzione
# return retValue
# ‘’’


# from datetime import datetime as orario

# print(orario.now().strftime("%H:%M:%S"))

h = int(input("Inserisci soltanto le ore: ")) * 3600
m = int(input("Inserisci soltanto i minuti: ")) * 60
s = int(input("Inserisci soltanto i secondi: "))

print(h + m + s)

#tempostringa=input("Inserisci la qta di tempo nel formato hh:mm:ss")

# def orario(time_str):
#     h, m, s = time_str.split(':')
#     return int(h) * 3600 + int(m) * 60 + int(s)
#     return int(h) + int(m) + int(s)

def orario2(h,m,s):
    #h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)
    # return int(h) + int(m) + int(s)

# print(orario("10:30:20"))