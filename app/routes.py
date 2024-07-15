from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    name = "Isaias"
    dados = {"profissao": "Musico", "instrumento": "Violino", "time": "Flamengo"}
    return render_template('index.html', name=name, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')
