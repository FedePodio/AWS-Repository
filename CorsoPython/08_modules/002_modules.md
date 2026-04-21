# Ecco un'altra selezione di moduli "must-know" per chi impara Python

---

### 4. Modulo `math` & `random`: Il Generatore di Cerchi

In questo esercizio uniamo la geometria alla casualità. L'obiettivo è generare raggi casuali e calcolare le aree.

```python
import math
import random

def geometria_casuale():
    # 1. Genera un raggio casuale tra 1 e 10 (float)
    # TODO: Usa random.uniform(1, 10)
    raggio = 

    # 2. Calcola l'area del cerchio (Area = pi * r^2)
    # TODO: Usa math.pi e math.pow() oppure l'operatore **
    area = 

    # 3. Arrotonda il risultato per eccesso
    # TODO: Usa math.ceil()
    area_arrotondata = 

    print(f"Raggio generato: {raggio:.2f}")
    print(f"L'area del cerchio è: {area:.2f}")
    print(f"Area arrotondata per eccesso: {area_arrotondata}")

# Sfida Extra: Genera 5 cerchi e trova quello con l'area maggiore usando max()

```

---

### 5. Modulo `statistics`: L'Analizzatore di Voti

Questo modulo è utilissimo per introdurre i concetti base dell'analisi dati senza usare librerie pesanti come Pandas.

```python
import statistics

def analizza_voti():
    # Lista di voti di una classe
    voti = [24, 27, 30, 18, 22, 24, 26, 30, 24, 29]

    # 1. Calcola la media aritmetica
    # TODO: Usa statistics.mean()
    media = 

    # 2. Trova la moda (il voto più frequente)
    # TODO: Usa statistics.mode()
    voto_comune = 

    # 3. Calcola la mediana
    # TODO: Usa statistics.median()
    mediana = 

    print(f"Media dei voti: {media}")
    print(f"Voto più frequente: {voto_comune}")
    print(f"Valore mediano: {mediana}")

# Sfida Extra: Aggiungi un controllo che verifichi se la media è >= 18 (promosso)

```

---

### 6. Modulo `shutil`: Il Gestore di File (Livello High-Level)

Mentre `os` lavora sui percorsi, `shutil` è la "ruspa" che serve per spostare e copiare intere cartelle o file con un solo comando.

```python
import shutil
import os

def gestore_archivi():
    file_origine = "appunti.txt"
    file_destinazione = "appunti_backup.txt"

    # Creiamo un file di prova se non esiste
    with open(file_origine, "w") as f:
        f.write("Questi sono i miei appunti di Python.")

    # 1. Copia il file
    # TODO: Usa shutil.copy(origine, destinazione)
    
    # 2. Crea un archivio compresso (ZIP) di una cartella
    # TODO: Usa shutil.make_archive("nome_zip", "zip", "cartella_da_zippare")
    # Nota: Assicurati che la cartella esista!

    print(f"Copia di {file_origine} creata con successo.")

# Sfida Extra: Scrivi una funzione che cerchi tutti i file .png e li sposti in una cartella 'Immagini'

```

---

### 7. Modulo `re` (Basics): Il Cacciatore di Email

Le espressioni regolari possono spaventare, ma per una scheda didattica basta mostrare come validare un formato semplice.

```python
import re

def convalida_email():
    testo = "Contattami a info@esempio.it o a supporto@python.org"
    
    # 1. Definisci un pattern semplice per l'email
    # Questo pattern cerca: caratteri + @ + caratteri + . + caratteri
    pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

    # 2. Trova tutte le email nel testo
    # TODO: Usa re.findall(pattern, testo)
    email_trovate = 

    print(f"Email estratte: {email_trovate}")

    # 3. Verifica se un input dell'utente è una mail valida
    user_input = input("Inserisci la tua email: ")
    # TODO: Usa re.match(pattern, user_input)
    if re.match(pattern, user_input):
        print("Email valida!")
    else:
        print("Formato email non valido.")

# Sfida Extra: Modifica il pattern per cercare solo email che finiscono con .edu

```

