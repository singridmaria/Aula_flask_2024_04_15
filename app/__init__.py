#DEFINIR ROTAS

from flask import Flask, render_template #importar framework
from flask_sqlalchemy import SQLALchemy

app = Flask(__name__) #inicializar aplicação
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'#CAMINHO PARA CRIAR DATABASE
db = SQLALchemy(app)




'''@app.route("/") # @ é o decorador
def index():
    return render_template("index.html")'''