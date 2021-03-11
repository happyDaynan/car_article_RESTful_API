from flask_restful import Resource, reqparse
from flask import jsonify
from server import db
from models import articleModels

class Cars(Resource):
    
    # 取出所有文章資料
    def get(self):
        
        cars = articleModels.query.filter(articleModels.articletype.isnot(True)).all()
        
        return jsonify({"data": list(map(lambda car: car.serizlize(), cars))})

class Car_country(Resource):
    # 依照國家取出data
    def get(self, country):
        car_country = articleModels.query.filter(articleModels.country == country and articleModels.articletype.isnot(True)).all()

        return jsonify({"data": list(map(lambda country: country.serizlize(), car_country))}) 
