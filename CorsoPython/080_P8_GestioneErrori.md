# 📘 Corso Python – Modulo 8

## Gestione degli errori

---

### 1. Cosa sono gli errori?

* **Errori di sintassi**: violano le regole del linguaggio.

  ```python
  if True
      print("Errore!")  # manca i due punti
  ```

* **Eccezioni**: errori che si verificano durante l’esecuzione.

  ```python
  x = int("abc")  # ValueError
  y = 10 / 0      # ZeroDivisionError
  ```

---

### 2. Struttura `try / except`

Serve per catturare ed evitare che il programma si blocchi.

```python
try:
    numero = int(input("Inserisci un numero: "))
    print("Hai inserito:", numero)
except ValueError:
    print("Errore: devi inserire un numero!")
```

---

### 3. Gestire più eccezioni

```python
try:
    x = int("abc")
except ValueError:
    print("Conversione non valida")
except TypeError:
    print("Errore di tipo")
```

---

### 4. Blocchi aggiuntivi

* **`else`** → eseguito solo se non ci sono eccezioni
* **`finally`** → eseguito sempre

```python
try:
    f = open("dati.txt", "r")
    contenuto = f.read()
except FileNotFoundError:
    print("File non trovato")
else:
    print("Lettura completata")
finally:
    print("Operazione terminata")
```

---

### 5. Sollevare eccezioni (`raise`)

Puoi generare un’eccezione manualmente.

```python
def dividi(a, b):
    if b == 0:
        raise ZeroDivisionError("Divisione per zero non consentita")
    return a / b
```

---

### 6. Buone pratiche

✅ Gestire solo le eccezioni previste
✅ Usare messaggi chiari per l’utente
✅ Evitare `except:` generici senza specificare l’errore
✅ Usare `finally` per chiudere file o connessioni

