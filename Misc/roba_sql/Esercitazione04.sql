use its2026;

select * from alimenti;

# 1-2
select * 
FROM alimenti
where
categoria = 'CARNE';

# 3
select count(*)  #seleziona tutto
AS numero_alimenti
FROM alimenti;

# 4
select *
FROM alimenti
where
proteine > 10;

# 5
select *
FROM alimenti
order by energia
DESC LIMIT 5;  #limite alla fine

# 6
select AVG(proteine)  #AVG(categoria) calcola la media aritmetica di una colonna numerica
AS media
FROM alimenti
WHERE
categoria = 'carne';

# 7
select *
FROM alimenti
WHERE
carboidrati = 0;

# 8
select *
FROM alimenti
order by lipidi
DESC LIMIT 1;

# 9
select count(*)
AS numero_alimenti
FROM alimenti
group by categoria;

# 10
select *
FROM alimenti
WHERE
carboidrati BETWEEN 10 AND 30;

# ----------------------------------------------------

# 1
select COUNT(*) 
AS alimenti_totale 
FROM alimenti;

# 2
select AVG(proteine)
AS media_proteine
FROM
alimenti;

# 3
select MAX(energia)
AS energia_max,
MIN(energia)
AS energia_min
FROM alimenti;

# 4
select SUM(lipidi)
AS lipidi_tot
FROM alimenti;

# 5
select count(*)
AS numero_alimennti
FROM alimenti
GROUP BY categoria;

# 6
select AVG(carboidrati)
AS media_carboidrati
FROM alimenti
GROUP BY categoria;

# 7
select AVG(energia)
AS media_energia
FROM alimenti
GROUP BY categoria
ORDER BY media_energia
DESC LIMIT 1;

# 8
select proteine
FROM alimenti
WHERE
proteine = (SELECT MAX(proteine) FROM alimenti);

# 9
select SUM(energia)
AS energia_tot
FROM alimenti
GROUP BY categoria;

# 10
select count(*)
AS alimenti_proteati
FROM alimenti
WHERE
proteine > 10;