# Tập tin init giống như phương thức khỏi tạo trong một lớp,
# khi mô-đun (gói) được nạp lên
# thì tập tin init sẽ được tự động chạy đầu tiên

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_babelex import Babel
from flask_login import LoginManager

# Tên mô-đun được đặt trong biến toàn cục "__name__",
# sẽ được tự động thay bằng tên package
app = Flask(__name__)
app.secret_key = 'UwU$40FD#IUO^OPXZC%NK^*23SN-_-M4MDFNB#SD62UvU3$GBXCVM%OwO'

app.config["SQLALCHEMY_DATABASE_URI"] =\
    "mysql+pymysql://root:1234@localhost/simplesaledb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_RECORD_QUERIES"] = True

csdl = SQLAlchemy(app=app)

login = LoginManager(app=app)

babel = Babel(app=app)
@babel.localeselector
def get_locale():
        # Put your logic here. Application can store locale in
        # user profile, cookie, session, etc.
        return 'vi'

