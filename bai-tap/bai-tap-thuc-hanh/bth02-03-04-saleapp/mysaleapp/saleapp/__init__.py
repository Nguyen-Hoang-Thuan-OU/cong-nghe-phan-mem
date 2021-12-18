from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'mysql+pymysql://root:1234@localhost/saledb?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key =\
    'UwU$40FD#IUO^OPXZC%NK^*23SN-_-M4MDFNB#SD62UvU3$GBXCVM%OwO'

db = SQLAlchemy(app=app)

admin = Admin(app=app,
              name='TRANG BÁN HÀNG TRỰC TUYẾN',
              template_mode='bootstrap4')
