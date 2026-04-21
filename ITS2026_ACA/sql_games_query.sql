SELECT * FROM its2026.games;

select 
	`year` as "Anno pubblicazione",  # ` = alt 96
	count(nome) "Numero giochi"
from games
group by `year`
order by count(nome) DESC
limit 0, 10;

select 
	publisher as "Platform",  
    publisher as "Publisher",
	count(nome) "Numero giochi"
from games
group by platform, publisher
order by count(nome) DESC, platform
limit 100;
