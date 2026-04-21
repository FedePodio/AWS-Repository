# 📘 Corso Python – Modulo 1

## Introduzione a Python

---

### 1. Cos’è Python?

* Linguaggio di programmazione **interpretato**, **ad alto livello**
* Creato da **Guido van Rossum** (1991)
* Open source, multipiattaforma
* Famoso per:

  * Sintassi semplice e leggibile
  * Grande ecosistema di librerie
  * Utilizzo in campi diversi: sviluppo web, automazione, data science, AI, scripting

---

### 2. Perché imparare Python?

* Uno dei linguaggi più usati al mondo
* Richiesto nel mondo del lavoro
* Facile da imparare, adatto anche a principianti
* Supporta vari paradigmi:

  * Procedurale
  * Orientato agli oggetti
  * Funzionale

---

### 3. Installazione

* **Windows**: scaricare da [python.org](https://www.python.org)
* **Linux/macOS**: spesso già installato, altrimenti `sudo apt install python3`
* **Ambienti consigliati**:

  * IDLE (integrato)
  * **VS Code** (molto usato)
  * **PyCharm** (IDE professionale)
  * **Jupyter Notebook** (per data science e didattica)

---

### 4. Il primo programma

File `hello.py`:

```python
print("Hello, World!")
```

* Esecuzione da terminale:

  ```bash
  python hello.py
  ```

* Oppure interattivo:

  ```bash
  python
  >>> print("Hello, World!")
  ```

---

### 5. Come funzionano i programmi Python

* Python legge ed esegue il codice **riga per riga** (interprete)
* Non serve compilazione preventiva
* L’indentazione (spazi) ha valore sintattico:

  ```python
  if True:
      print("Indentazione corretta")
  ```
