from flask import jsonify
from app.models.products import Products
from flask_restful import Resource, reqparse

argumentos = reqparse.RequestParser()
argumentos.add_argument('name', type=str)
argumentos.add_argument('price', type=float)

#atualizar
argumentos_update = reqparse.RequestParser()
argumentos_update.add_argument('id', type=int)
argumentos_update.add_argument('name', type=str)
argumentos_update.add_argument('price', type=float)

#deletar
argumentos_deletar =  reqparse.RequestParser()
argumentos_deletar.add_argument('id', type=int)



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
        
class ProductUpdate(Resource):
    def put(self):
        try:
            datas = argumentos_update.parse_args()
            Products.update_products(self,datas['id'],datas['name'],datas['price'])
            return {"message": 'Products update sucessfully'},200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500


class ProductDelete(Resource):
    def delete(self):
        try:
            datas = argumentos_deletar.parse_args()
            Products.delete_products(self,datas['id'])
            return {"message": 'Products delete sucessfully'},200
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500