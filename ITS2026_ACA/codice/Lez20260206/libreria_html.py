
# libri = [
#     ['L\'uomo ragno', 120, 15, 2],   # \' per usarlo come punteggiatura in print
#     ['La donna ragno ragno', 150, 25, 2],
#     ['Il bambino ragno', 220, 35, 2],
#     ['L\'insetto verde', 80, 10, 1],
#     ['L\'opossum grigio', 320, 45, 1]
# ]

libri =[]

source = open("ITS2026_ACA\database\libri.csv", 'r')

for riga in source:
    riga_splittata = riga.split(",")
    titolo = (riga_splittata[0].replace('"', ''))
    pagine = int(riga_splittata[2].replace('"', ''))
    prezzo = float(riga_splittata[4].replace('"', ''))
    print(f"il libro {titolo} ha {pagine} pagine e costa $ {prezzo}")
    #trovare una stragtegia per l'editore
    #aggiungiamo i dati di ciascun libro alla lista di libri
    libri.append([titolo, pagine, prezzo, 1])

source.close()





f = open("ITS2026_ACA\database\insert_libri.sql", "w")

f.write("<table>")
# f.write("<tr><th>pagine<")
for libro in libri:
    f.write("<tr>")
    titolo = str(libro[0]).replace("'","\'")
    #etc
    f.write("<tr>")
    pagine = libro[1]

    f.write("<tr>")
    prezzo = libro[2]
    
    editore_id = libro[3]
    f.write(f"INSERT INTO libri SET titolo = '{titolo}', pagine = {pagine}, prezzo = {pagine}, editore_id = {editore_id}';\n")


f.write("</table>")
f.close()

print('GAME OVER - tutto liscio - TOP!')