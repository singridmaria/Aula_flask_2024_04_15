from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
api= Api(app)
#Configuração com banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'
db = SQLAlchemy(app) 
from app.models.products import Products
with app.app_context():
    db.create_all()

from app.view.reso_products import Index, ProductsCreate, ProductUpdate, ProductDelete
api.add_resource(Index,'/') #Como se fosse a rota, so que com a chamada da api
api.add_resource(ProductsCreate,'/criar')
api.add_resource(ProductUpdate,'/atualizar')
api.add_resource(ProductDelete,'/deletar')


'''@app.route("/")
def index():
    #return "<h1> Minha Aplicação em Flask</h1>"
    return render_template("index.html")'''