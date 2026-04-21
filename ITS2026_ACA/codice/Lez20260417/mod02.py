import sys


print(f"Versione di Python in uso: {sys.version}")
print(f"Argomenti passati allo script: {sys.argv}")

# if len(sys.argv) !=3:
#     print("Uso; ppython script.py nome eta")
#     sys.exit(1)

# nome = sys.argv[1]
# eta = int(sys.argv[2])

# print(nome, eta)




x = [1,2,3]
print(sys.getsizeof(x))