# 📘 Corso Python – Modulo 5

## Collezioni: liste, tuple, set e dizionari

---

### 1. Liste (`list`)

* Sequenza ordinata e modificabile di elementi.
* Definita con `[]`.

```python
frutta = ["mela", "banana", "pera"]
print(frutta[0])   # mela
print(frutta[-1])  # pera
```

#### Operazioni principali

```python
frutta.append("arancia")   # aggiunge
frutta.remove("banana")    # rimuove
print(len(frutta))         # lunghezza
print(frutta[1:3])         # slicing
frutta.sort()              # ordina
```

---

### 2. Tuple (`tuple`)

* Sequenza ordinata **immutabile**.
* Definita con `()`.

```python
coordinate = (10, 20)
print(coordinate[0])  # 10
```

⚠️ Non si possono modificare gli elementi.

---

### 3. Set (`set`)

* Collezione **non ordinata**, senza duplicati.
* Definita con `{}`.

```python
numeri = {1, 2, 3, 3, 4}
print(numeri)  # {1, 2, 3, 4}
```

#### Operazioni insiemistiche

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # unione {1, 2, 3, 4, 5}
print(a & b)  # intersezione {3}
print(a - b)  # differenza {1, 2}
```

---

### 4. Dizionari (`dict`)

* Collezione di coppie **chiave → valore**.
* Definito con `{}`.

```python
studente = {"nome": "Anna", "età": 21}
print(studente["nome"])   # Anna
```

#### Metodi principali

```python
studente["corso"] = "Informatica"  # aggiunta
print(studente.keys())    # tutte le chiavi
print(studente.values())  # tutti i valori
print(studente.items())   # coppie chiave-valore
```

---

### 5. Iterazione sulle collezioni

```python
lista = [1, 2, 3]
for x in lista:
    print(x)
```

```python
for chiave, valore in studente.items():
    print(chiave, ":", valore)
```

---

### 6. Differenze principali

| Tipo      | Ordinato | Modificabile | Duplicati     | Accesso |
| --------- | -------- | ------------ | ------------- | ------- |
| **list**  | ✅        | ✅            | ✅             | Indice  |
| **tuple** | ✅        | ❌            | ✅             | Indice  |
| **set**   | ❌        | ✅            | ❌             | No      |
| **dict**  | ✅        | ✅            | Chiavi uniche | Chiave  |


---

# 📘 Corso Python – Modulo 5: Collezioni (Versione Approfondita)

## 1. Liste (`list`) - La Collezione più Versatile

### 1.1 Introduzione e Creazione

Le liste sono sequenze ordinate e modificabili di elementi. Sono il tipo di collezione più utilizzato in Python per la loro flessibilità.

```python
# Diversi modi per creare liste
lista_vuota = []
lista_numeri = [1, 2, 3, 4, 5]
lista_mista = [1, "ciao", 3.14, True, None]
lista_annidata = [[1, 2], [3, 4], [5, 6]]

# Creazione con list()
lista_da_stringa = list("Python")  # ['P', 'y', 't', 'h', 'o', 'n']
lista_da_range = list(range(5))     # [0, 1, 2, 3, 4]

# List comprehension (creazione avanzata)
quadrati = [x**2 for x in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
pari = [x for x in range(20) if x % 2 == 0]  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

### 1.2 Accesso agli Elementi

```python
frutta = ["mela", "banana", "pera", "arancia", "kiwi"]

# Accesso con indici positivi
print(frutta[0])    # "mela" (primo elemento)
print(frutta[2])    # "pera"

# Accesso con indici negativi
print(frutta[-1])   # "kiwi" (ultimo elemento)
print(frutta[-2])   # "arancia" (penultimo)

# Verifica esistenza elemento
print("banana" in frutta)     # True
print("limone" in frutta)     # False

# Trovare indice di un elemento
indice = frutta.index("pera")  # 2
```

### 1.3 Slicing (Affettamento)

```python
numeri = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Sintassi: lista[inizio:fine:passo]
print(numeri[2:6])      # [2, 3, 4, 5] (dal 2° al 5°)
print(numeri[:4])       # [0, 1, 2, 3] (dall'inizio al 3°)
print(numeri[6:])       # [6, 7, 8, 9] (dal 6° alla fine)
print(numeri[:])        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (copia completa)

# Con passo
print(numeri[::2])      # [0, 2, 4, 6, 8] (elementi pari)
print(numeri[1::2])     # [1, 3, 5, 7, 9] (elementi dispari)
print(numeri[::-1])     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (lista invertita)
```

### 1.4 Modifica delle Liste

```python
animali = ["gatto", "cane", "pesce"]

# Modifica singoli elementi
animali[0] = "leone"  # ["leone", "cane", "pesce"]

# Modifica con slicing
animali[1:3] = ["tigre", "elefante", "giraffa"]
print(animali)  # ["leone", "tigre", "elefante", "giraffa"]

# Aggiunta elementi
animali.append("zebra")              # Aggiunge alla fine
animali.insert(1, "orso")            # Inserisce in posizione specifica
animali.extend(["lupo", "volpe"])    # Aggiunge più elementi

print(animali)  # ["leone", "orso", "tigre", "elefante", "giraffa", "zebra", "lupo", "volpe"]
```

### 1.5 Rimozione di Elementi

```python
colori = ["rosso", "verde", "blu", "giallo", "verde", "nero"]

# Diversi metodi di rimozione
elemento = colori.pop()        # Rimuove e restituisce l'ultimo: "nero"
elemento = colori.pop(0)       # Rimuove e restituisce il primo: "rosso"

colori.remove("verde")         # Rimuove la prima occorrenza di "verde"
del colori[1]                  # Rimuove elemento all'indice 1

# Rimozione di più elementi
del colori[1:3]               # Rimuove slice

colori.clear()                # Svuota completamente la lista
```

### 1.6 Metodi Avanzati per Liste

```python
numeri = [3, 1, 4, 1, 5, 9, 2, 6]

# Ordinamento
numeri_copia = numeri.copy()       # Crea una copia
numeri.sort()                      # Ordina in-place: [1, 1, 2, 3, 4, 5, 6, 9]
numeri.sort(reverse=True)          # Ordine decrescente: [9, 6, 5, 4, 3, 2, 1, 1]

# Ordinamento senza modificare l'originale
numeri_ordinati = sorted(numeri_copia)  # Originale non modificato

# Altre operazioni
numeri.reverse()                   # Inverte l'ordine
conteggio = numeri.count(1)        # Conta occorrenze di 1

# Operazioni con funzioni built-in
lunghezza = len(numeri)            # Lunghezza
somma = sum(numeri)                # Somma elementi
massimo = max(numeri)              # Elemento massimo
minimo = min(numeri)               # Elemento minimo

# Statistiche avanzate
import statistics
media = statistics.mean(numeri)
mediana = statistics.median(numeri)
```

### 1.7 Liste Multidimensionali

```python
# Matrice 3x3
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accesso agli elementi
print(matrice[0][1])  # 2 (riga 0, colonna 1)
print(matrice[2][2])  # 9 (riga 2, colonna 2)

# Iterazione su matrice
for riga in matrice:
    for elemento in riga:
        print(elemento, end=" ")
    print()  # Nuova riga

# List comprehension per matrici
matrice_quadrati = [[x**2 for x in riga] for riga in matrice]
print(matrice_quadrati)  # [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
```

---

## 2. Tuple (`tuple`) - Immutabili e Affidabili

### 2.1 Creazione e Caratteristiche

```python
# Diversi modi per creare tuple
tupla_vuota = ()
tupla_singola = (42,)          # Nota la virgola!
tupla_numeri = (1, 2, 3, 4, 5)
tupla_mista = (1, "ciao", 3.14, True)

# Creazione senza parentesi (tuple packing)
coordinate = 10, 20, 30
print(type(coordinate))  # <class 'tuple'>

# Creazione con tuple()
tupla_da_lista = tuple([1, 2, 3, 4])
tupla_da_stringa = tuple("Python")  # ('P', 'y', 't', 'h', 'o', 'n')
```

### 2.2 Accesso e Operazioni Base

```python
point = (10, 20, 30)

# Accesso con indici (come le liste)
print(point[0])   # 10
print(point[-1])  # 30

# Slicing
print(point[1:3])  # (20, 30)

# Metodi disponibili
print(point.count(10))  # 1 (numero di occorrenze)
print(point.index(20))  # 1 (indice dell'elemento)

# Operazioni di concatenazione e ripetizione
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_combinata = tupla1 + tupla2  # (1, 2, 3, 4, 5, 6)
tupla_ripetuta = tupla1 * 3        # (1, 2, 3, 1, 2, 3, 1, 2, 3)
```

### 2.3 Tuple Unpacking (Scompattamento)

```python
# Assegnazione multipla
punto = (100, 200)
x, y = punto  # x=100, y=200

# Scambio di variabili
a, b = 1, 2
a, b = b, a  # Ora a=2, b=1

# Unpacking con asterisco
numeri = (1, 2, 3, 4, 5, 6)
primo, secondo, *resto = numeri
print(primo)    # 1
print(secondo)  # 2
print(resto)    # [3, 4, 5, 6]

# Uso nei cicli
studenti_voti = [("Mario", 85), ("Anna", 92), ("Luigi", 78)]
for nome, voto in studenti_voti:
    print(f"{nome}: {voto}")
```

### 2.4 Named Tuples (Tuple Nominate)

```python
from collections import namedtuple

# Definizione di una named tuple
Persona = namedtuple('Persona', ['nome', 'età', 'città'])
Punto = namedtuple('Punto', 'x y z')  # Alternativa con stringa

# Creazione istanze
p1 = Persona("Marco", 30, "Roma")
punto3d = Punto(10, 20, 30)

# Accesso tramite nome o indice
print(p1.nome)     # "Marco"
print(p1[0])       # "Marco"
print(punto3d.x)   # 10

# Named tuple sono immutabili come le tuple normali
# p1.età = 31  # Errore!

# Metodi utili delle named tuple
print(p1._asdict())  # Converte in dizionario
nuovo_punto = punto3d._replace(z=100)  # Crea nuova istanza con modifiche
```

### 2.5 Casi d'Uso delle Tuple

```python
# 1. Coordinate e punti
def calcola_distanza(p1, p2):
    """Calcola distanza tra due punti 2D"""
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

punto_a = (0, 0)
punto_b = (3, 4)
distanza = calcola_distanza(punto_a, punto_b)  # 5.0

# 2. Restituzione multipla da funzioni
def statistiche_lista(numeri):
    """Restituisce min, max, media"""
    return min(numeri), max(numeri), sum(numeri)/len(numeri)

dati = [1, 2, 3, 4, 5, 6, 7, 8, 9]
minimo, massimo, media = statistiche_lista(dati)

# 3. Chiavi di dizionari (le tuple sono hashable)
mappa_scacchiera = {
    (0, 0): "Torre",
    (0, 7): "Torre", 
    (4, 4): "Re"
}
```

---

## 3. Set (`set`) - Collezioni Uniche

### 3.1 Creazione e Caratteristiche Base

```python
# Diversi modi per creare set
set_vuoto = set()  # Non {} che crea un dizionario vuoto!
set_numeri = {1, 2, 3, 4, 5}
set_lettere = set("python")  # {'p', 'y', 't', 'h', 'o', 'n'}

# I duplicati vengono automaticamente rimossi
numeri_con_duplicati = {1, 2, 2, 3, 3, 3, 4}
print(numeri_con_duplicati)  # {1, 2, 3, 4}

# Creazione da altre collezioni
lista_con_duplicati = [1, 1, 2, 3, 3, 4, 4, 4]
set_unico = set(lista_con_duplicati)  # {1, 2, 3, 4}
```

### 3.2 Operazioni sui Set

```python
colori_primari = {"rosso", "verde", "blu"}
colori_secondari = {"giallo", "magenta", "ciano"}
colori_caldi = {"rosso", "giallo", "arancione"}

# Aggiunta e rimozione elementi
colori_primari.add("giallo")         # Aggiunge un elemento
colori_primari.update(["nero", "bianco"])  # Aggiunge più elementi

colori_primari.remove("verde")       # Rimuove (errore se non presente)
colori_primari.discard("viola")      # Rimuove (nessun errore se non presente)
elemento = colori_primari.pop()      # Rimuove e restituisce elemento casuale

# Controllo appartenenza
print("rosso" in colori_primari)     # True
print("viola" in colori_primari)     # False

# Lunghezza
print(len(colori_primari))           # Numero di elementi
```

### 3.3 Operazioni Insiemistiche

```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
c = {1, 2, 3}

# Unione (elementi in a O b)
unione1 = a | b                    # {1, 2, 3, 4, 5, 6, 7, 8}
unione2 = a.union(b)               # Stesso risultato

# Intersezione (elementi in a E b)
intersezione1 = a & b              # {4, 5}
intersezione2 = a.intersection(b)  # Stesso risultato

# Differenza (elementi in a ma NON in b)
differenza1 = a - b                # {1, 2, 3}
differenza2 = a.difference(b)      # Stesso risultato

# Differenza simmetrica (elementi in a O b ma NON in entrambi)
diff_simm1 = a ^ b                           # {1, 2, 3, 6, 7, 8}
diff_simm2 = a.symmetric_difference(b)       # Stesso risultato

# Test di relazioni tra set
print(c.issubset(a))      # True (c è sottoinsieme di a)
print(a.issuperset(c))    # True (a è sovrainsieme di c)
print(a.isdisjoint(b))    # False (hanno elementi in comune)
```

### 3.4 Operazioni Avanzate sui Set

```python
# Set comprehension
quadrati = {x**2 for x in range(10)}  # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
vocali = {char.lower() for char in "Hello World" if char.lower() in "aeiou"}

# Operazioni di aggiornamento in-place
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1 |= set2   # Equivale a set1 = set1 | set2  -> {1, 2, 3, 4, 5}
set1 &= {1, 2, 3}  # Intersezione in-place -> {1, 2, 3}
set1 -= {3}    # Differenza in-place -> {1, 2}

# Frozen set (set immutabile)
frozen = frozenset([1, 2, 3, 4])
# frozen.add(5)  # Errore! È immutabile
print(type(frozen))  # <class 'frozenset'>
```

### 3.5 Casi d'Uso Pratici dei Set

```python
# 1. Rimozione duplicati
def rimuovi_duplicati(lista):
    return list(set(lista))

numeri = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unici = rimuovi_duplicati(numeri)  # [1, 2, 3, 4]

# 2. Verifica permessi utente
permessi_admin = {"read", "write", "delete", "execute"}
permessi_user = {"read", "write"}
permessi_guest = {"read"}

def ha_permesso(utente, azione, permessi):
    return azione in permessi[utente]

utenti_permessi = {
    "admin": permessi_admin,
    "user": permessi_user,
    "guest": permessi_guest
}

# 3. Analisi testi
def parole_comuni(testo1, testo2):
    """Trova parole comuni tra due testi"""
    parole1 = set(testo1.lower().split())
    parole2 = set(testo2.lower().split())
    return parole1 & parole2

testo_a = "Python è un linguaggio di programmazione"
testo_b = "Java è anche un linguaggio di programmazione"
comuni = parole_comuni(testo_a, testo_b)  # {'è', 'un', 'linguaggio', 'di', 'programmazione'}
```

---

## 4. Dizionari (`dict`) - Mappature Chiave-Valore

### 4.1 Creazione e Accesso Base

```python
# Diversi modi per creare dizionari
dizionario_vuoto = {}
dizionario_vuoto2 = dict()

studente = {
    "nome": "Anna",
    "età": 21,
    "corso": "Informatica",
    "voti": [28, 30, 27, 29]
}

# Creazione con dict()
persona = dict(nome="Mario", età=30, città="Roma")

# Creazione da liste di coppie
coppie = [("a", 1), ("b", 2), ("c", 3)]
dizionario_da_coppie = dict(coppie)  # {"a": 1, "b": 2, "c": 3}

# Accesso agli elementi
print(studente["nome"])          # "Anna"
print(studente.get("nome"))      # "Anna"
print(studente.get("telefono", "Non presente"))  # "Non presente" (valore predefinito)
```

### 4.2 Modifica e Aggiornamento

```python
profilo = {"nome": "Luigi", "età": 25}

# Aggiunta/modifica elementi
profilo["città"] = "Milano"      # Aggiunge nuova chiave
profilo["età"] = 26              # Modifica valore esistente

# Aggiornamento multiplo
profilo.update({
    "professione": "Ingegnere",
    "hobbies": ["lettura", "cinema"]
})

# Aggiornamento con dizionario o parole chiave
profilo.update(salario=50000, esperienza=3)

print(profilo)
# {"nome": "Luigi", "età": 26, "città": "Milano", "professione": "Ingegnere", 
#  "hobbies": ["lettura", "cinema"], "salario": 50000, "esperienza": 3}
```

### 4.3 Rimozione di Elementi

```python
dati = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

# Diversi metodi di rimozione
valore = dati.pop("b")           # Rimuove e restituisce valore di "b"
valore = dati.pop("z", "Non presente")  # Con valore predefinito

elemento = dati.popitem()        # Rimuove e restituisce coppia casuale
del dati["c"]                    # Rimuove chiave "c"

# Rimozione condizionale
chiave_da_rimuovere = "d" if "d" in dati else None
if chiave_da_rimuovere:
    del dati[chiave_da_rimuovere]

dati.clear()                     # Svuota completamente il dizionario
```

### 4.4 Metodi di Accesso e Iterazione

```python
menu = {
    "pizza": 12.50,
    "pasta": 10.00,
    "insalata": 8.50,
    "dolce": 6.00
}

# Metodi di accesso
chiavi = menu.keys()             # dict_keys(['pizza', 'pasta', 'insalata', 'dolce'])
valori = menu.values()           # dict_values([12.5, 10.0, 8.5, 6.0])
elementi = menu.items()          # dict_items([('pizza', 12.5), ...])

# Conversione a liste
lista_chiavi = list(menu.keys())
lista_valori = list(menu.values())

# Iterazione
for piatto in menu:              # Itera sulle chiavi
    print(piatto)

for piatto, prezzo in menu.items():  # Itera su coppie chiave-valore
    print(f"{piatto}: €{prezzo}")

for prezzo in menu.values():     # Itera sui valori
    print(f"€{prezzo}")

# Controllo esistenza
print("pizza" in menu)          # True (verifica chiave)
print(12.50 in menu.values())   # True (verifica valore)
```

### 4.5 Dictionary Comprehension

```python
# Creazione dizionari con comprehension
quadrati = {x: x**2 for x in range(1, 6)}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Con condizioni
pari_quadrati = {x: x**2 for x in range(10) if x % 2 == 0}

# Da liste esistenti
nomi = ["Anna", "Mario", "Luigi"]
età = [25, 30, 35]
persone = {nome: età for nome, età in zip(nomi, età)}

# Trasformazione dizionari esistenti
prezzi_euro = {"pane": 2.50, "latte": 1.20, "uova": 3.00}
prezzi_dollaro = {prodotto: prezzo * 1.1 for prodotto, prezzo in prezzi_euro.items()}

# Filtraggio
prodotti_costosi = {k: v for k, v in prezzi_euro.items() if v > 2.00}
```

### 4.6 Dizionari Nidificati e Complessi

```python
# Dizionario di dizionari
azienda = {
    "dipendenti": {
        "001": {"nome": "Anna", "reparto": "IT", "salario": 50000},
        "002": {"nome": "Mario", "reparto": "Vendite", "salario": 45000},
        "003": {"nome": "Luigi", "reparto": "IT", "salario": 55000}
    },
    "reparti": {
        "IT": {"budget": 200000, "manager": "001"},
        "Vendite": {"budget": 150000, "manager": "002"}
    }
}

# Accesso a dati nidificati
nome_dipendente = azienda["dipendenti"]["001"]["nome"]  # "Anna"
budget_it = azienda["reparti"]["IT"]["budget"]          # 200000

# Accesso sicuro con get()
salario = azienda.get("dipendenti", {}).get("004", {}).get("salario", 0)

# Modifica di strutture nidificate
azienda["dipendenti"]["001"]["salario"] = 52000

# Aggiunta nuovo dipendente
azienda["dipendenti"]["004"] = {
    "nome": "Sara", 
    "reparto": "HR", 
    "salario": 48000
}
```

### 4.7 Metodi Avanzati per Dizionari

```python
# setdefault() - imposta valore se chiave non esiste
contatori = {}
parole = ["mela", "banana", "mela", "pera", "banana", "mela"]

for parola in parole:
    contatori.setdefault(parola, 0)
    contatori[parola] += 1

print(contatori)  # {"mela": 3, "banana": 2, "pera": 1}

# defaultdict per valori predefiniti automatici
from collections import defaultdict

# Raggruppa studenti per voto
studenti_voti = [("Anna", "A"), ("Mario", "B"), ("Luigi", "A"), ("Sara", "B"), ("Paolo", "A")]
gruppi = defaultdict(list)

for nome, voto in studenti_voti:
    gruppi[voto].append(nome)

print(dict(gruppi))  # {"A": ["Anna", "Luigi", "Paolo"], "B": ["Mario", "Sara"]}

# Counter per conteggi automatici
from collections import Counter
testo = "hello world"
conteggio_lettere = Counter(testo)
print(conteggio_lettere)  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
```

---

## 5. Iterazione Avanzata sulle Collezioni

### 5.1 Enumerate e Zip

```python
# enumerate() - ottiene indice e valore
frutta = ["mela", "banana", "pera"]

for i, frutto in enumerate(frutta):
    print(f"{i}: {frutto}")

# enumerate con start personalizzato
for numero, frutto in enumerate(frutta, start=1):
    print(f"{numero}. {frutto}")

# zip() - combina più collezioni
nomi = ["Anna", "Mario", "Luigi"]
voti = [85, 92, 78]
materie = ["Math", "Science", "History"]

for nome, voto, materia in zip(nomi, voti, materie):
    print(f"{nome} ha preso {voto} in {materia}")

# zip per creare dizionari
studenti = dict(zip(nomi, voti))  # {"Anna": 85, "Mario": 92, "Luigi": 78}
```

### 5.2 Itertools per Iterazioni Complesse

```python
import itertools

# product - prodotto cartesiano
colori = ["rosso", "verde"]
taglie = ["S", "M", "L"]
varianti = list(itertools.product(colori, taglie))
# [('rosso', 'S'), ('rosso', 'M'), ('rosso', 'L'), ('verde', 'S'), ('verde', 'M'), ('verde', 'L')]

# combinations - combinazioni senza ripetizione
numeri = [1, 2, 3, 4]
coppie = list(itertools.combinations(numeri, 2))
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

# permutations - permutazioni
lettere = ["A", "B", "C"]
permutazioni = list(itertools.permutations(lettere, 2))
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# chain - concatena iteratori
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
concatenata = list(itertools.chain(lista1, lista2))  # [1, 2, 3, 4, 5, 6]

# groupby - raggruppa elementi consecutivi
from itertools import groupby
dati = [("A", 1), ("A", 2), ("B", 3), ("B", 4), ("A", 5)]
for chiave, gruppo in groupby(dati, key=lambda x: x[0]):
    print(f"{chiave}: {list(gruppo)}")
```

---

## 6. Confronto Dettagliato delle Collezioni

### 6.1 Tabella delle Caratteristiche

| Caratteristica    | List           | Tuple          | Set            | Dict           |
|------------------|----------------|----------------|----------------|----------------|
| **Ordinato**     | ✅ (mantiene)   | ✅ (mantiene)   | ❌ (no ordine) | ✅ (da Python 3.7+) |
| **Modificabile** | ✅ (mutabile)   | ❌ (immutabile) | ✅ (mutabile)   | ✅ (mutabile)   |
| **Duplicati**    | ✅ (permessi)   | ✅ (permessi)   | ❌ (unici)      | ❌ (chiavi uniche) |
| **Accesso**      | Per indice     | Per indice     | Nessuno        | Per chiave     |
| **Sintassi**     | `[1, 2, 3]`    | `(1, 2, 3)`    | `{1, 2, 3}`    | `{"a": 1}`     |
| **Hashable**     | ❌             | ✅             | ❌ (elementi sì) | ❌ (chiavi sì)  |

### 6.2 Performance e Uso della Memoria

```python
import sys
import time

# Confronto uso memoria
lista = [i for i in range(1000)]
tupla = tuple(i for i in range(1000))
insieme = {i for i in range(1000)}
dizionario = {i: i for i in range(1000)}

print(f"Lista: {sys.getsizeof(lista)} bytes")
print(f"Tupla: {sys.getsizeof(tupla)} bytes")
print(f"Set: {sys.getsizeof(insieme)} bytes")
print(f"Dizionario: {sys.getsizeof(dizionario)} bytes")

# Confronto performance di ricerca
def test_ricerca(collezione, elemento):
    start = time.time()
    for _ in range(100000):
        elemento in collezione
    return time.time() - start

# Ricerca elemento in mezzo
elemento_test = 500

lista_time = test_ricerca(lista, elemento_test)
tupla_time = test_ricerca(tupla, elemento_test)
set_time = test_ricerca(insieme, elemento_test)
dict_time = test_ricerca(list(dizionario.keys()), elemento_test)

print(f"Tempo ricerca - Lista: {lista_time:.6f}s")
print(f"Tempo ricerca - Tupla: {tupla_time:.6f}s")
print(f"Tempo ricerca - Set: {set_time:.6f}s")
print(f"Tempo ricerca - Dict keys: {dict_time:.6f}s")
```

### 6.3 Quando Usare Ogni Collezione

```python
# 🟢 LISTE - Usa quando:
# - Hai bisogno di ordine
# - Elementi possono essere duplicati
# - Devi accedere per indice
# - Collezione cambia frequentemente di dimensione

carrello_spesa = ["pane", "latte", "uova", "pane"]  # Duplicati OK
carrello_spesa.append("burro")  # Modifica frequente
primo_articolo = carrello_spesa[0]  # Accesso per indice

# 🟡 TUPLE - Usa quando:
# - Dati non cambiano (immutabili)
# - Rappresenti coordinate, punti, record fissi
# - Chiavi di dizionari
# - Return multipli da funzioni

coordinate_gps = (45.4642, 9.1900)  # Milano - non cambiano
posizioni_gioco = {(0, 0): "vuoto", (1, 1): "X", (2, 2): "O"}

def info_utente():
    return "Mario", 30, "Ingegnere"  # Return multipli

# 🔵 SET - Usa quando:
# - Elementi devono essere unici
# - Operazioni insiemistiche (unione, intersezione)
# - Controllo veloce di appartenenza
# - Rimozione duplicati

utenti_attivi = {"mario", "anna", "luigi"}
utenti_premium = {"anna", "sara", "paolo"}
utenti_premium_attivi = utenti_attivi & utenti_premium  # Intersezione

# 🟠 DIZIONARI - Usa quando:
# - Associazioni chiave-valore
# - Lookup veloce per chiave
# - Strutture dati complesse
# - Cache e mappature

cache_risultati = {}  # Cache
profilo_utente = {"id": 123, "nome": "Anna", "email": "anna@email.com"}
configurazione = {"debug": True, "timeout": 30, "retries": 3}
```

---

## 7. Tecniche Avanzate e Patterns Comuni

### 7.1 Trasformazioni tra Collezioni

```python
# Lista → Altri tipi
numeri_lista = [1, 2, 2, 3, 3, 3, 4]

# Lista → Tupla
numeri_tupla = tuple(numeri_lista)

# Lista → Set (rimuove duplicati)
numeri_unici = set(numeri_lista)  # {1, 2, 3, 4}

# Lista → Dizionario (con enumerate)
indice_valore = dict(enumerate(numeri_lista))  # {0: 1, 1: 2, 2: 2, ...}

# Set → Lista (ordine casuale)
lista_da_set = list(numeri_unici)

# Dizionario → Liste
dati = {"a": 1, "b": 2, "c": 3}
chiavi_lista = list(dati.keys())      # ["a", "b", "c"]
valori_lista = list(dati.values())    # [1, 2, 3]
coppie_lista = list(dati.items())     # [("a", 1), ("b", 2), ("c", 3)]
```

### 7.2 Pattern di Aggregazione

```python
# Raggruppa elementi per caratteristica
from collections import defaultdict

studenti = [
    {"nome": "Anna", "classe": "A", "voto": 85},
    {"nome": "Mario", "classe": "B", "voto": 92},
    {"nome": "Luigi", "classe": "A", "voto": 78},
    {"nome": "Sara", "classe": "B", "voto": 88},
]

# Raggruppa per classe
per_classe = defaultdict(list)
for studente in studenti:
    per_classe[studente["classe"]].append(studente)

# Calcola statistiche per gruppo
statistiche = {}
for classe, gruppo in per_classe.items():
    voti = [s["voto"] for s in gruppo]
    statistiche[classe] = {
        "media": sum(voti) / len(voti),
        "massimo": max(voti),
        "minimo": min(voti),
        "count": len(voti)
    }

print(statistiche)
# {"A": {"media": 81.5, "massimo": 85, "minimo": 78, "count": 2}, ...}
```

### 7.3 Caching e Memoization

```python
# Cache con dizionario
cache_fibonacci = {}

def fibonacci(n):
    """Calcola n-esimo numero di Fibonacci con cache"""
    if n in cache_fibonacci:
        return cache_fibonacci[n]
    
    if n <= 1:
        result = n
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
    
    cache_fibonacci[n] = result
    return result

# Cache con decoratore
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci_decorato(n):
    """Fibonacci con cache automatico"""
    if n <= 1:
        return n
    return fibonacci_decorato(n-1) + fibonacci_decorato(n-2)

# Test performance
import time

start = time.time()
print(fibonacci(35))
print(f"Con cache: {time.time() - start:.4f}s")

start = time.time()
print(fibonacci_decorato(35))
print(f"Con @lru_cache: {time.time() - start:.4f}s")
```

### 7.4 Validazione e Pulizia Dati

```python
def pulisci_e_valida_dati(dati_grezzi):
    """
    Pulisce e valida una lista di dizionari rappresentanti persone
    """
    dati_puliti = []
    errori = []
    
    for i, persona in enumerate(dati_grezzi):
        try:
            # Validazione campi obbligatori
            if not persona.get("nome") or not persona.get("email"):
                errori.append(f"Riga {i}: nome o email mancante")
                continue
            
            # Pulizia dati
            persona_pulita = {
                "nome": persona["nome"].strip().title(),
                "email": persona["email"].strip().lower(),
                "età": int(persona.get("età", 0)),
                "città": persona.get("città", "").strip().title() or "Non specificata"
            }
            
            # Validazioni specifiche
            if "@" not in persona_pulita["email"]:
                errori.append(f"Riga {i}: email non valida")
                continue
            
            if persona_pulita["età"] < 0 or persona_pulita["età"] > 150:
                errori.append(f"Riga {i}: età non valida")
                continue
            
            dati_puliti.append(persona_pulita)
            
        except (ValueError, KeyError) as e:
            errori.append(f"Riga {i}: errore di formato - {e}")
    
    return dati_puliti, errori

# Esempio di utilizzo
dati_input = [
    {"nome": " mario rossi ", "email": "MARIO@EMAIL.COM", "età": "30", "città": "roma"},
    {"nome": "anna", "email": "invalid-email", "età": "25"},
    {"nome": "", "email": "test@test.com", "età": "200"},
    {"nome": "luigi bianchi", "email": "luigi@email.com", "età": "35", "città": "milano"}
]

dati_puliti, errori = pulisci_e_valida_dati(dati_input)
print(f"Dati validi: {len(dati_puliti)}")
print(f"Errori: {len(errori)}")
for errore in errori:
    print(f"❌ {errore}")
```

---

## 8. Collezioni Specializzate (collections module)

### 8.1 OrderedDict - Dizionari con Ordine Garantito

```python
from collections import OrderedDict

# Prima di Python 3.7, i dict normali non garantivano l'ordine
# OrderedDict è ancora utile per compatibilità e metodi speciali

menu = OrderedDict([
    ("antipasti", 8.50),
    ("primi", 12.00),
    ("secondi", 15.00),
    ("dolci", 6.00)
])

# Metodi speciali di OrderedDict
menu.move_to_end("antipasti")  # Sposta alla fine
ultimo = menu.popitem(last=True)   # Rimuove ultimo elemento
primo = menu.popitem(last=False)   # Rimuove primo elemento

print(menu)
```

### 8.2 ChainMap - Unione di Dizionari

```python
from collections import ChainMap

# Configurazioni con priorità
config_default = {"debug": False, "timeout": 30, "retries": 3}
config_user = {"timeout": 60, "host": "localhost"}
config_env = {"debug": True}

# ChainMap cerca nelle mappe in ordine
config = ChainMap(config_env, config_user, config_default)

print(config["debug"])    # True (da config_env)
print(config["timeout"]) # 60 (da config_user)
print(config["retries"]) # 3 (da config_default)

# Aggiunta nuova mappa con priorità massima
config_runtime = {"port": 8080}
config = config.new_child(config_runtime)
```

### 8.3 Deque - Double-ended Queue

```python
from collections import deque

# Deque è ottimizzata per inserimenti/rimozioni alle estremità
coda = deque(maxlen=5)  # Lunghezza massima 5

# Operazioni efficienti alle estremità
coda.append("primo")        # Aggiunge a destra
coda.appendleft("zero")     # Aggiunge a sinistra
coda.extend(["secondo", "terzo"])  # Aggiunge multipli a destra

print(coda)  # deque(['zero', 'primo', 'secondo', 'terzo'], maxlen=5)

# Rimozioni efficienti
ultimo = coda.pop()         # Rimuove da destra
primo = coda.popleft()      # Rimuove da sinistra

# Rotazione
coda.rotate(1)   # Sposta elementi a destra
coda.rotate(-1)  # Sposta elementi a sinistra

# Uso come buffer circolare
buffer = deque(maxlen=3)
for i in range(10):
    buffer.append(i)
    print(f"Buffer: {list(buffer)}")
# Mantiene sempre gli ultimi 3 elementi
```

---

## 9. Progetti Pratici Completi

### 9.1 Sistema di Gestione Biblioteca

```python
from collections import defaultdict, namedtuple
from datetime import datetime, timedelta

# Definizione strutture dati
Libro = namedtuple("Libro", ["isbn", "titolo", "autore", "genere", "anno"])
Utente = namedtuple("Utente", ["id", "nome", "email", "telefono"])

class Biblioteca:
    def __init__(self):
        # Collezioni per gestire i dati
        self.libri = {}  # isbn -> Libro
        self.utenti = {}  # id -> Utente
        self.prestiti = defaultdict(list)  # user_id -> [prestiti]
        self.disponibilità = defaultdict(int)  # isbn -> quantità
        self.storico = []  # Lista cronologica operazioni
        
        # Indici per ricerche veloci
        self.libri_per_autore = defaultdict(set)  # autore -> {isbn}
        self.libri_per_genere = defaultdict(set)  # genere -> {isbn}
    
    def aggiungi_libro(self, isbn, titolo, autore, genere, anno, quantità=1):
        """Aggiunge un libro al catalogo"""
        libro = Libro(isbn, titolo, autore, genere, anno)
        self.libri[isbn] = libro
        self.disponibilità[isbn] += quantità
        
        # Aggiorna indici
        self.libri_per_autore[autore].add(isbn)
        self.libri_per_genere[genere].add(isbn)
        
        # Storico
        self.storico.append({
            "data": datetime.now(),
            "operazione": "aggiunto_libro",
            "dettagli": {"isbn": isbn, "quantità": quantità}
        })
    
    def registra_utente(self, user_id, nome, email, telefono):
        """Registra un nuovo utente"""
        if user_id in self.utenti:
            raise ValueError(f"Utente {user_id} già esistente")
        
        utente = Utente(user_id, nome, email, telefono)
        self.utenti[user_id] = utente
        return utente
    
    def presta_libro(self, user_id, isbn):
        """Gestisce il prestito di un libro"""
        # Validazioni
        if user_id not in self.utenti:
            raise ValueError("Utente non registrato")
        
        if isbn not in self.libri:
            raise ValueError("Libro non presente nel catalogo")
        
        if self.disponibilità[isbn] <= 0:
            raise ValueError("Libro non disponibile")
        
        # Verifica prestiti attivi utente
        prestiti_attivi = [p for p in self.prestiti[user_id] 
                          if p.get("restituito") is None]
        if len(prestiti_attivi) >= 3:
            raise ValueError("Limite massimo prestiti raggiunto")
        
        # Crea prestito
        prestito = {
            "isbn": isbn,
            "data_prestito": datetime.now(),
            "data_scadenza": datetime.now() + timedelta(days=14),
            "restituito": None,
            "multa": 0
        }
        
        # Aggiorna stato
        self.prestiti[user_id].append(prestito)
        self.disponibilità[isbn] -= 1
        
        # Storico
        self.storico.append({
            "data": datetime.now(),
            "operazione": "prestito",
            "dettagli": {"user_id": user_id, "isbn": isbn}
        })
        
        return prestito
    
    def restituisci_libro(self, user_id, isbn):
        """Gestisce la restituzione di un libro"""
        # Trova prestito attivo
        prestiti_utente = self.prestiti[user_id]
        prestito = None
        
        for p in prestiti_utente:
            if p["isbn"] == isbn and p["restituito"] is None:
                prestito = p
                break
        
        if not prestito:
            raise ValueError("Prestito non trovato o già restituito")
        
        # Calcola multa se in ritardo
        data_restituzione = datetime.now()
        if data_restituzione > prestito["data_scadenza"]:
            giorni_ritardo = (data_restituzione - prestito["data_scadenza"]).days
            prestito["multa"] = giorni_ritardo * 0.50  # 50 cent al giorno
        
        # Aggiorna prestito
        prestito["restituito"] = data_restituzione
        self.disponibilità[isbn] += 1
        
        return prestito
    
    def cerca_libri(self, **criteri):
        """Cerca libri per diversi criteri"""
        risultati = set(self.libri.keys())  # Inizia con tutti i libri
        
        if "autore" in criteri:
            libri_autore = self.libri_per_autore.get(criteri["autore"], set())
            risultati &= libri_autore
        
        if "genere" in criteri:
            libri_genere = self.libri_per_genere.get(criteri["genere"], set())
            risultati &= libri_genere
        
        if "titolo" in criteri:
            titolo_ricerca = criteri["titolo"].lower()
            libri_titolo = {isbn for isbn, libro in self.libri.items() 
                           if titolo_ricerca in libro.titolo.lower()}
            risultati &= libri_titolo
        
        if "disponibile" in criteri and criteri["disponibile"]:
            libri_disponibili = {isbn for isbn, qta in self.disponibilità.items() 
                               if qta > 0}
            risultati &= libri_disponibili
        
        return [self.libri[isbn] for isbn in risultati]
    
    def rapporto_prestiti(self):
        """Genera statistiche sui prestiti"""
        stats = {
            "totale_prestiti": sum(len(prestiti) for prestiti in self.prestiti.values()),
            "prestiti_attivi": 0,
            "libri_più_prestati": defaultdict(int),
            "utenti_più_attivi": defaultdict(int),
            "multe_totali": 0
        }
        
        for user_id, prestiti in self.prestiti.items():
            stats["utenti_più_attivi"][user_id] = len(prestiti)
            
            for prestito in prestiti:
                stats["libri_più_prestati"][prestito["isbn"]] += 1
                stats["multe_totali"] += prestito["multa"]
                
                if prestito["restituito"] is None:
                    stats["prestiti_attivi"] += 1
        
        # Top 5 libri più prestati
        stats["top_libri"] = sorted(
            stats["libri_più_prestati"].items(), 
            key=lambda x: x[1], 
            reverse=True
        )[:5]
        
        return stats

# Esempio di utilizzo
biblioteca = Biblioteca()

# Aggiungi libri
biblioteca.aggiungi_libro("978-0-123456-78-9", "1984", "George Orwell", "Distopia", 1949, 3)
biblioteca.aggiungi_libro("978-0-987654-32-1", "Il Nome della Rosa", "Umberto Eco", "Storico", 1980, 2)
biblioteca.aggiungi_libro("978-0-111111-11-1", "Neuromante", "William Gibson", "Sci-Fi", 1984, 1)

# Registra utenti
biblioteca.registra_utente("user001", "Mario Rossi", "mario@email.com", "123-456-7890")
biblioteca.registra_utente("user002", "Anna Bianchi", "anna@email.com", "098-765-4321")

# Prestiti
biblioteca.presta_libro("user001", "978-0-123456-78-9")
biblioteca.presta_libro("user002", "978-0-987654-32-1")

# Ricerche
libri_distopia = biblioteca.cerca_libri(genere="Distopia")
libri_disponibili = biblioteca.cerca_libri(disponibile=True)

# Statistiche
stats = biblioteca.rapporto_prestiti()
print(f"Prestiti attivi: {stats['prestiti_attivi']}")
print(f"Libro più prestato: {stats['top_libri'][0] if stats['top_libri'] else 'Nessuno'}")
```
