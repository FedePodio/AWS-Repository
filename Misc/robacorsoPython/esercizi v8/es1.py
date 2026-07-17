"""
Autore: Federico Podio
Data: 01/06/2026
Titolo: Esercitazione PY 05
"""
# Esercizi sui files
# ES 1

# Scrivere un programma che, leggendo da tastiera una stringa, la salvi su file “stringa.txt”.
# Successivamente aprire il file “stringa.txt” e verificare il salvataggio.

def inserire():
    # inserimento della stringa da input

    stringa = input("Inserisci una stringa: ")
    while len(stringa) == 0:
        stringa = input("La stringa deve essere scritta, riprova: ")
    return stringa


def main():
    # inserimento stringa/scrittura su file e verifica del salvataggio

    stringa = inserire()
    with open("stringa.txt", "w") as fh:
        fh.write(stringa)
    print(stringa)

if __name__ == '__main__':
    main()

