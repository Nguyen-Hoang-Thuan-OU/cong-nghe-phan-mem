"""
- List[] - danh sách:
    + Là một collection có thứ tự, có thể thay đổi.
    + Cho phép chứa dữ liệu trùng lặp.

- Tuple() - bộ:
    + Là một collection có thứ tự, không thể thay đổi.
    + Cho phép chứa dữ liệu trùng lặp.

- Set{} - tập hợp:
    + Là một collection không có thứ tự, không có chỉ mục.
    + Không cho phép chứa dữ liệu trùng lặp.

- Dictionary{key:value} - từ điển:
    + Là một collection không có thứ tự, có thể thay đổi và lập chỉ mục.
    + Không cho phép chứa dữ liệu trùng lặp.
"""
# region - Thao tác với danh sách

a = [3, 7, 4, 2, 6, 1, 8, 5, 9]

print("\nMảng a = [3, 7, 4, 2, 6, 1, 8, 5, 9]\n")

# Thao tác giống với thao tác bên chuỗi
print("- Độ dài của mảng là: " + str(len(a)) + "\n")

print("- Phần tử thứ hai trong mảng là: " + str(a[1]) + "\n")

print("- Đoạn phần tử từ thứ hai đến thứ bảy: " + str(a[2:8]) + "\n")

a = a + [14, 18, 20, 13, 12, 16, 15, 19, 17, 10, 11]
print("- Nối mảng a với mảng [14, 18, 20, 13, 12, 16, 15, 19, 17, 10, 11]: " + str(a) + "\n")

a = a * 2
print("- Gấp đôi số lượng phần tử của mảng a: " + str(a) + "\n")

print("==========================================\n")

# Thêm phần tử vào cuối, vị trí bất kỳ
a.append(999)
print("- Thêm phần tử vào cuối mảng a: " + str(a) + "\n")

a.insert(2, 999)
print("- Thêm phần tử vào vị trí thứ hai: " + str(a) + "\n")

print("==========================================\n")

# Sắp xếp
a.sort()
print("- Sắp xếp tăng dần: " + str(a) + "\n")

a.reverse()
print("- Sắp xếp giảm dần: " + str(a) + "\n")

print("==========================================\n")

# Tìm kiếm
print("- Vị trí xuất hiện của phần tử 15 trong mảng: " + str(a.index(15)) + "\n")

print("==========================================\n")

# Xoá
a.remove(999)
print("- Xoá phần tử 999: " + str(a) + "\n")

a.pop(0)
print("- Xoá phần tử ở vị trí thứ không: " + str(a) + "\n")

del a[1]
print("- Xoá phần tử ở vị trí thứ nhất: " + str(a) + "\n")

print("==========================================\n")

# Duyệt
print("---Cách 1---" + "\n")
for phanTu in a:
    print(phanTu)
    
print("\n" + "---Cách 2---" + "\n")
for i in range(len(a)):
    print(a[i] + 1)
print()
    
# endregion

# region - Thao tác với bộ

# Tuple (bộ) cũng giống danh sách,
# nhưng không được phép thay đổi giá trị các phần tử

print("==========================================\n")

a = (5, 6, 7)
len(a)
print("Số phần tử trong mảng: " + str(a) + "\n")
# a[1] = 2 # lỗi 'tuple' object does not support item assignment

# endregion

# region - Thao tác với tập hợp

# Tập hợp không quan tâm thứ tự phần tử,
# hai phần tử bất kỳ của tập hợp không được phép trùng nhau

print("==========================================\n")

# Cách khai báo một tập hợp rỗng
a = {}
a = set()

a = {2, 3, 4, 2, 5, 6, 3}
print("Tập hợp a = {2, 3, 4, 2, 5, 6, 3} có phần tử trùng")
print("Sau khi đã chuyển thành tập hợp: " + str(a) + "\n")

print("==========================================\n")

# Ép chuỗi thành tập hợp
s = "aaaabbbbbccccxxxxyyyyzzzz"
print("""Chuỗi s = "aaaabbbbbccccxxxxyyyyzzzz" """)

print("- Chuyển chuỗi thành tập hợp và loại bỏ phần từ bị trùng: " + str(set(s)) + "\n")
print("- Chuyển tập hợp về lại chuỗi sau khi đã loại bỏ phần từ bị trùng: " + str("".join(set(s)) + "\n"))

print("==========================================\n")

a = {2, 3, 5, 6}
b = {3, 4, 5, 7}

print("Tập hợp a = {2, 3, 5, 6}")
print("Tập hợp b = {3, 4, 5, 7}")
print()

# Trừ hai tập hợp, lấy những phần từ thuộc a mà không thuộc b
print("Tập hợp a - b = " + str(a - b) + "\n")

# Hợp hai tập hợp, lấy những phần từ thuộc vào một trong hai tập hợp
print("Tập hợp a | b = " + str(a | b) + "\n")

# Giao hai tập hợp, lấy những phần từ thuộc cả hai tập hợp
print("Tập hợp a & b = " + str(a & b) + "\n")

# Khác biệt hai tập hợp, lấy những phần từ thuộc chỉ thuộc một trong hai tập hợp
print("Tập hợp a ^ b = " + str(a ^ b) + "\n")

# endregion

# region - Thao tác với từ điểm

# Cấu trúc từ điển chính là mảng băm,
# Key là giá trị duy nhất

print("==========================================\n")

sinhVien = {
    "ten" : "Nguyen Van A",
    "quen quan" : "TP.HCM"
}

print('''
        sinhVien = {
            "ten" : "Nguyen Van A",
            "que quan" : "TP.HCM"
        }
      ''' + "\n")

print("- Số phần tử trong từ điển: " + str(len(sinhVien)) + "\n")

print("""- Truy xuất giá trị của "que quan": """ + str(sinhVien["quen quan"]) + "\n")

# Thêm
sinhVien["gioi tinh"] = "nam"
print("Thêm giới tính cho sinh viên: " + str(sinhVien) + "\n")

# Xoá
del sinhVien["quen quan"]
print("Xoá quê quán của sinh viên: " + str(sinhVien) + "\n")

# Lấy danh sách key và value
print("Danh sách key: " + str(sinhVien.keys()) + "\n")
print("Danh sách value: " + str(sinhVien.values()) + "\n")

# Duyệt phần tử
for k, v in sinhVien.items():
    print(k, ':', v)

# endregion