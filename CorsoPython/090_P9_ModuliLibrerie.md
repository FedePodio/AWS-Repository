# 📘 Corso Python – Modulo 9

## Moduli e Librerie

---

### 1. Cos’è un modulo?

* Un **file Python** (`.py`) che contiene funzioni, classi o variabili.
* Permette di **organizzare** il codice e **riutilizzarlo**.

```python
# modulo mio_modulo.py
def saluta(nome):
    return f"Ciao {nome}!"
```

```python
# programma principale
import mio_modulo
print(mio_modulo.saluta("Anna"))
```

---

### 2. Importazione

* Import completo:

  ```python
  import math
  print(math.sqrt(16))  # 4.0
  ```

* Import parziale:

  ```python
  from math import sqrt
  print(sqrt(25))  # 5.0
  ```

* Alias:

  ```python
  import math as m
  print(m.pi)
  ```

---

### 3. Moduli standard utili

* **math** → funzioni matematiche
* **random** → numeri casuali
* **datetime** → date e orari
* **os** → interazione con sistema operativo
* **sys** → parametri ed esecuzione
* **statistics** → medie, varianze, ecc.

Esempi:

```python
import random, datetime

print(random.randint(1, 6))  # simulazione dado
print(datetime.date.today()) # data di oggi
```

---

### 4. Pacchetti

* Un **pacchetto** è una cartella con più moduli e un file `__init__.py`.
* Struttura:

  ```
  mio_pacchetto/
      __init__.py
      modulo1.py
      modulo2.py
  ```

---

### 5. Librerie esterne

* Installazione con **pip**:

  ```bash
  pip install requests
  ```

* Uso:

  ```python
  import requests
  risposta = requests.get("https://api.github.com")
  print(risposta.status_code)
  ```

---

### 6. Dove trovare librerie

* **PyPI (Python Package Index):**
  👉 [https://pypi.org](https://pypi.org)
* Migliaia di librerie disponibili:

  * Flask, Django → web
  * NumPy, Pandas → dati
  * Matplotlib → grafici
  * TensorFlow, PyTorch → AI

---

### 7. Buone pratiche

✅ Organizzare il codice in più file/moduli
✅ Usare nomi chiari per i moduli
✅ Non reinventare la ruota: usare librerie già esistenti
✅ Documentarsi su PyPI

---

# 📘 Corso Python – Modulo 9: Moduli e Librerie (Versione Approfondita)

## 1. Introduzione ai Moduli

### Cos'è un modulo?

Un **modulo** in Python è semplicemente un file `.py` che contiene definizioni di funzioni, classi, variabili e statement eseguibili. I moduli servono per:
* **Organizzare** il codice in unità logiche
* **Riutilizzare** funzionalità comuni
* **Evitare duplicazioni** di codice
* **Migliorare la manutenibilità** dei progetti

### Esempio pratico completo

**File: operazioni_matematiche.py**

```python
"""
Modulo per operazioni matematiche di base
"""

PI = 3.14159

def area_cerchio(raggio):
    """Calcola l'area di un cerchio"""
    return PI * raggio ** 2

def area_rettangolo(base, altezza):
    """Calcola l'area di un rettangolo"""
    return base * altezza

def volume_sfera(raggio):
    """Calcola il volume di una sfera"""
    return (4/3) * PI * raggio ** 3

class Calcolatrice:
    """Classe per operazioni matematiche avanzate"""
    
    def __init__(self):
        self.storico = []
    
    def somma(self, a, b):
        risultato = a + b
        self.storico.append(f"{a} + {b} = {risultato}")
        return risultato
    
    def mostra_storico(self):
        return self.storico
```

**File principale: main.py**

```python
import operazioni_matematiche

# Utilizzo delle funzioni
print(f"Area cerchio (r=5): {operazioni_matematiche.area_cerchio(5)}")
print(f"Volume sfera (r=3): {operazioni_matematiche.volume_sfera(3)}")

# Utilizzo della classe
calc = operazioni_matematiche.Calcolatrice()
print(calc.somma(10, 20))
print(calc.mostra_storico())
```

---

## 2. Metodi di Importazione Avanzati

### 2.1 Import completo

```python
import math
import os
import sys

# Utilizzo con nome completo del modulo
print(math.sqrt(16))
print(os.getcwd())  # directory corrente
```

### 2.2 Import con alias

```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Convenzioni standard nella community Python
data = np.array([1, 2, 3, 4, 5])
```

### 2.3 Import selettivo

```python
from datetime import datetime, timedelta, date
from random import randint, choice, shuffle

# Utilizzo diretto senza prefisso
oggi = date.today()
numero_casuale = randint(1, 100)
```

### 2.4 Import di tutto (sconsigliato)

```python
# ❌ EVITARE - può causare conflitti di nomi
from math import *

# ✅ MEGLIO - import specifico
from math import sqrt, sin, cos, pi
```

### 2.5 Import condizionale

```python
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False
    print("NumPy non disponibile, usando lista standard")

def calcola_media(numeri):
    if HAS_NUMPY:
        return np.mean(numeri)
    else:
        return sum(numeri) / len(numeri)
```

---

## 3. Moduli Standard della Libreria Python

### 3.1 Modulo `os` - Sistema Operativo

```python
import os

# Informazioni directory
print(f"Directory corrente: {os.getcwd()}")
print(f"Contenuto directory: {os.listdir('.')}")

# Manipolazione percorsi
percorso = os.path.join("cartella", "file.txt")
print(f"Percorso completo: {os.path.abspath(percorso)}")

# Variabili d'ambiente
print(f"Utente: {os.getenv('USER', 'Sconosciuto')}")
```

### 3.2 Modulo `datetime` - Date e Orari

```python
from datetime import datetime, timedelta, date

# Data e ora corrente
ora_corrente = datetime.now()
print(f"Ora corrente: {ora_corrente}")
print(f"Formato personalizzato: {ora_corrente.strftime('%d/%m/%Y %H:%M')}")

# Operazioni con le date
domani = date.today() + timedelta(days=1)
una_settimana_fa = datetime.now() - timedelta(weeks=1)

# Parsing da stringa
data_string = "2024-12-25"
natale = datetime.strptime(data_string, "%Y-%m-%d")
```

### 3.3 Modulo `random` - Numeri Casuali

```python
import random

# Numeri casuali
print(random.randint(1, 100))      # Intero tra 1 e 100
print(random.random())             # Float tra 0 e 1
print(random.uniform(1.5, 10.5))   # Float tra 1.5 e 10.5

# Scelte casuali
colori = ["rosso", "blu", "verde", "giallo"]
print(random.choice(colori))       # Un elemento casuale
print(random.sample(colori, 2))    # Due elementi casuali senza ripetizione

# Mescolamento
carte = ["A", "K", "Q", "J"]
random.shuffle(carte)
print(carte)
```

### 3.4 Modulo `json` - Gestione JSON

```python
import json

# Dati Python -> JSON
dati = {
    "nome": "Mario",
    "età": 30,
    "città": "Roma",
    "hobby": ["calcio", "lettura", "viaggi"]
}

# Conversione in stringa JSON
json_string = json.dumps(dati, indent=2, ensure_ascii=False)
print(json_string)

# Salvataggio su file
with open("dati.json", "w", encoding="utf-8") as file:
    json.dump(dati, file, indent=2, ensure_ascii=False)

# Lettura da file
with open("dati.json", "r", encoding="utf-8") as file:
    dati_caricati = json.load(file)
    print(dati_caricati)
```

### 3.5 Modulo `collections` - Strutture Dati Avanzate

```python
from collections import Counter, defaultdict, namedtuple

# Counter - conteggio elementi
parole = ["mela", "banana", "mela", "arancia", "banana", "mela"]
conteggio = Counter(parole)
print(conteggio)  # Counter({'mela': 3, 'banana': 2, 'arancia': 1})
print(conteggio.most_common(2))  # I 2 elementi più comuni

# defaultdict - dizionario con valore predefinito
gruppi = defaultdict(list)
studenti = [("Mario", "A"), ("Lucia", "B"), ("Paolo", "A"), ("Anna", "B")]

for nome, classe in studenti:
    gruppi[classe].append(nome)

# namedtuple - tupla con nomi
Punto = namedtuple("Punto", ["x", "y"])
p1 = Punto(3, 4)
print(f"Coordinate: x={p1.x}, y={p1.y}")
```

---

## 4. Creazione di Pacchetti

### Struttura di un pacchetto

```
mio_progetto/
├── __init__.py
├── utilities/
│   ├── __init__.py
│   ├── math_utils.py
│   └── string_utils.py
├── database/
│   ├── __init__.py
│   ├── connection.py
│   └── queries.py
└── main.py
```

### File `utilities/__init__.py`

```python
"""
Pacchetto utilities per funzioni di supporto
"""

from .math_utils import calcola_media, trova_massimo
from .string_utils import pulisci_stringa, formato_nome

__version__ = "1.0.0"
__author__ = "Il Tuo Nome"

# Funzioni disponibili quando si importa il pacchetto
__all__ = ["calcola_media", "trova_massimo", "pulisci_stringa", "formato_nome"]
```

### File `utilities/math_utils.py`

```python
def calcola_media(numeri):
    """Calcola la media di una lista di numeri"""
    if not numeri:
        return 0
    return sum(numeri) / len(numeri)

def trova_massimo(numeri):
    """Trova il valore massimo in una lista"""
    if not numeri:
        return None
    return max(numeri)

def deviazione_standard(numeri):
    """Calcola la deviazione standard"""
    if len(numeri) < 2:
        return 0
    
    media = calcola_media(numeri)
    varianza = sum((x - media) ** 2 for x in numeri) / (len(numeri) - 1)
    return varianza ** 0.5
```

### Utilizzo del pacchetto

```python
# Import dell'intero pacchetto
import utilities
print(utilities.calcola_media([1, 2, 3, 4, 5]))

# Import specifico
from utilities import calcola_media, trova_massimo
from utilities.string_utils import pulisci_stringa

# Import con alias
import utilities.math_utils as math_tools
```

---

## 5. Gestione delle Librerie Esterne

### 5.1 Installazione con pip

```bash
# Installazione singola libreria
pip install requests

# Installazione versione specifica
pip install django==4.2.0

# Installazione da requirements.txt
pip install -r requirements.txt

# Aggiornamento libreria
pip install --upgrade numpy

# Disinstallazione
pip uninstall matplotlib
```

### 5.2 File requirements.txt

```txt
requests>=2.31.0
pandas>=2.0.0
matplotlib>=3.7.0
numpy>=1.24.0
flask==2.3.0
```

### 5.3 Ambienti virtuali

```bash
# Creazione ambiente virtuale
python -m venv mio_progetto_env

# Attivazione (Linux/Mac)
source mio_progetto_env/bin/activate

# Attivazione (Windows)
mio_progetto_env\Scripts\activate

# Installazione librerie nell'ambiente
pip install requests pandas

# Salvataggio dipendenze
pip freeze > requirements.txt

# Disattivazione ambiente
deactivate
```

---

## 6. Librerie Popolari per Categoria

### 6.1 Sviluppo Web

```python
# Flask - Framework web minimalista
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/saluta/<nome>')
def saluta(nome):
    return jsonify({"messaggio": f"Ciao {nome}!"})

# Django - Framework web completo (esempio configurazione)
# pip install django
# django-admin startproject mio_sito
```

### 6.2 Data Science

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Pandas - manipolazione dati
df = pd.DataFrame({
    'nome': ['Alice', 'Bob', 'Charlie'],
    'età': [25, 30, 35],
    'salario': [50000, 60000, 70000]
})

print(df.describe())  # Statistiche descrittive
print(df.groupby('età').mean())  # Raggruppamento

# NumPy - calcolo numerico
array = np.array([1, 2, 3, 4, 5])
print(f"Media: {np.mean(array)}")
print(f"Deviazione standard: {np.std(array)}")

# Matplotlib - grafici
plt.figure(figsize=(10, 6))
plt.plot(df['nome'], df['salario'], marker='o')
plt.title('Salario per Persona')
plt.xlabel('Nome')
plt.ylabel('Salario')
plt.show()
```

### 6.3 Richieste HTTP

```python
import requests
import json

# GET request
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
if response.status_code == 200:
    data = response.json()
    print(f"Titolo: {data['title']}")

# POST request
nuovo_post = {
    'title': 'Mio Post',
    'body': 'Contenuto del post',
    'userId': 1
}

response = requests.post(
    'https://jsonplaceholder.typicode.com/posts',
    json=nuovo_post,
    headers={'Content-Type': 'application/json'}
)

print(f"Status: {response.status_code}")
print(f"Risposta: {response.json()}")
```

---

## 7. Buone Pratiche e Convenzioni

### 7.1 Organizzazione del Codice

```python
# ✅ Ordine corretto degli import
# 1. Librerie standard
import os
import sys
from datetime import datetime

# 2. Librerie terze parti
import requests
import pandas as pd

# 3. Moduli locali
from .utilities import helper_function
from .database import connection
```

### 7.2 Gestione degli Errori

```python
def carica_configurazione(file_path):
    """Carica configurazione da file JSON con gestione errori"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File {file_path} non trovato. Uso configurazione predefinita.")
        return {"debug": False, "port": 8000}
    except json.JSONDecodeError as e:
        print(f"Errore nel parsing JSON: {e}")
        return None
    except Exception as e:
        print(f"Errore imprevisto: {e}")
        return None
```

### 7.3 Documentazione dei Moduli

```python
"""
Modulo per la gestione degli utenti del sistema.

Questo modulo fornisce funzionalità per:
- Creazione e validazione utenti
- Autenticazione e autorizzazione
- Gestione profili utente

Esempio di utilizzo:
    from user_manager import crea_utente, autentica_utente
    
    utente = crea_utente("mario@email.com", "password123")
    if autentica_utente("mario@email.com", "password123"):
        print("Accesso riuscito!")

Autore: Il Tuo Nome
Data: Gennaio 2024
Versione: 1.2.0
"""

def crea_utente(email, password):
    """
    Crea un nuovo utente nel sistema.
    
    Args:
        email (str): Indirizzo email dell'utente
        password (str): Password dell'utente (minimo 8 caratteri)
    
    Returns:
        dict: Dizionario con i dati dell'utente creato
        None: Se la creazione fallisce
    
    Raises:
        ValueError: Se email o password non sono validi
    
    Example:
        >>> utente = crea_utente("test@email.com", "password123")
        >>> print(utente['email'])
        test@email.com
    """
    # Implementazione funzione...
    pass
```

---

## 8. Debugging e Testing dei Moduli

### 8.1 Testing con unittest

```python
# File: test_operazioni_matematiche.py
import unittest
from operazioni_matematiche import area_cerchio, Calcolatrice

class TestOperazioniMatematiche(unittest.TestCase):
    
    def setUp(self):
        """Metodo eseguito prima di ogni test"""
        self.calc = Calcolatrice()
    
    def test_area_cerchio(self):
        """Test calcolo area cerchio"""
        self.assertAlmostEqual(area_cerchio(1), 3.14159, places=4)
        self.assertAlmostEqual(area_cerchio(0), 0)
    
    def test_calcolatrice_somma(self):
        """Test somma calcolatrice"""
        risultato = self.calc.somma(5, 3)
        self.assertEqual(risultato, 8)
        self.assertEqual(len(self.calc.storico), 1)
    
    def tearDown(self):
        """Metodo eseguito dopo ogni test"""
        pass

if __name__ == '__main__':
    unittest.main()
```

### 8.2 Logging per Debug

```python
import logging

# Configurazione logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def funzione_complessa(dati):
    """Funzione con logging per debug"""
    logger.info(f"Inizio elaborazione di {len(dati)} elementi")
    
    try:
        # Logica della funzione
        risultato = []
        for i, elemento in enumerate(dati):
            logger.debug(f"Elaborazione elemento {i}: {elemento}")
            # ... elaborazione ...
            risultato.append(elemento * 2)
        
        logger.info(f"Elaborazione completata. Risultati: {len(risultato)}")
        return risultato
        
    except Exception as e:
        logger.error(f"Errore durante l'elaborazione: {e}")
        raise
```

---

## 9. Progetti Pratici

### 9.1 Gestore File di Configurazione

```python
# File: config_manager.py
import json
import os
from pathlib import Path

class ConfigManager:
    """Gestore configurazioni dell'applicazione"""
    
    def __init__(self, config_file="config.json"):
        self.config_file = Path(config_file)
        self.config = self._load_config()
    
    def _load_config(self):
        """Carica configurazione da file"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return self._default_config()
        else:
            return self._default_config()
    
    def _default_config(self):
        """Configurazione predefinita"""
        return {
            "database": {
                "host": "localhost",
                "port": 5432,
                "name": "mydb"
            },
            "app": {
                "debug": False,
                "log_level": "INFO"
            }
        }
    
    def get(self, key, default=None):
        """Ottiene valore configurazione"""
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def set(self, key, value):
        """Imposta valore configurazione"""
        keys = key.split('.')
        config = self.config
        
        for k in keys[:-1]:
            if k not in config:
                config[k] = {}
            config = config[k]
        
        config[keys[-1]] = value
        self._save_config()
    
    def _save_config(self):
        """Salva configurazione su file"""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)

# Utilizzo
config = ConfigManager()
print(config.get('database.host'))  # localhost
config.set('app.debug', True)
```

---

## 10. Risorse e Approfondimenti

### Documentazione Ufficiale

- [Python Module Index](https://docs.python.org/3/py-modindex.html)
* [Python Package User Guide](https://packaging.python.org/)

### Repository di Librerie

- [PyPI - Python Package Index](https://pypi.org/)
* [Awesome Python](https://github.com/vinta/awesome-python) - Lista curata di librerie

### Strumenti di Sviluppo

- **Poetry**: Gestione avanzata dipendenze
* **pipenv**: Ambiente virtuale + gestione dipendenze
* **Black**: Formattazione automatica codice
* **pylint/flake8**: Analisi statica codice

### Categorie Librerie Utili

- **Sviluppo Web**: Django, Flask, FastAPI
* **Data Science**: Pandas, NumPy, SciPy, Matplotlib, Seaborn
* **Machine Learning**: Scikit-learn, TensorFlow, PyTorch
* **Database**: SQLAlchemy, psycopg2, pymongo
* **Testing**: pytest, unittest, mock
* **GUI**: tkinter, PyQt, Kivy
* **Networking**: requests, urllib3, socket
