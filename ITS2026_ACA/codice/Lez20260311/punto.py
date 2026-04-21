""" Classe che rappresenta il punto sul piano cartesiano """

class Punto:
    # x = 1
    # y= 1

    def __init__(self, x: int, y: int):    # dunder (double under) methods
        self.x = x
        self.y = y
        # print(f"Ho creato un nuovo punto di coordinate ({self.x}, {self.y})")


    def stampa(self):
        return f"Le coordinate di questo punto sono: ({self.x}, {self.y})"