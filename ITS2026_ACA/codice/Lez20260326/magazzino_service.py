from prodotto_repo import ProdottoRepo

class MagazzinoService:

    def __init__(self):
        self.repo_prodotti = ProdottoRepo()

    def getALLProducts(self):
        return self.repo_prodotti.getProdotti()
    