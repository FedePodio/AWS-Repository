
# unpacking
class Studente:
    def __init__(self, nome, cognome, valutazione):
        self.nome = nome
        self.cognome = cognome
        self.valutazione = valutazione

#list
studenti = []

record1 = ['Pietro', 'Rossi', 28]

nome, cognome, valutazione = record1
# nome = record1[0]
# cognome = record1[1]
# valutazione = record1[2]

studenti.append(Studente(nome, cognome, valutazione))

