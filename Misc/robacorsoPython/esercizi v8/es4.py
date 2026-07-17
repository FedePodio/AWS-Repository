"""
Autore: Federico Podio
Data: 01/06/2026
Titolo: Esercitazione PY 05
"""
# Esercizi sui files
# ES 4

# Scrivere un programma che permetta di copiare il contenuto di un file in un altro file


# legge il contenuto del file
fr = open( 'percorso_file', 'r' ) # scritto percorso_file perchè non funzionerebbe una volta caricato sulla fad
contenuto_fr = fr.read()

# scrive il contenuto del primo file
fw = open( 'percorso_file_2', 'w' ) # come sopra ma percorso diverso
fw.write( contenuto_fr )