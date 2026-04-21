studenti = []

f = open('./studenti.txt')  #aggiungi cd + percorso file adatto

for riga in f:
    # print(riga)
    #per ogni riga del file aggiungo la riga alla lista studenti
    riga = riga.replace("\n", "")
    riga = riga.replace("\t", ",")   #tabulazione
    studenti.append(riga)

f.close()


f = open('./studenti.sql','w')

query_tabella ="""
DROP TABLE IF IT EXISTS studenti;\n\n

CREATE TABLE studenti(\n
    id int primary key auto_increment,\n
    nome varchar(309 not null,\n
    cognome carchar(50) not null\n
    );\n\n


"""
f.write(query_tabella)

for s in studenti:
    s = str(s)
    pezzi = s.split(",")
    nome = pezzi[0]
    cognome = pezzi[1]
    f.write(f"insert input studenti (nome, cognome) value ('{nome}', '{cognome}');\n")
    # print(f"il nome dello studente è {nome} e il cognome è {congome}")
f.close()

