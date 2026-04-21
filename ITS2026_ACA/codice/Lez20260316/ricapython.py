
# titolo: str = 'Quo vadis'
# anno = 1995
# print(type(anno))

# frutta = ['mele', 'pere', 'banane']
# frutti_piccoli = ['mirtilli', 'fragole', 'ribes']
# frutta.extend(frutti_piccoli)

# tutti_frutti = frutta + frutti_piccoli

# print(tutti_frutti)

# print("###### TIPO ######")
# print(type(frutta))


# print("###### HELP ######")
# print(help(frutta))
# --------------------------------------------------------

# UNPACKING

#           0        1        2
frutti = ['mele', 'pere', 'banane']
verdure = ['spinaci', 'costine', 'broccoli']
dolci = ['cassatina', 'cannolo', 'meringata']

alimenti = frutti + verdure + dolci
print(alimenti)

# for frutto in frutti:
#     print(frutto)

zippati = zip(frutti, verdure, dolci)

# print(frutti[0])
# print(frutti[1])
# print(frutti[2])

for frutto, verdura, dolce in zippati:
    print(frutto, verdura, dolce)

# LIST COMPREHENSION

scatola = [alimento for alimento in alimenti if alimento.startswith('c')]

# scatola = []
# for alimento in alimenti:
#     if alimento.startswith('c'):
#         scatola.append(alimento)

print(scatola)