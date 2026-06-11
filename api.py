from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def conectar():
    return sqlite3.connect("usuarios.db")

# Cria a tabela automaticamente
conn = conectar()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    usuario TEXT NOT NULL,
    senha TEXT NOT NULL
)
""")

conn.commit()
conn.close()


@app.route("/")
def inicio():
    return "API funcionando!"


@app.route("/cadastro", methods=["POST"])
def cadastro():

    dados = request.json

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO usuarios
        (nome, email, usuario, senha)
        VALUES (?, ?, ?, ?)
        """,
        (
            dados["nome"],
            dados["email"],
            dados["usuario"],
            dados["senha"]
        )
    )

    conn.commit()
    conn.close()

    return jsonify({
        "mensagem": "Usuário cadastrado com sucesso!"
    })


@app.route("/login", methods=["POST"])
def login():

    dados = request.json

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM usuarios
        WHERE usuario = ? AND senha = ?
        """,
        (
            dados["usuario"],
            dados["senha"]
        )
    )

    usuario = cursor.fetchone()

    conn.close()

    if usuario:
        return jsonify({
            "sucesso": True,
            "mensagem": "Login realizado!"
        })

    return jsonify({
        "sucesso": False,
        "mensagem": "Usuário ou senha inválidos!"
    })


if __name__ == "__main__":
    app.run(debug=True)