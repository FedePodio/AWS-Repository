# 📘 Corso Python – Modulo 2

## Tipi di dati di base

---

### 1. Tipi fondamentali

Python fornisce diversi tipi di dato integrati:

* **Numeri interi**: `int`

  ```python
  x = 42
  ```

* **Numeri decimali**: `float`

  ```python
  pi = 3.14159
  ```

* **Valori booleani**: `bool`

  ```python
  vero = True
  falso = False
  ```

* **Stringhe di testo**: `str`

  ```python
  nome = "Python"
  ```

---

### 2. Controllare il tipo

```python
x = 10
print(type(x))  # <class 'int'>
```

---

### 3. Operazioni sui numeri

* Somma, sottrazione, moltiplicazione, divisione:

  ```python
  a, b = 5, 2
  print(a + b)  # 7
  print(a - b)  # 3
  print(a * b)  # 10
  print(a / b)  # 2.5 (float)
  ```

* Divisione intera `//`, resto `%`, potenza `**`:

  ```python
  print(7 // 3)  # 2
  print(7 % 3)   # 1
  print(2 ** 3)  # 8
  ```

---

### 4. Stringhe

* Creazione:

  ```python
  s1 = "Ciao"
  s2 = 'Python'
  ```

* Concatenazione:

  ```python
  print(s1 + " " + s2)  # Ciao Python
  ```

* Moltiplicazione:

  ```python
  print("Ha" * 3)  # HaHaHa
  ```

* Slicing:

  ```python
  testo = "Programmazione"
  print(testo[0])     # 'P'
  print(testo[-1])    # 'e'
  print(testo[0:7])   # 'Program'
  ```

---

### 5. Metodi utili per stringhe

```python
msg = "ciao mondo"
print(msg.upper())   # 'CIAO MONDO'
print(msg.capitalize())  # 'Ciao mondo'
print(msg.replace("mondo", "Python"))  # 'ciao Python'
print(len(msg))  # lunghezza
```

---

### 6. Conversioni di tipo (Casting)

* Da numero a stringa:

  ```python
  str(123)  # "123"
  ```

* Da stringa a numero:

  ```python
  int("42")   # 42
  float("3.14")  # 3.14
  ```

* Da booleano a intero:

  ```python
  int(True)   # 1
  int(False)  # 0
  ```

