# Dùng từ khoá def để định nghĩa hàm,
# không có kiểu dữ liệu trả về

# Hàm tính tổng và a, b, c là danh sách tham số,
# truyền vào giá trị mặc định = 0
# tham số *args (argument) đại diện cho danh sách đối số,
# kw = keyword, kwargs cho phép truyền đối số dạng keyword
def tong(a = 0, b = 0, c = 0, *args, **kwargs):
    print("\n" + "Hàm tính tổng".center(20, "-"))
    tong = a + b + c
    
    for phanTu in args:
        tong = tong + phanTu
        
    if kwargs.get("so_nguyen_cua_toi"):
        tong = tong + kwargs["so_nguyen_cua_toi"]
        
    return tong

t = tong(a = 4, b = 5, c = 6, so_nguyen_cua_toi = 9999)
print("Tổng = " + str(t) + "\n")

# Biểu thức lambda: hàm nặc danh (anonymous), không cần tên,
# chỉ cần danh sách tham số và kết quả trả về
tongLambda = lambda x, y, z: x * y * z
print("Tổng được tính bằng lambda: " + str(tongLambda(77, 88, 99)))