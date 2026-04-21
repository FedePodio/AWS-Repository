from controller.disco_controller import DiscoController
from flask import Flask, jsonify, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)

ctrl = DiscoController()

@app.get("/")
def homepage():
    return "home page"

@app.get("/artisti")
def artisti():
    artisti = ctrl.getArtists()
    return render_template("artisti.html", artists = artisti)

@app.get("/api/artisti")
@cross_origin()
def artisti_json():
    
    return ctrl.getArtistiJson()

ctrl.getArtists()

app.run(debug=True, port=5001)











# from model.artist import Artist
# from model.album import Album
#from service.disco_service import DiscoService

# service = DiscoService()

# artisti = service.getAllArtists()

# for artista in artisti:
#     temp = Artist(artisti.get("ArtistId", 0), artisti.get("Name", 'Artista sconosciuto'))
#     print(temp.toHtmlTable() + '\n')

# artisti = [{
#     "ArtistId": 1,
#     "Name": "AC/DC"
# },
# {
#     "ArtistId": 3,
#     "Name": "Aerosmith"
# }
# ]

# a1 = Artist(artisti[0].get("ArtistId", 0), artisti[0].get("Name", 'Artista sconosciuto'))
# a2 = Artist(artisti[1].get("ArtistId", 0), artisti[1].get("Name", 'Artista sconosciuto'))


#print(isinstance(a1, Album)) #false
#print(isinstance(a1, Artist)) #true

# print(a1.nome)
# print(Artist.casa_discografica)

# print(a1.casa_discografica)
# print(Artist.casa_discografica)

