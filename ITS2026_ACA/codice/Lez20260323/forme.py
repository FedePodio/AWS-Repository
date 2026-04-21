
class Shape:
    def __init__(self, color):
        self.color = color

def describe(self):
    return f"Sono una forma di colore {self.color}"

class Circle:
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius
    def __str__(self):
        descrizione = f"Sono un cerchio di superfice {3.14 * self.radius * self.radius}"
        descrizione += super().__str__()
        return descrizione

class Triangle:
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height

class Square:
    def __init__(self, width, color):
        super().__init__(color)
        self.width = width

cerchio = Circle(5, 'red')
triangolo = Triangle(4, 6, 'green')
quadrato = Square(7, 'blue')

print(cerchio)
print(quadrato)
print(triangolo)