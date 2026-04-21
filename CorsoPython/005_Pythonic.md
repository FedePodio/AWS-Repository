# ✔️ Caratteristiche del codice *Pythonic*

In programmazione, **“Pythonic”** significa **scrivere codice nello stile tipico, elegante e naturale del linguaggio Python**, sfruttando al meglio le sue caratteristiche.

Non è solo “codice che funziona”, ma **codice che un programmatore Python esperto riconoscerebbe come ben scritto**, leggibile e idiomatico.

---

### **1. Sfrutta le funzioni e le strutture del linguaggio**

Esempi:

* usare `with open(...)` invece di `open()` e `close()`
* usare `diz.get(key, default)` invece di `if key in diz`
* usare list comprehension quando ha senso
* usare tuple unpacking (`a, b = ...`)

### **2. È semplice e leggibile**

Python segue il principio *"Simple is better than complex"* (Zen of Python).

Un codice Pythonic è conciso **senza essere criptico**.

---

# ✔️ Esempio non Pythonic vs Pythonic

### ❌ NON PYTHONIC

```python
diz = {}
if nome not in diz:
    diz[nome] = vincita
else:
    diz[nome] = diz[nome] + vincita
```

### ✔️ PYTHONIC

```python
diz[nome] = diz.get(nome, 0) + vincita
```

---

# ✔️ Altro esempio

### ❌ NON PYTHONIC

```python
righe = f.readlines()
for riga in righe:
    print(riga)
```

### ✔️ PYTHONIC

```python
for riga in f:
    print(riga)
```

---

# ✔️ Zen of Python (riassunto utile)

Python ha una filosofia chiamata "Zen of Python".
Si può vedere con:

```python
import this
```

Principi importanti:

* **Readability counts.**
* **Simple is better than complex.**
* **There should be one— and preferably only one —obvious way to do it.**
* **Beautiful is better than ugly.**

---

# ✔️ Riassunto

**Pythonic = usare Python come è pensato per essere usato.**
Vuol dire:

* scrivere codice elegante
* semplice
* leggibile
* idiomatico
* che usa gli strumenti del linguaggio

