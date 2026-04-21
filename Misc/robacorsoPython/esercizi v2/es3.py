"""
Autore: Federico Podio
Data: 20/03/2026
Titolo: Esercitazione PY 02
"""

#ES 3
# implementare una funzione convertiCF che converta una temperatura espressa in gradi Fahrenheit in una temperatura espressa in gradi Celsius.
# Usare la seguente formula: C = (F - 32) * 5 / 9

def convertiCF(fahrenheit):     # C = (F - 32) * 5 / 9
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Creare un programma principale che richiami la funzione e ne stampi il risultato visualizzando solo 3 cifre decimali.
t_fah = 66.6
t_cel = convertiCF(t_fah)

print(f"Temperatura base: {t_fah} °F")
print(f"Risultato Temperatura decimale: {t_cel:.3f} °C")