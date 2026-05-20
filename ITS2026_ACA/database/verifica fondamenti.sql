#ESERCIZIO VERIFICA FINALE FONDAMENTI - FEDERICO PODIO

#PARTE A

CREATE DATABASE ai_lab_federico_podio;
use ai_lab_federico_podio;

CREATE TABLE Utente_Podio (
	idUtente INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    cognome VARCHAR(100) NOT NULL,
    dataNascita DATE NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    ruolo VARCHAR(50) NOT NULL
		CHECK (ruolo IN ('annotatore', 'admin', 'ricercatore')),
    dataRegistrazione DATE NOT NULL
);

CREATE TABLE Dataset_Podio (
	idDataset INT PRIMARY KEY AUTO_INCREMENT,
    nomeDataset VARCHAR(200) NOT NULL,
    descrizione TEXT,
    lingua VARCHAR(50) NOT NULL,
    dataCreazione DATE NOT NULL,
    idCreatore INT,
    FOREIGN KEY (idCreatore) REFERENCES Utente_Podio(idUtente) 
		ON DELETE RESTRICT 
        ON UPDATE CASCADE,
    licenza VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE Documento_Podio(
	idDocumento INT PRIMARY KEY AUTO_INCREMENT,
    titolo VARCHAR(300) NOT NULL,
    testo TEXT,
    dataInserimento DATE NOT NULL,
    idDataset INT,
    FOREIGN KEY (idDataset) REFERENCES Dataset_Podio(idDataset)
		ON DELETE CASCADE 
        ON UPDATE CASCADE,
    lunghezzaCaratteri INT NOT NULL
);

CREATE TABLE Annotazione_Podio (
	idAnnotazione INT PRIMARY KEY AUTO_INCREMENT,
    idDocumento INT,
    FOREIGN KEY (idDocumento) REFERENCES Documento_Podio(idDocumento)
		ON DELETE CASCADE,
	idUtente INT,
    FOREIGN KEY (idUtente) REFERENCES Utente_Podio(idUtente)
		ON DELETE RESTRICT,
    etichetta VARCHAR(50) NOT NULL 
		CHECK (etichetta IN ('positivo', 'negativo', 'neutro', 'spam')),
    confidenza DECIMAL(3,2) NOT NULL 
		CHECK (confidenza >= 0 and confidenza <= 1),
    dataAnnotazione DATE NOT NULL
);

# PARTE B

INSERT INTO Utente_Podio (nome, cognome, dataNascita, email, ruolo, dataRegistrazione)
VALUES
('Federico', 'Podio', '1999-03-21', 'fede.podio@gmail.com', 'admin', '2026-05-15'),
('Giancarlo', 'Silvano', '1999-08-15', 'carlogiansilva@gmail.com', 'annotatore', '2026-05-15'),
('Mauro', 'Bogliaccino', '1347-12-25', 'maboglia@gmail.com', 'ricercatore', '2026-05-15');

INSERT INTO Dataset_Podio (nomeDataset, descrizione, lingua, dataCreazione, licenza)
VALUES
('Odiare SQL','Uno studio su quanto il mondo sarebbe più bello senza database','italiano','2026-01-19','CC0-0001'),
('Amare Python(il serpente non il linguaggio)','Ricerca sui rettili','italiano','2022-05-23','CC-BY-0024');

INSERT INTO Documento_Podio (titolo, testo, dataInserimento, idDataset, lunghezzaCaratteri)
VALUES
('Ricerca TOP secret', 'TOP secret', '2026-05-01', 1, 1233),
('odio programmare', 'self explanatory', '2026-05-10', 1, 563),
('odio mettere dati', 'self explanatory', '2026-05-11', 1, 32),
('Come va prof?', 'io tutto bene', '2026-02-01', 1, 124),
('non so', 'ricerca di se stessi', '2026-03-17', 1, 764),
('ricetta carbonara', 'spiegazioni culinarie', '2025-05-02', 2, 657);

INSERT INTO Annotazione_Podio (idDocumento, idUtente, etichetta, confidenza, dataAnnotazione)
VALUES
(7, 1, 'positivo', 1.0, '2026-05-15'),
(8, 1, 'negativo', 0.3, '2026-05-15'),
(11, 1, 'positivo', 1.0, '2026-04-15'),
(9, 1, 'negativo', 0.2, '2026-05-08'),
(8, 1, 'negativo', 0.0, '2026-05-12'),
(11, 1, 'positivo', 0.9, '2026-05-15'),
(12, 1, 'positivo', 0.7, '2026-05-09'),
(12, 1, 'negativo', 0.3, '2026-02-15'),
(7, 1, 'negativo', 0.2, '2023-05-15'),
(10, 1, 'positivo', 1.0, '2026-03-10');

# PARTE C

#1
SELECT Documento_Podio.titolo, Dataset_Podio.nomeDataset, Dataset_Podio.lingua, Utente_Podio.nome, Utente_Podio.cognome
FROM Documento_Podio d
JOIN Dataset_Podio ds ON Documento_Podio.idDataset = ds.idDataset
JOIN Utente_Podio ON Dataset_Podio.idCreatore = Utente_Podio.idUtente;

#2


#3
SELECT ds.nomeDataset,
	COUNT(d.idDocumento) AS totaleDocumenti
FROM Dataset_Podio ds
JOIN Documento_Podio d ON ds.idDataset = d.idDataset
GROUP BY ds.idDataset, ds.nomeDataset;

#4

#5

#6 Trova i documenti che non hanno ancora nessuna annotazione associata.
SELECT Documento_Podio.titolo
FROM Documento_Podio
JOIN Annotazione_Podio ON Documento_Podio.idDocumento = Annotazione_Podio.idDocumento
WHERE idDocumento NOT IN ;
#7

#8


#9 
SELECT Documento_Podio.titolo, Annotazione_Podio.etichetta, Annotazione_Podio.confidenza
FROM Annotazione_Podio
JOIN Documento_Podio ON Documento_Podio.idDocumento = Annotazione_Podio.idDocumento
WHERE etichetta = 'positivo' OR etichetta = 'neutro';

#10
SELECT Dataset_Podio.nomeDataset, COUNT(Annotazione_Podio.idAnnotazione) AS totaleAnnotazioni
FROM Dataset_Podio 
JOIN Documento_podio d ON Dataset_Podio.idDataset = d.idDataset
JOIN Annotazione_Podio a ON d.idDocumento = a.idDocumento
ORDER BY totaleAnnotazioni DESC;

# PARTE D

#1 La PRIMARY KEY identifica in modo "unico" le righe di una tabella. La FOREIGN KEY fa riferimento a 2 tabelle
#2 l'indice serve a recuperare piu efficentemente i dati nelle tabelle, come l'indice in un libro. Può essere dannoso se viene usato in tabelle piccole o viene spammato troppo
#3 WHERE serve a filtrare prima dei gruppi tipo GROUP BY mentroe HAVING lo fa dopo
#4 La Subquery correlata è una query che dipende da valori esterni, quindi è aggregata ad una query principale per funzionare


