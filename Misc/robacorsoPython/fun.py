""" 
variabile immutabile modificata = cambio id
variabile mutabile modificata = stesso id
"""


# def fun(a):
#     a = a + 1
#     print(a)  #stampa 4

# a = 4
# print(a) # 5
# print(fun(a)) # none
# print(a) # 4

# ---------------------------------------------------

# a = 1
# b = 2
# c = b
# print(id(a),id(b),id(c), sep = "\n")

# ---------------------------------------------------

# a = 1
# print("id prima modifica:", id(a))
# a += 1
# print("id dopo modifica:", id(a))

# ---------------------------------------------------

# a = [1, 2]
# print("id prima modifica:", id(a))
# a += [3]
# print("id dopo modifica:", id(a))

# ---------------------------------------------------

# def fun(a):
#     print(id(a))

# a = 1
# print(id(a))  # uguale
# fun(a)

# ---------------------------------------------------

# def fun(a):                               # valore:
#     print("id(a) prima modifica:", id(a)) # xxx
#     a += 1
#     print("id(a) dopo modifica:", id(a)) # yyy
#     print("Valore a dopo modifica:", a)

# a = 1
# print("id(a) prima chiamata:", id(a)) # xxx
# fun(a)
# print("id(a) dopo modifica:", id(a)) # xxx
# print("Valore a dopo funzione:", a)

# ---------------------------------------------------

# def areaRettangolo(base = 2, altezza = 4):
#     return base*altezza

# print("Area 1 =", areaRettangolo()) # valori default di sopra
# print("Area 2 =", areaRettangolo(5))  # rimpiazza solo primo valore
# print("Area 3 =", areaRettangolo(5,5)) # rimpiazza entrambi

# ---------------------------------------------------

# def areaRettangolo(base, altezza, profondita):
#     return base*altezza*profondita

# print("Area 3 =", areaRettangolo(5, altezza = 5, profondita = 3)) 

# ---------------------------------------------------

# def media(*parametri):  #???
#     somma = 0

#     for val in parametri:
#         somma += val
#     return somma / len(parametri)

# print("Media 1 = ", media(1,2,3))
# print("Media 2 = ", media(1,2,3,4,5,6))
# print("Media 3 = ", media())

# ---------------------------------------------------


