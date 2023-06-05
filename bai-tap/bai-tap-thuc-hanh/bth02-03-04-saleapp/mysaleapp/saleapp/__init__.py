from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager
import cloudinary

app = Flask(__name__)
app.secret_key = \
    'UwU$40FD#IUO^OPXZC%NK^*23SN-_-MFB#SD62UvU3$GBXCVM%OwO'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+pymysql://root:1234@localhost/saledb?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['PAGE_SIZE'] = 8

db = SQLAlchemy(app=app)

admin = Admin(app=app,
              name='TRANG BÁN HÀNG TRỰC TUYẾN',
              template_mode='bootstrap4')


login = LoginManager(app=app)


# Cấu hình cloudinary
cloudinary.config(
    cloud_name='',
    api_key='',
    api_secret='')
