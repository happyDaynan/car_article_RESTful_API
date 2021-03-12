from re import M
from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from server import db
from models import articleModels
import traceback

parser = reqparse.RequestParser()
parser.add_argument('article_id')
parser.add_argument('country')
parser.add_argument('brand')
parser.add_argument('href')
parser.add_argument('todbtime')




class Cars(Resource):
    
    # 取出所有文章資料
    def get(self):
        
        cars = articleModels.query.filter(articleModels.articletype.isnot(True)).all()
        
        return jsonify({"data": list(map(lambda car: car.serizlize(), cars))})

    # 新增文章data
    def post(self):
        arg = parser.parse_args()
        # print(arg['article_id'])

        response = {}
        status_code = 200

        try:
            new_data = articleModels(article_id= arg['article_id'], country = arg['country'], brand = arg['brand'], href = arg['href'], todbtime = arg['todbtime'])
            db.session.add(new_data)
            db.session.commit()
            response['msg'] = 'success'
        except:
            status_code = 400
            traceback.print_exc()
            response['msg'] = 'failed'
        return make_response(jsonify(response), status_code)
    
    # 刪除文章data
    def delete(self):
        arg = parser.parse_args()
        data = articleModels.query.filter(articleModels.article_id == arg['article_id']).first()
        
        response = {}
        try:
            db.session.delete(data)
            db.session.commit()
            response['msg'] = "delete success"
        except:
            response['msg'] = "delete failed"
        return make_response(jsonify(response))




class Car_country(Resource):
    # 依照國家取出data
    def get(self, country):
        car_country = articleModels.query.filter(articleModels.country == country and articleModels.articletype.isnot(True)).all()

        return jsonify({"data": list(map(lambda country: country.serizlize(), car_country))}) 
