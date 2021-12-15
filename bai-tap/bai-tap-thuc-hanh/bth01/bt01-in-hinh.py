# Cho người dùng nhập số nguyên n và xuất các hình

n = int(input("Nhập n = "))
print()

# Câu a
print(("*" * n + "\n")*n)

# Câu b
for i in range(1, n + 1):
    print("*" * i)
print()

# Câu c
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
print()

# Câu d
for i in range(1, n + 1, 2):
    print(("*" * i).center(n))
print()