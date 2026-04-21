# Moduli built-in di Python: Guida Rapida

Python è famoso per la sua filosofia **"batteries included"**: la sua libreria standard è vastissima e permette di fare quasi tutto senza installare pacchetti esterni.

Ecco una panoramica dei moduli built-in più utilizzati e dei loro metodi principali.

---

## 🛠️ Interazione con il Sistema Operativo

Questi moduli sono fondamentali per gestire file, cartelle e parametri di sistema.

### 1. `os` (Operating System)

Permette di interagire con il sistema operativo sottostante.

* `os.getcwd()`: Restituisce la directory di lavoro corrente.
* `os.listdir(path)`: Elenca i file e le cartelle in un percorso.
* `os.mkdir(dir)`: Crea una nuova cartella.
* `os.path.join(path, *paths)`: Unisce diversi segmenti di percorso in modo intelligente (gestendo `/` o `\`).
* `os.path.exists(path)`: Verifica se un file o una cartella esiste.

### 2. `sys` (System-specific parameters)

Fornisce l'accesso a variabili e funzioni utilizzate dall'interprete Python.

* `sys.argv`: Una lista che contiene gli argomenti passati da riga di comando.
* `sys.exit()`: Esce dal programma.
* `sys.path`: Una lista di stringhe che specifica i percorsi di ricerca per i moduli.

---

## 🔢 Matematica e Logica

### 3. `math`

Fornisce funzioni matematiche per numeri reali.

* `math.sqrt(x)`: Radice quadrata.
* `math.ceil(x)` / `math.floor(x)`: Arrotondamento per eccesso o per difetto.
* `math.pi`: La costante Pi greco.
* `math.pow(x, y)`: Elevamento a potenza.

### 4. `random`

Utilizzato per generare numeri pseudo-casuali.

* `random.random()`: Restituisce un float tra 0.0 e 1.0.
* `random.randint(a, b)`: Restituisce un intero casuale tra `a` e `b` inclusi.
* `random.choice(sequence)`: Sceglie un elemento a caso da una lista o tupla.
* `random.shuffle(list)`: Mescola gli elementi di una lista sul posto.

---

## 📅 Gestione Dati e Tempo

### 5. `datetime`

Indispensabile per manipolare date e orari.

* `datetime.datetime.now()`: Restituisce la data e l'ora attuali.
* `datetime.date(year, month, day)`: Crea un oggetto data.
* `strftime(format)`: Formatta una data in una stringa leggibile (es. `"%d/%m/%Y"`).
* `strptime(string, format)`: Converte una stringa in un oggetto datetime.

### 6. `json`

Per codificare e decodificare dati in formato JSON (standard nel web).

* `json.dumps(obj)`: Converte un dizionario/lista Python in una stringa JSON.
* `json.loads(string)`: Converte una stringa JSON in un oggetto Python.
* `json.dump(obj, file)`: Scrive dati JSON direttamente in un file.

---

## 🔍 Manipolazione Testo e Dati complessi

### 7. `re` (Regular Expressions)

Per la ricerca e manipolazione avanzata di stringhe tramite espressioni regolari.

* `re.search(pattern, string)`: Cerca la prima corrispondenza del pattern.
* `re.findall(pattern, string)`: Restituisce una lista di tutte le corrispondenze.
* `re.sub(pattern, repl, string)`: Sostituisce le occorrenze del pattern con una stringa.

### 8. `collections`

Offre tipi di dati specializzati che estendono i classici `dict`, `list`, `set` e `tuple`.

* `Counter`: Conta gli elementi in un iterabile.
* `namedtuple()`: Crea tuple i cui elementi sono accessibili anche tramite nome.
* `defaultdict`: Un dizionario che non solleva errori se una chiave è assente, ma crea un valore di default.

---

### Tabella Riassuntiva Rapida

| Modulo | Scopo Principale | Metodo Simbolo |
| --- | --- | --- |
| **os** | File system | `os.path.join()` |
| **sys** | Interprete | `sys.argv` |
| **math** | Calcoli scientifici | `math.sqrt()` |
| **datetime** | Gestione tempo | `datetime.now()` |
| **json** | Scambio dati | `json.loads()` |
| **random** | Casualità | `random.randint()` |

---

## 1. Modulo `os`: Il ponte verso il File System

Il modulo `os` permette al codice Python di "guardare fuori" dalla propria finestra e interagire con le cartelle e i file del computer.

* **Concetto chiave:** L'indipendenza dalla piattaforma. Usare `os.path.join("cartella", "file.txt")` garantisce che il codice funzioni sia su Windows (che usa `\`) che su Linux/Mac (che usano `/`).
* **Snippet Didattico:**

```python
import os
# Creare una cartella solo se non esiste
if not os.path.exists("dati_esercitazione"):
    os.mkdir("dati_esercitazione")

```

* **Pro-Tip:** Oggi esiste anche `pathlib` (più moderno e orientato agli oggetti), ma `os` resta lo standard fondamentale da conoscere.

---

## 2. Modulo `sys`: Il controllo dell'Interprete

Mentre `os` gestisce il computer, `sys` gestisce l'ambiente di Python stesso.

* **L'uso dei parametri (`sys.argv`):** È fondamentale per creare script che accettano input da terminale (es: `python script.py file_da_leggere.txt`).
* **Gestione dei percorsi (`sys.path`):** Spiega che se Python "non trova un modulo", è perché quel percorso non è in questa lista.
* **Esempio didattico:**

```python
import sys
print(f"Versione di Python in uso: {sys.version}")
print(f"Argomenti passati allo script: {sys.argv}")

```

---

## 3. Modulo `datetime`: Gestire il Tempo

Il tempo in programmazione è complesso (fusi orari, anni bisestili). `datetime` semplifica tutto.

* **La sfida dei formati:** Da non confondere `strftime` e `strptime`.
* **`strftime` (f = format):** Da oggetto a stringa (per stampare la data).
* **`strptime` (p = parse):** Da stringa a oggetto (per elaborare una data scritta dall'utente).

* **Operazioni matematiche:** Si possono sottrarre due date per ottenere un oggetto `timedelta` (la differenza di tempo).

---

## 4. Modulo `json`: Lo standard dello scambio dati

JSON è la lingua franca del web. 

* **La distinzione "s":**
* `json.dump()` e `json.load()` lavorano con i **file**.
* `json.dumps()` e `json.loads()` lavorano con le **stringhe** (la "s" sta per string).

* **Esempio pratico:**

```python
import json
dati = {"studente": "Mario", "voti": [28, 30, 27]}
stringa_json = json.dumps(dati) # Serializzazione

```

---

## 5. Modulo `collections`: Strutture dati "Speciali"

Questo è un modulo per un livello intermedio, ottimo per mostrare come scrivere codice più pulito.

* **`Counter`**: Perfetto per esercizi di analisi del testo (es. "conta quante volte appare ogni parola").
* **`defaultdict`**: Risolve il fastidioso errore `KeyError`. Se cerchi una chiave che non esiste, la crea lui con un valore di default (es. 0 o una lista vuota).
* **`namedtuple`**: Per creare oggetti leggeri senza dover scrivere una classe intera.

---

## 6. Modulo `re`: La potenza delle Regex

Le Espressioni Regolari sono come un "super-cerca" per il testo.

* **Caso d'uso tipico:** Validare una email o estrarre tutti i numeri di telefono da un documento.
* **Metodo chiave:** `re.findall(pattern, testo)` è il più intuitivo per chi inizia, perché restituisce una lista di tutto ciò che ha trovato.

---

### Suggerimento per Esercizi Pratici

* *In `random`:* Ricorda che `random.randint(1, 6)` include sia l'1 che il 6 (a differenza del `range` classico).
* *In `os`:* Prima di eliminare un file con `os.remove()`, controlla sempre che esista!

