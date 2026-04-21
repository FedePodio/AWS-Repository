# saluto = 'HELLO '
# nome = input("Come ti chiami? ")

# print(saluto + nome)

# print(f"Il tuo nome è {nome}")
# print(f"Il tuo nome è lungo {len(nome)} caratteri")
# print(f"Il tuo nome maiuscolo {nome.upper} ")
# print(f"Il tuo nome minuscolo {nome.lower} ")
# print(f"Il tuo nome capitalizzato {nome.capitalize} ")

# for carattere in nome:
#     print(carattere)

# print(nome[0:10:2])

carattere = input("Inserisci il carattere da usare: ")

# print(((carattere + ' ') * 4 + '\n') * 4)

for i in range(4):
    for j in range(4):
        print(carattere + ' ', end = ' ')
    print() # ogni 4 ripetizioni vai a capo