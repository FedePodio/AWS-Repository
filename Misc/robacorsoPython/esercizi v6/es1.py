"""
Autore: Federico Podio
Data: 28/05/2026
Titolo: Esercitazione PY 05
"""
# Esercizi su OOP
# ES 1

# Creare una classe Insegnante con attributi nome, età e stipendio, dove stipendio deve
# essere un attributo privato.
# Costruire tutti i metodi getter e setter per gli attributi (anche per quelli pubblici)
# Effettuare l’overriding del metodo __str__ in maniera tale che restituisca gli attributi nome e età.
# Provare la classe istanziando almeno due oggetti.

class Insegnante(object):
   
    def __init__(self, nome: str, eta: int, stipendio: float):
        self.nome = nome
        self.eta = eta
        self.__stipendio = stipendio

# nome
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str) and len(nome) > 0:
            self.__nome = nome
        else:
            raise ValueError("Invalid name")

# età
    @property    
    def eta(self):
        return self.__eta
    @eta.setter
    def eta(self, eta):
        if isinstance(eta, int) and eta > 0:
            self.__eta = eta
        else:
            raise ValueError("Invalid age")
        
# stipendio  
    @property
    def stipendio(self):
        return self.__stipendio
    @stipendio.setter
    def stipendio(self, stipendio):
        if isinstance(stipendio, (float, int)):
            self.__stipendio = stipendio
        else:
            raise ValueError("Invalid salary")

    def __str__(self):
        return F"Nome : {self.nome}, eta: {self.eta} anni"
    
    
insegnate1 = Insegnante("Jan", 25, 2000)  
print(insegnate1.nome)
print(insegnate1.eta)
print(insegnate1.stipendio)

insegnate1.nome = "Ice"
insegnate1.eta = 50
insegnate1.stipendio = 1000.0
print(insegnate1)

insegnate2 = Insegnante("Bruh", 50, 1600.5)

print(insegnate2.nome)
print(insegnate2.eta)
print(insegnate2.stipendio)

insegnate2.nome = "Joevanni"
insegnate2.eta = 44
insegnate2.stipendio = 1002.2

print(insegnate2)