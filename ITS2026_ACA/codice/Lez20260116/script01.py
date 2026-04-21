
cities = ['milano', 'torino', 'roma', 'napoli']

def checkTemperatura(citta):

    frase = f"Qual è la temperatura esterna della città di {citta}?" # formatted string

    temperatura = int(input(frase))

    if temperatura > 25:
        print("Fa caldo")
        print("accendi il ventilatore")
    elif temperatura > 15:
        print("Come si sta bene oggi")
        print("spegni il ventilatore")
    else:
        print("oggi fa freddo")
        print("accendi il riscaldamento")


for city in cities:
    # print(c)
    checkTemperatura(city)


print("Bye")