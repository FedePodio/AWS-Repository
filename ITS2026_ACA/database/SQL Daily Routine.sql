create database EsercizioSQL;

create user esercizio_user@localhost identified by 'password123';

grant all on EsercizioSQL.* to esercizio_user@localhost;

use EsercizioSQL;

# 2---------------------------------------------------------------------------
create table Clienti(
id_cliente INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(50) NOT NULL,
email VARCHAR(100) UNIQUE NOT NULL
);

create table Prodotti(
id_prodotto INT PRIMARY KEY AUTO_INCREMENT,
nome VARCHAR(50) NOT NULL,
prezzo DECIMAL(10, 2) NOT NULL
);

create table Ordini(
id_ordine INT PRIMARY KEY AUTO_INCREMENT,
id_cliente INT NOT NULL,
id_prodotto INT NOT NULL,
quantita INT NOT NULL CHECK (quantita > 0),
data_ordine datetime DEFAULT current_timestamp,
FOREIGN KEY (id_cliente) references Clienti(id_cliente),
FOREIGN KEY (id_prodotto) references Prodotti(id_prodotto)
);

# 3---------------------------------------------------------------------------
INSERT INTO Clienti(nome, email)
VALUES
('Gian Marco Silvano', 'gianmarco.silvano@edu-its.it'),
('Alessandro Verduna', 'alessandro.verduna@edu-its.it'),
('Cristian Torres', 'cristian.torres@edu-its.it'),
('Janice Brun', 'janice.brun@edu-its.it'),
('Sara Ingrassia', 'sara.ingrassia@edu-its.it');

INSERT INTO Prodotti(nome, prezzo)
VALUES
('Scivolizia', 250),
('Laptop', 1200.99),
('Kebab', 4.50);

INSERT INTO Ordini(id_cliente, id_prodotto, quantita)
VALUES
(1, 1, 35),
(1, 2, 1),
(4, 3, 2),
(5, 1, 3);

# 4---------------------------------------------------------------------------
SELECT * 
FROM Ordini;

SELECT id_cliente, COUNT(id_ordine) AS numero_ordini
FROM ordini
GROUP BY id_cliente;

SELECT Clienti.nome, COUNT(Ordini.id_cliente) as orders
FROM Clienti
INNER JOIN Ordini ON Clienti.id_cliente = Ordini.id_cliente
GROUP BY Ordini.id_cliente
HAVING COUNT(Ordini.id_cliente) > 1;

SELECT Clienti.nome, SUM(Prodotti.prezzo * Ordini.quantita) AS TotaleSpeso
FROM Clienti
JOIN Ordini ON Clienti.id_cliente = Ordini.id_cliente
JOIN Prodotti ON Ordini.id_prodotto = Prodotti.id_prodotto
GROUP BY Clienti.id_cliente;

# 5---------------------------------------------------------------------------
SET SQL_SAFE_UPDATES = 0;
SET SQL_SAFE_UPDATES = 1;

UPDATE Prodotti SET prezzo = 1300.00 
WHERE nome = 'Laptop';

# punto 16: ogni ordine associato al cliente verrà eliminato

DELETE FROM Ordini WHERE id_ordine = 1;
# 6---------------------------------------------------------------------------
INSERT INTO Ordini(id_cliente, id_prodotto, quantita)
VALUES
(5, 1, -2);
# da errore in quanto abbiamo usato "quantita INT NOT NULL CHECK (quantita > 0)"

# 7---------------------------------------------------------------------------
TRUNCATE TABLE Ordini;

DROP TABLE Ordini;
DROP TABLE Clienti;
DROP TABLE Prodotti;

DROP USER 'esercizio_user'@'localhost';
DROP DATABASE EsercizioSQL;