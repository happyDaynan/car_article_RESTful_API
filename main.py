from flask import Flask
from flask_restful import Api
from server import app
from car_article.article_href import Cars, Car_country

# create api
api = Api(app)

# car
api.add_resource(Cars, '/cars')
api.add_resource(Car_country, '/car/<country>')

if __name__ == '__main__':
    app.debug = True
    app.run()