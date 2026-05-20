"""
Autore: Federico Podio
Data: 15/04/2026
Titolo: Esercitazione PY 03
"""
# Esercizi sulle tuple
# ES 4

def conta_elementi_fino_a_tupla(lista):
    contatore = 0
    
    for elemento in lista:
        # Controllare se l'elemento è una tupla
        if isinstance(elemento, tuple):
            # Ferma il ciclo
            break  
        
        contatore += 1
    
    return contatore

mia_lista = [123, "ascsaad", 32312, (1, 2), "aaaa"]

risultato = conta_elementi_fino_a_tupla(mia_lista)

print(f"La lista era: {mia_lista}")
print(f"Numero di elementi prima della prima tupla: {risultato}")