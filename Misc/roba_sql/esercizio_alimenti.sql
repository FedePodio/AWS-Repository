use its2026;

# 3
select distinct categoria
from alimenti a;

-- operatore IN

select * from alimenti a
where categoria not in ('CARNE', 'PESCE');

# 4
create table dolci as
select * from alimenti
where categoria = 'DOLCI';

create table dolci_esagerati as
select * from alimenti
where categoria = 'DOLCI'
order by energia desc
limit 10;


# 1
select * 
FROM alimenti a
where 
-- a.proteine >= 10 and a.proteine <= 20;
a.proteine between 10 and 20
and
a.lipidi between 10 and 20
order by a.energia desc;


# 2
select '90% di grissini' as prodotto,
(a.proteine * 0.9) as proteine_grissini,
(a.carboidrati * 0.9) as carboidrati_grissini,
(a.lipidi * 0.9) as lipidi_grissini
from alimenti a
where
prodotto like '%grissini%';

# 5
select * from dolci d
union
select * from dolci_esagerati de;

select a.categoria, count(a.prodotto) as 'Num.Prodotti x Cat',
AVG(a.energia) as 'Valore energetico medio'
from alimenti a
group by categoria
order by AVG(a.energia);


