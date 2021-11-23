n = int(input("Nhập n = "))

# Câu a
print(("*" * n + "\n")*n)

# Câu b
for i in range(1, n + 1):
    print("*" * i)

# Câu c
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)

# Câu d
for i in range(1, n + 1, 2):
    print(("*" * i).center(n))