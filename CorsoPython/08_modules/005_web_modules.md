# 🌐 SCHEDA DIDATTICA: Python & Il Web

**Obiettivo:** Imparare come Python interagisce con Internet, scarica dati e comunica con i browser.

---

## 1. La Teoria: Come "parlano" i computer?

Quando scrivi un indirizzo nel browser, avviene uno scambio chiamato **Modello Client-Server**:

1. **Client (Tu):** Chiede una pagina (Invia una **Request**).
2. **Server (Il sito):** Risponde inviando i dati (Invia una **Response**).

### I Codici di Stato

Il server ti risponde sempre con un numero. I più comuni sono:

* **200**: "Tutto ok, ecco i tuoi dati!"
* **404**: "Pagina non trovata."
* **500**: "Il server ha un problema tecnico."

---

## 2. Modulo `webbrowser`: Controllare il Browser

Questo modulo è il più semplice: serve ad aprire pagine web direttamente dal tuo script.

**Metodo principale:**

* `webbrowser.open("url")`: Apre l'indirizzo indicato nel browser predefinito.

> **Esempio Pratico:**
>
> ```python
> import webbrowser
> webbrowser.open("https://www.python.org")
> 
> ```
>
>

---

## 3. Modulo `urllib.request`: Scaricare dati

Questo modulo permette a Python di comportarsi come un browser: si collega a un sito e ne "legge" il contenuto.

**I passaggi fondamentali:**

1. **Apertura:** Si usa `urlopen(url)`.
2. **Lettura:** Il contenuto arriva in formato **Bytes** (linguaggio macchina).
3. **Decodifica:** Bisogna trasformare i Bytes in **Stringhe** usando `.decode("utf-8")`.

**Esempio di codice:**

```python
import urllib.request

with urllib.request.urlopen("http://www.google.com") as risposta:
    corpo_pagine_bytes = risposta.read()
    testo_finale = corpo_pagine_bytes.decode("utf-8")

```

---

## 4. Modulo `urllib.parse`: Pulizia degli URL

Gli URL non possono contenere spazi o caratteri speciali. Se vuoi inviare un messaggio tramite URL, devi "codificarlo".

**Metodo principale:**

* `quote("testo")`: Trasforma gli spazi in `%20` e i caratteri speciali in codici leggibili dai server.

> **Esempio:**
> `quote("Ciao a tutti!")` diventa `Ciao%20a%20tutti%21`

---

## 5. Gestione degli Errori (Try/Except)

A volte il sito è irraggiungibile o l'URL è sbagliato. Per evitare che il programma si blocchi, usiamo `urllib.error`.

```python
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

try:
    risposta = urlopen("https://sito-che-non-esiste.it")
except HTTPError as e:
    print(f"Errore del server: {e.code}")
except URLError as e:
    print(f"Impossibile raggiungere il server: {e.reason}")

```

---

## 🛠️ Laboratorio Pratico: "Il Mini-Browser"

**Compila le parti mancanti (TODO) nello script seguente:**

```python
import urllib.request
import urllib.parse
import webbrowser

def mini_strumento_web():
    print("1. Apri sito | 2. Leggi Sorgente | 3. Codifica Messaggio")
    scelta = input("Cosa vuoi fare? ")

    if scelta == "1":
        url = input("Inserisci l'URL (es. https://google.it): ")
        # TODO: Usa il metodo corretto per aprire l'URL nel browser
        
    elif scelta == "2":
        url = input("Inserisci l'URL da leggere: ")
        # TODO: Usa urlopen() per scaricare la pagina e decode() per stamparla
        
    elif scelta == "3":
        messaggio = input("Scrivi una frase con spazi: ")
        # TODO: Usa quote() per trasformare la frase in formato URL
        print(f"Versione codificata: ...")

mini_strumento_web()

```

---

### 💡 Pro-Tip

Sapevi che puoi creare un server web istantaneo?
Apri il terminale in una cartella con file HTML e scrivi:
`python -m http.server 8000`
Poi vai su `http://localhost:8000` nel tuo browser. Complimenti, sei diventato un **Server**!

---

**Cosa puoi fare ora?**
Dopo aver completato questa scheda, prova a risolvere gli esercizi di "Cacciatore di Email" o "Costruttore di Link" che abbiamo visto prima.

Ti piacerebbe che aggiungessi una **sezione di quiz a risposta multipla** per verificare la comprensione dei concetti?

Per scrivere schede didattiche sul web, è importante distinguere tra ciò che Python fa "dietro le quinte" (richieste dati) e ciò che l'utente vede (pagine nel browser).

Ecco i moduli built-in più adatti a un livello scolastico/introduttivo, evitando librerie esterne pesanti come *Requests* o *Flask*.

---

## 8. Modulo `webbrowser`: Il ponte con il Browser

Questo è il modulo più semplice in assoluto. Non scarica dati, ma permette al codice di controllare il browser dell'utente. È perfetto per i principianti assoluti.

* **Concetto chiave:** Automazione della navigazione.
* **Metodo principale:** `webbrowser.open(url)`.

### 💡 Esercizio: "Il Cercatore Automatico"

```python
import webbrowser

def ricerca_veloce():
    # 1. Chiedi all'utente cosa vuole cercare
    argomento = input("Cosa vuoi cercare oggi su Wikipedia? ")
    
    # 2. Costruisci l'URL di ricerca
    url = f"https://it.wikipedia.org/wiki/{argomento}"
    
    print(f"Apertura di {url} in corso...")
    
    # 3. Apri il browser
    # TODO: Usa webbrowser.open()
    
# Sfida: Crea un menu che permetta di scegliere se cercare su Google, YouTube o Wikipedia.

```

---

## 9. Modulo `urllib.request`: Scaricare Dati dal Web

Questo modulo è il motore che permette a Python di "leggere" il contenuto di una pagina web o di un'API come se fosse un file locale.

* **Concetto chiave:** La richiesta HTTP (Request) e la risposta del server (Response).
* **Metodo principale:** `urllib.request.urlopen(url)`.

### 💡 Esercizio: "Il Lettore di Codice Sorgente"

```python
import urllib.request

def scarica_pagina(url):
    print(f"Connessione a {url}...")
    
    # 1. Apri l'URL
    # TODO: Usa urllib.request.urlopen() e assegna a una variabile 'risposta'
    with urllib.request.urlopen(url) as risposta:
        
        # 2. Leggi il contenuto (che arriva in formato 'bytes')
        contenuto_raw = risposta.read()
        
        # 3. Converti i bytes in testo leggibile (stringa)
        # TODO: Usa il metodo .decode("utf-8")
        testo = 
        
        print("--- Inizio Contenuto HTML ---")
        print(testo[:500]) # Stampiamo solo i primi 500 caratteri
        print("--- Fine Anteprima ---")

# Prova con: scarica_pagina("https://www.google.it")

```

---

## 10. Modulo `urllib.parse`: Gestire gli URL

Spesso gli URL contengono spazi o caratteri speciali (come `@` o `?`) che il web non capisce bene. Questo modulo "pulisce" gli URL.

* **Concetto chiave:** URL Encoding (es. lo spazio diventa `%20`).

### 💡 Esercizio: "Il Costruttore di Link Sicuri"

```python
from urllib.parse import quote

def crea_link_whatsapp():
    numero = "3912345678"
    messaggio = "Ciao! Ho appena finito la mia scheda didattica su Python 🐍"
    
    # 1. Gli spazi e le emoji nel messaggio vanno "codificati" per il web
    # TODO: Usa quote(messaggio)
    messaggio_codificato = 
    
    # 2. Unisci tutto nell'URL finale
    link_finale = f"https://wa.me/{numero}?text={messaggio_codificato}"
    
    print(f"Il tuo link pronto da inviare è:\n{link_finale}")

# Sfida: Usa il modulo 'webbrowser' per aprire il link appena creato!

```

---

## 11. Modulo `http.server`: Creare un Server Locale

Questo è il "colpo di scena" per gli studenti. Python può trasformare il computer in un server web con una sola riga di comando. Non serve scrivere codice complesso, si usa dal terminale.

* **Istruzione didattica:**

1. Apri il terminale nella cartella dove hai i tuoi file HTML.
2. Digita: `python -m http.server 8000`.
3. Apri il browser su `http://localhost:8000`.

* **Cosa imparano:** La differenza tra "Client" (il browser) e "Server" (il programma Python che distribuisce i file).

---

### Tabella dei Codici di Stato

Quando si lavora con il web, il modulo `urllib` può restituire degli errori (es. il famoso 404). È utile includere questa piccola legenda per gli studenti:

| Codice | Significato | Messaggio tipico |
| --- | --- | --- |
| **200** | OK | Tutto ha funzionato! |
| **404** | Not Found | La pagina non esiste. |
| **403** | Forbidden | Non hai il permesso di entrare. |
| **500** | Server Error | Il sito ha un problema tecnico. |

