# 🧩 **Functions**

Le funzioni in Python permettono di organizzare il codice in blocchi riutilizzabili, rendendolo più chiaro, modulare ed efficiente.

---

## 📘 **Defining Functions**

Le funzioni si definiscono con la parola chiave `def`, un nome descrittivo e un blocco di istruzioni da eseguire quando la funzione viene chiamata.

**Punti chiave**

* Sintassi: `def function_name():`
* Il codice rientrato forma il corpo della funzione
* La funzione viene eseguita solo quando chiamata

---

## 📘 **Arguments**

Gli *argomenti* permettono di passare dati alla funzione, rendendola flessibile e personalizzabile.

**Punti chiave**

* Si definiscono tra parentesi dopo il nome della funzione
* Sono variabili disponibili dentro la funzione
* Ordine e numero degli argomenti devono essere rispettati

---

## 📘 **Types of Functions**

Python supporta vari tipi di funzioni per differenti scenari.

**Esempi**

* Funzioni senza argomenti né valore di ritorno
* Funzioni con argomenti
* Funzioni che ritornano valori
* Funzioni che elaborano e modificano dati

---

## 📘 **Keyword Arguments**

Gli argomenti possono essere passati specificando il *nome* invece della posizione.

**Punti chiave**

* Consentono ordine arbitrario degli argomenti
* Migliorano leggibilità e chiarezza
* Esempio: `greet(name="Alex")`

---

## 📘 **Default Arguments**

Gli argomenti possono avere valori predefiniti da usare se non forniti nella chiamata.

**Punti chiave**

* Sintassi: `def func(a, b=10):`
* Evitano errori quando un parametro non viene passato
* Ideali per comportamenti predefiniti

---

## 📘 ***args**

Permette di passare un numero variabile di argomenti *posizionali*.

**Punti chiave**

* Si scrive `*args`
* Si ottiene una tupla contenente tutti gli argomenti extra
* Utile quando il numero di parametri non è noto

---

## 📘 ****kwargs**

Permette di passare un numero variabile di argomenti *keyword*.

**Punti chiave**

* Si scrive `**kwargs`
* Produce un dizionario con chiave=valore
* Ideale per opzioni variabili o configurazioni

---

## 📘 **Scope**

Lo *scope* definisce dove una variabile è accessibile nel programma.

**Punti chiave**

* Variabili locali: esistono solo nella funzione
* Variabili globali: definite fuori da ogni funzione
* Regola LEGB: Local → Enclosing → Global → Built-in

---

## 📘 **Debugging**

Tecniche per individuare errori e anomalie nell’esecuzione delle funzioni.

**Punti chiave**

* Uso di `print()` per tracciare valori
* Controllo degli argomenti
* Individuazione dei ritorni non corretti
* Gestione eccezioni per prevenire crash

---

## 📘 **Exercise**

Crea una funzione che:

1. Accetta una lista di prezzi e una percentuale di sconto
2. Applica lo sconto a ogni prezzo
3. Restituisce una nuova lista con i prezzi aggiornati

---

## 📘 **Solution**

```python
def apply_discount(prices, discount):
    updated = []
    for price in prices:
        updated.append(price - price * discount)
    return updated

# Example
print(apply_discount([10, 20, 30], 0.1))
```
