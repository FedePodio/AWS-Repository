import os

# Informazioni directory
print(f"Directory corrente: {os.getcwd()}")
print(f"Contenuto directory: {os.listdir('.')}")

# studenti_file = open("studenti.txt", "r", encoding="utf-8", newline="\n")
# lettura = studenti_file.read()
# for riga in lettura.splitlines():
#     os.mkdir(riga)

# studenti_file.close()

# os.mkdir("fatta in fad")
# os.makedirs("a/b/c")
# os.rmdir("fatta in fad")

for elem in os.listdir('.'):
    print(elem)

