import database
from dataclasses import dataclass

@dataclass
class Impiegato:
    # def __init__(self, nome, cognome, ruolo):  #senza @dataclass
    #     self.nome = nome
    #     self.cognome = cognome
    #     self.ruolo = ruolo
    # def __str__(self):
    #     pass
    # def __repr__(self):
    #     pass
    # def stampa_utente():
    #     pass
    nome: str    #con @dataclass
    cognome: str
    ruolo: str

class EmployeeDao:

    def findImpiegati(self):
        DB_impiegati = database.connetti()
        impiegati = database.interroga(DB_impiegati, "select a.FirstName, a.LastName, a.Title from employee a;")

        return [Impiegato(n,c,r) for n, c, r  in impiegati]
