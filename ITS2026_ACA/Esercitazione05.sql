use its2026;

# 1
select * FROM games;

# 2
select nome FROM games;

# 3
select nome
FROM games
WHERE 
year = 2000;   #2020 non ha giochi nella lista

# 4
select nome
FROM games
WHERE 
genere = "Action";

# 5
select nome
FROM games
WHERE 
publisher = "Nintendo";

# 6
select nome, publisher
FROM games
WHERE 
genere = 'Role-playing' and publisher = 'Square Enix';

# 7
select nome
FROM games
WHERE 
platform = "Playstation";

# 8
select nome
FROM games
WHERE
`year` < 2000;

# 9
select DISTINCT Genere 
FROM games;

# 10
select nome
FROM games
ORDER BY year DESC;

# 11
select nome
FROM games
WHERE
genere NOT IN ("Action", "Adventure");

# 12
select nome
FROM games
WHERE
`year` BETWEEN 2000 AND 2010;

# 13
select nome, publisher
FROM games
WHERE
`year` > 2015
ORDER BY publisher;

# 14
select count(*) as giochi_totale
FROM games;

# 15
select genere, COUNT(*) AS n_giochi_per_genere
FROM games
GROUP BY genere;

# 16
select nome
FROM games
WHERE
`year` = (SELECT MAX(year) 
FROM games);

# 17
select publisher, count(*) AS games_per_publisher
FROM games
GROUP BY publisher;

# 18
# select genere
# FROM games
# WHERE
# genere = (select MAX(genere) FROM games); # vehicle simulation?

select genere, count(*) AS genere_slop
FROM games
GROUP BY genere
ORDER BY genere_slop DESC LIMIT 1;  # action adv 40

# 19
SELECT `year`, count(*) AS games_per_year
FROM games
GROUP BY `year`;

# 20
select nome, platform, length(platform) - length(REPLACE(platform, ',', '')) + 1 AS multiplatform
FROM games
HAVING 
multiplatform > 1
ORDER BY multiplatform; 

# 21
select nome, `year`, count(DISTINCT publisher) AS different_publisher
FROM games
GROUP BY nome, `year`
HAVING 
different_publisher > 1;

# 22
select publisher, count(DISTINCT platform) AS multi_publisher
FROM games
GROUP BY publisher
HAVING
multi_publisher > 2;

# 23
select platform, year, count(*) AS console_war
FROM games
GROUP BY platform, year
HAVING 
count(*) > 5;

# 24
select nome, count(DISTINCT genere) AS genere_per_game
FROM games
GROUP BY nome
HAVING
genere_per_game > 1;  # non ce ne sono

# 25
select genere, publisher, count(*) AS mostgames_editor
FROM games
GROUP BY genere, publisher
HAVING 
count(*) = (
    select MAX(PubCount)
    FROM (
        select publisher, genere, count(*) AS PubCount
        FROM games
        GROUP BY genere, publisher
    ) AS SubQuery
    WHERE 
    SubQuery.genere = games.genere
);

# 26
select platform, nome, `year`
FROM games
WHERE
	(platform, `year`) IN (SELECT platform, MIN(`year`)
	FROM games
    GROUP BY platform
);

# 27
select nome, genere, publisher
FROM games
WHERE
nome IN(
	select nome
    FROM games
    GROUP BY nome
    HAVING 
    count(DISTINCT genere) > 1
    OR
    count(DISTINCT publisher) > 1      #solo 2 volte gow
);

# 28
select genere, count(*) AS totale_giochi, 
ROUND((count(*) * 100.0 / (select count(*) FROM games)), 2) AS percentage
FROM games
GROUP BY genere;

# 29
select publisher, count(*) AS rank_games, 
RANK() OVER (ORDER BY count(*) DESC) AS rank_games
FROM games
GROUP BY publisher;

# 30
select `year`, genere, COUNT(*) AS TOPgeneri,
RANK() OVER (partition by `year`, ORDER BY count(*) DESC) 
AS `RANK`
FROM games
GROUP BY `year`, genere
ORDER BY `year`, `RANK`;


