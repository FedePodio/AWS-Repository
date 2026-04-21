# 📘 Corso Python – Modulo 7

## Input/Output

---

### 1. Input da tastiera

* Con la funzione `input()` si acquisisce una stringa da tastiera.

```python
nome = input("Come ti chiami? ")
print("Ciao", nome)
```

⚠️ Tutto ciò che arriva da `input()` è una **stringa**, bisogna fare conversioni:

```python
età = int(input("Quanti anni hai? "))
print("Tra 10 anni avrai", età + 10)
```

---

### 2. Output con `print()`

```python
print("Hello, World!")   # stampa stringa
print(10, 20, 30)        # separa con spazio
print("A", "B", sep="-") # separatore personalizzato
print("Fine", end="!")   # senza a capo
```

---

### 3. Formattazione dell’output

#### Con `f-string` (consigliato)

```python
nome = "Anna"
età = 22
print(f"{nome} ha {età} anni")
```

#### Con `format()`

```python
print("{} ha {} anni".format("Luca", 30))
```

#### Con percentuale (vecchio stile)

```python
print("%s ha %d anni" % ("Marco", 25))
```

---

### 4. Lavorare con i file

Apertura file con `open(nome, modalità)`:

* `"r"` = lettura (default)
* `"w"` = scrittura (sovrascrive)
* `"a"` = append (aggiunge in coda)
* `"x"` = crea un nuovo file
* `"b"` = binario

---

### 5. Lettura da file

```python
f = open("dati.txt", "r")
contenuto = f.read()
f.close()
print(contenuto)
```

```python
f = open("dati.txt", "r")
for riga in f:
    print(riga.strip())
f.close()
```

---

### 6. Scrittura su file

```python
f = open("output.txt", "w")
f.write("Ciao Python!\n")
f.write("Seconda riga\n")
f.close()
```

---

### 7. Gestione sicura con `with`

Chiude automaticamente il file alla fine del blocco.

```python
with open("output.txt", "a") as f:
    f.write("Nuova riga\n")
```

---

### 8. Lettura e scrittura insieme

```python
with open("note.txt", "r+") as f:
    contenuto = f.read()
    f.write("\nAggiunta finale")
```

