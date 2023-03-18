import sqlite3
from flask import Flask, render_template, request, redirect
from data.receber import Coordenadas

app = Flask(__name__)

valor_index = 0
valor_coordenada = [
    Coordenadas(id = None, x = None, y = None, z = None)
]

@app.route("/")
def index():
    db = sqlite3.connect("data/banco.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Coordenadas")
    valores = cursor.fetchall()
    db.close()

    for posicao in range(len(valores)):
        valores[posicao] = Coordenadas(
            id = valores[posicao][0],
            x = valores[posicao][1],
            y = valores[posicao][2],
            z = valores[posicao][3]
        )
    return render_template("index.html", valores=valores)

@app.route("/criar", methods=["POST"])
def numeros():
    valores = Coordenadas(
        id = None,
        x = request.form["x"],
        y = request.form["y"],
        z = request.form["z"]
    )
    db = sqlite3.connect("data/banco.db")
    cursor = db.cursor()
    cursor.execute("INSERT INTO Coordenadas (x, y, z) VALUES (?, ?, ?)", (valores.x, valores.y, valores.z))
    db.commit()
    db.close()
    valor_coordenada.append(valores)
    return redirect("/")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)