print("\nGIẢI VÀ BIỆN LUẬN PHƯƠNG TRÌNH BẬC MỘT: ax + b = 0 \n")

while True:
    # Chứa các câu lệnh nghi ngờ rằng
    # trong quá trình thực thi có thể phát sinh vấn đề
    # (ví dụ: nhập ký tự, nhập chuỗi)
    try:
        a = float(input("Nhập a: " ))
        b = float(input("Nhập b: " ))

    # Thực thi những câu lệnh bên trong
    # khi xảy ra vấn đề
    except ValueError as ngoaiLe:
        # str() dùng để ép đối tượng ngoaiLe thành chuỗi
        print("\nĐã xảy ra lỗi: " + str(ngoaiLe))
        print("Vui lòng nhập lại!")

    # Đặc trung của python,
    # được gọi khi không hề có một lỗi nào xảy ra
    else:
        if a == 0:
            if b == 0:
                print("Phương trình vô số nghiệm! \n")
            else:
                print("Phương trình vô nghiệm! \n")
        else:
            x = -b / a
        print("\nNghiệm x = ", x)
        
        # Dùng để dừng vòng lặp và kết thúc
        # sau khi đã thực hiện tính toán xong
        break

    # Luôn được thực thi
    # bất chấp có xảy ra vấn đề hay không
    finally:
        print("\nHoàn tất \n")
