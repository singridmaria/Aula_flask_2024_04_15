from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'
db = SQLAlchemy(app) 
api= Api(app)
from app.models.products import Products
with app.app_context():
    db.create_all()

from app.view.reso_products import Index, ProductsCreate
api.add_resource(Index,'/')
api.add_resource(ProductsCreate,'/criar')


'''@app.route("/")
def index():
    #return "<h1> Minha Aplicação em Flask</h1>"
    return render_template("index.html")'''