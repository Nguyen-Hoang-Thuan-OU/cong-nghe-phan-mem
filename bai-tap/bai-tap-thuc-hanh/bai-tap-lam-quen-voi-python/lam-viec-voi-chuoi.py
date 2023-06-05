print("\n============================================\n")

chuoi = "Python is simple, Python is great!!!"

print("""Chuỗi gốc: "Python is simple, Python is great!!!" \n """)

print("- Độ dài của chuỗi là: " + str(len(chuoi)) + "\n")

print("- Ký tự ở vị trí thứ 18 là: " + str(chuoi[18]) + "\n")

print("""- Chuỗi "simple" ở vị trí từ 10 đến 15: """ + str(chuoi[10:16]) + "\n")

print("""- Chuỗi "great" ở vị trí từ 28 đến 32 (cách 1): """ + str(chuoi[28:33]) + "\n")
print("""- Chuỗi "great" ở vị trí từ 28 đến 32 (cách 2): """ + str(chuoi[-8:-3]) + "\n")

print("""- In ra chuỗi "Python is great!!!": """ + str(chuoi[18:]) + "\n")

print("""- Vị trí đầu tiên tìm thấy chữ "is" là: """ + str(chuoi.find("is")) + "\n")

print("""- Số lần chuỗi "Python" xuất hiện: """ + str(chuoi.count("Python")) + "\n")

print("""- Thay thế chuỗi "Python" thành "Programming" và in chuỗi sau khi đã thay đổi ra: """ + str(chuoi.replace("Python", "Programming")) + "\n")

print("""- Cắt chuỗi ra làm đôi, thành mảng hai phần tử khi gặp dấu phẩy: """ + str(chuoi.split(", ")) + "\n")

print("============================================\n")

a, b, c = 10, 20, 50

chuoi = str.format("{SoThuNhat} + {SoThuhai} + {SoThuBa} = {KetQua}",\
                SoThuNhat = a, SoThuhai = b, SoThuBa = c, KetQua = a + b + c)
print("Kết quả của phép tính " + chuoi)

mang = [3, 5, 7]
chuoi = str.format("{0[0]} + {0[1]} + {0[2]} = {KetQua}", mang, KetQua = 3 + 5 + 7)
print("Kết quả của phép tính " + chuoi + "\n")

chuoi = str.format("{0:,.2f}", 98765432123456.789876543212)
print("Chuỗi định dạng theo tiền tệ: " + chuoi + "\n")

print("============================================\n")

'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
print("Hình vuông 5 x 5".center(26, "-"))
print((" *" * 5 + "\n") * 5)

print("============================================\n")