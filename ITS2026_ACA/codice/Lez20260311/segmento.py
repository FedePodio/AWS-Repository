from punto import Punto
from math import sqrt, pow

class Segmento:

    def __init__(self, A: Punto, B: Punto):
        self.A = A
        self.B = B

    def lunghezza(self):
        """Questo metodo calcola la lunghezza di questo segmento"""
        lunghezza = 0

        # radice_quadrata di (Bx - Ax)^2 + (By - Ay)^2
        return sqrt(   pow(self.B.x - self.A.x, 2) + pow(self.B.y - self.A.y, 2)  )

        