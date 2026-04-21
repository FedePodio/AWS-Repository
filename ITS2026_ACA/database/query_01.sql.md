


mysql> create database ITS2026;
Query OK, 1 row affected (0.00 sec)

mysql> create user ITS2026@localhost identified by 'ITS2026';
Query OK, 0 rows affected (0.01 sec)

mysql> grant all on ITS2026.* to ITS2026@localhost;
Query OK, 0 rows affected (0.01 sec)

--------------------------------------------------






PS C:\Users\federico.podio\Desktop\AWSREPO> mysql -u ITS2026 -p 
mysql : Termine 'mysql' non riconosciuto come nome di cmdlet, funzione, programma eseguibile o file script. Controllare 
l'ortografia del nome o verificare che il percorso sia incluso e corretto, quindi riprovare.
In riga:1 car:1
+ mysql -u ITS2026 -p
+ ~~~~~
    + CategoryInfo          : ObjectNotFound: (mysql:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
 
PS C:\Users\federico.podio\Desktop\AWSREPO> 
 *  History restored 

PS C:\Users\federico.podio\Desktop\AWSREPO> mysql -u ITS2026 -p
Enter password: *******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 22
Server version: 8.4.8 MySQL Community Server - GPL

Copyright (c) 2000, 2026, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| its2026            |
| performance_schema |
+--------------------+
3 rows in set (0.00 sec)

mysql> use its2026;
Database changed
mysql> show tables;
Empty set (0.00 sec)

mysql> create table canzoni(id int, titolo varchar(40), cantante varchart(60));
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'varchart(60))' at line 1
mysql> create table canzoni(id int, titolo varchar(40) , cantante varchart(60));
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'varchart(60))' at line 1
mysql> create table canzoni(id int, titolo varchar(40), cantante varchar(60));  
Query OK, 0 rows affected (0.05 sec)

mysql> show tables;
+-------------------+
| Tables_in_its2026 |
+-------------------+
| canzoni           |
+-------------------+
1 row in set (0.00 sec)

mysql> desc canzoni;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| id       | int         | YES  |     | NULL    |       |
| titolo   | varchar(40) | YES  |     | NULL    |       |
| cantante | varchar(60) | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
3 rows in set (0.02 sec)

mysql> insert into canzoni values (1, '', '');
Query OK, 1 row affected (0.02 sec)

mysql> drop table canzoni;
Query OK, 0 rows affected (0.10 sec)

mysql> show tables; 
Empty set (0.00 sec)

mysql> create table canzoni(id int, titolo varchar(40) NOT NULL, cantante varchart(60));
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'varchart(60))' at line 1
mysql> create table canzoni(id int, titolo varchar(40) NOT NULL, cantante varchar(60)); 
Query OK, 0 rows affected (0.10 sec)

mysql> insert into canzoni values (1, '','');
Query OK, 1 row affected (0.02 sec)

mysql> drop table canzoni;
Query OK, 0 rows affected (0.13 sec)

mysql> create table canzoni(id int, titolo varchar(40) NOT NULL DEFAULT 'titolo sconosciuto', cantante varchar(60) NOT NUL
L);
Query OK, 0 rows affected (0.13 sec)

mysql> insert into canzoni values (1, NULL, NULL);                                                                        
ERROR 1048 (23000): Column 'titolo' cannot be null
mysql> insert into canzoni values (1, '', NULL);  
ERROR 1048 (23000): Column 'cantante' cannot be null
mysql> insert into canzoni values (1, '', '');
Query OK, 1 row affected (0.05 sec)

mysql> select * from canzoni
    -> s
    -> select * from canzoni;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'select * from canzoni' at line 3
mysql> select * from canzoni;
+------+--------+----------+
| id   | titolo | cantante |
+------+--------+----------+
|    1 |        |          |
+------+--------+----------+
1 row in set (0.00 sec)

mysql> select * from canzoni;
+------+--------+----------+
| id   | titolo | cantante |
+------+--------+----------+
|    1 |        |          |
+------+--------+----------+
1 row in set (0.00 sec)

mysql> update canzoni set titolo = 'Sinceramente', cantante = 'Annalisa' where id = 1;
Query OK, 1 row affected (0.05 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> delete from canzoni where id = 1;
Query OK, 1 row affected (0.04 sec)

mysql> select * from canzoni;
Empty set (0.00 sec)

mysql> 