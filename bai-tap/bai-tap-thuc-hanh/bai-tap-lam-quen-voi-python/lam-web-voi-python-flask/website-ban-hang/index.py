'''
Bước 01: cài flask thông qua terminal bằng câu lệnh "pip install flask"
            (chuyển terminal sang cmd nếu gặp lỗi)
Bước 02: tạo một gói (package)
            (tập tin init giống như phương thức khỏi tạo trong một lớp,
            khi mô-đun (gói) được nạp lên thì tập tin init sẽ được tự động chạy đầu tiên)
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
'''

from flask import Flask, render_template

# Tên mô-đun được đặt trong biến toàn cục "__name__",
# sẽ được tự động thay bằng tên package
app = Flask (__name__)

# Định nghĩa trang chủ
@app.route("/")
def home():
    return render_template('index.html')

# Định nghĩa trang thứ hai
@app.route("/trang-hai")
def tranghai():
    return "Trang thứ hai!"

# Kiểm tra nếu đang được thực thi.
# Dùng trong trường hợp run trực tiếp file
# bằng cách nhấn chuột phải vào file -> Run 'index',
# còn khi import sang nơi khác
# thì phần này sẽ không được thưc thi
if __name__ == "__main__":
    # Truyền biến debug vào hàm run() và bật lên
    # để khi xảy ra lỗi ra quá trình lập trình
    # thì lỗi sẽ được hiện trực tiếp lên trình duyệt
    app.run(debug = True)
