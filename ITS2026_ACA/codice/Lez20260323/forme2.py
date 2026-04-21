class Shape:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"Sono una forma di colore {self.color}"

    def describe(self):
        return f"Sono una forma di colore {self.color}"

class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius
       
    def __str__(self):
        descrizione =  f"Superficie: {3.14 * self.radius * self.radius}\n"
        descrizione += super().__str__()
        return descrizione

class Triangle(Shape):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height

class Square(Shape):
    def __init__(self, width, color):
        super().__init__(color)
        self.width = width

cerchio = Circle(5, "red")
#cerchio_rosso = cerchio
triangolo = Triangle(4, 6, "blue")
quadrato = Square(4, "green")

#print(cerchio)
#print(cerchio_rosso)

print(cerchio)
print(quadrato)
print(triangolo)
