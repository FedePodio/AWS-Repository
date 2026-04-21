from magazzino_service import MagazzinoService
# pip install flask
from flask import Flask, jsonify

app = Flask(__name__)

service = MagazzinoService()
@app.get('/api/prodotti')
def prodotti():
    return jsonify(service.getALLProducts())  #aggiungi /api/prodotti al link


app.run(debug=True)
