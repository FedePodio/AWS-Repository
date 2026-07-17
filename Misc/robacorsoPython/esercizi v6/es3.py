"""
Autore: Federico Podio
Data: 28/05/2026
Titolo: Esercitazione PY 05
"""
# Esercizi su OOP
# ES 3

# 1 - Creare una classe Calcolo con un costruttore di default (senza parametri) che consenta
# di eseguire vari calcoli su numeri interi.
# 2 - Creare un metodo chiamato Factorial() che permetta di calcolare il fattoriale di un
# intero. Testare il metodo istanziando la classe.
# 3 - Creare un metodo chiamato Sum() che consenta di calcolare la somma dei primi n
# interi 1 + 2 + 3 + .. + n. Prova questo metodo.
# 4 - Creare un metodo tableMult() che crea e visualizza la tabellina di un dato intero. Quindi
# creare un metodo allTablesMult() per visualizzare tutte le tabelline di numeri interi 1, 2, 3,
# ..., 9.

class Calcolo(object):
    def __init__(self):
        pass

    def factorial(self, numero: int) -> int:
        fattoriale = 1
        for base in range(1, numero + 1):
            fattoriale *= base
        return fattoriale

    def sum(self, n: int) -> int:
        risultato_somma = 0
        for numero in range(1, n + 1):
            risultato_somma += numero

        return risultato_somma
    
    def tableMult(self, numero: int, moltiplicatore: int) -> list:
        multipli = []      
        for i in range(1, moltiplicatore +1) :
            risultato = (numero * i)
            multipli.append(risultato)

        return multipli
    
    def alltablesMult(self) -> dict:
        tabelline_dict = {}
        for numero in range(1,10):
            tabelline_dict[numero] = self.tableMult(numero, 10)
        
        return tabelline_dict

calc = Calcolo()
print(calc.sum(15))
print(calc.tableMult(2,10))
print(calc.factorial(5))
print(calc.alltablesMult())