use its2026;

select * FROM Prodotti;  #mostra tabella con contenuti
select * FROM orders;
select * FROM customers;
select * FROM books;


SET SQL_SAFE_UPDATES = 0;    #disable safe mode
SET SQL_SAFE_UPDATES = 1;    #enable safe mode

# 1
insert into Prodotti (code, name, description, price, quantity)
values
('PRD00001', 'Pasta integrale', 'Pasta di grano duro 100% ingrale 500Kg', 1.49, 100),
('PRD00002', 'Olio extravergine', 'Olio extravergine d\oliva 750ml', 6.90, 50),
('PRD00003', 'Biscotti al cacao', 'Biscotti secchi con gocce di cioccolato', 2.75, 80),
('PRD00004', 'Passata di pomodoro', 'Passata di pomodoro biologica 700g', 1.29, 100),
('PRD00005', 'Riso basmati', 'Riso basmati confezione da 1kg', 3.10, 60);

# 2
insert into orders (order_date, total, shipping, shipping_address, customer_id)
values
('2025-06-01', 25.38, 'shipped', 'Via Roma 12 Milano', 101),
('2025-06-02', 47.20, 'delivered', 'Corso Italia 45 Torino', 102),
('2025-06-03', 15.90, 'to ship', 'Via Verdi 8 Firenze', 103),
('2025-06-03', 83.70, 'shipped', 'Piazza Garibaldi 20 Napoli', 104),
('2025-06-04', 9.99, 'delivered', 'Via Mazzini 5 Bologna', 101),
('2025-06-05', 29.50, 'to ship', 'Via Cavour 3 Venezia', 102),
('2025-06-06', 12.75, 'shipped', 'Via Amendola 14 Bari', 103),
('2025-06-07', 65.00, 'delivered', 'Corso Garibaldi 101 Genova', 104),
('2025-06-07', 19.80, 'to ship', 'Via Marconi 22 Palermo', 101),
('2025-06-08', 34.60, 'shipped', 'Via Leopardi 9 Verona', 102);

# 3
insert into customers (first_name, last_name, phone, email, address, city, province, region, postal_code, registration_date)
values
('Luca', 'Bianchi', 3201234567, 'luca.bianchi@email.it', 'Via Dante 10', 'Milano', 'MI', 'Lombardia', 20121, '2025-05-01'),
('Giulia', 'Rossi', 3479876543, 'giulia.rossi@email.it', 'Corso Venezia 22', 'Torino', 'TO', 'Piemonte', 10121, '2025-05-03'),
('Marco', 'Verdi', 3391122334, 'marco.verdi@email.it', 'Via Mazzini 18', 'Bologna', 'BO', 'Emilia-Romagna', 40121, '2025-05-05'),
('Elena', 'Neri', 3284455667, 'elena.neri@email.it', 'Piazza Duomo 1', 'Firenze', 'FI', 'Toscana', 50122, '2025-05-07'),
('Paolo', 'Ricci', 3339988776, 'paolo.ricci@email.it', 'Via Garibaldi 55', 'Napoli', 'NA', 'Campania', 80134, '2025-05-10'),
('Sara', 'Moretti', 3315566778, 'sara.moretti@email.it', 'Via Cavour 16', 'Venezia', 'VE', 'Veneto', 30121, '2025-05-12'),
('Davide', 'Ferrari', 3491122334, 'davide.ferrari@email.it', 'Via Manzoni 8', 'Genova', 'GE', 'Liguria', 16121, '2025-05-15'),
('Chiara', 'Gallo', 3278899001, 'chiara.gallo@email.it', 'Via Roma 77', 'Palermo', 'PA', 'Sicilia', 90133, '2025-05-18');

# 4
insert into America (state, capital_id, population)
values
('Brasile', 1, 216000000),
('Messico', 2, 129000000),
('Canada', 3, 39000000);

insert into Africa (state, capital_id, population)
values
('Nigeria', 4, 223000000),
('Egitto', 5, 111000000),
('Sudafrica', 6, 61000000);

insert into Asia (state, capital_id, population)
values
('Cina', 7, 1410000000),
('India', 8, 1400000000),
('Giappone', 9, 125000000);

# 5
insert into books (ISBN, title, price, price_VAT, pages, editor_id)
values
(9788801234567, 'La coscienza di Zeno', 15.00, 18.30, 250, 1),
(9788804567890, 'Il nome della rosa', 20.00, 24.40, 512, 2),
(9788867890123, 'I promessi sposi', 18.50, 22.57, 600, 1),
(9788876543210, 'Se questo è un uomo', 14.00, 17.08, 180, 3),
(9788898765432, 'Il Gattopardo', 22.00, 26.84, 350, 2),
(9788812345678, 'La storia', 19.00, 23.18, 430, 3),
(9788823456789, 'Cristo si è fermato a Eboli', 16.50, 20.13, 300, 1);

# 6
UPDATE Prodotti
SET description = 'Pasta di grano duro 100% integrale, 500g'
WHERE code = 'PRD00001';

# 7
UPDATE books
SET editor_id = 2
WHERE editor_id = 3;

# 8

UPDATE customers
SET 
	region = 'Lombardia',
    city = 'Milano',
    province = 'MI',
    postal_code = 20121
WHERE 
	region = 'Campania';

# 9
DELETE FROM books
WHERE ISBN = 9788812345678;

# 10
DELETE FROM customers
WHERE province = 'MI';

