from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    name = "Anne"
    dados = {"profissao": "Professora", "Turno": "Manhã", "time": "São Paulo"}
    return render_template('index.html', name=name, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')
