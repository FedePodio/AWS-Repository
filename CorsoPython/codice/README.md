# 📁 Struttura repository

```
corso-python-base/
│
├── moduli/
│   ├── modulo_01_introduzione/
│   ├── modulo_02_tipi_dati/
│   ├── modulo_03_variabili_operatori/
│   ├── modulo_04_strutture_controllo/
│   ├── modulo_05_collezioni/
│   ├── modulo_06_funzioni/
│   ├── modulo_07_input_output/
│   ├── modulo_08_errori/
│   ├── modulo_09_moduli/
│   ├── modulo_10_progetti/
│
└── README.md
```

---

## 🧩 **modulo_01_introduzione/esempio.py**

```python
# Modulo 1 - Introduzione a Python

print("Ciao, mondo!")  # Il classico primo programma

# Python come calcolatrice
print(3 + 5)
print(10 / 2)

# Uso di commenti
# Questo è un commento su una riga
"""
Questo è un commento su
più righe (docstring)
"""
```

---

## 🔢 **modulo_02_tipi_dati/esempio.py**

```python
# Modulo 2 - Tipi di Dati di Base

intero = 42
reale = 3.14
testo = "Python"
booleano = True

print(type(intero), intero)
print(type(reale), reale)
print(type(testo), testo)
print(type(booleano), booleano)

# Conversioni
numero = int("10")
valore = float("3.5")
print(numero + valore)
```

---

## 🧮 **modulo_03_variabili_operatori/esempio.py**

```python
# Modulo 3 - Variabili e Operatori

a = 10
b = 3

print("Somma:", a + b)
print("Differenza:", a - b)
print("Prodotto:", a * b)
print("Divisione:", a / b)
print("Divisione intera:", a // b)
print("Resto:", a % b)

# Operatori logici
x = True
y = False
print("x AND y:", x and y)
print("x OR y:", x or y)
print("NOT x:", not x)
```

---

## 🔁 **modulo_04_strutture_controllo/esempio.py**

```python
# Modulo 4 - Strutture di Controllo

numero = int(input("Inserisci un numero: "))

if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Zero")

# Ciclo for
for i in range(1, 6):
    print("Numero:", i)

# Ciclo while
n = 0
while n < 3:
    print("Iterazione:", n)
    n += 1
```

---

## 🧺 **modulo_05_collezioni/esempio.py**

```python
# Modulo 5 - Collezioni

# Liste
numeri = [1, 2, 3, 4]
numeri.append(5)
print(numeri)

# Tuple
coordinate = (10, 20)
print("X:", coordinate[0])

# Set
colori = {"rosso", "verde", "blu"}
colori.add("giallo")
print(colori)

# Dizionari
persona = {"nome": "Luca", "eta": 25}
print(persona["nome"])
persona["citta"] = "Roma"
print(persona)
```

---

## ⚙️ **modulo_06_funzioni/esempio.py**

```python
# Modulo 6 - Funzioni

def saluta(nome):
    """Restituisce un saluto personalizzato."""
    return f"Ciao, {nome}!"

def somma(a, b=0):
    """Somma due numeri con parametro di default."""
    return a + b

print(saluta("Marta"))
print("Somma:", somma(4, 5))
print("Somma con default:", somma(10))
```

---

## 📥 **modulo_07_input_output/esempio.py**

```python
# Modulo 7 - Input e Output

# Input da tastiera
nome = input("Come ti chiami? ")
print("Ciao", nome)

# Scrittura su file
with open("dati.txt", "w") as f:
    f.write(f"Benvenuto, {nome}!\n")

# Lettura da file
with open("dati.txt", "r") as f:
    contenuto = f.read()
    print("Contenuto del file:")
    print(contenuto)
```

---

## 🧯 **modulo_08_errori/esempio.py**

```python
# Modulo 8 - Gestione degli Errori

try:
    x = int(input("Inserisci un numero: "))
    risultato = 10 / x
    print("Risultato:", risultato)
except ZeroDivisionError:
    print("Errore: divisione per zero!")
except ValueError:
    print("Errore: devi inserire un numero intero!")
finally:
    print("Operazione terminata.")
```

---

## 📦 **modulo_09_moduli/esempio.py**

```python
# Modulo 9 - Moduli e Librerie

import math
import random
from datetime import date

print("Radice quadrata di 16:", math.sqrt(16))
print("Numero casuale 1-10:", random.randint(1, 10))
print("Data di oggi:", date.today())

# Uso di un modulo personalizzato
# (vedi file 'mio_modulo.py' nello stesso folder)
import mio_modulo
print(mio_modulo.saluta("Paolo"))
```

📄 **mio_modulo.py**

```python
def saluta(nome):
    return f"Ciao {nome}, benvenuto nel modulo personalizzato!"
```

---

## 🧠 **modulo_10_progetti/**

Contiene i **mini-progetti pratici** del corso:

```
modulo_10_progetti/
│
├── calcolatrice.py
├── rubrica.py
├── password_generator.py
└── file_reader.py
```

📄 **calcolatrice.py**

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
    scelta = input("Scegli: ")
    if scelta == "5": break

    try:
        a = float(input("Primo numero: "))
        b = float(input("Secondo numero: "))
        operazioni = {"1": somma, "2": sottrai, "3": moltiplica, "4": dividi}
        print("Risultato:", operazioni[scelta](a, b))
    except Exception as e:
        print("Errore:", e)
```

📄 **rubrica.py**

```python
import json

FILE = "rubrica.json"

def carica():
    try:
        with open(FILE, "r") as f: return json.load(f)
    except FileNotFoundError: return {}

def salva(dati):
    with open(FILE, "w") as f: json.dump(dati, f, indent=4)

rubrica = carica()

while True:
    print("\n1. Aggiungi\n2. Cerca\n3. Elimina\n4. Mostra tutti\n5. Esci")
    scelta = input("Scegli: ")

    if scelta == "1":
        nome = input("Nome: ")
        tel = input("Telefono: ")
        rubrica[nome] = tel
        salva(rubrica)
    elif scelta == "2":
        nome = input("Nome da cercare: ")
        print(f"{nome}: {rubrica.get(nome, 'non trovato')}")
    elif scelta == "3":
        nome = input("Nome da eliminare: ")
        rubrica.pop(nome, None)
        salva(rubrica)
    elif scelta == "4":
        for n, t in rubrica.items(): print(f"{n}: {t}")
    elif scelta == "5": break
```

📄 **password_generator.py**

```python
import random, string

def genera(lunghezza=12):
    caratteri = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caratteri) for _ in range(lunghezza))

lunghezza = int(input("Lunghezza password: "))
print("Password generata:", genera(lunghezza))
```

📄 **file_reader.py**

```python
def analizza(file):
    try:
        with open(file, "r", encoding="utf-8") as f:
            testo = f.read()
            righe = testo.splitlines()
            parole = testo.split()
            print(f"Righe: {len(righe)}")
            print(f"Parole: {len(parole)}")
            print(f"Caratteri: {len(testo)}")
    except FileNotFoundError:
        print("File non trovato.")

nome_file = input("Nome file da analizzare: ")
analizza(nome_file)
```

