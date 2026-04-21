#create database libreria;
use libreria;

create table editori(
	editore_id int primary key auto_increment,
    nome varchar(100),
    contatto varchar(100)
);

create table libri(
	libro_id int primary key auto_increment,
    titolo varchar(100),
    prezzo decimal(6,2),
    pagine int,
    editore_id int
);
    
    create table autori(
	autore_id int primary key auto_increment,
    nome varchar(30),
    cognome varchar(50),
    nazionalità char(2)
);
    
create table autori_libri(
	autore_id int,
    libro_id int,
    primary key(autore_id, libro_id) #cosi si puo avere piu volte lo stesso libro o autore ma non entrambi contemp
);    

insert into editori
select * FROM  editore;

insert into libri
select * FROM libro;

insert into autori
select * FROM autore;

insert into autori_libri
select * FROM autore_libro;


select * 
FROM libri as l, editori e
WHERE l.editore_id = e.editore_id;

select count(*) from editori;

select *
FROM libri l
right join editori e on l.editore_id = e.editore_id;

select 
l.titolo,
concat(a.nome, ' ', a.cognome) as autore,
e.nome as editore
FROM libri l
left join editori e on l.editore_id = e.editore_id
left join autori_libri al on l.libro_id = al.libro_id
left join autori a on a.autore_id = al.autore_id;

truncate autori_libri;

insert into autori_libri
select autore_id, libro_id FROM autore_libro;

-- ---------------------------------------------------------
use its2026;

select
genere, 
count(nome) as totale
FROM games
group by totale DESC
;





