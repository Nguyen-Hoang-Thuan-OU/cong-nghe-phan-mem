# Tập tin init giống như phương thức khỏi tạo trong một lớp,
# khi mô-đun (gói) được nạp lên
# thì tập tin init sẽ được tự động chạy đầu tiên

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Tên mô-đun được đặt trong biến toàn cục "__name__",
# sẽ được tự động thay bằng tên package
app = Flask (__name__)

app.config["SQLALCHEMY_DATABASE_URI"] =\
    "mysql+pymysql://root:1234@localhost/saledb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

csdl = SQLAlchemy(app=app)
