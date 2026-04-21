# moduli built-in di Python: Esercizi Pratici

---

## 📂 Modulo `os` e `sys`

**Sfida: "L'Organizzatore di File"**
Crea uno script che:

1. Prenda come argomento da riga di comando (usando `sys.argv`) il nome di una cartella.
2. Controlli se la cartella esiste.
3. Se esiste, elenchi tutti i file al suo interno e crei una sottocartella chiamata `backup`.
4. Sposti (o copi) un file specifico dentro la cartella `backup`.

* **Cosa imparano:** Gestione dei percorsi, verifica esistenza file, automazione di sistema.

---

## 🔢 Modulo `math` e `random`

**Sfida: "Il Simulatore di Lancio Dadi"**
Scrivi un programma che simuli il lancio di due dadi a 6 facce per 1000 volte.

1. Usa `random.randint` per generare i lanci.
2. Calcola la media dei risultati.
3. Usa `math.isclose` per verificare se la media ottenuta è vicina alla media teorica ( per dado).

---

## 📅 Modulo `datetime`

**Sfida: "Calcolatore di Scadenze"**
Crea un programma che chieda all'utente la sua data di nascita (formato `GG/MM/AAAA`).

1. Trasforma la stringa in un oggetto `datetime` usando `strptime`.
2. Calcola quanti giorni mancano al suo prossimo compleanno.
3. Stampa il giorno della settimana in cui cadrà il suo prossimo compleanno (es. "Sarà un Sabato").

* **Pro-Tip didattico:** Fai attenzione alla gestione degli anni bisestili se il compleanno è il 29 febbraio!

---

## 📦 Modulo `json`

**Sfida: "La Rubrica Digitale"**
Crea un piccolo database in formato JSON.

1. Definisci un dizionario Python con alcuni contatti (nome e telefono).
2. Salva questo dizionario in un file chiamato `rubrica.json`.
3. Riapri il file, aggiungi un nuovo contatto al dizionario e salva nuovamente.

---

## 🔍 Modulo `re` e `collections`

**Sfida: "Analizzatore di Testo Avanzato"**
Prendi un paragrafo di testo (es. un articolo di giornale) e:

1. Usa `re.findall` per estrarre tutte le parole che iniziano con una lettera maiuscola.
2. Usa `re.sub` per rimuovere tutta la punteggiatura dal testo.
3. Usa `collections.Counter` per trovare le 3 parole più frequenti nel testo pulito.

---

## 💡 Idea per un "Esercizio Riepilogativo"

Se vuoi creare una scheda di fine modulo, potresti proporre un **"Gestore di Spese"**:

* L'utente inserisce una spesa (nome e importo).
* Il programma salva la data corrente (`datetime`).
* Salva tutto in un file `spese.json`.
* A fine mese, il programma legge il file e calcola il totale (`math.fsum`) e la categoria più frequente (`collections.Counter`).

---

### Struttura consigliata per la tua scheda

Per ogni esercizio, ti suggerisco di includere:

1. **Obiettivo:** Quale problema risolviamo?
2. **Ingredienti:** Quali moduli e metodi servono.
3. **Traccia di codice:** Un piccolo scheletro con dei `# TODO` da riempire.
4. **Soluzione commentata:** Da mettere sul retro o in fondo.

---

## Usa i tre scheletri di codice pronti qui sotto per risolvere gli esercizi

---

### 1. Scheda `os` & `sys`: L'Organizzatore di File

Questo esercizio insegna a manipolare il file system e a leggere parametri dall'esterno.

```python
import os
import sys

def organizza_cartella():
    # 1. Controlla se l'utente ha passato un argomento (il nome della cartella)
    if len(sys.argv) < 2:
        print("Errore: Devi fornire il percorso di una cartella.")
        sys.exit(1)

    percorso = sys.argv[1]

    # 2. Verifica se il percorso esiste ed è una cartella
    # TODO: Usa os.path.exists() e os.path.isdir()
    
    print(f"Analizzando la cartella: {percorso}")

    # 3. Crea una cartella di backup se non esiste
    path_backup = os.path.join(percorso, "backup")
    # TODO: Usa os.mkdir() gestendo l'eventualità che esista già

    # 4. Elenca i file e "fai finta" di spostarli
    # TODO: Usa os.listdir() per iterare sui file
    # for file in ... :
    #     print(f"Trovato file: {file}")

if __name__ == "__main__":
    organizza_cartella()

```

---

### 2. Scheda `datetime`: Il Calcolatore di Compleanni

Perfetto per spiegare la differenza tra "oggetti tempo" e "stringhe".

```python
from datetime import datetime

def calcola_compleanno():
    data_input = input("Inserisci la tua data di nascita (GG/MM/AAAA): ")

    try:
        # 1. Converti la stringa in oggetto datetime
        # TODO: Usa datetime.strptime()
        nascita = 

        # 2. Ottieni la data di oggi
        oggi = datetime.now()

        # 3. Crea la data del prossimo compleanno (stesso giorno/mese, anno corrente)
        # TODO: Usa il metodo .replace() sull'oggetto nascita
        prossimo_compleanno = 

        # Se il compleanno è già passato quest'anno, calcola quello dell'anno prossimo
        if prossimo_compleanno < oggi:
            prossimo_compleanno = prossimo_compleanno.replace(year=oggi.year + 1)

        # 4. Calcola la differenza
        differenza = prossimo_compleanno - oggi
        
        # 5. Stampa il risultato e il giorno della settimana
        # TODO: Usa .days per i giorni e .strftime("%A") per il nome del giorno
        print(f"Mancano {differenza.days} giorni al tuo compleanno!")
        print(f"Cadrà di: {prossimo_compleanno.strftime('%A')}")

    except ValueError:
        print("Formato data non valido!")

calcola_compleanno()

```

---

### 3. Scheda `json` & `collections`: Analizzatore di Inventario

Un esercizio più avanzato che combina la gestione dati con il conteggio intelligente.

```python
import json
from collections import Counter

def analizza_inventario(file_json):
    # 1. Carica i dati dal file
    # TODO: Apri il file con open() e usa json.load()
    with open(file_json, 'r') as f:
        dati = 

    # Immaginiamo che 'dati' sia una lista di prodotti: [{"nome": "mela", "cat": "frutta"}, ...]
    
    # 2. Estrai solo le categorie
    # TODO: Usa una list comprehension per creare una lista di tutte le categorie
    categorie = [prodotto['cat'] for prodotto in dati]

    # 3. Conta le occorrenze di ogni categoria
    # TODO: Usa collections.Counter
    conteggio = 

    print("Analisi Inventario:")
    for cat, num in conteggio.items():
        print(f"- {cat}: {num} articoli")

    # 4. Trova la categoria più presente
    # TODO: Usa il metodo .most_common(1) di Counter
    piu_comune = 
    print(f"\nLa categoria dominante è: {piu_comune}")

# Esempio di avvio (crea un file inventario.json per testare!)
# analizza_inventario("inventario.json")

```

---

### **"Sfida Extra"** per ogni esercizio:

* **Per `os**`: Fai in modo che lo script sposti solo i file con estensione `.txt`.
* **Per `datetime**`: Calcola anche l'età esatta dell'utente in ore.
* **Per `json**`: Permetti all'utente di aggiungere un nuovo prodotto via input e salva il file aggiornato.

