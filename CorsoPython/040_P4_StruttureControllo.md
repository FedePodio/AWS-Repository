# 📘 Corso Python – Modulo 4

## Strutture di controllo

---

### 1. Le decisioni: `if / elif / else`

Permettono di eseguire istruzioni diverse a seconda di una condizione.

```python
x = 10

if x > 0:
    print("Numero positivo")
elif x == 0:
    print("Zero")
else:
    print("Numero negativo")
```

⚠️ **Indentazione obbligatoria**: in Python gli spazi sono parte della sintassi.

---

### 2. Ciclo `while`

Ripete un blocco finché la condizione è vera.

```python
n = 1
while n <= 5:
    print(n)
    n += 1
```

⚠️ Attenzione: se la condizione non diventa mai falsa → ciclo infinito.

---

### 3. Ciclo `for`

Itera su una sequenza (lista, stringa, range...).

```python
for i in range(5):
    print(i)  # stampa 0,1,2,3,4
```

```python
for lettera in "Python":
    print(lettera)
```

---

### 4. Funzioni utili

* `range(start, stop, step)` → genera numeri in sequenza

  ```python
  for i in range(2, 10, 2):
      print(i)  # 2 4 6 8
  ```

* `enumerate()` → restituisce indice + valore

  ```python
  parole = ["ciao", "mondo"]
  for i, parola in enumerate(parole):
      print(i, parola)
  ```

---

### 5. Interruzione di cicli

* **`break`** → esce dal ciclo
* **`continue`** → salta all’iterazione successiva
* **`pass`** → non fa nulla (placeholder)

```python
for i in range(10):
    if i == 5:
        break   # interrompe il ciclo
    if i % 2 == 0:
        continue  # salta i numeri pari
    print(i)
```

---

### 6. Esempio combinato

```python
numero = int(input("Inserisci un numero: "))

if numero % 2 == 0:
    print("Pari")
else:
    print("Dispari")

for i in range(1, numero + 1):
    if i % 2 == 0:
        print(i, "è pari")
    else:
        print(i, "è dispari")
```

