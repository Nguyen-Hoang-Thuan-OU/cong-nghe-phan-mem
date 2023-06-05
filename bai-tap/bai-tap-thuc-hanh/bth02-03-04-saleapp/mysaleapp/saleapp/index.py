import math
import utils
import cloudinary.uploader
from flask import render_template, request,\
    redirect, url_for, session, jsonify
from saleapp import app, login
from saleapp.admin import *
from flask_login import login_user, logout_user


# Trang chủ
@app.route("/")
def home():
    cate_id = request.args.get("category_id")
    kw = request.args.get("keyword")
    page = request.args.get('page', 1)
    products = utils.load_products(cate_id=cate_id,
                                   kw=kw,
                                   page=int(page))
    counter = utils.count_products()

    return render_template('index.html',
                           products=products,
                           pages=math.ceil(counter / app.config['PAGE_SIZE']))


# Trang đăng ký tài khoản
@app.route("/register", methods=['GET', 'POST'])
def user_register():
    err_msg = ""
    if request.method.__eq__('POST'):
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        email = request.form.get('email')
        avatar_path = None

        try:
            if password.strip().__eq__(confirm.strip()):
                avatar = request.files.get('avatar')
                if avatar:
                    res = cloudinary.uploader.upload(avatar)
                    avatar_path = res['secure_url']

                utils.add_user(name=name,
                               username=username,
                               password=password,
                               email=email,
                               avatar=avatar_path)
                return redirect(url_for('user_signin'))
            else:
                err_msg = "Mật khẩu nhập lại không khớp!"
        except Exception as ex:
            err_msg = "Hệ thống đang xảy ra lỗi: " + str(ex)

    return render_template('register.html',
                           err_msg=err_msg)


# Trang đăng nhập tài khoản
@app.route("/user-login", methods=['GET', 'POST'])
def user_signin():
    err_msg = ""
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')

        user = utils.check_login(username=username,
                                 password=password)
        if user:
            login_user(user=user)
            return redirect(url_for('home'))
        else:
            err_msg = "Tên đăng nhập hoặc mật khẩu không chính xác!"

    return render_template('login.html',
                           err_msg=err_msg)


@app.route('/user-logout')
def user_signout():
    logout_user()
    return redirect(url_for('user_signin'))


@login.user_loader
def user_load(user_id):
    return utils.get_user_by_id(user_id=user_id)


# Luôn hiển thị các danh mục sản phẩm ở các trang
@app.context_processor
def common_respone():
    return {
        'categories': utils.load_categories()
    }


# Trang danh sách sản phẩm
@app.route("/products")
def product_list():
    cate_id = request.args.get("category_id")
    kw = request.args.get("keyword")
    from_price = request.args.get("from_price")
    to_price = request.args.get("to_price")

    products = utils.load_products(cate_id=cate_id,
                                   kw=kw,
                                   from_price=from_price,
                                   to_price=to_price)

    return render_template("products.html",
                           products=products)


# Trang chi tiết sản phẩm
@app.route("/products/<int:product_id>")
def product_detail(product_id):
    product = utils.get_product_by_id(product_id)

    return render_template("product_detail.html",
                           product=product)


# Xử lý gọi dữ liệu JavaScript của giỏ hàng bằng API
@app.route('/api/add-cart', methods=['POST'])
def add_to_cart():
    data = request.json
    id = str(data.get('id'))
    name = data.get('name')
    price = data.get('price')

    cart = session.get('cart')
    if not cart:
        cart = {}

    if id in cart:
        cart[id]['quantity'] = cart[id]['quantity'] + 1
    else:
        cart[id] = {
            'id': id,
            'name': name,
            'price': price,
            'quantity': 1
        }

    session['cart'] = cart

    return jsonify(utils.count_cart(cart))


if __name__ == '__main__':
    # Đổi port thành 9696 thay vì mặc định là 5000
    app.run(host='127.0.0.1', port=9696)

    # Bật tính năng debug trên trình duyệt
    app.run(debug=True)
