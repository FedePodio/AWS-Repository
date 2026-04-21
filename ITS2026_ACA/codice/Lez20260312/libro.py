""" Classe libro, rappresenta un libro nel database """

class Libro:

    def __init__(self, libroId, collocazione, titolo, autore, editore, classificazione):
        self.libroId = libroId
        self.collocazione = collocazione
        self.titolo = titolo
        self.autore = autore
        self.editore = editore
        self.autore = autore
        self.classificazione = classificazione

    def __str__(self):
        return f"""
            Titolo: {self.titolo}, 
            Autore: {self.autore},
            Editore: {self.editore},
            Collocazione: {self.collocazione}
            """

    def toHtml(self):
            return f"""
                <div>
                    <h2>Titolo: {self.titolo}</h2>
                    <h3>Autore: {self.autore}</h3>
                    <h4>Editore: {self.editore}</h4>
                    <h5>Collocazione: {self.collocazione}</h5>
                </div>
                """