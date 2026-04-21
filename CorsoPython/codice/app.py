
# print("hello world")

# print("*" * 10)

# x = 1

# price = 10
# rating = 4.9
# name = 'John Smith'
# is_published = True
# print(price)

# Calcola paga settimanale
# pagaOraria=float(input("Inserisci la paga oraria: "))
# oreSettimana=float(input("Inserisci il numero di ore lavorate durante la settimana: "))
# oreStra=float(input("Inserisci il numero di ore di lavoro straordinario svolto durante la settimana: "))
# pagaSettimana=(pagaOraria*oreSettimana)+(1.5*pagaOraria*oreStra)
# print("La paga di questa settimana è:", pagaSettimana)

# temperatura = input('quanti gradi ci sono?')

# gradi = int(temperatura)

# if gradi > 30:
#     print('Fa caldo')
# elif gradi > 20:
#     print("non fa caldo, ci sono " + str(gradi))
# else:
#     print('fa freddo')

# a = 5

# while a >= 0:
#     print(-a)
#     a = a - 1

# for i in range(1, gradi):
#     print(i)

# with open("output.txt", "a") as f:
#     f.write("Nuova riga\n")

f = open("output.txt", "w")
f.write("Ciao Python!\n")
f.write("Seconda riga\n")
f.close()