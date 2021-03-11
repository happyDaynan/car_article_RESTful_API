from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 建立連線資訊
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:2020aiot@127.0.0.1:3306/car'

db = SQLAlchemy(app)