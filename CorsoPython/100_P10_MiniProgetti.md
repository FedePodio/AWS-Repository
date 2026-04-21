# 📘 Corso Python – Modulo 10

## Mini-Progetti Pratici

---

## 🧮 1. Calcolatrice da console

### Obiettivo

Creare una semplice calcolatrice che esegua le quattro operazioni fondamentali.

### Codice di esempio

```python
def somma(a, b): return a + b
def sottrai(a, b): return a - b
def moltiplica(a, b): return a * b
def dividi(a, b): 
    if b == 0:
        raise ZeroDivisionError("Divisione per zero non consentita")
    return a / b

while True:
    print("\n=== CALCOLATRICE ===")
    print("1. Somma\n2. Sottrai\n3. Moltiplica\n4. Dividi\n5. Esci")
    scelta = input("Scegli un'opzione: ")

    if scelta == "5":
        print("Uscita dal programma.")
        break

    try:
        a = float(input("Primo numero: "))
        b = float(input("Secondo numero: "))
        operazioni = {"1": somma, "2": sottrai, "3": moltiplica, "4": dividi}
        risultato = operazioni[scelta](a, b)
        print(f"Risultato: {risultato}")
    except KeyError:
        print("Scelta non valida!")
    except ValueError:
        print("Inserisci solo numeri!")
    except ZeroDivisionError as e:
        print(e)
```

---

## 📇 2. Rubrica (dizionari + file)

### Obiettivo

Gestire una piccola rubrica salvando i contatti su file.

### Codice di esempio

```python
import json

FILE = "rubrica.json"

def carica_rubrica():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def salva_rubrica(rubrica):
    with open(FILE, "w") as f:
        json.dump(rubrica, f, indent=4)

rubrica = carica_rubrica()

while True:
    print("\n=== RUBRICA ===")
    print("1. Aggiungi contatto\n2. Cerca contatto\n3. Elimina contatto\n4. Mostra tutti\n5. Esci")
    scelta = input("Scegli: ")

    if scelta == "1":
        nome = input("Nome: ")
        telefono = input("Telefono: ")
        rubrica[nome] = telefono
        salva_rubrica(rubrica)
    elif scelta == "2":
        nome = input("Nome da cercare: ")
        print(f"{nome}: {rubrica.get(nome, 'non trovato')}")
    elif scelta == "3":
        nome = input("Nome da eliminare: ")
        rubrica.pop(nome, None)
        salva_rubrica(rubrica)
    elif scelta == "4":
        for n, t in rubrica.items():
            print(f"{n}: {t}")
    elif scelta == "5":
        break
```

---

## 🔐 3. Password Generator

### Obiettivo

Generare password casuali con lettere, numeri e simboli.

### Codice di esempio

```python
import random
import string

def genera_password(lunghezza=12):
    caratteri = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caratteri) for _ in range(lunghezza))

lunghezza = int(input("Lunghezza password: "))
print("Password generata:", genera_password(lunghezza))
```

---

## 📂 4. File Reader (conteggio parole)

### Obiettivo

Leggere un file di testo e contare righe, parole e caratteri.

### Codice di esempio

```python
def analizza_file(nome_file):
    try:
        with open(nome_file, "r", encoding="utf-8") as f:
            testo = f.read()
            righe = testo.splitlines()
            parole = testo.split()
            print(f"Righe: {len(righe)}")
            print(f"Parole: {len(parole)}")
            print(f"Caratteri: {len(testo)}")
    except FileNotFoundError:
        print("File non trovato.")

file = input("Inserisci il nome del file: ")
analizza_file(file)
```

---

## 🔁 Obiettivi formativi

Con questi mini-progetti lo studente:

* Consolida l’uso di **variabili, funzioni, cicli, condizioni**
* Impara a **gestire file e strutture dati**
* Applica la **gestione delle eccezioni**
* Comprende l’organizzazione del codice in **moduli riutilizzabili**

---

## 💡 Estensioni possibili

* Aggiungere salvataggio automatico in CSV o JSON
* Gestire interfaccia CLI più evoluta con `argparse`
* Creare un piccolo **menu principale** per lanciare i vari progetti

