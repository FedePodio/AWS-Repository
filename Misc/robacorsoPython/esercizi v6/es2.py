"""
Autore: Federico Podio
Data: 28/05/2026
Titolo: Esercitazione PY 05
"""
# Esercizi su OOP
# ES 2

# Creare una classe Rettangolo con attributi base e altezza. Costruire tutti i metodi setter e
# getter per gli attributi. Aggiungere i metodi per il calcolo dell ’area e del perimetro.
# Implementare un metodo di nome: “contiene” che ha come parametro un oggetto
# rettangolo. Tale metodo deve restituire true se il rettangolo oggetto chiamante contiene il
# rettangolo oggetto parametro, false se non lo contiene. Un rettangolo “contiene” un altro
# quando la sua altezza e la sua base sono maggiori rispettivamente della base e
# dell’altezza del secondo rettangolo.

class Rettangolo(object):

    def __init__(self, base, altezza):
        self.__base = base
        self.__altezza = altezza

    def calcolaPerimetro(self):
        return 2 * (self.base + self.altezza)
    
    def calcolaArea(self):
        return self.base * self.altezza
    
    def contiene(self, rettangolo2)-> bool:
        if isinstance(rettangolo2, Rettangolo):
            if self.base > rettangolo2.base and self.altezza > rettangolo2.altezza:
                return True
            else:
                return False
    
# metodo __str__ (perimetro/area)

    def __str__(self):
        """Metodo che restituisce una stringa con il perimetro e l'area del rettangolo"""
        return F"Perimetro : {self.calcolaPerimetro()}, Area : {self.calcolaArea()}"

# base/ h

    @property
    def base(self):
        return self.__base
    @base.setter
    def base(self, base):
        if isinstance(base, (int, float)) and base > 0:
            self.__base = base
        else:
            raise ValueError("Valore invalido")

    @property
    def altezza(self):
        return self.__altezza
    @altezza.setter
    def altezza(self, altezza):
        if isinstance(altezza, (int, float)) and altezza > 0:
            self.__altezza = altezza
        else:
            raise ValueError("Valore invalido")

# test classe

# rettangolo1 = Rettangolo(2,4)
# rettangolo2 = Rettangolo(1,2)
# print(rettangolo1)
# print(rettangolo1.contiene(rettangolo2))