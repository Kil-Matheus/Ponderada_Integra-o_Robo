import sqlite3 # Importa o módulo sqlite3
from flask import Flask, render_template, request, redirect # Importa o módulo Flask, junto com as bibliotecas utilizadas
from data.receber import Coordenadas # Importa a classe Coordenadas do arquivo receber.py

# Cria a aplicação Flask
app = Flask(__name__)

# Variáveis globais que vão receber os dados para o banco de dados para ser exibido na página
valor_coordenada = [
    Coordenadas(x = None, y = None, z = None)
]

# Cria a rota inicial da aplicação, que vai renderizar o template index.html e exibir os dados do banco de dados
@app.route("/")
def index():
    db = sqlite3.connect("data/banco.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Coordenadas")
    valores = cursor.fetchall()
    db.close()

#Loop que vai percorrer a lista de valores e vai atribuir os valores de cada posição para a classe Coordenadas. O For vai pegar a o 'valores[posição]' e vai receber a 'Coordenadas()' e dentro da classe vai receber os valores de cada posição segundo as suas posições dentro da array.
    for posicao in range(len(valores)):
        valores[posicao] = Coordenadas(
            x = valores[posicao][0],
            y = valores[posicao][1],
            z = valores[posicao][2]
        )
    return render_template("index.html", valores=valores)

# Cria a rota que vai receber os dados do formulário e vai inserir no banco de dados
@app.route("/criar", methods=["GET", "POST"])
def numeros():
    if request.method == "POST":
        valores = Coordenadas(
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

#Ele está pegando a utima posição da array (linha) do meu banco de dados e retornando para a aplicação.
    db = sqlite3.connect("data/banco.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Coordenadas ORDER BY rowid DESC LIMIT 1")
    valores = cursor.fetchall()
    db.close()

    return valores

@app.route("/deletar", methods=["POST"])
def deletar():
    db = sqlite3.connect("data/banco.db")
    cursor = db.cursor()
    cursor.execute("DELETE * FROM Coordenadas")
    db.commit()
    db.close()
    return redirect("/")

# Cria a rota que vai receber os dados do formulário e vai atualizar no banco de dados
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)