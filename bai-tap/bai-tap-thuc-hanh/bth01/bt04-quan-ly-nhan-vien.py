# Quản lý nhân viên ở một học viện
# bằng kiểu từ điển (dictionary)

import json

# Câu a: Hiển thị danh sách nhân viên
def hien_thi_mot_nhan_vien(nhan_vien):
    for k, v in nhan_vien.items():
        if k == 'ma_nv':
            print("Mã nhân viên = %d" % v)
        elif k == 'ten_nv':
            print("Tên nhân viên = %s" % v)

def hien_thi_danh_sach_nhan_vien(danh_sach_nhan_vien):
    for nhan_vien in danh_sach_nhan_vien:
        hien_thi_mot_nhan_vien(nhan_vien)

def doc_danh_sach_nhan_vien():
    file = open("bt04-danh-sach-nhan-vien.json", "r", encoding="utf8")
    du_lieu = json.load(file)
    file.close()
    
    return du_lieu

danh_sach_nhan_vien = doc_danh_sach_nhan_vien()

print("\n==========================================\n")

print("Hiển thị danh sách nhân viên: ")
hien_thi_danh_sach_nhan_vien(danh_sach_nhan_vien)

# Câu b: Tìm kiếm nhân viên theo tên nhân viên
def tim_kiem_nhan_vien(danh_sach_nhan_vien, tu_khoa):
    danh_sach_ket_qua = []
    
    for nhan_vien in danh_sach_nhan_vien:
        if nhan_vien["ten_nv"].find(tu_khoa) >= 0:
            danh_sach_ket_qua.append(nhan_vien)
    
    return danh_sach_ket_qua

print("\n==========================================\n")

tu_khoa = input("Nhập tên nhân viên cần tìm: ")
danh_sach_ket_qua = tim_kiem_nhan_vien(danh_sach_nhan_vien, tu_khoa)
hien_thi_danh_sach_nhan_vien(danh_sach_ket_qua)

# Câu c: Xoá một nhân viên khỏi danh sách

# region - Cách 1
def xoa_nhan_vien(danh_sach_nhan_vien, id):
    for nhan_vien in danh_sach_nhan_vien:
        if nhan_vien["ma_nv"] == id:
            danh_sach_nhan_vien.remove(nhan_vien)
            return True
    return False
# endregion

# region - Cách 2
def xoa_nhan_vien_2(danh_sach_nhan_vien, id):
    for chi_so_nhan_vien_trong_mang, nhan_vien in enumerate(danh_sach_nhan_vien):
        if nhan_vien["ma_nv"] == id:
            del danh_sach_nhan_vien[chi_so_nhan_vien_trong_mang]
            return True
    return False
# endregion

print("\n==========================================\n")

if xoa_nhan_vien_2(danh_sach_nhan_vien, 2) == True:
    print("Danh sách nhân viên sau khi xoá: ")
    hien_thi_danh_sach_nhan_vien(danh_sach_nhan_vien)
else:
    print("Không có nhân viên cần xoá!")

# Câu d: Thêm một nhân viên mới vào danh sách
def them_nhan_vien_vao_danh_sach(danh_sach_nhan_vien, id, ten):
    nv = {
        "ma_nv": id,
        "ten_nv": ten,
    }
    
    danh_sach_nhan_vien.append(nv)
    ghi_danh_sach_nhan_vien(danh_sach_nhan_vien)

def ghi_danh_sach_nhan_vien(danh_sach_nhan_vien):
    file = open("bt04-danh-sach-nhan-vien.json", "w")
    json.dump(danh_sach_nhan_vien, file, ensure_ascii=False, encoding="utf8", indent=4)
    file.close()

print("\n==========================================\n")

id = int(input("Nhập mã nhân viên: "))
ten = input("Nhập tên nhân viên: ")
print()

them_nhan_vien_vao_danh_sach(danh_sach_nhan_vien, id, ten)
print("Danh sách nhân viên sau khi thêm mới: ")
hien_thi_danh_sach_nhan_vien(danh_sach_nhan_vien)

print("\n==========================================\n")
