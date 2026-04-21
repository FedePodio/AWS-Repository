""" Madlibs game """

nome = input("Inserisci un nome: ")
aggettivo1 = input("Inserisci un aggettivo: ")
animale = input("Inserisci un animale: ")
cibo = input("Inserisci un cibo: ")
numero = input("Inserisci un numero: ")
colore = input("Inserisci un colore: ")
verbo = input("Inserisci un verbo: ")


# storia = f"""
# 🌟 LA STORIA DI {nome.upper()} 🌟

# C'era una volta {nome}, una persona molto {aggettivo1}.
# Un giorno, mentre camminava nel bosco, incontrò un {animale} {colore}.
# L'animale aveva {numero} pezzi di {cibo} e voleva {verbo}.
# {nome} decise di aiutarlo e insieme vissero felici e contenti!
# """
# print(storia)

# V2 randomized
import random as rnd

nome = ['francesca', 'giovanni', 'bread pitt']
aggettivo1 = ['bella', 'utile', 'top']
animale = ['cane', 'cinghiale', 'orso']
cibo = ['pizza', 'banane', 'lamponi']
numero = ['12', '3', '4']
colore = ['verde', 'giallo', 'blu']
verbo = ['correre', 'camminare', 'giocare']

with open("stories.txt", "w") as f:

    for x in range(10):

        f.write(f"-----------------------Storia n° {x+1}-----------------------")

        storia = f"""
        🌟 LA STORIA DI {rnd.choice(nome).upper()} 🌟
        C'era una volta {rnd.chioce(nome).upper}, una persona molto {rnd.choice(aggettivo1)}.
        Un giorno, mentre camminava nel bosco, incontrò un {rnd.choice(animale)} {rnd.choice(colore)}.
        L'animale aveva {rnd.choice(numero)} pezzi di {rnd.choice(cibo)} e voleva {rnd.choice(verbo)}.
        {rnd.choice(nome)} decise di aiutarlo e insieme vissero felici e contenti!
        """
        f.write(storia)
        f.write("----------------------------------------------")

print("Le storie sono pronte")
print(storia)