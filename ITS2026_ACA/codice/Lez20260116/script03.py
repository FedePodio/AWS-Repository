frutti = ['pere','mele','banane']
verdure = ['broccoli', 'spinaci', 'barbabietole']

frutti.insert(1, "arance")

if 'melanzane' not in verdure:
    verdure.append('melanzane')


ortofrutticoli = [frutti, verdure]

# lettere = list("ciao")

# for lettera in list("ciao"):
#     print(lettera, end = " - ")  #\n

frutti.append('fragole')

frutti.remove('fragole')


#frutti.sort()

for prodotto in ortofrutticoli:
    for p in prodotto:
        print(p)
    print("-" * 10)
