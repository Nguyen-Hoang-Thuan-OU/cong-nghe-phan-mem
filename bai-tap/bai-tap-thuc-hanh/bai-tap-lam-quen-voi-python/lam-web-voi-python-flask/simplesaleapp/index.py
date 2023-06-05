"""
Bước 01: cài flask thông qua terminal bằng câu lệnh "pip install flask"
            (chuyển terminal sang cmd nếu gặp lỗi)
Bước 02: tạo một gói (package)
Bước 03: import flask bằng câu lệnh "from flask import Flask"
Bước 04: tạo app từ flask (tạo đối tượng trong lập trình hướng đối tượng
            nhưng không cần từ khoá new)
Bước 05: Tạo các trang, chỉ định đường dẫn
            và nội dung của trang
Bước 05.01: bật tính năng debug ngay trên trình duyệt
                bằng "if __name__ == "__main__": app.run(debug = True)"
Bước 06: tạo folder "templates"
            để chứa các tập tin html hiển thị cho người dùng
Bước 07: import render_template
            để trả về template thay vì chuỗi
Bước 08: tạo folder static chứa các tài nguyên tĩnh
            (css, js, hình ảnh, âm thanh, video,...
            mỗi loại tài nguyên sẽ có một folder riêng)
"""
from flask import render_template, request, redirect
from simplesaleapp import app, login
import os
import utils
from flask_login import login_user
from simplesaleapp.admin import *


# Định nghĩa trang chủ
@app.route("/")
def home():
    danh_sach_nguoi_dung = [{
        "ten": "Nguyen Van A",
        "email": "a@gmail.com"
    }, {
        "ten": "Nguyen Van B",
        "email": "b@gmail.com"
    }, {
        "ten": "Nguyen Van C",
        "email": "c@gmail.com"
    }]

    tu_khoa = request.args.get("tukhoa")
    if tu_khoa:
        ket_qua = []

        for nguoi_dung in danh_sach_nguoi_dung:
            if nguoi_dung['ten'].lower().find(tu_khoa.lower()) >= 0:
                ket_qua.append(nguoi_dung)

        danh_sach_nguoi_dung = ket_qua

    return render_template('index.html',
                           danhsachnguoidung=danh_sach_nguoi_dung)


# # Định nghĩa trang thứ hai
# @app.route("/trang-hai")
# def trang_hai():
#     return "Trang thứ hai!"
#
#
# # ten_tham_so là tham số
# #   sẽ được tự động nhập vào hàm xin_chao
# # int: dùng để ràng buộc dữ liệu nhập vào
# #   phải ở dạng số nguyên
# @app.route("/xin-chao/<int:ten_tham_so>")
# def xin_chao(ten_tham_so):
#     return render_template('index.html',
#                            thong_diep = "Xin chào, %d!!!" % ten_tham_so)
#
#
# @app.route("/xin-chao")
# def xin_chao_2():
#     # Tất cả những cái truy vấn (query)
#     # đều nằm trong thuộc tính args
#     ten = request.args.get('ten', 'A')
#     ho = request.args.get('ho', 'Nguyen')
#
#     return render_template('index.html',
#                            thong_diep = "Xin chào, %s %s!!!" % (ten, ho))
#
#
# @app.route("/dang-nhap", methods=["POST"])
# def dang_nhap():
#     ten_tai_khoan = request.form['tentaikhoan']
#     mat_khau = request.form['matkhau']
#
#     if ten_tai_khoan == 'admin' and mat_khau == '123':
#         return 'Đăng nhập thành công!'
#
#     return 'Đăng nhập thất bại'
#
#
# @app.route("/tai-len", methods=["POST"])
# def tai_len():
#     file = request.files['hinhanh']
#     file.save(os.path.join(app.root_path, 'static/uploads/', file.filename))
#
#     return 'Tải lên thành công!'


@app.route("/dang-nhap-tu-cach-quan-tri-vien", methods=['GET', 'POST'])
def dang_nhap_tu_cach_quan_tri():
    if request.method == "POST":
        ten_dang_nhap = request.form.get('tendangnhap')
        mat_khau_dang_nhap = request.form.get('matkhaudangnhap')

        nguoi_dung = utils.kiem_tra_dang_nhap(ten_dang_nhap=ten_dang_nhap,
                                              mat_khau_dang_nhap=mat_khau_dang_nhap)
        if nguoi_dung:
            login_user(user=nguoi_dung)

    return redirect('/admin')


@login.user_loader
def tai_nguoi_dung(id_nguoi_dung):
    return utils.lay_nguoi_dung_theo_id(id_nguoi_dung=id_nguoi_dung)


# Kiểm tra nếu đang được thực thi.
# Dùng trong trường hợp run trực tiếp file
# bằng cách nhấn chuột phải vào file -> Run 'index',
# còn khi import sang nơi khác
# thì phần này sẽ không được thưc thi
if __name__ == "__main__":
    # Truyền biến debug vào hàm run() và bật lên
    # để khi xảy ra lỗi ra quá trình lập trình
    # thì lỗi sẽ được hiện trực tiếp lên trình duyệt
    app.run(host='127.0.0.1', port=6969)
    app.run(debug=True)
