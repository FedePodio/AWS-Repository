# Altri Moduli Fondamentali in Python

Ecco i moduli **`pathlib`** (il futuro della gestione file), **`sqlite3`** (per i database) e **`time`** (per il controllo temporale).

---

## 12. Modulo `pathlib`: Gestire i percorsi come oggetti

Mentre il modulo `os` tratta i percorsi dei file come semplici stringhe, `pathlib` li tratta come **oggetti**. È il modo moderno e più leggibile di scrivere codice oggi.

* **Concetto chiave:** Non più concatenazione manuale di cartelle, ma uso dell'operatore `/`.
* **Metodi principali:**
* `Path.cwd()`: Ottiene la cartella corrente.
* `Path.exists()`: Verifica se il file esiste.
* `Path.read_text()`: Legge tutto il file in una stringa (senza bisogno di `open`).

### 💡 Esercizio: "Il Cercatore di Estensioni"

```python
from pathlib import Path

def analizza_cartella():
    # 1. Crea un oggetto Path per la cartella corrente
    cartella = Path.cwd()
    
    print(f"Sto analizzando: {cartella}")

    # 2. Itera su tutti i file .txt
    # TODO: Usa cartella.glob("*.txt")
    for file in cartella.glob("*.txt"):
        # 3. Stampa nome e dimensione
        # TODO: Usa file.name e file.stat().st_size
        print(f"File: {file.name} - Dimensione: {file.stat().st_size} bytes")

# Sfida: Crea una funzione che legga il contenuto di un file usando solo .read_text()

```

---

## 13. Modulo `sqlite3`: Il tuo primo Database

Molti studenti pensano che serva un server complesso per usare i database. Invece, Python ha **SQLite** integrato: un database potente che salva tutto in un unico file `.db`.

* **Concetto chiave:** Linguaggio SQL (Structured Query Language).
* **Flusso di lavoro:** Connessione → Cursore → Esecuzione comando → Commit (salvataggio).

### 💡 Esercizio: "Il Registro dei Videogiochi"

```python
import sqlite3

def gestore_database():
    # 1. Connettiti al database (lo crea se non esiste)
    connessione = sqlite3.connect("videogiochi.db")
    cursore = connessione.cursor()

    # 2. Crea una tabella
    cursore.execute("CREATE TABLE IF NOT EXISTS giochi (titolo TEXT, anno INTEGER)")

    # 3. Inserisci un dato
    titolo = input("Inserisci titolo gioco: ")
    anno = int(input("Anno di uscita: "))
    # TODO: Usa cursore.execute("INSERT INTO giochi VALUES (?, ?)", (titolo, anno))
    
    # 4. Salva e chiudi
    connessione.commit()
    connessione.close()
    print("Dati salvati con successo!")

# Sfida: Scrivi una funzione che legga tutti i giochi dal database usando "SELECT * FROM giochi"

```

---

## 14. Modulo `time`: Cronometri e Pause

Essenziale per misurare quanto tempo impiega un codice a girare o per far "aspettare" il programma.

* **Metodi principali:**
* `time.sleep(secondi)`: Blocca l'esecuzione per un tot di tempo.
* `time.time()`: Restituisce il "Timestamp Unix" (secondi passati dal 1° gennaio 1970).

### 💡 Esercizio: "Il Timer di Studio"

```python
import time

def timer_studio(minuti):
    secondi = minuti * 60
    print(f"Timer avviato per {minuti} minuti. Buon lavoro!")
    
    # 1. Aspetta il tempo indicato
    # TODO: Usa time.sleep()
    
    print("⏰ Tempo scaduto! Fai una pausa.")

def misura_performance():
    # 2. Prendi il tempo iniziale
    inizio = time.time()
    
    # Esegui un'operazione (es. un ciclo lungo)
    sum(range(1000000))
    
    # 3. Prendi il tempo finale e calcola la differenza
    fine = time.time()
    print(f"L'operazione ha richiesto {fine - inizio:.4f} secondi.")

# Sfida: Crea un countdown che stampi ogni secondo rimanente (es. 5... 4... 3...)

```

---

## 15. Modulo `logging`: Addio ai `print` selvaggi

Quando un programma diventa grande, usare `print()` per capire cosa succede non basta più. `logging` permette di scrivere messaggi di errore o di stato in modo ordinato.

* **Livelli di gravità:** DEBUG, INFO, WARNING, ERROR, CRITICAL.

---

### 💡 Esercizio: "Il Diario di Bordo"

```python
import logging

# Configura il logging per scrivere su un file
logging.basicConfig(filename='app.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def divisione_sicura():
    try:
        a = int(input("Numero A: "))
        b = int(input("Numero B: "))
        risultato = a / b
        logging.info(f"Divisione riuscita: {a}/{b} = {risultato}")
    except ZeroDivisionError:
        # TODO: Usa logging.error() per registrare l'errore
        print("Errore: non puoi dividere per zero!")

# Nota: Controlla il file 'app.log' dopo aver eseguito lo script!

```

Questa è la scheda del **Progetto Finale**. È pensata per essere una sfida riepilogativa che trasforma uno studente da "chi scrive piccoli script" a "chi crea un mini-software".

---

# 🏆 PROGETTO FINALE: Sistema Gestione Biblioteca

**Obiettivo:** Creare un programma che gestisca il prestito dei libri, calcoli le scadenze e salvi tutto in un database professionale.

---

## 🛠️ Come lavorano insieme i moduli?

1. **`pathlib`**: Serve a definire dove salvare il database, assicurandosi che il programma funzioni su qualsiasi cartella.
2. **`sqlite3`**: È il cuore del progetto. Memorizza i libri, i nomi degli utenti e le date.
3. **`datetime`**: Serve a registrare il momento esatto del prestito e a calcolare la data di restituzione (es. tra 15 giorni).

---

## 1. La Struttura dei Dati

Il nostro database si chiamerà `biblioteca.db` e conterrà una tabella chiamata `prestiti` con queste colonne:

* **Titolo**: Nome del libro.
* **Utente**: Chi ha preso il libro.
* **Inizio**: Data del prestito.
* **Scadenza**: Data entro cui restituirlo.

---

## 2. Lo Scheletro del Progetto (Da completare)

```python
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path

# --- CONFIGURAZIONE PERCORSO (pathlib) ---
# Creiamo il percorso per il database nella cartella corrente
percorso_db = Path.cwd() / "biblioteca.db"

def inizializza_db():
    """Crea il database e la tabella se non esistono."""
    conn = sqlite3.connect(percorso_db)
    cursor = conn.cursor()
    # TODO: Crea la tabella 'prestiti' con le colonne: titolo, utente, inizio, scadenza
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS prestiti (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titolo TEXT,
            utente TEXT,
            inizio TEXT,
            scadenza TEXT
        )
    ''')
    conn.commit()
    conn.close()

def registra_prestito():
    """Registra un nuovo prestito calcolando le date."""
    titolo = input("Titolo del libro: ")
    utente = input("Nome utente: ")

    # --- LOGICA DEL TEMPO (datetime) ---
    # 1. Prendi la data di oggi
    oggi = datetime.now()
    
    # 2. Calcola la scadenza tra 14 giorni
    # TODO: Usa timedelta(days=14)
    data_scadenza = oggi + timedelta(days=14)

    # Formattiamo le date come stringhe leggibili (es. 2023-12-31)
    inizio_str = oggi.strftime("%d/%m/%Y")
    scadenza_str = data_scadenza.strftime("%d/%m/%Y")

    # --- SALVATAGGIO (sqlite3) ---
    conn = sqlite3.connect(percorso_db)
    cursor = conn.cursor()
    # TODO: Inserisci i dati nella tabella
    cursor.execute("INSERT INTO prestiti (titolo, utente, inizio, scadenza) VALUES (?, ?, ?, ?)", 
                   (titolo, utente, inizio_str, scadenza_str))
    conn.commit()
    conn.close()
    print(f"Prestito registrato! Scadenza: {scadenza_str}")

def visualizza_prestiti():
    """Mostra tutti i prestiti attivi."""
    conn = sqlite3.connect(percorso_db)
    cursor = conn.cursor()
    # TODO: Seleziona tutti i dati dalla tabella prestiti
    cursor.execute("SELECT * FROM prestiti")
    righe = cursor.fetchall()
    
    print("\n--- ELENCO PRESTITI ---")
    for riga in righe:
        print(f"ID: {riga[0]} | Libro: {riga[1]} | Utente: {riga[2]} | Scadenza: {riga[4]}")
    conn.close()

# --- AVVIO PROGRAMMA ---
if __name__ == "__main__":
    inizializza_db()
    while True:
        print("\n1. Nuovo Prestito | 2. Elenco | 3. Esci")
        scelta = input("Scegli: ")
        if scelta == "1": registra_prestito()
        elif scelta == "2": visualizza_prestiti()
        elif scelta == "3": break

```

---

## 🧐 Approfondimento per lo studente

### La magia di `timedelta`

Nel progetto abbiamo usato `timedelta(days=14)`. Questo oggetto è fondamentale perché Python gestisce automaticamente il passaggio tra mesi e anni. Se presti un libro il 28 dicembre, Python sa che tra 14 giorni saremo a gennaio dell'anno dopo!

### Perché `Path.cwd() / "nome.db"`?

L'operatore `/` usato con `Path` non è una divisione matematica. `pathlib` ha "sovrascritto" quell'operatore per permetterti di unire percorsi in modo elegante, sostituendo il vecchio e noioso `os.path.join()`.

---

## 🌟 Sfide Extra

1. **Cerca Scadenze**: Aggiungi una funzione che mostri solo i libri la cui scadenza è oggi (usa `datetime.now().strftime(...)` per il confronto).
2. **Cancellazione**: Aggiungi una funzione per eliminare un prestito dal database quando il libro viene restituito (usa il comando SQL `DELETE FROM prestiti WHERE id = ?`).
3. **Esporta in JSON**: Usa il modulo `json` per esportare l'elenco dei prestiti in un file `.json` di backup.

---

### Cosa abbiamo imparato?

Con questo progetto, hai creato un software che:

* Ha una **memoria a lungo termine** (Database).
* Capisce il **concetto di tempo** (Scadenze).
* Sa **dove si trova** nel computer (File System).

