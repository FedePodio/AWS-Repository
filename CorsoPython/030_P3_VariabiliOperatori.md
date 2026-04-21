# 📘 Corso Python – Modulo 3

## Variabili e Operatori

---

### 1. Variabili in Python

* Una variabile è un “contenitore” che memorizza un valore.
* In Python **non serve dichiarare il tipo**: viene dedotto automaticamente.

Esempi:

```python
x = 10         # int
prezzo = 19.99 # float
nome = "Anna"  # stringa
attivo = True  # booleano
```

---

### 2. Naming convention

* Il nome può contenere lettere, numeri e `_` ma **non può iniziare con un numero**.
* Convenzioni comuni:

  * `snake_case` → `nome_variabile` ✅
  * evitare nomi troppo generici → `dato`, `x` ❌
  * nomi descrittivi → `prezzo_prodotto` ✅

---

### 3. Assegnazioni multiple

```python
a, b = 5, 10
print(a, b)  # 5 10
```

```python
x = y = z = 0
print(x, y, z)  # 0 0 0
```

---

### 4. Operatori aritmetici

```python
a, b = 7, 3

print(a + b)   # 10 (somma)
print(a - b)   # 4 (sottrazione)
print(a * b)   # 21 (moltiplicazione)
print(a / b)   # 2.333... (divisione)
print(a // b)  # 2 (divisione intera)
print(a % b)   # 1 (resto)
print(a ** b)  # 343 (potenza)
```

---

### 5. Operatori di confronto

```python
x, y = 5, 10

print(x == y)  # False
print(x != y)  # True
print(x < y)   # True
print(x > y)   # False
print(x <= 5)  # True
print(y >= 10) # True
```

---

### 6. Operatori logici

```python
p, q = True, False

print(p and q)  # False
print(p or q)   # True
print(not p)    # False
```

---

### 7. Operatori di assegnazione

```python
x = 10
x += 5   # equivalente a x = x + 5
x -= 3   # equivalente a x = x - 3
x *= 2
x /= 4
```

---

### 8. Operatori su stringhe

```python
nome = "Python"
print(nome * 3)       # "PythonPythonPython"
print("Py" + "thon")  # "Python"
```
