use its2026;

describe Prodotti;   #mostra struttura tabella
describe customers;
drop table if exists orders;

# 1
create table Prodotti (
	code char(8) primary key,
	name varchar(30) not null,
    description TEXT,   #2
    price decimal(6,2) not null default(0.0),
    quantity int not null default 0,
    CONSTRAINT quantity_max CHECK (quantity <= 100)
);


#alter table Prodotti
#add column Descrizione varchar(255)

# 3
create table orders (
	id int primary key AUTO_INCREMENT,
	order_date DATE NOT NULL,
    total decimal(10,2) NOT NULL default 0,
    shipping ENUM('delivered', 'shipped', 'to ship') NOT NULL default 'to ship',
    shipping_address varchar(100) NOT NULL,
    customer_id int NOT NULL
);

# 4
create table clienti(
	id int primary key AUTO_INCREMENT,
    first_name varchar(30) NOT NULL,
    last_name varchar(30) NOT NULL,
    email varchar(100) NOT NULL UNIQUE,
    address varchar(100),
    city varchar(50),
    province char(2),
    region varchar(30),
    registration_date DATE NOT NULL
);

# 5
ALTER TABLE clienti
modify COLUMN last_name varchar(50) NOT NULL,
ADD COLUMN phone varchar(20) after last_name,
ADD COLUMN postal_code char(5) after region;

# 6
create table America(
	id int primary key AUTO_INCREMENT,
    state varchar(50) NOT NULL,
    capital_id TINYINT UNSIGNED,  #int varchar(255) NOT NULL (non ottimizzato)
    population BIGINT
);

create table Asia(
	id int primary key AUTO_INCREMENT,
    state varchar(50) NOT NULL,
    capital_id TINYINT UNSIGNED,
    population BIGINT
);

create table Africa(
	id int primary key AUTO_INCREMENT,
    state varchar(50) NOT NULL,
    capital_id TINYINT UNSIGNED,
    population BIGINT
);

# 7
create table Books(
	ISBN char(13) primary key UNIQUE,
    title varchar(100) NOT NULL,
    price decimal(6,2) NOT NULL default 0,
    price_VAT decimal(6,2) NOT NULL default 0,
    pages int default 0,
    editor_id int NOT NULL default 0
);

# 8
ALTER TABLE clienti
RENAME TO customers;

