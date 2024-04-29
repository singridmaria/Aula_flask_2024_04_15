from flask import jsonify
from app.models.products import Products
from flask_restful import Resource, reqparse

argumentos = reqparse.RequestParser()
argumentos.add_argument('name', type=str)
argumentos.add_argument('price', type=float)
class Index(Resource):
    def get(self):
        return jsonify("Welcome Aplication Flask")

class ProductsCreate(Resource): 
    def post(self):
        try:
            datas = argumentos.parse_args()
            print(datas)
            Products.save_products(self,datas['name'], datas['price'])
            return {"message": 'Products create sucessfully'},200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500