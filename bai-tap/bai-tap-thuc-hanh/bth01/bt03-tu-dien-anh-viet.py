# Viết chương trình thực hiện việc xử lý từ điển Anh – Việt

# Câu a: Thêm một từ mới vào từ điển
def them_tu(tuDien, tu, yNghia):
    if tu not in tuDien:
        tuDien[tu] = yNghia

# Câu b: Hiển thị từ điển,
#           cho biết từ điển hiện tại cho bao nhiêu từ
def hien_thi_tu_dien(tuDien):
    for tu, yNghia in tuDien.items():
        print("%s = %s" % (tu, yNghia))

print("\n======================================\n")

tuDien = {
    "hello" : "xin chào",
    "table" : "cái bàn"
}
hien_thi_tu_dien(tuDien)

print("\n======================================\n")

them_tu(tuDien, "computer", "máy tính")
hien_thi_tu_dien(tuDien)

print("\n======================================\n")

# Câu c: Tìm kiếm từ tiếng Anh,
#           nếu tìm thấy thì hiển thị key và value.
#           Nếu không tìm thấy thì thông báo không tìm thấy
def tim_kiem_tu(tuDien, tu):
    if tu in tuDien:
        return tuDien[tu]
    return None
hien_thi_tu_dien(tuDien)

print("\n======================================\n")

tu = input("Nhập từ cần tìm: ")
ket_qua = tim_kiem_tu(tuDien, tu)

if ket_qua:
    print("Nghĩa của từ là:", ket_qua)
else:
    print("Không có từ cần tìm!")

print("\n======================================\n")

# Câu d: Xoá một từ trong từ điển dựa trên key cung cấp
def xoa_tu(tuDien, tu):
    if tu in tuDien:
        del tuDien[tu]

print("\n======================================\n")

xoa_tu(tuDien, "table")
hien_thi_tu_dien(tuDien)

print("\n======================================\n")