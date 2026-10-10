# Bước 1: Nhập tên khách hàng chưa được chuẩn hóa
ten_khach_hang = " nGuYen VAn A "

# Bước 2: Xóa khoảng trắng thừa ở đầu và cuối chuỗi
ten_khach_hang = ten_khach_hang.strip()

# Bước 3: Chuẩn hóa chữ hoa và chữ thường
ten_khach_hang = ten_khach_hang.title()

# Bước 4: In tên khách hàng sau khi chuẩn hóa
print("Tên khách hàng:", ten_khach_hang)
