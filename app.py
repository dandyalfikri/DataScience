from flask import Flask, request, jsonify
from random_forest import *
import os

app = Flask(__name__)

@app.route('/afi', methods=['POST'])
def index():
    umur = request.json['umur']
    rencana_pembelian = request.json['rencana_pembelian']
    luas_tanah = request.json['luas_tanah']
    luas_bangunan = request.json['luas_bangunan']
    jumlah_lantai = request.json['jumlah_lantai']
    metode_pembayaran = request.json['metode_pembayaran']
    budget=request.json['budget']
    list_data = []
    dataFinal = []
    list_data.append(umur)
    list_data.append(rencana_pembelian)
    list_data.append(luas_tanah)
    list_data.append(luas_bangunan)
    list_data.append(jumlah_lantai)
    list_data.append(metode_pembayaran)
    list_data.append(budget)
    dataFinal.append(list_data)
    print(dataFinal)

    result = fitting(dataFinal)

    print(result)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)