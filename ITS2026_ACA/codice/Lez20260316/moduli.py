import requests

# url = 'https://pokeapi.co/api/v2/pokemon/'

# risposta = requests.get(url + 'pichu')

# if risposta.status_code == 200:
#     pokemon = risposta.json()
    
#     for key, valore in pokemon.items():
#         print(f"la chiave {key}: il valore {valore} ")
#         print('--------------------------------------')

url = 'https://api.tvmaze.com/singlesearch/shows?q='

cerca = input("Scrivi il titolo di una serie tv: ")

risposta = requests.get(url + cerca)

if risposta.status_code == 200:
    show = risposta.json()
    
    titolo = show.get('name')
    rating = show.get('rating')
    image = show.get('image')

    print(titolo, rating['average'], image['medium'])