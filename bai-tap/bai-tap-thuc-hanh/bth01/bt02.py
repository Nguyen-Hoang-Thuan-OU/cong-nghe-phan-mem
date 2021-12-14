# region - Cách 1
def nhap_danh_sach(n):
    a = []
    for i in range(n):
        x = int(input("a[%d] = " % i))
        a.append(x)
    return a
# endregion

# region - Cách 2
def nhap_danh_sach_2(n):
    return [int(input("a[%d] = " % i)) for i in range(n)]
# endregion

print("\n=====================================\n")

n = int(input("Nhập n = "))
a = nhap_danh_sach_2(n)
print("Mảng a =", a)

print("\n=====================================\n")

# Câu a: tìm số dương lớn nhất và số âm bé nhất

# region - Cách 1
duong = []
for x in a:
    if x > 0:
        duong.append(x)
# endregion

# region - Cách 2
duong = [x for x in  a if x > 0]
# endregion

if len(duong) > 0:
    print("Số dương lớn nhất = ", max(duong))
else:
    print("*")

print("\n=====================================\n")

# Câu b: hiển thị tần số xuất hiện
#           của từng phần tử trong danh sách
for x in set(a):
    print("Số %d xuất hiện %d lần" % (x, a.count(x)))

print("\n=====================================\n")

# Câu c: hiển thị các phần tử trong danh sách
#           xuất hiện k lần, k nhập từ bàn phím
k = int(input("Nhập số cần đếm tần suất xuất hiện = "))
kq = []
for x in set(a):
    t = a.count(x)
    if t == k:
        kq.append(x)
    
print("Các phần tử xuất hiện %d lần là %s" % (k, str(kq)))

print("\n=====================================\n")

# Câu d: ắp xếp danh sách giảm dần
a.sort(reverse=True)
print("Mảng được sắp xếp theo tứ tự giảm dần: ", a, "\n")