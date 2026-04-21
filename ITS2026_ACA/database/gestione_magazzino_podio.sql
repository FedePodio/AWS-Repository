# create database magazzino;
use magazzino;

-- Creazione Tabella Categorie
CREATE TABLE Categorie (
    id_categoria INT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL UNIQUE,
    descrizione TEXT
);

-- Creazione Tabella Fornitori
CREATE TABLE Fornitori (
    id_fornitore INT PRIMARY KEY,
    ragione_sociale VARCHAR(100) NOT NULL,
    citta VARCHAR(50),
    email VARCHAR(100) CHECK (email LIKE '%@%')
);

-- Creazione Tabella Prodotti
CREATE TABLE Prodotti (
    id_prodotto INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    prezzo_unitario DECIMAL(10, 2) NOT NULL CHECK (prezzo_unitario > 0),
    quantita_stock INT DEFAULT 0 CHECK (quantita_stock >= 0),
    id_categoria INT,
    id_fornitore INT,
    FOREIGN KEY (id_categoria) REFERENCES Categorie(id_categoria) ON DELETE SET NULL,
    FOREIGN KEY (id_fornitore) REFERENCES Fornitori(id_fornitore) ON DELETE CASCADE
);

INSERT INTO Categorie VALUES (1, 'Elettronica', 'Dispositivi hardware e gadget');
INSERT INTO Categorie VALUES (2, 'Arredamento', 'Mobili e ufficio');

INSERT INTO Fornitori VALUES (10, 'TechSpA', 'Milano', 'info@techspa.it');
INSERT INTO Fornitori VALUES (20, 'WoodDesign', 'Torino', 'sales@wood.com');

INSERT INTO Prodotti VALUES (101, 'Laptop Pro', 1200.00, 15, 1, 10);
INSERT INTO Prodotti VALUES (102, 'Mouse Wireless', 25.50, 50, 1, 10);
INSERT INTO Prodotti VALUES (103, 'Scrivania Legno', 150.00, 5, 2, 20);
INSERT INTO Prodotti VALUES (104, 'Sedia Ergonomica', 89.99, 0, 2, 20);
INSERT INTO Prodotti VALUES (105, 'Monitor 4K', 350.00, 8, 1, 10);

INSERT INTO Categorie (id_categoria, nome, descrizione) VALUES 
(3, 'Periferiche', 'Accessori per computer e input/output'),
(4, 'Illuminazione', 'Lampade e sistemi di luce per ufficio'),
(5, 'Cancelleria', 'Materiale di consumo per ufficio');

INSERT INTO Fornitori (id_fornitore, ragione_sociale, citta, email) VALUES 
(30, 'OfficeSupply Co.', 'Bologna', 'ordini@officesupply.it'),
(40, 'LuceDesign', 'Firenze', 'contact@lucedesign.com'),
(50, 'Global Logistics', 'Milano', 'logistics@global.com'),
(60, 'Cartiera Veneta', 'Padova', 'info@cartieraveneta.it');

INSERT INTO Prodotti (id_prodotto, nome, prezzo_unitario, quantita_stock, id_categoria, id_fornitore) VALUES 
-- Elettronica & Periferiche (TechSpA)
(106, 'Tastiera Meccanica', 75.00, 25, 3, 10),
(107, 'Cuffie Noise Cancelling', 199.00, 12, 1, 10),
(108, 'Webcam HD', 45.90, 0, 3, 10),

-- Arredamento & Illuminazione (WoodDesign e LuceDesign)
(109, 'Libreria Modulare', 210.00, 3, 2, 20),
(110, 'Lampada da Scrivania LED', 35.00, 40, 4, 40),
(111, 'Piantana Alogena', 120.00, 7, 4, 40),

-- Cancelleria (OfficeSupply e Cartiera Veneta)
(112, 'Risme Carta A4 (5pz)', 22.50, 100, 5, 60),
(113, 'Set Penne Gel', 12.00, 200, 5, 30),
(114, 'Organizer da tavolo', 18.50, 15, 5, 30),

-- Altri prodotti misti
(115, 'Hard Disk Esterno 2TB', 85.00, 30, 1, 50),
(116, 'Smartphone Entry Level', 150.00, 10, 1, 50),
(117, 'Cavo HDMI 2m', 9.99, 150, 3, 50);

# -----------------------------------------------------------------------------------

# 3. Esercitazione: 30 Query SQL
# Ecco una lista di query divise per livello di difficoltà crescente.

# Query di Base (Selezione e Filtro)
# Selezionare tutti i prodotti.
select * FROM prodotti;
# Selezionare nome e prezzo dei prodotti con prezzo superiore a 100€.
select nome, prezzo_unitario
FROM prodotti
WHERE
prezzo_unitario > 100.00;
# Elencare i fornitori di Milano.
select ragione_sociale
FROM fornitori
WHERE
citta = 'Milano';
# Trovare i prodotti con quantità in stock pari a 0 (esauriti).
select nome, quantita_stock
FROM prodotti
WHERE
quantita_stock = 0;
# Selezionare i prodotti che contengono la parola 'Laptop' nel nome.
select nome
FROM prodotti
WHERE
nome like '%Laptop%';
# Elencare le categorie in ordine alfabetico.
select nome
FROM categorie
ORDER BY nome;
# Trovare i prodotti con prezzo compreso tra 50€ e 500€.
select nome, prezzo_unitario
FROM prodotti
WHERE
prezzo_unitario BETWEEN 50 and 500;
# Mostrare i fornitori che non hanno un'email specificata (se fosse NULL).
select *
FROM fornitori
WHERE
email = NULL;
# Selezionare i primi 3 prodotti più costosi.
select nome, prezzo_unitario
FROM prodotti
ORDER BY prezzo_unitario DESC LIMIT 3;
# Calcolare il valore totale della merce (prezzo * quantità) per ogni prodotto.
select nome, (prezzo_unitario * quantita_stock) as valore_merce
FROM prodotti;

# -----------------------------------------------------------------------------------

# Query con Join (Relazioni tra tabelle)
# Visualizzare nome prodotto e nome della relativa categoria.
select prodotti.nome, prodotti.id_categoria
FROM prodotti JOIN categorie
on prodotti.id_categoria = categorie.id_categoria;
# Elencare i prodotti insieme alla ragione sociale del loro fornitore.
select prodotti.nome, fornitori.ragione_sociale
FROM prodotti JOIN fornitori
on prodotti.id_fornitore = fornitori.id_fornitore;
# Trovare tutti i prodotti della categoria 'Elettronica'.
select *
FROM prodotti
WHERE
id_categoria = 1;
# Mostrare i prodotti forniti da 'TechSpA'.
select *
FROM prodotti
WHERE
id_fornitore = 10;
# Elencare i nomi dei prodotti e le città dei loro fornitori.
select prodotti.nome, fornitori.citta
FROM prodotti JOIN fornitori
on prodotti.id_fornitore = fornitori.id_fornitore;
# Visualizzare i prodotti della categoria 'Arredamento' con stock > 0.
select prodotti.nome, categorie.id_categoria
FROM prodotti JOIN categorie
on prodotti.id_categoria = categorie.id_categoria
WHERE 
categorie.id_categoria = 2
AND prodotti.quantita_stock > 0;
# Mostrare le categorie che hanno almeno un prodotto fornito da un fornitore di 'Torino'.
select DISTINCT categorie.nome, prodotti.id_categoria, fornitori.citta
FROM prodotti 
JOIN categorie on categorie.id_categoria = prodotti.id_categoria
JOIN fornitori on prodotti.id_fornitore = fornitori.id_fornitore
WHERE 
fornitori.citta = 'Torino';
# Visualizzare i prodotti (nome) e il fornitore, ma solo se il prezzo è > 200€.
select prodotti.nome, fornitori.ragione_sociale
FROM prodotti
JOIN fornitori
WHERE
prezzo_unitario > 200.00;
# Lista completa: Nome Prodotto, Categoria, Fornitore.
select prodotti.nome, categorie.nome, fornitori.ragione_sociale
FROM prodotti
JOIN categorie on prodotti.id_categoria = categorie.id_categoria
JOIN fornitori on prodotti.id_fornitore = fornitori.id_fornitore;
# Trovare i nomi dei fornitori che forniscono prodotti nella categoria 'Elettronica'.
select DISTINCT fornitori.ragione_sociale, categorie.nome
FROM fornitori
JOIN prodotti on fornitori.id_fornitore = prodotti.id_fornitore
JOIN categorie on prodotti.id_categoria = categorie.id_categoria
WHERE
categorie.nome = 'Elettronica';
# Query di Aggregazione e Funzioni (Statistiche)
# Contare quanti prodotti ci sono in totale nel database.
select count(nome)
FROM prodotti;
# Calcolare il prezzo medio dei prodotti.
select AVG(prezzo_unitario)
FROM prodotti;
# Calcolare la somma totale degli articoli in magazzino.
select SUM(quantita_stock)
FROM prodotti;
# Trovare il prezzo massimo per ogni categoria.
select categorie.nome, max(prodotti.prezzo_unitario) as 'Prezzo massimo'
FROM prodotti
JOIN categorie on prodotti.id_categoria = categorie.id_categoria
GROUP BY categorie.nome;
# Contare quanti prodotti fornisce ogni fornitore.
select count(prodotti.quantita_stock) as 'Tot prodotti', fornitori.ragione_sociale
FROM prodotti
JOIN fornitori on prodotti.id_fornitore = fornitori.id_fornitore
GROUP BY fornitori.ragione_sociale;
# Calcolare il valore totale economico del magazzino intero.
select SUM(prezzo_unitario) * SUM(quantita_stock) as 'Valore totale'
FROM prodotti;
# Mostrare le categorie che hanno più di 2 prodotti.
select DISTINCT categorie.nome
FROM categorie
JOIN prodotti on categorie.id_categoria = prodotti.id_categoria
WHERE
prodotti.quantita_stock >= 2;
# Trovare il fornitore che ha il prodotto più economico.
select fornitori.ragione_sociale, prodotti.prezzo_unitario
FROM fornitori
JOIN prodotti on fornitori.id_fornitore = prodotti.id_fornitore
ORDER BY prodotti.prezzo_unitario ASC LIMIT 1;
# Calcolare la media dei prezzi dei prodotti per il fornitore 'TechSpA'.
select AVG(prodotti.prezzo_unitario) as 'Media Prezzi'
FROM prodotti
JOIN fornitori on prodotti.id_fornitore = fornitori.id_fornitore
WHERE
fornitori.ragione_sociale = 'TechSpA';
# Visualizzare le categorie e il numero di pezzi totali (somma stock) per ognuna.
select categorie.nome, SUM(prodotti.quantita_stock)
FROM prodotti
JOIN categorie on prodotti.id_categoria = categorie.id_categoria
GROUP BY categorie.nome;
# Esempio di risoluzione (Query 25 & 27)
# Se vuoi testare la logica più complessa:
#
# -- Query 25: Numero prodotti per fornitore
# SELECT F.ragione_sociale, COUNT(P.id_prodotto) AS Totale_Prodotti
# FROM Fornitori F
# LEFT JOIN Prodotti P ON F.id_fornitore = P.id_fornitore
# GROUP BY F.ragione_sociale;
#
# -- Query 27: Categorie con più di 2 prodotti
# SELECT C.nome, COUNT(P.id_prodotto)
# FROM Categorie C
# JOIN Prodotti P ON C.id_categoria = P.id_categoria
# GROUP BY C.nome
# HAVING COUNT(P.id_prodotto) > 2;

